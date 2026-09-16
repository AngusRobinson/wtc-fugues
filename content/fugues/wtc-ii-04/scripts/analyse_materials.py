"""Editorial spans checked against the score; times are crotchets."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
E=json.loads((R/'data/score.json').read_text())['events'];A=[];occupied=set()
def at(bar,beat=1):return (bar-1)*3+(beat-1)*.75
def span(kind,v,start,end,label,name,status='statement',inverted=False):
 ns=[n for n in E if n['voice']==v and start<=n['start']<end]
 assert ns and ns[0]['start']==start,(kind,v,start)
 assert all(n['start']+n['duration']<=end for n in ns),(kind,v,start,end)
 assert not any(n['id'] in occupied for n in ns),(kind,v,start)
 A.append(dict(id=f'{kind}-{len(A)+1}',kind=kind,voice=v,start=start,end=end,label=label,name=name,status=status,inverted=inverted,notes=[n['id'] for n in ns]));occupied.update(n['id'] for n in ns)
# The 22-note model ends on its first returning tonic; sequential extensions remain separate.
for v,b,beat,label,name in [
 (2,1,1,'S1','First subject'),(0,2,3,'A1','Real answer'),(1,5,1,'S1','First subject'),
 (0,16,1,'S1','First subject'),(1,17,3,'A1','Real answer'),(2,20,1,'S1','First subject in E major'),
 (0,24,1,'S1i','First subject inverted'),(1,26,1,'S1i','First subject inverted'),(2,28,1,'S1i','First subject inverted'),
 (1,30,1,'S1','First subject; direct form'),(2,55,1,'S1*','First subject; tied-in opening and raised third'),
 (1,66,1,'S1','First subject'),(2,67,3,'A1*','Final answer; tied-in opening and altered intervals')]:
 start=at(b,beat);end=start+5.5
 if b==1:end=at(3,2)
 span('subject',v,start,end,label,name,'variant' if '*' in label else 'statement','i' in label)
span('subject',0,at(48),at(50,2),'S1*','First subject; tied-in opening and broadened close','variant')
span('subject',1,at(53),at(54,4)+.25,'S1i*','First subject inverted; altered intervals','variant',True)
span('subject',1,at(61),at(63),'S1*','First subject; altered ascent and continuation','variant')
# S2 includes the chromatic descent and its continuation; incomplete/altered forms are explicit.
for v,b,beat,e,eb,label,name in [
 (0,35,1,37,4,'S2','Second subject'),
 (1,36,1,37,3,'S2*','Second subject; octave-displaced opening, incomplete'),
 (2,37,4,39,2,'S2*','Second subject; shortened opening and continuation'),
 (2,48,1,50,2,'S2*','Second subject; altered continuation'),
 (0,55,1,57,3,'S2*','Second subject; altered close'),
 (2,61,1,62,3+2/3,'S2*','Second subject; shortened continuation'),
 (0,66,1,68,1,'S2*','Second subject; shortened continuation'),
 (1,68,1,70,3,'S2*','Second subject; compressed close')]:
 span('second',v,at(b,beat),at(e,eb),label,name,'variant' if '*' in label else 'statement')
# Foreshadowings, not additional complete entries of S2.
for v,b,beat,e,eb in [(2,17,3,19,2),(0,20,1,21,2),(0,27,1,28,1)]:
 span('motif',v,at(b,beat),at(e,eb),'ch','Chromatic foreshadowing','fragment')
# Rising arpeggio and descending scale: the distinctive episode figure identified by Tovey.
for v,b,beat,e,eb,var in [(0,13,3,14,3,False),(0,33,1,34,1,True),(1,34,1,35,1,True),(0,44,1,44,3,False),(0,59,2,60,2,False)]:
 span('motif',v,at(b,beat),at(e,eb),'r*' if var else 'r','Arpeggio-and-scale figure'+('; variant' if var else ''),'fragment')
# Exact diatonic transpositions of the subject's six-note sequential tail.
model=[n for n in E if n['voice']==2 and 3<=n['start']<4.5]
shape=[n['diatonic']-model[0]['diatonic'] for n in model]
for v in range(3):
 ns=[n for n in E if n['voice']==v]
 for i,n in enumerate(ns):
  sub=ns[i:i+6]
  if len(sub)<6 or any(x['id'] in occupied for x in sub):continue
  if any(x['duration']!=.25 or x['start']!=n['start']+j*.25 for j,x in enumerate(sub)):continue
  ds=[x['diatonic']-n['diatonic'] for x in sub]
  if ds==shape or ds==[-x for x in shape]:
   inv=ds!=shape;span('motif',v,n['start'],n['start']+1.5,'ti' if inv else 't','Sequential tail'+('; inverted' if inv else ''),'fragment',inv)
A.sort(key=lambda a:(a['start'],a['voice']))
(R/'data/annotations.json').write_text(json.dumps({'annotations':A},ensure_ascii=False,separators=(',',':')))
print({k:sum(a['kind']==k for a in A) for k in ['subject','second','motif']})
