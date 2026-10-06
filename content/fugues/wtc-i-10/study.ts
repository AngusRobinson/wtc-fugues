import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'uVAPgZyXPNE',startSeconds:137,performer:'Frédérick Haas',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-855'}},
 voices:voices.map((name,i)=>({name,short:['S','B'][i]})),bars:Array.from({length:42},(_,i)=>({number:i+1,start:i*3,duration:3,beatQuarters:1})),
 tempo:{initial:112,min:72,max:144,beatQuarters:1,label:'Crotchet'},initialLoop:[1,5],initialTone:'fs5',seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Countersubject',colour:'#a45112',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller reads two equal spans of nineteen bars, the second inverting the disposition of the first, followed by a four-bar coda.',formalSource:{label:'Keller, pp. 74–75.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv855.pdf#page=2'},map:'● Arrival · ◆ Cadence',disposition:'S soprano · B bass. Beats are crotchets.',notation:'S subject · A real answer · CS countersubject · * variant / fragment · > continuation',cells:'e episodic semiquavers · a quaver arpeggio · d descending scale',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. The formal reading follows Keller. His printed second span, bars 20–39, is corrected to 20–38 to agree with the score and the four-bar coda. Prout and Tovey confirm the inversion of the two main episodes.','The octave passages are at two octaves in bar 19 and one octave in bar 38. The answer’s altered final note and the measured silence after the final arpeggio are retained.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f10.krn'}},
};export default study;
