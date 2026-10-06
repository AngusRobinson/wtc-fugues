import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'6RQdmnx3gl8',startSeconds:110,performer:'Jacques Ogg',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-859'}},
 voices:voices.map((name,i)=>({name,short:'SATB'[i]})),bars:Array.from({length:40},(_,i)=>({number:i+1,start:i*6,duration:6,beatQuarters:1})),
 tempo:{initial:96,min:64,max:112,beatQuarters:1,label:'Crotchet'},initialLoop:[1,11],initialTone:'cs7',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer / inversion',colour:'#244f91',role:'subject'},{id:'cs1',label:'Countersubject',colour:'#a45112',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller divides the fugue at the first inverted entry. The delayed fourth exposition entry belongs to the first part; the second alternates inverted and direct entries before the final soprano statement.',formalSource:{label:'Keller, pp. 85–87.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv859.pdf#page=2'},map:'● Arrival · ◆ Cadence',disposition:'S soprano · A alto · T tenor · B bass. Beats are crotchets.',notation:'S subject · A real answer · Si inverted subject · CS countersubject · * variant / fragment · > continuation',cells:'q rising quavers · s countersubject-derived quaver pairs',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. The formal reading follows Keller. Prout and Tovey confirm the real answer, the two inverted entries and the ornamented entry in bar 25.','The final countersubject is altered and incomplete; its tenor doubling is marked only where the correspondence remains recognisable. Tonal arrivals distinguish local cadences from subject-entry pitches.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f14.krn'}},
};export default study;
