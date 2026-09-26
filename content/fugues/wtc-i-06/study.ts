import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'nz7JakMMG-c',startSeconds:134,performer:'Tineke Steenbrink',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-851'}},
 voices:voices.map((name,i)=>({name,short:['S','A','B'][i]})),bars:Array.from({length:44},(_,i)=>({number:i+1,start:i*3,duration:3,beatQuarters:1})),
 tempo:{initial:72,min:46,max:104,beatQuarters:1,label:'Crotchet'},initialLoop:[1,6],initialTone:'a21',seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Countersubject',colour:'#a45112',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller’s two-part reading emphasises the correspondences between the episodes and the two closing stretti.',formalSource:{label:'Keller, pp. 60–61.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv851.pdf#page=3'},map:'● Arrival · ◆ Cadence',disposition:'S soprano · A alto · B bass. Beats are crotchets.',notation:'S subject · A real answer · i inversion · * altered / incomplete · > continuation',cells:'c falling semiquavers · d returning-note figure · h subject head · i inversion',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. The formal reading follows Keller; Prout places his final section at bar 39. Concealed statements in bars 11 and 32 are marked as variants, separately from isolated head fragments.','The encoded turns in bars 9–11 are retained. Tovey disputes this ornament reading and recommends staccato or the thematic trill. F♯ in the bass of bar 40 agrees with the parallel at bar 18 and with Tovey’s editorial reading.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f06.krn'}},
};export default study;
