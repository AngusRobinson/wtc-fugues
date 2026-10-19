from pathlib import Path
import json,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations'];notes={n['id']:n for n in E}
def ns(v,a,b,src=E):return sorted([n for n in src if n['voice']==v and a<=n['start']<b and not n.get('tied')],key=lambda n:n['start'])
x=ns(0,0,12);assert len(x)==24
for v,a,shift in [(1,12,-5),(2,36,-12),(1,54,0),(2,96,-17),(0,132,7),(2,162,-24),(2,288,-24),(0,306,7),(1,372,-12),(0,402,0)]:
 z=ns(v,a,a+12);assert len(z)==24
 assert all(n['pitch']-m['pitch']==shift and n['start']-m['start']==a and n['duration']==m['duration']for m,n in zip(x,z)),a
z=ns(1,330,342);assert len(z)==24 and all(n['diatonic']-m['diatonic']==-2 for m,n in zip(x,z))
x=ns(0,181,193,audio);assert len(x)==12
for v,a,b,shift in [(1,196,208,-7),(2,211,223,-14),(1,289,300.5,-7),(1,307,318.5,-12),(0,331,343,1),(1,403,419,-7)]:
 z=ns(v,a,b,audio);assert len(z)==12
 assert all(n['pitch']-m['pitch']==shift and n['start']-m['start']==a-181 for m,n in zip(x,z))
 assert all(n['duration']==m['duration']for m,n in zip(x[:-1],z[:-1]))
z=ns(0,235,248.5,audio);assert len(z)==14 and all(n['pitch']-m['pitch']==5 and n['start']-m['start']==54 for m,n in zip(x[:11],z[:11]))
z=ns(2,373,383,audio);assert len(z)==11 and all(n['pitch']-m['pitch']==-31 and n['start']-m['start']==192 for m,n in zip(x,z))
x=ns(0,12,24.5,audio);y=ns(2,54,67.5,audio);assert len(x)==len(y)==9
assert all(n['pitch']-m['pitch']==-19 and n['start']-m['start']==42 for m,n in zip(x,y))
assert all(n['duration']==m['duration']for m,n in zip(x[:-1],y[:-1]))
# The two combined subjects invert at the octave across the register change.
for bv,a,b,v,c,d,shift in [(2,288,300,0,306,318,18),(1,289,300.5,1,307,318.5,-3)]:
 x=ns(bv,a,b);y=ns(v,c,d);assert len(x)==len(y)
 assert all(n['diatonic']-m['diatonic']==shift and n['start']-m['start']==18 for m,n in zip(x,y))
assert 18-(-3)==21
for q,pcs in [(24, {3, 6}), (37, {8, 3, 11}), (66, {8, 11}), (69, {8, 1, 4}), (96, {3, 6}), (108, {10, 6}), (114, {1, 4}), (120, {11, 3}), (144, {10, 3, 6}), (147, {1, 4}), (150, {11, 3}), (158, {8, 3, 11}), (162, {8, 11}), (180.5, {3, 7}), (207, {8, 11}), (225, {10, 4, 6}), (234.5, {8, 11}), (252, {10, 3, 6}), (255.5, {0, 8}), (258.5, {1, 5}), (261.5, {10, 6}), (264.5, {11, 3}), (276.5, {10, 3, 7}), (288, {8, 11}), (306, {3, 6}), (318, {3, 6}), (334.5, {8, 11, 4}), (342, {8, 4}), (348.5, {1, 4}), (366, {1, 3, 7}), (372, {8, 11}), (387, {8, 3, 11}), (393, {8, 11, 4}), (402, {8, 3, 11}), (414, {8, 11}), (426, {8})]:
 assert {n['pitch']%12 for n in audio if n['start']<=q<n['start']+n['duration']}==pcs,q
assert len(E)==1691 and len(audio)==1529 and sum(n['tied']for n in E)==162 and D['duration']==429
assert sum(a['kind']=='subject'for a in anns)==12
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
assert len(printed)==len(set(printed))==1691 and set(printed)==set(notes)
print('BWV887: twelve first-subject entries, real answer, second-subject variants, chromatic countersubject, octave inversion, thirty-six harmonic anchors and 1691 notes/162 ties verified.')
