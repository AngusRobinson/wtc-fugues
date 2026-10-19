import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'oqQk2nS6gcA',startSeconds:271,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-881'}},
 voices:voices.map((name,i)=>({name,short:'SAB'[i]})),bars:[{number:0,start:0,duration:.5,beatQuarters:1},...Array.from({length:85},(_,i)=>({number:i+1,start:.5+i*2,duration:i==84?1.5:2,beatQuarters:1}))],
 tempo:{initial:76,min:48,max:108,beatQuarters:1,label:'Crotchet'},initialLoop:[0,4],initialTone:'t14-5',seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller places the recurring episodes at 17–24, 33–40, 66–71 and 78–85. They frame the exposition and three subsequent pairs of entries.',formalSource:{label:'Keller, pp. 154–155.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv881.pdf#page=3'},map:'● Arrival · ◆ Cadence · ○ Key context',disposition:'S soprano · A alto · B bass. Beats are crotchets; entry positions include the upbeat.',notation:'S subject · A tonal answer · * altered / incomplete · > continuation',cells:'r refrain · p repeated-note accompaniment · a arpeggiated bass · d semiquaver tail · q quaver figure · h head',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller’s recurrent-episode plan governs the divisions. Prout instead begins a long final section at bar 40; Tovey emphasises the contrasting characters of the two episodic types.','Prout calls the overlap of the final pair a stretto; it concerns the closing tail. The developmental bass figures in bars 56–65 are head fragments, not complete subject entries. The source’s bass rest in bar 53 is retained.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f12.krn'}},
};export default study;
