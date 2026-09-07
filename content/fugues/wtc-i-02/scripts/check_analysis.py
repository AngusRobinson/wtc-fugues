"""Check thematic identity, analytical boundaries and sounding harmonic evidence."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
D=json.loads((R/'data/score.json').read_text());E=D['events'];N={e['id']:e for e in E};A=json.loads((R/'data/annotations.json').read_text())['annotations']
assert len(E)==770 and len(D['audio'])==754 and D['duration']==124
entries=[a for a in A if a['kind']=='subject'];assert len(entries)==8
assert [(a['voice'],a['start']) for a in entries]==[(1,.5),(0,8.5),(2,24.5),(0,40.5),(1,56.5),(0,76.5),(2,102.5),(0,114.5)]
base=[N[n] for n in entries[0]['notes']]
for a in entries:
 seq=[N[n] for n in a['notes']];assert len(seq)==len(base)==20
 assert [n['start']-a['start'] for n in seq]==[n['start']-.5 for n in base]
 expected=[n['diatonic']-base[0]['diatonic'] for n in base]
 if a['start'] in [8.5,56.5]:expected[3]-=1
 assert [n['diatonic']-seq[0]['diatonic'] for n in seq]==expected,a['id']
 assert [n['duration'] for n in seq[:-1]]==[n['duration'] for n in base[:-1]]
 assert a['end']==seq[-1]['start']+seq[-1]['duration']
# The final major third belongs to the subject; the added B in bar 30 does not.
assert N[entries[-1]['notes'][-1]]['pitch']==64
assert 'note-L442F3S2' not in entries[-1]['notes']
for pitch in [36,48]:
 pedal=[n for n in D['audio'] if n['voice']==2 and n['pitch']==pitch and n['start']>=114]
 assert len(pedal)==1 and pedal[0]['start']==114 and pedal[0]['duration']==10
assert len([a for a in A if a['kind']=='cs1'])==6
assert len([a for a in A if a['kind']=='cs2'])==5
assert all(a['status']=='variant' for a in A if a['kind']=='cs2' and a['start']>26.5)
# Compare the quaver counterpoint's diatonic identity in all six appearances.
cs=[a for a in A if a['kind']=='cs1'];ref=[N[n] for n in cs[0]['notes']]
for a in cs[1:]:
 seq=[N[n] for n in a['notes']];common=11 if a['start']==104.5 else 12
 assert [n['diatonic']-seq[0]['diatonic'] for n in seq[:common]]==[n['diatonic']-ref[0]['diatonic'] for n in ref[:common]]
assert any(a['kind']=='motif' and a['voice']==0 and a['start']==102.25 for a in A)
assert any(a['kind']=='cs1' and a['voice']==1 and a['start']==104.5 for a in A)
# These are sounding sonorities, not merely the entry's transposition label.
for q,expected in [(16,{67,70}),(24.5,{60,72,75}),(40,{39,67,75}),(48,{51,58,67}),(64,{43,58,67}),(76,{51,60}),(84,{48,60,63}),(114,{36,48,60}),(122,{36,48,55,60,64})]:
 pitches={e['pitch'] for e in E if e['start']<=q<e['start']+e['duration']}
 assert pitches==expected,(q,pitches,expected)
all_ids=[n for a in A for n in a['notes']];assert len(set(all_ids))==len(all_ids)
for a in A:
 assert all(N[n]['voice']==a['voice'] and a['start']<=N[n]['start']<a['end'] for n in a['notes'])
print('BWV 847 musical checks passed: eight complete entries, answer mutations, six CS1/five CS2 spans, cadences, closing chord and ten-crotchet pedal.')
