"""Editorial thematic spans; primary score checked against Keller, Prout and Tovey."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
E=json.loads((R/'data/score.json').read_text())['events'];A=[];occupied=set()
def at(b,o=0):return (b-1)*4+o
def span(kind,v,start,end,label,name,status='statement',inv=False):
 ns=[n for n in E if n['voice']==v and start<=n['start']<end]
 assert ns and ns[0]['start']==start,(kind,v,start)
 assert all(n['start']+n['duration']<=end for n in ns),(kind,v,start,end)
 assert not any(n['id'] in occupied for n in ns),(kind,v,start,'overlap')
 A.append(dict(id=f'{kind}-{len(A)+1}',kind=kind,voice=v,start=start,end=end,label=label,name=name,status=status,inverted=inv,notes=[n['id'] for n in ns]));occupied.update(n['id'] for n in ns)

# Voice indices follow the retained Kroll/Huron part allocation.
entries=[(0,1,0,'S'),(1,3,0,'A'),(2,10,0,'S'),(3,12,0,'A'),(4,15,0,'S'),
 (0,25,0,'S'),(1,27,0,'A'),(3,29,0,'S'),(4,32,0,'S'),(1,37,0,'A'),
 (2,46,1,'A'),(4,48,0,'A'),(0,50,0,'A'),(1,50,2,'A'),(4,52,0,'A'),(3,53,0,'A'),
 (1,55,0,'A'),(2,55,0,'S'),
 (0,67,2,'S'),(1,68,0,'A'),(2,68,2,'S'),(3,69,0,'A'),(4,69,2,'S')]
for v,b,o,label in entries:
 start=at(b,o);line=[n for n in E if n['voice']==v and n['start']>=start and not n['tied']]
 ns=line[:6];assert len(ns)==6
 # Include the subsequent four-note turn only when the model continues intact.
 tail=line[6:10];shape=[n['diatonic']-ns[-1]['diatonic'] for n in tail]
 full=shape==[-1,0,1,2] and all(n['duration']==1 for n in tail[:3]) and all(a['start']+a['duration']==z['start'] for a,z in zip(line[5:9],tail))
 if full:ns+=tail
 end=ns[-1]['start']+ns[-1]['duration']
 model=[0,-3,5,4,3,2] if label=='S' else [0,-4,5,4,3,2]
 core=[n['diatonic']-line[0]['diatonic'] for n in line[:6]]
 rhythm=[n['start']-start for n in line[:6]]
 var=core!=model or rhythm!=[0,2,5,6,7,8] or not full
 if b==52 and v==4:var=True
 span('subject',v,start,end,label+('*' if var else ''),('Subject' if label=='S' else 'Tonal answer')+('; varied or shortened' if var else ''),'variant' if var else 'statement')
# Two aborted answer openings in the coda: altered first intervals.
span('head',4,at(73),at(75),'h*','Altered answer head in the coda','fragment')
span('head',3,at(74),at(76),'h*','Answer-head allusion; tonic resolution','fragment')
# The two-quaver lead into a long note recurs in the sequential codetta and episode.
for v in range(5):
 line=[n for n in E if n['voice']==v]
 for i in range(len(line)-2):
  ns=line[i:i+3]
  if not (4<=ns[0]['bar']<=12 or 41<=ns[0]['bar']<=45):continue
  if any(n['id'] in occupied for n in ns) or [n['duration'] for n in ns[:2]]!=[.5,.5] or ns[2]['duration']<1:continue
  if any(a['start']+a['duration']!=b['start'] for a,b in zip(ns,ns[1:])):continue
  end=ns[-1]['start']+ns[-1]['duration'];last=ns[-1]
  for n in line[i+3:]:
   if n['start']==end and n['tied'] and n['pitch']==last['pitch']:end+=n['duration']
   else:break
  span('sequence',v,ns[0]['start'],end,'q','Sequential quaver figure','fragment')
# Four-step crotchet strands, direct and inverted, outside the main entries.
for v in range(5):
 line=[n for n in E if n['voice']==v]
 for i in range(len(line)-3):
  ns=line[i:i+4]
  if any(n['id'] in occupied for n in ns) or [n['duration'] for n in ns]!=[1]*4:continue
  if any(a['start']+a['duration']!=b['start'] for a,b in zip(ns,ns[1:])):continue
  shape=[n['diatonic']-ns[0]['diatonic'] for n in ns]
  if shape not in [[0,-1,-2,-3],[0,1,2,3]]:continue
  inv=shape[1]>0
  span('motif',v,ns[0]['start'],ns[-1]['start']+1,'di' if inv else 'd','Descending crotchet figure'+(' in inversion' if inv else ''),'fragment',inv)

A.sort(key=lambda a:(a['start'],a['voice']))
(R/'data/annotations.json').write_text(json.dumps({'annotations':A},ensure_ascii=False,separators=(',',':')))
print({k:sum(a['kind']==k for a in A) for k in sorted({a['kind'] for a in A})})
