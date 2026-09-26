"""Check the answer, canonic combinations, augmentation, shared notes and tonal anchors."""
from pathlib import Path
import json,re,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];A=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations'];ids={n['id']:n for n in E}
def ns(v,a,b):return [{**n,'diatonic':ids[n['id']]['diatonic']} for n in A if n['voice']==v and a<=n['start']<b]
def sounding(q):return {n['pitch']%12 for n in A if n['start']<=q<n['start']+n['duration']}
s=ns(1,0,11.5);a=ns(0,10,20.5)
assert [n['pitch'] for n in s]==[63,70,71,70,68,66,68,70,63,68,66,65,63]
assert [b['pitch']-a['pitch'] for a,b in zip(s,a)]==[7,5,7,7,7,7,7,7,7,7,7,7,7]
assert [(n['start'],n['duration']) for n in s[:-1]]==[(n['start']-10,n['duration']) for n in a[:-1]]
# First stretto: exact octave canon until the final-note variants.
x=ns(1,74,84);y=ns(0,76,86)
assert len(x)==len(y) and all(b['pitch']-a['pitch']==12 for a,b in zip(x,y))
assert [(n['start']-74,n['duration']) for n in x]==[(n['start']-76,n['duration']) for n in y]
# Its inversion in double counterpoint at the twelfth: +9 and -2 diatonic steps.
for v,a,b,w,c,d,delta in [(1,75,81,0,105,111,9),(0,77,83,1,107,113,-2)]:
 x=ns(v,a,b);y=ns(w,c,d);assert len(x)==len(y)
 assert all(q['diatonic']-p['diatonic']==delta for p,q in zip(x,y))
 assert [(n['start']-a,n['duration']) for n in x]==[(n['start']-c,n['duration']) for n in y]
# Augmentation doubles every internal duration; the last note can start a new entry.
for v,q in [(2,244),(1,266),(0,306)]:
 x=ns(v,q,q+20)
 assert len(x)==12 and [(n['start']-q,n['duration']) for n in x]==[(2*n['start'],2*n['duration']) for n in s[:-1]]
 assert ns(v,q+20,q+20.1), 'Final note is present'
# Inversion of normal and augmented forms: down a sixth/up a seventh = twelfth.
for v,a,b,w,c,d,delta in [(1,243,251,2,265,273,-5),(2,246,264,1,268,286,6)]:
 x=ns(v,a,b);y=ns(w,c,d);assert len(x)==len(y)
 assert all(q['diatonic']-p['diatonic']==delta for p,q in zip(x,y))
 assert [(n['start']-a,n['duration']) for n in x]==[(n['start']-c,n['duration']) for n in y]
# Tied-in structural beginnings are still ties, not new sounding attacks.
for v,q in [(0,104),(0,224),(2,304)]:assert any(n['voice']==v and n['start']==q and n['tied'] for n in E)
assert len([a for a in anns if a['kind']=='subject'])==23
assert len([a for a in anns if a['kind']=='augmentation'])==6
assert [(a['voice'],a['start']) for a in anns if a['kind']=='motif' and a['start']>=204]==[(2,204),(1,205),(0,206),(2,212),(1,213),(0,214)]
assert [(a['voice'],a['start']) for a in anns if a['start'] in [304,305,306]]==[(2,304),(1,305),(0,306)]
assert not any(a['kind'].startswith('cs') for a in anns)
for q,pc in [(20,{10}),(38,{3,6}),(44,{2,10}),(74,{10}),(116,{6}),(136,{8,11}),(152,{3,6}),(184,{3,8,11}),(204,{2,10}),(242,{2,5,10}),(264,{8,11}),(274,{6,10}),(284,{8,11}),(304.5,{2,5,10}),(340,{3,6,10}),(346,{3,7})]:assert sounding(q)==pc,(q,sounding(q))
assert len(E)==1484 and len(A)==1385 and sum(n['tied'] for n in E)==99 and D['duration']==348
seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end'] for n in a['notes'])
# Both overlapping augmentation closures remain coloured as the next normal entry.
for v,q in [(2,264),(1,286)]:
 n=next(n for n in E if n['voice']==v and n['start']==q)
 assert any(a['kind']=='subject' and n['id'] in a['notes'] for a in anns)
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==len(E) and set(printed)==set(ids)
for ex in json.loads((R/'data/thematic-examples.json').read_text()):
 root=ET.fromstring(ex['svg'])
 for g in root.iter():
  if g.get('class')=='beam':assert len([n for n in g.iter() if 'note' in n.get('class','').split()])>=2,'Orphan example beam'
print('BWV853: tonal answer,octave canon,two twelfth-inversions,three full augmentations,six head entries,three tied-in openings,16harmonic anchors,1484notes/99ties checked.')
