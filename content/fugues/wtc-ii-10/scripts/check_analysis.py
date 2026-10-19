from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return[n for n in audio if n['voice']==v and a-1e-7<=n['start']<b-1e-7]
a=ns(0,1/3,25+1/3);assert len(a)==48
for v,s,trans in [(1,24+1/3,-5),(2,48+1/3,-12),(2,164+1/3,-17),(1,196+1/3,0),(0,236+1/3,5),(2,284+1/3,-24)]:
 b=ns(v,s,s+24);assert len(b)>=42
 assert all(abs(y['start']-x['start']-(s-1/3))<1e-7 and y['pitch']-x['pitch']==trans for x,y in zip(a[:42],b[:42]))
# Major-mode statements preserve the diatonic contour and rhythmic profile.
dia={n['id']:n['diatonic']for n in E}
for v,s,trans in [(0,92+1/3,2),(1,116+1/3,-1)]:
 b=ns(v,s,s+24)
 assert all(abs(y['start']-x['start']-(s-1/3))<1e-7 and dia[y['id']]-dia[x['id']]==trans for x,y in zip(a[:42],b[:42]))
assert [x['pitch']for x in ns(1,47+1/3,49)]==[69,67,66,64,63]
# Check the recurring sustained portion independently of its free arpeggiated lead-in.
cs=ns(0,33,46);assert len(cs)==7
for v,s,tr in [(1,57,-7),(1,173,-12),(2,205,-19),(1,293,-7)]:
 b=ns(v,s,s+11);assert len(b)==7
 assert all(y['pitch']-x['pitch']==tr and abs(y['start']-x['start']-(s-33))<1e-7 for x,y in zip(cs,b))
for q,pcs in [(25,{2,11}),(49,{4,7,11}),(71,{4,7,11}),(79,{2,7,11}),(93,{7,11}),(117,{2,6}),(137,{2,4,6}),(151,{2,6,11}),(187,{2,6,11}),(197,{4,7}),(217,{4,7}),(221,{0,4,9}),(229,{2,7,11}),(237,{0,9}),(257,{0,9}),(278,{3,6,11}),(283,{4,7}),(309,{4,7,11}),(344,{4,8,11})]:
 actual={n['pitch']%12 for n in audio if n['start']<=q<n['start']+n['duration']};assert actual==pcs,(q,actual,pcs)
assert {(n['voice'],n['pitch'])for n in E if n['start']==331 and n['voice']!=0}=={(1,54),(1,57),(2,48)}
assert len(E)==1561 and len(audio)==1434 and sum(n['tied']for n in E)==127 and D['duration']==345
ids={n['id']:n for n in E};seen=set()
assert sum(a['kind']=='subject'for a in anns)==9
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice']and a['start']-1e-7<=ids[n]['start']and ids[n]['start']+ids[n]['duration']<=a['end']+1e-7 for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^\"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==1561 and set(printed)==set(ids)
for s in systems:assert all(s['start']<=ids[n]['bar']<=s['end']for n in re.findall(r'data-note-id="([^\"]+)"',s['svg']))
print('BWV879: nine entries, real answer with cadential alteration, redistributed countersubject, nineteen harmonic anchors, selected Kroll variant, 1561 notes and 127 ties verified.')
