import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'_yPvwJXwRtE',startSeconds:183,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-882'}},
 voices:voices.map((name,i)=>({name,short:'SAB'[i]})),bars:[{number:0,start:0,duration:2,beatQuarters:2},...Array.from({length:84},(_,i)=>({number:i+1,start:2+i*4,duration:i==83?2:4,beatQuarters:2}))],
 tempo:{initial:80,min:52,max:112,beatQuarters:2,label:'Minim'},initialLoop:[0,4],initialTone:'t32',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Countersubject 1',colour:'#a45112',role:'countersubject'},{id:'cs2',label:'Countersubject 2',colour:'#843d7c',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller’s divisions are 12 + 12 + 8 + 12 + 8 + 4 + 8 + 20 bars. The four headings group these spans; the detailed divisions follow below.',formalSource:{label:'Keller, pp. 156–157.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv882.pdf#page=2'},map:'● Arrival · ◆ Cadence · ○ Key context',disposition:'S soprano · A alto · B bass. Beats are minims; each entry begins at the half-bar.',notation:'S subject · A real answer · CS1 / CS2 countersubjects · * altered / incomplete · > continuation',cells:'q episodic quavers · m ascending minims · c crotchet figure · g gavotte figure · b bass quavers',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller governs the formal divisions and the two countersubjects in triple counterpoint. Prout names only the first countersubject and groups the entries at 20, 32 and 36 as a counter-exposition.','Tovey identifies all six dispositions of the first episodic texture and the broad transposed return of bars 12–36 in 44–68. The opening trill is written out at bars 20 and 70; synthetic playback follows the encoded pitches rather than realising every ornamental sign.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f13.krn'}},
};export default study;
