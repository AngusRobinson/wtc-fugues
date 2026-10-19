from pathlib import Path
import json,re,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return sorted([n for n in E if n['voice']==v and a<=n['start']<b and not n['tied']],key=lambda n:n['start'])
s=ns(1,1.5,12.5);assert len(s)==15
z=ns(0,13.5,24.5);assert [b['pitch']-a['pitch']for a,b in zip(s,z)]==[5]+[7]*14
assert all(b['start']-a['start']==12 and b['duration']==a['duration']for a,b in zip(s,z))
for v,start,end,tr in [(2,31.5,43,-12),(0,61.5,73.5,12),(1,111.5,123.5,5),(1,203.5,215,5)]:
 z=ns(v,start,end);assert len(z)==15
 assert all(b['pitch']-a['pitch']==tr and b['start']-a['start']==start-1.5 for a,b in zip(s,z))
# The C-sharp-minor bass statement changes the cadential trill into D-sharp/G-sharp.
z=ns(2,133.5,145);assert len(z)==16
assert all(b['pitch']-a['pitch']==-5 and b['start']-a['start']==132 for a,b in zip(s[:14],z[:14]))
assert [(n['start'],n['pitch'])for n in z[-3:]]==[(142,51),(143,56),(144,49)]
# The first two triple combinations embed varied heads in semiquaver motion.
for v,start,end,body,tr in [(0,215.5,226.5,217,12),(2,237.5,248.25,239,-5)]:
 z=ns(v,body,end);assert len(z)==12
 assert all(b['pitch']-a['pitch']==tr and b['start']-a['start']==body-3 for a,b in zip(s[3:],z))
z=ns(0,263.5,274.75);assert len(z)==15
assert all(b['pitch']-a['pitch']==12 for a,b in zip(s,z))
assert all(b['start']-a['start']==262 for a,b in zip(s[:-1],z[:-1]));assert z[-1]['start']==274.25
# Inverted heads retain the tonal answer's third/second pattern.
heads=[a for a in anns if a['label']=='hi'];assert len(heads)>=6
for a in heads:
 z=ns(a['voice'],a['start'],a['end']);assert len(z)==3
 assert [z[i+1]['diatonic']-z[i]['diatonic']for i in [0,1]]in [[2,2],[1,2]]
# S2: distinguish complete six-note entries from the intervening imitations.
s2=ns(2,78.5,83);assert len(s2)==6
assert [n['start']-78.5 for n in s2]==[0,.5,1.25,1.5,2,2.5]
assert [n['duration']for n in s2]==[.5,.75,.25,.5,.5,2]
for v,start,tr in [(0,82.5,17),(1,86.5,10),(1,106.5,5),(1,220.5,12),(1,242.5,7),(2,268.5,0)]:
 z=ns(v,start,start+4.5);assert len(z)==6
 assert all(b['pitch']-a['pitch']==tr and b['start']-a['start']==start-78.5 for a,b in zip(s2,z))
z=ns(2,90.5,95);assert [b['pitch']-a['pitch']for a,b in zip(s2,z)]==[4,3,3,3,3,3]
z=ns(2,116.5,120.5);assert len(z)==6 and all(b['pitch']-a['pitch']==-7 for a,b in zip(s2,z))
assert len(ns(1,80.5,83.5))==4 and len(ns(1,84.5,86.5))==4
# S3's two-unit core, extended forms and exact diatonic inversion.
s3=ns(1,141.5,146.5);assert len(s3)==18
for v,start,tr in [(0,145.5,3),(2,149.5,-8)]:
 z=ns(v,start,start+5);assert len(z)==18
 assert all(b['diatonic']-a['diatonic']==tr and b['start']-a['start']==start-141.5 and b['duration']==a['duration']for a,b in zip(s3,z))
core=[0,1,0,-1,0,-1,-2,0]
for v,start,inv in [(1,142,False),(1,144,False),(0,188,True),(0,190,True),(2,230,True),(2,234,True),(0,240,False),(0,242,False),(0,244,False),(0,246,False),(1,266,False),(1,268,False),(1,270,False),(1,272,False)]:
 z=ns(v,start,start+2);assert len(z)==8 and all(n['duration']==.25 for n in z)
 assert [n['diatonic']-z[0]['diatonic']for n in z]==[(-1 if inv else 1)*n for n in core]
perms=[]
for q in [221,243,269]:
 parts=tuple(next(a['voice']for a in anns if a['kind']==k and a['start']<=q<a['end'])for k in ['subject','subject2','subject3'])
 assert len(set(parts))==3;perms.append(parts)
assert perms==[(0,1,2),(2,1,0),(0,2,1)]
assert {p.index(2)for p in perms}=={0,1,2}
for q,pcs in [(24,{1,4}),(32,{6,9}),(42,{6,9}),(54,{1,4,8}),(62,{6,9}),(78,{1,9}),(93,{1,4,9}),(109,{2,11}),(134,{1,4}),(144,{1,4}),(148,{6,9}),(152,{2,6,11}),(161,{1,4,8}),(170,{8,11}),(174,{4,8}),(192,{2,6,11}),(204,{2,11}),(213,{1,6,9}),(226,{6,9}),(233,{1,4}),(248,{1,4}),(253,{2,11}),(257,{1,9}),(261,{6,9}),(274.25,{6,9}),(278,{6})]:
 assert {n['pitch']%12 for n in audio if n['start']<=q<n['start']+n['duration']}==pcs,q
assert len(E)==1497 and len(audio)==1400 and sum(n['tied']for n in E)==97 and D['duration']==280
assert sum(a['kind']=='subject'for a in anns)==10
assert not any(a['kind']=='subject'and a['voice']==2 and 47<a['start']<61 for a in anns)
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
assert len(printed)==len(set(printed))==1497 and set(printed)==set(ids)
print('BWV883: tonal answer, ten S1 statements, S2 entries/fragments, S3 inversion, three triple-counterpoint dispositions, twenty-six harmonic anchors and 1497 notes/97 ties verified.')
