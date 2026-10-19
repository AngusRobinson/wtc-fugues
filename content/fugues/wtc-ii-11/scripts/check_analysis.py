from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return sorted([n for n in E if n['voice']==v and a<=n['start']<b and not n['tied']],key=lambda n:(n['start'],n['pitch']))
s=ns(0,.75,6.75);a=ns(1,6.75,12.75);assert len(s)==len(a)==20
assert [y['pitch']-x['pitch']for x,y in zip(s,a)]==[-5,-6,-5,-7]+[-5]*16
assert all(y['start']-x['start']==6 and y['duration']==x['duration']for x,y in zip(s,a))
for v,start,tr in [(2,20.25,-12),(1,77.25,-12),(2,98.25,-19)]:
 b=ns(v,start,start+6);assert len(b)==20
 assert all(y['pitch']-x['pitch']==tr and y['start']-x['start']==start-.75 and y['duration']==x['duration']for x,y in zip(s,b))
# The soprano return retains the subject strand through added inner chord tones.
last=[n for n in ns(0,126.75,132.25)if n['id']not in ['note-L616F3S2','note-L609F3','note-L610F3','note-L611F3']];assert len(last)==18
assert [y['pitch']-x['pitch']for x,y in zip(s,last)]==[0]*7+[-1]+[0]*10
assert all(y['start']-x['start']==126 and y['duration']==x['duration']for x,y in zip(s,last))
assert next(n for n in E if n['id']=='note-L609F2S1')['voice']==0
assert all(next(n for n in E if n['id']==i)['voice']==0 for i in ['note-L609F3','note-L610F3','note-L611F3'])
# The final answer has two extra bars of sequence before the descending tail.
final=ns(2,132.75,141.25);assert len(final)==26
assert [n['pitch']for n in final[:19]]==[41,40,41,46,43,41,43,48,45,43,45,50,46,45,46,52,48,50,52]
assert final[19]['start']-final[0]['start']==s[11]['start']-s[0]['start']+3
assert all(y['duration']==x['duration']for x,y in zip(s[11:18],final[19:]))
# The cadential bass returns exactly a fifth lower.
c=ns(2,36,42);c2=ns(2,141,147);assert len(c)==len(c2)
assert all(y['pitch']-x['pitch']==-7 and y['start']-x['start']==105 and y['duration']==x['duration']for x,y in zip(c,c2))
# Diatonic seventh imitation, one dotted-quaver beat later.
k=ns(0,107.25,111.75);k2=ns(1,108,112.5);assert len(k)==len(k2)
assert all(y['diatonic']-x['diatonic']==-6 and y['start']-x['start']==.75 and y['duration']==x['duration']for x,y in zip(k,k2))
assert any(n['voice']==2 and n['pitch']==41 and n['start']==90 and n['duration']==6.5 for n in audio)
assert any(n['voice']==2 and n['pitch']==48 and n['start']==112.5 and n['duration']==9.25 for n in audio)
for q,pcs in [(12,{0,4}),(20.25,{5,9}),(30.75,{0,4,7}),(42,{0,4}),(46.5,{2,5,9}),(51.75,{7,10}),(66,{5,9}),(69,{0,3,7}),(72,{7,9,10}),(75,{2,5,9}),(82.5,{2,5,9}),(90,{3,5,9}),(98.25,{2,5,10}),(105,{3,7,10}),(108,{0,5,8}),(112.5,{0,4,7}),(126.75,{5,8}),(132,{5,9}),(147,{5})]:
 assert {n['pitch']%12 for n in audio if n['start']<=q<n['start']+n['duration']}==pcs,q
assert len(E)==1104 and len(audio)==979 and sum(n['tied']for n in E)==125 and D['duration']==148.5
ids={n['id']:n for n in E};seen=set();assert sum(a['kind']=='subject'for a in anns)==8
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end']for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^\"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==1104 and set(printed)==set(ids)
for s in systems:assert all(s['start']<=ids[n]['bar']<=s['end']for n in re.findall(r'data-note-id="([^\"]+)"',s['svg']))
print('BWV880: tonal answer, eight entries, chordal voice allocation, sequential expansion, seventh imitation, both pedals, transposed cadence, nineteen harmonic anchors and 1104 notes/125 ties verified.')
