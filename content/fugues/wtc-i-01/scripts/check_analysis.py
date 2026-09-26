"""Independent checks of pitches, thematic readings, cadences and rendered note coverage."""
import json,re
from pathlib import Path
import xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];A=D['audio'];byid={n['id']:n for n in E};anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def q(b,o=0):return (b-1)*4+o
def head(v,b,o=0,count=6):return [n for n in E if n['voice']==v and n['start']>=q(b,o) and not n['tied']][:count]
def sounding(b,o=0):return {n['pitch']%12 for n in A if n['start']<=q(b,o)<n['start']+n['duration']}

s=head(1,1,.5,14);answer=head(0,2,2.5,14)
assert [n['pitch'] for n in s]==[60,62,64,65,67,65,64,69,62,67,69,67,65,64]
assert [n['pitch']-m['pitch'] for n,m in zip(answer,s)]==[7]*14,'Real answer'
assert [(a['voice'],a['label']) for a in anns if a['kind']=='subject'][:4]==[(1,'S'),(0,'A'),(2,'A'),(3,'S')]
assert sum(a['kind']=='subject' for a in anns)==24 and sum(a['kind']=='head' for a in anns)==3
assert [head(v,b,o,1)[0]['start'] for v,b,o in [(1,14,.5),(2,14,1.5),(3,15,.5),(0,15,2.5)]]==[52.5,53.5,56.5,58.5]
assert head(3,17,2,1)[0]['duration']==1,'Lengthened bass opening'
assert head(3,20,2.5,6)[3]['duration']==.25,'Undotted altered bass head'
assert sounding(14)=={9} and sounding(23,1)=={0,4,7} and sounding(24)=={0,4,7}
assert sounding(27,2)=={0,4,7} and max(n['pitch'] for n in E)==84
assert any(n['voice']==3 and n['pitch']==48 and n['start']==q(24) and n['duration']==16 for n in A),'Tonic pedal'
assert len(E)==786 and len(A)==734 and sum(n['tied'] for n in E)==52 and D['duration']==108

seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(byid[n]['voice']==a['voice'] and a['start']<=byid[n]['start'] and byid[n]['start']+byid[n]['duration']<=a['end'] for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text())
printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==len(E) and set(printed)==set(byid)
for ex in json.loads((R/'data/thematic-examples.json').read_text()):
 root=ET.fromstring(ex['svg'])
 for g in root.iter():
  if g.get('class')=='beam':assert len([n for n in g.iter() if 'note' in n.get('class','').split()])>=2,'Orphan beam in example'

print('BWV 846: real answer, irregular exposition, 24 entries and three head allusions, stretched bass entry, cadences, tonic pedal, 786 notes and 52 ties verified.')
