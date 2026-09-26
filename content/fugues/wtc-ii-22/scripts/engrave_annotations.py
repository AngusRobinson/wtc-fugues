"""Engrave the complete score with shared analytical labels and colours."""
import copy,json,re
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[4]/'scripts'))
from engraving import tidy_score,finish_svg
import xml.etree.ElementTree as ET
import verovio
ROOT=Path(__file__).resolve().parents[1]
NS={'s':'http://www.w3.org/2000/svg','m':'http://www.music-encoding.org/ns/mei'}
M='{http://www.music-encoding.org/ns/mei}';V='{http://www.w3.org/2000/svg}';XMLID='{http://www.w3.org/XML/1998/namespace}id'
ET.register_namespace('','http://www.w3.org/2000/svg');ET.register_namespace('xlink','http://www.w3.org/1999/xlink')
data=json.loads((ROOT/'data/score.json').read_text())
anns=json.loads((ROOT/'data/annotations.json').read_text())['annotations']
notes={n['id']:n for n in data['events']}
members={nid:a for a in anns for nid in a['notes']}
colours={'subject':'#244f91','cs1':'#a45112','cs2':'#843d7c','motif':'#637878'}
mtree=ET.fromstring((ROOT/'sources/bwv891-four-voices.mei').read_text())
ranges=[(a,101 if a==97 else a+3) for a in range(1,98,4)]
def annotated_mei():
 root=copy.deepcopy(mtree)
 sd=root.find('.//m:scoreDef',NS)
 for head in list(sd.findall(M+'pgHead')):sd.remove(head)
 for st in sd.findall('.//m:staffDef',NS):
  label=ET.SubElement(st,M+'label');label.text=['Soprano','Alto','Tenor','Bass'][int(st.get('n'))-1]
  abbr=ET.SubElement(st,M+'labelAbbr');abbr.text=['S','A','T','B'][int(st.get('n'))-1]
 for n in root.findall('.//m:note',NS):
  ann=members.get(n.get(XMLID))
  if ann:n.set('color',colours[ann['kind']])
 section=root.find('.//m:section',NS)
 for a,b in ranges:
  if a>1:
   measure=section.find('./m:measure[@n="'+str(a)+'"]',NS)
   section.insert(list(section).index(measure),ET.Element(M+'pb'))
  for ann in anns:
   en=[notes[nid] for nid in ann['notes'] if a<=notes[nid]['bar']<=b]
   if not en:continue
   first=en[0];bar=first['bar']
   measure=root.find('.//m:measure[@n="'+str(bar)+'"]',NS)
   label=ann['label']+(' >' if ann['start']<(a-1)*6 else '')
   d=ET.SubElement(measure,M+'dir',{XMLID:'mark-'+ann['id']+'-'+str(a),'staff':str(ann['voice']+1),'startid':'#'+first['id'],'place':'above','color':colours[ann['kind']]})
   rend=ET.SubElement(d,M+'rend',{'fontfam':'Arial','fontweight':'bold','fontstyle':'normal','fontsize':'small'})
   rend.text=label
 tidy_score(root,notes,False,ROOT.name)
 return ET.tostring(root,encoding='unicode').replace('ns0:','').replace('xmlns:ns0=','xmlns=')
def decorate(svg,a):
 rr=ET.fromstring(finish_svg(svg));prefix='sys'+str(a)+'-';oldroot=rr.get('id')
 for g in rr.iter():
  id=g.get('id','')
  if id in notes:
   n=notes[id];g.set('data-note-id',id);g.set('data-time',str(n['start']));g.set('data-voice',str(n['voice']))
   ann=members.get(id)
   if ann:
    g.set('class',g.get('class','')+' material material-'+ann['kind'])
    g.set('data-kind',ann['kind']);g.set('data-annotation-id',ann['id'])
    g.set('color',colours[ann['kind']]);g.set('fill',colours[ann['kind']]);g.set('stroke',colours[ann['kind']])
   else:
    g.set('color','#222b36');g.set('fill','#222b36');g.set('stroke','#222b36')
  if id.startswith('mark-'):
   ann=next(x for x in anns if id=='mark-'+x['id']+'-'+str(a))
   g.set('class',g.get('class','')+' annotation-label material-'+ann['kind']);g.set('data-kind',ann['kind']);g.set('data-annotation-id',ann['id'])
 for g in rr.iter():
  if g.tag==V+'style' and g.text:g.text=g.text.replace('#'+oldroot,'#'+prefix+oldroot)
  if g.get('id'):g.set('id',prefix+g.get('id'))
  for attr in ['href','{http://www.w3.org/1999/xlink}href']:
   h=g.get(attr)
   if h and h.startswith('#'):g.set(attr,'#'+prefix+h[1:])
 return re.sub(r'>\s+<','><',ET.tostring(rr,encoding='unicode'))
systems=[]
tk=verovio.toolkit()
tk.setOptions({'inputFrom':'mei','pageWidth':2600,'pageHeight':20000,'scale':40,'adjustPageHeight':True,'header':'none','footer':'none','svgViewBox':True,'breaks':'encoded','xmlIdSeed':891,'mnumInterval':1,'spacingStaff':11})
assert tk.loadData(annotated_mei())
assert tk.getPageCount()==len(ranges),(tk.getPageCount(),len(ranges))
for page,(a,b) in enumerate(ranges,1):
 svg=decorate(tk.renderToSVG(page),a)
 systems.append({'start':a,'end':b,'svg':svg})
 print('Annotated bars',a,'-',b,flush=True)
(ROOT/'data/annotated-systems.json').write_text(json.dumps(systems,ensure_ascii=False,separators=(',',':')))
print('Finished',len(systems),'systems.',flush=True)
