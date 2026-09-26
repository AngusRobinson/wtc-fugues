"""Check Keller's extended span, Prout's shorter answer, variants and episodic inversion."""
from pathlib import Path
import json,re,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];A=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations'];ids={n['id']:n for n in E}
def ns(v,a,b):return [n for n in E if n['voice']==v and a<=n['start']<b]
def sounding(q):return {n['pitch']%12 for n in A if n['start']<=q<n['start']+n['duration']}
s=ns(1,1.5,8.25);a=ns(0,5.5,12.25);assert len(s)==len(a)==22
assert [(n['start']-1.5,n['duration']) for n in s]==[(n['start']-5.5,n['duration']) for n in a]
assert [y['pitch']-x['pitch'] for x,y in zip(s,a)]==[7]*14+[6,7,7,7,6,7,7,6]
assert all(y['pitch']-x['pitch']==7 for x,y in zip(ns(1,1.5,6.25),ns(0,5.5,10.25))), 'Prout shorter subject has a real answer'
assert ns(1,8,8.25)[0]['pitch']==63 and ns(0,12,12.25)[0]['pitch']==69,'Keller extended ending has tonal alteration'
entries=[a for a in anns if a['kind']=='subject'];assert len(entries)==12
assert [(a['voice'],a['start']) for a in entries]==[(1,1.5),(0,5.5),(2,11.5),(0,23.5),(1,27.5),(2,35.5),(0,45),(1,61.5),(2,73.5),(0,76.25),(1,81.5),(0,97.5)]
assert any(n['voice']==0 and n['start']==45 and n['duration']==1.5 and n['pitch']==73 for n in A)
assert ns(0,46.5,47)[0]['duration']==.5,'Varied head rhythm at bar12 retained'
assert [n['pitch'] for n in ns(0,76.25,78)]==[59,61,63,64,66,68,64], 'Bar20 extended semiquaver approach retained'
# Two upper parts invert in double counterpoint at the fifteenth, transposed:
# old soprano falls a sixth, old alto rises a tenth (14 diatonic steps apart).
for v,a,b,w,c,d,delta in [(0,52,58,1,88,94,-5),(1,52,61.5,0,88,97.5,9)]:
 x=ns(v,a,b);y=ns(w,c,d);assert len(x)==len(y)
 assert [(n['start']-a,n['duration']) for n in x]==[(n['start']-c,n['duration']) for n in y]
 assert all(q['diatonic']-p['diatonic']==delta for p,q in zip(x,y))
# Fixed semiquaver continuation in its initial form and octave-transposed recurrence.
x=ns(1,6.25,9.25);y=ns(0,28.25,31.25)
assert len(x)==len(y)==12 and all(q['pitch']-p['pitch']==12 for p,q in zip(x,y))
assert [(n['start']-6.25,n['duration']) for n in x]==[(n['start']-28.25,n['duration']) for n in y]
assert [n['pitch'] for n in ns(2,104,108)]==[52,47,49,44,45,40,42,37], 'Bar27 leaping revision retained'
assert [n['pitch'] for n in ns(2,94,96)]==[57,56,54,52], 'Bar24 scalar version retained'
for q,pc in [(8,{3,11}),(18,{3,11}),(41,{1,4,8}),(49,{1,4}),(64,{1,4}),(73.5,{4,8,11}),(81,{3,11}),(97,{4,8,11}),(112,{4,8})]:assert sounding(q)==pc,(q,sounding(q))
assert len(E)==762 and len(A)==733 and sum(n['tied'] for n in E)==29 and D['duration']==116
seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end'] for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==len(E) and set(printed)==set(ids)
for ex in json.loads((R/'data/thematic-examples.json').read_text()):
 root=ET.fromstring(ex['svg'])
 for g in root.iter():
  if g.get('class')=='beam':assert len([n for n in g.iter() if 'note' in n.get('class','').split()])>=2,'Orphan example beam'
print('BWV854: both subject-boundary readings,real opening/tonal continuation,12entries,irregular rhythms,CS recurrence,double counterpoint at15th,nine arrivals,762notes/29ties checked.')
