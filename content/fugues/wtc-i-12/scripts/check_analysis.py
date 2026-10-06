"""Verify thematic onsets, tonal answer, invertible combinations and arrivals."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];A=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return [n for n in E if n['voice']==v and a<=n['start']<b]
def paired(x,y,shift,delta):
 assert len(x)==len(y),(len(x),len(y))
 assert all(abs(b['start']-a['start']-shift)<1e-7 and a['duration']==b['duration'] and b['pitch']-a['pitch']==delta for a,b in zip(x,y))
s,a=ns(2,1,12.5),ns(1,13,24.5);assert len(s)==len(a)==11
assert [y['pitch']-x['pitch'] for x,y in zip(s,a)]==[5]+[7]*10
subjects=[(2,1),(1,13),(3,25),(0,49),(2,73),(3,107),(1,133),(2,159),(0,185),(3,209)]
assert [(a['voice'],a['start']) for a in anns if a['kind']=='subject']==subjects
for v,q in subjects:
 x=ns(v,q,q+11)
 assert len(x)==10
 assert [n['start']-q for n in x]==list(range(10))
 assert [n['duration'] for n in x]==[1]*9+[2]
assert [n['pitch'] for n in ns(3,107,118)]==[n['pitch']-12 for n in ns(2,1,12)]
assert [n['pitch'] for n in ns(3,209,220)]==[n['pitch']-12 for n in ns(2,1,12)]
# Three main themes invert between the fourth and sixth entries.
paired(ns(0,49,60),ns(3,107,118),58,-24)
paired(ns(3,50.25,61),ns(2,108.25,119),58,12)
x=ns(1,51.5,54.5)+ns(2,55.25,61);y=ns(0,109.5,119)
assert [(b['start']-a['start'],b['pitch']-a['pitch']) for a,b in zip(x,y)]==[(58,12)]*20
assert [(a['start'],b['duration']-a['duration']) for a,b in zip(x,y) if a['duration']!=b['duration']]==[(54,.5)]
# Tovey's additional countersubject crosses the second at its first appearance.
x=ns(2,51.25,54.5)+ns(1,55.5,61);y=ns(1,109.25,119)
assert len(x)==len(y)
assert [n['start'] for n in y]==[n['start']+58 for n in x]
assert [n['pitch'] for n in y]==[n['pitch']+12 for n in x]
# Minor rhythmic variants at the joined notes do not change that thematic identity.
assert sum(a['duration']!=b['duration'] for a,b in zip(x,y))<=2
for q,pcs in [(24,{0}),(36,{5,8}),(60.5,{0,5,8}),(72.5,{0,3,7}),(84,{0,3}),(118,{0,5,8}),(133,{0,3,8}),(159.5,{3,7,10}),(170,{3,7,10}),(190.25,{0,3,7}),(196.5,{0,3,7}),(208.5,{5,8}),(228,{0,5,9})]:
 assert {n['pitch']%12 for n in A if n['start']<=q<n['start']+n['duration']}==pcs,q
assert len(E)==1409 and len(A)==1318 and sum(n['tied'] for n in E)==91 and D['duration']==232
ids={n['id']:n for n in E};seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end'] for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==1409 and set(printed)==set(ids)
print('BWV857: ten subject entries, tonal answer, triple counterpoint, divided additional countersubject, thirteen harmonic anchors, 1409 notes/91 ties and final major third verified.')
