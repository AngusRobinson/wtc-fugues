import type {FugueData} from './types';

export function validateStudy(study:FugueData):void {
 const check=(ok:unknown,message:string)=>{if(!ok)throw new Error(study.metadata.id+': '+message);};
 const unique=(ids:(string|number)[],name:string)=>check(new Set(ids).size===ids.length,'Duplicate '+name);
 const {bars,score,systems,materials,annotations}=study;
 check(bars.length&&study.voices.length&&systems.length,'Missing bars, voices or systems');
 unique(bars.map(b=>b.number),'bar');
 let time=0;
 bars.forEach((bar,i)=>{
  check(bar.start===time&&bar.duration>0&&bar.beatQuarters>0,'Non-contiguous or invalid bar');
  check(!i||bar.number===bars[i-1].number+1,'Non-consecutive bar numbering');
  time+=bar.duration;
 });
 check(time===score.duration,'Bar lengths differ from score duration');
 check(study.tempo.min>0&&study.tempo.initial>=study.tempo.min&&study.tempo.initial<=study.tempo.max&&study.tempo.beatQuarters>0,'Invalid tempo');
 check(study.seekStep>0,'Invalid seek step');
 unique(materials.map(m=>m.id),'material');
 materials.forEach(m=>check(/^[a-z][a-z0-9-]*$/.test(m.id),'Invalid material ID'));
 const kinds=new Set(materials.map(m=>m.id));
 unique(annotations.map(a=>a.id),'annotation');
 const validVoice=(voice:number)=>Number.isInteger(voice)&&voice>=0&&voice<study.voices.length;
 const validSpan=(start:number,end:number)=>Number.isFinite(start)&&Number.isFinite(end)&&start>=0&&end>start&&end<=time;
 annotations.forEach(a=>check(kinds.has(a.kind)&&validVoice(a.voice)&&validSpan(a.start,a.end)&&a.name,'Invalid annotation '+a.id));
 unique(score.events.map(n=>n.id),'score note');
 for(const note of [...score.events,...score.audio])check(validVoice(note.voice)&&validSpan(note.start,note.start+note.duration)&&note.pitch>=0&&note.pitch<=127,'Invalid note '+note.id);
 score.audio.forEach((note,i)=>check(!i||note.start>=score.audio[i-1].start,'Unsorted playback notes'));
 const numbers=new Set(bars.map(b=>b.number));
 score.events.forEach(note=>{
  const bar=bars.find(b=>b.number===note.bar);
  check(bar&&note.start>=bar.start&&note.start<bar.start+bar.duration,'Incorrect note bar '+note.id);
 });
 systems.forEach((system,i)=>check(numbers.has(system.start)&&numbers.has(system.end)&&system.end>=system.start&&system.start===(i?systems[i-1].end+1:bars[0].number),'Incomplete or overlapping systems'));
 check(systems[systems.length-1].end===bars[bars.length-1].number,'Missing final system');
 check(numbers.has(study.initialLoop[0])&&numbers.has(study.initialLoop[1])&&study.initialLoop[0]<=study.initialLoop[1],'Invalid initial loop');
 for(const section of [...study.sections,...study.formalGroups])check(numbers.has(section.start)&&numbers.has(section.end)&&section.start<=section.end,'Invalid section');
 for(const group of study.formalGroups){
  const first=bars.find(b=>b.number===group.start)!,last=bars.find(b=>b.number===group.end)!;
  const start=group.startQ??first.start,end=group.endQ??(last.start+last.duration);
  check(validSpan(start,end)&&start>=first.start&&start<first.start+first.duration&&end>=last.start&&end<=last.start+last.duration,'Invalid formal boundary');
 }
 unique(study.examples.map(e=>e.id),'example');
 study.themes.forEach(theme=>check(kinds.has(theme.id)&&study.examples.some(e=>e.id===theme.id),'Theme without material or engraving'));
 unique(study.tonalEvents.map(t=>t.id),'tonal event');
 study.tonalEvents.forEach(event=>{
  const bar=bars.find(b=>b.number===event.bar);
  check(bar&&event.q>=bar.start&&event.q<bar.start+bar.duration,'Incorrect tonal event bar');
 });
 check(!study.initialTone||study.tonalEvents.some(t=>t.id===study.initialTone),'Unknown initial tonal event');
}
