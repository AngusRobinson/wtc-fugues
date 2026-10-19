import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'Lll4ELmHHgk',startSeconds:134,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-893'}},
 voices:voices.map((name,i)=>({name,short:'SAB'[i]})),bars:[{number:0,start:0,duration:.5,beatQuarters:.5},...Array.from({length:100},(_,i)=>({number:i+1,start:.5+i*1.5,duration:1.5,beatQuarters:.5}))],
 tempo:{initial:58,min:40,max:78,beatQuarters:1.5,label:'Dotted crotchet'},initialLoop:[0,6],initialTone:'t47',seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / tonal answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Exposition countersubject',colour:'#a45112',role:'countersubject'},{id:'cs2',label:'Main countersubject',colour:'#843d7c',role:'countersubject'},{id:'motif',label:'Recurring figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller places the main divisions at 29 and 69, with a four-bar coda at 97–100.',formalSource:{label:'Keller, pp. 186–187.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv893.pdf#page=2'},map:'● Arrival · ◆ Cadence',disposition:'Positions use bar:beat; beats are quavers. Bar 0 is the upbeat.',notation:'S subject · A tonal answer · Ar real answer · CS1 exposition countersubject · CS2 main countersubject · * variant / fragment · > continuation',cells:'h subject-head fragment · t trill figure · r rocking sequence · d descending scale',edition:['Kroll, Bach-Gesellschaft XIV (1866), pp. 200–202; Humdrum encoding by David Huron, revised by Craig Sapp. Keller governs the formal divisions and the character of the later accompaniment. Tovey treats that accompaniment as a second subject; it is labelled the main countersubject here.','The subject annotations end at the sixth-bar mediant arrival shown by Prout; the following semiquavers continue into the episodes. Keller’s six-bar design and the variants at 18, 56 and 70–76 are retained. The entry labels distinguish the incomplete alto statement from the bass’s continuation.','The closing appoggiaturas in Kroll, omitted by the transcription, are restored as measured quavers, a duration explicitly permitted by Tovey. The final D-sharp is retained. The unaltered transcription is preserved; other notes follow Kroll.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f24.krn'}},
};export default study;
