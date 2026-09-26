"""Build both annotated scores and the public-domain source extracts."""
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
p=argparse.ArgumentParser();p.add_argument('--prout',type=Path);p.add_argument('--tovey',type=Path);p.add_argument('--scores-only',action='store_true');args=p.parse_args()
if not args.scores_only and (not args.prout or not args.tovey):p.error('--prout and --tovey are required unless --scores-only is used')
R=Path(__file__).resolve().parents[1];TEMP=R.parents[2]/'tmp'/R.name;W,H=A4;left=30;width=W-60
for mode,suffix,description in [('open','annotated','Four staves'),('keyboard','keyboard','Two staves')]:
 systems=json.loads((TEMP/f'{mode}-systems.json').read_text())
 batches=[];batch=[];used=0
 for s in systems:
  s['height']=score_height(R,s,width)
  available=H-(105 if not batches else 28)-42
  if batch and used+s['height']+8>available:batches.append(batch);batch=[];used=0
  batch.append(s);used+=s['height']+8
 if batch:batches.append(batch)
 if mode=='open':batches=[systems[i:i+3] for i in range(0,len(systems),3)]
 dest=R/f'pdf/bach-b-major-fugue-{suffix}.pdf';c=canvas.Canvas(str(dest),pagesize=A4,pageCompression=1,invariant=1)
 c.setTitle(f'Bach - Fugue in B major, BWV 868 - {description}');c.setAuthor('J. S. Bach; analysis with reference to Keller, Prout and Tovey');c.setCreator('WTC fugue analyses');c.setSubject('Tonal answer, inversion, countersubject and episode figures.')
 for page,batch in enumerate(batches):
  c.setFillColor(HexColor('#202b39'))
  if page==0:
   c.setFont('Times-Roman',20);c.drawString(left,H-34,'Fugue in B major')
   c.setFont('Helvetica',9);c.drawRightString(W-left,H-33,'J. S. BACH / BWV 868')
   c.setFont('Helvetica',8);c.drawString(left,H-50,'WTC I, no. 23 / Annotated score / '+description+' / 4/4')
   for x,lab,col in [(left,'S subject / A tonal answer','#244f91'),(left+205,'CS countersubject','#a45112'),(left+345,'Derived figures','#637878')]:
    c.setFillColor(HexColor(col));c.rect(x,H-67,6,6,fill=1,stroke=0);c.setFont('Helvetica-Bold',8);c.drawString(x+10,H-67,lab)
   c.setFillColor(HexColor('#526174'));c.setFont('Helvetica',7)
   c.drawString(left,H-81,'i inversion; * adapted statement; > continuation; c countersubject opening; e episode figure; ei its inversion')
   c.drawString(left,H-93,'Beats are crotchets.')
   y=H-105
  else:
   y=H-28
  gap=min(25,(y-42-sum(s['height'] for s in batch))/max(1,len(batch)-1));assert gap>=8
  for s in batch:
   draw_score(c,R,s,TEMP/f'{mode}-{s["start"]}.png',left,y-s['height'],width,s['height']);y-=s['height']+gap
  assert y+gap>35
  if page==len(batches)-1:
   c.setFillColor(HexColor('#657486'));c.setFont('Helvetica',6.7)
   c.drawString(left,23,'Kroll 1866 / Huron-Sapp encoding / Analysis checked against Keller, Prout and Tovey')
  page_number(c,W,page+1)
  c.showPage()
 c.save();print(dest.name,len(batches),'pages')
if args.scores_only:raise SystemExit(0)
extracts=[
 ('prout',args.prout,[53,54],"Ebenezer Prout: Analysis of J. S. Bach's Forty-Eight Fugues",'Ed. Louis B. Prout. London: Edwin Ashdown, 1910. Printed pp. 50-51.',"https://waltercosand.com/CosandScores/Composers%20L-P/Composers_P/Prout%2C%20Ebenezer/Prout-Analysis_of_Bach%27s_48_Fugues.pdf"),
 ('tovey',args.tovey,[170],"Donald Francis Tovey: The Well-Tempered Clavier, Book I",'Associated Board, 1924. Printed p. 151. Fugue XXIII commentary.', 'https://s9.imslp.org/files/imglnks/usimg/4/4f/IMSLP911003-PMLP05948-Bach_-_48_Preludes_and_Fugues_%28Tovey%29_-_Book_I.pdf')]
for name,source,indices,title,edition,url in extracts:
 reader=PdfReader(source);writer=PdfWriter()
 for j,i in enumerate(indices):
  original=reader.pages[i]
  if j:writer.add_page(original);continue
  w,h=float(original.mediabox.width),float(original.mediabox.height)
  page=writer.add_blank_page(width=w,height=h+66);page.merge_transformed_page(original,Transformation().translate(0,66))
  stream=BytesIO();c=canvas.Canvas(stream,pagesize=(w,h+66),invariant=1)
  for y,line in zip([47,35,23],[title,edition,'BWV 868. Complete original pages; adjoining commentary is retained.']):
   size=min(8,8*(w-40)/c.stringWidth(line,'Helvetica',8));c.setFont('Helvetica',size);c.drawString(20,y,line)
  c.setFillColor(HexColor('#244f91'));c.setFont('Helvetica',8);c.drawString(20,11,'Full source scan');c.linkURL(url,(20,8,w-20,20),relative=0,thickness=0);c.save();page.merge_page(PdfReader(stream).pages[0],over=False)
 writer.add_metadata({'/Title':f'{name.title()} - Analysis of Bach Fugue in B major, BWV 868','/Author':title.split(':')[0],'/Subject':edition+' Public-domain source extract. '+url})
 dest=R/f'pdf/{name}-bwv868-analysis.pdf';writer.write(dest);print(dest.name,len(indices),'pages')
