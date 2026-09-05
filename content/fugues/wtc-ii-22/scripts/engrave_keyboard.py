"""Engrave the four contrapuntal voices on a keyboard grand staff."""
import copy, json, re
from pathlib import Path
import xml.etree.ElementTree as ET
import verovio

ROOT = Path(__file__).resolve().parents[1]
TEMP=ROOT.parents[2]/'tmp'/ROOT.name
OUT = TEMP/'pdfs/keyboard'
OUT.mkdir(parents=True, exist_ok=True)
M = '{http://www.music-encoding.org/ns/mei}'
V = '{http://www.w3.org/2000/svg}'
ID = '{http://www.w3.org/XML/1998/namespace}id'
NS = {'m': M[1:-1], 's': V[1:-1]}
ET.register_namespace('', M[1:-1])
source = ET.parse(ROOT / 'sources/bwv891-four-voices.mei').getroot()
root = copy.deepcopy(source)
score = json.loads((ROOT / 'data/score.json').read_text())
notes = {n['id']: n for n in score['events']}
annotations = json.loads((ROOT / 'data/annotations.json').read_text())['annotations']
members = {nid: a for a in annotations for nid in a['notes']}
colours = {'subject':'#244f91','cs1':'#a45112','cs2':'#843d7c','motif':'#637878'}

# A fixed treble/bass pair replaces the four independent clef streams.
definition = root.find('.//m:scoreDef', NS)
for child in list(definition):
    definition.remove(child)
group = ET.SubElement(definition, M+'staffGrp', {'symbol':'brace','bar.thru':'true'})
for staff, clef, line in [(1,'G','2'),(2,'F','4')]:
    sd = ET.SubElement(group, M+'staffDef', {'n':str(staff),'lines':'5'})
    ET.SubElement(sd, M+'clef', {'shape':clef,'line':line})
    ET.SubElement(sd, M+'keySig', {'sig':'5f','mode':'minor','pname':'b'})
    ET.SubElement(sd, M+'meterSig', {'count':'3','unit':'2'})
section = root.find('.//m:section', NS)
for child in list(section):
    if child.tag == M+'scoreDef':
        section.remove(child)

for measure in root.findall('.//m:measure', NS):
    old = list(measure.findall('m:staff', NS))
    assert len(old) == 4
    for staff in old:
        measure.remove(staff)
    for pair in range(2):
        staff = ET.Element(M+'staff', {'n':str(pair+1), ID:f'keyboard-staff-{measure.get("n")}-{pair+1}'})
        measure.insert(pair, staff)
        layers = [old[pair*2+i].find('m:layer', NS) for i in range(2)]
        active = [bool(layer.findall('.//m:note', NS)) for layer in layers]
        for i, layer in enumerate(layers):
            layer.set('n', str(i+1))
            for parent in layer.iter():
                for child in list(parent):
                    if child.tag == M+'clef':
                        parent.remove(child)
            for note in layer.findall('.//m:note', NS):
                note.set('stem.dir', 'up' if i == 0 else 'down')
                annotation = members.get(note.get(ID))
                if annotation:
                    note.set('color', colours[annotation['kind']])
            # Suppress empty voice rests when another voice occupies the staff;
            # show one centred rest when both voices are silent.
            if not active[i] and (any(active) or i == 1):
                for rest in layer.findall('.//m:mRest', NS):
                    rest.set('visible', 'false')
            staff.append(layer)
        # Accidentals now share a stave. Preserve the source's explicit signs
        # and add cancellations where the other voice changed the same pitch.
        state={}
        by_time={}
        for note in staff.findall('.//m:note', NS):
            event=notes[note.get(ID)]
            natural=12*(int(note.get('oct'))+1)+{'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}[note.get('pname')]
            alteration=event['pitch']-natural
            accidental=note.find('m:accid',NS)
            target=accidental if accidental is not None else note
            target.set('accid.ges',{-2:'ff',-1:'f',0:'n',1:'s',2:'ss'}[alteration])
            by_time.setdefault(event['start'],[]).append((note,event,alteration))
        for time, simultaneous in sorted(by_time.items()):
            updates={}
            for note,event,alteration in simultaneous:
                key=(note.get('pname'),note.get('oct'))
                default=-1 if key[0] in 'beadg' else 0
                previous=state.get(key,default)
                conflicts=any(other.get('pname')==key[0] and other.get('oct')==key[1] and alt!=alteration for other,_,alt in simultaneous)
                if not event['tied'] and (previous!=alteration or conflicts):
                    accidental=note.find('m:accid',NS)
                    target=accidental if accidental is not None else note
                    target.set('accid',{-2:'ff',-1:'f',0:'n',1:'s',2:'ss'}[alteration])
                if not event['tied'] or note.get('accid'):
                    updates[key]=None if conflicts else alteration
            state.update(updates)
    for child in list(measure):
        if child.tag == M+'staff':
            continue
        original_staff = child.get('staff')
        if original_staff:
            v = int(original_staff)-1
            child.set('staff', str(v//2+1))
            if child.tag == M+'fermata':
                if v in [1,3]:
                    measure.remove(child)
                    continue
                child.set('place', 'above')
        if child.tag == M+'tie':
            v = notes[child.get('startid')[1:]]['voice']
            child.set('curvedir', 'above' if v%2 == 0 else 'below')

ranges = [(a, 101 if a == 97 else a+3) for a in range(1,98,4)]
for start, end in ranges:
    if start > 1:
        measure = section.find(f'm:measure[@n="{start}"]', NS)
        section.insert(list(section).index(measure), ET.Element(M+'pb'))
    for a in annotations:
        included = [notes[nid] for nid in a['notes'] if start <= notes[nid]['bar'] <= end]
        if not included:
            continue
        first = included[0]
        measure = section.find(f'm:measure[@n="{first["bar"]}"]', NS)
        v = a['voice']
        direction = ET.SubElement(measure, M+'dir', {
            'staff':str(v//2+1), 'startid':'#'+first['id'],
            'place':'above' if v%2 == 0 else 'below', 'color':colours[a['kind']],
            ID:f'keyboard-label-{a["id"]}-{start}'})
        label = ['S','A','T','B'][v]+': '+a['label']+(' >' if a['start']<(start-1)*6 else '')
        ET.SubElement(direction, M+'rend', {'fontfam':'Arial','fontweight':'bold','fontstyle':'normal','fontsize':'small'}).text = label

# The transformation changes layout, not pitches, durations, rests or ties.
def signature(node):
    return {n.get(ID): {k:v for k,v in n.attrib.items() if k not in ['stem.dir','color','accid','accid.ges']}
            for n in node.findall('.//m:note',NS)}
assert signature(root) == signature(source)
assert len(root.findall('.//m:note',NS)) == 1828
assert len(root.findall('.//m:tie',NS)) == 76
mei = ET.tostring(root, encoding='unicode')
(OUT / 'keyboard.mei').write_text(mei)
tk = verovio.toolkit()
tk.setOptions({'inputFrom':'mei','pageWidth':2300,'pageHeight':20000,'scale':40,
               'adjustPageHeight':True,'header':'none','footer':'none','svgViewBox':True,
               'breaks':'encoded','xmlIdSeed':891,'mnumInterval':1,'spacingStaff':14})
assert tk.loadData(mei)
assert tk.getPageCount() == len(ranges)
tk.renderToMIDI()
for nid,event in notes.items():
    assert tk.getMIDIValuesForElement(nid)['pitch']==event['pitch'],nid
systems=[]
rendered=[]
for page,(start,end) in enumerate(ranges,1):
    svg=tk.renderToSVG(page)
    svg=re.sub(r'>\s+<','><',svg)
    rr=ET.fromstring(svg)
    rendered.extend(e.get('id') for e in rr.iter() if e.get('id') in notes)
    systems.append({'start':start,'end':end,'svg':svg})
assert len(rendered) == len(set(rendered)) == 1828
(OUT / 'systems.json').write_text(json.dumps(systems,ensure_ascii=False,separators=(',',':')))
print(f'Keyboard engraving: {len(systems)} systems; 1,828 notes and 76 ties preserved.')
