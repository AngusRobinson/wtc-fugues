"""Check the tonal answer, thematic dispositions, anchored harmonies and rendered notes."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];A=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return [n for n in E if n['voice']==v and a<=n['start']<b]
x,y=ns(0,.5,12.75),ns(1,12.5,24.75);assert len(x)==len(y)==38
assert [b['pitch']-a['pitch']for a,b in zip(x,y)]==[-7,-5,-7]+[-5]*35
assert all(b['start']-a['start']==12 and a['duration']==b['duration']for a,b in zip(x,y))
assert [(a['voice'],a['start'])for a in anns if a['kind']=='subject' and a['status']=='statement']==[(0,.5),(1,12.5),(2,24.5),(0,36.5),(1,63.5),(2,75.5),(0,108.5),(1,120.5)]
assert [(a['voice'],a['start'],a['end'])for a in anns if a['kind']=='subject' and a['status']=='fragment']==[(1,102.5,108)]
# The later bars of both countersubjects retain exact diatonic shapes in new registers.
for v,q,w,r,delta in [(0,30,1,42,-10),(1,30,2,42,-10),(0,30,2,69,-16),(1,30,0,69,5),(1,30,1,114,-4)]:
 x,y=ns(v,q,q+6),ns(w,r,r+6);assert len(x)==len(y)
 assert all(b['diatonic']-a['diatonic']==delta and b['start']-r==a['start']-q and (a['duration']==b['duration'] or v==0 and a['start']-q==3 and a['duration']==1 and b['duration']==.5)for a,b in zip(x,y))
for q,pcs in [(24.5,{0,5,9}),(36,{2,5,10}),(48,{5,9}),(63,{2,6}),(75,{2,7,10}),(87,{0,3,7}),(102,{0,3}),(120,{3,7,10}),(132,{2,5,10}),(141,{2,10})]:
 assert {n['pitch']%12 for n in A if n['start']<=q<n['start']+n['duration']}==pcs,q
assert len(E)==968 and len(A)==952 and sum(n['tied']for n in E)==16 and D['duration']==144
ids={n['id']:n for n in E};seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end']for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==968 and set(printed)==set(ids)
print('BWV866: tonal answer, eight complete entries and one fragment, countersubject inversions, ten tonal anchors, 968 notes and 16 ties verified.')
