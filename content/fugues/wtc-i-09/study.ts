import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'5gf-QYR1Ap0',startSeconds:98,performer:'Christian Rieger',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-854'}},
 voices:voices.map((name,i)=>({name,short:['S','A','B'][i]})),bars:Array.from({length:29},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:100,min:64,max:132,beatQuarters:1,label:'Crotchet'},initialLoop:[1,6],initialTone:'cs11',seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Countersubject continuation',colour:'#a45112',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller places the four-bar C♯ minor centre between two larger spans. Its varied soprano entry begins in bar 12, before the central episode proper.',formalSource:{label:'Keller, pp. 71–73.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv854.pdf#page=2'},map:'● Arrival · ◆ Cadence',disposition:'S soprano · A alto · B bass. Beats are crotchets.',notation:'S subject · A tonal answer (extended boundary) · CS countersubject continuation · * variant / fragment · > continuation',cells:'c semiquaver continuation · q leaping quavers · p suspensions · h subject head',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. The subject boundary and principal divisions follow Keller. Prout separates the countersubject earlier and consequently calls the opening answer real; Tovey deliberately leaves the boundary open.','The altered rhythms in bars 12 and 20 are retained. The bass has scalar quavers in bar 24 and leaping figures in bar 27. Keller discusses the revised leaping versions; Tovey accepts bar 27 but regards the corresponding change in bar 24 as less securely attested.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f09.krn'}},
};export default study;
