"""Thematic readings checked against the score, Keller, Prout and Tovey."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
E=json.loads((R/'data/score.json').read_text())['events'];A=[];occupied=set()
def at(b,offset=0):return (b-1)*3+offset
def span(kind,v,start,end,label,name,status='statement',inv=False):
 ns=[n for n in E if n['voice']==v and start<=n['start']<end]
 assert ns and ns[0]['start']==start,(kind,v,start)
 assert all(n['start']+n['duration']<=end for n in ns),(kind,v,end)
 assert not any(n['id'] in occupied for n in ns),(kind,v,start)
 A.append(dict(id=f'{kind}-{len(A)+1}',kind=kind,voice=v,start=start,end=end,label=label,name=name,status=status,inverted=inv,notes=[n['id'] for n in ns]));occupied.update(n['id'] for n in ns)
entries=[
 (0,1,0,5,.5,'S','Subject'),(1,5,0,9,.5,'A','Real answer'),(2,11,0,15,1,'S','Subject'),
 (1,20,0,24,.5,'Si*','Inverted subject; adjusted ending'),(0,24,0,28,1,'Ai*','Inverted answer; adjusted ending'),(2,28,0,31,0,'Si*','Inverted subject; final bar omitted'),
 (0,38,0,42,.5,'S','Subject in E minor'),(1,43,0,46,0,'Si*','Inverted subject in E minor; final bar omitted'),
 (0,51,.25,54,.25,'S*','Subject in B minor; second bar omitted'),(2,52,0,54,0,'S*','Stretto response; shortened and broken off'),
 (1,60,1.5,63,2.5,'S*','Subject in D major; second bar omitted'),(0,61,1.5,63,.5,'S*','Stretto response; head and adapted close, leap-bars omitted'),
 (2,69,1.5,73,0,'Si*','Inverted subject; closing bar curtailed'),(1,77,0,79,.5,'Si*','Inverted subject; second bar omitted, then broken off'),
 (2,78,.25,80,0,'Si*','Inverted head continued in descending sequence'),(0,79,0,82,.25,'S*','Direct subject; altered continuation'),
 (1,79,.5,80,1.5,'S*','Subject fragment in parallel thirds with the soprano')]
for v,b,o,e,eo,label,name in entries:span('subject',v,at(b,o),at(e,eo),label,name,'variant' if '*' in label else 'statement','i' in label)
for v,b,o,e,eo,inv,var in [(0,6,1.5,9,.25,False,False),(1,12,1.5,15,.25,False,True),(2,21,1.5,23,0,True,True),(1,25,1.5,27,0,True,True),(0,29,1.5,31,0,True,True),(1,40,0,42,.25,False,True),(0,44,1.5,46,0,True,True),(1,70,1.75,72,1.5,True,True)]:
 span('cs1',v,at(b,o),at(e,eo),'CS'+('i' if inv else '')+('*' if var else ''),('Inverted countersubject' if inv else 'Countersubject')+('; abridged or adapted' if var else ''),'variant' if var else 'statement',inv)
# Four dispositions of the episode's three lines, named by their roles at 17–19.
for b,end,permutation in [(17,20,'pqr'),(31,34,'rqp'),(48,51,'qpr'),(65,68,'rpq')]:
 for v,label in enumerate(permutation):
  ns=[n for n in E if n['voice']==v and at(b)<=n['start']<at(end)]
  start=ns[0]['start'];stop=max(n['start']+n['duration'] for n in ns)
  span('motif',v,start,stop,label,{'p':'Episode: rising third and descending continuation','q':'Episode: slower line','r':'Episode: semiquaver figure'}[label]+(' (varied)' if b==65 or label=='q' and b==31 else ''),'episode')
# Exact diatonic/rhythmic recurrences of the codetta's semiquaver figure.
model=[n for n in E if n['voice']==0 and at(9,.25)<=n['start']<at(10)]
shape=[n['diatonic']-model[0]['diatonic'] for n in model];rhythm=[n['duration'] for n in model]
for v in range(3):
 line=[n for n in E if n['voice']==v]
 for i in range(len(line)-len(model)+1):
  ns=line[i:i+len(model)]
  if any(n['id'] in occupied for n in ns):continue
  if [n['duration'] for n in ns]!=rhythm:continue
  if any(a['start']+a['duration']!=b['start'] for a,b in zip(ns,ns[1:])):continue
  found=[n['diatonic']-ns[0]['diatonic'] for n in ns];inv=found==[-x for x in shape]
  if found!=shape and not inv:continue
  span('motif',v,ns[0]['start'],ns[-1]['start']+ns[-1]['duration'],'ri' if inv else 'r','Codetta semiquaver figure'+(' in inversion' if inv else ''),'fragment',inv)
# Scale passages paired with r/ri; terminal adjustments remain within their phrase.
for v,b,o,e,eo in [(0,34,.25,35,0),(2,35,.25,36,0),(2,36,0,37,0),(0,37,.25,37,2.75),(2,73,.5,74,0),(0,74,.25,75,0),(0,75,.25,76,0),(2,76,.25,77,0)]:
 span('motif',v,at(b,o),at(e,eo),'d','Scale figure','fragment')
A.sort(key=lambda a:(a['start'],a['voice']))
(R/'data/annotations.json').write_text(json.dumps({'annotations':A},ensure_ascii=False,separators=(',',':')))
print({k:sum(a['kind']==k for a in A) for k in ['subject','cs1','motif']})
