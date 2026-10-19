from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return sorted([n for n in E if n['voice']==v and a<=n['start']<b and not n['tied']],key=lambda n:(n['start'],n['pitch']))
s=ns(1,0,16);assert len(s)==22
for v,start,tr in [(0,16,7),(2,32,-12),(2,128,-5)]:
 z=ns(v,start,start+16);assert len(z)==22
 assert all(b['pitch']-a['pitch']==tr and b['start']-a['start']==start and b['duration']==a['duration']for a,b in zip(s,z))
for v,start,tr in [(1,144,0),(2,256,-12),(0,304,12)]:
 z=ns(v,start,start+16);assert len(z)==21
 assert all(b['pitch']-a['pitch']==tr and b['start']-a['start']==start and b['duration']==a['duration']for a,b in zip(s[:20],z[:20]))
 assert z[-1]['pitch']==s[-2]['pitch']+tr and z[-1]['duration']==1
# Written-out trills preserve the subsequent subject, with the simplified ending.
for v,start,tr in [(0,80,12),(1,280,7)]:
 z=ns(v,start,start+16);assert len(z)==23
 assert [n['start']-start for n in z[:5]]==[0,.5,.75,1,1.5]
 assert [n['pitch']-z[0]['pitch']for n in z[:5]]==[0,1,0,-2,0]
 assert all(b['pitch']-a['pitch']==tr and b['start']-a['start']==start for a,b in zip(s[3:21],z[5:]))
minor=ns(0,160,176);assert len(minor)==22
assert all(b['diatonic']-a['diatonic']==5 and b['start']-a['start']==160 for a,b in zip(s,minor))
cs=ns(1,17,31);assert len(cs)==12
for v,start,shift,diffs in [(0,33,16,[5]*12),(2,81,64,[-7]*7+[-8]+[-7]*4),(1,161,144,[2]*12)]:
 z=ns(v,start,start+13.5);assert len(z)==12
 assert [b['pitch']-a['pitch']for a,b in zip(cs,z)]==diffs
 assert all(b['start']-a['start']==shift for a,b in zip(cs,z))
# The bar36 accompaniment is in the bass, despite Prout's treble attribution.
z=ns(2,145.5,159.5);assert len(z)==12 and all(b['pitch']-a['pitch']==-7 for a,b in zip(cs,z))
# CS2's rising central portion recurs above the bass answer and final bass entry.
c2=ns(1,34,41)
for v,start,tr in [(0,130,7),(1,258,0)]:
 z=ns(v,start,start+8)
 for a in c2:
  b=next(n for n in z if n['start']==a['start']+start-34)
  assert b['pitch']==a['pitch']+tr
# The episodic minim figure is the same whole-tone/semitone ascent in all voices.
for v,start in [(1,50),(0,58),(2,66),(1,74),(0,178),(1,186),(2,194),(0,202)]:
 z=ns(v,start,start+5);assert len(z)==3
 assert [n['start']-start for n in z]==[0,2,4]
 assert [n['pitch']-z[0]['pitch']for n in z]==[0,2,3]
 assert all(n['duration']==2 for n in z[:2])
# Six distributions of the three episodic figures; verify their distinctive cores.
# q = quaver figure; m = minim ascent; c = repeated crotchet and descending second.
perms=[]
for qv,mv,cv,t in [(0,1,2,49),(2,0,1,57),(1,2,0,65),(1,0,2,177),(2,1,0,185),(0,2,1,193)]:
 m=ns(mv,t+1,t+5);assert [n['duration']for n in m]==[2,2]
 # Each active texture has three distinct parts; quaver detail may be varied.
 assert len({qv,mv,cv})==3 and any(n['duration']==.5 for n in ns(qv,t,t+5))
 assert any(n['duration']==1 for n in ns(cv,t,t+5))
 perms.append((qv,mv,cv))
assert len(set(perms))==6
for q,pcs in [(32,{1,5}),(48,{6,10}),(54,{3,6}),(62,{3,8,11}),(70,{1,5,8}),(78,{6,10}),(96,{6,10}),(103,{3,6}),(112,{0,8}),(144,{1,5}),(176,{3,6}),(182,{8,11}),(190,{1,5,8}),(198,{1,6,10}),(206,{3,11}),(223,{3,11}),(233,{1,4,8}),(255,{3,6}),(282,{1,5}),(319.5,{6,10}),(332,{1,5,8}),(334,{6,10})]:
 assert {n['pitch']%12 for n in audio if n['start']<=q<n['start']+n['duration']}==pcs,q
assert len(E)==1150 and len(audio)==1123 and sum(n['tied']for n in E)==27 and D['duration']==336
ids={n['id']:n for n in E};seen=set();assert sum(a['kind']=='subject'for a in anns)==11
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end']for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^\"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==1150 and set(printed)==set(ids)
for s in systems:assert all(s['start']<=ids[n]['bar']<=s['end']for n in re.findall(r'data-note-id="([^\"]+)"',s['svg']))
print('BWV882: real answer, eleven entries, written-out trills, both countersubjects, six episodic dispositions, twenty-two harmonic anchors and 1150 notes/27 ties verified.')
