import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'GMNfdK48n3o',startSeconds:289,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-877'}},
 voices:voices.map((name,i)=>({name,short:'SATB'[i]})),bars:Array.from({length:46},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:58,min:40,max:80,beatQuarters:1,label:'Crotchet'},initialLoop:[1,7],initialTone:'t24',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Countersubject',colour:'#a45112',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'The four entry groups follow Keller. The third contains the alto–bass stretto and C♯-minor soprano entry; the fourth extends across the later episode to the final direct and inverted combination.',formalSource:{label:'Keller, pp. 142–143.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv877.pdf#page=2'},map:'● Arrival · ◆ Cadence · ○ Key context',disposition:'S soprano · A alto · T tenor · B bass. Beats are crotchets.',notation:'S subject · A real answer · Si inversion · CS countersubject · * altered / incomplete · > continuation',cells:'h subject head · e episodic figure · u sequential / semiquaver continuation',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller governs the four-group design. Tovey places greater weight on the recurring episodic material and the countersubject.','Prout’s fourth exposition entry is soprano, not tenor; his tenor head at “bar 28” occurs in bar 24. Entry labels give the actual upbeat onsets, including bars 40 and 43 for Keller’s final two entries.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f08.krn'}},
};export default study;
