import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'EApfsZe1sxk',startSeconds:341,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-889'}},
 voices:voices.map((name,i)=>({name,short:'SAB'[i]})),bars:Array.from({length:28},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:64,min:40,max:90,beatQuarters:1,label:'Crotchet'},initialLoop:[1,3],initialTone:'t10',seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / tonal answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Main countersubject',colour:'#a45112',role:'countersubject'},{id:'cs2',label:'Second countersubject',colour:'#843d7c',role:'countersubject'},{id:'motif',label:'Recurring figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Subject boundaries and variants follow Keller; formal headings group the entries and episodes described by Prout.',formalSource:{label:'Keller, pp. 174–175.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv889.pdf#page=3'},map:'● Arrival · ◆ Cadence',disposition:'Positions use bar:beat; beats are crotchets.',notation:'S subject · A tonal answer · * altered / shortened / fragment · > continuation',cells:'q subject-derived quavers · e episodic demisemiquavers · k canon',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller governs the full subject boundary and its later variants; Prout and Tovey provide complementary accounts of the episodes and triple counterpoint.','The final C-sharp follows Keller’s major close. Tovey records this autograph reading but adopts a minor ending, as does Kroll; the unaltered transcription is retained. Other notes follow Kroll, including the readings at 6 and 17 discussed by Tovey.','Tovey identifies five combinations of the subject and two countersubjects in four vertical dispositions. Their melodic and rhythmic variants are distinguished in the annotations.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f20.krn'}},
};export default study;
