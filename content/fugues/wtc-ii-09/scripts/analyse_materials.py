"""Score-derived spans. Times are crotchets; printed beats are minims."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
E=json.loads((R/'data/score.json').read_text())['events'];A=[];occupied=set()
def at(bar,beat=1):return (bar-1)*8+(beat-1)*2
def span(kind,voice,start,end,label,name,status='statement',inverted=False):
 ns=[n for n in E if n['voice']==voice and start<=n['start']<end]
 assert ns and ns[0]['start']==start,(kind,voice,start)
 assert not any(n['id'] in occupied for n in ns),(kind,voice,start)
 aid=f'{kind}-{len(A)+1}'
 A.append(dict(id=aid,kind=kind,voice=voice,start=start,end=end,label=label,name=name,status=status,inverted=inverted,notes=[n['id'] for n in ns]))
 occupied.update(n['id'] for n in ns)
# Entries include their final note, including its tied continuation.
entries=[
 (3,1,1,2,3.5,'S','Subject'),(2,2,3,4,2.5,'A','Real answer'),
 (1,4,1,5,4,'S','Subject'),(0,5,3,7,3.5,'A','Real answer'),
 (1,9,2,10,3.5,'A*','Answer; shortened opening'),(2,9,3,11,1.5,'S','Subject'),
 (3,10,3,12,4,'A','Answer'),(0,11,1,12,3.5,'S*','Subject; raised closing note'),
 (1,16,1,17,3.5,'S','Subject'),(0,17,1,18,4,'A','Answer'),
 (3,19,1,20,3.5,'A','Answer'),(2,20,1,21,4.5,'S*','Subject in F-sharp minor; syncopated close'),
 (0,23,1,24,4,'Sv','Subject variation in F-sharp minor'),(1,23,2,25,1.5,'Av','Answer variation'),
 (3,25,1,27,2,'Sv','Subject variation in G-sharp minor'),(2,25,2,27,1,'Av','Answer variation'),
 (0,26,4,27,4,'Sd','Subject in diminution'),(1,27,2,28,1.5,'Ad','Answer in diminution'),
 (2,28,2,29,1.5,'Sd','Subject in diminution'),(3,28,4,29,4,'Ad','Answer in diminution'),
 (3,30,2,31,1.5,'Ad*','Diminished answer; altered close'),(1,30,3,32,1.5,'S','Subject in original values'),
 (1,35,2,36,4,'A*','Answer; shortened opening'),(2,35,3,37,2,'S','Subject'),
 (3,36,3,38,1.5,'A','Answer'),(0,37,4,39,2,'S*','Subject; shortened opening in the highest register'),
 (3,40,1,41,4,'A','Final answer')]
for v,b,bt,e,et,label,name in entries:
 span('subject',v,at(b,bt),at(e,et),label,name,'variant' if '*' in label or label.endswith('v') else 'statement')
# The conventional countersubject, with modified returns explicitly distinguished.
for v,b,bt,e,et,var in [(3,3,1,4,4,False),(2,4,3,5,4,True),(1,6,1,7,3,False),
 (2,11,4,12,4,True),(0,36,1,37,3,True),(1,37,1,38,1.5,True),(2,38,1,39,2.5,True),(1,40,3.5,42,3,True)]:
 span('cs1',v,at(b,bt),at(e,et),'CS*' if var else 'CS','Countersubject'+('; variant' if var else ''),'variant' if var else 'statement')
# The recurrent chromatic pair of bars 16-20 (Tovey's additional countersubjects).
for v,b,bt,e,et,var in [(2,16,1,17,4.5,False),(1,17,3.5,19,1,True),(0,19,1,20,3,True)]:
 span('cs2',v,at(b,bt),at(e,et),'x*' if var else 'x','Chromatic counterpoint x'+('; adapted opening' if var else ''),'variant' if var else 'statement')
for v,b,bt,e,et,var in [(3,16,1,18,1,False),(2,17,4.5,19,1,True),(1,19,1,21,1,True)]:
 span('cs3',v,at(b,bt),at(e,et),'y*' if var else 'y','Chromatic counterpoint y'+('; variant' if var else ''),'variant' if var else 'statement')
# Conventional-counterpoint derivation: codetta and the imitative episode.
for v,b,bt,e,et in [(2,8,1.5,9,2),(2,11,1.5,11,4),(0,12,3.5,14,3),(1,13,1,15,1),(3,13,3,15,1),(2,14,1,15,3),(1,15,1,16,1)]:
 span('motif',v,at(b,bt),at(e,et),'c*','Countersubject-derived figure','fragment')
# Sequential development and inversion-like material; not complete exact inversions.
for v,b,bt,e,et in [(0,31,2.5,33,1.5),(1,32,1.5,34,1),(0,35,2.5,36,1)]:
 span('motif',v,at(b,bt),at(e,et),'i*','Altered inverted-diminution figure','fragment',True)
for b in [31,32,33]:span('motif',3,at(b,1.5),at(b+1,1.5),'c*','Sequential ascending figure','fragment')
A.sort(key=lambda a:(a['start'],a['voice']))
(R/'data/annotations.json').write_text(json.dumps({'annotations':A},ensure_ascii=False,separators=(',',':')))
print({k:sum(a['kind']==k for a in A) for k in ['subject','cs1','cs2','cs3','motif']})
