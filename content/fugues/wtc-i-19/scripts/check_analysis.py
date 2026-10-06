"""Verify answer, divided entries, countersubject recurrence and exact tonal anchors."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];A=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return[n for n in E if n['voice']==v and a<=n['start']<b]
s,a=ns(0,0,6.5),ns(1,4.5,11);assert len(s)==len(a)==10
assert [y['diatonic']-x['diatonic']for x,y in zip(s,a)]==[-3,-4,-4]+[-3]*7
assert all(y['start']-x['start']==4.5 for x,y in zip(s,a))
x,y=ns(1,99,108),ns(2,117,126);assert len(x)==len(y)==36
assert all(b['start']-a['start']==18 and b['duration']==a['duration'] and b['diatonic']-a['diatonic']==-10 for a,b in zip(x[:-1],y[:-1]))
assert y[-1]['name']=='B3' and x[-1]['name']=='A5'
# Cadential phrase: the middle line recurs at the lower fifth, then changes octave.
x,y=ns(1,72,84),ns(1,202.5,214.5)
assert len(x)==len(y)==15
assert all(b['start']-a['start']==130.5 and b['duration']==a['duration'] and b['diatonic']-a['diatonic'] in [-4,3] for a,b in zip(x,y))
assert ns(0,135,135.5)[0]['name']=='D6'
assert len([a for a in anns if a['kind']=='subject'])==19 # Sixteen entries; three handovers split into two spans.
assert [(n['voice'],n['start'])for n in E if n['start']in [108,109.5,110,111.5] and n['id']in {i for a in anns if a['kind']=='subject'for i in a['notes']}] # Both upper handovers encoded.
for q,pcs in [(15,{4,8}),(36,{2,9}),(54,{6,8,9}),(67.5,{2,11}),(73,{4,8,11}),(85.5,{4}),(99,{1,9}),(108,{4,8}),(135,{2,6}),(144,{2,6}),(157.5,{11}),(184.5,{6}),(216,{9}),(238.5,{1,9})]:
 actual={n['pitch']%12 for n in A if n['start']<=q<n['start']+n['duration']};assert actual==pcs,(q,actual)
assert len(E)==1282 and len(A)==1180 and sum(n['tied']for n in E)==102 and D['duration']==241.5
ids={n['id']:n for n in E};seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end']for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==1282 and set(printed)==set(ids)
print('BWV864: tonal answer, countersubject recurrence, divided entries, cadential reprise, fourteen harmonic anchors and 1282 notes/102 ties checked.')
