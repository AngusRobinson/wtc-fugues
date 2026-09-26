"""Independent checks of the answer, entry variants, counterpoint and harmonic arrivals."""
from pathlib import Path
import json,re,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];A=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations'];byid={n['id']:n for n in E}
def notes(v,a,b):return [n for n in E if n['voice']==v and a<=n['start']<b]
def sounding(q):return {n['pitch']%12 for n in A if n['start']<=q<n['start']+n['duration']}
s=notes(0,.5,7);a=notes(1,6.5,13)
assert [n['pitch'] for n in s]==[62,64,65,67,64,65,62,61,62,70,67,69]
assert [y['pitch']-x['pitch'] for x,y in zip(s,a)]==[-5]*12
assert [(n['start']-.5,n['duration']) for n in s]==[(n['start']-6.5,n['duration']) for n in a]
assert [n['pitch'] for n in notes(0,7.75,9)][::-1]==[n['pitch'] for n in notes(0,.5,3)], 'Retrograde relationship of link and head'
assert [n['pitch']+5 for n in notes(0,7,9)]==[n['pitch'] for n in notes(0,16,18)]
assert [n['pitch']-7 for n in notes(0,9.5,12)]==[n['pitch'] for n in notes(1,18.5,21)], 'Divided countersubject continuation'
for v,q in [(1,39.5),(0,63.5),(2,66.5),(0,78.5),(2,84.5)]:
 ns=notes(v,q,q+2.5);assert len(ns)==5 and [n['diatonic']-ns[0]['diatonic'] for n in ns]==[0,-1,-2,-3,-1]
x=sorted((n['voice'],n['start']-48,n['duration'],n['pitch']+5) for n in E if 48.5<=n['start']<60)
y=sorted((n['voice'],n['start']-114,n['duration'],n['pitch']) for n in E if 114.5<=n['start']<126)
assert x==y, 'Closing stretti and cadences correspond at the fourth'
assert notes(2,117,117.25)[0]['pitch']==54, 'Bass F-sharp in bar40'
for q,pc in [(15,{2,5}),(60,{9}),(72,{2,5}),(81,{2,5}),(90.25,{7,10}),(99,{2,5,9}),(126,{2}),(129,{2,6,9})]:assert sounding(q)==pc,(q,sounding(q))
entries=[a for a in anns if a['kind']=='subject'];assert len(entries)==19
assert {(a['voice'],a['start']) for a in entries if a['inverted']}=={(1,39.5),(0,63.5),(2,66.5),(0,78.5),(2,84.5)}
assert {(a['voice'],a['start']) for a in entries if 'concealed' in a['name']}=={(2,30),(0,93)}
assert len(E)==747 and len(A)==718 and sum(n['tied'] for n in E)==29 and D['duration']==132
assert len(notes(0,126,129))==11 and len(notes(1,126,129))==10, 'Closing extra voices retained'
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
print('BWV851: real answer, divided countersubject, retrograde head, five inverted statements, concealed entries, transposed closing stretti, eight arrivals,747notes and29ties checked.')
