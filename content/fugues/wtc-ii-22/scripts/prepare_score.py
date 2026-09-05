"""Compile a note-accurate, offline study from the credited Humdrum source."""
import json, re, copy
from pathlib import Path
import xml.etree.ElementTree as ET
import verovio
ROOT=Path(__file__).resolve().parents[1]
raw=(ROOT/'sources/bwv891.krn').read_text()
events=[]; clocks=[0.0]*4; bar=0; bars={}
for line_no,line in enumerate(raw.splitlines(),1):
    if not line or line[0] in '! *': continue
    if line.startswith('='):
        m=re.match(r'=(\d+)',line)
        if m:
            bar=int(m[1]); bars[bar]=line_no
            assert all(t==(bar-1)*6 for t in clocks),(bar,clocks)
        continue
    tokens=line.split('\t')
    assert len(tokens)==4,(line_no,tokens)
    for spine,t in enumerate(tokens):
        if t=='.': continue
        dm=re.search(r'(\d+)(\.*)',t);assert dm,(line_no,t)
        duration=4/int(dm[1])*sum(0.5**j for j in range(len(dm[2])+1))
        start=clocks[spine]; clocks[spine]+=duration
        if 'r' in t: continue
        pm=re.search(r'([a-g]+|[A-G]+)([#n-]*)',t);assert pm,(line_no,t)
        letters,acc=pm.groups(); letter=letters[0].lower()
        octave=3+len(letters) if letters.islower() else 4-len(letters)
        midi=12*(octave+1)+{'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}[letter]+acc.count('#')-acc.count('-')
        events.append(dict(id=f'note-L{line_no}F{spine+1}',voice=3-spine,start=start,duration=duration,pitch=midi,bar=bar,name=letter.upper()+('♭'*acc.count('-'))+('♯'*acc.count('#'))+str(octave),diatonic=octave*7+'cdefgab'.index(letter),token=t,tied=('_' in t or ']' in t)))
assert clocks==[606]*4,clocks
print('Parsed',len(events),'written notes;',len(bars),'bars.',flush=True)
opts={'inputFrom':'humdrum','pageWidth':2400,'pageHeight':20000,'scale':40,'adjustPageHeight':True,'header':'none','footer':'none','svgViewBox':True,'breaks':'auto','xmlIdSeed':891,'mnumInterval':1,'spacingStaff':7}
# The complete source timing was validated against Verovio before excerpt engraving.
mei=(ROOT/'sources/bwv891-four-voices.mei').read_text()
NS={'s':'http://www.w3.org/2000/svg','m':'http://www.music-encoding.org/ns/mei'}
XMLID='{http://www.w3.org/XML/1998/namespace}id'
ET.register_namespace('','http://www.w3.org/2000/svg')
ET.register_namespace('xlink','http://www.w3.org/1999/xlink')
notes={e['id']:e for e in events}
entry_specs=[[1,1,0,0],[5,0,0,0],[11,3,0,0],[17,2,0,0],[27,2,0,0],[27,1,0,2],[33,0,0,0],[33,3,0,2],[42,2,1,0],[46,1,1,0],[52,0,1,0],[58,3,1,0],[67,2,1,0],[67,0,1,2],[73,1,1,0],[73,3,1,2],[80,0,1,0],[80,2,0,2],[89,3,0,0],[89,1,1,2],[96,0,0,0],[96,1,0,0],[96,2,1,2],[96,3,1,2]]
entries=[]
for i,(b,voice,inv,offset) in enumerate(entry_specs):
    st=(b-1)*6+offset
    en=st+25
    # The bass/tenor inversion at the close changes its ending into cadential counterpoint.
    if b==96 and inv: en=592
    ee=[e for e in events if e['voice']==voice and st<=e['start']<en]
    assert ee and ee[0]['start']==st
    print('Entry',i+1,b,voice,'inv' if inv else 'orig',' '.join(e['name'] for e in ee[:6]),flush=True)
    entries.append(dict(id=i,bar=b,voice=voice,inverted=bool(inv),start=st,end=en,notes=[e['id'] for e in ee],pitch=ee[0]['name'],altered=(b==96)))
membership={nid:(e['id'],e['inverted']) for e in entries for nid in e['notes']}
def decorate(svg):
    root=ET.fromstring(svg)
    for g in root.iter():
        id=g.get('id','')
        if id in notes:
            n=notes[id]
            g.set('data-voice',str(n['voice']))
            g.set('data-time',str(n['start']))
            g.set('class',g.get('class','')+f' voice-{n["voice"]}')
            if id in membership:
                eid,inv=membership[id]
                g.set('data-entry',str(eid))
                g.set('class',g.get('class','')+' thematic'+(' inverse' if inv else ''))
            title=ET.Element('{http://www.w3.org/2000/svg}title')
            title.text=f'{["Soprano","Alto","Tenor","Bass"][n["voice"]]} · {n["name"]} · bar {n["bar"]}'
            g.insert(0,title)
        if g.get('class')=='staff':
            mm=re.search(r'F([1-4])',id)
            if mm: g.set('data-voice',str(4-int(mm[1])))
    out=ET.tostring(root,encoding='unicode')
    return re.sub(r'>\s+<','><',out)

# Engrave physically cropped MEI documents, preserving source note IDs.
mtree=ET.fromstring(mei)
M='{http://www.music-encoding.org/ns/mei}'
scoredef=mtree.find('.//m:scoreDef',NS)
allmeasures=mtree.findall('.//m:measure',NS)
def slice_mei(a,b,voice=None):
    sd=copy.deepcopy(scoredef)
    for head in list(sd.findall(M+'pgHead')): sd.remove(head)
    # Carry each clef forward from music preceding the excerpt.
    for staffdef in sd.findall('.//'+M+'staffDef'):
        sn=staffdef.get('n')
        latest=staffdef.find(M+'clef')
        for mm in allmeasures[:a-1]:
            for st in mm.findall(M+'staff'):
                if st.get('n')==sn:
                    cs=st.findall('.//'+M+'clef')
                    if cs: latest=cs[-1]
        current=staffdef.find(M+'clef')
        if current is not None: staffdef.remove(current)
        staffdef.insert(0,copy.deepcopy(latest))
        label=ET.SubElement(staffdef,M+'label')
        label.text=['Soprano','Alto','Tenor','Bass'][int(sn)-1] if voice is None else ''
    if voice is not None:
        sg=sd.find(M+'staffGrp')
        for st in list(sg):
            if st.tag==M+'staffDef' and int(st.get('n'))!=voice+1: sg.remove(st)
        for st in sg.findall(M+'staffDef'): st.set('n','1')
        sg.set('symbol','none')
    root=ET.Element(M+'mei',{'meiversion':'5.0'})
    mu=ET.SubElement(root,M+'music');body=ET.SubElement(mu,M+'body')
    div=ET.SubElement(body,M+'mdiv');score=ET.SubElement(div,M+'score')
    score.append(sd);sec=ET.SubElement(score,M+'section')
    for m in allmeasures[a-1:b]:
        mm=copy.deepcopy(m)
        if voice is not None:
            for st in list(mm.findall(M+'staff')):
                if int(st.get('n'))!=voice+1: mm.remove(st)
                else: st.set('n','1')
        sec.append(mm)
    ids={x.get(XMLID) for x in sec.iter()}
    for mm in sec:
        for el in list(mm):
            if any(el.get(k,'').startswith('#') and el.get(k)[1:] not in ids for k in ['startid','endid']):mm.remove(el)
    return ET.tostring(root,encoding='unicode').replace('ns0:', '').replace('xmlns:ns0=', 'xmlns=')
def engrave(a,b,voice=None):
    w=verovio.toolkit()
    w.setOptions({**opts,'inputFrom':'mei','breaks':'none'})
    assert w.loadData(slice_mei(a,b,voice))
    return decorate(w.renderToSVG(1))
windows=[]
for a in range(1,102,4):
    b=min(101,a+3)
    svg=engrave(a,b)
    windows.append(dict(start=a,end=b,svg=svg))
    (ROOT/'data/windows.json').write_text(json.dumps(windows,separators=(',',':')))
    print('Engraved bars',a,b,flush=True)
examples=[]
for name,a,b,voice in [('subject',1,5,1),('inversion',42,46,2),('counterpoint',5,9,1)]:
    svg=engrave(a,b,voice)
    rr=ET.fromstring(svg)
    for style in rr.findall('.//s:style',NS):
        style.text=style.text.replace('#'+rr.get('id'),'#'+name+'-'+rr.get('id'))
    for el in rr.iter():
        if el.get('id'): el.set('id',name+'-'+el.get('id'))
        for attr in ['href','{http://www.w3.org/1999/xlink}href']:
            val=el.get(attr)
            if val and val.startswith('#'): el.set(attr,'#'+name+'-'+val[1:])
    examples.append(dict(name=name,start=a,end=b,svg=ET.tostring(rr,encoding='unicode')))
# Sustained audio events merge tied notes, whereas engraving retains each written note.
audio=[]
for voice in range(4):
    for e in sorted([e for e in events if e['voice']==voice],key=lambda x:x['start']):
        if e['tied']:
            assert audio and audio[-1]['voice']==voice and audio[-1]['pitch']==e['pitch'] and audio[-1]['start']+audio[-1]['duration']==e['start'],e
            audio[-1]['duration']+=e['duration']
        else: audio.append({k:e[k] for k in ['id','voice','start','duration','pitch']})
data={'events':events,'audio':sorted(audio,key=lambda e:e['start']),'windows':windows,'examples':examples,'entries':entries,'duration':606}
(ROOT/'data/score.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')))
print('Saved data/score.json:',(ROOT/'data/score.json').stat().st_size,'bytes.',flush=True)
