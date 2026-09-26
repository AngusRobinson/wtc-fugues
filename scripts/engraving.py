"""Shared engraving conventions; preserve sounding notes and silence durations."""
import re
import xml.etree.ElementTree as ET
M='{http://www.music-encoding.org/ns/mei}';V='{http://www.w3.org/2000/svg}';ID='{http://www.w3.org/XML/1998/namespace}id';NS={'m':M[1:-1]}

def tidy_score(root,notes,keyboard=False,work=''):
 # MEI distinguishes a croix double sharp (x) from two separate sharps (ss).
 for el in root.iter():
  if el.get('accid')=='ss':el.set('accid','x')
 # The added filling part in BWV 860 needs no rests before/between its notes.
 if work=='wtc-i-15':
  for el in root.iter():
   if el.get(ID) in {'rest-L1072F5','rest-L1084F5','rest-L1086F5','rest-L1089F5'}:el.tag=M+'space';el.attrib.pop('visible',None)
 directions={}
 meter=root.find('.//m:scoreDef//m:meterSig',NS)
 bar_length=int(meter.get('count'))*4/int(meter.get('unit')) if meter is not None else 4
 for measure in root.findall('.//m:measure',NS):
  for staff in measure.findall(M+'staff'):
   layers=staff.findall(M+'layer');active=[l for l in layers if l.findall('.//m:note',NS)]
   # Whole-bar silences belong to the staff only when every part is silent.
   shown=False
   for layer in layers:
    for rest in layer.findall('.//m:mRest',NS):
     rest.set('visible','false' if active or shown else 'true');shown=True
     for attr in ['loc','ploc','oloc']:rest.attrib.pop(attr,None)
   if len(layers)<2:continue
   mean=lambda l:sum(notes[n.get(ID)]['pitch'] for n in l.findall('.//m:note',NS))/len(l.findall('.//m:note',NS))
   for layer in active:
    rank=active.index(layer);direction=None
    if len(active)>1:
     direction='up' if rank==0 else 'down'
     if 0<rank<len(active)-1:
      pitch=mean(layer);direction='up' if abs(pitch-mean(active[-1]))<abs(pitch-mean(active[0])) else 'down'
    for n in layer.iter():
     if n.tag in [M+'note',M+'chord']:
      if direction:n.set('stem.dir',direction)
      else:n.attrib.pop('stem.dir',None)
     if n.tag==M+'note':directions[n.get(ID)]=direction
    # Place a polyphonic rest outside the neighbouring sounding notes, not
    # at a fixed staff position that can coincide with those notes.
    if direction:
     cursor=(int(measure.get('n'))-1)*bar_length
     def leaves(parent):
      for child in parent:
       if child.tag in [M+'note',M+'chord',M+'rest',M+'space',M+'mRest']:yield child
       else:yield from leaves(child)
     staff_notes=[notes[n.get(ID)] for n in staff.findall('.//m:note',NS)]
     own={n.get(ID) for n in layer.findall('.//m:note',NS)}
     bottom=30 if keyboard and staff.get('n')=='1' or not keyboard and staff.get('n')=='1' else 18
     for el in leaves(layer):
      if el.tag in [M+'note',M+'chord']:
       es=[notes[el.get(ID)]] if el.tag==M+'note' else [notes[n.get(ID)] for n in el.findall(M+'note')]
       cursor=max(n['start']+n['duration'] for n in es);continue
      dur=bar_length if el.tag==M+'mRest' else 4/int(el.get('dur','1'))*sum(.5**j for j in range(int(el.get('dots','0'))+1))
      if el.tag==M+'rest':
       other=[n['diatonic']-bottom for n in staff_notes if n['id'] not in own and n['start']<cursor+dur and n['start']+n['duration']>cursor]
       loc=(max(8,max(other,default=4)+6)+1)//2*2 if direction=='up' else (min(0,min(other,default=4)-4))//2*2
       for attr in ['ploc','oloc']:el.attrib.pop(attr,None)
       el.set('loc',str(loc))
      cursor+=dur
  for tie in measure.findall(M+'tie'):
   direction=directions.get(tie.get('startid','')[1:])
   if direction:tie.set('curvedir','above' if direction=='up' else 'below')
   else:tie.attrib.pop('curvedir',None)
  if keyboard:
   seen=set()
   for fermata in measure.findall(M+'fermata'):
    key=(fermata.get('staff'),notes.get(fermata.get('startid','')[1:],{}).get('start',fermata.get('tstamp')))
    if key in seen:measure.remove(fermata)
    else:seen.add(key);fermata.set('place','above')
 return root

def finish_svg(svg):
 """Reserve the existing upper page margin for a consistent bar-number row."""
 root=ET.fromstring(svg)
 for group in root.iter():
  if 'mNum' not in group.get('class','').split():continue
  group.set('data-bar-number','true')
  for text in group.findall(V+'text'):
   text.set('y','-100');text.set('font-family','Arial, sans-serif');text.set('font-style','normal')
   for span in text.iter():
    if span.get('font-size') and span.get('font-size')!='0px':span.set('font-size','300px')
 ET.register_namespace('',V[1:-1]);ET.register_namespace('xlink','http://www.w3.org/1999/xlink')
 return re.sub(r'>\s+<','><',ET.tostring(root,encoding='unicode'))
