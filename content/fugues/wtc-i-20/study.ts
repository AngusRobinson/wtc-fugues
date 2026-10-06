import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'hViR1LQh1MM',startSeconds:80,performer:'Olga Pashchenko',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-865'}},
 voices:voices.map((name,i)=>({name,short:'SATBP'[i]})),bars:Array.from({length:87},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:66,min:48,max:88,beatQuarters:1,label:'Crotchet'},initialLoop:[1,14],initialTone:'a8',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer / inversion',colour:'#244f91',role:'subject'},{id:'cs1',label:'Countersubject',colour:'#a45112',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'},{id:'pedal',label:'Tonic pedal',colour:'#728094',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller’s six groups organise successive combinations of direct and inverted subjects. Group IV continues above the start of group V.',formalSource:{label:'Keller, pp. 101–103.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv865.pdf#page=2'},map:'● Arrival · ◆ Cadence',disposition:'S soprano · A alto · T tenor · B bass · P added pedal. Beats are crotchets.',notation:'S subject · A real answer · Si inverted subject · CS countersubject · P pedal · * variant / fragment · > continuation',cells:'h subject head · d / di descending / ascending scale figure · t subject-tail figure',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller’s six-group reading governs the form. Tovey identifies an exposition countersubject; Prout’s “no regular countersubject” describes its lack of consistent complete recurrence.','The score has 87 bars, and the pair beginning in bar 73 is bass/alto: these correct Keller’s printed 85 bars and bass/soprano. The closing eight bars, commented out in the encoding, are restored and checked against Tovey and the independent Mutopia edition. Malformed final ties and one duplicate unison are corrected; the original download is retained.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f20.krn'}},
};export default study;
