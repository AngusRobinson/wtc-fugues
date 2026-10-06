import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'vRzFIt4nmSg',startSeconds:199,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-871'}},
 voices:voices.map((name,i)=>({name,short:'SATB'[i]})),bars:Array.from({length:28},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:60,min:44,max:80,beatQuarters:1,label:'Crotchet'},initialLoop:[1,5],initialTone:'g14',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller divides the fugue at the G minor cadence in bar 14. The second part intensifies the imitative writing and reserves the bass for the augmented entry in bar 19.',formalSource:{label:'Keller, pp. 127–128.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv871.pdf#page=2'},map:'● Arrival · ◆ Cadence',disposition:'S soprano · A alto · T tenor · B bass. Beats are crotchets.',notation:'S subject · A tonal answer · Si inversion · S×2 augmentation · * variant / fragment · > continuation',cells:'e semiquaver figure · ei inversion · h head · ti inverted tail',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller’s two-part reading and delayed bass entry govern the analysis. Prout treats bars 7–11 as a counter-exposition; Tovey supports the fourth voice’s entrance in bar 19.','The source preserves A natural in the tenor and D natural in the soprano at bar 18, the reading defended by Keller and Tovey. Keller’s final simultaneous bass–alto imitation is distinguished here from the tenor’s complete entry beginning late in bar 25.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f02.krn'}},
};export default study;
