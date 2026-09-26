"""Parse the credited three-voice score, preserving closing chords and ties."""
import json,re,argparse
from pathlib import Path
import xml.etree.ElementTree as ET
import verovio
p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);root=p.parse_args().root
raw=(root/'sources/bwv860.krn').read_text()
events=[];clocks=[0.,0.,0.];parts=[2,1,0];bar=0
for line_no,line in enumerate(raw.splitlines(),1):
 if not line or line[0] in '! ':continue
 if line.startswith('*'):
  if '*^' in line:
   cc=[];pp=[]
   for i,t in enumerate(line.split('\t')):
    for _ in range(2 if t=='*^' else 1):cc.append(clocks[i]);pp.append(parts[i])
   clocks,parts=cc,pp
  continue
 if line.startswith('='):
  match=re.match(r'=(\d+)',line)
  if match:
   bar=int(match[1]);assert clocks==[(bar-1)*3]*len(clocks),(bar,clocks)
  continue
 tokens=line.split('\t');assert len(tokens)==len(clocks)
 for spine,token in enumerate(tokens):
  if token=='.':continue
  dm=re.search(r'(\d+)(\.*)',token);assert dm
  duration=(8 if dm[1]=='0' else 4/int(dm[1]))*sum(.5**j for j in range(len(dm[2])+1))
  start=clocks[spine];clocks[spine]+=duration
  if 'r' in token:continue
  chord=token.split()
  for j,part in enumerate(chord,1):
   pm=re.search(r'([a-g]+|[A-G]+)([#n-]*)',part);assert pm
   letters,acc=pm.groups();letter=letters[0].lower()
   octave=3+len(letters) if letters.islower() else 4-len(letters)
   pitch=12*(octave+1)+{'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}[letter]+acc.count('#')-acc.count('-')
   events.append(dict(id=f'note-L{line_no}F{spine+1}'+(f'S{j}' if len(chord)>1 else ''),voice=parts[spine],start=start,duration=duration,pitch=pitch,bar=bar,name=letter.upper()+'♭'*acc.count('-')+'♯'*acc.count('#')+str(octave),diatonic=octave*7+'cdefgab'.index(letter),token=part,tied=('_' in part or ']' in part)))
assert clocks==[258]*5 and bar==86
# Key by voice and pitch: chords make an adjacency-only tie merge incorrect.
audio=[];last={}
for e in sorted(events,key=lambda e:(e['start'],e['voice'],e['pitch'])):
 key=(e['voice'],e['pitch'])
 if e['tied']:
  previous=last[key];assert previous['start']+previous['duration']==e['start']
  previous['duration']+=e['duration']
 else:
  a={k:e[k] for k in ['id','voice','start','duration','pitch']};audio.append(a);last[key]=a
# Split the three voices onto separate staves; closing added voices retain their source staff.
(root/'data/score.json').write_text(json.dumps({'events':events,'audio':audio,'duration':258},ensure_ascii=False,separators=(',',':')))
print('Converting Humdrum',flush=True)
tk=verovio.toolkit();tk.setOptions({'inputFrom':'humdrum','xmlIdSeed':860})
assert tk.loadData(raw.replace('*staff2\t*staff1\t*staff1','*staff3\t*staff2\t*staff1'))
print('Loaded Humdrum',flush=True)
mei=tk.getMEI();tree=ET.fromstring(mei);ns={'m':'http://www.music-encoding.org/ns/mei'};ID='{http://www.w3.org/XML/1998/namespace}id'
assert {n.get(ID) for n in tree.findall('.//m:note',ns)}=={e['id'] for e in events}
# Verify written pitch against MEI's independent key/accidental spelling.
by_id={e['id']:e for e in events};codes={'ff':-2,'f':-1,'n':0,'s':1,'ss':2,'x':2}
sustained={}
for measure in tree.findall('.//m:measure',ns):
 for staff in measure.findall('m:staff',ns):
  state={}
  for note in staff.findall('.//m:note',ns):
   e=by_id[note.get(ID)];pname=note.get('pname');octave=int(note.get('oct'));key=(pname,octave)
   acc=note.find('m:accid',ns);target=acc if acc is not None else note
   sign=target.get('accid') or target.get('accid.ges')
   alt=codes[sign] if sign else (sustained[(e['voice'],key)] if e['tied'] else state.get(key,1 if pname in 'f' else 0))
   sustained[(e['voice'],key)]=alt
   expected=12*(octave+1)+{'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}[pname]+alt
   assert expected==e['pitch'],(e,expected)
   state[key]=alt
   # Explicit gestural accidentals avoid Verovio 6.3 MIDI ignoring key signatures.
   target.set('accid.ges',{-2:'ff',-1:'f',0:'n',1:'s',2:'ss'}[alt])
ET.register_namespace('','http://www.music-encoding.org/ns/mei')
mei=ET.tostring(tree,encoding='unicode')
tk=verovio.toolkit();tk.setOptions({'inputFrom':'mei'});assert tk.loadData(mei)
tk.renderToMIDI()
for e in events:
 values=tk.getMIDIValuesForElement(e['id']);assert values['pitch']==e['pitch'],(e,values)
 assert abs(values['time']-e['start']*60000/102)<2,(e,values)
(root/'sources/bwv860-three-voices.mei').write_text(mei)
(root/'data/score.json').write_text(json.dumps({'events':events,'audio':audio,'duration':258},ensure_ascii=False,separators=(',',':')))
print(f'{len(events)} written notes, {len(audio)} sounding events, 86 bars; every pitch/onset agrees with Verovio.')
