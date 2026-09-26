"""Isolated thematic examples; original pitches, rhythms, rests and internal ties."""
import ast,copy,json,re
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[4]/'scripts'))
from engraving import tidy_score,finish_svg
import xml.etree.ElementTree as ET
import verovio
R=Path(__file__).resolve().parents[1]
NS={'m':'http://www.music-encoding.org/ns/mei','s':'http://www.w3.org/2000/svg'}
M='{http://www.music-encoding.org/ns/mei}';V='{http://www.w3.org/2000/svg}';XMLID='{http://www.w3.org/XML/1998/namespace}id'
ET.register_namespace('','http://www.w3.org/2000/svg');ET.register_namespace('xlink','http://www.w3.org/1999/xlink')
source=ET.parse(R/'sources/bwv891-four-voices.mei').getroot();scoredef=source.find('.//m:scoreDef',NS);allmeasures=source.findall('.//m:measure',NS)
tree=ast.parse((R/'scripts/prepare_score.py').read_text())
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='slice_mei'],type_ignores=[]),'slice','exec'))
score=json.loads((R/'data/score.json').read_text());notes={n['id']:n for n in score['events']}
examples=[]
for name,a,b,voice,start,end,colour,cells in [
 ('subject',1,5,1,0,25,'#244f91',[(21,'s')]),
 ('cs1',5,9,1,25,49,'#a45112',[(25,'c1'),(43,'t1')]),
 ('cs2',11,15,0,61,85,'#843d7c',[(72,'c2')])]:
 root=ET.fromstring(slice_mei(a,b,voice))
 last=root.find('.//m:measure[@n="'+str(b)+'"]',NS);layer=last.find('.//m:layer',NS)
 closing=next(n for n in layer.iter(M+'note') if notes[n.get(XMLID)]['start']==end-1)
 for child in list(layer):layer.remove(child)
 layer.append(copy.deepcopy(closing));last.set('metcon','false');last.set('right','invis')
 ids={n.get(XMLID) for n in root.iter()}
 for m in root.findall('.//m:measure',NS):
  for child in list(m):
   if any(child.get(k,'').startswith('#') and child.get(k)[1:] not in ids for k in ['startid','endid']):m.remove(child)
 for n in root.findall('.//m:note',NS):
  d=notes[n.get(XMLID)];n.set('color',colour if start<=d['start']<end else '#a2a8b0')
 for q,label in cells:
  n=next(n for n in notes.values() if n['voice']==voice and n['start']==q)
  m=root.find('.//m:measure[@n="'+str(n['bar'])+'"]',NS)
  d=ET.SubElement(m,M+'dir',{'staff':'1','startid':'#'+n['id'],'place':'above','color':colour})
  ET.SubElement(d,M+'rend',{'fontfam':'Arial','fontweight':'bold','fontstyle':'normal','fontsize':'small'}).text=label
 tk=verovio.toolkit();tk.setOptions({'inputFrom':'mei','pageWidth':2500,'pageHeight':5000,'scale':40,'adjustPageHeight':True,'header':'none','footer':'none','svgViewBox':True,'breaks':'none','xmlIdSeed':892,'mnumInterval':1,'spacingStaff':5})
 assert tk.loadData(ET.tostring(root,encoding='unicode').replace('ns0:','').replace('xmlns:ns0=','xmlns='))
 svg=ET.fromstring(finish_svg(tk.renderToSVG(1)));prefix='theme-'+name+'-';old=svg.get('id')
 for el in svg.iter():
  if el.tag==V+'style' and el.text:el.text=el.text.replace('#'+old,'#'+prefix+old)
  if el.get('id'):el.set('id',prefix+el.get('id'))
  for attr in ['href','{http://www.w3.org/1999/xlink}href']:
   if el.get(attr,'').startswith('#'):el.set(attr,'#'+prefix+el.get(attr)[1:])
 examples.append({'id':name,'start':start,'end':end,'voice':voice,'svg':re.sub(r'>\s+<','><',ET.tostring(svg,encoding='unicode'))})
 print(name,flush=True)
(R/'data/thematic-examples.json').write_text(json.dumps(examples,ensure_ascii=False,separators=(',',':')))
