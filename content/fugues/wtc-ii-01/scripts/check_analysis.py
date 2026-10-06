from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return [n for n in E if n['voice']==v and a<=n['start']<b]
x,y=ns(1,.5,2),ns(0,8.5,10)
assert [n['pitch']for n in x]==[67,65,67,60]
assert [n['pitch']for n in y]==[72,71,72,67]
assert [n['duration']for n in x]==[n['duration']for n in y]==[.25,.25,.5,.5]
# The semiquaver canon passes from soprano bar 33 to alto bar 34 a diatonic fifth below.
x,y=ns(0,64,66),ns(1,66,68)
assert len(x)==len(y)==7
assert all(b['diatonic']-a['diatonic']==-4 and b['start']-a['start']==2 and b['duration']==a['duration']for a,b in zip(x,y))
for q,pcs in [(16,{7,11}),(24,{0,4}),(48,{2,5}),(56,{0,9}),(92,{0,4}),(108,{7,11}),(132,{0,4,7}),(134,{0,9}),(150,{0,4}),(164,{0,4,7})]:
 assert {n['pitch']%12 for n in audio if n['start']<=q<n['start']+n['duration']}==pcs,q
assert len([a for a in anns if a['kind']=='subject' and a['status']=='statement'])==8
assert len([a for a in anns if a['kind']=='subject' and a['status']=='fragment'])==4
assert len(E)==1072 and len(audio)==1035 and sum(n['tied']for n in E)==37 and D['duration']==166
ids={n['id']:n for n in E};seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end']for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==1072 and set(printed)==set(ids)
print('BWV870: tonal answer, semiquaver canon, ten harmonic anchors, eight complete and four partial entries, 1072 notes and 37 ties verified.')
