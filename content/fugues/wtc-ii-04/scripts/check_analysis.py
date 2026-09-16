"""Musical regressions for BWV 873, independent of the engraving runtime."""
import json
from pathlib import Path
import xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1]
score=json.loads((R/'data/score.json').read_text());E=score['events'];audio=score['audio']
A=json.loads((R/'data/annotations.json').read_text())['annotations'];byid={n['id']:n for n in E}
def q(b,beat=1):return (b-1)*3+(beat-1)*.75
def notes(v,start,end):return [n for n in E if n['voice']==v and start<=n['start']<end]
def entry(v,b,beat=1):return next(a for a in A if a['kind']=='subject' and a['voice']==v and a['start']==q(b,beat))
assert len(E)==1443 and len(audio)==1353 and score['duration']==213
assert sum(n['tied'] for n in E)==90
assert sum(a['kind']=='subject' for a in A)==16
assert sum(a['kind']=='second' for a in A)==8
subject=notes(2,0,6)
answer=notes(0,q(2,3),q(2,3)+5.5)
assert len(subject)==len(answer)==22
assert all(a['pitch']-s['pitch']==19 for s,a in zip(subject,answer)), 'Real answer at the fifth plus an octave'
shape=[n['diatonic']-subject[0]['diatonic'] for n in subject]
for v,b in [(0,24),(1,26),(2,28)]:
 a=entry(v,b);ns=[byid[n] for n in a['notes']]
 assert [n['diatonic']-ns[0]['diatonic'] for n in ns]==[-x for x in shape]
 assert a['inverted']
for v,b,beat in [(0,48,1),(2,55,1),(2,67,3)]:
 a=entry(v,b,beat);first=byid[a['notes'][0]]
 assert first['tied']
 assert any(n['voice']==v and n['pitch']==first['pitch'] and n['start']<first['start']<n['start']+n['duration'] for n in audio)
 assert not any(n['voice']==v and n['start']==first['start'] and n['pitch']==first['pitch'] for n in audio)
# Chromatic theme, with full opening distinct from the earlier foreshadowings.
s2=next(a for a in A if a['kind']=='second' and a['start']==q(35))
assert [byid[n]['pitch'] for n in s2['notes'][:6]]==[78,77,76,75,80,73]
assert not any(a['kind']=='second' and a['start']<q(35) for a in A)
for b,first,second in [(48,0,2),(55,2,0),(61,1,2),(66,1,0)]:
 assert entry(first,b)
 assert any(a['kind']=='second' and a['voice']==second and a['start']==q(b) for a in A)
assert entry(2,67,3)['start']+.75*2==next(a['start'] for a in A if a['kind']=='second' and a['voice']==1 and a['start']==q(68))
assert notes(2,q(55,4)+.5,q(56))[0]['name']=='E♯3'
# Check that a theme starting on C sharp/G sharp is not confused with the underlying harmony.
for b,pitches in [(16,{49,64,73}),(20,{52,68,76}),(35,{54,57,78}),(44,{47,59,63}),(48,{54,57,73}),(53,{45,61,69}),(61,{49,56,76}),(71,{37,65,73})]:
 assert {n['pitch'] for n in E if n['start']<=q(b)<n['start']+n['duration']}==pitches,(b,pitches)
last=notes(0,q(71),213)+notes(1,q(71),213)+notes(2,q(71),213)
assert len(last)==3 and all(n['duration']==.75 for n in last)
assert max(n['start']+n['duration'] for n in audio)==210.75
seen=set()
for a in A:
 ns=[byid[i] for i in a['notes']]
 assert ns and ns[0]['start']==a['start']
 assert all(n['voice']==a['voice'] and a['start']<=n['start']<n['start']+n['duration']<=a['end'] for n in ns)
 assert not (set(a['notes'])&seen)
 seen.update(a['notes'])
 if a['label'] in ('t','ti'):
  assert len(ns)==6 and all(n['duration']==.25 for n in ns)
  tail=[n['diatonic']-subject[12]['diatonic'] for n in subject[12:18]]
  assert [n['diatonic']-ns[0]['diatonic'] for n in ns]==[(-x if a['inverted'] else x) for x in tail]
ns={'m':'http://www.music-encoding.org/ns/mei'};ID='{http://www.w3.org/XML/1998/namespace}id'
root=ET.parse(R/'sources/bwv873-three-voices.mei')
assert len(root.findall('.//m:tie',ns))==90
assert {n.get(ID) for n in root.findall('.//m:note',ns)}==set(byid)
print('BWV 873: pitches, real answer, inversion, two-theme combinations, tied-in entries, variants, harmonic arrivals and final silence verified.')
