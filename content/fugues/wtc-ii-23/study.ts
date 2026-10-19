import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'0Eo_inT9L14',startSeconds:137,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-892'}},
 voices:voices.map((name,i)=>({name,short:'SATB'[i]})),bars:Array.from({length:104},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:2})),
 tempo:{initial:63,min:40,max:85,beatQuarters:2,label:'Minim'},initialLoop:[1,4],initialTone:'t104',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'First subject / real answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Exposition countersubject',colour:'#a45112',role:'countersubject'},{id:'cs2',label:'Second subject',colour:'#843d7c',role:'subject'},{id:'motif',label:'Recurring figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller’s two parts distinguish the exposition from the double fugue beginning at 27–28.',formalSource:{label:'Keller, pp. 183–184.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv892.pdf#page=2'},map:'● Arrival · ◆ Cadence',disposition:'Positions use bar:beat; beats are minims.',notation:'S1 first subject · A1 real answer · CS exposition countersubject · S2 second subject · * variant / fragment · > continuation',cells:'q coiling quavers · r turning scale figure · o semitone oscillation',edition:['Kroll, Bach-Gesellschaft XIV (1866), pp. 194–197; Humdrum encoding by David Huron, revised by Craig Sapp. The notes follow Kroll. Keller and Tovey treat the theme introduced at 28 as a second subject; Prout calls it CS2. Keller’s interpretation is followed here.','Keller’s reference to the displaced soprano entry at 59 should read 60:2½. The first subject begins in the tenor at 60:1; Prout and Tovey give the correct bar. Independent S2 statements and later fragments are distinguished from the eight combinations with S1.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f23.krn'}},
};export default study;
