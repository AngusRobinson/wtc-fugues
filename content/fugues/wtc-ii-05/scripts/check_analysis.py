from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def sounding(v,a,b):return [n for n in audio if n['voice']==v and a<=n['start']<b]
x,y=sounding(2,.5,7),sounding(1,6.5,12.5)
assert len(x)==len(y)==9 and all(b['pitch']-a['pitch']==7 and b['start']-a['start']==6 for a,b in zip(x,y))
assert x[4]['duration']==1.5 and y[4]['duration']==1
subjects=[a for a in anns if a['kind']=='subject'];assert len(subjects)==25 and sum(a['label']=='h'for a in subjects)==2
for starts,voices,pitches in [([106.5,107.5,108.5],[3,0,1],[57,81,69]),([128.5,129.5,130.5],[2,1,0],[62,71,79]),([174.5,175.5,176.5,177.5],[0,1,2,3],[81,78,62,59])]:
 for q,v,p in zip(starts,voices,pitches):assert any(n['voice']==v and n['start']==q and n['pitch']==p for n in E)
scale=sounding(3,149,156.5);assert len(scale)==15 and [n['pitch']for n in scale]==[62,61,59,57,55,54,52,50,49,47,45,43,42,40,38]
for q,pcs in [(12,{9,1}),(26,{9,1,4}),(29,{2,6}),(36,{9,1,4}),(42,{4,7,11}),(48,{11,2,6}),(52,{9,1,4}),(60,{2,6}),(78.5,{9,1,4}),(96.5,{6,9,1}),(106,{6,9}),(113,{9,1}),(128,{7,11,2}),(156,{2,6}),(174,{9,1,4}),(186,{7,11}),(190,{2,6,9}),(198,{2,6,9})]:assert {n['pitch']%12 for n in audio if n['start']<=q<n['start']+n['duration']}==pcs,q
assert len(E)==965 and len(audio)==876 and sum(n['tied']for n in E)==89 and D['duration']==200
ids={n['id']:n for n in E};seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end']for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==965 and set(printed)==set(ids)
print('BWV874: real answer, 23 statements and two heads, stretto pitches/onsets, two-octave bass scale, eighteen harmonic anchors, 965 notes and 89 ties verified.')
