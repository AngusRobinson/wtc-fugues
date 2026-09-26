"""Musical and engraving checks for BWV 860, independent of span generation."""
import json,re
from pathlib import Path
import xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1]
score=json.loads((R/'data/score.json').read_text());E=score['events'];anns=json.loads((R/'data/annotations.json').read_text())['annotations'];byid={n['id']:n for n in E}
def seg(v,b,o,e,eo=0):return [n for n in E if n['voice']==v and (b-1)*3+o<=n['start']<(e-1)*3+eo]
def shape(ns):return [n['diatonic']-ns[0]['diatonic'] for n in ns]
subject=seg(0,1,0,5,.5);answer=seg(1,5,0,9,.5)
assert len(subject)==len(answer)==31
for a,b in [(subject[13],subject[14]),(subject[18],subject[19])]:
 assert b['diatonic']-a['diatonic']==6 and b['pitch']-a['pitch']==10, 'Two rising minor sevenths'
assert all(b['pitch']-a['pitch']==-5 and a['duration']==b['duration'] for a,b in zip(subject,answer)), 'Real answer is a strict fourth-down transposition'
for v,b,o in [(1,20,0),(0,24,0),(2,28,0),(1,43,0),(2,69,1.5)]:
 ns=[n for n in E if n['voice']==v and n['start']>=(b-1)*3+o][:20]
 assert shape(ns)==[-d for d in shape(subject[:20])],('Inverted first three bars',v,b)
# Both leading stretto statements omit the subject's second bar.
condensed=subject[:10]+subject[15:]
for v,b,o,e,eo in [(0,51,.25,54,.25),(1,60,1.5,63,2.5)]:
 ns=seg(v,b,o,e,eo)
 assert shape(ns)==shape(condensed),(v,b)
# Episode p and r retain their diatonic identity across the voice permutations.
for name,v,b,mv in [('p',2,31,0),('p',1,48,0),('p',1,65,0),('r',0,31,2),('r',2,48,2),('r',0,66,2)]:
 a=seg(mv,17,0,18);n=seg(v,b,0,b+1)
 assert shape(a)==shape(n),(name,v,b)
# Full score, closing five-part texture, ties and annotation membership.
assert len(E)==1759 and len(score['audio'])==1696 and score['duration']==258
assert sum(n['tied'] for n in E)==63
assert len([a for a in anns if a['kind']=='subject'])==17
assert len([a for a in anns if a['kind']=='cs1'])==8
assert all(not seg(2,b,0,b+1) for b in range(41,47))
assert {n['pitch']%12 for n in E if n['start']<=256.5<n['start']+n['duration']}=={7,11,2}
assert sum(n['start']<=256.5<n['start']+n['duration'] for n in E)==5
seen=set()
for a in anns:
 assert all(a['start']<=byid[n]['start'] and byid[n]['start']+byid[n]['duration']<=a['end'] and byid[n]['voice']==a['voice'] for n in a['notes'])
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text())
assert systems[0]['start']==1 and systems[-1]['end']==86 and len(systems)==22
printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==1759 and set(printed)==set(byid)
assert all('data-time=' in s['svg'] for s in systems)
print('BWV 860: real answer, five inversions, shortened stretti, episode permutations, 1,759 printed notes, 63 ties and five-part close verified.')

# Cropped ending notes retain their quaver/semiquaver flags, with no beam stub.
for example in json.loads((R/'data/thematic-examples.json').read_text()):
 if example['id'] not in ['subject','cs1']:continue
 root=ET.fromstring(example['svg'])
 measures=[g for g in root.iter() if g.get('class')=='measure']
 last=measures[-1]
 assert not any(g.get('class')=='beam' for g in last.iter()), 'Orphan beam on cropped ending'
 assert any(g.get('class')=='flag' for g in last.iter()), 'Missing flag on cropped ending'
