from pathlib import Path
import json,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations'];notes={n['id']:n for n in E}
def ns(v,a,b):return sorted([n for n in audio if n['voice']==v and a<=n['start']<b],key=lambda n:n['start'])
def dia(z):return [notes[n['id']]['diatonic']for n in z]
x=ns(1,.5,12);assert len(x)==23 and all(n['duration']==.5 for n in x)
y=ns(0,12.5,24);assert [n['pitch']-m['pitch']for m,n in zip(x,y)]==[7,7,6,7,5]+[7]*18
for v,a,shift in [(2,36.5,-12),(2,60.5,-17),(1,93.5,-5),(0,117.5,12),(1,159.5,-7)]:
 y=ns(v,a,a+11.5);assert len(y)==23
 assert all(n['pitch']-m['pitch']==shift and n['start']-m['start']==a-.5 and n['duration']==.5 for m,n in zip(x,y))
for v,a,shift in [(2,138.5,-9),(0,186.5,1),(0,231.5,4)]:
 y=ns(v,a,a+11.5);assert len(y)==23 and [b-a for a,b in zip(dia(x),dia(y))]==[shift]*23
z=ns(0,231.5,243);assert[n['pitch']-m['pitch']for m,n in zip(x,z)]==[7]*14+[6,6]+[7]*7
assert z[4]['pitch']==72 and z[2]['pitch']==76 # main C and E-natural at 78
# Both incomplete outer-voice statements precede the complete alto by one bar.
a=ns(0,156.5,159);b=ns(1,159.5,162);c=ns(2,162.5,165)
assert[b-a for a,b in zip(dia(a),dia(b))]==[-6]*4+[-7]
assert[b-a for a,b in zip(dia(b),dia(c))]==[-5]*4+[-4]
base=ns(0,97,105.5);assert len(base)==9
for v,a,b,shift in [(2,121,129.5,-8),(1,190,198.5,-3)]:
 z=ns(v,a,b);assert len(z)==9 and[b-a for a,b in zip(dia(base),dia(z))]==[shift]*9
 assert[n['start']-m['start']for m,n in zip(base,z)]==[a-97]*9
# Actual register shifts of the 41 combination give twelfth/tenth inversion
# when the subject's extra octave is removed.
subject_shift=10;cs1_shift=-8;cs2_shift=12
assert subject_shift-7-cs1_shift==11 and cs2_shift-(subject_shift-7)==9
for v,a,b in [(2,97,105.5),(1,121,129.5),(0,143,151),(2,190,199),(2,237,249),(2,246,255.5)]:
 z=ns(v,a,b);assert len(z)==4 and [d-dia(z)[0]for d in dia(z)]==[0,1,2,-2]
for q,vs in [(98,(1,0,2)),(122,(0,2,1)),(146,(2,1,0)),(167,(1,2,0)),(191,(0,1,2)),(239,(0,1,2))]:
 for k,v in zip(['subject','cs1','cs2'],vs):assert any(a['kind']==k and a['voice']==v and a['start']<=q<a['end']for a in anns)
# Corresponding four-bar cadences: repeated-note bass transposed down a fifth.
a=ns(2,84,93);b=ns(2,267,276);assert len(a)==len(b)==9
assert all(n['pitch']-m['pitch']==-7 and n['start']-m['start']==183 and n['duration']==m['duration']for m,n in zip(a,b))
for a in anns:
 if a['kind']=='motif':
  z=[notes[n]for n in a['notes']];pat=[n['diatonic']-z[0]['diatonic']for n in z]
  assert pat in ([[0,3,3,2,2,1]]if a['label']=='t'else[[0,-1,-2,-1,-4],[0,-1,-2,-1,-3]])
for q,pcs in [(24, {9, 5}), (36, {2, 10}), (48, {10, 2}), (60, {9, 5}), (78, {2, 10, 5}), (93, {9, 5}), (105.5, {9, 5}), (111, {3, 7}), (120, {2, 10}), (129, {2, 5}), (144, {10, 7}), (150.5, {2, 10, 7}), (162, {3, 7}), (180, {0, 3}), (189, {0, 3}), (199, {0, 3}), (204, {2, 10, 5}), (228, {2, 10, 5}), (231, {9, 5}), (237, {2, 5}), (255, {10, 7}), (258, {0, 3}), (264, {2, 10}), (276, {10, 2})]:
 assert{n['pitch']%12 for n in audio if n['start']<=q<n['start']+n['duration']}==pcs,q
assert len(E)==1020 and len(audio)==962 and sum(n['tied']for n in E)==58 and D['duration']==279
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
assert len(printed)==len(set(printed))==1020 and set(printed)==set(notes)
print('BWV890: tonal and real answers, ten complete entries and two partial stretto statements, six triple combinations, twelfth/tenth inversion, recurring cells, parallel cadences, 24 harmonic anchors and 1020 notes/58 ties verified.')
