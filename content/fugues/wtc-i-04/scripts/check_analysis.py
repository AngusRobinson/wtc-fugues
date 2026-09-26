"""Independent pitch, entry, disposition, cadence and engraving checks for BWV 849."""
import json,re
from pathlib import Path
import xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];A=D['audio'];byid={n['id']:n for n in E};anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def q(b,o=0):return (b-1)*4+o
def head(v,b,o=0,count=5):return [n for n in E if n['voice']==v and n['start']>=q(b,o) and not n['tied']][:count]
def shape(ns):return [n['diatonic']-ns[0]['diatonic'] for n in ns]
s=head(4,1);answer=head(3,4)
assert [n['pitch'] for n in s]==[49,48,52,51,49]
assert [n['pitch']-m['pitch'] for n,m in zip(answer,s)]==[7]*5,'Real answer'
assert shape(s)==[0,-1,2,1,0] and s[2]['pitch']-s[1]['pitch']==4,'Diminished fourth B sharp to E'
assert [n['name'] for n in head(1,12,2)]==['G♯4','E♯4','A4','G♯4','F♯4'],'Fourth entry is a tonal form'
assert shape(head(0,36,count=8))==[0,-1,0,1,0,-1,-2,0]
assert shape(head(3,41,count=8))==[0,1,0,-1,0,1,2,0],'S2 inversion'
assert shape(head(2,49,1,8))==[0,3,3,3,2,1,2,3]
# Four audible dispositions; select the three principal strands, ignoring a lingering S2 ending in bass at 49.
for b,vs,expected in [(49,[0,1,2],['subject','subject2','subject3']),(52,[0,2,3],['subject3','subject2','subject']),(67,[0,1,4],['subject','subject3','subject2']),(74,[2,3,4],['subject2','subject3','subject'])]:
 found=[next(a['kind'] for a in anns if a['voice']==v and a['start']<=q(b,1)<a['end']) for v in vs]
 assert found==expected,(b,found)
assert [next(a['start'] for a in anns if a['kind']=='subject3' and a['voice']==v and a['start']==q(b,o)) for v,b,o in [(1,98,1),(3,98,3),(0,99,1)]]==[389,391,393],'Half-bar stretto'
assert max(a['end'] for a in anns if a['kind']=='subject2')==q(94,1)
assert any(a['kind']=='subject' and a['voice']==0 and a['start']==q(48) for a in anns),'Whole ornamented bar is included in S1'
assert head(4,73)[1]['pitch']-head(4,73)[0]['pitch']==11,'Displaced second note of bass subject'
assert head(0,107)[2]['duration']==2 and any(n['tied'] and n['voice']==0 and n['start']==q(109) for n in E),'Syncopated third note'
assert {n['pitch']%12 for n in A if n['start']<=q(115)<n['start']+n['duration']}=={1,5,8},'Major close'
assert len(E)==1429 and len(A)==1326 and sum(n['tied'] for n in E)==103 and D['duration']==460
seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(byid[n]['voice']==a['voice'] and a['start']<=byid[n]['start'] and byid[n]['start']+byid[n]['duration']<=a['end'] for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());assert len(systems)==23 and systems[-1]['end']==115
printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==1429 and set(printed)==set(byid)
for ex in json.loads((R/'data/thematic-examples.json').read_text()):
 root=ET.fromstring(ex['svg'])
 for g in root.iter():
  if g.get('class')=='beam':assert len([n for n in g.iter() if 'note' in n.get('class','').split()])>=2,'Orphan beam in example'
print('BWV 849: real and tonal answers, S2 inversion, four triple-counterpoint dispositions, half-bar stretto, altered entries, 1,429 printed notes, 103 ties and major close verified.')
