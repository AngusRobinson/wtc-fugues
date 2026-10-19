import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'AXvI4tHiriw',startSeconds:154,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-885'}},
 voices:voices.map((name,i)=>({name,short:'SATB'[i]})),bars:Array.from({length:84},(_,i)=>({number:i+1,start:i*3,duration:3,beatQuarters:1})),
 tempo:{initial:72,min:48,max:96,beatQuarters:1,label:'Crotchet'},initialLoop:[1,5],initialTone:'t25',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Countersubject',colour:'#a45112',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller includes the tenor entry at 20 in the exposition and distinguishes the later groups at 28 and 45. The final return and extensions are shown separately.',formalSource:{label:'Keller, pp. 163–165.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv885.pdf#page=2'},map:'● Arrival · ◆ Cadence · ○ Key context',disposition:'Positions use bar:beat; beats are crotchets.',notation:'S subject · A tonal answer · CS countersubject · +3 / +6 doubling · * altered / incomplete · > continuation',cells:'a ascending semiquavers · d descending semiquaver figure',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller’s enlarged exposition and successive doublings govern the analysis. Prout and Tovey supply the detailed account of inversion at the octave, tenth and twelfth.','The predominantly three-part middle group briefly expands to four parts at 36–40. The final bass entry at 79–83, discussed by Prout and Tovey, follows the closing extension described by Keller. Bars 28–35 assign the continuing lowest line to the bass without changing any pitches or rhythms.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f16.krn'}},
};export default study;
