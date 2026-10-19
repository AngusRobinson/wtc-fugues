from pathlib import Path
import json,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return sorted([n for n in E if n['voice']==v and a<=n['start']<b and not n['tied']],key=lambda n:n['start'])
s=ns(0,.25,7.75);assert len(s)==30
z=ns(1,10.75,18.25);assert len(z)==30
assert [b['pitch']-a['pitch']for a,b in zip(s,z)]==[-7]+[-5]*29
assert all(b['start']-a['start']==10.5 and b['duration']==a['duration']for a,b in zip(s,z))
for v,start,end in [(2,21.25,28.75),(1,96.25,104)]:
 z=ns(v,start,end);assert len(z)==30
 assert all(b['pitch']-a['pitch']==-12 and b['start']-a['start']==start-.25 for a,b in zip(s,z))
for v,start,tr in [(2,48.25,-9),(0,58.75,2)]:
 z=ns(v,start,start+7.5);assert len(z)==30
 want=[tr]*30
 if v==0:want[0]=1
 assert [b['diatonic']-a['diatonic']for a,b in zip(s,z)]==want
 assert all(b['start']-a['start']==start-.25 and b['duration']==a['duration']for a,b in zip(s,z))
# The sequential core of CS1 recurs above the bass and then below the soprano.
cs=ns(0,24,27.75);assert len(cs)==8
for v,a,tr in [(0,51,-2),(2,61.5,-12)]:
 z=ns(v,a,a+3.75);assert len(z)==8
 assert all(y['diatonic']-x['diatonic']==tr and y['start']-x['start']==a-24 and y['duration']==x['duration']for x,y in zip(cs,z))
cs=ns(1,24,28.5);z=ns(1,61.5,66);assert len(cs)==len(z)==6
assert all(y['diatonic']-x['diatonic']==-5 and y['start']-x['start']==37.5 and y['duration']==x['duration']for x,y in zip(cs,z))
assert [tuple(next(a['voice']for a in anns if a['kind']==k and a['start']<=q<a['end'])for k in ['subject','cs1','cs2'])for q in [25,52,63]]==[(2,0,1),(2,0,1),(0,2,1)]
run=[n for n in E if 92.25<=n['start']<96 and n['duration']==.125]
assert len(run)==30 and all(n['voice']==0 for n in run)
assert sorted(n['start']for n in run)==[92.25+i*.125 for i in range(30)]
assert min(n['pitch']for n in run)==38 and max(n['pitch']for n in run)==72
assert [(n['start'],n['pitch'],n['duration'])for n in ns(0,106.5,108)]==[(106.5,60,.5),(107,59,1)]
# The two corrected notes in the bar-30 chord both remain tied into bar 31.
assert {(n['pitch'],n['tied'])for n in E if n['voice']==1 and n['start']==45}=={(72,True),(69,True)}
for q,pcs in [(18.5,{2,6}),(21,{7,11}),(33,{2,6}),(36.5,{7,11}),(42.5,{0,9}),(49.5,{4,7}),(56,{4,7}),(59,{2,11}),(66,{2,11}),(72.5,{0,9}),(78.5,{7,11}),(82.5,{0,2,6}),(103.75,{7,11}),(107,{7,11})]:
 assert {n['pitch']%12 for n in audio if n['start']<=q<n['start']+n['duration']}==pcs,q
assert len(E)==738 and len(audio)==692 and sum(n['tied']for n in E)==46 and D['duration']==108
assert sum(a['kind']=='subject'for a in anns)==6
ids={n['id']:n for n in E};seen=set();member={}
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 for nid in a['notes']:
  n=ids[nid];assert n['voice']==a['voice']and a['start']<=n['start']and n['start']+n['duration']<=a['end'];member[nid]=a['id']
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[]
for s in systems:
 for g in ET.fromstring(s['svg']).iter():
  nid=g.get('data-note-id')
  if not nid:continue
  printed.append(nid);assert s['start']<=ids[nid]['bar']<=s['end']
  assert g.get('data-annotation-id')==member.get(nid)
assert len(printed)==len(set(printed))==738 and set(printed)==set(ids)
print('BWV884: six entries, tonal answer, minor forms, two-part countersubject and triple counterpoint, continuous soprano run, closing appoggiatura, fourteen harmonic anchors, 738 notes/46 ties verified.')
