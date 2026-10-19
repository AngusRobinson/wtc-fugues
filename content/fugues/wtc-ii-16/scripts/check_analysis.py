from pathlib import Path
import json,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return sorted([n for n in E if n['voice']==v and a<=n['start']<b and not n['tied']],key=lambda n:n['start'])
s=ns(2,1,13.25);assert len(s)==18
for v,start,tr,first in [(1,13,7,5),(0,25,12,12),(3,37,-5,-7)]:
 z=ns(v,start,start+12.25);assert len(z)==18
 assert [b['pitch']-a['pitch']for a,b in zip(s,z)]==[first]+[tr]*17
 assert all(b['start']-a['start']==start-1 and b['duration']==a['duration']for a,b in zip(s,z))
# The added tenor entry retains the autograph tie between bars 23 and 24.
z=ns(2,58,70.25);assert len(z)==17
assert [(n['start']-57,n['pitch'])for n in z]==[(n['start'],n['pitch'])for n in s if n['start']!=12]
assert next(n for n in E if n['voice']==2 and n['start']==69)['tied']
# Compare complete sequential bodies, not just labels: S has six attacks, CS sixteen.
s0=ns(0,27,33);c0=ns(1,27,33);assert len(s0)==6 and len(c0)==16
for sv,cv,q,sd,cd,interval in [(3,0,39,-10,4,8),(1,0,84,-3,8,12),(3,0,108,-8,8,10)]:
 for original,v,shift in [(s0,sv,sd),(c0,cv,cd)]:
  z=ns(v,q,q+6);assert len(z)==len(original)
  assert all(b['diatonic']-a['diatonic']==shift and b['start']-a['start']==q-27 and b['duration']==a['duration']for a,b in zip(original,z))
 # Reduce compound inversion intervals to octave, tenth or twelfth.
 assert (cd-sd-(interval-1))%7==0
for a,b,v,w,steps in [(133,144,1,2,2),(151,162,0,1,5),(175,186,2,3,2),(175.25,183,0,1,2)]:
 x=ns(v,a,b);y=ns(w,a,b);assert len(x)==len(y)
 assert all(xx['diatonic']-yy['diatonic']==steps and xx['start']==yy['start']and xx['duration']==yy['duration']for xx,yy in zip(x,y))
# The return begins with a subject-head sequence, not a full stretto statement.
z=ns(2,199,207);assert len(z)==8
assert [(n['start']-198,n['pitch'])for n in z]==[(n['start'],n['pitch'])for n in s[:8]]
assert next(a for a in anns if a['voice']==2 and a['start']==199)['status']=='fragment'
# Final bass entry: repeated D instead of the first B-flat, semiquaver expansions.
z=ns(3,235,247.5)
assert [(n['start'],n['pitch'])for n in z[:4]]==[(235,50),(236.5,50),(237,51),(238,48)]
assert [(n['start'],n['pitch'])for n in ns(3,239,240)]==[(239.25,45),(239.5,47),(239.75,48)]
assert [(n['start'],n['pitch'])for n in ns(3,242,243)]==[(242.25,43),(242.5,45),(242.75,47)]
for a in anns:
 if a['kind']!='motif':continue
 z=sorted([n for n in E if n['id']in a['notes']],key=lambda n:n['start']);want=[0,1,2,3,2]if a['label']=='a'else[0,-1,0,-1,-2,-3,-2,-3,-4,-5,-4,-5]
 assert [n['diatonic']-z[0]['diatonic']for n in z]==want
for q,pcs in [(25,{2,5}),(37,{2,7,10}),(49,{2,5}),(70,{7,10}),(73,{2,5,9}),(76,{0,3}),(82,{2,5,9}),(94.5,{2,5,10}),(105.5,{2,5,10}),(118,{5,9}),(132.5,{0,3}),(145,{5,9}),(151,{0,3,7}),(166,{0,3,7}),(187,{3,7,10}),(189,{0,3,7}),(196,{2,7,10}),(198,{2,6,9}),(206,{7,10}),(209,{5,9}),(212,{3,7}),(218,{2,7,10}),(222,{2,7,10}),(235,{2,6}),(238,{0,3,7}),(249.5,{2,7,11})]:
 assert {n['pitch']%12 for n in audio if n['start']<=q<n['start']+n['duration']}==pcs,q
assert not any(n['voice']==2 and 81.25<=n['start']<105 for n in E)
assert len(E)==1735 and len(audio)==1659 and sum(n['tied']for n in E)==76 and D['duration']==252
assert sum(a['kind']=='subject'for a in anns)==17
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
assert len(printed)==len(set(printed))==1735 and set(printed)==set(ids)
print('BWV885: tonal answer, octave/tenth/twelfth inversion, thirds/sixths, both themes doubled, tied tenor ending, sequential return, final varied bass entry, twenty-six harmonic anchors and 1735 notes/76 ties verified.')
