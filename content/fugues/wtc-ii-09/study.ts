import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 recording:{youtubeId:'0qp9vJ_hG7I',startSeconds:374,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-878'}},
 metadata,voices:voices.map((name,i)=>({name,short:'SATB'[i]})),
 bars:Array.from({length:43},(_,i)=>({number:i+1,start:i*8,duration:8,beatQuarters:2})),
 tempo:{initial:60,min:36,max:90,beatQuarters:2,label:'Minim'},initialLoop:[1,9],initialTone:'b9',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[
 {id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},
 {id:'cs1',label:'Main countersubject',colour:'#a45112',role:'countersubject'},
 {id:'cs2',label:'Countersubject x',colour:'#843d7c',role:'countersubject'},
 {id:'cs3',label:'Countersubject y',colour:'#35735a',role:'countersubject'},
 {id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],
 annotations:annotated.annotations,
 notes:{
 examples:'Grey notes provide context outside the marked material. Beats are minims throughout.',
 formal:'The six groups follow Keller. The fourth and fifth overlap at bar 26 beat 4; the last group begins after the G♯ minor cadence.',
 formalSource:{label:'Keller, pp. 145–146.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv878.pdf#page=3'},
 map:'● Harmonic arrival · ◆ Cadence · ○ Entry context. Positions within bars are shown in minim beats.',
 disposition:'Positions use bar:beat; e.g. 26:4 means bar 26, fourth minim. S, A, T, B in the diagram denote voices. The shortened alto openings at bars 9 and 35 are shown at their sounding onset, rather than the implied beginning of the unshortened subject.',
 notation:'S subject · A answer · v ornamented variation · d diminution · * adapted statement / fragment · > continuation',
 cells:'c = countersubject-derived figure · i = altered inverted-diminution figure. Neither denotes a complete additional subject entry.',
 edition:[
 'Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Formal grouping follows Keller; recurring material and harmonic arrivals were checked against the score, Prout and Tovey. Countersubjects x and y follow Tovey’s identification; they combine with the subject in triple counterpoint, with adapted forms marked. Scrolling playback joins ties and omits expressive timing.',
 'Prout and Tovey: public-domain extracts with bibliographic details and scan links. Keller: external link to the German text. Tovey’s proposed octave alterations at bar 35 are not adopted; the inverted figure is labelled as altered.'
 ],
 scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f09.krn'}
 }
};
export default study;
