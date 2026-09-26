"""Independent checks of the answer, entry variants, counterpoint and harmonic arrivals."""
from pathlib import Path
import json,re,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];A=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations'];byid={n['id']:n for n in E}
def notes(v,a,b):return [n for n in E if n['voice']==v and a<=n['start']<b]
def sounding(q):return {n['pitch']%12 for n in A if n['start']<=q<n['start']+n['duration']}
s=notes(3,1,4.75);a=notes(2,5,9)
assert len(s)==len(a)==13
assert [n['pitch'] for n in s]==[50,52,54,55,54,52,54,50,59,59,57,55,54]
assert [y['pitch']-x['pitch'] for x,y in zip(s,a)]==[7]*13
assert [n['start']-1 for n in s]==[n['start']-5 for n in a]
entries=[a for a in anns if a['kind']=='subject']
assert [(a['voice'],a['start']) for a in entries]==[(3,1),(2,5),(1,13),(0,17),(3,25),(0,29),(0,41),(1,45),(0,49),(2,53),(3,57)]
assert all(a['kind'] in ('subject','motif') for a in anns), 'No regular countersubject'
assert max(a['start'] for a in entries)==57, 'Last full subject in bar15'
assert [(a['voice'],a['start']) for a in anns if 76<=a['start']<80]==[(0,76),(1,77),(3,78),(2,79)]
assert [n['pitch'] for n in notes(3,48,49.75)]==[47,49,50,52,50,49,50,47,59], 'Retain the edition’s octave leap in bar13'
for q,pc in [(8,{9,1}),(20,{9,1}),(25,{2,6,9}),(32,{11,2}),(40,{7,11,2}),(57,{4,7,11}),(64,{4,7}),(80,{2,6}),(104,{2,6,9})]:assert sounding(q)==pc,(q,sounding(q))
assert len(E)==796 and len(A)==780 and sum(n['tied'] for n in E)==16 and D['duration']==108
assert all(n['start']==104 and n['duration']==4 for n in E if n['bar']==27), 'Whole-bar closing chord'
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
print('BWV850: real answer,11complete entries,head imitation,9tonal arrivals,retained bar13 octave,796notes and16ties checked.')
