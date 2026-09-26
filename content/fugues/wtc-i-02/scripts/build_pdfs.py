"""Create compact annotated scores and a credited public-domain Prout extract."""
import json,re,argparse
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[4]/'scripts'))
from pdf_score import score_height,draw_score,page_number
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from pypdf import PdfReader,PdfWriter,Transformation
p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--prout',type=Path);p.add_argument('--scores-only',action='store_true');args=p.parse_args();R=args.root
if not args.scores_only and not args.prout:p.error('--prout is required unless --scores-only is used')
TEMP=R.parents[2]/'tmp'/R.name if R.name=='wtc-i-02' else R/'tmp'
(R/'pdf').mkdir(exist_ok=True)
for mode,suffix,description in [('open','annotated','Annotated open score / Three staves'),('keyboard','keyboard','Annotated keyboard score / Two staves')]:
 systems=json.loads((TEMP/f'{mode}-systems.json').read_text());dest=R/f'pdf/bach-c-minor-fugue-{suffix}.pdf'
 c=canvas.Canvas(str(dest),pagesize=A4,pageCompression=1,invariant=1);W,H=A4;left=30;width=W-60
 c.setTitle(f'Bach - Fugue in C minor, BWV 847 - {description}');c.setAuthor('J. S. Bach; analysis with reference to Keller and Prout');c.setCreator('WTC fugue analyses');c.setSubject('Subject, two countersubjects, scale links and recurring thematic cells.')
 for page in range(2):
  batch=systems[page*4:page*4+4];c.setFillColor(HexColor('#202b39'))
  if page==0:
   c.setFont('Times-Roman',20);c.drawString(left,H-34,'Fugue in C minor')
   c.setFont('Helvetica',9);c.drawRightString(W-left,H-33,'J. S. BACH / BWV 847')
   c.setFont('Helvetica',8);c.drawString(left,H-50,'WTC I, no. 2 / '+description)
   for x,lab,col in [(left,'S subject / A answer','#244f91'),(left+153,'CS1','#a45112'),(left+222,'CS2','#843d7c'),(left+294,'h / d / q cells','#637878')]:
    c.setFillColor(HexColor(col));c.rect(x,H-67,6,6,fill=1,stroke=0);c.setFont('Helvetica-Bold',8);c.drawString(x+10,H-67,lab)
   c.setFillColor(HexColor('#526174'));c.setFont('Helvetica',7)
   c.drawString(left,H-81,'* variant / fragment; > continuation; h subject head; d scale figure; q quaver counterpoint; arrow = ascending form')
   c.drawString(left,H-93,'Counterpoint boundaries follow Keller.')
   y=H-102
  else:
   y=H-28
  heights=[score_height(R,s,width) for s in batch]
  gap=min(26,(y-44-sum(heights))/3);assert gap>=8,(mode,page,gap,heights)
  for s,h in zip(batch,heights):
   draw_score(c,R,s,TEMP/f'{mode}-{s["start"]}.png',left,y-h,width,h);y-=h+gap
  if page==1:
   c.setFillColor(HexColor('#657486'));c.setFont('Helvetica',6.7)
   c.drawString(left,23,'Kroll 1866 / Huron-Sapp encoding / Analytical edition after Keller, checked against Prout')
  page_number(c,W,page+1)
  c.showPage()
 c.save();assert len(PdfReader(dest).pages)==2;print(dest.name,': 2 pages')
# Prout's complete analysis spans printed pp. 14-16, scan pp. 18-20.
if args.scores_only:raise SystemExit(0)
reader=PdfReader(args.prout);writer=PdfWriter();url='https://waltercosand.com/CosandScores/Composers%20L-P/Composers_P/Prout%2C%20Ebenezer/Prout-Analysis_of_Bach%27s_48_Fugues.pdf'
for j,i in enumerate([17,18,19]):
 original=reader.pages[i]
 if j:writer.add_page(original);continue
 w,h=float(original.mediabox.width),float(original.mediabox.height)
 page=writer.add_blank_page(width=w,height=h+68);page.merge_transformed_page(original,Transformation().translate(0,68))
 stream=BytesIO();c=canvas.Canvas(stream,pagesize=(w,h+68),invariant=1)
 lines=["Ebenezer Prout: Analysis of J. S. Bach's Forty-Eight Fugues",'Ed. Louis B. Prout. London: Edwin Ashdown, 1910. Printed pp. 14-16.','Fugue 2, BWV 847. Original pages; the beginning of Fugue 3 is retained.']
 for y,line in zip([47,35,23],lines):
  size=min(8,8*(w-40)/c.stringWidth(line,'Helvetica',8));c.setFont('Helvetica',size);c.drawString(20,y,line)
 c.setFillColor(HexColor('#244f91'));c.setFont('Helvetica',8);c.drawString(20,11,'Full scan: Walter Cosand Library');c.linkURL(url,(20,8,w-20,20),relative=0,thickness=0);c.save()
 page.merge_page(PdfReader(stream).pages[0],over=False)
writer.add_metadata({'/Title':"Prout - Analysis of Bach's Fugue in C minor, BWV 847",'/Author':'Ebenezer Prout; edited by Louis B. Prout','/Subject':'1910 edition, pp. 14-16. Public-domain source extract. '+url})
writer.write(R/'pdf/prout-bwv847-analysis.pdf');print('prout-bwv847-analysis.pdf: 3 pages')
