"""Check analytical selections against the independently parsed score."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
s=json.loads((R/'data/score.json').read_text());E=s['events'];N={n['id']:n for n in E}
A=json.loads((R/'data/annotations.json').read_text())['annotations']
assert len(E)==802 and len(s['audio'])==750 and s['duration']==344
assert sum(n['tied'] for n in E)==52
assert len({n for a in A for n in a['notes']})==sum(len(a['notes']) for a in A)
subjects=[a for a in A if a['kind']=='subject'];assert len(subjects)==27
for a in subjects:
 ns=[N[n] for n in a['notes'] if not N[n]['tied']]
 d=[n['diatonic']-ns[0]['diatonic'] for n in ns]
 if a['label'].endswith('v'):assert d==[0,1,2,3,2,1,0],(a['name'],d)
 elif a['label']=='Ad*':assert d==[0,1,3,2,1,2],d
 else:assert d==[0,1,3,2,1,0],(a['name'],d)
 if a['label'] in ['Sd','Ad']:
  assert [n['duration'] for n in ns[:5]]==[2,1,1,1,1]
first=next(a for a in subjects if a['start']==0)
answer=next(a for a in subjects if a['start']==12)
assert [N[y]['pitch']-N[x]['pitch'] for x,y in zip(first['notes'],answer['notes'])]==[7]*6
# Actual one-minim gaps where the first note is shortened, not the implied half-bar gaps.
for start in [66,274]:
 alto=next(a for a in subjects if a['start']==start and a['voice']==1)
 tenor=next(a for a in subjects if a['start']==start+2 and a['voice']==2)
 assert N[alto['notes'][0]]['duration']==2 and N[tenor['notes'][0]]['duration']==4
# Register climax: a delayed entry, not a fictitious onset on the bar line.
climax=next(a for a in subjects if a['voice']==0 and a['start']==294)
assert max(N[n]['pitch'] for n in climax['notes'])==81==max(n['pitch'] for n in E)
assert all(a['kind']!='subject' for a in A if a['inverted'])
assert sum(a['kind']=='cs1' for a in A)==8
assert sum(a['kind']=='cs2' for a in A)==sum(a['kind']=='cs3' for a in A)==3
# Harmonic cadences, sampled after resolution and before the next entry.
for q,pitches in [(64,{47,54,59,63}),(120,{49,64,73}),(176,{42,49,57,66}),(216,{47,63,71}),(272,{44,59,63,68}),(340,{40,56,59,64})]:
 actual={n['pitch'] for n in s['audio'] if n['start']<=q<n['start']+n['duration']}
 assert actual==pitches,(q,actual,pitches)
print('BWV 878 checks passed: 27 entries/variants; real answer; diminution; shortened openings; chromatic pair; cadences; register climax; 52 ties.')
