"""Independent checks of the answer, entry variants, counterpoint and harmonic arrivals."""
from pathlib import Path
import json,re,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];A=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations'];byid={n['id']:n for n in E}
def notes(v,a,b):return [n for n in E if n['voice']==v and a<=n['start']<b]
def sounding(q):return {n['pitch']%12 for n in A if n['start']<=q<n['start']+n['duration']}
s=notes(0,0,6.25);a=notes(1,8,14.25)
assert len(s)==len(a)==16
assert [n['pitch'] for n in s]==[70,67,65,67,63,68,67,68,72,70,69,65,75,74,72,70]
assert [y['pitch']-x['pitch'] for x,y in zip(s,a)]==[-7]+[-5]*9+[-7]*6
assert [(n['start'],n['duration']) for n in s]==[(n['start']-8,n['duration']) for n in a]
# Exact rhythmic and diatonic permutation of all three episodic lines.
for v,w in [(0,1),(1,2),(2,0)]:
 for a,b in [(28,48),(32,52)]:
  x=notes(v,a,a+4);y=notes(w,b,b+4);assert len(x)==len(y)
  assert [(n['start']-a,n['duration']) for n in x]==[(n['start']-b,n['duration']) for n in y]
  ds=[q['diatonic']-p['diatonic'] for p,q in zip(x,y)]
  assert ds==([10]*10+[9] if v==2 and a==32 else ([10]*len(x) if v==2 else [-11]*len(x)))
entries=[a for a in anns if a['kind']=='subject'];assert len(entries)==9
assert [(a['voice'],a['start']) for a in entries]==[(0,0),(1,8),(2,20),(0,40),(1,66),(2,78),(2,100),(0,112),(1,132)]
assert all(a['end']<=b['start'] for a,b in zip(entries,entries[1:])), 'No stretto'
assert len([a for a in anns if a['kind']=='cs1'])==7
assert not any(a['kind']=='cs1' and a['start']>=132 for a in anns), 'Final answer has no countersubject'
assert notes(0,112,112.25)[0]['pitch']==68 and [n['pitch'] for n in notes(0,112.25,118.5)]==[n['pitch'] for n in s[1:]], 'Opening A-flat, then the original subject'
assert notes(1,134,134.5)[0]['pitch']==66, 'G-flat in final answer'
for q,pc in [(6,{10}),(14,{3,7}),(26,{2,10}),(46,{3,7}),(66,{0}),(72,{0,3}),(84,{7,10}),(92,{3,7}),(106,{3,7}),(118,{2,10}),(138,{0,3}),(146,{3,7,10})]:assert sounding(q)==pc,(q,sounding(q))
assert len(E)==938 and len(A)==900 and sum(n['tied'] for n in E)==38 and D['duration']==148
assert [n['pitch'] for n in notes(0,144.25,148)]==[61,60,59,58], 'D-flat/C/C-flat/B-flat final inner descent'
seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(byid[n]['voice']==a['voice'] and a['start']<=byid[n]['start'] and byid[n]['start']+byid[n]['duration']<=a['end'] for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==len(E) and set(printed)==set(byid)
for ex in json.loads((R/'data/thematic-examples.json').read_text()):
 root=ET.fromstring(ex['svg'])
 for g in root.iter():
  if g.get('class')=='beam':assert len([n for n in g.iter() if 'note' in n.get('class','').split()])>=2,'Orphan example beam'
print('BWV852: tonal answer mutations,nine entries,seven countersubjects,two-bar triple-counterpoint permutation,mid-bar entries,12arrivals,938notes and38ties checked.')
