from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return[n for n in E if n['voice']==v and a<=n['start']<b]
a,b=ns(3,0,20),ns(2,24,44)
assert len(a)==len(b)==14
assert [y['pitch']-x['pitch']for x,y in zip(a,b)]==[7,5]+[7]*12
assert all(y['start']-x['start']==24 and y['duration']==x['duration']for x,y in zip(a,b))
for v,s,trans in [(1,52,12),(0,148,24),(3,236,0)]:
 n=ns(v,s,s+20);assert len(n)==14 and all(y['pitch']-x['pitch']==trans and y['start']-x['start']==s for x,y in zip(a,n))
assert ns(3,122,124)[0]['pitch']==51 and ns(3,122,124)[0]['duration']==2
assert ns(2,210,212)[0]['name']=='B♭3' and ns(2,210,212)[0]['duration']==2
x,y=ns(0,184,200),ns(1,192,208)
assert len(x)==len(y) and all(b['pitch']-a['pitch']==-7 and b['start']-a['start']==8 and b['duration']==a['duration']for a,b in zip(x,y))
x,y=ns(3,34,44),ns(1,90,100)
assert len(x)==len(y) and all(b['pitch']-a['pitch']==12 and b['start']-a['start']==56 for a,b in zip(x,y))
for q,pcs in [(32,{2,10}),(52,{3,7}),(72,{3,7}),(100,{2,10}),(116,{2,10}),(128,{3,7,10}),(144,{3,7,10}),(172,{0,3,7}),(188,{0,4,10}),(196,{3,5,9}),(213,{0,3,8}),(228,{0,3,8}),(236,{3,7}),(276,{3,7,10})]:
 actual={n['pitch']%12 for n in audio if n['start']<=q and q<n['start']+n['duration']};assert actual==pcs,(q,actual,pcs)
assert len(E)==750 and len(audio)==707 and sum(n['tied']for n in E)==43 and D['duration']==280
ids={n['id']:n for n in E};seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice']and a['start']<=ids[n]['start']and ids[n]['start']+ids[n]['duration']<=a['end']for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^\"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==750 and set(printed)==set(ids)
print('BWV876: Keller boundary, tonal answer, three stretto pairs, countersubject recurrence, canonic episode, fourteen harmonic anchors, 750 notes and 43 ties verified.')
