"""Score-derived thematic spans; all times and printed beats are crotchets."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
E=json.loads((R/'data/score.json').read_text())['events'];A=[];occupied=set()
def at(bar,beat=1):return (bar-1)*4+beat-1
def span(kind,voice,start,end,label,name,status='statement',inverted=False):
 ns=[n for n in E if n['voice']==voice and start<=n['start']<end]
 assert ns and ns[0]['start']==start,(kind,voice,start)
 assert all(n['start']+n['duration']<=end for n in ns),(kind,voice,end)
 assert not any(n['id'] in occupied for n in ns),(kind,voice,start)
 aid=f'{kind}-{len(A)+1}'
 A.append(dict(id=aid,kind=kind,voice=voice,start=start,end=end,label=label,name=name,status=status,inverted=inverted,notes=[n['id'] for n in ns]))
 occupied.update(n['id'] for n in ns)
entries=[
 (2,1,1.5,3,2.5,'S','Subject'),(1,3,1.5,5,2,'A','Tonal answer'),
 (0,5,1.5,7,2.5,'S*','Subject; decorated close'),(3,7,1.5,9,2,'A','Tonal answer'),
 (2,11,3.5,13,3.5,'S','Subject'),(1,16,1.5,18,2,'S*','Subject in F-sharp major; altered close'),
 (0,18,1.5,20,2,'Si*','Inverted subject; altered closing note'),
 (1,20,1.5,22,2,'Ai*','Inverted answer; adjusted opening and close'),
 (3,21,3.5,23,3.5,'S','Subject'),(2,24,1.5,26,2,'S*','Subject in C-sharp minor, beginning on E; decorated close'),
 (1,29,1.5,31,2.5,'S*','Subject; decorated close'),(0,31,1.5,33,2.5,'A','Final tonal answer')]
for v,b,bt,e,et,label,name in entries:
 span('subject',v,at(b,bt),at(e,et),label,name,'variant' if '*' in label else 'statement','i' in label)
# Full countersubject statements: three in the exposition and the late alto return.
for v,b,bt,e,et,var in [(2,3,2.5,5,1.5,False),(1,5,2.5,7,1,True),(0,7,2.5,9,1.5,True),(1,31,2.5,33,1.5,True)]:
 span('cs1',v,at(b,bt),at(e,et),'CS*' if var else 'CS','Countersubject'+('; adapted continuation' if var else ''),'variant' if var else 'statement')
# Select exact diatonic/rhythmic recurrences of the countersubject's seven-note opening.
model=[n for n in E if n['voice']==2 and at(3,2.5)<=n['start']<at(3,4.5)]
assert len(model)==7
# The six-semiquaver episode figure first appears in the alto at the end of bar 7.
e_model=[n for n in E if n['voice']==1 and at(7,3.5)<=n['start']<at(8)]
assert len(e_model)==6
for kind_model,label,name in [(model,'c','Countersubject opening'),(e_model,'e','Episode figure')]:
 shape=[n['diatonic']-kind_model[0]['diatonic'] for n in kind_model];rhythm=[n['duration'] for n in kind_model]
 for v in range(4):
  line=[n for n in E if n['voice']==v]
  for i in range(len(line)-len(kind_model)+1):
   ns=line[i:i+len(kind_model)]
   if any(n['id'] in occupied for n in ns):continue
   # Keep musically clear starts; omit two incidental cross-bar matches.
   if label=='e' and (v,ns[0]['start']) in [(2,at(19,4.75)),(3,at(32,4.75))]:continue
   if [n['duration'] for n in ns]!=rhythm or any(a['start']+a['duration']!=b['start'] for a,b in zip(ns,ns[1:])):continue
   found=[n['diatonic']-ns[0]['diatonic'] for n in ns]
   inverse=found==[-x for x in shape]
   if found!=shape and not (label=='e' and inverse):continue
   span('motif',v,ns[0]['start'],ns[-1]['start']+ns[-1]['duration'],label+('i' if inverse else ''),name+(' in inversion' if inverse else ''),'fragment',inverse)
A.sort(key=lambda a:(a['start'],a['voice']))
(R/'data/annotations.json').write_text(json.dumps({'annotations':A},ensure_ascii=False,separators=(',',':')))
print({k:sum(a['kind']==k for a in A) for k in ['subject','cs1','motif']})
