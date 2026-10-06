from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return [n for n in E if n['voice']==v and a<=n['start']<b]
x,y=ns(1,.5,5),ns(0,4.5,9)
assert len(x)==len(y)==9 and [b['pitch']-a['pitch']for a,b in zip(x,y)]==[5]+[7]*8
assert all(b['duration']==a['duration'] and b['start']-a['start']==4 for a,b in zip(x,y))
a,b=ns(2,16,20),ns(0,20,24)
assert len(a)==len(b)==16 and len({x['diatonic']+y['diatonic']for x,y in zip(a,b)})==1
assert all(x['duration']==y['duration']==.25 for x,y in zip(a,b))
# Both augmented subjects preserve every onset and pitch of the original at twice the time scale.
for voice,start,transposition in [(1,53,0),(3,73,-12)]:
 z=ns(voice,start,start+7.5)
 assert len(z)==9
 assert all(n['start']-start==2*(m['start']-.5) and n['pitch']-m['pitch']==transposition for m,n in zip(x,z))
assert not [n for n in E if n['voice']==3 and n['start']<73]
assert any(n['voice']==2 and n['start']==68 and n['name']=='A3'for n in E)
assert any(n['voice']==0 and n['start']==69.5 and n['name']=='D5'for n in E)
for q,pcs in [(8,{7,10}),(16,{0,3}),(28,{2,11}),(36,{5,8}),(52,{7}),(60,{0,3}),(68,{5,9}),(90,{0,3}),(94,{0,4,7}),(96,{5,8}),(108,{0,3,7})]:
 assert {n['pitch']%12 for n in audio if n['start']<=q<n['start']+n['duration']}==pcs,q
assert len(E)==700 and len(audio)==657 and sum(n['tied']for n in E)==43 and D['duration']==112
ids={n['id']:n for n in E};seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end']for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==700 and set(printed)==set(ids)
print('BWV871: tonal answer, exact semiquaver inversion, two augmentations, delayed bass, bar-18 readings, eleven harmonic anchors, 700 notes and 43 ties verified.')
