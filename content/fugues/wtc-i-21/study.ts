import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'NCD5vHrTLqA',startSeconds:94,performer:'Bart Naessens',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-866'}},
 voices:voices.map((name,i)=>({name,short:'SAB'[i]})),bars:Array.from({length:48},(_,i)=>({number:i+1,start:i*3,duration:3,beatQuarters:1})),
 tempo:{initial:96,min:60,max:116,beatQuarters:1,label:'Crotchet'},initialLoop:[1,13],initialTone:'f9',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'First countersubject',colour:'#a45112',role:'countersubject'},{id:'cs2',label:'Second countersubject',colour:'#843d7c',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller divides the fugue at the alto entry in bar 22. The second part contains two pairs of complete entries, separated by the second episode and incomplete answer.',formalSource:{label:'Keller, pp. 104–106.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv866.pdf#page=2'},map:'● Arrival · ◆ Cadence',disposition:'S soprano · A alto · B bass. Beats are crotchets.',notation:'S subject · A tonal answer · CS1 / CS2 countersubjects · * variant / fragment · > continuation',cells:'b semiquaver tail · ai inverted quaver head',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller’s two-part reading and incomplete entry at bar 35 govern the analysis. Prout includes bar 35 within an entry group and separates a final section at bar 41.','The first countersubject follows Keller’s complete phrase from bar 5; Prout begins his identification at the last quaver of bar 6. Tovey discusses the subject’s internal inversions and the two countersubjects in triple counterpoint. Shared boundary notes retain the preceding material’s colour.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f21.krn'}},
};export default study;
