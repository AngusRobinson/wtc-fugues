"""Musical checks for BWV 868, independent of the engraving runtime."""
import json
from pathlib import Path
import xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1]
score=json.loads((R/'data/score.json').read_text());E=score['events'];audio=score['audio']
A=json.loads((R/'data/annotations.json').read_text())['annotations'];byid={n['id']:n for n in E}
def q(b,beat=1):return (b-1)*4+beat-1
def notes(v,start,end):return [n for n in E if n['voice']==v and start<=n['start']<end]
def entry(v,b,beat=1.5):return next(a for a in A if a['kind']=='subject' and a['voice']==v and a['start']==q(b,beat))
assert len(E)==876 and len(audio)==827 and score['duration']==136
assert sum(n['tied'] for n in E)==49
assert sum(a['kind']=='subject' for a in A)==12
assert [(a['voice'],a['start']) for a in A if a['kind']=='cs1']==[(2,q(3,2.5)),(1,q(5,2.5)),(0,q(7,2.5)),(1,q(31,2.5))]
subject=notes(2,.5,9.5);answer=notes(1,q(3,1.5),q(5,2))
assert len(subject)==len(answer)==14
assert [a['pitch']-s['pitch'] for s,a in zip(subject,answer)]==[7,5,5,5,5,7,7,7,7,7,7,7,7,7]
assert [n['duration'] for n in subject[:-1]]==[n['duration'] for n in answer[:-1]]
for v,b in [(0,18),(1,20)]:assert entry(v,b)['inverted'] and entry(v,b)['status']=='variant'
inverted=[byid[i] for i in entry(0,18)['notes']]
assert [n['diatonic']-inverted[0]['diatonic'] for n in inverted[:13]]==[-(n['diatonic']-subject[0]['diatonic']) for n in subject[:13]]
inv_answer=[byid[i] for i in entry(1,20)['notes']]
assert all(a['pitch']-s['pitch']==-5 for s,a in zip(inverted[1:13],inv_answer[1:13]))
assert inv_answer[0]['name']=='B4' and inverted[-1]['name']=='D♯5'
assert entry(2,11,3.5)['start']==42.5
assert entry(3,21,3.5)['start']==82.5<entry(1,20)['end']
assert byid[entry(2,24)['notes'][0]]['name']=='E4'
assert min(n['pitch'] for n in notes(3,q(25),q(26)))==37
seen=set()
for a in A:
 ns=[byid[i] for i in a['notes']]
 assert ns and ns[0]['start']==a['start']
 assert all(n['voice']==a['voice'] and a['start']<=n['start']<n['start']+n['duration']<=a['end'] for n in ns)
 assert not (set(a['notes'])&seen)
 seen.update(a['notes'])
 if a['label'] in ('e','ei'):
  assert len(ns)==6 and all(n['duration']==.25 for n in ns)
  shape=[0,-1,0,1,2,3]
  assert [n['diatonic']-ns[0]['diatonic'] for n in ns]==[(-x if a['inverted'] else x) for x in shape]
for b,pitches in [(9,{54,70,78}),(18,{42,49,70,78}),(20,{47,73,75}),(26,{37,64,73}),(29,{47,63,73}),(34,{47,54,71,75})]:
 assert {n['pitch'] for n in E if n['start']<=q(b)<n['start']+n['duration']}==pitches,b
last=[n for n in E if n['bar']==34]
assert len(last)==4 and all(n['duration']==4 for n in last)
assert max(n['start']+n['duration'] for n in audio)==136
ns={'m':'http://www.music-encoding.org/ns/mei'};ID='{http://www.w3.org/XML/1998/namespace}id'
root=ET.parse(R/'sources/bwv868-four-voices.mei')
assert len(root.findall('.//m:tie',ns))==49
assert {n.get(ID) for n in root.findall('.//m:note',ns)}==set(byid)
for l in root.findall('.//m:layer',ns):
 if not l.findall('.//m:note',ns):assert l.find('m:mRest',ns) is not None or l.findall('m:rest',ns)
print('BWV 868: tonal answer, inverted pair, 12 entries, countersubjects, episode figures, tonal arrivals, 49 ties and final chord verified.')
