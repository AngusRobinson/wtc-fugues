import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 recording:{youtubeId:'H3Pmr8wa4vw',startSeconds:65,performer:'Ketil Haugsand',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-860'}},
 metadata,voices:voices.map((name,i)=>({name,short:'SAB'[i]})),
 bars:Array.from({length:86},(_,i)=>({number:i+1,start:i*3,duration:3,beatQuarters:1.5})),
 tempo:{initial:66,min:44,max:90,beatQuarters:1.5,label:'Dotted crotchet'},initialLoop:[1,5],initialTone:'d10',seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[
 {id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},
 {id:'cs1',label:'Countersubject',colour:'#a45112',role:'countersubject'},
 {id:'motif',label:'Episode figures',colour:'#637878',role:'cell'}],
 annotations:annotated.annotations,
 notes:{
 examples:'',formal:'Entry groups and intervening episodes.',
 formalSource:{label:'Keller, pp. 88–90.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv860.pdf#page=2'},
 map:'● Harmonic arrival · ◆ Cadence · ○ Entry context. Beats are dotted crotchets.',
 disposition:'Positions use bar:beat. The soprano at 51 and bass at 78 enter one semiquaver after the bar-line.',
 notation:'S subject · A real answer · i inversion · * adapted / incomplete statement · > continuation',
 cells:'p rising-third figure · q slower line · r semiquaver figure · ri its inversion · d scale figure',
 edition:[
 'Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. The analysis follows Keller’s account of the entries and episodes, checked against the score, Prout and Tovey. The five diagram headings are editorial groupings. Scrolling playback joins ties and omits ornaments; dotted crotchet = 66 follows Keller’s suggested range.',
 'Tovey explicitly identifies the episodes’ triple counterpoint. The added parts at the close share the soprano and bass staves.'
 ],
 scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f15.krn'}
 }
};
export default study;
