import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'M0dtEcWyJ08',startSeconds:213,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-880'}},
 voices:voices.map((name,i)=>({name,short:'SAB'[i]})),bars:Array.from({length:99},(_,i)=>({number:i+1,start:i*1.5,duration:1.5,beatQuarters:.75})),
 tempo:{initial:96,min:60,max:140,beatQuarters:.75,label:'Dotted quaver'},initialLoop:[1,5],initialTone:'t12',seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller keeps the first section through the C-major cadence in bar 29. The subsequent long episode, middle entries and pedals, and final pair form the remaining divisions shown here.',formalSource:{label:'Keller, pp. 150–152.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv880.pdf#page=2'},map:'● Arrival · ◆ Cadence · ○ Key context',disposition:'S soprano · A alto · B bass. Beats are dotted quavers.',notation:'S subject · A tonal answer · * altered / extended · > continuation',cells:'d descending tail · e sequential derivative · r quaver–semiquaver rhythm · k seventh imitation · c cadence',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller governs the first section through bar 29 and the importance of the subject’s tail. Prout begins his first episode at bar 25; Tovey distinguishes its cadential introduction from the ensuing episode.','Keller’s tenor register is labelled by its continuing part: bass at bar 14, alto at bar 52. At bar 86, C5 continues the soprano subject; F4–D4–E4 remains an added inner part on the upper stave. All source pitches, durations and ties are retained.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f11.krn'}},
};export default study;
