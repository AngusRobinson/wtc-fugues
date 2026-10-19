import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'tPhnMw5RheE',startSeconds:171,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-883'}},
 voices:voices.map((name,i)=>({name,short:'SAB'[i]})), bars:Array.from({length:70},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:84,min:56,max:112,beatQuarters:1,label:'Crotchet'},initialLoop:[1,4],initialTone:'t24',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'First subject / answer',colour:'#244f91',role:'subject'},{id:'subject2',label:'Second subject',colour:'#a45112',role:'subject'},{id:'subject3',label:'Third subject',colour:'#843d7c',role:'subject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],
annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller’s successive introductions and combinations: S1; S2; S1 + S2; S3; S1 + S3; S1 + S2 + S3.',formalSource:{label:'Keller, pp. 159–160.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv883.pdf#page=2'},map:'● Arrival · ◆ Cadence · ○ Key context',disposition:'Positions use bar:beat; beats are crotchets.',notation:'S1 first subject · A1 answer · S2 / S3 later subjects · i inversion · * altered / incomplete · > continuation',cells:'h three-quaver head · hi inversion · f falling fifth · e derived semiquavers',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller’s triple-fugue interpretation governs the divisions and thematic labels; Tovey also recognises three subjects. Prout treats the two later themes as eventual countersubjects because their separate expositions are irregular.','Prout calls the bass passage at 14–16 an incomplete real answer in stretto with the soprano. Keller stresses the misleading subject fragments; the bass passage is therefore distinguished from the ten complete or substantially complete S1 statements. The varied heads at 55 and 60 are marked with an asterisk.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f14.krn'}},
};export default study;
