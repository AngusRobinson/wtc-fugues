"""Engrave annotated open/keyboard scores and isolated thematic examples."""
import copy,json,re,argparse
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[4]/'scripts'))
from engraving import tidy_score,finish_svg
from verify_render import verify_midi
import xml.etree.ElementTree as ET
import verovio
p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--layout-only',action='store_true');args=p.parse_args();R=args.root
TEMP=R.parents[2]/'tmp'/R.name
TEMP.mkdir(parents=True,exist_ok=True)
M='{http://www.music-encoding.org/ns/mei}';V='{http://www.w3.org/2000/svg}';ID='{http://www.w3.org/XML/1998/namespace}id';NS={'m':M[1:-1]}
ET.register_namespace('',M[1:-1]);ET.register_namespace('xlink','http://www.w3.org/1999/xlink')
source=ET.parse(R/'sources/bwv881-3-voices.mei').getroot()
notes={n['id']:n for n in json.loads((R/'data/score.json').read_text())['events']}
anns=json.loads((R/'data/annotations.json').read_text())['annotations'];members={nid:a for a in anns for nid in a['notes']}
TIE_ROUTES=json.loads((R/'scripts/tie_routes.json').read_text()) if (R/'scripts/tie_routes.json').exists() else {}
colours={'subject':'#244f91','cs1':'#a45112','cs2':'#843d7c','cs3':'#35735a','motif':'#637878'}
ranges=[[0, 4], [5, 10], [11, 16], [17, 22], [23, 28], [29, 34], [35, 40], [41, 46], [47, 52], [53, 58], [59, 64], [65, 70], [71, 76], [77, 82], [83, 85]]
def bar_start(b):return 0 if b==0 else 0.5+(b-1)*2.0
def serial(root):
 ET.register_namespace('',M[1:-1]);return ET.tostring(root,encoding='unicode')
def prefix_svg(svg,prefix,interactive=False):
 ET.register_namespace('',V[1:-1])
 rr=ET.fromstring(finish_svg(svg));old=rr.get('id')
 for parent in rr.iter():
  for child in list(parent):
   if 'mNum' in child.get('class','').split() and ''.join(child.itertext()).strip()=='0':parent.remove(child)
 seen=set()
 for g in rr.iter():
  nid=g.get('id','')
  if nid and nid in seen:
   assert nid not in notes and g.tag in [V+'g',V+'tspan']
   while nid in seen:nid+='-duplicate'
   g.set('id',nid)
  seen.add(nid)
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
 root.find('.//m:measure[@n="0"]',NS).set('metcon','false')
 for h in sd.findall(M+'pgHead'):sd.remove(h)
 for n in root.findall('.//m:note',NS):
  ann=members.get(n.get(ID))
  if ann:n.set('color',colours[ann['kind']])
 return root

def staff_for(v,b):return 2 if v==2 or (v==1 and (50<=b<=54 or 72<=b<=73)) else 1
def keyboard(root):
 sd=root.find('.//m:scoreDef',NS)
 for c in list(sd):sd.remove(c)
 group=ET.SubElement(sd,M+'staffGrp',{'symbol':'brace','bar.thru':'true'})
 for sn,clef,line in [(1,'G','2'),(2,'F','4')]:
  st=ET.SubElement(group,M+'staffDef',{'n':str(sn),'lines':'5'})
  ET.SubElement(st,M+'clef',{'shape':clef,'line':line});ET.SubElement(st,M+'keySig',{'sig': '4f', 'mode': 'minor', 'pname': 'f'});ET.SubElement(st,M+'meterSig',{'count': '2', 'unit': '4'})
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
      for rest in layer.findall('.//m:mRest',NS):
       rest.tag=M+'mSpace';rest.attrib.pop('visible',None)
      if int(m.get('n'))==0:
       for rest in layer.findall('.//m:rest',NS):rest.tag=M+'space'
    staff.append(layer)
   # Recalculate displayed cancellations where voices share a stave.
   state={};bytime={}
   for note in staff.findall('.//m:note',NS):bytime.setdefault(notes[note.get(ID)]['start'],[]).append(note)
   for q,ns in sorted(bytime.items()):
    updates={}
    for note in ns:
     e=notes[note.get(ID)];key=(note.get('pname'),note.get('oct'));acc=note.find(M+'accid');target=acc if acc is not None else note
     alt={'ff':-2,'f':-1,'n':0,'s':1,'ss':2,'x':2}[target.get('accid.ges')];before=state.get(key,{'b': -1, 'e': -1, 'a': -1, 'd': -1}.get(key[0],0))
     if not e['tied'] and before!=alt:target.set('accid',{-2:'ff',-1:'f',0:'n',1:'s',2:'ss'}[alt])
     updates[key]=alt
    state.update(updates)
  for c in list(m):
   if c.tag==M+'staff':continue
   if c.get('staff'):c.set('staff',str(staff_for(int(c.get('staff'))-1,int(m.get('n')))))
   if c.tag==M+'tie':c.set('curvedir','below' if notes[c.get('startid')[1:]]['voice']%2==1 else 'above')
 return root

def complete(is_keyboard):
 root=root_score()
 if is_keyboard:root=keyboard(root)
 else:
  for st in root.findall('.//m:staffDef',NS):
   v=int(st.get('n'))-1
   ET.SubElement(st,M+'label').text=['Soprano', 'Alto', 'Bass'][v];ET.SubElement(st,M+'labelAbbr').text='SAB'[v]
 if not is_keyboard:
  for bar,shape,line in [(51,'F','4'),(55,'G','2'),(72,'F','4'),(74,'G','2')]:
   root.find(f'.//m:measure[@n="{bar}"]/m:staff[@n="2"]/m:layer',NS).insert(0,ET.Element(M+'clef',{'shape':shape,'line':line}))
 for bar,shape,line in [(45,'G','2'),(48,'F','4'),(65,'G','2'),(70,'F','4')]:
  sn=2 if is_keyboard else 3
  root.find(f'.//m:measure[@n="{bar}"]/m:staff[@n="{sn}"]/m:layer',NS).insert(0,ET.Element(M+'clef',{'shape':shape,'line':line}))
 sec=root.find('.//m:section',NS)
 for start,end in ranges:
  m=sec.find(f'm:measure[@n="{start}"]',NS)
  if start>1:sec.insert(list(sec).index(m),ET.Element(M+'pb'))
  for ann in anns:
   ns=[notes[n] for n in ann['notes'] if start<=notes[n]['bar']<=end]
   if not ns:continue
   # A single closing note needs its colour, not another crowded label.
   if ann['start']<bar_start(start) and ann['end']-bar_start(start)<=1:continue
   first=ns[0];v=ann['voice'];m=sec.find(f'm:measure[@n="{first["bar"]}"]',NS)
   staff=staff_for(v,first['bar'])
   d=ET.SubElement(m,M+'dir',{ID:f'mark-{ann["id"]}-{start}','staff':str(staff if is_keyboard else v+1),'startid':'#'+first['id'],'place':'below' if is_keyboard and v==max(w for w in range(3) if staff_for(w,first['bar'])==staff) and sum(staff_for(w,first['bar'])==staff for w in range(3))>1 else 'above','color':colours[ann['kind']]})
   text=ann['label']+(' >' if ann['start']<bar_start(start) else '')
   ET.SubElement(d,M+'rend',{'fontfam':'Arial','fontweight':'bold','fontstyle':'normal','fontsize':'small'}).text=text
 assert {n.get(ID) for n in root.findall('.//m:note',NS)}==set(notes)
 assert len(root.findall('.//m:tie',NS))==len(source.findall('.//m:tie',NS))
 tidy_score(root,notes,is_keyboard,R.name)
 for measure in root.findall('.//m:measure',NS):
  chosen={}
  for f in measure.findall(M+'fermata'):
   target=next((n for n in measure.iter() if n.get(ID)==f.get('startid','')[1:]),None)
   if target is None:continue
   ns=[target] if target.tag==M+'note' else target.findall('.//m:note',NS)
   onset=min(notes[n.get(ID)]['start'] for n in ns);end=max(notes[n.get(ID)]['start']+notes[n.get(ID)]['duration'] for n in ns)
   key=(f.get('staff'),end)
   if key not in chosen or onset>chosen[key][0]:
    if key in chosen:measure.remove(chosen[key][1])
    chosen[key]=(onset,f)
   else:measure.remove(f)
 mode='keyboard' if is_keyboard else 'open'
 (TEMP/f'{mode}.mei').write_text(serial(root))
 tk=verovio.toolkit();tk.setOptions({'inputFrom':'mei','pageWidth':2900 if is_keyboard else 3000,'pageHeight':20000,'scale':40,'adjustPageHeight':True,'header':'none','footer':'none','svgViewBox':True,'breaks':'encoded','xmlIdSeed':881,'mnumInterval':1,'spacingStaff':20 if is_keyboard else 9})
 assert tk.loadData(serial(root));assert tk.getPageCount()==len(ranges),(mode,tk.getPageCount())
 if not args.layout_only:
  verify_midi(tk,list(notes.values()))
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
 for kind,a,b,voice,start,end in [['subject', 0, 4, 0, 0, 6.75], ['motif', 17, 18, 0, 32.5, 36.5]]:
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
   if int(m.get('n'))==b:
    cursor=bar_start(b)
    def cut(parent):
     nonlocal cursor
     for child in list(parent):
      if child.tag in [M+'note',M+'rest',M+'space',M+'mRest']:
       if child.tag==M+'note':event=notes[child.get(ID)];cursor=event['start'];dur=event['duration']
       else:dur=2.0 if child.tag==M+'mRest' else 4/int(child.get('dur','1'))*sum(.5**j for j in range(int(child.get('dots','0'))+1))
       if cursor>=end:parent.remove(child)
       cursor+=dur
      else:cut(child)
    cut(m)
    for parent in list(m.iter()):
     for child in list(parent):
      if child.tag==M+'note' and notes[child.get(ID)]['start']>=end:parent.remove(child)
    for parent in reversed(list(m.iter())):
     for child in list(parent):
      if child.tag==M+'beam':
       ns=child.findall('.//m:note',NS)
       if not ns:parent.remove(child)
       elif len(ns)==1:
        i=list(parent).index(child);parent.remove(child);parent.insert(i,ns[0])
    m.set('metcon','false');m.set('right','invis')
   for n in m.findall('.//m:note',NS):n.set('color',colours[kind] if start<=notes[n.get(ID)]['start']<end else '#a2a8b0')
  ids={n.get(ID) for n in root.iter()}
  for m in sec:
   for c in list(m):
    if any(c.get(k,'').startswith('#') and c.get(k)[1:] not in ids for k in ['startid','endid']):m.remove(c)
    elif c.get('staff'):c.set('staff','1')
  tk=verovio.toolkit();tk.setOptions({'inputFrom':'mei','pageWidth':1900,'pageHeight':5000,'scale':40,'adjustPageHeight':True,'header':'none','footer':'none','svgViewBox':True,'breaks':'none','xmlIdSeed':881,'mnumInterval':1})
  assert tk.loadData(serial(root))
  out.append({'id':kind,'start':start,'svg':prefix_svg(tk.renderToSVG(1),'theme-'+kind+'-')})
 (R/'data/thematic-examples.json').write_text(json.dumps(out,ensure_ascii=False,separators=(',',':')))
 print('Subject and countersubject examples.',flush=True)
complete(False);complete(True);examples()
