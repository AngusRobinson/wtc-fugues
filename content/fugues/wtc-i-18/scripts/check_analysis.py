"""Check answer, source correction, triple counterpoint, tonal anchors and score coverage."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];A=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return[n for n in E if n['voice']==v and a<=n['start']<b]
s,a=ns(2,1,8.5),ns(1,9,17);assert len(s)==len(a)==15
assert[y['pitch']-x['pitch']for x,y in zip(s,a)]==[7]+[5]*14
assert all(y['start']-x['start']==8 for x,y in zip(s,a))
x,y=ns(2,9,16.5),ns(1,17,25);assert len(x)==len(y)==15
assert all(b['pitch']-a['pitch']==7 and b['start']-a['start']==8 for a,b in zip(x,y))
assert ns(1,20.75,21)[0]['pitch']==65
for v,q,end,w,r,delta in [(2,41,49,1,73,0),(0,41,48.5,2,73,-24),(1,42.5,49,3,74.5,-24)]:
 x,y=ns(v,q,end),ns(w,r,r+end-q-.5 if v in [2,1] else r+end-q)
 assert len(x)==len(y),(v,len(x),len(y))
 assert all(b['start']-a['start']==32 and b['pitch']-a['pitch']==delta for a,b in zip(x,y))
 assert all(a['duration']==b['duration'] for a,b in zip(x[:-1],y[:-1]))
f=ns(0,145.5,152.5);assert len(f)==15 and all(b['pitch']-a['pitch']==17 for a,b in zip(s,f))
assert f[0]['duration']==.5 and all(b['start']-a['start']==144 for a,b in zip(s[1:],f[1:]))
assert len([a for a in anns if a['kind']=='subject'])==12
for q,pcs in [(8,{3}),(16,{8}),(24,{3,8}),(32,{3,8,11}),(36,{3,6,11}),(40,{3,6}),(48,{1,8}),(56,{1,6}),(64,{1,3,8}),(72,{3,5,6}),(108,{1,4,11}),(116,{3,8}),(125,{3,8,11}),(133,{3,6,10}),(141.5,{4,8,11}),(144,{1,6,8}),(160,{3,8,11})]:
 actual={n['pitch']%12 for n in A if n['start']<=q<n['start']+n['duration']};assert actual==pcs,(q,actual)
assert len(E)==847 and len(A)==804 and sum(n['tied']for n in E)==43 and D['duration']==164
ids={n['id']:n for n in E};seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end'] for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==847 and set(printed)==set(ids)
print('BWV863: tonal and real answers, corrected E sharp, triple counterpoint, twelve entries, seventeen harmonic anchors and all 847 notes verified.')
