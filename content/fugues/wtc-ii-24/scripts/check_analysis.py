from pathlib import Path
import json,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations'];notes={n['id']:n for n in E}
def ns(v,a,b):return sorted([n for n in audio if n['voice']==v and a<=n['start']<b],key=lambda n:n['start'])
def dia(z):return [notes[n['id']]['diatonic']for n in z]
x=ns(1,0,8.25)
assert [n['pitch']for n in x]==[66,62,59,58,59,61,62,64,66,67,55,67,66,54,66,64,66,64,62,61,62]
# The first answer changes the upbeat to the tonic; later answers are real.
for v,a,b,shifts in [(0,9,17.25,[5]+[7]*20),(2,22.5,30.75,[-12]*9+[-11]*3+[-12]*9),(1,39,47.5,[-5]*21),(1,81,90.5,[7]*6+[8]+[7]*14),(0,121.5,130,[12]*21)]:
 z=ns(v,a,b);assert len(z)==21,(v,a,len(z));assert[n['pitch']-m['pitch']for m,n in zip(x,z)]==shifts,(v,a)
 assert[n['start']-m['start']for m,n in zip(x,z)]==[a]*21
for v,a,b,shift in [(0,52.5,60.75,9),(2,66,74.25,-8)]:
 z=ns(v,a,b);assert len(z)==21 and[b-a for a,b in zip(dia(x),dia(z))]==[shift]*21
 assert[n['start']-m['start']for m,n in zip(x,z)]==[a]*21
# The bass continues the E-minor subject without its normal upbeat at71.
z=ns(2,105.5,113.5);assert len(z)==20
assert[n['pitch']-m['pitch']for m,n in zip(x[1:],z)]==[-7]*20
assert[n['start']-m['start']for m,n in zip(x[1:],z)]==[105]*20
# Exposition countersubject: its latter part returns a fourth higher.
a=ns(1,11,17.5);b=ns(1,24.5,31);assert len(a)==len(b)==20
assert[n['pitch']-m['pitch']for m,n in zip(a,b)]==[5]*20
assert[n['start']-m['start']for m,n in zip(a,b)]==[13.5]*20
base=ns(2,42.75,47.25);assert len(base)==18
assert[n['pitch']for n in base]==[57,47,57,47,56,45,56,45,56,45,54,44,54,53,56,49,53,42]
for v,a,b,shifts in [(0,84.75,89.5,[24]*17+[36]),(0,108.75,113.25,[22]*17+[34])]:
 z=ns(v,a,b);assert len(z)==18 and[n['pitch']-m['pitch']for m,n in zip(base,z)]==shifts
 assert[n['start']-m['start']for m,n in zip(base,z)]==[a-42.75]*18
z=ns(1,56.25,60.75);assert[b-a for a,b in zip(dia(base),dia(z))]==[5]*9+[3]+[5]*7+[12]
z=ns(0,69.75,74.5);assert[b-a for a,b in zip(dia(base),dia(z))]==[9]*17+[16]
# The final CS2 passes from alto to bass, with one note doubled across the handover.
a=ns(1,125.25,128.5);b=ns(2,128,129.75)
assert[n['pitch']-m['pitch']for m,n in zip(base[:12],a)]==[17]*12
assert[n['pitch']-m['pitch']for m,n in zip(base[11:],b)]==[5]*7
# Incomplete closing stretto, with the bass passing-note and soprano ornament retained.
assert[n['pitch']for n in ns(1,144,146.25)]==[66,62,59,58,59]
assert[n['pitch']for n in ns(2,145.5,148)]==[54,52,50,47,46,47]
assert[n['pitch']for n in ns(0,147.25,150.5)]==[78,76,74,73,71,73,70,73,71]
# Kroll's two closing appoggiaturas, realised as quavers as permitted by Tovey.
assert[(n['pitch'],n['duration'])for n in ns(0,149,150.5)]==[(73,.5),(71,1)]
assert[(n['pitch'],n['duration'])for n in ns(1,149,150.5)]==[(64,.5),(63,1)]
assert sum(a['kind']=='subject'for a in anns)==13
for a in anns:
 if a['kind']=='motif':
  z=[notes[n]for n in a['notes']];pat=[n['diatonic']-z[0]['diatonic']for n in z]
  assert pat in {'t':[[0,1,1,0,1]],'r':[[0,7,1,7,2,7],[0,4,1,4,2,4]],'d':[[0,-1,-2,-3,-4,-5]],'h':[[0,-2,-3]]}[a['label']]
for q,pcs in [(17, {9, 6}), (23, {2, 11}), (30.5, {2, 11, 6}), (39.5, {1, 9, 6}), (47, {1, 9, 6}), (53, {2, 6}), (60.5, {2, 6}), (65, {8, 11, 4}), (66.5, {1, 9}), (74.5, {1, 4, 9}), (81.5, {1, 9, 6}), (89, {1, 9, 6}), (92.5, {11, 4, 7}), (95.5, {9, 2, 6}), (99.5, {2, 11, 6}), (102.5, {10, 4, 6}), (107, {4, 7}), (113, {11, 4, 7}), (116, {9, 2, 6}), (120.5, {10, 4, 6}), (122, {2, 11}), (143.5, {10, 6}), (144.5, {2, 11}), (149.5, {11, 3})]:
 assert{n['pitch']%12 for n in audio if n['start']<=q<n['start']+n['duration']}==pcs,q
assert len(E)==1038 and len(audio)==985 and sum(n['tied']for n in E)==53 and D['duration']==150.5
seen=set();member={}
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 for nid in a['notes']:
  n=notes[nid];assert n['voice']==a['voice']and a['start']<=n['start']and n['start']+n['duration']<=a['end'];member[nid]=a['id']
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[]
for s in systems:
 for g in ET.fromstring(s['svg']).iter():
  nid=g.get('data-note-id')
  if not nid:continue
  printed.append(nid);assert s['start']<=notes[nid]['bar']<=s['end']
  assert g.get('data-annotation-id')==member.get(nid)
assert len(printed)==len(set(printed))==1038 and set(printed)==set(notes)
print('BWV893: tonal and real answers, nine subject continuations, four incomplete entries, both countersubjects, final handover, closing appoggiaturas,24 tonal anchors and1038 notes/53 ties verified.')
