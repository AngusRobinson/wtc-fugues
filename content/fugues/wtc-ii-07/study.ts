import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'w2NkonSuEZg',startSeconds:174,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-876'}},
 voices:voices.map((name,i)=>({name,short:'SATB'[i]})),bars:Array.from({length:70},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:76,min:52,max:100,beatQuarters:1,label:'Crotchet'},initialLoop:[1,7],initialTone:'t32',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Partial countersubject',colour:'#a45112',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller centres the design on the long exposition and three subsequent stretto pairs. The subject boundary follows his five-bar example; Prout includes the next sequential bar and its resolution.',formalSource:{label:'Keller, p. 140.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv876.pdf#page=2'},map:'● Arrival · ◆ Cadence · ○ Key context',disposition:'S soprano · A alto · T tenor · B bass. Beats are crotchets.',notation:'S subject · A tonal answer · CS partial countersubject · * altered · > continuation',cells:'a fourth figure · b crotchet–quaver figure · c episodic continuation',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller supplies the principal reading; Prout and Tovey provide complementary accounts of the accompanying material.','The first stretto begins six crotchets apart, not one bar as stated by Prout. In the final pair, the soprano enters at bar 59 and the bass at bar 60; Keller reverses the voice names.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f07.krn'}},
};export default study;
