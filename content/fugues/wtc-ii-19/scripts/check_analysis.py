from pathlib import Path
import json,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations'];notes={n['id']:n for n in E}
def ns(v,a,b,src=audio):return sorted([n for n in src if n['voice']==v and a<=n['start']<b and not n.get('tied')],key=lambda n:n['start'])
x=ns(2,.5,6.5);assert len(x)==19
for v,a,b,shift in [(1,6.5,12.25,7),(0,16.5,22.25,12),(2,24.5,30.25,-5)]:
 z=ns(v,a,b);assert len(z)==19
 assert all(n['pitch']-m['pitch']==shift and n['start']-m['start']==a-.5 for m,n in zip(x,z))
 assert all(n['duration']==m['duration']for m,n in zip(x[:-1],z[:-1]))
for v,a,b,shift,alter in [(0,34.5,42,5,None),(1,44.5,50.75,2,None),(2,60.5,66.25,-7,13),(0,76.5,84,10,13),(1,90.5,96.25,4,5),(0,106.5,112.75,7,13)]:
 z=ns(v,a,b);assert len(z)==19
 assert all(notes[n['id']]['diatonic']-notes[m['id']]['diatonic']==shift and n['start']-m['start']==a-.5 for m,n in zip(x,z))
 extra=ns(v,a-.25,a);assert len(extra)==1 and extra[0]['duration']==.25
 if alter is not None:
  steps=[n['pitch']-m['pitch']for m,n in zip(x,z)];base=steps[0];assert steps[alter]==base+(-1 if alter==5 else 1)
assert next(n for n in E if n['voice']==2 and n['start']==60)['pitch']==33
for a in anns:
 if a['label']in ['t','ti']:
  z=[notes[n]for n in a['notes']];assert len(z)==8 and all(n['duration']==.25 for n in z)
  assert [n['diatonic']-z[0]['diatonic']for n in z]==([0,2,1,0,1,-2,-1,0]if a['label']=='t'else[0,-2,-1,0,-1,2,1,0])
for q,pcs in [(12, {8, 4}), (16.5, {9, 4, 1}), (22, {1, 9}), (24, {8, 11, 4}), (35, {1, 9, 6}), (40, {9, 6}), (45, {8, 1, 4}), (50.5, {1, 4}), (56, {2, 11}), (60, {1, 9}), (67, {9, 2, 6}), (72, {2, 11, 6}), (77, {9, 2, 6}), (90.5, {8, 4}), (98, {8, 4}), (100, {1, 9}), (104, {2, 6}), (107, {9, 4, 1}), (112, {1, 9}), (114, {9, 1})]:
 assert {n['pitch']%12 for n in audio if n['start']<=q<n['start']+n['duration']}==pcs,q
assert len(E)==806 and len(audio)==754 and sum(n['tied']for n in E)==52 and D['duration']==116
assert sum(a['kind']=='subject'for a in anns)==10
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
assert len(printed)==len(set(printed))==806 and set(printed)==set(notes)
print('BWV888: real answer, ten entries, six extended upbeats, chromatic variants, direct/inverted tail figures, twenty harmonic arrivals and 806 notes/52 ties verified.')
