"""Engrave annotated open/keyboard scores and isolated thematic examples."""
import copy,json,re,argparse
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[4]/'scripts'))
from engraving import tidy_score,finish_svg
import xml.etree.ElementTree as ET
import verovio
p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);R=p.parse_args().root
TEMP=R.parents[2]/'tmp'/R.name 
TEMP.mkdir(parents=True,exist_ok=True)
M='{http://www.music-encoding.org/ns/mei}';V='{http://www.w3.org/2000/svg}';ID='{http://www.w3.org/XML/1998/namespace}id';NS={'m':M[1:-1]}
ET.register_namespace('',M[1:-1]);ET.register_namespace('xlink','http://www.w3.org/1999/xlink')
source=ET.parse(R/'sources/bwv848-three-voices.mei').getroot()
notes={n['id']:n for n in json.loads((R/'data/score.json').read_text())['events']}
anns=json.loads((R/'data/annotations.json').read_text())['annotations'];members={nid:a for a in anns for nid in a['notes']}
TIE_ROUTES=json.loads((R/'scripts/tie_routes.json').read_text())
colours={'subject':'#244f91','cs1':'#a45112','cs2':'#843d7c','motif':'#637878'}
ranges=[(a,min(a+3,55)) for a in range(1,56,4)]
def serial(root):
 ET.register_namespace('',M[1:-1]);return ET.tostring(root,encoding='unicode')
def prefix_svg(svg,prefix,interactive=False):
 ET.register_namespace('',V[1:-1])
 rr=ET.fromstring(finish_svg(svg));old=rr.get('id')
 for g in rr.iter():
  nid=g.get('id','')
  route=TIE_ROUTES.get(prefix+nid)
  if route:
   for path in g.findall(V+'path'):path.set('d',route['d'])
  if interactive and nid in notes:
   n=notes[nid];g.set('data-note-id',nid);g.set('data-time',str(n['start']));g.set('data-voice',str(n['voice']))
   ann=members.get(nid)
   if ann:
    g.set('class',g.get('class','')+' material material-'+ann['kind']);g.set('data-kind',ann['kind']);g.set('data-annotation-id',ann['id'])
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
 return root

LOW_ALTO=set(range(12,16))|set(range(20,25))|{27}|set(range(31,35))|set(range(52,56))
def staff_for(v,b):return 2 if v==2 or v==1 and b in LOW_ALTO else 1
def keyboard(root):
 sd=root.find('.//m:scoreDef',NS)
 for c in list(sd):sd.remove(c)
 group=ET.SubElement(sd,M+'staffGrp',{'symbol':'brace','bar.thru':'true'})
 for sn,clef,line in [(1,'G','2'),(2,'F','4')]:
  st=ET.SubElement(group,M+'staffDef',{'n':str(sn),'lines':'5'})
  ET.SubElement(st,M+'clef',{'shape':clef,'line':line});ET.SubElement(st,M+'keySig',{'sig':'7s','mode':'major','pname':'c'});ET.SubElement(st,M+'meterSig',{'count':'4','unit':'4'})
 for m in root.findall('.//m:measure',NS):
  old=m.findall(M+'staff');assert len(old)==3
  for st in old:m.remove(st)
  for sn in [1,2]:
   vs=[v for v in range(3) if staff_for(v,int(m.get('n')))==sn]
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
     alt={'ff':-2,'f':-1,'n':0,'s':1,'ss':2,'x':2}[target.get('accid.ges')];before=state.get(key,1)
     if not e['tied'] and before!=alt:target.set('accid',{-2:'ff',-1:'f',0:'n',1:'s',2:'ss'}[alt])
     updates[key]=alt
    state.update(updates)
  for c in list(m):
   if c.tag==M+'staff':continue
   if c.get('staff'):c.set('staff',str(staff_for(int(c.get('staff'))-1,int(m.get('n')))))
   if c.tag==M+'tie':c.set('curvedir','below' if notes[c.get('startid')[1:]]['voice']==1 else 'above')
 return root

def complete(is_keyboard):
 root=root_score()
 if is_keyboard:root=keyboard(root)
 else:
  for st in root.findall('.//m:staffDef',NS):
   v=int(st.get('n'))-1
   ET.SubElement(st,M+'label').text=['Soprano','Alto','Bass'][v];ET.SubElement(st,M+'labelAbbr').text='SAB'[v]
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
   staff=staff_for(v,first['bar'])
   d=ET.SubElement(m,M+'dir',{ID:f'mark-{ann["id"]}-{start}','staff':str(staff if is_keyboard else v+1),'startid':'#'+first['id'],'place':'below' if is_keyboard and (v==1 and staff==1 or v==2 and first['bar'] in LOW_ALTO) else 'above','color':colours[ann['kind']]})
   text=ann['label']+(' >' if ann['start']<(start-1)*4 else '')
   ET.SubElement(d,M+'rend',{'fontfam':'Arial','fontweight':'bold','fontstyle':'normal','fontsize':'small'}).text=text
 assert {n.get(ID) for n in root.findall('.//m:note',NS)}==set(notes)
 assert len(root.findall('.//m:tie',NS))==len(source.findall('.//m:tie',NS))
 tidy_score(root,notes,is_keyboard,R.name)
 if is_keyboard:
  # One fermata per stave at the closing chord.
  for m in root.findall('.//m:measure',NS):
   for f in m.findall(M+'fermata'):
    if f.get(ID)=='fermata-L915F4':m.remove(f)
  # The dialogue crosses: route these soprano ties below the intervening alto.
  for t in root.findall('.//m:tie',NS):
   if t.get('startid') in ['#note-L112F3','#note-L128F3','#note-L813F3','#note-L829F3']:t.set('curvedir','below')
 mode='keyboard' if is_keyboard else 'open'
 (TEMP/f'{mode}.mei').write_text(serial(root))
 tk=verovio.toolkit();tk.setOptions({'inputFrom':'mei','pageWidth':2300 if is_keyboard else 2500,'pageHeight':20000,'scale':40,'adjustPageHeight':True,'header':'none','footer':'none','svgViewBox':True,'breaks':'encoded','xmlIdSeed':848,'mnumInterval':1,'spacingStaff':14 if is_keyboard else 11})
 assert tk.loadData(serial(root));assert tk.getPageCount()==len(ranges),(mode,tk.getPageCount())
 tk.renderToMIDI()
 for nid,e in notes.items():
  actual=tk.getMIDIValuesForElement(nid);assert actual['pitch']==e['pitch'],(mode,nid,actual,e)
  assert abs(actual['time']-e['start']*60000/106)<2,(mode,nid)
 systems=[];rendered=[]
 for page,(a,b) in enumerate(ranges,1):
  svg=tk.renderToSVG(page);rr=ET.fromstring(svg)
  rendered.extend(g.get('id') for g in rr.iter() if g.get('id') in notes)
  systems.append({'start':a,'end':b,'svg':prefix_svg(svg,f'{mode}-{a}-',not is_keyboard)})
 assert len(rendered)==len(set(rendered))==len(notes)
 (TEMP/f'{mode}-systems.json').write_text(json.dumps(systems,ensure_ascii=False,separators=(',',':')))
 if not is_keyboard:(R/'data/annotated-systems.json').write_text(json.dumps(systems,ensure_ascii=False,separators=(',',':')))
 print(mode,len(systems),'systems;',len(notes),'notes and',len(source.findall('.//m:tie',NS)),'ties preserved.',flush=True)

def examples():
 out=[]
 for kind,a,b,voice,start,end in [('subject',1,3,0,1.5,8.5),('cs1',3,5,0,10,16.5),('cs2',5,7,0,17,24.5)]:
  root=tidy_score(root_score(),notes,False,R.name);sd=root.find('.//m:scoreDef',NS);group=sd.find(M+'staffGrp');group.set('symbol','none')
  for st in list(group):
   if st.tag==M+'staffDef':
    if int(st.get('n'))!=voice+1:group.remove(st)
    else:st.set('n','1')
  sec=root.find('.//m:section',NS)
  for m in list(sec):
   if m.tag!=M+'measure' or not a<=int(m.get('n'))<=b:sec.remove(m);continue
   for st in list(m.findall(M+'staff')):
    if int(st.get('n'))!=voice+1:m.remove(st)
    else:st.set('n','1')
   # Cut the last bar after its closing note, preserving its original duration.
   if int(m.get('n'))==b:
    layer=m.find('.//m:layer',NS);last=next(n for n in layer.iter(M+'note') if notes[n.get(ID)]['start']==(b-1)*4)
    for c in list(layer):layer.remove(c)
    layer.append(copy.deepcopy(last));m.set('metcon','false');m.set('right','invis')
   for n in m.findall('.//m:note',NS):n.set('color',colours[kind] if start<=notes[n.get(ID)]['start']<end else '#a2a8b0')
  ids={n.get(ID) for n in root.iter()}
  for m in sec:
   for c in list(m):
    if any(c.get(k,'').startswith('#') and c.get(k)[1:] not in ids for k in ['startid','endid']):m.remove(c)
    elif c.get('staff'):c.set('staff','1')
  tk=verovio.toolkit();tk.setOptions({'inputFrom':'mei','pageWidth':1900,'pageHeight':5000,'scale':40,'adjustPageHeight':True,'header':'none','footer':'none','svgViewBox':True,'breaks':'none','xmlIdSeed':848,'mnumInterval':1})
  assert tk.loadData(serial(root))
  out.append({'id':kind,'start':start,'svg':prefix_svg(tk.renderToSVG(1),'theme-'+kind+'-')})
 (R/'data/thematic-examples.json').write_text(json.dumps(out,ensure_ascii=False,separators=(',',':')))
 print('Three thematic examples.',flush=True)
complete(False);complete(True);examples()
