from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return[n for n in audio if n['voice']==v and a<=n['start']<b]
a=ns(1,.5,9.5)
assert len(a)==15
for v,s,e,tr in [(2,8.5,17.5,-5),(3,24.5,33.5,-12)]:
 b=ns(v,s,e);assert len(a)==len(b)and all(y['pitch']-x['pitch']==tr and y['start']-x['start']==s-.5 and y['duration']==x['duration']for x,y in zip(a,b))
cs=ns(1,10,16.5)
for v,s,e,tr in [(2,26,32.5,-7),(3,34,40.5,-12),(0,58,64.5,-2),(2,82,89,-7)]:
 b=ns(v,s,e);assert len(cs)==len(b)==10 and all(y['pitch']-x['pitch']==tr and y['start']-x['start']==s-10 for x,y in zip(cs,b))
assert len(ns(2,92.5,95.5))==6
b=ns(2,170.5,179.5);diat={(n['voice'],n['start'],n['pitch']):n['diatonic']for n in E}
assert len(b)==15 and all(y['start']-x['start']==170 for x,y in zip(a,b))
assert [diat[(x['voice'],x['start'],x['pitch'])]+diat[(y['voice'],y['start'],y['pitch'])]for x,y in zip(a,b)]==[55]*13+[57,55]
for q,pcs in [(16,{1,10}),(24,{3,6}),(52,{3,6,10}),(64,{3,8,11}),(72,{1,6,10}),(80,{1,3,11}),(88,{3,6}),(92,{3,7,10}),(108.5,{1,4,8}),(118,{6,10}),(120,{1,3,11}),(125,{3,8,11}),(132.5,{3,6,10}),(138,{1,10}),(158.5,{3,6,10}),(170,{3,6}),(182,{3,7,10})]:
 actual={n['pitch']%12 for n in audio if n['start']<=q<n['start']+n['duration']};assert actual==pcs,(q,actual,pcs)
assert len(E)==1117 and len(audio)==1022 and sum(n['tied']for n in E)==95 and D['duration']==184
ids={n['id']:n for n in E};seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice']and a['start']<=ids[n]['start']and ids[n]['start']+ids[n]['duration']<=a['end']for n in a['notes'])
# The added upper-voice divisi note at 45.4-and is not part of the subject.
assert all(n['id']not in seen for n in E if n['voice']==0 and n['start']==179.5)
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^\"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==1117 and set(printed)==set(ids)
for s in systems:
 assert all(s['start']<=ids[n]['bar']<=s['end']for n in re.findall(r'data-note-id="([^\"]+)"',s['svg']))
print('BWV877: real answer, countersubject transpositions, stretto head, final diatonic inversion, seventeen harmonic anchors, 1117 notes and 95 ties verified.')
