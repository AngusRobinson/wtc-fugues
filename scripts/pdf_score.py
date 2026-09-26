"""Place tonal-arrival numerals above the engraved beat, using the study's analysis."""
from functools import lru_cache
import hashlib,json,re,statistics,subprocess,xml.etree.ElementTree as ET
from pathlib import Path
from reportlab.lib.colors import HexColor
V='{http://www.w3.org/2000/svg}'


@lru_cache(None)
def material(root):
    result=subprocess.run(['node','--input-type=module','-e',
        "import{pathToFileURL}from'node:url';const m=await import(pathToFileURL(process.argv[1]).href);console.log(JSON.stringify(m.tonalEvents));",
        str(root/'analysis.ts')],capture_output=True,text=True,check=True)
    # Entry-context markers do not claim a harmonic arrival at the onset.
    arrivals=[e for e in json.loads(result.stdout) if e['type'] in ('arrival','cadence','close')]
    notes=json.loads((root/'data/score.json').read_text())['events']
    return arrivals,notes

def arrivals_in(root,system):
    return [e for e in material(root)[0] if system['start']<=e['bar']<=system['end']]

def score_height(root,system,width):
    vb=list(map(float,ET.fromstring(system['svg']).get('viewBox').split()))
    return width*vb[3]/vb[2]

def arrival_positions(root,system):
    events=arrivals_in(root,system)
    if not events:return []
    svg=ET.fromstring(system['svg']);inner=svg.find(V+'svg')
    inner_width=float(inner.get('viewBox').split()[2])
    margin=next(g for g in inner.iter() if g.get('class')=='page-margin')
    dx=float(re.search(r'translate\(([-\d.]+)',margin.get('transform'))[1])
    positions={}
    for group in margin.iter():
        if 'note' not in group.get('class','').split():continue
        head=next((g for g in group if g.get('class')=='notehead'),None)
        if head is None:continue
        use=head.find(V+'use')
        if use is None:continue
        x=float(re.search(r'translate\(([-\d.]+)',use.get('transform'))[1])
        # Prefixes used by the interactive engraving precede the original ID.
        ident=re.search(r'note-L[^ ]+$',group.get('id',''))
        if ident:positions[ident[0]]=(dx+x)/inner_width
    result=[]
    for event in events:
        onsets=[n for n in material(root)[1] if n['bar']==event['bar'] and abs(n['start']-event['q'])<1e-7 and n['id'] in positions]
        assert onsets,(root.name,event['id'],'no engraved note at arrival')
        x=statistics.median(positions[n['id']] for n in onsets)
        assert 0<x<1,(root.name,event['id'],x)
        result.append((event,x))
    return result

def pdf_svg(system):
    """Keep a single system-start bar number; browser numbering is unchanged."""
    root=ET.fromstring(system['svg']);kept=[]
    for parent in root.iter():
        for group in list(parent):
            if 'mNum' not in group.get('class','').split():continue
            if not kept:kept.append(''.join(group.itertext()).strip())
            else:parent.remove(group)
    assert kept==[str(system['start'])],(system['start'],kept)
    ET.register_namespace('',V[1:-1]);ET.register_namespace('xlink','http://www.w3.org/1999/xlink')
    return ET.tostring(root,encoding='unicode')

def pdf_image(system,image):
    """Cache separately so PDF numbering never alters the browser engraving."""
    svg=pdf_svg(system);digest=hashlib.sha256(svg.encode()).hexdigest()
    target=image.with_name(image.stem+'-pdf.png');stamp=target.with_suffix('.sha256')
    if not target.exists() or not stamp.exists() or stamp.read_text()!=digest:
        subprocess.run(['node',str(Path(__file__).with_name('raster_pdf_score.mjs')),str(target)],
                       input=svg,text=True,capture_output=True,check=True)
        stamp.write_text(digest)
    return target

def numeral_baseline(system,width):
    """Use the clear upper row formerly occupied by internal bar numbers."""
    svg=ET.fromstring(system['svg']);inner=svg.find(V+'svg')
    margin=next(g for g in inner.iter() if g.get('class')=='page-margin')
    dy=float(re.search(r'translate\([\-\d.]+[, ]+([\-\d.]+)',margin.get('transform'))[1])
    number=next(g for g in margin.iter() if 'mNum' in g.get('class','').split())
    y=float(number.find(V+'text').get('y'))
    return width*(dy+y)/float(inner.get('viewBox').split()[2])

def draw_score(canvas,root,system,image,left,bottom,width,height):
    positions=arrival_positions(root,system)
    canvas.drawImage(str(pdf_image(system,image)),left,bottom,width=width,height=height)
    if positions:
        canvas.saveState();canvas.setFillColor(HexColor('#35465e'));canvas.setFont('Times-Bold',9)
        baseline=bottom+height-numeral_baseline(system,width)
        end=-1
        for event,x in sorted(positions,key=lambda pair:pair[1]):
            centre=left+x*width;half=canvas.stringWidth(event['roman'],'Times-Bold',9)/2
            assert centre-half>end+3,(root.name,event['id'],'tonal labels overlap')
            canvas.drawCentredString(centre,baseline,event['roman']);end=centre+half
        canvas.restoreState()


def page_number(canvas,width,number):
    """Plain page number, clear of the final-page source credit."""
    canvas.saveState();canvas.setFillColor(HexColor('#657486'));canvas.setFont('Helvetica',8)
    canvas.drawRightString(width-30,12,str(number));canvas.restoreState()
