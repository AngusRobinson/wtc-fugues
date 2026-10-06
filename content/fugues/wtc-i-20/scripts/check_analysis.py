"""Check answer, inversions, twelfth counterpoint, restored ending and tonal anchors."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];A=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return[n for n in E if n['voice']==v and a<=n['start']<b]
s,a=ns(1,.5,13),ns(0,12.5,24.5);assert len(s)==len(a)==31
assert all(y['pitch']-x['pitch']==7 and y['start']-x['start']==12 for x,y in zip(s,a))
head=ns(1,.5,4)
for v,q in [(0,54.5),(2,68.5),(3,80.5),(1,92.5),(1,190.5),(2,192.5),(3,208.5),(0,210.5),(0,226.5),(1,228.5),(0,266.5),(1,268.5),(3,288.5),(1,290.5),(2,300.5),(3,330.5),(2,332.5)]:
 x=ns(v,q,q+3.5);assert len(x)==len(head)==9
 assert len({n['diatonic']+m['diatonic']for n,m in zip(x,head)})==1,(v,q)
 assert all(n['start']-m['start']==q-.5 and n['duration']==m['duration']for n,m in zip(x,head))
# Octave stretto becomes a fifth stretto: leader down a twelfth, follower unchanged.
for v,a,b,w,c,d,delta in [(0,106.5,118.5,3,254.5,266.5,-11),(2,108.5,122,2,256.5,269,0)]:
 x,y=ns(v,a,b),ns(w,c,d);assert len(x)==len(y)==31
 assert all(q['diatonic']-p['diatonic']==delta and q['start']-p['start']==c-a for p,q in zip(x,y))
 assert all(q['duration']==p['duration']for p,q in zip(x[:-1],y[:-1]))
# First six countersubject notes return an octave higher; later continuations vary.
x=ns(1,13,16)
for v,q in [(0,29),(1,41)]:
 y=ns(v,q,q+3);assert len(y)==len(x)==6
 assert all(b['diatonic']-a['diatonic']==7 and b['duration']==a['duration']for a,b in zip(x,y))
assert len([a for a in anns if a['kind']=='subject'])==39
assert ns(2,332.5,332.75)[0]['name']=='A4'
assert any(n['voice']==4 and n['start']==330 and n['duration']==18 and n['pitch']==45 for n in A)
for q,pcs in [(28,{0,9}),(42,{4,7}),(54,{8,4}),(68,{2,11,7}),(79.5,{9,2,5}),(91,{0,4,7}),(106,{0,9}),(136,{4,7}),(168.5,{0,4,7}),(188,{0,4,7}),(254.5,{9,2,5}),(266.5,{0,9,4}),(286.5,{0,9,5}),(300,{2,10,7}),(328,{0,9,4}),(330,{9,4,1}),(346,{9,4,1})]:
 actual={n['pitch']%12 for n in A if n['start']<=q<n['start']+n['duration']};assert actual==pcs,(q,actual)
assert len(E)==2516 and len(A)==2407 and sum(n['tied']for n in E)==109 and D['duration']==348
ids={n['id']:n for n in E};seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end']for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==2516 and set(printed)==set(ids)
print('BWV865: real answer, inversions, double counterpoint at the twelfth, 39 full/partial entries, restored ending and 16 exact harmonic anchors plus one entry context checked.')
