from pathlib import Path
import json,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations'];notes={n['id']:n for n in E}
def ns(v,a,b,src=E):return sorted([n for n in src if n['voice']==v and a<=n['start']<b and not n.get('tied')],key=lambda n:n['start'])
s=ns(1,.5,8.25);assert len(s)==20 and s[5]['pitch']==73
for v,start,end,shifts in [(0,8.5,16.25,[5]+[7]*19),(2,20.5,28.25,[-12]*20),(1,62.5,71,[-7]+[-5]*19),(2,70.5,78.5,[-12]*20),(0,84.5,92.5,[0]*20)]:
 z=ns(v,start,end);assert len(z)==20 and [b['pitch']-a['pitch']for a,b in zip(s,z)]==shifts
 assert all(b['start']-a['start']==start-.5 for a,b in zip(s,z))
# Twelfth inversion changes the sixth subject attack to D natural.
z=ns(3,50.5,58.5);assert z[5]['pitch']==50 and [n['pitch']for n in ns(2,51,56.5)]==[63,62,61,60,59,58]
x=ns(2,124.5,132.25);y=ns(0,136.5,145);assert len(x)==len(y)==20
assert all(b['pitch']-a['pitch']==19 and b['start']-a['start']==12 for a,b in zip(x[:-1],y[:-1]))
# Fourteenth: subject rises an octave, countersubject descends a seventh.
for v,a,b,bv,ba,bb,shift in [(0,86,89,2,22,25,7),(2,86,89,1,22,25,-6)]:
 x=ns(bv,ba,bb);y=ns(v,a,b);assert len(x)==len(y)
 assert all(n['diatonic']-m['diatonic']==shift and n['start']-m['start']==64 and n['duration']==m['duration']for m,n in zip(x,y))
assert 7-(-6)==13
x=ns(1,128,130);y=ns(0,128,130);assert len(x)==len(y)==8
assert all(b['diatonic']-a['diatonic']==2 and a['start']==b['start']and a['duration']==b['duration']for a,b in zip(x,y))
# Four episodic dispositions, comparing whole melodic cells and merged ties.
for bv,ba,bb,tests in [(1,37,42,[(3,107,112,-9),(0,113,118,1),(1,119,124,-3)]),(2,37.5,40.5,[(1,107.5,110.5,-2),(3,113.5,116.5,-6),(0,119.5,122.5,4)])]:
 x=ns(bv,ba,bb,audio)
 for v,a,b,shift in tests:
  y=ns(v,a,b,audio);assert len(x)==len(y)
  for m,n in zip(x,y):assert n['start']-m['start']==a-ba and n['duration']==m['duration']and notes[n['id']]['diatonic']-notes[m['id']]['diatonic']==shift
for v,q in [(3,36),(0,106),(1,112),(3,118)]:
 z=ns(v,q+.25,q+2);assert len(z)==7
 assert [n['diatonic']-z[0]['diatonic']for n in z]==[0,1,2,3,2,1,3]
assert not any(a['kind']=='cs1'and(a['start']<=64<a['end']or a['start']<=128<a['end'])for a in anns)
assert next(a for a in anns if a['kind']=='subject'and a['start']==166.5)['start']-160.5==6
z=next(a for a in anns if a['kind']=='subject'and a['start']==190.5);zz=sorted([notes[n]for n in z['notes']if not notes[n]['tied']],key=lambda n:n['start']);assert len(zz)==20
assert [n['pitch']-m['pitch']for m,n in zip(s,zz)]==[-14]+[-12]*19
cs=next(a for a in anns if a['kind']=='cs1'and a['start']==191);assert [notes[n]['pitch']for n in cs['notes']]==[56,55,54,53,52,51,51]
for q,pcs in [(16,{3,7}),(28,{0,3,8}),(36,{3,7}),(43,{0,8}),(48,{1,5}),(51,{0,3,8}),(62,{5,8}),(85,{0,8}),(93,{1,5,8}),(100,{3,5,8}),(106,{0,3}),(112,{5,8}),(118,{1,10}),(124,{3,6,10}),(137,{1,10}),(146,{1,5,8}),(166.5,{0,3,8}),(170,{3,7,10,1}),(182,{3,7,10,1}),(184,{0,8}),(190,{0,5,8}),(198,{0,3,8})]:
 assert {n['pitch']%12 for n in audio if n['start']<=q<n['start']+n['duration']}==pcs,q
assert len(E)==1407 and len(audio)==1346 and sum(n['tied']for n in E)==61 and D['duration']==200
assert sum(a['kind']=='subject'for a in anns)==15
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
assert len(printed)==len(set(printed))==1407 and set(printed)==set(notes)
print('BWV886: tonal answer, two subjects, semiquaver countersubject, four episodic permutations, fourteenth inversion, thirds, real minor-mode answer, stretto, five-part coda, twenty-two harmonic anchors and 1407 notes/61 ties verified.')
