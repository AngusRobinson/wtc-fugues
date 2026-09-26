"""Independent checks of the answer, entry variants, counterpoint and harmonic arrivals."""
from pathlib import Path
import json,re,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];A=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations'];byid={n['id']:n for n in E}
def notes(v,a,b):return [n for n in E if n['voice']==v and a<=n['start']<b]
def sounding(q):return {n['pitch']%12 for n in A if n['start']<=q<n['start']+n['duration']}
s=notes(0,1.5,8.5);a=notes(1,9.5,16.5)
assert len(s)==len(a)==17
assert [n['pitch'] for n in s]==[68,70,68,66,68,77,73,68,66,65,66,75,65,73,63,72,61]
assert [y['pitch']-x['pitch'] for x,y in zip(s,a)]==[-7]+[-5]*16
assert [(n['start']-1.5,n['duration']) for n in s]==[(n['start']-9.5,n['duration']) for n in a]
entries=[a for a in anns if a['kind']=='subject'];assert len(entries)==12
assert [(a['voice'],a['start']) for a in entries]==[(0,1.5),(1,9.5),(2,17.5),(0,37.5),(2,53.5),(1,73.5),(0,95.5),(1,103.5),(0,165.5),(1,173.5),(2,181.5),(0,203.5)]
assert all(x['end']<=y['start'] for x,y in zip(entries,entries[1:])),'No stretto'
for voice,q in [(0,37.5),(0,95.5),(1,173.5),(0,203.5)]:assert [n['duration'] for n in notes(voice,q,q+.5)]==[.25,.25]
for q,expected in [(18,['cs2','cs1','subject']),(74,['cs2','subject','cs1']),(98,['subject','cs2','cs1']),(106,['cs1','subject','cs2'])]:
 assert [next(a['kind'] for a in anns if a['voice']==v and a['start']<=q<a['end']) for v in range(3)]==expected
for q,pc in [(16,{8,0}),(24.5,{1,5,8}),(44,{8,0}),(52,{3,6}),(60,{10,1}),(86,{5,8}),(102,{8,0,3}),(110,{1,5}),(172,{1,5}),(180,{8,0}),(210,{10,1,5}),(218,{1,5,8})]:assert sounding(q)==pc,(q,sounding(q))
assert len(E)==1471 and len(A)==1418 and sum(n['tied'] for n in E)==53 and D['duration']==220
assert any(n['pitch']==79 for n in notes(0,10,11)) and any(n['pitch']==78 for n in notes(0,174,175)),'CS1 F-double-sharp/F-sharp variants retained'
assert len(notes(0,216,220))==14,'Both final soprano layers retained'
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
print('BWV848: tonal answer,12entries,4triple-counterpoint dispositions,12harmonic arrivals,1471notes,53ties and final extra layer checked.')
