import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'d_DFyOgtCzw',startSeconds:90,performer:'Patrick Ayrton',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-848'}},
 voices:voices.map((name,i)=>({name,short:['S','A','B'][i]})),bars:Array.from({length:55},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:88,min:56,max:120,beatQuarters:1,label:'Crotchet'},initialLoop:[1,7],initialTone:'es22',seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Countersubject 1',colour:'#a45112',role:'countersubject'},{id:'cs2',label:'Countersubject 2',colour:'#843d7c',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'The three principal divisions follow Keller; the return begins within bar 42.',formalSource:{label:'Keller, pp. 49–51.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv848.pdf#page=3'},map:'● Arrival · ◆ Cadence · ○ Entry context',disposition:'S soprano · A alto · B bass. Beats are crotchets. There is no stretto.',notation:'S subject · A tonal answer · * variant / fragment · > continuation',cells:'d rolling thirds · di inversion · e episode dialogue · h subject head',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. The principal divisions follow Keller; Prout places the beginning of his middle section at bar 12; his printed reference to the final entry in bar 57 should read 51. The thematic variants and precise harmonic arrivals are checked against the score, Prout and Tovey.','CS1 is marked from its recurring turn figure; preceding links are excluded. Its accidental differences are retained, as discussed by Tovey. The final bar preserves the additional upper layer and the crossing subject-tail figure.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f03.krn'}},
};export default study;
