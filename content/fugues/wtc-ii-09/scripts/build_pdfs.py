"""Build both annotated scores and the public-domain source extracts."""
import json,re,argparse
from pathlib import Path
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from pypdf import PdfReader,PdfWriter,Transformation
p=argparse.ArgumentParser();p.add_argument('--prout',type=Path,required=True);p.add_argument('--tovey',type=Path,required=True);args=p.parse_args()
R=Path(__file__).resolve().parents[1];TEMP=R/'tmp';W,H=A4;left=30;width=W-60
for mode,suffix,description in [('open','annotated','Four staves'),('keyboard','keyboard','Two staves')]:
 systems=json.loads((TEMP/f'{mode}-systems.json').read_text())
 batches=[];batch=[];used=0
 for s in systems:
  dims=re.search(r'viewBox="[\d.]+ [\d.]+ ([\d.]+) ([\d.]+)"',s['svg']);s['height']=width*float(dims[2])/float(dims[1])
  available=H-(115 if not batches else 45)-45
  if batch and used+s['height']+16>available:batches.append(batch);batch=[];used=0
  batch.append(s);used+=s['height']+16
 if batch:batches.append(batch)
 dest=R/f'pdf/bach-e-major-fugue-{suffix}.pdf';c=canvas.Canvas(str(dest),pagesize=A4,pageCompression=1,invariant=1)
 c.setTitle(f'Bach - Fugue in E major, BWV 878 - {description}');c.setAuthor('J. S. Bach; analysis with reference to Keller, Prout and Tovey');c.setCreator('WTC fugue analyses');c.setSubject('Subject, real answer, countersubject, chromatic counterpoints and derived figures.')
 for page,batch in enumerate(batches):
  c.setFillColor(HexColor('#202b39'))
  if page==0:
   c.setFont('Times-Roman',20);c.drawString(left,H-34,'Fugue in E major')
   c.setFont('Helvetica',9);c.drawRightString(W-left,H-33,'J. S. BACH / BWV 878')
   c.setFont('Helvetica',8);c.drawString(left,H-50,'WTC II, no. 9 / Annotated score / '+description+' / 4/2')
   for x,lab,col in [(left,'S subject / A real answer','#244f91'),(left+163,'CS','#a45112'),(left+221,'x','#843d7c'),(left+259,'y','#35735a'),(left+300,'c / i figures','#637878')]:
    c.setFillColor(HexColor(col));c.rect(x,H-67,6,6,fill=1,stroke=0);c.setFont('Helvetica-Bold',8);c.drawString(x+10,H-67,lab)
   c.setFillColor(HexColor('#526174'));c.setFont('Helvetica',7)
   c.drawString(left,H-81,'v ornamented variation; d diminution; * adapted statement / fragment; > continuation; x/y chromatic counterpoints')
   c.drawString(left,H-93,'c countersubject-derived figure; i altered inverted diminution. Voice prefixes: S soprano, A alto, T tenor, B bass.')
   y=H-105
  else:
   c.setFont('Times-Roman',11);c.drawString(left,H-29,'Bach - Fugue in E major, BWV 878')
   c.setFont('Helvetica',8);c.drawRightString(W-left,H-29,f'Bars {batch[0]["start"]}-{batch[-1]["end"]}')
   y=H-43
  gap=min(25,(y-42-sum(s['height'] for s in batch))/max(1,len(batch)-1));assert gap>=8
  for s in batch:
   c.drawImage(str(TEMP/f'{mode}-{s["start"]}.png'),left,y-s['height'],width=width,height=s['height']);y-=s['height']+gap
  assert y+gap>35
  c.setFillColor(HexColor('#657486'));c.setFont('Helvetica',6.7)
  c.drawString(left,23,'Kroll 1866 / Huron-Sapp encoding / Analysis checked against Keller, Prout and Tovey')
  c.drawRightString(W-left,23,f'{page+1} / {len(batches)}');c.showPage()
 c.save();print(dest.name,len(batches),'pages')
extracts=[
 ('prout',args.prout,[67,68,69],"Ebenezer Prout: Analysis of J. S. Bach's Forty-Eight Fugues",'Ed. Louis B. Prout. London: Edwin Ashdown, 1910. Printed pp. 64-66.',"https://waltercosand.com/CosandScores/Composers%20L-P/Composers_P/Prout%2C%20Ebenezer/Prout-Analysis_of_Bach%27s_48_Fugues.pdf"),
 ('tovey',args.tovey,[75,76],"Donald Francis Tovey: The Well-Tempered Clavier, Book II",'Associated Board, 1924. Printed pp. 56-57. Fugue IX commentary.', 'https://s9.imslp.org/files/imglnks/usimg/1/1c/IMSLP911004-PMLP05899-Bach_-_48_Preludes_and_Fugues_%28Tovey%29_-_Book_II.pdf')]
for name,source,indices,title,edition,url in extracts:
 reader=PdfReader(source);writer=PdfWriter()
 for j,i in enumerate(indices):
  original=reader.pages[i]
  if j:writer.add_page(original);continue
  w,h=float(original.mediabox.width),float(original.mediabox.height)
  page=writer.add_blank_page(width=w,height=h+66);page.merge_transformed_page(original,Transformation().translate(0,66))
  stream=BytesIO();c=canvas.Canvas(stream,pagesize=(w,h+66),invariant=1)
  for y,line in zip([47,35,23],[title,edition,'BWV 878. Complete original pages; adjoining commentary is retained.']):
   size=min(8,8*(w-40)/c.stringWidth(line,'Helvetica',8));c.setFont('Helvetica',size);c.drawString(20,y,line)
  c.setFillColor(HexColor('#244f91'));c.setFont('Helvetica',8);c.drawString(20,11,'Full source scan');c.linkURL(url,(20,8,w-20,20),relative=0,thickness=0);c.save();page.merge_page(PdfReader(stream).pages[0],over=False)
 writer.add_metadata({'/Title':f'{name.title()} - Analysis of Bach Fugue in E major, BWV 878','/Author':title.split(':')[0],'/Subject':edition+' Public-domain source extract. '+url})
 dest=R/f'pdf/{name}-bwv878-analysis.pdf';writer.write(dest);print(dest.name,len(indices),'pages')
