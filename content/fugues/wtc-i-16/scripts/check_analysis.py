"""Check subject/answer, stretti, countersubject derivation and tonal anchors."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];A=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return [n for n in E if n['voice']==v and a<=n['start']<b]
s=ns(1,.5,7);a=ns(0,6.5,12.5);assert len(s)==len(a)==11
assert [y['pitch']-x['pitch'] for x,y in zip(s,a)]==[5]+[7]*10
assert [y['start']-x['start'] for x,y in zip(s,a)]==[6]*11
# Countersubject inverts the tail, then the head, at their original rhythms.
c=ns(1,8.5,13.5);assert len(c)==10
assert len(set(x['diatonic']+y['diatonic'] for x,y in zip(s[5:10],c[:5])))==1
# The head-derived continuation is freely adapted, not an exact inversion.
sub=[a for a in anns if a['kind']=='subject'];assert len(sub)==17
assert [(a['voice'],a['start']) for a in sub[7:9]]==[(3,64.5),(1,66.5)]
assert [(a['voice'],a['start']) for a in sub[12:15]]==[(0,108.5),(2,110.5),(3,112.5)]
# The two stretto combinations retain the head-to-tail rhythm and invert register.
for v,q,w,r,delta in [(3,64.5,0,108.5,12),(1,66.5,2,110.5,-6)]:
 x,y=ns(v,q,q+5.5),ns(w,r,r+5.5);assert len(x)==len(y)==10
 assert all(b['start']-r==a['start']-q for a,b in zip(x,y))
 assert [b['diatonic']-a['diatonic'] for a,b in zip(x,y)]==([12]*10 if v==3 else [-6]*5+[-5]*5)
for q,pcs in [(12,{2,5}),(22,{2,7,10}),(38,{7,10}),(44,{2,10}),(56.5,{0,5,9}),(62,{0,5,9}),(70,{2,5,10}),(82,{0,3,7}),(88,{0,3,7}),(94,{7,10}),(108,{2,6}),(134,{2,7,11})]:
 actual={n['pitch']%12 for n in A if n['start']<=q<n['start']+n['duration']};assert actual==pcs,(q,actual)
assert len(E)==786 and len(A)==754 and sum(n['tied'] for n in E)==32 and D['duration']==136
ids={n['id']:n for n in E};seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice'] and a['start']<=ids[n]['start'] and ids[n]['start']+ids[n]['duration']<=a['end'] for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==786 and set(printed)==set(ids)
print('BWV861: tonal answer, countersubject derivation, seventeen entries/fragments, two stretto combinations, twelve tonal anchors and 786 notes/32 ties verified.')
