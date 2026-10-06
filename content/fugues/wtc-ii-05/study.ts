import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'MtZ8yjOgp4A',startSeconds:321,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-874'}},
 voices:voices.map((name,i)=>({name,short:'SATB'[i]})),bars:Array.from({length:50},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:2})),
 tempo:{initial:84,min:60,max:108,beatQuarters:1,label:'Crotchet'},initialLoop:[1,7],initialTone:'fs27',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'motif',label:'Four-note tail',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller divides the fugue at the F♯ minor cadence in bar 27. The second part brings the entries closer: octaves, ascending sixths, then four voices in descending thirds.',formalSource:{label:'Keller, pp. 135–136.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv874.pdf#page=2'},map:'● Arrival · ◆ Cadence',disposition:'S soprano · A alto · T tenor · B bass. Beat positions below count crotchets.',notation:'S subject · A real answer · h incomplete head · * altered form · > continuation',cells:'b four-note tail',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller’s two-part reading governs the analysis. Prout identifies the separate bass answer in bar 25; Tovey emphasises the continuity of the tail-derived texture.','The two incomplete entries, alto in bar 28 and tenor in bar 44, are distinguished from the 23 complete or altered statements. Bar references follow the 50-bar score; Keller’s final reference to bar 51 is a slip.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f05.krn'}},
};export default study;
