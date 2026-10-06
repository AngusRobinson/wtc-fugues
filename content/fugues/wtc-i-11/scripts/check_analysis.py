"""Verify the anacrusis, tonal answer, paired stretti and closing alterations."""
from pathlib import Path
import json,re,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];A=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return [n for n in E if n['voice']==v and a<=n['start']<b]
def pair(v,a,b,w,c,d,delta):
 x,y=ns(v,a,b),ns(w,c,d);assert len(x)==len(y)
 assert [(n['start']-a,n['duration']) for n in x]==[(n['start']-c,n['duration']) for n in y]
 assert all(q['pitch']-p['pitch']==delta for p,q in zip(x,y))
 return len(x)
s,a=ns(1,0,5.25),ns(0,6,11.25);assert len(s)==len(a)==15
assert [q['pitch']-p['pitch'] for p,q in zip(s,a)]==[5]+[7]*14
assert pair(1,0,5.25,2,13.5,18.75,-12)==15
assert pair(0,54,59,1,57,62,-12)==14
assert pair(1,57,62,2,60,65,-12)==14
assert pair(2,69,74,1,72,77,12)==15
assert pair(2,69.5,74,0,75.5,80,24)==14
assert ns(0,75,75.5)[0]['pitch']==72 and ns(0,75,75.5)[1]['pitch']==74
assert [n['pitch'] for n in ns(0,96.25,98.5)]==[72,74,72,75,74,72,70,72]
assert next(n for n in E if n['voice']==0 and n['start']==81.25)['pitch']==73
# The characteristic CS tail passes from alto to bass in the counter-exposition.
assert pair(1,8,11,2,27.5,30.5,-7)==7
for q,pc in [(11,{0,4}),(24.5,{0,2,4}),(30.5,{5,9}),(45.5,{5,7,9}),(68,{2}),(83,{7}),(95,{5,7,9}),(107,{5})]:
 assert {n['pitch']%12 for n in A if n['start']<=q<n['start']+n['duration']}==pc,q
assert len(E)==696 and len(A)==670 and sum(n['tied'] for n in E)==26 and D['duration']==108
assert {n['bar'] for n in E}==set(range(73))
assert max(n['start']+n['duration'] for n in E if n['bar']==0)==.5
assert all(n['start']>=107 and n['start']+n['duration']<=108 for n in E if n['bar']==72)
assert len([a for a in anns if a['kind']=='subject'])==15
assert next(a for a in anns if a['kind']=='subject' and a['start']==97.5)['end']==108
ids={n['id']:n for n in E};seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end'] for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==696 and set(printed)==set(ids)
for ex in json.loads((R/'data/thematic-examples.json').read_text()):
 for g in ET.fromstring(ex['svg']).iter():
  if g.get('class')=='beam':assert len([n for n in g.iter() if 'note' in n.get('class','').split()])>=2
print('BWV856: anacrusis, tonal answer, two octave-stretto dispositions, divided countersubject, ornamented final entries, eight harmonic anchors, 696 notes/26 ties and shortened final bar verified.')
