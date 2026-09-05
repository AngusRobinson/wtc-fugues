"""Preserve the public-domain analysis pages, adding provenance below the first."""
from io import BytesIO
import argparse
from pathlib import Path
from pypdf import PdfReader, PdfWriter, Transformation
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
TEMP=ROOT.parents[2]/'tmp'/ROOT.name
OUTPUT = ROOT / 'pdf'
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source-dir', type=Path, default=TEMP/'source-scans')
SOURCE_DIR = parser.parse_args().source_dir
SOURCES = [
    dict(name='prout', path=SOURCE_DIR / 'prout-bach-48.pdf', pages=[88, 89],
         title='Ebenezer Prout: Analysis of J. S. Bach\'s Forty-Eight Fugues',
         edition='Ed. Louis B. Prout. London: Edwin Ashdown, 1910. Printed pp. 85-86.',
         url='https://waltercosand.com/CosandScores/Composers%20L-P/Composers_P/Prout%2C%20Ebenezer/Prout-Analysis_of_Bach%27s_48_Fugues.pdf',
         source='Full scan: Walter Cosand Library',
         note='Fugue 46 (Book II, 22), BWV 891. Original pages, including the editorial footnote.'),
    dict(name='tovey', path=SOURCE_DIR / 'tovey-bach-ii.pdf', pages=[175, 176],
         title='Donald Francis Tovey: Forty-Eight Preludes and Fugues, Book II',
         edition='London: Associated Board, 1924. Plate A.B. 100. Printed pp. 156-157.',
         url='https://s9.imslp.org/files/imglnks/usimg/1/1c/IMSLP911004-PMLP05899-Bach_-_48_Preludes_and_Fugues_%28Tovey%29_-_Book_II.pdf',
         source='Full scan: IMSLP #911004 / Internet Archive',
         note='Fugue XXII begins near the foot of p. 156. The preceding prelude commentary is retained.')
]

OUTPUT.mkdir(parents=True, exist_ok=True)
for item in SOURCES:
    reader = PdfReader(item['path'])
    writer = PdfWriter()
    for number, index in enumerate(item['pages']):
        original = reader.pages[index]
        if number:
            writer.add_page(original)
            continue
        width, height = float(original.mediabox.width), float(original.mediabox.height)
        margin = 68
        page = writer.add_blank_page(width=width, height=height+margin)
        page.merge_transformed_page(original, Transformation().translate(0, margin))
        stream = BytesIO()
        c = canvas.Canvas(stream, pagesize=(width, height+margin))
        c.setFillColorRGB(.22, .27, .33)
        c.setStrokeColorRGB(.7, .73, .77)
        c.line(20, 59, width-20, 59)
        for y, line, bold in [(47,item['title'],True),(35,item['edition'],False),(23,item['note'],False)]:
            font = 'Helvetica-Bold' if bold else 'Helvetica'
            size = min(8, 8*(width-40)/max(1,c.stringWidth(line,font,8)))
            c.setFont(font,size)
            c.drawString(20,y,line)
        c.setFont('Helvetica',8)
        c.setFillColorRGB(.14,.31,.57)
        c.drawString(20,11,item['source'])
        c.linkURL(item['url'],(20,8,width-20,20),relative=0,thickness=0)
        c.save()
        page.merge_page(PdfReader(stream).pages[0], over=False)
    writer.add_metadata({'/Title':item['title']+' - BWV 891 analysis',
                         '/Author':item['title'].split(':')[0],
                         '/Subject':item['edition']+' Public-domain source extract. '+item['url']})
    output=OUTPUT / (item['name']+'-bwv891-analysis.pdf')
    writer.write(output)
    check=PdfReader(output)
    assert len(check.pages)==2
    assert check.pages[0].get('/Annots')
    print(f'{output}: 2 pages, {output.stat().st_size:,} bytes')
