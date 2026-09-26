import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'su9NVEb6qEY',startSeconds:157,performer:'Bart Jacobs',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-853'}},
 voices:voices.map((name,i)=>({name,short:['S','A','B'][i]})),bars:Array.from({length:87},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:64,min:44,max:100,beatQuarters:1,label:'Crotchet'},initialLoop:[1,6],initialTone:'as19',seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer / inversion',colour:'#244f91',role:'subject'},{id:'augmentation',label:'Full / partial augmentation',colour:'#843d7c',role:'subject'},{id:'motif',label:'Subject fragments',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller’s six divisions distinguish the successive contrapuntal combinations. The last begins with the bass augmentation in bar 62; the alto anticipates it in bar 61.',formalSource:{label:'Keller, pp. 67–70.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv853.pdf#page=3'},map:'● Arrival · ◆ Cadence',disposition:'S soprano · A alto · B bass. Beats are crotchets.',notation:'S subject · A tonal answer · i inversion · ×2 full augmentation · · partial augmentation · * variant / fragment · > continuation',cells:'h subject head · t syncopated tail',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller discusses the fugue enharmonically in E♭ minor; the score here retains D♯ minor. His proposed alteration to the soprano scale in bar 15 is not adopted.','Prout begins his middle section at bar 15 and final section at bar 57. Tovey’s ten-stretto account clarifies the partially augmented forms and double counterpoint at the twelfth. At bar 45 the crossed entry remains in the soprano, following Keller and the encoded part; Prout assigns it to the alto.','Tied-in openings at bars 27, 57 and 77 remain tied. The last note of the bass augmentation at bar 67 and the alto augmentation at bar 72 also begins the next normal entry; those shared notes take the colour of the new entry.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f08.krn'}},
};export default study;
