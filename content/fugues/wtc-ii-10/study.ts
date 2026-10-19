import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'bjJdAdR9Owg',startSeconds:273,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-879'}},
 voices:voices.map((name,i)=>({name,short:'SAB'[i]})),bars:[{number:0,start:0,duration:1,beatQuarters:1},...Array.from({length:86},(_,i)=>({number:i+1,start:1+i*4,duration:4,beatQuarters:1}))],
 tempo:{initial:138,min:80,max:180,beatQuarters:1,label:'Crotchet'},initialLoop:[0,7],initialTone:'t25',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Countersubject',colour:'#a45112',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller groups the six entries after the exposition into three pairs. Prout separates the final E-minor bass entry as a concluding section; it remains paired here with the preceding A-minor entry.',formalSource:{label:'Keller, pp. 147–149.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv879.pdf#page=2'},map:'● Arrival · ◆ Cadence · ○ Key context',disposition:'S soprano · A alto · B bass. Beats are crotchets; “upbeat” denotes the final two triplet quavers before the following bar.',notation:'S subject · A real answer · CS countersubject · * altered / incomplete · > continuation',cells:'d triplet tail · di ascending form',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller governs the paired entries and the broader countersubject. Prout concentrates on its sustained portion; Tovey stresses its division between adjacent voices.','Bar 83 uses Kroll’s C–F♯–A reading, favoured by Keller, rather than the A–F♯–B alternative. Dotted figures appear in their triplet realisation, as in the encoding and Keller’s performance reading.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f10.krn'}},
};export default study;
