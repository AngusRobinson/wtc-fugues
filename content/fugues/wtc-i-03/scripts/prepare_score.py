"""Parse the credited three-spine score, preserving closing chords and ties."""
import json,re,argparse
from pathlib import Path
import xml.etree.ElementTree as ET
import verovio
p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);root=p.parse_args().root
raw=(root/'sources/bwv848.krn').read_text()
events=[];clocks=[0.,0.,0.];voice_map=[2,1,0];bar=0
for line_no,line in enumerate(raw.splitlines(),1):
 if line.startswith('*'):
  fs=line.split('\t')
  if '*^' in fs:
   nc=[];nv=[]
   for j,f in enumerate(fs):
    nc.extend([clocks[j]]*(2 if f=='*^' else 1));nv.extend([voice_map[j]]*(2 if f=='*^' else 1))
   clocks,voice_map=nc,nv
  elif '*v' in fs:
   nc=[];nv=[];j=0
   while j<len(fs):
    nc.append(clocks[j]);nv.append(voice_map[j])
    if fs[j]=='*v':
     old=j;j+=1
     while j<len(fs) and fs[j]=='*v':
      assert clocks[j]==clocks[old] and voice_map[j]==voice_map[old];j+=1
    else:j+=1
   clocks,voice_map=nc,nv
  continue
 if not line or line[0] in '! ':continue
 if line.startswith('='):
  match=re.match(r'=(\d+)',line)
  if match:
   bar=int(match[1]);assert clocks==[(bar-1)*4]*len(clocks),(bar,clocks)
  continue
 tokens=line.split('\t');assert len(tokens)==len(clocks)
 for spine,token in enumerate(tokens):
  if token=='.':continue
  dm=re.search(r'(\d+)(\.*)',token);assert dm
  duration=4/int(dm[1])*sum(.5**j for j in range(len(dm[2])+1))
  start=clocks[spine];clocks[spine]+=duration
  if 'r' in token:continue
  chord=token.split()
  for j,part in enumerate(chord,1):
   pm=re.search(r'([a-g]+|[A-G]+)([#n-]*)',part);assert pm
   letters,acc=pm.groups();letter=letters[0].lower()
   octave=3+len(letters) if letters.islower() else 4-len(letters)
   pitch=12*(octave+1)+{'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}[letter]+acc.count('#')-acc.count('-')
   events.append(dict(id=f'note-L{line_no}F{spine+1}'+(f'S{j}' if len(chord)>1 else ''),voice=voice_map[spine],start=start,duration=duration,pitch=pitch,bar=bar,name=letter.upper()+'♭'*acc.count('-')+'♯'*acc.count('#')+str(octave),diatonic=octave*7+'cdefgab'.index(letter),token=part,tied=('_' in part or ']' in part)))
assert clocks==[220]*3 and bar==55
# Key by voice and pitch: chords make an adjacency-only tie merge incorrect.
audio=[];last={}
for e in sorted(events,key=lambda e:(e['start'],e['voice'],e['pitch'])):
 key=(e['voice'],e['pitch'])
 if e['tied']:
  previous=last[key];assert previous['start']+previous['duration']==e['start']
  previous['duration']+=e['duration']
 else:
  a={k:e[k] for k in ['id','voice','start','duration','pitch']};audio.append(a);last[key]=a
# The source keeps S/A on one stave; the analytical score separates all three.
tk=verovio.toolkit();tk.setOptions({'inputFrom':'humdrum','xmlIdSeed':848})
assert tk.loadData(raw.replace('*staff2\t*staff1\t*staff1','*staff3\t*staff2\t*staff1'))
mei=tk.getMEI();tree=ET.fromstring(mei);ns={'m':'http://www.music-encoding.org/ns/mei'};ID='{http://www.w3.org/XML/1998/namespace}id'
assert {n.get(ID) for n in tree.findall('.//m:note',ns)}=={e['id'] for e in events}
# Verify written pitch against MEI's independent key/accidental spelling.
by_id={e['id']:e for e in events};codes={'ff':-2,'f':-1,'n':0,'s':1,'ss':2,'x':2}
carried={}
for measure in tree.findall('.//m:measure',ns):
 for staff in measure.findall('m:staff',ns):
  state={}
  for note in staff.findall('.//m:note',ns):
   e=by_id[note.get(ID)];pname=note.get('pname');octave=int(note.get('oct'));key=(pname,octave)
   acc=note.find('m:accid',ns);target=acc if acc is not None else note
   sign=target.get('accid') or target.get('accid.ges')
   alt=codes[sign] if sign else (carried[(staff.get('n'),key)] if e['tied'] else state.get(key,1))
   expected=12*(octave+1)+{'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}[pname]+alt
   assert expected==e['pitch'],(e,expected)
   state[key]=alt;carried[(staff.get('n'),key)]=alt
   # Explicit gestural accidentals avoid Verovio 6.3 MIDI ignoring key signatures.
   target.set('accid.ges',{-2:'ff',-1:'f',0:'n',1:'s',2:'ss'}[alt])
ET.register_namespace('','http://www.music-encoding.org/ns/mei')
mei=ET.tostring(tree,encoding='unicode')
tk=verovio.toolkit();tk.setOptions({'inputFrom':'mei'});assert tk.loadData(mei)
tk.renderToMIDI()
for e in events:
 values=tk.getMIDIValuesForElement(e['id']);assert values['pitch']==e['pitch'],(e,values)
 assert abs(values['time']-e['start']*60000/106)<2,(e,values)
(root/'sources/bwv848-three-voices.mei').write_text(mei)
(root/'data/score.json').write_text(json.dumps({'events':events,'audio':audio,'duration':220},ensure_ascii=False,separators=(',',':')))
print(f'{len(events)} written notes, {len(audio)} sounding events, 55 bars; every pitch/onset agrees with Verovio.')
