'use client';
import {useState} from 'react';
import {Button} from '@/components/ui/button';
import type {FugueData} from '@/lib/fugues/types';
import {barAt,barStart,barEnd,scorePosition} from '@/lib/fugues/position';
const left=83,right=1170,width=right-left;
// Preserve the engraving scale instead of stretching short examples across the page.
const exampleWidth=(svg:string)=>Number(svg.match(/viewBox="0 0 ([\d.]+)/)?.[1])||840;
export function ThematicMaterial({study,onSeek}:{study:FugueData;onSeek:(q:number)=>void}){
 const {themes,examples}=study;
 const colours=Object.fromEntries(study.materials.map(m=>[m.id,m.colour]));
 return <section className="thematic-material" aria-labelledby="themes-title"><h2 id="themes-title">{study.materials.some(m=>m.role==='countersubject')?'Subject and countersubjects':'Subjects and figures'}</h2>
 {themes.map(theme=>{const example=examples.find(e=>e.id===theme.id)!;return <figure className="theme-example" key={theme.id}>
 <figcaption><h3 style={{color:colours[theme.id]}}>{theme.title}</h3><span>{theme.location}</span><Button variant="ghost" size="sm" aria-label={'Show '+theme.title+' in the complete score'} onClick={()=>onSeek(example.start)}>Score ↗</Button></figcaption>
 <div className="theme-scroll"><div className="theme-notation" style={{width:exampleWidth(example.svg)}} role="img" aria-label={theme.title+', '+theme.location} dangerouslySetInnerHTML={{__html:example.svg}}/></div>
 <p>{theme.text}</p></figure>;})}
 </section>;
}
export function AnalyticalMap({study,onSeek,onPassage}:{study:FugueData;onSeek:(q:number,id?:string|null,scroll?:boolean)=>void;onPassage:(start:number,end:number)=>void}){
 const {formalGroups,sections,tonalEvents,voices,annotations,bars,materials}=study;
 const colours=Object.fromEntries(materials.map(m=>[m.id,m.colour]));
 const x=(q:number)=>left+q/study.score.duration*width;
 const rowBottom=34+voices.length*48,tonalY=rowBottom+15;
 const gridStep=Math.max(1,Math.ceil((bars.length-1)/10));
 const grid=bars.filter((_,i)=>i%gridStep===0);
 if(grid[grid.length-1]!==bars[bars.length-1])grid.push(bars[bars.length-1]);
 const ends=[-100,-100,-100];
 const tonalLayout=tonalEvents.map(event=>{const px=x(event.q),labelX=Math.max(left+26,Math.min(right-26,px));let row=ends.findIndex(end=>end<labelX-29);if(row<0)row=ends.indexOf(Math.min(...ends));ends[row]=labelX+29;return{...event,px,labelX,row};});
 const [toneId,setToneId]=useState(study.initialTone??tonalEvents[0]?.id),[entryId,setEntryId]=useState<string|null>(null);
 const tone=tonalEvents.find(t=>t.id===toneId);
 const entry=annotations.find(a=>a.id===entryId);
 function chooseTone(id:string,q:number){setToneId(id);onSeek(q,null,false);}
 const activate=(fn:()=>void)=>(e:React.KeyboardEvent)=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();fn();}};
 return <section className="analytical-map" aria-labelledby="map-title"><h2 id="map-title">{materials.some(m=>m.role==='countersubject')?'Entries, countersubjects and modulation':'Entries and tonal arrivals'}</h2>
 <div className="map-legend">{materials.map(m=><span key={m.id}><i style={{background:m.colour}}/>{m.label}</span>)}{annotations.some(a=>a.inverted)&&<span className="map-symbols">Hatched: inversion</span>}</div>
 <div className="analysis-map-scroll"><svg className="analysis-map-svg" viewBox={`0 0 1200 ${rowBottom+212}`} role="group" aria-label={`${formalGroups.length} principal sections, thematic entries in ${voices.length} voices, and modulation markers`}>
 <defs><pattern id="map-inversion-hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(135)"><line x1="0" y1="0" x2="0" y2="7" stroke="#fff" strokeOpacity=".65" strokeWidth="2"/></pattern></defs>
 {formalGroups.map(g=>{const a=x(g.startQ??barStart(bars,g.start)),b=x(g.endQ??barEnd(bars,g.end));return <g className="formal-group" key={g.number}>
 <title>{g.number+'. '+g.label+', bars '+g.range+'. '+g.continuation}</title>
 <line x1={a+3} x2={b-3} y1="4" y2="4" stroke="#465d7a" strokeWidth="2"/>
 <text x={a+6} y="25" className="formal-title">{g.number} · {g.label}</text>
 <text x={a+6} y="44">{g.range}</text>
 <text x={a+6} y="65" className="formal-continuation">{g.continuation}</text>
 <line x1={a} x2={a} y1="80" y2={rowBottom+89} stroke="#a9b4c2" strokeDasharray="3 4"/>
 </g>;})}
 <g transform="translate(0 89)">
 {grid.map(b=><g key={b.number}><line x1={x(b.start)} x2={x(b.start)} y1="22" y2={rowBottom} stroke="#e2e5e9"/><text x={x(b.start)} y="13" textAnchor="middle">{b.number}</text></g>)}
 <text x="8" y="13">Bar</text>
 {voices.map((voice,v)=><g key={voice.name}><text x="4" y={49+v*48} className="map-voice">{voice.name}</text><line x1={left} x2={right} y1={70+v*48} y2={70+v*48} stroke="#e6e9ed"/>
 {annotations.filter(a=>a.voice===v).map(a=>{const role=materials.find(m=>m.id===a.kind)!.role;const y=31+v*48+(role==='subject'?0:role==='cell'?29:16);const h=role==='subject'?13:role==='cell'?5:10;const w=Math.max(3,x(a.end)-x(a.start));const desc=a.name+'; '+voice.name+'; bar '+barAt(bars,a.start).number+(a.inverted?'; inversion':'');const choose=()=>{setEntryId(a.id);onSeek(a.start,a.id,false);};return <g role="button" tabIndex={0} aria-label={desc} key={a.id} className={'map-entry '+(entryId===a.id?'selected':'')} onClick={choose} onKeyDown={activate(choose)}><title>{desc}</title><rect className="map-hit" x={x(a.start)} y={y-2} width={w} height={Math.max(h+4,11)} fill="transparent"/><rect x={x(a.start)} y={y} width={w} height={h} fill={colours[a.kind]}/>{a.inverted&&<rect x={x(a.start)} y={y} width={w} height={h} fill="url(#map-inversion-hatch)"/>}</g>;})}</g>)}
 <text x="4" y={tonalY-1} className="map-tonal-label">Tonal</text><text x="4" y={tonalY+15} className="map-tonal-label">arrivals</text><line x1={left} x2={right} y1={tonalY} y2={tonalY} stroke="#707a88" strokeWidth=".8"/>
 {tonalLayout.map(t=>{const y=tonalY+29+t.row*29;return <g key={t.id} className={'tonal-marker '+(toneId===t.id?'selected':'')} role="button" tabIndex={0} aria-label={'Bar '+t.bar+': '+t.key+', '+t.type} onClick={()=>chooseTone(t.id,t.q)} onKeyDown={activate(()=>chooseTone(t.id,t.q))}><title>{'bar '+t.bar+' · '+t.key+' · '+t.evidence}</title><line x1={t.px} x2={t.px} y1={rowBottom} y2={tonalY+3} stroke="#6d7888"/><path d={'M '+t.px+' '+(tonalY+5)+' L '+t.labelX+' '+(y-13)} stroke="#abb3bd" fill="none"/>{t.type==='cadence'||t.type==='close'?<path d={'M '+t.px+' '+(tonalY-5)+' l 5 5 l -5 5 l -5 -5 Z'} fill="#35465e"/>:<circle cx={t.px} cy={tonalY} r={toneId===t.id?4:3} fill={t.type==='entry'?'#fff':'#35465e'} stroke="#35465e"/>}<rect x={t.labelX-29} y={y-12} width="58" height="23" rx="2" fill={toneId===t.id?'#e8edf4':'#fff'}/><text x={t.labelX} y={y+2} textAnchor="middle">{t.bar} {t.short}</text></g>;})}
 </g>
 </svg></div>
 <p className="formal-correspondences">{study.notes.formal} {study.notes.formalSource&&<a href={study.notes.formalSource.href} target="_blank" rel="noreferrer">{study.notes.formalSource.label}</a>}</p>
 {entry&&<p className="entry-detail"><strong>{entry.name}</strong> · {voices[entry.voice].name} · bar {barAt(bars,entry.start).number}, beat {scorePosition(bars,entry.start).split(':')[1]}{entry.status==='statement'?'':' · '+entry.status}</p>}
 {tone&&<div className="tonal-evidence" aria-live="polite"><p><strong>Bar {tone.bar} · {tone.key}.</strong> {tone.evidence}</p><Button variant="ghost" size="sm" onClick={()=>onSeek(tone.q)}>Score ↗</Button></div>}
 <p className="map-note">{study.notes.map}</p>
 <details className="disposition" open><summary>Contrapuntal disposition</summary><table><thead><tr><th>Bars</th><th>Disposition</th><th>Entries and construction</th></tr></thead><tbody>{sections.map(c=><tr key={c.start}><td><button onClick={()=>onPassage(c.start,c.end)}>{c.start}–{c.end}</button></td><td>{c.label}</td><td><strong>{c.entries}</strong><br/>{c.detail}</td></tr>)}</tbody></table><p>{study.notes.disposition}</p></details>
 <nav className="analysis-links" aria-label="Published analyses"><span>Analyses:</span>{study.metadata.analyses.map(link=><a key={link.href} href={link.href} target="_blank" rel="noreferrer">{link.label}</a>)}</nav>
 </section>;
}
