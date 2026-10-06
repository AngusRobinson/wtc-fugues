from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return [n for n in E if n['voice']==v and a<=n['start']<b]
a,b,c=ns(2,.5,5),ns(0,2.5,7),ns(1,4.5,9)
assert len(a)==len(b)==len(c)==8
assert [y['pitch']-x['pitch']for x,y in zip(a,b)]==[19]*3+[17]*5
assert len({x['diatonic']+y['diatonic']for x,y in zip(a,c)})==1
assert all(y['start']-x['start']==2 and z['start']-x['start']==4 for x,y,z in zip(a,b,c))
assert [n['pitch']for n in ns(2,114,116)]==[58,61,64]
assert [n['duration']for n in ns(2,114,116)]==[.5,.5,1]
assert not ns(1,114,115.5) and ns(1,115.5,116)[0]['pitch']==67
assert [n['start']for n in ns(1,97,101)]==[97,98,99,100]
assert [n['start']for n in ns(2,105,112)]==[105,106,107,108]
for q,pcs in [(12,{1,5}),(24,{8,0}),(32,{3,6}),(40,{1,5,8}),(51,{10,1,5}),(54,{5,9}),(60,{8,0,3}),(64,{1,5}),(83,{1,5}),(88,{1,5}),(90,{6,10}),(96,{8,0}),(108,{8,0,6}),(130,{1,6}),(138,{1,5,8})]:
 assert {n['pitch']%12 for n in audio if n['start']<=q<n['start']+n['duration']}==pcs,q
assert len(E)==884 and len(audio)==812 and sum(n['tied']for n in E)==72 and D['duration']==140
ids={n['id']:n for n in E};seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end']for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==884 and set(printed)==set(ids)
print('BWV872: eight-note subject, tonal answer, inversion, augmentations, corrected bar 29, fifteen harmonic anchors, 884 notes and 72 ties verified.')
