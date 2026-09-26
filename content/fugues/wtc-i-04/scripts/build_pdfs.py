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
R=Path(__file__).resolve().parents[1];TEMP=(R.parents[2]/'tmp'/R.name) if R.parent.name=='fugues' else R/'tmp';W,H=A4;left=30;width=W-60
for mode,suffix,description in [('open','annotated','Five staves'),('keyboard','keyboard','Two staves')]:
 systems=json.loads((TEMP/f'{mode}-systems.json').read_text())
 batches=[];batch=[];used=0
 for s in systems:
  s['height']=score_height(R,s,width)
  available=H-(105 if not batches else 28)-42
  if batch and used+s['height']+8>available:batches.append(batch);batch=[];used=0
  batch.append(s);used+=s['height']+8
 if batch:batches.append(batch)
 # Keep the final stretto and coda together; avoid a sparsely filled last page.
 # Balance the final two pages without exceeding their height budgets.
 if len(batches)>1:
  while len(batches[-2])>len(batches[-1])+1:
   candidate=batches[-2][-1]
   if sum(s['height']+16 for s in [candidate]+batches[-1])>H-90:break
   batches[-1].insert(0,batches[-2].pop())
 # Six systems fit comfortably once the inter-system gap is allowed below 8pt.
 # Keep the existing engraving size, opening title and final-page credit.
 if mode=='keyboard':
  assert len(systems)==23
  batches=[systems[:5],systems[5:11],systems[11:17],systems[17:]]
 dest=R/f'pdf/bach-c-sharp-minor-fugue-{suffix}.pdf';c=canvas.Canvas(str(dest),pagesize=A4,pageCompression=1,invariant=1)
 c.setTitle(f'Bach - Fugue in C sharp minor, BWV 849 - {description}');c.setAuthor('J. S. Bach; analysis with reference to Keller, Prout and Tovey');c.setCreator('WTC fugue analyses');c.setSubject('Three subjects, triple counterpoint and combined stretti.')
 for page,batch in enumerate(batches):
  c.setFillColor(HexColor('#202b39'))
  if page==0:
   c.setFont('Times-Roman',20);c.drawString(left,H-34,'Fugue in C sharp minor')
   c.setFont('Helvetica',9);c.drawRightString(W-left,H-33,'J. S. BACH / BWV 849')
   c.setFont('Helvetica',8);c.drawString(left,H-50,'WTC I, no. 4 / Annotated score / '+description+' / 2/2')
   for x,lab,col in [(left,'S1 / A1 first subject / answer','#244f91'),(left+190,'S2 second subject','#a45112'),(left+330,'S3 third subject','#7d3b7b')]:
    c.setFillColor(HexColor(col));c.rect(x,H-67,6,6,fill=1,stroke=0);c.setFont('Helvetica-Bold',8);c.drawString(x+10,H-67,lab)
   c.setFillColor(HexColor('#526174'));c.setFont('Helvetica',7)
   c.drawString(left,H-81,'i inversion; * adapted / incomplete; > continuation; d stepwise crotchet figure (grey); /2 diminution')
   c.drawString(left,H-93,'The first answer is real.')
   y=H-105
  else:
   y=H-28
  gap=min(25,(y-42-sum(s['height'] for s in batch))/max(1,len(batch)-1));assert gap>=(5 if mode=='keyboard' else 8)
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
 ('prout',args.prout,[22,23,24,25],"Ebenezer Prout: Analysis of J. S. Bach's Forty-Eight Fugues",'Ed. Louis B. Prout. London: Edwin Ashdown, 1910. Printed pp. 19-22.',"https://waltercosand.com/CosandScores/Composers%20L-P/Composers_P/Prout%2C%20Ebenezer/Prout-Analysis_of_Bach%27s_48_Fugues.pdf"),
 ('tovey',args.tovey,[41,42],"Donald Francis Tovey: The Well-Tempered Clavier, Book I",'Associated Board, 1924. Printed pp. 22-23. Fugue IV commentary.', 'https://s9.imslp.org/files/imglnks/usimg/4/4f/IMSLP911003-PMLP05948-Bach_-_48_Preludes_and_Fugues_%28Tovey%29_-_Book_I.pdf')]
for name,source,indices,title,edition,url in extracts:
 reader=PdfReader(source);writer=PdfWriter()
 for j,i in enumerate(indices):
  original=reader.pages[i]
  if j:writer.add_page(original);continue
  w,h=float(original.mediabox.width),float(original.mediabox.height)
  page=writer.add_blank_page(width=w,height=h+66);page.merge_transformed_page(original,Transformation().translate(0,66))
  stream=BytesIO();c=canvas.Canvas(stream,pagesize=(w,h+66),invariant=1)
  for y,line in zip([47,35,23],[title,edition,'BWV 849. Complete original pages; adjoining commentary is retained.']):
   size=min(8,8*(w-40)/c.stringWidth(line,'Helvetica',8));c.setFont('Helvetica',size);c.drawString(20,y,line)
  c.setFillColor(HexColor('#244f91'));c.setFont('Helvetica',8);c.drawString(20,11,'Full source scan');c.linkURL(url,(20,8,w-20,20),relative=0,thickness=0);c.save();page.merge_page(PdfReader(stream).pages[0],over=False)
 writer.add_metadata({'/Title':f'{name.title()} - Analysis of Bach Fugue in C sharp minor, BWV 849','/Author':title.split(':')[0],'/Subject':edition+' Public-domain source extract. '+url})
 dest=R/f'pdf/{name}-bwv849-analysis.pdf';writer.write(dest);print(dest.name,len(indices),'pages')
