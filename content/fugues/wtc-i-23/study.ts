import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 recording:{youtubeId:'2I3hdaTQvcA',startSeconds:91,performer:'Diego Ares',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-868'}},
 metadata,voices:voices.map((name,i)=>({name,short:'SATB'[i]})),
 bars:Array.from({length:34},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:60,min:40,max:100,beatQuarters:1,label:'Crotchet'},initialLoop:[1,5],initialTone:'fs9',seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[
 {id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},
 {id:'cs1',label:'Countersubject',colour:'#a45112',role:'countersubject'},
 {id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],
 annotations:annotated.annotations,
 notes:{
 examples:'',formal:'Two equal halves, following Keller; each contains a four-entry group and a later pair.',
 formalSource:{label:'Keller, pp. 111–112.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv868.pdf#page=2'},
 map:'◆ Cadence · ○ Entry context. Beats are crotchets.',
 disposition:'Positions use bar:beat. Entries generally begin on a second quaver; the tenor at 11 and bass at 21 begin on beat 3½.',
 notation:'S subject · A tonal answer · i inversion · * adapted statement · > continuation',
 cells:'c countersubject opening · e episode figure · ei its inversion',
 edition:[
 'Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Formal grouping follows Keller. Thematic spans and harmonic markers are editorial readings checked against the score, Prout and Tovey. Scrolling playback joins ties and omits ornaments; its initial tempo, crotchet = 60, follows Keller.',
 'Prout emphasises the countersubject’s limited complete returns; Tovey emphasises its importance and the related episodes. Complete statements and their adapted continuations are distinguished from short derived figures. The bass entry commonly assigned to bar 22 begins at 21:3½; both inverted entries have adjusted endings.'
 ],
 scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f23.krn'}
 }
};
export default study;
