from pathlib import Path
import json,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations'];notes={n['id']:n for n in E}
def ns(v,a,b):return sorted([n for n in audio if n['voice']==v and a<=n['start']<b],key=lambda n:n['start'])
def dia(z):return [notes[n['id']]['diatonic']for n in z]
x=ns(3,0,13);assert[n['pitch']for n in x]==[47,51,56,52,49,58,59]
for v,a,shift in [(2,16,7),(1,36,12),(0,52,19),(3,72,0),(2,104,7),(1,136,12),(0,164,19),(2,208,5),(3,296,0),(2,336,7),(0,368,24)]:
 y=ns(v,a,a+13);assert len(y)==7 and[n['pitch']-m['pitch']for m,n in zip(x,y)]==[shift]*7
 assert[n['start']-m['start']for m,n in zip(x,y)]==[a]*7
for v,a,shift in [(3,188,-2),(2,236,5)]:
 y=ns(v,a,a+12.5);assert len(y)==7 and[b-a for a,b in zip(dia(x),dia(y))]==[shift]*7
base=ns(3,16,29);assert len(base)==16
z=ns(1,52,65);assert[n['pitch']-m['pitch']for m,n in zip(base,z)]==[12]*16
z=ns(2,36,49);assert[n['pitch']-m['pitch']for m,n in zip(base,z)]==[3,7]+[5]*14
y=ns(0,72,85);assert[n['pitch']-m['pitch']for m,n in zip(z,y)]==[12]*16
base=ns(0,109,116)
assert len(base)==13 and[d-dia(base)[0]for d in dia(base)]==[0,-1,-2,-1,0,-2,-4,-3,-2,-4,-6,-5,-4]
for v,a in [(3,121),(0,129),(3,141),(1,169),(0,193),(1,213),(0,239),(1,341),(2,373)]:
 z=ns(v,a,a+7);assert len(z)==13 and[d-dia(z)[0]for d in dia(z)]==[0,-1,-2,-1,0,-2,-4,-3,-2,-4,-6,-5,-4],(v,a)
 assert[n['start']-m['start']for m,n in zip(base,z)]==[a-109]*13
# Double counterpoint at the twelfth, using the 27/28 and42/43 combinations.
a=ns(2,104,117);b=ns(0,164,177);c=ns(1,169,176)
assert[b-a for a,b in zip(dia(a),dia(b))]==[7]*7
assert[b-a for a,b in zip(dia(base),dia(c))]==[-4]*13
assert 7-(-4)==11
# At35/36 the same inversion includes an additional octave displacement.
c=ns(3,141,148);assert[b-a for a,b in zip(dia(base),dia(c))]==[-15]*13
assert 3-(-15)-7==11
# S2 at60 begins3q after S1, instead of5q. No S2 statement accompanies75.
assert any(a['kind']=='cs2'and a['start']==239 for a in anns)
assert not any(a['kind']=='cs2'and 296<=a['start']<310 for a in anns)
assert sum(a['kind']=='subject'for a in anns)==14
for a in anns:
 if a['kind']=='motif':
  z=[notes[n]for n in a['notes']];pat=[n['diatonic']-z[0]['diatonic']for n in z]
  assert pat in {'q':[[0,-1,-2,-1,0,-2]],'r':[[0,1,2,0],[0,-1,-2,0]],'o':[[0,-1,0,-1]]}[a['label']]
for q,pcs in [(28, {10, 6}), (52, {3, 11, 6}), (68, {10, 6}), (88, {8, 3, 11}), (104, {10, 6}), (129, {3, 11}), (137, {3, 11}), (165, {1, 10, 6}), (189, {8, 3, 11}), (201, {8, 3, 11}), (209, {8, 11, 4}), (223, {1, 4}), (236, {8, 4}), (248, {8, 3, 11}), (269, {8, 11}), (281, {10, 6}), (296.5, {3, 11, 6}), (308, {3, 11, 6}), (312, {8, 3, 11}), (349, {10, 6}), (359, {8, 1, 4}), (367, {3, 11, 6}), (370, {8, 3, 11}), (381, {3, 11}), (404, {1, 10, 6}), (412, {3, 11, 6})]:
 assert{n['pitch']%12 for n in audio if n['start']<=q<n['start']+n['duration']}==pcs,q
assert len(E)==1466 and len(audio)==1319 and sum(n['tied']for n in E)==147 and D['duration']==416
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
assert len(printed)==len(set(printed))==1466 and set(printed)==set(notes)
print('BWV892: real answer, fourteen first-subject entries, exposition countersubject, second-subject variants, twelfth inversion, displaced combination,26 harmonic anchors and1466 notes/147 ties verified.')
