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

# Twenty-four entries, including the curtailed tenor and soprano at 14-16.
entries=[(1,1,.5,'S'),(0,2,2.5,'A'),(2,4,.5,'A'),(3,5,2.5,'S'),
 (0,7,.5,'S'),(2,7,1.5,'A'),(1,9,.5,'A'),
 (3,10,2.5,'S'),(1,10,3.5,'A'),(2,12,.5,'S*'),
 (1,14,.5,'S'),(2,14,1.5,'A*'),(3,15,.5,'A'),(0,15,2.5,'A*'),
 (0,16,1.5,'S'),(1,16,2.5,'A'),(2,17,.5,'S*'),(3,17,2,'S*'),
 (2,19,.5,'S*'),(1,19,1.5,'S*'),(0,20,3.5,'S'),(2,21,2.5,'S*'),
 (2,24,.5,'S'),(1,24,2.5,'S')]
for v,b,o,label in entries:
 start=at(b,o);line=[n for n in E if n['voice']==v and n['start']>=start and not n['tied']]
 count=14
 if b==14 and v==2:count=10
 if b==15 and v==0:count=7
 selected=line[:count];end=selected[-1]['start']+selected[-1]['duration']
 # Preserve the full length of any tied closing note.
 for n in E:
  if n['voice']==v and n['start']==end and n['tied'] and n['pitch']==selected[-1]['pitch']:end+=n['duration']
 span('subject',v,start,end,label,('Answer' if label.startswith('A') else 'Subject')+('; adapted or incomplete' if '*' in label else ''),'variant' if '*' in label else 'statement')
# Further allusions are distinguished from the twenty-four entries.
span('head',1,at(16,.5),at(16,2),'h*','Subject-head fragment','fragment')
span('head',3,at(20,2.5),at(21,2),'h*','Altered subject head; undotted turn','fragment')
span('head',0,at(24,3.5),at(25,1),'h*','Subject-head fragment and descending continuation','fragment')
# Four descending semiquavers at the subject end, and their inversion.
for v in range(4):
 line=[n for n in E if n['voice']==v]
 for i in range(len(line)-3):
  ns=line[i:i+4]
  if any(n['id'] in occupied for n in ns) or [n['duration'] for n in ns]!=[.25]*4:continue
  if any(a['start']+a['duration']!=b['start'] for a,b in zip(ns,ns[1:])):continue
  shape=[n['diatonic']-ns[0]['diatonic'] for n in ns]
  if shape not in [[0,-1,-2,-3],[0,1,2,3]]:continue
  inv=shape[1]>0
  span('motif',v,ns[0]['start'],ns[-1]['start']+.25,'di' if inv else 'd','Descending semiquaver figure'+(' in inversion' if inv else ''),'fragment',inv)

A.sort(key=lambda a:(a['start'],a['voice']))
(R/'data/annotations.json').write_text(json.dumps({'annotations':A},ensure_ascii=False,separators=(',',':')))
print({k:sum(a['kind']==k for a in A) for k in sorted({a['kind'] for a in A})})
