"""Analytical spans: Keller's counterpoints; scale links and thematic fragments."""
import json,argparse
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);R=p.parse_args().root
E=json.loads((R/'data/score.json').read_text())['events'];A=[];occupied=set()
def span(kind,voice,start,end,label,name,status='statement',inverted=False):
 notes=[n for n in E if n['voice']==voice and start<=n['start']<end and not (kind=='subject' and n['id'].endswith('S2'))]
 assert notes and notes[0]['start']==start,(label,start)
 assert not any(n['id'] in occupied for n in notes),(kind,start)
 aid=f'{kind}-{len(A)+1}';A.append(dict(id=aid,kind=kind,voice=voice,start=start,end=end,label=label,name=name,inverted=inverted,status=status,notes=[n['id'] for n in notes]))
 occupied.update(n['id'] for n in notes)
for v,s,e,label,name in [(1,.5,8.25,'S','Subject'),(0,8.5,16.5,'A','Tonal answer'),(2,24.5,32.25,'S','Subject'),(0,40.5,48.25,'S','Subject in E♭ major'),(1,56.5,64.5,'A','Answer-form entry in G minor'),(0,76.5,84.5,'S','Subject'),(2,102.5,111,'S','Subject; displaced by half a bar'),(0,114.5,124,'S*','Subject; major closing third')]:span('subject',v,s,e,label,name,'variant' if s==114.5 else 'statement')
# Keller's quaver counterpoint excludes the intervening descending scale.
for v,s,e in [(1,10.5,17),(0,26.5,32.5),(2,42.5,48.5),(0,58.5,64.5),(1,78.5,85),(1,104.5,111)]:
 span('cs1',v,s,e,'CS1*' if s==104.5 else 'CS1','Countersubject 1'+('; cadential variant' if s==104.5 else ''),'variant' if s==104.5 else 'statement')
for v,s,e in [(1,26.5,33),(1,42.5,48.5),(2,58.5,64.5),(2,78.5,84.25),(0,104.5,111)]:
 span('cs2',v,s,e,'CS2' if s==26.5 else 'CS2*','Countersubject 2'+('' if s==26.5 else '; variant'),'statement' if s==26.5 else 'variant')
# Scale links and their sequential developments. Arrows indicate direction,
# not an exact interval-for-interval inversion of the complete countersubject.
for v,s,e in [(1,8.25,10.5),(0,24.5,26.5),(2,40.25,42.5),(0,56,58.5),(1,76.25,78.5),(0,102.25,104.5)]:
 span('motif',v,s,e,'d','Descending scale link','cell')
for v,s,e,lab,name in [(1,17.25,23,'d↑*','Ascending scale sequence'),(2,32.25,40.25,'d*','Descending scale sequence'),(0,48.25,56,'d↑*','Ascending scale sequence'),(1,65.25,70,'d↑*','Ascending scale sequence'),(2,71.25,76.5,'d↑*','Scale sequence, transferred to bass'),(2,84.25,94.5,'d*','Descending scale sequence'),(2,95.25,102.5,'d↑*','Scale sequence and dominant approach')]:
 span('motif',v,s,e,lab,name,'fragment')
# The quaver counterpoint in thirds in bars 13-15 derives from CS1.
for v in [1,2]:span('motif',v,48.5,56.5,'q*','Quaver counterpoint derived from CS1','fragment')
# The added soprano isolates the three-note head in thirds or tenths.
for q in [64.5,66.5,68.5,70.5,72.5,74.5]:span('motif',0,q,q+1,'h*','Subject-head fragment; upper third or tenth','fragment')
# Short subject-head cells: exact semiquaver/quaver rhythm and lower neighbour.
# Complete entries and counterpoints take priority over fragment labels.
for voice in range(3):
 seq=sorted([n for n in E if n['voice']==voice],key=lambda n:n['start'])
 for i in range(len(seq)-3):
  ns=seq[i:i+4]
  if any(n['id'] in occupied for n in ns):continue
  if [n['duration'] for n in ns]!=[.25,.25,.5,.5]:continue
  if any(a['start']+a['duration']!=b['start'] for a,b in zip(ns,ns[1:])):continue
  d=[n['diatonic'] for n in ns]
  if d[1]!=d[0]-1 or d[2]!=d[0] or d[3]>d[0]-2:continue
  s=ns[0]['start']
  if not any(a<=s<b for a,b in [(16.5,24),(32.5,40.5),(48.25,56),(64.5,76.25),(84.5,102.25)]):continue
  span('motif',voice,s,ns[-1]['start']+.5,'h*','Subject-head fragment','fragment')
A.sort(key=lambda a:(a['start'],a['voice']))
(R/'data/annotations.json').write_text(json.dumps({'annotations':A},ensure_ascii=False,separators=(',',':')))
print('Annotations:',{k:sum(a['kind']==k for a in A) for k in ['subject','cs1','cs2','motif']})
