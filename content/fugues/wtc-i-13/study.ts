import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'z3KzC_Uu28c',startSeconds:103,performer:'Menno van Delft',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-858'}},
 voices:voices.map((name,i)=>({name,short:['S','A','B'][i]})),bars:Array.from({length:35},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:66,min:44,max:88,beatQuarters:1,label:'Crotchet'},initialLoop:[1,7],initialTone:'cs5',seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Main countersubject',colour:'#a45112',role:'countersubject'},{id:'cs2',label:'Additional countersubject',colour:'#843d7c',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller divides the fugue after the second complete entry group and its close in D♯ minor. The second part contains only two full entries; much of its thematic work falls to the head motif.',formalSource:{label:'Keller, pp. 82–84.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv858.pdf#page=2'},map:'● Arrival · ◆ Cadence',disposition:'S soprano · A alto · B bass. Beats are crotchets.',notation:'S subject · A tonal answer · CS1 main countersubject · CS2 additional countersubject · * variant / fragment · > continuation',cells:'a four-quaver head · a* reordered head · e episodic semiquavers',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. The formal division follows Keller. Prout treats the bar 11 entry as an additional exposition entry; Prout and Tovey identify the subsequent inversion at the twelfth and the recurring accompanying theme derived from the episode.','The source’s tie from a semiquaver to a quaver in the alto in bar 22 is retained: Keller distinguishes this reading from later alterations. Double sharps use the conventional cross sign.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f13.krn'}},
};export default study;
