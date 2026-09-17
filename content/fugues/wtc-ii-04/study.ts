import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 recording:{youtubeId:'EkYsShTb4AQ',startSeconds:269,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-873'}},
 metadata,voices:voices.map((name,i)=>({name,short:'SAB'[i]})),
 bars:Array.from({length:71},(_,i)=>({number:i+1,start:i*3,duration:3,beatQuarters:.75})),
 tempo:{initial:112,min:64,max:144,beatQuarters:.75,label:'Dotted quaver'},initialLoop:[1,6],initialTone:'cs16',seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[
 {id:'subject',label:'First subject / answer',colour:'#244f91',role:'subject'},
 {id:'second',label:'Second subject',colour:'#a45112',role:'subject'},
 {id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],
 annotations:annotated.annotations,
 notes:{
 examples:'',formal:'Five groups, following Keller; episodes are included within each group.',
 formalSource:{label:'Keller, pp. 132–133.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv873.pdf#page=3'},
 map:'● Harmonic arrival · ◆ Cadence · ○ Entry context. Beats are dotted quavers.',
 disposition:'Positions use bar:beat, with four dotted-quaver beats per bar. Late entries at 48:1, 55:1 and 67:3 begin on tied notes; their metrical beginnings are shown.',
 notation:'S1 first subject · A1 real answer · S2 second subject · i inversion · * variant / incomplete statement · > continuation',
 cells:'t sequential tail · r arpeggio-and-scale figure · ch chromatic foreshadowing',
 edition:[
 'Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Formal grouping follows Keller; thematic spans and harmonic markers are editorial readings checked against the score, Prout and Tovey. Scrolling playback joins ties and omits ornaments.',
 'Keller regards the work as a borderline double fugue; Tovey treats the chromatic theme as a second subject, while Prout includes its first appearances in an extended episode. The study follows Keller’s grouping and distinguishes foreshadowings from second-subject entries. Keller’s suggested readings from the earlier C minor version are not substituted for the supplied score.'
 ],
 scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f04.krn'}
 }
};
export default study;
