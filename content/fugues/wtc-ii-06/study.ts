import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'JVbT-Cq10AA',startSeconds:119,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-875'}},
 voices:voices.map((name,i)=>({name,short:'SAB'[i]})),bars:Array.from({length:27},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:72,min:52,max:90,beatQuarters:1,label:'Crotchet'},initialLoop:[1,8],initialTone:'d10',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Countersubject',colour:'#a45112',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'The divisions follow the exposition, direct and inverted stretti, extended episode and closing entries. Keller stresses the fugue’s restricted tonal range and the two stretti a crotchet apart.',formalSource:{label:'Keller, pp. 138–139.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv875.pdf#page=3'},map:'● Arrival · ◆ Cadence · ○ Key context',disposition:'S soprano · A alto · B bass. Beats are crotchets.',notation:'S subject · A real answer · Si inversion · CS countersubject · * incomplete / altered · > continuation',cells:'h triplet head · hi inversion · e semiquavers · t countersubject tail · c chromatic descent',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller’s two principal stretti and interrupted approach to F major govern the reading. Prout and Tovey distinguish complete statements from the shorter triplet dialogue.','The soprano remains in the upper octave at bars 13–14, following the corrected reading described by Keller. The lower-octave ossia is not combined with it.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f06.krn'}},
};export default study;
