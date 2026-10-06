import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'T24-ZRHXpbQ',startSeconds:95,performer:'Korneel Bernolet',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-863'}},
 voices:voices.map((name,i)=>({name,short:'SATB'[i]})),bars:Array.from({length:41},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:63,min:44,max:80,beatQuarters:1,label:'Crotchet'},initialLoop:[1,9],initialTone:'ds3',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Main countersubject',colour:'#a45112',role:'countersubject'},{id:'cs2',label:'Second countersubject',colour:'#843d7c',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller hears progressively smaller entry groups: four voices and an additional answer, then three voices, two voices, and isolated tenor and soprano entries.',formalSource:{label:'Keller, pp. 95–97.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv863.pdf#page=2'},map:'● Arrival · ◆ Cadence · Entry key in the tonal list',disposition:'S soprano · A alto · T tenor · B bass. Beats are crotchets.',notation:'S subject · A tonal answer · CS1 main countersubject · CS2 second countersubject · * variant / fragment · > continuation',cells:'e main-CS figure · r repeated quavers · p suspensions · t tritone figure',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. The principal reading follows Keller, including the derivation of the second episodic type from the subject’s tritone. Prout calls this new material and groups the earlier middle entries as an irregular counter-exposition.','Bar 6, alto, fourth semiquaver: E♯ corrects E natural in the encoding, checked against Tovey’s score, p. 120. The original source download is retained. The B♯ in the tenor’s bar 32 entry follows the principal source reading, rather than its alternative B natural.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f18.krn'}},
};export default study;
