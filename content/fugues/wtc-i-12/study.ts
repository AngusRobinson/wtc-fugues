import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'74suFWTO8P0',startSeconds:150,performer:'Pieter Dirksen',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-857'}},
 voices:voices.map((name,i)=>({name,short:['S','A','T','B'][i]})),bars:Array.from({length:58},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:52,min:36,max:72,beatQuarters:1,label:'Crotchet'},initialLoop:[1,7],initialTone:'c7',seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Main CS1',colour:'#a45112',role:'countersubject'},{id:'cs2',label:'Main CS2',colour:'#843d7c',role:'countersubject'},{id:'cs3',label:'Additional CS3',colour:'#35735a',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller reads a rondo-like alternation of chromatic thematic passages and diatonic episodes, rather than closed expository groups. The headings locate the successive entries; the episodes interrupt and separate them.',formalSource:{label:'Keller, pp. 79–81.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv857.pdf#page=2'},map:'● Arrival · ◆ Cadence',disposition:'S soprano · A alto · T tenor · B bass. Beats are crotchets.',notation:'S subject · A tonal answer · CS1 / CS2 main countersubjects · CS3 additional countersubject · * variant / fragment · > continuation',cells:'e episodic link figure · ei inversion · r rising countersubject figure',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. The principal reading and the boundaries of the two main countersubjects follow Keller. Prout includes the preceding link in his first countersubject and proposes a partial counter-exposition; Tovey also identifies the additional countersubject.','The soprano enters in bar 13 after the episode in bars 10–12. The score retains Kroll’s distribution of parts and its unornamented subject. The major-mode forms, delayed soprano resolutions and final major third are preserved.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f12.krn'}},
};export default study;
