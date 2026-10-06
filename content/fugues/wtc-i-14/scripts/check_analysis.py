"""Verify real answer, diatonic inversions, countersubject recurrence and harmonic anchors."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];A=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return [n for n in E if n['voice']==v and a<=n['start']<b]
s=ns(2,1,21);a=ns(1,19,36.5);assert len(s)==len(a)==20
assert all(y['pitch']-x['pitch']==7 and y['start']-x['start']==18 for x,y in zip(s,a))
assert [(a['voice'],a['start']) for a in anns if a['kind']=='subject']==[(2,1),(1,19),(3,43),(0,85),(1,118),(0,145),(2,169),(3,187),(0,217)]
for v,q,end,total in [(1,118,137,59),(3,187,207,48)]:
 inv=ns(v,q,end);assert len(inv)==20
 assert all(x['diatonic']+y['diatonic']==total and y['start']-q==x['start']-1 for x,y in zip(s,inv))
for v,q,end,delta in [(1,45.5,63,5),(3,87.5,103.5,-7),(1,147.5,163.5,12)]:
 x,y=ns(2,21.5,37.5),ns(v,q,end);assert len(x)==len(y)
 assert all(b['pitch']-a['pitch']==delta and b['start']-q==a['start']-21.5 for a,b in zip(x,y))
for q,pcs in [(36,{1}),(60.5,{6,9}),(102,{1,6,9}),(117,{1,4}),(129,{6,9}),(145,{1,6,9}),(162,{1}),(171,{6,9}),(186,{6,9}),(198,{2,11}),(204,{1,6,8,9}),(234,{1,6,10})]:
 actual={n['pitch']%12 for n in A if n['start']<=q<n['start']+n['duration']};assert actual==pcs,(q,actual,pcs)
assert len(E)==883 and len(A)==811 and sum(n['tied'] for n in E)==72 and D['duration']==240
ids={n['id']:n for n in E};seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end'] for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==883 and set(printed)==set(ids)
print('BWV859: real answer, nine entries, two diatonic inversions, countersubject recurrence, twelve harmonic anchors and 883 notes/72 ties verified.')
