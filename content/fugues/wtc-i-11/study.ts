import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'DF8bGzcrWkY',startSeconds:96,performer:'Ursula Dütschler',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-856'}},
 voices:voices.map((name,i)=>({name,short:['S','A','B'][i]})),bars:[{number:0,start:0,duration:.5,beatQuarters:.5},...Array.from({length:72},(_,i)=>({number:i+1,start:.5+i*1.5,duration:i===71?1:1.5,beatQuarters:.5}))],
 tempo:{initial:52,min:36,max:72,beatQuarters:1.5,label:'Dotted crotchet'},initialLoop:[0,8],initialTone:'c8',seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Countersubject',colour:'#a45112',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'Keller reads two equal halves, each containing two complete entry groups and an additional alto entry. The second half begins with the upbeat in bar 36; its closing alto entry is altered and extended.',formalSource:{label:'Keller, pp. 76–78.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv856.pdf#page=2'},map:'● Arrival · ◆ Cadence · ○ Entry context',disposition:'S soprano · A alto · B bass. Beats are quavers.',notation:'S subject · A tonal answer · CS countersubject · * variant / fragment · > continuation',cells:'h head allusion · hi ascending head figure · d descending semiquaver tail',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. The formal divisions and extended closing alto entry follow Keller. Prout stops identifying the latter as subject at bar 68; Tovey describes the close as a suggestion of a closer stretto.','The opening upbeat and shortened final bar are retained. Subject spans include their closing note while distinguishing the semiquaver continuation that follows. The ornamented later entries and C♯ in bar 54 are preserved.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f11.krn'}},
};export default study;
