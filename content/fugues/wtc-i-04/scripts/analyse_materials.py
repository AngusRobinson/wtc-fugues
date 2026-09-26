"""Thematic spans checked against Keller, Prout, Tovey and the five score parts."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
D=json.loads((R/'data/score.json').read_text());E=D['events'];A=[];occupied=set()
def at(b,o=0):return (b-1)*4+o
def span(kind,v,start,end,label,name,status='statement',inv=False):
 ns=[n for n in E if n['voice']==v and start<=n['start']<end]
 assert ns and ns[0]['start']==start,(kind,v,start,ns[:1])
 assert all(n['start']+n['duration']<=end for n in ns),(kind,v,start,end,[(n['bar'],n['start'],n['duration']) for n in ns if n['start']+n['duration']>end])
 assert not any(n['id'] in occupied for n in ns),(kind,v,start,'overlap')
 A.append(dict(id=f'{kind}-{len(A)+1}',kind=kind,voice=v,start=start,end=end,label=label,name=name,status=status,inverted=inv,notes=[n['id'] for n in ns]));occupied.update(n['id'] for n in ns)
# An asterisk distinguishes altered or incomplete forms from the five-note model.
entries=[
 (4,1,0,4,1,'S1','First subject'),(3,4,0,7,2,'A1','Real answer'),
 (2,7,2,10,2,'S1*','First subject; initial note shortened'),
 (1,12,2,15,2,'A1*','Tonal form of the answer, leading to F sharp minor'),
 (0,14,2,17,3,'S1*','First subject; initial note shortened'),
 (3,19,2,22,1,'S1*','First subject in G sharp minor'),
 (3,22,3,26,1,'S1*','First subject in F sharp minor; initial note shortened'),
 (2,25,2,30,0,'S1*','First subject in C sharp minor; extended close'),
 (4,29,2,33,1,'S1*','First subject in B major'),(2,32,2,35,2,'S1*','First subject in E major'),
 (3,35,2,39,1,'S1*','First subject in C sharp minor'),
 (2,38,2,42,1,'A1*','Answer; extended ending with passing note'),
 (1,44,2,48,2,'S1*','First subject; extended close'),
 (0,48,0,51,1.5,'S1*','First subject in F sharp minor; ornamented initial note'),
 (3,51,2,55,0,'S1*','First subject in F sharp minor'),
 (1,54,2,57,1,'S1*','First subject in A major; ending passes into the third subject'),
 (0,59,0,62,1,'S1*','First subject; ending passes into the third subject'),
 (0,66,0,69,.5,'S1*','First subject in D sharp minor; chromatically altered ending'),
 (4,73,0,76,1,'S1*','First subject; second note displaced by an octave'),
 (0,76,0,80,2,'S1*','First subject; extended ending'),
 (3,81,0,84,1,'S1','First subject'),
 (0,89,0,92,1,'S1*','First subject; closing C sharp also begins the third subject'),
 (0,94,0,96,2,'S1*','First-subject head in stretto; four-note form'),
 (1,95,2,98,0,'S1*','First-subject head in stretto; four-note form'),
 (0,96,2,98,1,'S1*','First-subject head in stretto; four-note form'),
 (4,97,2,100,1,'S1*','First subject in stretto; initial note shortened'),
 (3,100,0,102,1,'S1*','First-subject head; three-note fragment'),
 (0,107,0,110,0,'S1*','First subject over the dominant pedal; third note syncopated'),
 (1,112,2,116,0,'S1*','Final subdominant entry; last note retained as the fifth of the tonic chord')]
for v,b,o,e,eo,l,n in entries:span('subject',v,at(b,o),at(e,eo),l,n,'variant' if '*' in l else 'statement')
# S3: the repeated-note core, with tied continuations and available tonic resolution.
# A resolution already beginning the next theme is assigned to that new theme.
heads={0:[(52,1),(62,1),(92,1),(99,1)],1:[(57,1),(67,1),(77,1),(85,1),(93,1),(98,1),(107,1)],2:[(49,1),(64,1),(69,1),(82,1),(95,1),(97,1),(107,1)],3:[(60,1),(74,1),(84,1),(94,1),(96,1),(98,3),(102,1),(105,1),(108,1)],4:[(55,1),(65,1),(79,1),(86,1),(90,1),(100,1)]}
for v,starts in heads.items():
 for b,o in starts:
  ns=[n for n in E if n['voice']==v and n['start']>=at(b,o)][:7]
  end=ns[-1]['start']+ns[-1]['duration']
  rest=[n for n in E if n['voice']==v and n['start']>=end]
  for n in rest:
   if n['start']!=end or n['id'] in occupied:break
   if n['tied'] and n['pitch']==ns[-1]['pitch']:end=n['start']+n['duration']
   elif n['diatonic']==ns[0]['diatonic']+3:
    end=n['start']+n['duration'];break
   else:break
  # The last repeated-note entry becomes the three-note S1 head at 100.
  if v==3 and b==98:end=at(100)
  pitches=[n['diatonic']-ns[0]['diatonic'] for n in ns]
  var=pitches!=[0,3,3,3,2,1,2] or [n['duration'] for n in ns]!=[1,1,1,1,.5,.5,2]
  span('subject3',v,at(b,o),end,'S3'+('*' if var else ''),'Third subject'+('; adapted' if var else ''),'variant' if var else 'statement')
span('subject3',2,at(113,1),at(116),'S3*','Third subject; broadened final cadence','variant')
# S2 is a sequential strand: its length changes with the accompanying entries.
strands=[(0,35,1,41,2.5,False,False),(3,41,0,45,0,True,False),
 (4,44,1,49,2,False,True),(0,47,0,48,0,False,True),
 (1,49,0,51,2.5,False,True),(2,51,1,59,0,False,False),
 (0,57,1.5,59,0,False,True),(1,59,1,65,2,False,True),
 (4,66,2.5,69,0,False,True),(0,69,.5,71,2,False,True),
 (2,72,0,77,2,False,True),(4,76,1,79,1,False,True),
 (1,79,0,82,1,False,True),(0,81,1,88,2,False,True),
 (1,89,2.5,92,1,False,True),(3,92,0,94,1,False,True)]
for v,b,o,e,eo,inv,var in strands:span('subject2',v,at(b,o),at(e,eo),'S2'+('i' if inv else '')+('*' if var else ''),'Second subject'+(' in inversion' if inv else '')+('; varied or curtailed' if var else ''),'variant' if var else 'statement',inv)
# Early stepwise figure: exact diatonic/rhythmic recurrences, including diminution.
for v in range(5):
 line=[n for n in E if n['voice']==v and n['bar']<35]
 for i in range(len(line)-3):
  ns=line[i:i+4]
  if any(n['id'] in occupied for n in ns):continue
  rhythm=[n['duration'] for n in ns]
  if rhythm not in [[1]*4,[.5]*4]:continue
  if any(a['start']+a['duration']!=b['start'] for a,b in zip(ns,ns[1:])):continue
  shape=[n['diatonic']-ns[0]['diatonic'] for n in ns]
  if shape not in [[0,-1,-2,-3],[0,1,2,3]]:continue
  inv=shape[1]==1;dim=rhythm[0]==.5
  span('motif',v,ns[0]['start'],ns[-1]['start']+ns[-1]['duration'],'d'+('i' if inv else '')+('/2' if dim else ''),'Stepwise crotchet figure'+(' in inversion' if inv else '')+(' and diminution' if dim else ''),'fragment',inv)
A.sort(key=lambda a:(a['start'],a['voice']))
(R/'data/annotations.json').write_text(json.dumps({'annotations':A},ensure_ascii=False,separators=(',',':')))
print({k:sum(a['kind']==k for a in A) for k in ['subject','subject2','subject3','motif']})
