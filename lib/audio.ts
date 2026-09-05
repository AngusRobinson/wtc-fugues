export type SoundNote={id:string;voice:number;start:number;duration:number;pitch:number};
export class StudyAudio {
 private ctx:AudioContext|null=null;
 private master:GainNode|null=null;
 private voices:GainNode[]=[];
 private sounding:OscillatorNode[]=[];
 private timer:ReturnType<typeof setInterval>|null=null;
 private origin=0;
 private position=0;
 private next=0;
 private bpm:number;
 private range:[number,number];
 private loop=false;
 private running=false;
 private enabled:boolean[];
 onPosition:(beat:number)=>void=()=>{};
 onStop:()=>void=()=>{};
 constructor(private notes:SoundNote[],private config:{duration:number;voiceCount:number;beatQuarters:number;tempo:number}){
  this.bpm=config.tempo;this.range=[0,config.duration];this.enabled=Array(config.voiceCount).fill(true);
 }
 private async init(){
  if(!this.ctx){
   const audioWindow=window as typeof window & {webkitAudioContext?:typeof AudioContext};
   const Ctor=window.AudioContext||audioWindow.webkitAudioContext;
   if(!Ctor)throw new Error('This browser does not support audio playback.');
   this.ctx=new Ctor();this.master=this.ctx.createGain();this.master.gain.value=.65;this.master.connect(this.ctx.destination);
   this.voices=Array.from({length:this.config.voiceCount},(_,i)=>{const g=this.ctx!.createGain();g.gain.value=this.enabled[i]?1:0;g.connect(this.master!);return g;});
  }
  await this.ctx.resume();
 }
 private secondsPerQuarter(){return 60/(this.bpm*this.config.beatQuarters);}
 current(){return this.running&&this.ctx?Math.min(this.range[1],this.position+(this.ctx.currentTime-this.origin)/this.secondsPerQuarter()):this.position;}
 setVoices(enabled:boolean[]){this.enabled=enabled;this.voices.forEach((g,i)=>g.gain.setTargetAtTime(enabled[i]?1:0,this.ctx!.currentTime,.02));}
 setTempo(bpm:number){const q=this.current();this.bpm=bpm;if(this.running)this.rebase(q);else this.position=q;}
 setRange(start:number,end:number,loop:boolean){this.range=[start,end];this.loop=loop;if(this.running){const q=this.current();this.rebase(q<start||q>=end?start:q);}}
 private clearSound(){this.sounding.forEach(o=>{try{o.stop();}catch{}});this.sounding=[];}
 private rebase(q:number){
  this.clearSound();this.position=q;this.origin=this.ctx!.currentTime;
  this.next=this.notes.findIndex(n=>n.start+n.duration>q);
  if(this.next<0)this.next=this.notes.length;
  this.tick();
 }
 async play(q=this.position){
  await this.init();this.running=true;
  if(q<this.range[0]||q>=this.range[1])q=this.range[0];
  this.rebase(q);
  if(this.timer)clearInterval(this.timer);
  this.timer=setInterval(()=>this.tick(),25);
 }
 pause(){this.position=this.current();this.running=false;if(this.timer)clearInterval(this.timer);this.timer=null;this.clearSound();this.onPosition(this.position);}
 seek(q:number){q=Math.max(0,Math.min(this.config.duration,q));if(this.running)this.rebase(q);else{this.position=q;this.onPosition(q);}}
 private sound(n:SoundNote,at:number,duration:number){
  const ctx=this.ctx!;const envelope=ctx.createGain();const filter=ctx.createBiquadFilter();
  filter.type='lowpass';filter.frequency.value=2800;filter.Q.value=.3;
  const osc=ctx.createOscillator();osc.type='triangle';osc.frequency.value=440*2**((n.pitch-69)/12);
  osc.connect(filter);filter.connect(envelope);envelope.connect(this.voices[n.voice]);
  const end=at+Math.max(.045,duration);
  envelope.gain.setValueAtTime(0,at);envelope.gain.linearRampToValueAtTime(.15,at+.008);
  envelope.gain.exponentialRampToValueAtTime(.07,Math.min(at+.22,end-.012));
  envelope.gain.setValueAtTime(.07,Math.max(at+.025,end-.025));envelope.gain.linearRampToValueAtTime(0,end+.025);
  osc.start(at);osc.stop(end+.04);this.sounding.push(osc);
  osc.onended=()=>{osc.disconnect();filter.disconnect();envelope.disconnect();this.sounding=this.sounding.filter(o=>o!==osc);};
 }
 private tick(){
  if(!this.running||!this.ctx)return;
  let q=this.current();
  if(q>=this.range[1]-.001){
   if(this.loop){this.rebase(this.range[0]);return;}
   this.pause();this.position=this.range[1];this.onPosition(this.position);this.onStop();return;
  }
  const horizon=q+.13/this.secondsPerQuarter();
  while(this.next<this.notes.length){
   const n=this.notes[this.next];if(n.start>horizon||n.start>=this.range[1])break;
   this.next++;
   const begin=Math.max(n.start,this.position);
   const end=Math.min(n.start+n.duration,this.range[1]);
   if(end<=q||end<=begin)continue;
   const at=Math.max(this.ctx.currentTime+.004,this.origin+(begin-this.position)*this.secondsPerQuarter());
   this.sound(n,at,(end-Math.max(begin,q))*this.secondsPerQuarter());
  }
  this.onPosition(q);
 }
 dispose(){this.pause();void this.ctx?.close();this.ctx=null;}
}
