import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'4pXSan5YMnM',startSeconds:89,performer:'Olivier Fortin',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-862'}},
 voices:voices.map((name,i)=>({name,short:'SATB'[i]})),bars:Array.from({length:35},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:48,min:36,max:68,beatQuarters:1,label:'Crotchet'},initialLoop:[1,7],initialTone:'ab5',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Countersubject',colour:'#a45112',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller places three pairs of entries between the exposition and the final complete group of four voices. The broad sequences connect these groups and provide much of the fugue’s continuity.',formalSource:{label:'Keller, pp. 93–94.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv862.pdf#page=2'},map:'● Arrival · ◆ Cadence',disposition:'S soprano · A alto · T tenor · B bass. Beats are crotchets.',notation:'S subject · A tonal answer · CS countersubject · * variant / fragment · > continuation',cells:'h incomplete head · e semiquavers · p suspensions · a derived quavers',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller’s paired-entry reading is primary. Prout treats the tenor entry in bar 10 as an addition to the exposition; Tovey gives greater weight to the sequential episodes.','The opening accompanying phrase is labelled countersubject following Tovey, with its later transformations marked separately. Prout’s statement that there is no regular countersubject describes its limited recurrence as a complete phrase. The episodes in bars 11–12, 14–15 and 19–20 use triple counterpoint at the twelfth and octave.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f17.krn'}},
};export default study;
