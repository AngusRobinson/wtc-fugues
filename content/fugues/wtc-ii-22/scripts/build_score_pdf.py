"""A score-only PDF using the browser's annotated engraving."""
import json,re
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[4]/'scripts'))
from pdf_score import score_height,draw_score,page_number
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from pypdf import PdfReader
R=Path(__file__).resolve().parents[1]
TEMP=R.parents[2]/'tmp'/R.name
systems=json.loads((R/'data/annotated-systems.json').read_text())
output=R/'pdf/bach-bflat-minor-fugue-annotated.pdf'
output.parent.mkdir(parents=True,exist_ok=True)
c=canvas.Canvas(str(output),pagesize=A4,pageCompression=1)
c.setTitle('J. S. Bach - Fugue in B-flat minor, BWV 891 - Annotated score')
c.setAuthor('J. S. Bach; analytical annotations after Hermann Keller')
c.setSubject('WTC II, No. 22. Subject, countersubjects and selected recurring cells.')
W,H=A4;left=32;width=W-64
colours={'S / Si':'#244f91','CS1 / CS1i':'#a45112','CS2':'#843d7c','Cells':'#637878'}
groups=[4,4,4,4,3,3,3]
assert sum(groups)==len(systems)
page_manifest=[];i=0
for p,count in enumerate(groups,1):
 batch=systems[i:i+count];i+=count
 c.setFillColor(HexColor('#202b39'))
 if p==1:
  c.setFont('Times-Roman',20);c.drawString(left,H-35,'Fugue in B-flat minor')
  c.setFont('Helvetica',9);c.drawRightString(W-left,H-34,'J. S. BACH  /  WTC II, 22  /  BWV 891')
  x=left
  for label,colour in colours.items():
   c.setFillColor(HexColor(colour));c.rect(x,H-54,6,6,fill=1,stroke=0)
   c.setFont('Helvetica-Bold',8);c.drawString(x+10,H-54,label);x+=102
  c.setFillColor(HexColor('#526174'));c.setFont('Helvetica',7.3)
  c.drawString(left,H-69,'i inversion   * variant / fragment   > continued from previous system')
  c.drawString(left,H-81,'s subject tail   c1 chromatic cell   c2 detached-crotchet cell   t1 CS1 tail')
  y=H-94
 else:
  y=H-28
 heights=[score_height(R,s,width) for s in batch]
 gap=12 if p==1 else (23 if count==4 else 47)
 assert y-sum(heights)-gap*(count-1)>40,(p,y,heights)
 placements=[]
 for s,h in zip(batch,heights):
  draw_score(c,R,s,TEMP/f'pdfs/system-{s["start"]}.png',left,y-h,width,h)
  placements.append({'bars':[s['start'],s['end']],'top':round(y,2),'bottom':round(y-h,2)})
  y-=h+gap
 if p==len(groups):
  c.setFillColor(HexColor('#657486'));c.setFont('Helvetica',6.6)
  c.drawString(left,23,'Kroll 1866 / Huron-Sapp encoding / Analytical labels after Keller')
 page_number(c,W,p)
 c.showPage();page_manifest.append({'page':p,'systems':placements})
c.save()
pdf=PdfReader(output)
assert len(pdf.pages)==len(groups)
(TEMP/'pdfs/layout.json').write_text(json.dumps(page_manifest,indent=2))
print(f'Created {output} ({len(pdf.pages)} pages, {output.stat().st_size:,} bytes)')
