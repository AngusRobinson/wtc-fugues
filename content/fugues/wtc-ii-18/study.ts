import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'7Hbjytwp9r4',startSeconds:296,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-887'}},
 voices:voices.map((name,i)=>({name,short:'SAB'[i]})),bars:Array.from({length:143},(_,i)=>({number:i+1,start:i*3,duration:3,beatQuarters:1.5})),
 tempo:{initial:96,min:60,max:112,beatQuarters:1.5,label:'Dotted crotchet'},initialLoop:[1,4],initialTone:'t288',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'First subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Chromatic countersubject',colour:'#a45112',role:'countersubject'},{id:'cs2',label:'Second subject',colour:'#843d7c',role:'subject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller separates the first-subject exposition and further entries, then the second-subject exposition and the combined section. The main divisions begin at 61 and 97.',formalSource:{label:'Keller, pp. 169–170.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv887.pdf#page=3'},map:'● Arrival · ◆ Cadence · ○ Key context',disposition:'Positions use bar:beat; beats are dotted crotchets.',notation:'S1 first subject · A1 real answer · S2 second subject · CS countersubject · * altered / incomplete · > continuation',cells:'h subject head · t subject tail · e link figure · c chromatic ascent · r rising sequence',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller’s double-fugue interpretation governs the analysis; entries and episodes are checked against Prout, Tovey and the score.','Keller’s high soprano entry is at 79, not the printed 73. His total of 144 counts the final bar twice for the 5:3:4 proportions; the notated score has 143 bars. The first subject’s entries at 33 and 45 are in D-sharp minor.','The score retains Kroll’s readings and printed ornaments. Tovey discusses later autograph variants and the optional extension of the second subject’s closing trill to other entries.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f18.krn'}},
};export default study;
