import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'F-XocOOr4tw',startSeconds:124,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-872'}},
 voices:voices.map((name,i)=>({name,short:'SAB'[i]})),bars:Array.from({length:35},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:66,min:48,max:90,beatQuarters:1,label:'Crotchet'},initialLoop:[1,4],initialTone:'c4',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer / head',colour:'#244f91',role:'subject'},{id:'motif',label:'Derived and recurring figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller distinguishes the short cadential divisions up to bar 14 from the more sustained continuation. The four-note head becomes the principal unit of imitation.',formalSource:{label:'Keller, pp. 129–130.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv872.pdf#page=2'},map:'● Arrival · ◆ Cadence',disposition:'S soprano · A alto · B bass. Beats are crotchets.',notation:'S subject · A tonal answer · h head · i inversion · ×2 augmentation · ÷2 diminution · * variant · > continuation',cells:'d scale figure · e, f sequential figures',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller’s subject comprises eight notes; Prout takes four, Tovey twelve. Complete statements and four-note heads are distinguished here.','The malformed electronic reading in bar 29 is corrected against Kroll: C♯–E natural in the added lower part, with an alto rest before F double sharp. Tovey prints a different distribution.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f03.krn'}},
};export default study;
