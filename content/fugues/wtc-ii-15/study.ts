import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'rrCNoLqvRIU',startSeconds:175,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-884'}},
 voices:voices.map((name,i)=>({name,short:'SAB'[i]})),bars:Array.from({length:72},(_,i)=>({number:i+1,start:i*1.5,duration:1.5,beatQuarters:.5})),
 tempo:{initial:48,min:32,max:64,beatQuarters:1.5,label:'Dotted crotchet'},initialLoop:[1,8],initialTone:'t18-5',seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Countersubject: part 1',colour:'#a45112',role:'countersubject'},{id:'cs2',label:'Countersubject: part 2',colour:'#843d7c',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller identifies only three entries after the exposition: bass at 33, soprano at 40 and alto at 65.',formalSource:{label:'Keller, p. 162.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv884.pdf#page=2'},map:'● Arrival · ◆ Cadence · ○ Key context',disposition:'Positions use bar:beat; beats are quavers.',notation:'S subject · A tonal answer · CS1 / CS2 parts of the countersubject · * altered · > continuation',cells:'h head-derived arpeggios · q scalar continuation · r demisemiquaver run',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller governs the subject entries. Tovey identifies the two-part countersubject and its triple counterpoint at 40–45; Prout recognises no regular countersubject.','The original encoding’s bar-30 chord ties are corrected against Kroll. The continuous run at 62–64 is allocated to the soprano. The closing appoggiatura is written out as a quaver, following Keller; the main-text reading at bar 60 follows Kroll.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f15.krn'}},
};export default study;
