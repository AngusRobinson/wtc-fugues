from pathlib import Path
import json,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations'];notes={n['id']:n for n in E}
def ns(v,a,b):return sorted([n for n in audio if n['voice']==v and a<=n['start']<b],key=lambda n:n['start'])
def rel(z):return [n['start']-z[0]['start']for n in z]
def dia(z):return [notes[n['id']]['diatonic']for n in z]
x=ns(2,1,10.5);assert [n['pitch']for n in x]==[64,60,65,56,62,59,64,60,57,54,63,52]
assert rel(x)==[0,1,2,3,5.5,6,6.5,7,7.5,8,8.5,9]
# Tonal answer: first note a fourth above; subsequent notes a fifth above.
a=ns(1,9,16.5);assert len(a)==8
assert [n['pitch']-m['pitch']for m,n in zip(x,a)]==[5]+[7]*7
assert rel(a)==rel(x)[:8]
z=ns(0,21,28.5);assert len(z)==8 and [n['pitch']-m['pitch']for m,n in zip(x,z)]==[12]*8
# All later statements have abbreviated or altered endings, as Keller observes.
expected=[(2,35,42.75,[55,53,52,57,47,53,50,55,52]),(0,49,58.5,[81,79,84,75,81,78,83,79,76,73,81,77]),(1,65.5,72.5,[62,60,65,56,62,59,64,60]),(0,81,88.5,[81,77,82,73,79,76,81,77]),(2,99,108,[52,50,48,53,44,50,47,52,48,45,40,43])]
for v,a,b,pitches in expected:assert [n['pitch']for n in ns(v,a,b)]==pitches
# Main countersubject and its transpositions; C-major variant uses the same diatonic shape.
c=ns(2,10.5,16.5);assert len(c)==28
for v,a,b,shift in [(1,22.5,28.5,5),(1,50.5,56.5,12),(2,66.5,72.75,-7)]:
 z=ns(v,a,b);assert len(z)==28 and rel(z)==rel(c)
 assert all(n['pitch']-m['pitch']==shift for m,n in zip(c,z))
 assert [n['duration']for n in z[:-1]]==[n['duration']for n in c[:-1]]
z=ns(0,36.5,43);assert len(z)==28 and rel(z)==rel(c)
assert [b-a for a,b in zip(dia(c),dia(z))]==[12]*28
# At 21 the head changes; the remainder is a strict transposition from bar 22.
z=ns(2,84,88);tail=ns(2,12,16);assert len(z)==len(tail)==18
assert all(n['pitch']-m['pitch']==-2 and n['start']-m['start']==72 and n['duration']==m['duration']for m,n in zip(tail,z))
# Second countersubject: original and literal transposition, then labelled variants.
c2=ns(2,24.5,28.5);assert [n['pitch']for n in c2]==[53,47,50,44,47,52,45]
z=ns(2,52.5,56.5);assert rel(z)==rel(c2)
assert all(n['pitch']-m['pitch']==7 and n['duration']==m['duration']for m,n in zip(c2,z))
for v,a,b,shift,count in [(1,38.5,43,9,5),(0,68.5,72.5,14,5),(1,84.5,88.5,10,4)]:
 z=ns(v,a,b);assert [b-a for a,b in zip(dia(c2)[:count],dia(z)[:count])]==[shift]*count
assert ns(1,84.5,88.5)[4]['pitch']==76 # octave displacement, E5
# Five actual combinations, four vertical dispositions: subject/CS1/CS2.
combinations=[(26.5,(0,1,2)),(40.5,(2,0,1)),(54.5,(0,1,2)),(70.5,(1,2,0)),(86.5,(0,2,1))]
for q,voices in combinations:
 for kind,v in zip(['subject','cs1','cs2'],voices):
  assert any(a['kind']==kind and a['voice']==v and a['start']<=q<a['end']for a in anns)
assert len({v for q,v in combinations})==4
# Canon at the lower fifth, with the first phrase's final note adjusted.
for a,b,end1,end2 in [(72.5,74.5,74.5,76.5),(76.25,78.25,78.5,80.25)]:
 x=ns(0,a,end1);y=ns(1,b,end2);assert len(x)==len(y)
 assert all(n['start']-m['start']==2 for m,n in zip(x,y))
 assert [n['pitch']-m['pitch']for m,n in zip(x,y)]==([-7]*8+[-6]if a==72.5 else[-7]*8)
for ann in anns:
 if ann['label']=='q':
  z=[notes[n]for n in ann['notes']];assert len(z)==4 and all(n['duration']==.5 for n in z)
  assert[n['diatonic']-z[0]['diatonic']for n in z]in [[0,-2,1,-1],[0,-2,-4,1]]
for q,pcs in [(10, {4, 7}), (16, {4, 7}), (20.5, {0, 9}), (28, {0, 9}), (36, {0, 4}), (42, {0, 4, 7}), (48, {0, 9}), (56, {4, 7}), (58, {2, 5}), (63, {0, 9}), (70, {8, 4}), (72.5, {9, 4}), (74, {2, 5}), (76, {11, 7}), (78, {0, 4}), (80, {9, 5}), (81, {9, 2}), (88, {9, 2, 5}), (92, {0, 4, 7}), (96, {0, 9}), (99, {8, 11, 4}), (100, {0, 9, 4}), (106, {0, 9}), (110, {9, 4, 1})]:
 assert {n['pitch']%12 for n in audio if n['start']<=q<n['start']+n['duration']}==pcs,q
# Keller's major close is editorial. The historical source remains unchanged.
assert '2e; 2c;'in(R/'sources/bwv889.krn').read_text()
assert sorted(n['pitch']for n in audio if n['start']==110)==[33,45,61,64,69]
assert len(E)==762 and len(audio)==733 and sum(n['tied']for n in E)==29 and D['duration']==112
assert sum(a['kind']=='subject'for a in anns)==8
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
assert len(printed)==len(set(printed))==762 and set(printed)==set(notes)
print('BWV889: tonal answer, eight varied subject entries, both countersubjects, five triple-counterpoint combinations/four dispositions, canon, 23 harmonic arrivals plus entry context, editorial major close and 762 notes/29 ties verified.')
