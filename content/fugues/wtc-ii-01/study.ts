import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'YKyur1dMzDw',startSeconds:162,performer:'Christine Schornsheim',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-870'}},
 voices:voices.map((name,i)=>({name,short:'SAB'[i]})),bars:Array.from({length:83},(_,i)=>({number:i+1,start:i*2,duration:2,beatQuarters:1})),
 tempo:{initial:112,min:80,max:132,beatQuarters:1,label:'Crotchet'},initialLoop:[1,13],initialTone:'c13',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'tail',label:'Derived accompaniment',colour:'#a45112',role:'cell'},{id:'motif',label:'Subject head',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller’s four groups include the coda’s partial statements. The linking passage at bars 43–47 remains within the third group.',formalSource:{label:'Keller, pp. 125–126.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv870.pdf#page=2'},map:'● Arrival · ◆ Cadence',disposition:'S soprano · A alto · B bass. Beats are crotchets.',notation:'S subject · A tonal answer · * incomplete / altered · > continuation',cells:'h subject head · c semiquaver accompaniment',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller supplies the four-part plan; the second alto entry begins in bar 21, and the third long episode occupies bars 55–68.','Prout numbers the internal link at bars 43–47 as a separate episode. Prout and Tovey distinguish the derived semiquaver accompaniment from a regular countersubject; the coda entries retain only the subject’s opening.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f01.krn'}},
};export default study;
