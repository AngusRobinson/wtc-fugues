import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'irneC1jhpqg',startSeconds:446,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-890'}},
 voices:voices.map((name,i)=>({name,short:'SAB'[i]})),bars:Array.from({length:93},(_,i)=>({number:i+1,start:i*3,duration:3,beatQuarters:1})),
 tempo:{initial:120,min:75,max:150,beatQuarters:1,label:'Crotchet'},initialLoop:[1,4],initialTone:'t93',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / tonal answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Syncopated countersubject',colour:'#a45112',role:'countersubject'},{id:'cs2',label:'Long-note countersubject',colour:'#843d7c',role:'countersubject'},{id:'motif',label:'Recurring figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller divides the fugue at 32. The four-bar closing cadence recalls the end of the first part.',formalSource:{label:'Keller, pp. 176–177.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv890.pdf#page=2'},map:'● Arrival · ◆ Cadence',disposition:'Positions use bar:beat; beats are crotchets.',notation:'S subject · A tonal answer · Ar real answer · * altered / incomplete · > continuation',cells:'h subject-head figure · t paired-quaver tail',edition:['Kroll, Bach-Gesellschaft XIV (1866), pp. 184–185; Humdrum encoding by David Huron, revised by Craig Sapp. Keller governs the two-part form and the six combinations of subject and countersubjects; Prout and Tovey provide complementary accounts.','Prout’s heading mistakenly gives four voices. His final tonal-answer description corresponds to the alternative B-flat at 78:3½. Kroll’s main reading has C, advocated by Tovey; that reading is retained, with E-natural in the head and A-flat in the tail.','Keller’s combinations at 49, 56 and 80 include shortened or displaced forms. The annotations distinguish them from the complete statements.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f21.krn'}},
};export default study;
