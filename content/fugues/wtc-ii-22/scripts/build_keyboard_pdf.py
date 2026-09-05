"""Create the annotated keyboard score from the two-staff engraving."""
import json, re
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
TEMP=ROOT.parents[2]/'tmp'/ROOT.name
IMAGES=TEMP/'pdfs/keyboard'
systems=json.loads((IMAGES/'systems.json').read_text())
assert len(systems)==25
output=ROOT/'pdf/bach-bflat-minor-fugue-keyboard.pdf'
c=canvas.Canvas(str(output),pagesize=A4,pageCompression=1,invariant=1)
c.setTitle('Bach - Fugue in B-flat minor, BWV 891 - Annotated keyboard score')
c.setAuthor('J. S. Bach; analytical annotations after Hermann Keller')
c.setCreator('BWV 891 analytical edition')
c.setSubject('Two staves; four independent voices; subject, countersubjects and recurring cells.')
W,H=A4
left=32
width=W-64
manifest=[]
for index in range(5):
    batch=systems[index*5:index*5+5]
    c.setFillColor(HexColor('#202b39'))
    if index==0:
        c.setFont('Times-Roman',20)
        c.drawString(left,H-35,'Fugue in B-flat minor')
        c.setFont('Helvetica',9)
        c.drawRightString(W-left,H-34,'J. S. BACH / BWV 891')
        c.setFont('Helvetica',8)
        c.drawString(left,H-51,'WTC II, no. 22 / Annotated keyboard score')
        for x,label,colour in [(left,'S / Si','#244f91'),(left+110,'CS1 / CS1i','#a45112'),
                                (left+230,'CS2','#843d7c'),(left+330,'Cells','#637878')]:
            c.setFillColor(HexColor(colour))
            c.rect(x,H-68,6,6,stroke=0,fill=1)
            c.setFont('Helvetica-Bold',8)
            c.drawString(x+10,H-68,label)
        c.setFillColor(HexColor('#526174'))
        c.setFont('Helvetica',7.3)
        c.drawString(left,H-82,'Voice prefixes S, A, T, B / i inversion / * variant or fragment / > continuation')
        c.drawString(left,H-94,'s subject tail / c1 chromatic cell / c2 detached-crotchet cell / t1 CS1 tail')
        y=H-105
    else:
        c.setFont('Times-Roman',11)
        c.drawString(left,H-29,'Bach - Fugue in B-flat minor, BWV 891')
        c.setFont('Helvetica',8)
        c.drawRightString(W-left,H-29,f'Bars {batch[0]["start"]}-{batch[-1]["end"]}')
        c.setStrokeColor(HexColor('#dce2e8'))
        c.setLineWidth(.4)
        c.line(left,H-38,W-left,H-38)
        y=H-47
    heights=[]
    for system in batch:
        vb=list(map(float,re.search(r'viewBox="([^"]+)"',system['svg']).group(1).split()))
        heights.append(width*vb[3]/vb[2])
    gap=min(24,(y-45-sum(heights))/4)
    assert gap>=8,(index,gap)
    placements=[]
    for system,height in zip(batch,heights):
        c.drawImage(str(IMAGES/f'system-{system["start"]}.png'),left,y-height,width=width,height=height)
        placements.append({'bars':[system['start'],system['end']],'top':y,'bottom':y-height})
        y-=height+gap
    c.setFillColor(HexColor('#657486'))
    c.setFont('Helvetica',6.6)
    c.drawString(left,23,'Kroll 1866 / Huron-Sapp encoding / Analytical labels after Keller')
    c.drawRightString(W-left,23,f'{index+1} / 5')
    c.showPage()
    manifest.append(placements)
c.save()
assert len(PdfReader(output).pages)==5
(IMAGES/'layout.json').write_text(json.dumps(manifest,indent=2))
print(f'Created five-page keyboard score ({output.stat().st_size:,} bytes).')
