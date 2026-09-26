"""Independent checks of pitches, thematic readings, cadences and rendered note coverage."""
import json,re
from pathlib import Path
import xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];A=D['audio'];byid={n['id']:n for n in E};anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def q(b,o=0):return (b-1)*4+o
def head(v,b,o=0,count=6):return [n for n in E if n['voice']==v and n['start']>=q(b,o) and not n['tied']][:count]
def sounding(b,o=0):return {n['pitch']%12 for n in A if n['start']<=q(b,o)<n['start']+n['duration']}

s=head(0,1);answer=head(1,3)
assert [n['pitch'] for n in s]==[70,65,78,77,75,73]
assert [n['pitch'] for n in answer]==[65,58,73,72,70,68]
assert [n['pitch']-m['pitch'] for n,m in zip(answer,s)]==[-5,-7,-5,-5,-5,-5],'Tonal answer'
assert s[2]['pitch']-s[1]['pitch']==13,'Minor ninth'
assert [head(v,b,0,1)[0]['start'] for v,b in [(0,1),(1,3),(2,10),(3,12),(4,15)]]==[0,8,36,44,56]
assert head(4,15)[-1]['name']=='D3','Major third in bass ending'
assert head(2,46,1,2)[1]['duration']==1,'Shortened second note in displaced entry'
assert [n['name'] for n in head(4,52)][:3]==['E♭3','A♭2','G♭2'],'Altered bass leap'
last=[a for a in anns if a['kind']=='subject' and q(67)<=a['start']<q(70)]
assert [a['voice'] for a in last]==[0,1,2,3,4] and [a['start'] for a in last]==[266,268,270,272,274]
assert [n['name'] for n in head(1,68)][-1]=='B♭4' and [n['name'] for n in head(3,69)][-1]=='B♭3','Altered final answers'
assert sounding(25)=={1,5,8} and sounding(37)=={0,3,8} and sounding(55)=={3,6,10} and sounding(75)=={2,5,10}
assert len(E)==813 and len(A)==745 and sum(n['tied'] for n in E)==68 and D['duration']==300

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

print('BWV 867: tonal answer, ninth leap, bass entry at 15, displaced and altered entries, five-part minim stretto, cadences, 813 notes and 68 ties verified.')
