"""Musician-facing thematic annotations shared by the page and PDF."""
import json,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]
s=json.loads((R/'data/score.json').read_text());ev=s['events']
anns=[]
def add(kind,voice,start,end,label,inverted=False,status='statement',basis=''):
 ns=[n for n in ev if n['voice']==voice and start<=n['start']<end]
 if not ns:return
 # A nominal selection window identifies the notes; the map must include the
 # complete final note, and must not extend a cell through its following rest.
 end=max(n['start']+n['duration'] for n in ns)
 anns.append(dict(id='a'+str(len(anns)),kind=kind,voice=voice,start=start,end=end,label=label,inverted=inverted,status=status,notes=[n['id'] for n in ns],basis=basis))
for e in s['entries']:
 add('subject',e['voice'],e['start'],e['end'],'S'+('i' if e['inverted'] else '')+('*' if e['altered'] else ''),e['inverted'],'variant' if e['altered'] else 'statement','Principal subject entry; local melodic adjustments included. Closing paired entries adapted.')
for v,a,b,inv,status in [(1,25,49,False,'statement'),(1,61,85,False,'statement'),(3,97,120,False,'variant'),(1,247,266,True,'truncated'),(2,271,289,True,'truncated'),(1,307,323,True,'truncated'),(0,349,361,True,'fragment')]:
 add('cs1',v,a,b,'CS1'+('i' if inv else '')+('*' if status!='statement' else ''),inv,status,'Chromatic countersubject: ascending or descending semitone cells and sustained arrival.')
add('cs2',0,61,85,'CS2',basis='Keller\'s second counterpoint: melodic opening and detached crotchets against the subject\'s quavers.')
add('cs2',0,96,121,'CS2*',status='variant',basis='Varied continuation in the soprano: altered opening and sustained notes at the central crotchet cell.')
add('cs2',1,103,115,'CS2*',status='fragment',basis='Alto fragment: melodic turn in bar 18 followed by the detached crotchet cell in bar 19.')
# Readily identifiable detached-crotchet cells, without claiming a complete CS2.
for v,bar,q in [(0,29,2),(2,35,2),(0,44,0),(3,44,0),(3,48,0),(2,54,0),(1,60,0),(2,60,0),(0,75,0),(0,91,0)]:
 st=(bar-1)*6+q
 ns=[n for n in ev if n['voice']==v and st<=n['start']<st+6 and not n['tied']]
 assert len(ns)>=3 and [n['start']-st for n in ns[:3]]==[0,2,4],(v,bar,ns)
 assert all(n['duration']==1 for n in ns[:3]),(v,bar,ns)
 add('motif',v,st,st+5,'c2',status='fragment',basis='CS2 detached-crotchet cell; pitches vary with the counterpoint.')
# A late chromatic cell, not a renewed complete countersubject.
add('motif',1,487,494,'c1i',True,'fragment','Descending chromatic cell from the second limb of CS1; bar 82 into 83.')
occupied={nid for a in anns for nid in a['notes']}
voices={v:[n for n in ev if n['voice']==v and not n['tied']] for v in range(4)}
for v,ns in voices.items():
 for i in range(len(ns)-4):
  z=ns[i:i+5];t=z[0]['start']
  if [n['start']-t for n in z]!=[0,1,2,2.5,3] or any(n['id'] in occupied for n in z):continue
  ds=[n['diatonic']-z[1]['diatonic'] for n in z]
  for direction in [1,-1]:
   if ds[0]*direction in [3,4] and [d*direction for d in ds[1:]]==[0,1,2,1]:
    add('motif',v,t,z[-1]['start']+z[-1]['duration'],'s'+('i' if direction<0 else ''),direction<0,'fragment','Subject-tail derivative: leap, ascending or descending quaver turn, closing step; initial leap adapted.')
    occupied.update(n['id'] for n in z)
# Sequential repetitions of the suspensive tail of CS1.
for v,ns in voices.items():
 for i in range(len(ns)-3):
  z=ns[i:i+4];t=z[0]['start']
  if [n['start']-t for n in z]!=[0,.5,1,4] or any(n['id'] in occupied for n in z):continue
  if [n['duration'] for n in z[:3]]!=[.5,.5,2]:continue
  ds=[n['diatonic']-z[0]['diatonic'] for n in z]
  if ds[:3] not in [[0,-1,0],[0,1,0]] or abs(z[3]['pitch']-z[0]['pitch'])>2:continue
  inv=ds[1]>0
  add('motif',v,t,z[-1]['start']+z[-1]['duration'],'t1'+('i' if inv else ''),inv,'fragment','Sequential derivative of the CS1 suspension/turn ending.')
  occupied.update(n['id'] for n in z)
anns.sort(key=lambda a:(a['start'],a['voice']))
out={'annotations':anns,'legend':{'subject':'S / Si','cs1':'CS1 / CS1i','cs2':'CS2','motif':'s · c1 · c2 · t1'},'notes':'i = inversion; * = variant, truncated statement or fragment. Lower-case tags identify detached cells, not complete countersubjects. CS2 is less consistent than CS1.'}
(R/'data/annotations.json').write_text(json.dumps(out,ensure_ascii=False,separators=(',',':')))
for a in anns:
 if a['kind']!='subject':print(a['label'],['S','A','T','B'][a['voice']],int(a['start']//6)+1,a['start']%6,'-',int((a['end']-.001)//6)+1,a['status'])
print('Total',len(anns))
