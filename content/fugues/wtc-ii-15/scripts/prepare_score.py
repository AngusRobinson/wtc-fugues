"""Parse the credited 3-spine score, preserving closing chords and ties."""
import json,re,argparse
from pathlib import Path
import xml.etree.ElementTree as ET
import verovio
p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);root=p.parse_args().root
raw=(root/'sources/bwv884.krn').read_text()
# Both notes of the bar-30 alto chord tie into bar 31 (Kroll, BGA XIV, p. 152).
# The retained source has a tie continuation without a beginning on C, and no tie end on A.
for before,after in [('8cc_ [8aJ','[8cc [8aJ'),('8cc] 8aL','8cc] 8a]L')]:
 assert raw.count(before)==1,before
 raw=raw.replace(before,after)

events=[];clocks=[0.0, 0.0, 0.0];voice_map=[2, 1, 0];included=[True, True, True];bar=0
for line_no,line in enumerate(raw.splitlines(),1):
 if line.startswith('*'):
  fs=line.split('\t')
  if '*^' in fs:
   nc=[];nv=[];ni=[]
   for j,f in enumerate(fs):
    nc.extend([clocks[j]]*(2 if f=='*^' else 1));nv.extend([voice_map[j]]*(2 if f=='*^' else 1));ni.extend([included[j]]*(2 if f=='*^' else 1))
   clocks,voice_map,included=nc,nv,ni
  elif '*v' in fs:
   nc=[];nv=[];ni=[];j=0
   while j<len(fs):
    nc.append(clocks[j]);nv.append(voice_map[j]);ni.append(included[j])
    if fs[j]=='*v':
     old=j;j+=1
     while j<len(fs) and fs[j]=='*v':
      assert clocks[j]==clocks[old] and voice_map[j]==voice_map[old];j+=1
    else:j+=1
   clocks,voice_map,included=nc,nv,ni
  if '*S/ossia' in fs:
   included=[old and f!='*S/ossia' for old,f in zip(included,fs)]
  continue
 if not line or line[0] in '! ':continue
 if line.startswith('='):
  match=re.match(r'=(\d+)',line)
  if match:
   bar=int(match[1]);assert clocks==[(bar-1)*1.5]*len(clocks),(bar,clocks)
  continue
 tokens=line.split('\t');assert len(tokens)==len(clocks)
 for spine,token in enumerate(tokens):
  if token=='.':continue
  dm=re.search(r'(\d+)(\.*)',token);assert dm
  duration=4/int(dm[1])*sum(.5**j for j in range(len(dm[2])+1))
  start=clocks[spine];clocks[spine]+=duration
  if 'r' in token or not included[spine]:continue
  chord=token.split()
  for j,part in enumerate(chord,1):
   pm=re.search(r'([a-g]+|[A-G]+)([#n-]*)',part);assert pm
   letters,acc=pm.groups();letter=letters[0].lower()
   octave=3+len(letters) if letters.islower() else 4-len(letters)
   pitch=12*(octave+1)+{'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}[letter]+acc.count('#')-acc.count('-')
   events.append(dict(id=f'note-L{line_no}F{spine+1}'+(f'S{j}' if len(chord)>1 else ''),voice=voice_map[spine],start=start,duration=duration,pitch=pitch,bar=bar,name=letter.upper()+'♭'*acc.count('-')+'♯'*acc.count('#')+str(octave),diatonic=octave*7+'cdefgab'.index(letter),token=part,tied=('_' in part or ']' in part)))
assert len(set(clocks))==1 and bar==72;duration=clocks[0]
original_ids={e['id']for e in events}
# The three-octave run is one soprano line (Keller p.162; Prout p.75).
# The keyboard transcription changes spines when it changes staff.
for e in events:
 if 92.25<=e['start']<96 and e['duration']==.125:e['voice']=0
# Realise the final appoggiatura as a quaver, following Keller and Kroll p.153.
closing=next(e for e in events if e['bar']==72 and e['voice']==0)
assert closing['pitch']==59 and closing['start']==106.5 and closing['duration']==1.5
closing['start']=107;closing['duration']=1
app=dict(id='note-appoggiatura-72',voice=0,start=106.5,duration=.5,pitch=60,bar=72,name='C4',diatonic=28,token='8c',tied=False)
events.append(app)
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
tk=verovio.toolkit();tk.setOptions({'inputFrom':'humdrum','xmlIdSeed':884})
assert tk.loadData(re.sub(r'^\*staff[^\n]*','*staff3\t*staff2\t*staff1',raw,flags=re.M))
mei=tk.getMEI();tree=ET.fromstring(mei);ns={'m':'http://www.music-encoding.org/ns/mei'};ID='{http://www.w3.org/XML/1998/namespace}id'
assert {n.get(ID) for n in tree.findall('.//m:note',ns)}==original_ids
# Verify written pitch against MEI's independent key/accidental spelling.
by_id={e['id']:e for e in events};codes={'ff':-2,'f':-1,'n':0,'s':1,'ss':2,'x':2}
carried={}
for measure in tree.findall('.//m:measure',ns):
 for staff in measure.findall('m:staff',ns):
  state={}
  for note in sorted(staff.findall('.//m:note',ns),key=lambda n:by_id[n.get(ID)]['start']):
   e=by_id[note.get(ID)];pname=note.get('pname');octave=int(note.get('oct'));key=(pname,octave)
   acc=note.find('m:accid',ns);target=acc if acc is not None else note
   sign=target.get('accid') or target.get('accid.ges')
   alt=codes[sign] if sign else (carried[(staff.get('n'),key)] if e['tied'] else state.get(key,{'f': 1}.get(pname,0)))
   expected=12*(octave+1)+{'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}[pname]+alt
   assert expected==e['pitch'],(e,expected)
   state[key]=alt;carried[(staff.get('n'),key)]=alt
   # Explicit gestural accidentals avoid Verovio 6.3 MIDI ignoring key signatures.
   target.set('accid.ges',{-2:'ff',-1:'f',0:'n',1:'s',2:'ss'}[alt])
# Regroup only bars 62–64: retain every pitch, onset, duration and note ID.
M='{http://www.music-encoding.org/ns/mei}'
for b in [62,63,64]:
 measure=tree.find(f'.//m:measure[@n="{b}"]',ns)
 saved={n.get(ID):n for n in measure.findall('.//m:note',ns)}
 for staff in measure.findall('m:staff',ns):
  v=int(staff.get('n'))-1;layer=staff.find('m:layer',ns);layer.clear();layer.set('n','1')
  ns0=sorted([e for e in events if e['bar']==b and e['voice']==v],key=lambda e:e['start'])
  cursor=(b-1)*1.5;beam=None
  def rest(d):
   values={.125:('32',None),.25:('16',None),.5:('8',None),.75:('8','1'),1:('4',None),1.5:('4','1')}
   dur,dots=values[d];r=ET.SubElement(layer,M+'rest',{'dur':dur})
   if dots:r.set('dots',dots)
  if not ns0:ET.SubElement(layer,M+'mRest');continue
  for e in ns0:
   if e['start']>cursor:rest(e['start']-cursor)
   if e['duration']==.125:
    if beam is None:beam=ET.SubElement(layer,M+'beam')
    beam.append(saved[e['id']])
   else:beam=None;layer.append(saved[e['id']])
   cursor=e['start']+e['duration']
  if cursor<b*1.5:rest(b*1.5-cursor)
measure=tree.find('.//m:measure[@n="72"]',ns);layer=measure.find('m:staff[@n="1"]/m:layer',ns)
final=layer.find('m:note',ns);assert final.get(ID)==closing['id']
final.set('dur','4');final.attrib.pop('dots',None)
note=ET.Element(M+'note',{ID:app['id'],'pname':'c','oct':'4','dur':'8','accid.ges':'n'})
layer.insert(0,note)
ET.SubElement(measure,M+'slur',{'startid':'#'+app['id'],'endid':'#'+closing['id'],'staff':'1','curvedir':'above'})
ET.register_namespace('','http://www.music-encoding.org/ns/mei')
mei=ET.tostring(tree,encoding='unicode')
import sys
sys.path.insert(0,str(root.parents[2]/'scripts'))
from verify_render import verify_midi
tk=verovio.toolkit();tk.setOptions({'inputFrom':'mei'});assert tk.loadData(mei)
verify_midi(tk,events)
(root/'sources/bwv884-3-voices.mei').write_text(mei)
(root/'data/score.json').write_text(json.dumps({'events':events,'audio':audio,'duration':duration},ensure_ascii=False,separators=(',',':')))
print(f'{len(events)} written notes, {len(audio)} sounding events, 72 bars; every pitch/onset agrees with Verovio.')
