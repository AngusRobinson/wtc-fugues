"""Build the two annotated scores and credited public-domain source extracts."""
import argparse,json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[4]/'scripts'))
from pdf_score import score_height,draw_score,page_number
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from io import BytesIO
from pypdf import PdfReader,PdfWriter,Transformation
p=argparse.ArgumentParser();p.add_argument('--scores-only',action='store_true');p.add_argument('--prout',type=Path);p.add_argument('--tovey',type=Path);args=p.parse_args()
if not args.scores_only and (not args.prout or not args.tovey):p.error('--prout and --tovey are required unless --scores-only is used')
R=Path(__file__).resolve().parents[1];cfg=json.loads(Path(__file__).with_name('pdf_config.json').read_text());TEMP=R.parents[2]/'tmp'/R.name
W,H=A4;left=30;width=W-60
for mode,suffix in [('open','annotated'),('keyboard','keyboard')]:
 systems=json.loads((TEMP/f'{mode}-systems.json').read_text());heights=[score_height(R,s,width) for s in systems]
 batches=[];batch=[];used=0
 for s,h in zip(systems,heights):
  available=H-(100 if not batches else 28)-42
  if batch and used+h+9>available:batches.append(batch);batch=[];used=0
  batch.append((s,h));used+=h+9
 if batch:batches.append(batch)
 # Avoid leaving a single system on a final page where a balanced division fits.
 if len(batches)>1:
  while len(batches[-2])>len(batches[-1])+1 and sum(h+15 for _,h in [batches[-2][-1]]+batches[-1])<H-75:
   batches[-1].insert(0,batches[-2].pop())
 dest=R/f'pdf/bach-{cfg["slug"]}-fugue-{suffix}.pdf';c=canvas.Canvas(str(dest),pagesize=A4,pageCompression=1,invariant=1)
 description='Two staves' if mode=='keyboard' else {3:'Three staves',4:'Four staves',5:'Five staves'}[cfg['voices']]
 c.setTitle('Bach - '+cfg['title']+f', BWV {cfg["bwv"]} - '+description);c.setAuthor('J. S. Bach; analysis checked against Keller, Prout and Tovey');c.setCreator('WTC fugue analyses')
 for page,batch in enumerate(batches):
  c.setFillColor(HexColor('#202b39'))
  if page==0:
   c.setFont('Times-Roman',20);c.drawString(left,H-34,cfg['title'])
   c.setFont('Helvetica',9);c.drawRightString(W-left,H-33,f'J. S. BACH / BWV {cfg["bwv"]}')
   c.setFont('Helvetica',8);c.drawString(left,H-50,f'WTC I, no. {cfg["number"]} / Annotated score / {description} / {cfg["meter"]}')
   legend=[(left,'S subject / A tonal answer','#244f91'),(left+190,'CS continuation','#a45112'),(left+340,'Derived figures','#637878')]
   if cfg['bwv']==867:legend.append((left+405,'q sequence','#8a6548'))
   for x,label,colour in legend:
    c.setFillColor(HexColor(colour));c.rect(x,H-67,6,6,fill=1,stroke=0);c.setFont('Helvetica-Bold',8);c.drawString(x+10,H-67,label)
   c.setFillColor(HexColor('#526174'));c.setFont('Helvetica',7)
   c.drawString(left,H-82,'* variant / fragment; > continuation; c semiquavers; q leaping quavers; p suspensions; h subject head')
   y=H-98
  else:y=H-28
  gap=min(24,(y-42-sum(h for _,h in batch))/max(1,len(batch)-1));assert gap>=9
  for s,h in batch:
   draw_score(c,R,s,TEMP/f'{mode}-{s["start"]}.png',left,y-h,width,h);y-=h+gap
  assert y+gap>38
  if page==len(batches)-1:
   c.setFillColor(HexColor('#657486'));c.setFont('Helvetica',6.7);c.drawString(left,23,'Kroll 1866 / Huron-Sapp encoding / Analysis checked against Keller, Prout and Tovey')
  page_number(c,W,page+1);c.showPage()
 c.save();print(dest.name,len(batches),'pages',flush=True)
if args.scores_only:raise SystemExit(0)
urls={
 'prout':"https://waltercosand.com/CosandScores/Composers%20L-P/Composers_P/Prout%2C%20Ebenezer/Prout-Analysis_of_Bach%27s_48_Fugues.pdf",
 'tovey':'https://s9.imslp.org/files/imglnks/usimg/4/4f/IMSLP911003-PMLP05948-Bach_-_48_Preludes_and_Fugues_%28Tovey%29_-_Book_I.pdf'}
for name,source,title,edition in [('prout',args.prout,"Ebenezer Prout: Analysis of J. S. Bach's Forty-Eight Fugues",'Ed. Louis B. Prout. London: Edwin Ashdown, 1910.'),('tovey',args.tovey,'Donald Francis Tovey: The Well-Tempered Clavier, Book I','Associated Board, 1924.')]:
 reader=PdfReader(source);writer=PdfWriter()
 for j,i in enumerate(cfg[name+'Pages']):
  original=reader.pages[i]
  if j:writer.add_page(original);continue
  w,h=float(original.mediabox.width),float(original.mediabox.height);page=writer.add_blank_page(width=w,height=h+66);page.merge_transformed_page(original,Transformation().translate(0,66))
  stream=BytesIO();c=canvas.Canvas(stream,pagesize=(w,h+66),invariant=1)
  for y,line in zip([47,35,23],[title,edition+' Printed pp. '+cfg[name+'Printed'].replace('–','-')+'.',f'BWV {cfg["bwv"]}. Complete original pages; adjoining commentary is retained.']):
   size=min(8,8*(w-40)/c.stringWidth(line,'Helvetica',8));c.setFont('Helvetica',size);c.drawString(20,y,line)
  c.setFillColor(HexColor('#244f91'));c.setFont('Helvetica',8);c.drawString(20,11,'Full source scan');c.linkURL(urls[name],(20,8,w-20,20),relative=0,thickness=0);c.save();page.merge_page(PdfReader(stream).pages[0],over=False)
 writer.add_metadata({'/Title':name.title()+f' - Analysis of Bach BWV {cfg["bwv"]}','/Author':title.split(':')[0],'/Subject':edition+' Public-domain source extract. '+urls[name]})
 dest=R/f'pdf/{name}-bwv{cfg["bwv"]}-analysis.pdf';writer.write(dest);print(dest.name,len(cfg[name+'Pages']),'pages')
