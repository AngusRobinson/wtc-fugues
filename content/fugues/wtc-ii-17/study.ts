import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'lCcvrsgHhpk',startSeconds:251,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-886'}},
 voices:voices.map((name,i)=>({name,short:'SATB'[i]})),bars:Array.from({length:50},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:62,min:44,max:84,beatQuarters:1,label:'Crotchet'},initialLoop:[1,3],initialTone:'t124',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'First subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Second subject',colour:'#a45112',role:'countersubject'},{id:'cs2',label:'Semiquaver countersubject',colour:'#843d7c',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller distinguishes four entry groups and a coda. Bars 1–23 expand the earlier F-major fughetta, BWV 901; the new continuation begins at 24.',formalSource:{label:'Keller, pp. 166–167.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv886.pdf#page=2'},map:'● Arrival · ◆ Cadence · ○ Key context',disposition:'Positions use bar:beat; beats are crotchets.',notation:'S1 first subject · A answer · S2 second subject · CS semiquaver countersubject · * altered / incomplete · > continuation',cells:'h subject head · t subject tail · e episodic semiquavers · r sustained line · q quaver line',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller’s double-fugue interpretation and four entry groups govern the reading. Triple counterpoint is checked against Tovey and the score.','The B-flat-minor soprano entry is at 35; Keller’s 25 is a misprint. His distinction between the two subjects is retained at 16–17, where Prout describes an incomplete countersubject. The tenor stave divides in the five-part coda.','The opening subject’s D-flat at 1:3¾ corrects D natural in the encoding, following Kroll and Prout. Other readings follow Kroll rather than the later autograph readings adopted by Tovey.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f17.krn'}},
};export default study;
