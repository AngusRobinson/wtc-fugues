from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return [n for n in E if n['voice']==v and a-1e-8<=n['start']<b-1e-8]
a,b,c=ns(1,0,8),ns(0,8,16),ns(2,20,28)
assert len(a)==len(b)==len(c)==24
assert all(y['pitch']-x['pitch']==7 and abs(y['start']-x['start']-8)<1e-8 for x,y in zip(a,b))
assert all(y['pitch']-x['pitch']==-12 and abs(y['start']-x['start']-20)<1e-8 for x,y in zip(a,c))
x,y=ns(1,10.25,16),ns(0,22.25,28)
assert len(x)==len(y) and all(b['pitch']-a['pitch']==5 and abs(b['start']-a['start']-12)<1e-8 for a,b in zip(x,y))
x,y=ns(1,64,66),ns(2,65,67)
assert len(x)==len(y)==12 and all(a['pitch']-b['pitch']==19 and abs(b['start']-a['start']-1)<1e-8 for a,b in zip(x,y))
assert ns(0,50.25,50.5)[0]['pitch']==81
for q,pcs in [(20,{2,5}),(36,{2,5}),(44,{5,9}),(46,{2,6}),(48.5,{2,5,10}),(52,{2,5}),(59.5,{0,4,9}),(70,{2,7,10}),(76,{0,4}),(78,{5,9}),(80,{2,10}),(92,{2,5}),(96,{2,5}),(106,{2})]:assert {n['pitch']%12 for n in audio if n['start']<=q+1e-8 and q<n['start']+n['duration']-1e-8}==pcs,q
assert len(E)==834 and len(audio)==800 and sum(n['tied']for n in E)==34 and D['duration']==108
ids={n['id']:n for n in E};seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']-1e-8<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end']+1e-8 for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==834 and set(printed)==set(ids)
print('BWV875: real answer, countersubject recurrence, inverted stretto, corrected octave reading, fourteen harmonic anchors, 834 notes and 34 ties verified.')
