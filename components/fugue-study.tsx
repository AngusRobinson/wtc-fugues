'use client';
import {memo,useCallback,useEffect,useLayoutEffect,useMemo,useRef,useState} from 'react';
import {Play,Pause,RotateCcw,Download} from 'lucide-react';
import {Button} from '@/components/ui/button';
import {Slider} from '@/components/ui/slider';
import {Switch} from '@/components/ui/switch';
import {Toggle} from '@/components/ui/toggle';
import {Input} from '@/components/ui/input';
import {StudyAudio} from '@/lib/audio';
import type {FugueData,ScoreSystem} from '@/lib/fugues/types';
import {barAt,barStart,barEnd,systemAt,scorePosition} from '@/lib/fugues/position';
import {ThematicMaterial,AnalyticalMap} from '@/components/analysis-overview';
const fmt=(s:number)=>Math.floor(s/60)+':'+String(Math.floor(s%60)).padStart(2,'0');
const valueOf=(v:number|readonly number[])=>typeof v==='number'?v:v[0];
const System=memo(function System({study,system,index,beat,enabled,classes,onSeek}:{study:FugueData;system:ScoreSystem;index:number;beat:number|null;enabled:boolean[];classes:string;onSeek:(q:number,annotation:string|null,scroll?:boolean)=>void}){
 const {score,tonalEvents,bars}=study;
 const ref=useRef<HTMLDivElement>(null);
 const [cursor,setCursor]=useState<{x:number;height:number}|null>(null);
 const [revision,setRevision]=useState(0);
 const notes=useMemo(()=>score.events.filter(n=>n.bar>=system.start&&n.bar<=system.end),[system,score]);
 useEffect(()=>{if(!ref.current)return;const r=new ResizeObserver(()=>setRevision(n=>n+1));r.observe(ref.current);return()=>r.disconnect();},[]);
 useLayoutEffect(()=>{
  const box=ref.current;if(!box)return;
  box.querySelectorAll('.sounding').forEach(el=>el.classList.remove('sounding'));
  if(beat===null){setCursor(null);return;}
  const rect=box.getBoundingClientRect();const xs=new Map<number,number>();
  for(const n of notes){
   const el=box.querySelector('[data-note-id="'+n.id+'"]');if(!el)continue;
   if(beat>=n.start&&beat<n.start+n.duration&&enabled[n.voice])el.classList.add('sounding');
   const head=el.querySelector('.notehead')||el;const r=head.getBoundingClientRect();
   if(r.width&&!xs.has(n.start))xs.set(n.start,r.left+r.width/2-rect.left);
  }
  const points=[...xs].sort((a,b)=>a[0]-b[0]);const before=[...points].reverse().find(p=>p[0]<=beat);const after=points.find(p=>p[0]>beat);
  let x=points[0]?.[1]??0;
  if(before){const next=after||[barEnd(bars,system.end),rect.width-18];const f=Math.max(0,Math.min(1,(beat-before[0])/Math.max(.001,next[0]-before[0])));x=before[1]+f*(next[1]-before[1]);}
  setCursor({x,height:rect.height});
 },[beat,notes,system,enabled,revision,bars]);
 return <section id={'system-'+index} className={'score-system '+classes} aria-label={'Score, bars '+system.start+' to '+system.end}>
 <div className="system-heading"><span>{system.start}–{system.end}</span><span>{tonalEvents.filter(t=>t.bar>=system.start&&t.bar<=system.end).map(t=>'bar '+t.bar+' '+t.key).join(' · ')}</span></div>
 <div className="system-scroll"><div ref={ref} className="system-engraving">
  <div role="img" aria-label={'Annotated score, bars '+system.start+' to '+system.end} onClick={e=>{const el=(e.target as Element).closest('[data-note-id]');if(el)onSeek(Number(el.getAttribute('data-time')),el.getAttribute('data-annotation-id'),false);}} dangerouslySetInnerHTML={{__html:system.svg}}/>
  {cursor&&<div className="score-cursor" aria-hidden="true" style={{left:cursor.x,height:Math.max(0,cursor.height-20)}}/>}
 </div></div>
 </section>;
});
export default function FugueStudy({study,collectionHref}:{study:FugueData;collectionHref?:string}){
 const {score,systems,bars,voices,materials,metadata,sections:chapters}=study;
 const lastBar=bars[bars.length-1].number,firstBar=bars[0].number,duration=score.duration;
 const materialColours=Object.fromEntries(materials.map(m=>[m.id,m.colour]));
 const formatPosition=(q:number)=>scorePosition(bars,q);
 const secondsPerQuarter=60/study.tempo.beatQuarters;
 const [position,setPosition]=useState(0),[playing,setPlaying]=useState(false),[tempo,setTempo]=useState(study.tempo.initial);
 const [loop,setLoop]=useState(false),[loopStart,setLoopStart]=useState(study.initialLoop[0]),[loopEnd,setLoopEnd]=useState(study.initialLoop[1]);
 const [muted,setMuted]=useState(voices.map(()=>false)),[solo,setSolo]=useState<number|null>(null);
 const [visible,setVisible]=useState<Record<string,boolean>>(Object.fromEntries(materials.map(m=>[m.id,true])));
 const [follow,setFollow]=useState(true),[size,setSize]=useState(90),[selected,setSelected]=useState<string|null>(null),[error,setError]=useState('');
 const player=useRef<StudyAudio|null>(null),toolbar=useRef<HTMLDivElement>(null);
 const enabled=useMemo(()=>muted.map((m,v)=>!m&&(solo===null||v===solo)),[muted,solo]);
 const bar=barAt(bars,position).number,activeIndex=systemAt(systems,bar);
 const selectedAnnotation=study.annotations.find(a=>a.id===selected);
 const classes=Object.entries(visible).filter(([,v])=>!v).map(([k])=>'hide-'+k).join(' ');
 useEffect(()=>{const a=new StudyAudio(score.audio,{duration,voiceCount:voices.length,beatQuarters:study.tempo.beatQuarters,tempo:study.tempo.initial});player.current=a;a.onPosition=setPosition;a.onStop=()=>setPlaying(false);return()=>{a.dispose();player.current=null;};},[study,score,duration,voices.length]);
 useEffect(()=>{player.current?.setTempo(tempo);},[tempo]);
 useEffect(()=>{player.current?.setVoices(enabled);},[enabled]);
 useEffect(()=>{player.current?.setRange(loop?barStart(bars,loopStart):0,loop?barEnd(bars,loopEnd):duration,loop);},[loop,loopStart,loopEnd,bars,duration,chapters,systems]);
 useEffect(()=>{
  if(!playing||!follow)return;
  const el=document.getElementById('system-'+activeIndex);if(!el)return;
  const r=el.getBoundingClientRect(),limit=(toolbar.current?.getBoundingClientRect().bottom??0)+12;
  if(r.top<limit||r.bottom>window.innerHeight-15)el.scrollIntoView({behavior:'smooth',block:'start'});
 },[activeIndex,playing,follow]);
 const navigate=useCallback((q:number,annotation:string|null=null,scroll=true)=>{
  q=Math.max(0,Math.min(duration,q));setSelected(annotation);
  const b=barAt(bars,q).number;
  if(loop&&(b<loopStart||b>loopEnd)){
   const c=chapters.find(c=>b>=c.start&&b<=c.end)??{start:b,end:b};setLoopStart(c.start);setLoopEnd(c.end);player.current?.setRange(barStart(bars,c.start),barEnd(bars,c.end),true);
  }
  player.current?.seek(q);setPosition(q);
  if(scroll)requestAnimationFrame(()=>document.getElementById('system-'+systemAt(systems,b))?.scrollIntoView({behavior:'smooth',block:'start'}));
 },[loop,loopStart,loopEnd,bars,duration,chapters,systems]);
 async function playPause(){if(playing){player.current?.pause();setPlaying(false);return;}try{setError('');await player.current?.play(position);setPlaying(true);}catch(e){setError(e instanceof Error?e.message:'Audio unavailable.');}}
 function selectPassage(start:number,end:number){setLoopStart(start);setLoopEnd(end);if(loop)player.current?.setRange(barStart(bars,start),barEnd(bars,end),true);navigate(barStart(bars,start));}
 return <main className="musician-study">
 {collectionHref&&<nav className="collection-back" aria-label="Collection"><a href={collectionHref}>The Well-Tempered Clavier · Fugues</a></nav>}
 <style>{materials.map(m=>`.hide-${m.id} .material-${m.id}.note,.hide-${m.id} .material-${m.id}.note *{fill:#222b36!important;stroke:#222b36!important;color:#222b36!important}.hide-${m.id} .material-${m.id}.annotation-label{visibility:hidden}`).join('')}</style>
 <header className="study-title"><div><h1>{metadata.title}</h1><p>{metadata.subtitle}</p></div><nav className="score-downloads" aria-label="Annotated score PDFs">{metadata.downloads.map(link=><a key={link.href} className="pdf-link" href={link.href} target="_blank" rel="noreferrer"><Download size={16}/>{link.label}</a>)}</nav></header>
 <ThematicMaterial study={study} onSeek={q=>navigate(q)}/>
 <AnalyticalMap study={study} onSeek={navigate} onPassage={selectPassage}/>
 <h2 id="complete-score" className="complete-score-title">Annotated score</h2>
 <div className="study-toolbar" ref={toolbar}>
  <div className="transport">
   <Button className="play-button" onClick={playPause}>{playing?<Pause size={16}/>:<Play size={16}/>} {playing?'Pause':'Play'}</Button>
   <Button variant="outline" size="icon" aria-label="Return to beginning" onClick={()=>navigate(0)}><RotateCcw size={16}/></Button>
   <span className="position-readout">{position>=duration?'End':formatPosition(position-position%study.seekStep)}</span>
   <div className="seek-control"><Slider min={0} max={duration} step={study.seekStep} value={[position]} aria-label="Score position" onValueChange={v=>navigate(valueOf(v),null,false)}/><span>{fmt(position*secondsPerQuarter/tempo)} / {fmt(duration*secondsPerQuarter/tempo)}</span></div>
   <div className="tempo-control"><label id="tempo-label">{study.tempo.label} = {tempo}</label><Slider min={study.tempo.min} max={study.tempo.max} step={1} value={[tempo]} aria-labelledby="tempo-label" onValueChange={v=>setTempo(valueOf(v))}/></div>
   <form className="go-form" onSubmit={e=>{e.preventDefault();const n=Number(new FormData(e.currentTarget).get('bar'));if(bars.some(b=>b.number===n))navigate(barStart(bars,n));}}><Input type="number" min={firstBar} max={lastBar} name="bar" placeholder="Bar" aria-label="Go to bar"/><Button type="submit" variant="outline" size="sm">Go</Button></form>
  </div>
  <div className="control-row"><div className="loop-controls"><Switch id="loop" checked={loop} onCheckedChange={setLoop}/><label htmlFor="loop">Loop</label><Input aria-label="First loop bar" type="number" min={firstBar} max={loopEnd} value={loopStart} onChange={e=>setLoopStart(Math.max(firstBar,Math.min(loopEnd,Number(e.target.value)||firstBar)))}/><span>–</span><Input aria-label="Last loop bar" type="number" min={loopStart} max={lastBar} value={loopEnd} onChange={e=>setLoopEnd(Math.min(lastBar,Math.max(loopStart,Number(e.target.value)||lastBar)))}/></div>
   <div className="follow-control"><Switch id="follow" checked={follow} onCheckedChange={setFollow}/><label htmlFor="follow">Follow</label></div>
   <div className="size-control"><label id="size-label">Score {size}%</label><Slider aria-labelledby="size-label" min={70} max={120} step={5} value={[size]} onValueChange={v=>setSize(valueOf(v))}/></div>
   <div className="voice-controls" aria-label="Voice mixer">{voices.map((v,i)=><div key={v.name}><span title={v.name}>{v.short}</span><Toggle pressed={muted[i]} onPressedChange={()=>setMuted(m=>m.map((x,j)=>i===j?!x:x))} aria-label={'Mute '+v.name}>M</Toggle><Toggle pressed={solo===i} onPressedChange={()=>{setSolo(x=>x===i?null:i);setMuted(m=>m.map((x,j)=>i===j?false:x));}} aria-label={'Solo '+v.name}>Solo</Toggle></div>)}</div>
  </div>
  <div className="annotation-controls" aria-label="Annotation layers">{materials.map(({id:kind,label})=><Toggle key={kind} pressed={visible[kind]} onPressedChange={v=>setVisible(x=>({...x,[kind]:v}))}><i style={{background:materialColours[kind]}}/>{label}</Toggle>)}<span className="notation-key">{study.notes.notation}</span></div>
  {error&&<p className="error" role="alert">{error}</p>}
 </div>
 <div className="selection-strip" aria-live="polite">{selectedAnnotation?<><strong style={{color:materialColours[selectedAnnotation.kind]}}>{selectedAnnotation.label}</strong> · {voices[selectedAnnotation.voice].name} · {formatPosition(selectedAnnotation.start)}–{formatPosition(selectedAnnotation.end)} <span>{selectedAnnotation.status==='statement'?'':selectedAnnotation.status}</span></>:<span>{study.notes.cells}</span>}</div>
 <div className="continuous-score" style={{'--score-size':size/100} as React.CSSProperties}>{systems.map((system,index)=><System study={study} key={system.start} system={system} index={index} beat={index===activeIndex?position:null} enabled={enabled} classes={classes} onSeek={navigate}/>)}</div>
 <footer><details><summary>Edition & annotation notes</summary>{study.notes.edition.map((note,i)=><p key={i}>{note}</p>)}<p><a href={study.notes.scoreSource.href} target="_blank" rel="noreferrer">{study.notes.scoreSource.label}</a>. Engraved with Verovio.</p></details></footer>
 </main>;
}
