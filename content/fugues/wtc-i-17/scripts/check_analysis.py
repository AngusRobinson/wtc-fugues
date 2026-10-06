"""Verify tonal answer, the semiquaver inversion and episodic triple counterpoint."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];A=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return [n for n in E if n['voice']==v and a<=n['start']<b]
s=ns(2,1,5);a=ns(3,5,8.5);assert len(s)==len(a)==7
assert [y['pitch']-x['pitch'] for x,y in zip(s,a)]==[-5,-7,-5,-5,-5,-5,-5]
assert [y['start']-x['start'] for x,y in zip(s,a)]==[4]*7
x,y=ns(2,5,7),ns(2,7,9);assert len(x)==len(y)==8
assert len(set(a['diatonic']+b['diatonic']for a,b in zip(x,y)))==1
for v,q,end,w,r,delta in [(0,41.25,46,3,53.25,-22),(2,41,46,0,53,10),(3,41,46,1,53,10),(0,41.25,48,1,73.25,-8),(2,41,48,2,73,-1),(3,41,48,0,73,13)]:
 x,y=ns(v,q,end),ns(w,r,r+end-q)
 if v==3 and w==0:
  y=[dict(n)for n in y if n['start']!=76.75]
  next(n for n in y if n['start']==76.5)['duration']=.5
 assert len(x)==len(y),(v,q,w,r)
 assert all(a['start']-q==b['start']-r and a['duration']==b['duration'] and b['diatonic']-a['diatonic']==delta for a,b in zip(x,y)),(v,q,w,r,[(a['start'],b['start'],b['diatonic']-a['diatonic'])for a,b in zip(x,y)])
assert len([a for a in anns if a['kind']=='subject'])==15
assert [(a['voice'],a['start'])for a in anns if a['kind']=='subject' and 105<=a['start']<121]==[(3,105),(2,109),(1,113),(0,117)]
for q,pcs in [(17,{0,8}),(25,{3,7,10}),(36,{0,8}),(52,{0,5,8}),(60,{5,8}),(69,{1,5,10}),(72.5,{1,10}),(88,{3,7}),(105,{0,8}),(112,{0,5,7}),(120.5,{1,5,8}),(124,{0,5,8}),(127,{0,8}),(138,{0,3,8})]:
 actual={n['pitch']%12 for n in A if n['start']<=q<n['start']+n['duration']};assert actual==pcs,(q,actual)
assert len(E)==933 and len(A)==891 and sum(n['tied']for n in E)==42 and D['duration']==140
ids={n['id']:n for n in E};seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end'] for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==933 and set(printed)==set(ids)
print('BWV862: tonal answer, fifteen entries, semiquaver inversion, triple counterpoint in two dispositions, fourteen tonal anchors and 933 notes/42 ties verified.')
