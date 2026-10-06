"""Verify the tonal answer, twelfth inversion, closing recurrence and cadence anchors."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];A=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return [n for n in E if n['voice']==v and a<=n['start']<b]
def pair(v,a,b,w,c,d,delta):
 x,y=ns(v,a,b),ns(w,c,d);assert len(x)==len(y)
 assert [(n['start']-a,n['duration']) for n in x]==[(n['start']-c,n['duration']) for n in y]
 assert all(q['pitch']-p['pitch']==delta for p,q in zip(x,y));return len(x)
s,a=ns(0,.5,8.5),ns(1,8.5,16.5);assert len(s)==len(a)==16
assert [y['pitch']-x['pitch'] for x,y in zip(s,a)]==[-7]+[-5]*15
assert [(n['start']-.5,n['duration']) for n in s]==[(n['start']-8.5,n['duration']) for n in a]
assert [(a['voice'],a['start']) for a in anns if a['kind']=='subject']==[(0,.5),(1,8.5),(2,16.5),(0,42.5),(1,56.5),(2,76.5),(1,108.5),(0,122.5)]
x,y=ns(0,10,14),ns(2,58,62)
assert len(x)==len(y)==15
assert [(n['start']-10,n['duration']) for n in x]==[(n['start']-58,n['duration']) for n in y]
assert [b['diatonic']-a['diatonic'] for a,b in zip(x,y)]==[-11]*15
assert [b['pitch']-a['pitch'] for a,b in zip(x,y)]==[-19,-18,-19,-19,-18]+[-19]*10
assert pair(2,58,64,2,124,130,-7)==20
assert pair(1,56.5,64,0,122.5,130,5)==15
assert pair(0,56,64,1,122,130,-7)==15
# Bach's short-to-long tie, discussed by Keller, remains intact.
n=next(n for n in E if n['voice']==1 and n['start']==86.75);t=next(n for n in E if n['voice']==1 and n['start']==87)
assert n['duration']==.25 and t['duration']==.5 and t['tied'] and n['pitch']==t['pitch']==75
for q,pcs in [(16,{1,5}),(24,{6,10}),(42,{1,5}),(64,{1,5}),(68,{1,10}),(77,{3,6}),(84.25,{3,6}),(88,{3}),(110.25,{3,11}),(116,{3,11}),(130,{6,10}),(136,{6,10})]:
 assert {n['pitch']%12 for n in A if n['start']<=q<n['start']+n['duration']}==pcs,q
assert len(E)==891 and len(A)==858 and sum(n['tied'] for n in E)==33 and D['duration']==140
ids={n['id']:n for n in E};seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end'] for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==891 and set(printed)==set(ids)
print('BWV858: tonal answer, eight entries, twelfth inversion with tonal adjustments, closing three-part recurrence, twelve harmonic anchors, original short-to-long tie and 891 notes/33 ties verified.')
