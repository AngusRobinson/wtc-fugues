"""Refresh isolated excerpts and add the visible inversion notation key."""
import ast,json,re,copy
from pathlib import Path
import xml.etree.ElementTree as ET
import verovio
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'data/score.json';data=json.loads(p.read_text())
NS={'s':'http://www.w3.org/2000/svg','m':'http://www.music-encoding.org/ns/mei'}
M='{http://www.music-encoding.org/ns/mei}';XMLID='{http://www.w3.org/XML/1998/namespace}id'
ET.register_namespace('','http://www.w3.org/2000/svg');ET.register_namespace('xlink','http://www.w3.org/1999/xlink')
mtree=ET.fromstring((ROOT/'sources/bwv891-four-voices.mei').read_text())
scoredef=mtree.find('.//m:scoreDef',NS);allmeasures=mtree.findall('.//m:measure',NS)
opts={'pageWidth':2600,'pageHeight':20000,'scale':40,'adjustPageHeight':True,'header':'none','footer':'none','svgViewBox':True,'xmlIdSeed':891,'mnumInterval':1,'spacingStaff':7}
notes={e['id']:e for e in data['events']}
membership={nid:(e['id'],e['inverted']) for e in data['entries'] for nid in e['notes']}
tree=ast.parse((ROOT/'scripts/prepare_score.py').read_text())
functions=[n for n in tree.body if isinstance(n,ast.FunctionDef)]
exec(compile(ast.Module(body=functions,type_ignores=[]),'score-functions','exec'))
examples=[]
for name,a,b,voice in [('subject',1,5,1),('inversion',42,46,2),('counterpoint',5,9,1)]:
    svg=engrave(a,b,voice);rr=ET.fromstring(svg)
    for style in rr.findall('.//s:style',NS):
        style.text=style.text.replace('#'+rr.get('id'),'#'+name+'-'+rr.get('id'))
    for el in rr.iter():
        if el.get('id'): el.set('id',name+'-'+el.get('id'))
        for attr in ['href','{http://www.w3.org/1999/xlink}href']:
            val=el.get(attr)
            if val and val.startswith('#'):el.set(attr,'#'+name+'-'+val[1:])
    examples.append(dict(name=name,start=a,end=b,svg=ET.tostring(rr,encoding='unicode')))
    print('Repaired example:',name,flush=True)
data['examples']=examples
for e in data['entries']: e['altered']=e['bar']==96
for item in data['windows']+data['examples']:
    rr=ET.fromstring(item['svg'])
    for el in list(rr.iter()):
        if 'inverse' not in el.get('class','').split(): continue
        if el.find('.//s:line[@class="inverse-mark"]',NS) is not None:continue
        use=el.find('./s:g[@class="notehead"]/s:use',NS)
        if use is None:continue
        m=re.search(r'translate\(([-\d.]+),\s*([-\d.]+)\)',use.get('transform',''))
        if not m:continue
        x,y=map(float,m.groups())
        ET.SubElement(el,'{http://www.w3.org/2000/svg}line',{'class':'inverse-mark','x1':str(x-10),'x2':str(x+225),'y1':str(y+160),'y2':str(y+160),'stroke-width':'22','stroke':'currentColor'})
    item['svg']=re.sub(r'>\s+<','><',ET.tostring(rr,encoding='unicode'))
p.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')))
print('Added inversion underlines and refreshed excerpts.',flush=True)
