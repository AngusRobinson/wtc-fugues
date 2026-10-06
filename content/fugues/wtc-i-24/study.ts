import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'UGieOVATEOM',startSeconds:330,performer:'Bob van Asperen',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-869'}},
 voices:voices.map((name,i)=>({name,short:'SATB'[i]})),bars:Array.from({length:76},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:50,min:36,max:66,beatQuarters:1,label:'Crotchet'},initialLoop:[1,16],initialTone:'b7',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Countersubject',colour:'#a45112',role:'countersubject'},{id:'motif',label:'Semiquaver figures',colour:'#637878',role:'cell'},{id:'episode',label:'Suspension sequence',colour:'#8a6548',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller declines to group the later entries into regular expositions: incomplete anticipations and contrasting episodes articulate the succession of complete statements.',formalSource:{label:'Keller, pp. 114–117.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv869.pdf#page=3'},map:'● Arrival · ◆ Cadence',disposition:'S soprano · A alto · T tenor · B bass. Beats are crotchets.',notation:'S subject · A tonal answer · CS countersubject · h anticipation · * variant / fragment · > continuation',cells:'e introductory figure · ei inversion · f closing figure · p suspension sequence',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller’s account of anticipations governs the reading. Prout groups the passages at bars 34 and 41 as stretti; his tenor entry at bar 28 is the head anticipating the complete entry at bar 30.','The soprano answer in bar 13 retains C♯ as its fifth note, as in Kroll and Tovey’s principal text; Keller discusses the alternative B. The inverted introductory figure in bar 9 is in the alto. The later bass answer begins at bar 47 beat 3½.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f24.krn'}},
};export default study;
