import assert from 'node:assert/strict';
import {build} from 'esbuild';
import fs from 'node:fs';
fs.mkdirSync('tmp/checks',{recursive:true});
await build({entryPoints:['lib/audio.ts'],bundle:true,platform:'node',format:'esm',outfile:'tmp/checks/audio.mjs'});
const {StudyAudio}=await import('../tmp/checks/audio.mjs');
let timerId=0;const timers=new Map();
globalThis.setInterval=fn=>{timers.set(++timerId,fn);return timerId;};
globalThis.clearInterval=id=>timers.delete(id);
class Param{value=0;setValueAtTime(v,t){assert(Number.isFinite(v)&&Number.isFinite(t));this.value=v;}linearRampToValueAtTime(v,t){this.setValueAtTime(v,t);}exponentialRampToValueAtTime(v,t){assert(v>0);this.setValueAtTime(v,t);}setTargetAtTime(v,t){this.setValueAtTime(v,t);}}
class Node{gain=new Param();frequency=new Param();Q=new Param();connect(){}disconnect(){}start(t){this.started=t;}stop(t){this.stopped=t;}}
class Context{
 static last;currentTime=0;destination={};osc=[];
 constructor(){Context.last=this;}
 createGain(){return new Node();}createBiquadFilter(){return new Node();}
 createOscillator(){const n=new Node();this.osc.push(n);return n;}
 async resume(){}async close(){}
}
globalThis.window={AudioContext:Context};
const notes=[{id:'a',voice:0,start:0,duration:4,pitch:60},{id:'b',voice:1,start:2,duration:2,pitch:64},{id:'c',voice:2,start:6,duration:1,pitch:67}];
const a=new StudyAudio(notes,{duration:606,voiceCount:4,beatQuarters:2,tempo:66});let q=-1,stopped=false;a.onPosition=p=>q=p;a.onStop=()=>stopped=true;
a.setTempo(60);await a.play(0);
assert.equal(Context.last.osc.length,1);
Context.last.currentTime=1;for(const fn of timers.values())fn();
assert.equal(q,2);assert.equal(Context.last.osc.length,2);
a.seek(3);assert.equal(a.current(),3);
assert.equal(Context.last.osc.length,4,'Both sustained voices restart when seeking into tied/sustained material.');
a.setTempo(120);Context.last.currentTime+=.25;for(const fn of timers.values())fn();assert.equal(q,4);
a.pause();assert.equal(timers.size,0);
a.setRange(0,6,false);await a.play(5);Context.last.currentTime+=1;for(const fn of [...timers.values()])fn();
assert.equal(q,6);assert(stopped);assert.equal(timers.size,0);
a.setRange(2,4,true);await a.play(2);Context.last.currentTime+=1;for(const fn of [...timers.values()])fn();assert.equal(a.current(),2,'Loop returns to the selected start.');
a.setVoices([false,true,false,false]);a.dispose();assert.equal(timers.size,0);
console.log('Audio checks passed: timing, sustained-note seek, tempo change, pause, excerpt stop, loop and cleanup.');
const extra=new StudyAudio([{id:'fifth',voice:4,start:0,duration:3,pitch:60}],{duration:10,voiceCount:5,beatQuarters:1,tempo:60});
await extra.play(0);assert.equal(extra.voices.length,5);
Context.last.currentTime=1;for(const fn of timers.values())fn();assert.equal(extra.current(),1,'Crotchet tempo uses one crotchet per second at 60.');
extra.pause();extra.seek(100);assert.equal(extra.current(),10,'Seeking clamps to this work\'s duration.');
extra.setVoices([true,true,true,true,false]);assert.equal(extra.voices[4].gain.value,0);
extra.dispose();assert.equal(timers.size,0);
console.log('Audio configuration checks passed: five voices, crotchet beat and independent duration.');
