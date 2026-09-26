"""Engrave annotated open/keyboard scores and isolated thematic examples."""
import copy,json,re,argparse
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[4]/'scripts'))
from engraving import tidy_score,finish_svg
import xml.etree.ElementTree as ET
import verovio
p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--examples-only',action='store_true');args=p.parse_args();R=args.root
TEMP=(R.parents[2]/'tmp'/R.name) if R.parent.name=='fugues' else R/'tmp'
TEMP.mkdir(parents=True,exist_ok=True)
M='{http://www.music-encoding.org/ns/mei}';V='{http://www.w3.org/2000/svg}';ID='{http://www.w3.org/XML/1998/namespace}id';NS={'m':M[1:-1]}
ET.register_namespace('',M[1:-1]);ET.register_namespace('xlink','http://www.w3.org/1999/xlink')
source=ET.parse(R/'sources/bwv867-5-voices.mei').getroot()
notes={n['id']:n for n in json.loads((R/'data/score.json').read_text())['events']}
anns=json.loads((R/'data/annotations.json').read_text())['annotations'];members={nid:a for a in anns for nid in a['notes']}
colours={'subject':'#244f91','head':'#637878','motif':'#637878','sequence':'#8a6548'}
ranges=[(a,min(a+4,75)) for a in range(1,76,5)]
low_alto=set()
def keyboard_staff(v,bar):return 1 if v in [0,1] or (v==2 and bar not in low_alto) else 2
def serial(root):
 ET.register_namespace('',M[1:-1]);return ET.tostring(root,encoding='unicode')
def prefix_svg(svg,prefix,interactive=False):
 ET.register_namespace('',V[1:-1])
 rr=ET.fromstring(finish_svg(svg));old=rr.get('id')
 for g in rr.iter():
  nid=g.get('id','')
  if interactive and nid in notes:
   n=notes[nid];g.set('data-note-id',nid);g.set('data-time',str(n['start']));g.set('data-voice',str(n['voice']))
   ann=members.get(nid)
   if ann:
    g.set('class',g.get('class','')+' material material-'+ann['kind']);g.set('data-kind',ann['kind']);g.set('data-annotation-id',ann['id'])
  # Refine individual tie bows where the default curve meets a passing
  # note or accidental; preserve each tie's connection to its written notes.
  tie_id=nid or next((x.removeprefix('id-') for x in g.get('class','').split() if x.startswith('id-tie-')),'')
  adjustments={'tie-L202F5-L208F5':-630,'tie-L71F4-L75F4':270,
               'tie-L103F4-L106F4':-80,'tie-L116F4-L122F4':0}
  if prefix.startswith('keyboard-') and nid and tie_id in adjustments:
   path=g.find(V+'path');a=list(map(float,re.findall(r'-?\d+(?:\.\d+)?',path.get('d'))))
   assert len(a)==14
   for index in (3,5,9,11):a[index]+=adjustments[tie_id]
   if tie_id=='tie-L103F4-L106F4':
    a[3]=a[5]=a[1]+15;a[9]=a[11]=a[1]+45
   if tie_id=='tie-L202F5-L208F5':a[7]-=100
   if tie_id=='tie-L116F4-L122F4':
    # The upper adjacent note at bar 19 projects to the left of the tied
    # notehead. End the tie at the latter's lower-left edge.
    a[6]-=90;a[7]+=65
   path.set('d',f'M{a[0]:g},{a[1]:g} C{a[2]:g},{a[3]:g} {a[4]:g},{a[5]:g} {a[6]:g},{a[7]:g} C{a[8]:g},{a[9]:g} {a[10]:g},{a[11]:g} {a[12]:g},{a[13]:g}')
  if nid.startswith('mark-'):
   aid=nid.removeprefix('mark-').rsplit('-',1)[0];ann=next(a for a in anns if a['id']==aid)
   g.set('class',g.get('class','')+' annotation-label material-'+ann['kind']);g.set('data-kind',ann['kind']);g.set('data-annotation-id',aid)
  if g.tag==V+'style' and g.text:g.text=g.text.replace('#'+old,'#'+prefix+old)
  if g.get('id'):g.set('id',prefix+g.get('id'))
  for attr in ['href','{http://www.w3.org/1999/xlink}href']:
   if g.get(attr,'').startswith('#'):g.set(attr,'#'+prefix+g.get(attr)[1:])
 return re.sub(r'>\s+<','><',ET.tostring(rr,encoding='unicode'))
def root_score():
 root=copy.deepcopy(source);sd=root.find('.//m:scoreDef',NS)
 for h in sd.findall(M+'pgHead'):sd.remove(h)
 for n in root.findall('.//m:note',NS):
  ann=members.get(n.get(ID))
  if ann:n.set('color',colours[ann['kind']])
 for staff in root.findall('.//m:measure/m:staff',NS):
  for layer in staff.findall(M+'layer'):
   if not layer.findall('.//m:note',NS):
    for child in list(layer):layer.remove(child)
    ET.SubElement(layer,M+'mRest',{ID:'rest-'+staff.get(ID,'')+'-'+layer.get('n','1')})
 return root

def keyboard(root):
 sd=root.find('.//m:scoreDef',NS)
 for c in list(sd):sd.remove(c)
 group=ET.SubElement(sd,M+'staffGrp',{'symbol':'brace','bar.thru':'true'})
 for sn,clef,line in [(1,'G','2'),(2,'F','4')]:
  st=ET.SubElement(group,M+'staffDef',{'n':str(sn),'lines':'5'})
  ET.SubElement(st,M+'clef',{'shape':clef,'line':line});ET.SubElement(st,M+'keySig',{'sig':'5f','mode':'minor','pname':'b'});ET.SubElement(st,M+'meterSig',{'count':'2','unit':'2'})
 for m in root.findall('.//m:measure',NS):
  old=m.findall(M+'staff');assert len(old)==5
  for st in old:m.remove(st)
  bar=int(m.get('n'))
  distribution=[(1,[0,1]),(2,[2,3,4])] if bar in low_alto else [(1,[0,1,2]),(2,[3,4])]
  for sn,vs in distribution:
   staff=ET.Element(M+'staff',{'n':str(sn),ID:f'keyboard-staff-{m.get("n")}-{sn}'});m.insert(sn-1,staff)
   layers=[l for v in vs for l in old[v].findall(M+'layer')];active=[bool(l.findall('.//m:note',NS)) for l in layers]
   for i,layer in enumerate(layers):
    layer.set('n',str(i+1))
    for parent in layer.iter():
     for child in list(parent):
      if child.tag==M+'clef':parent.remove(child)
    if len(layers)>1:
     for n in layer.iter():
      if n.tag in [M+'note',M+'chord']:n.set('stem.dir','up' if i==0 else 'down')
     if not active[i] and (any(active) or i==1):
      for rest in layer.findall('.//m:mRest',NS):rest.set('visible','false')
    staff.append(layer)
   # Recalculate displayed cancellations where voices share a stave.
   state={};bytime={}
   for note in staff.findall('.//m:note',NS):bytime.setdefault(notes[note.get(ID)]['start'],[]).append(note)
   for q,ns in sorted(bytime.items()):
    updates={}
    for note in ns:
     e=notes[note.get(ID)];key=(note.get('pname'),note.get('oct'));acc=note.find(M+'accid');target=acc if acc is not None else note
     alt={'ff':-2,'f':-1,'n':0,'s':1,'ss':2}[target.get('accid.ges')];before=state.get(key,-1 if key[0] in 'beadg' else 0)
     if not e['tied'] and before!=alt:target.set('accid',{-2:'ff',-1:'f',0:'n',1:'s',2:'ss'}[alt])
     updates[key]=alt
    state.update(updates)
  for c in list(m):
   if c.tag==M+'staff':continue
   if c.get('staff'):c.set('staff',str(keyboard_staff(int(c.get('staff'))-1,bar)))
   if c.tag==M+'tie':
    v=notes[c.get('startid')[1:]]['voice'];c.set('curvedir','below' if v in [1,4] or (v==2 and bar not in low_alto) or (v==3 and bar in low_alto) else 'above')
 return root

def complete(is_keyboard):
 root=root_score()
 if is_keyboard:root=keyboard(root)
 else:
  for st in root.findall('.//m:staffDef',NS):
   v=int(st.get('n'))-1
   ET.SubElement(st,M+'label').text=['Soprano I','Soprano II','Alto','Tenor','Bass'][v];ET.SubElement(st,M+'labelAbbr').text=['SI','SII','A','T','B'][v]
 sec=root.find('.//m:section',NS)
 for start,end in ranges:
  m=sec.find(f'm:measure[@n="{start}"]',NS)
  if start>1:sec.insert(list(sec).index(m),ET.Element(M+'pb'))
  for ann in anns:
   ns=[notes[n] for n in ann['notes'] if start<=notes[n]['bar']<=end]
   if not ns:continue
   # A single closing note needs its colour, not another crowded label.
   if ann['start']<(start-1)*4 and ann['end']-(start-1)*4<=1:continue
   first=ns[0];v=ann['voice'];m=sec.find(f'm:measure[@n="{first["bar"]}"]',NS)
   staff=keyboard_staff(v,first['bar'])
   d=ET.SubElement(m,M+'dir',{ID:f'mark-{ann["id"]}-{start}','staff':str(staff if is_keyboard else v+1),'startid':'#'+first['id'],'place':'below' if is_keyboard and (v in [1,4] or (v==2 and first['bar'] not in low_alto) or (v==3 and first['bar'] in low_alto)) else 'above','color':colours[ann['kind']]})
   text=ann['label']+(' >' if ann['start']<(start-1)*4 else '')
   ET.SubElement(d,M+'rend',{'fontfam':'Arial','fontweight':'bold','fontstyle':'normal','fontsize':'small'}).text=text
 assert {n.get(ID) for n in root.findall('.//m:note',NS)}==set(notes)
 assert len(root.findall('.//m:tie',NS))==len(source.findall('.//m:tie',NS))==68
 tidy_score(root,notes,is_keyboard,R.name)
 if is_keyboard:
  # Soprano II lies below the alto in this passage. Keep its sustained
  # B-flat ties outside the texture, irrespective of the source layer order.
  for bar in range(30,34):
   measure=root.find(f'.//m:measure[@n="{bar}"]',NS)
   for tie in measure.findall(M+'tie'):
    if notes[tie.get('startid')[1:]]['voice']==1:tie.set('curvedir','below')
  # Other inner-part ties need the clear side of the surrounding notes.
  tie_sides={'tie-L71F4-L75F4':'below','tie-L103F4-L106F4':'below',
             'tie-L116F4-L122F4':'above','tie-L320F4-L325F4':'above'}
  for tie in root.findall('.//m:tie',NS):
   if tie.get(ID) in tie_sides:tie.set('curvedir',tie_sides[tie.get(ID)])
  # The second soprano's crotchet rest belongs between the sounding outer
  # parts, below soprano I's B-flat, rather than above the top voice.
  rest=root.find('.//m:rest[@xml:id="rest-L312F4"]',dict(NS,xml='http://www.w3.org/XML/1998/namespace'))
  assert rest is not None
  rest.set('loc','4')
 mode='keyboard' if is_keyboard else 'open'
 (TEMP/f'{mode}.mei').write_text(serial(root))
 tk=verovio.toolkit();tk.setOptions({'inputFrom':'mei','pageWidth':2500 if is_keyboard else 2700,'pageHeight':20000,'scale':40,'adjustPageHeight':True,'header':'none','footer':'none','svgViewBox':True,'breaks':'encoded','xmlIdSeed':867,'mnumInterval':1,'spacingStaff':16 if is_keyboard else 10})
 assert tk.loadData(serial(root));assert tk.getPageCount()==len(ranges),(mode,tk.getPageCount())
 tk.renderToMIDI()
 for nid,e in notes.items():
  actual=tk.getMIDIValuesForElement(nid);assert actual['pitch']==e['pitch'],(mode,nid,actual,e)
  assert abs(actual['time']-e['start']*60000/126)<2,(mode,nid)
 systems=[];rendered=[]
 for page,(a,b) in enumerate(ranges,1):
  svg=tk.renderToSVG(page);rr=ET.fromstring(svg)
  rendered.extend(g.get('id') for g in rr.iter() if g.get('id') in notes)
  systems.append({'start':a,'end':b,'svg':prefix_svg(svg,f'{mode}-{a}-',not is_keyboard)})
 assert len(rendered)==len(set(rendered))==813
 (TEMP/f'{mode}-systems.json').write_text(json.dumps(systems,ensure_ascii=False,separators=(',',':')))
 if not is_keyboard:(R/'data/annotated-systems.json').write_text(json.dumps(systems,ensure_ascii=False,separators=(',',':')))
 print(mode,': all 813 notes and 68 ties preserved.',flush=True)

def examples():
 out=[]
 for kind,a,b,voice,start,end in [('subject',1,4,0,0,13),('motif',2,3,0,5,9),('sequence',4,6,0,13,24)]:
  root=tidy_score(root_score(),notes,False,R.name);sd=root.find('.//m:scoreDef',NS);group=sd.find(M+'staffGrp');group.set('symbol','none')
  # Flatten staff groups if the input importer nests the two keyboard staves.
  defs=sd.findall('.//m:staffDef',NS)
  for child in list(sd):sd.remove(child)
  group=ET.SubElement(sd,M+'staffGrp',{'symbol':'none'})
  for st in defs:
   if voice is None or int(st.get('n'))==voice+1:
    selected=copy.deepcopy(st)
    if voice is not None:selected.set('n','1')
    group.append(selected)
  sec=root.find('.//m:section',NS)
  for m in list(sec):
   if m.tag!=M+'measure' or not a<=int(m.get('n'))<=b:sec.remove(m);continue
   for st in list(m.findall(M+'staff')):
    if voice is not None:
     if int(st.get('n'))!=voice+1:m.remove(st)
     else:st.set('n','1')
   for n in m.findall('.//m:note',NS):n.set('color',colours[kind] if start<=notes[n.get(ID)]['start']<end else '#a2a8b0')
  if voice is not None:
   last=sec.findall(M+'measure')[-1]
   if end<(b-1)*4+4:
    layer=last.find('.//m:layer',NS)
    def trim(parent):
     for child in list(parent):
      if child.tag==M+'note' and notes[child.get(ID)]['start']>=end:parent.remove(child)
      else:
       trim(child)
       if child.tag in [M+'beam',M+'tuplet'] and not child.findall('.//m:note',NS):parent.remove(child)
       elif child.tag==M+'beam' and len(child.findall('.//m:note',NS))==1:
        # A cropped beam must become a flagged note, not an isolated beam stub.
        index=list(parent).index(child)
        for item in list(child):parent.insert(index,item);index+=1
        parent.remove(child)
    trim(layer);last.set('metcon','false')
  ids={n.get(ID) for n in root.iter()}
  for m in sec:
   for c in list(m):
    if any(c.get(k,'').startswith('#') and c.get(k)[1:] not in ids for k in ['startid','endid']):m.remove(c)
    elif c.get('staff') and voice is not None:c.set('staff','1')
  tk=verovio.toolkit();tk.setOptions({'inputFrom':'mei','pageWidth':2200 if kind=='subject' else 1800,'pageHeight':5000,'scale':40,'adjustPageHeight':True,'header':'none','footer':'none','svgViewBox':True,'breaks':'none','xmlIdSeed':1867,'mnumInterval':1})
  assert tk.loadData(serial(root))
  out.append({'id':kind,'start':start,'svg':prefix_svg(tk.renderToSVG(1),'theme-'+kind+'-')})
 (R/'data/thematic-examples.json').write_text(json.dumps(out,ensure_ascii=False,separators=(',',':')))
 print('Thematic examples complete.',flush=True)
if not args.examples_only:complete(False);complete(True)
examples()
