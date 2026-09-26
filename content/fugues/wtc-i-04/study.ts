import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 recording:{youtubeId:'pbZkfxboS7Y',startSeconds:188,performer:'Bertrand Cuiller',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-849'}},
 metadata,voices:voices.map((name,i)=>({name,short:['SI','SII','A','T','B'][i]})),
 bars:Array.from({length:115},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:2})),
 tempo:{initial:60,min:42,max:76,beatQuarters:2,label:'Minim'},initialLoop:[1,7],initialTone:'e35',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[
 {id:'subject',label:'First subject',colour:'#244f91',role:'subject'},
 {id:'subject2',label:'Second subject',colour:'#a45112',role:'subject'},
 {id:'subject3',label:'Third subject',colour:'#7d3b7b',role:'subject'},
 {id:'motif',label:'Crotchet figure',colour:'#637878',role:'cell'}],
 annotations:annotated.annotations,
 notes:{
 examples:'',formal:'Three sections, following Keller and Tovey.',
 formalSource:{label:'Keller, pp. 53–55.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv849.pdf#page=3'},
 map:'● Harmonic arrival · ◆ Cadence · ○ Entry context. Beats are minims.',
 disposition:'Positions use bar:beat. SI and SII denote the two soprano parts.',
 notation:'S1 first subject · A1 answer · S2 second subject · S3 third subject · i inversion · * adapted / incomplete · > continuation',
 cells:'d stepwise crotchet figure · di inversion · d/2 diminution',
 edition:[
 'Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Note values, pitches and voice assignments follow this score. Scrolling playback joins ties; minim = 60 lies within Keller’s suggested range.',
 'Keller and Tovey call the later themes subjects; Prout calls them countersubjects, since neither has a separate exposition. Prout begins his final section at 73, whereas Keller and Tovey reserve the last division for the withdrawal of S2 and the combined stretti at 94.',
 'Tovey suggests an additional S1 in the soprano at 54–57 and a cross-voice reading at 85–88. Neither is marked as a settled entry here. At 96 the score retains Kroll’s minim F♯ and ensuing voice crossing. The soprano’s closing C♯ at 92 also begins S3; it is coloured as S3.'
 ],
 scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f04.krn'}
 }
};
export default study;
