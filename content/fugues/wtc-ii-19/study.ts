import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'C7K0m8OPD7I',startSeconds:111,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-888'}},
 voices:voices.map((name,i)=>({name,short:'SAB'[i]})),bars:Array.from({length:29},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:72,min:45,max:100,beatQuarters:1,label:'Crotchet'},initialLoop:[1,2],initialTone:'t60',seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / real answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Dotted accompaniment',colour:'#a45112',role:'cell'},{id:'motif',label:'Subject-tail figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller’s exposition, second group and second part beginning at 16; the closing episode and final entry form the coda.',formalSource:{label:'Keller, pp. 171–172.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv888.pdf#page=2'},map:'● Arrival · ◆ Cadence',disposition:'Positions use bar:beat; beats are crotchets.',notation:'S subject · A real answer · * altered / extended · > continuation',cells:'d dotted accompaniment · t subject-tail figure · ti inversion',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller governs the formal divisions and extended upbeats; the score is checked against Prout and Tovey.','Prout includes the bass answer at 7 in the exposition and places the middle section at 9. His final soprano entry is printed as 28–29; its extended upbeat begins at 27:3¼.','The score retains Kroll’s chromatic variants and the low A at 16. Tovey adopts several Altnikol readings and discusses the articulation of the dotted rhythms.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f19.krn'}},
};export default study;
