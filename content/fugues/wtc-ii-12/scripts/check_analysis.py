from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return sorted([n for n in E if n['voice']==v and a<=n['start']<b and not n['tied']],key=lambda n:(n['start'],n['pitch']))
s=ns(0,0,6.75);a=ns(1,8,14.75);assert len(s)==len(a)==21
assert [y['pitch']-x['pitch']for x,y in zip(s,a)]==[-7]+[-5]*20
assert all(y['start']-x['start']==8 and y['duration']==x['duration']for x,y in zip(s,a))
for v,start,tr,ending in [(2,22,-12,.25),(2,80,-12,.25),(1,100,-12,.5),(0,142,5,.5),(1,148,0,.5)]:
 b=ns(v,start,start+6.75);assert len(b)==21
 assert all(y['pitch']-x['pitch']==tr and y['start']-x['start']==start for x,y in zip(s,b))
 assert [n['duration']for n in b]==[n['duration']for n in s[:-1]]+[ending]
major=ns(0,48,54.75);ma=ns(1,56,64.5);assert len(major)==len(ma)==21
assert all(y['diatonic']-x['diatonic']==2 and y['start']-x['start']==48 and y['duration']==x['duration']for x,y in zip(s,major))
assert [y['pitch']-x['pitch']for x,y in zip(major,ma)]==[-7]+[-5]*20
assert [n['duration']for n in ma]==[n['duration']for n in s[:-1]]+[2]
# Invertible upper pair: one part moves down a fourth, the other up a fifth.
for v,w,tr in [(0,1,-5),(1,0,7),(2,2,-5)]:
 x=ns(v,32.5,36.5);y=ns(w,64.5,68.5);assert len(x)==len(y)
 assert all(b['pitch']-a['pitch']==tr and b['start']-a['start']==32 and b['duration']==a['duration']for a,b in zip(x,y))
# The last entry overlaps only the preceding statement's closing tail.
last_s=next(a for a in anns if a['kind']=='subject' and a['voice']==0 and a['start']==142)
last_a=next(a for a in anns if a['kind']=='subject' and a['voice']==1 and a['start']==148)
assert last_s['start']+4.5<last_a['start']<last_s['end']
assert [n['pitch']for n in ns(0,last_a['start'],last_s['end'])]==[77,75,73]
# Repeated-quaver head sequences have changed intervals: they are not entries.
for start in [110.5,122.5]:
 head=ns(2,start,start+6);assert len(head)==15
 for j in [0,5,10]:
  group=head[j:j+5];assert len({n['pitch']for n in group[:3]})==1
  assert [n['duration']for n in group]==[.5,.5,.5,.25,.25]
assert not [n for n in E if n['voice']==2 and n['bar']==53]
assert {n['pitch']for n in ns(2,98.5,104.5)}=={48}
for q,pcs in [(14.5,{0,3}),(22.5,{5,8}),(32.5,{0,5,8}),(40.5,{1,5,8}),(44.5,{0,8}),(64.5,{0,3,7}),(72.5,{0,3,8}),(79,{0,4}),(80.5,{5,7,8}),(94.5,{1,5}),(98.5,{0,4}),(106.5,{1,5,8}),(117,{1,10}),(122.5,{0,7,10}),(130.5,{5,8}),(138.5,{1,5,8}),(142.5,{1,10}),(152.5,{0,4,10}),(154.5,{0,5,8}),(168.5,{5})]:
 assert {n['pitch']%12 for n in audio if n['start']<=q<n['start']+n['duration']}==pcs,q
assert len(E)==1165 and len(audio)==1117 and sum(n['tied']for n in E)==48 and D['duration']==170
ids={n['id']:n for n in E};seen=set();assert sum(a['kind']=='subject'for a in anns)==9
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end']for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^\"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==1165 and set(printed)==set(ids)
for s in systems:assert all(s['start']<=ids[n]['bar']<=s['end']for n in re.findall(r'data-note-id="([^\"]+)"',s['svg']))
print('BWV881: tonal answer, nine entries, major-mode pair, inverted episodic upper parts, head development, authentic bass rest, twenty harmonic anchors and 1165 notes/48 ties verified.')
