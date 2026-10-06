"""Verify chromatic subject, tonal variants, anticipations, motifs and harmonic arrivals."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'data/score.json').read_text());E=D['events'];audio=D['audio'];anns=json.loads((R/'data/annotations.json').read_text())['annotations']
def ns(v,a,b):return[n for n in E if n['voice']==v and a<=n['start']<b]
s=ns(1,.5,12);a=ns(2,12.5,24);sop=ns(0,48.5,60)
assert len(s)==len(a)==len(sop)==20 and {n['pitch']%12 for n in s}==set(range(12))
assert [y['pitch']-x['pitch']for x,y in zip(s,a)]==[-7,-5,-5,-5]+[-7]*16
assert [y['pitch']-x['pitch']for x,y in zip(s,sop)]==[5,7,7,7,7]+[5]*15
assert all(y['start']-x['start']==12 and x['duration']==y['duration']for x,y in zip(s,a))
full=[a for a in anns if a['kind']=='subject'and a['status']!='fragment'];heads=[a for a in anns if a['kind']=='subject'and a['status']=='fragment']
assert len(full)==13 and len(heads)==9
assert [(a['voice'],a['start'])for a in full]==[(1,.5),(2,12.5),(3,32.5),(0,48.5),(1,80.5),(2,116.5),(3,148.5),(2,172.5),(3,186.5),(2,210.5),(3,226.5),(2,238.5),(3,276.5)]
for v,a,b in [(1,72.5,80.5),(2,108.5,116.5)]:assert [(n['pitch'],n['duration'])for n in ns(v,a,a+1.5)]==[(n['pitch'],n['duration'])for n in ns(v,b,b+1.5)]
for v,t,inv in [(1,33,True),(2,49,True),(2,133,False),(2,137,False),(3,81,False),(3,161,False),(3,165,False),(0,149,False),(0,169,False),(0,273,False),(1,211,False)]:
 x,y=ns(1,13,15),ns(v,t,t+2);assert len(x)==len(y)==8
 assert all((n['diatonic']-y[0]['diatonic'])==(-1 if inv else 1)*(m['diatonic']-x[0]['diatonic'])and n['start']-t==m['start']-13 for m,n in zip(x,y))
for q,pcs in [(24,{2,11}),(62,{2,6,11}),(65,{1,6,9}),(81,{2,11}),(117,{4,7}),(132,{1,5,8}),(173,{2,6}),(198,{2,6}),(223,{1,4,8}),(239,{2,11}),(257,{2,6,11}),(277,{4,7}),(288,{2,6,11}),(300,{3,6,11})]:
 assert{n['pitch']%12 for n in audio if n['start']<=q<n['start']+n['duration']}==pcs,q
assert len(E)==1946 and len(audio)==1809 and sum(n['tied']for n in E)==137 and D['duration']==304
assert len(ns(3,300,304))==2
ids={n['id']:n for n in E};seen=set()
for a in anns:
 assert not seen.intersection(a['notes']);seen.update(a['notes'])
 assert all(ids[n]['voice']==a['voice']and a['start']<=ids[n]['start']and ids[n]['start']+ids[n]['duration']<=a['end']for n in a['notes'])
systems=json.loads((R/'data/annotated-systems.json').read_text());printed=[n for s in systems for n in re.findall(r'data-note-id="([^"]+)"',s['svg'])]
assert len(printed)==len(set(printed))==1946 and set(printed)==set(ids)
print('BWV869: twelve pitch classes, tonal answer variants, thirteen complete entries and nine anticipations, semiquaver inversions, fourteen harmonic anchors, 1946 notes and 137 ties verified.')
