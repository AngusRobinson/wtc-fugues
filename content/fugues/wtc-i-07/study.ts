import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'kvJRRWbsgSE',startSeconds:287,performer:'Pieter-Jan Belder',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-852'}},
 voices:voices.map((name,i)=>({name,short:['S','A','B'][i]})),bars:Array.from({length:37},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:88,min:56,max:120,beatQuarters:1,label:'Crotchet'},initialLoop:[1,6],initialTone:'c17',seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Countersubject',colour:'#a45112',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'The two principal spans follow Keller. Their entries are separated by episodes; there is no stretto.',formalSource:{label:'Keller, pp. 64–65.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv852.pdf#page=4'},map:'● Arrival · ◆ Cadence',disposition:'S soprano · A alto · B bass. Beats are crotchets.',notation:'S subject · A tonal answer · * variant / fragment · > continuation',cells:'c arpeggio · r rising upbeat · q descending quavers · h subject head',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Formal divisions follow Keller. Prout places the middle section within bar 12 and the final group at bar 26. Tovey counts the early links as episodes and identifies the triple counterpoint of the three-part episode.','The entry at bar 17 begins on beat 3, as does the bass entry at bar 20. Bars 22–23 contain incomplete first-bar sequences. The final added inner part and its chromatic descent are retained.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f07.krn'}},
};export default study;
