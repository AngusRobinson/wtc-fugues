"""Check the two-part construction independently against the parsed score."""
from pathlib import Path
import json,re,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];A=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return [n for n in E if n['voice']==v and a<=n['start']<b]
def pair(v,a,b,w,c,d,deltas):
 x,y=ns(v,a,b),ns(w,c,d);assert len(x)==len(y)
 assert [(n['start']-a,n['duration']) for n in x]==[(n['start']-c,n['duration']) for n in y]
 assert {q['pitch']-p['pitch'] for p,q in zip(x,y)}==set(deltas)
 return len(x)
s,a=ns(0,0,6.5),ns(1,6,12.5)
assert len(s)==len(a)==25
assert [y['pitch']-x['pitch'] for x,y in zip(s,a)]==[-17]*24+[-16]
assert pair(0,0,6.5,1,57,63.5,[-19])==25
assert pair(1,6,12.5,0,63,69.5,[17])==25
assert pair(0,12,27,1,69,84,[-19])==54
assert pair(1,12,27,0,69,84,[17,29])==45
assert pair(0,42,54,1,99,111,[-17])==36
assert pair(1,42,54,0,99,111,[19])==36
assert pair(0,7.25,12.25,1,64.25,69.25,[-19])==17
for q,interval in [(54,-24),(111,-12)]:assert pair(0,q,q+3,1,q,q+3,[interval])==12
for q,pcs in [(6,{2,11}),(12.25,{6,10}),(30,{7,11}),(36,{2,6}),(57,{9}),(63,{4,7}),(87,{2,5}),(93,{0,9}),(114,{4}),(123,{4,8})]:
 assert {n['pitch']%12 for n in A if n['start']<=q<n['start']+n['duration']}==pcs,q
assert len(E)==825 and len(A)==810 and sum(n['tied'] for n in E)==15 and D['duration']==126
assert max(n['start']+n['duration'] for n in A)==123.5
entries=[a for a in anns if a['kind']=='subject'];assert len(entries)==10 and sum(a['status']=='fragment' for a in entries)==2
ids={n['id']:n for n in E};seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end'] for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==825 and set(printed)==set(ids)
for ex in json.loads((R/'data/thematic-examples.json').read_text()):
 for g in ET.fromstring(ex['svg']).iter():
  if g.get('class')=='beam':assert len([n for n in g.iter() if 'note' in n.get('class','').split()])>=2
print('BWV855: real answer with altered final note, two contrapuntal inversions, countersubject recurrence, octave passages, ten harmonic anchors, 825 notes/15 ties and final measured silence verified.')
