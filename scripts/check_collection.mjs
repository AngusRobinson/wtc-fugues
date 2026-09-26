import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import {build} from 'esbuild';
import React from 'react';
import {renderToStaticMarkup} from 'react-dom/server';
import {readCatalogue,root,workRoot} from './catalogue.mjs';

fs.mkdirSync('tmp/checks',{recursive:true});
await build({stdin:{contents:`export {default as Study} from './components/fugue-study';export * from './lib/fugues/catalogue';export * from './lib/fugues/position';export * from './lib/fugues/validate';`,resolveDir:root,loader:'tsx'},bundle:true,packages:'external',platform:'node',format:'esm',alias:{'@':root},outfile:'tmp/checks/collection-check.mjs'});
const {Study,loadStudy,barAt,barStart,barEnd,systemAt,scorePosition,validateStudy}=await import('../tmp/checks/collection-check.mjs');
const works=readCatalogue();
const missing=Array.from({length:48},(_,i)=>`wtc-${i<24?'i':'ii'}-${String(i%24+1).padStart(2,'0')}`).find(id=>!works.some(w=>w.id===id));
if(missing)assert.equal(await loadStudy(missing),undefined,'Unavailable studies do not fall back to another fugue');
assert.equal(await loadStudy('__proto__'),undefined);
const site=path.join(root,'output/site');
const index=fs.readFileSync(path.join(site,'index.html'),'utf8');
assert(!index.includes('<script'),'The catalogue should not load any score bundle');
function checkHostedLink(href,page){
 for(const prefix of ['/','/wtc-fugues/']){
  const base=new URL(prefix,'https://pages.example');
  const target=new URL(href,new URL(page,base));
  assert.equal(target.origin,base.origin,'Internal link changed host');
  assert(target.pathname.startsWith(prefix),'Internal link escaped the repository subdirectory');
  const file=decodeURIComponent(target.pathname.slice(prefix.length));
  assert(fs.existsSync(path.join(site,file)),`Missing hosted file: ${target.pathname}`);
 }
}
for(const [,href] of index.matchAll(/href="([^"]+)"/g))checkHostedLink(href,'index.html');
for(const work of works){
 const study=await loadStudy(work.id);validateStudy(study);
 const directory=path.join(site,'fugues',work.id);
 assert(index.includes(`./fugues/${work.id}/index.html`));
 const packed=fs.readFileSync(path.join(directory,'index.html'),'utf8');
 assert(!/<script[^>]+src=/.test(packed));assert(!/<link[^>]+(?:stylesheet|preload)/.test(packed));
 assert(packed.includes('data-collection-href="../../index.html"'));
 const rendered=renderToStaticMarkup(React.createElement(Study,{study,collectionHref:'../../index.html'}));
 assert.equal((rendered.match(/class="tonal-roman"/g)||[]).length,study.tonalEvents.length,'Every tonal marker has a Roman numeral');
 const arrivals=study.tonalEvents.filter(t=>['arrival','cadence','close'].includes(t.type));
 assert.equal((rendered.match(/class="score-tone"/g)||[]).length,arrivals.length,'The full score shows harmonic arrivals, not entry-only key contexts');
 for(const t of arrivals)assert(study.score.events.some(n=>Math.abs(n.start-t.q)<1e-7&&n.bar===t.bar),'No engraved anchor for '+work.id+' '+t.id);
 for(const event of study.tonalEvents){
  assert.equal(event.roman,event.key.endsWith('minor')?event.roman.toLowerCase():event.roman.toUpperCase(),'Roman-numeral case follows key mode');
 }
 const ids=[...rendered.matchAll(/\sid="([^"]+)"/g)].map(x=>x[1]);
 assert.equal(new Set(ids).size,ids.length,'Duplicate identifiers in '+work.id);
 for(const [,href] of rendered.matchAll(/href="([^"]+)"/g)){
  if(href.startsWith('http'))continue;
  checkHostedLink(href,`fugues/${work.id}/index.html`);
  const [file,fragment]=href.split('#');
  if(file)assert(fs.existsSync(path.resolve(directory,file)),`Broken link: ${work.id} ${href}`);
  else if(fragment)assert(ids.includes(fragment));
 }
 for(const file of work.publicFiles){
  const target=file==='sources/NOTICE.txt'?'SOURCE-NOTICES.txt':file;
  assert.deepEqual(fs.readFileSync(path.join(directory,target)),fs.readFileSync(path.join(workRoot(work.id),file)));
 }
}

// A deliberately different fixture exposes assumptions hidden by the current fugue:
// variable bar lengths, two/five voices, an additional subject, and uneven systems.
for(const voiceCount of [2,5]){
 const bars=[{number:1,start:0,duration:3,beatQuarters:1},{number:2,start:3,duration:3,beatQuarters:1},{number:3,start:6,duration:4,beatQuarters:1}];
 const note={id:'fixture-note',voice:voiceCount-1,start:6,duration:1,pitch:60,bar:3};
 const fixture={
  metadata:{id:'test-fixture',title:'Fixture fugue',subtitle:'Fixture subtitle',downloads:[],analyses:[]},
  bars,voices:Array.from({length:voiceCount},(_,i)=>({name:'Voice '+(i+1),short:String(i+1)})),
  tempo:{initial:60,min:40,max:120,beatQuarters:1,label:'Crotchet'},initialLoop:[1,3],seekStep:.25,
  score:{events:[note],audio:[note],duration:10},
  systems:[{start:1,end:1,svg:'<svg></svg>'},{start:2,end:3,svg:'<svg></svg>'}],
  materials:[{id:'subject2',label:'Second subject',role:'subject',colour:'#244f91'}],
  annotations:[{id:'fixture-entry',kind:'subject2',voice:voiceCount-1,start:6,end:7,label:'S2',name:'Second subject',inverted:false,status:'statement'}],
  themes:[],examples:[],formalGroups:[],sections:[],tonalEvents:[],
  notes:{examples:'',formal:'',map:'',disposition:'',notation:'',cells:'',edition:[],scoreSource:{label:'Fixture source',href:'https://example.com/'}},
 };
 validateStudy(fixture);
 const rendered=renderToStaticMarkup(React.createElement(Study,{study:fixture}));
 assert.equal((rendered.match(/aria-label="Mute Voice/g)||[]).length,voiceCount);
 assert(rendered.includes('Crotchet = 60'));
 assert(rendered.includes('0:10'));
 assert(rendered.includes('.hide-subject2 .material-subject2.note'));
 assert(rendered.includes(`${voiceCount} voices, and modulation markers`));
 assert(!/BWV 891|Keller|Prout|Countersubject 1|B♭/.test(rendered),'Work-specific content leaked into shared rendering');
 assert.equal(barAt(bars,6).number,3);assert.equal(barAt(bars,10).number,3);
 assert.equal(barStart(bars,2),3);assert.equal(barEnd(bars,3),10);
 assert.equal(scorePosition(bars,7.5),'3:2½');assert.equal(systemAt(fixture.systems,2),1);
 assert.throws(()=>validateStudy({...fixture,score:{...fixture.score,duration:9}}));
}
const compoundBars=[{number:1,start:0,duration:3,beatQuarters:.75},{number:2,start:3,duration:3,beatQuarters:.75}];
assert.equal(scorePosition(compoundBars,.25),'1:1⅓');
assert.equal(scorePosition(compoundBars,.5),'1:1⅔');
assert.equal(scorePosition(compoundBars,2.75),'1:4⅔');
assert.equal(scorePosition(compoundBars,3),'2:1');
const sixEight=[{number:1,start:0,duration:3,beatQuarters:1.5}];
assert.equal(scorePosition(sixEight,.25),'1:1⅙');
assert.equal(scorePosition(sixEight,1.25),'1:1⅚');
console.log('Collection checks passed: catalogue, document links, unchanged PDFs, unique IDs, variable metres, compound beats, two/five voices, extra subjects and missing-work handling.');
