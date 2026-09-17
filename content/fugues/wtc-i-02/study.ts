import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 recording:{youtubeId:'XkSJq_W58TU',startSeconds:99,performer:'Masato Suzuki',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-847'}},
 metadata,voices:voices.map((name,i)=>({name,short:['S','A','B'][i]})),
 bars:Array.from({length:31},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:63,min:40,max:108,beatQuarters:1,label:'Crotchet'},initialLoop:[1,9],initialTone:'eb11',seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[
  {id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},
  {id:'cs1',label:'Countersubject 1',colour:'#a45112',role:'countersubject'},
  {id:'cs2',label:'Countersubject 2',colour:'#843d7c',role:'countersubject'},
  {id:'motif',label:'Recurring cells',colour:'#637878',role:'cell'},
 ],annotations:annotated.annotations,
 notes:{
  examples:'Grey notes provide context. The colours define the analytical boundaries; the final bar of each example is shortened after its closing note.',
  formal:'The principal division at bar 15 follows Keller. Entries and episodes overlap at their boundary bars.',
  formalSource:{label:'Keller, pp. 45–47.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv847.pdf#page=2'},
  map:'● Tonic arrival · ◆ Cadence · ○ Entry context. Markers identify the arrival, which may follow the beginning of an entry.',
  disposition:'Voice names: S soprano, A alto, B bass. Decimal positions give bar and crotchet beat. No complete entries overlap in stretto.',
  notation:'S subject · A answer · * variant / fragment · > continuation',
  cells:'h subject head · d scale figure · q quaver counterpoint · ↑ ascending form',
  edition:[
   'Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Counterpoint boundaries and the principal division follow Keller; the harmonic markers and detailed variant spans are editorial readings checked against the score and Prout. Prout’s countersubject crosses from soprano to alto in bars 26–27 because it includes the scale link. The quaver portion labelled CS1 here is wholly in the alto.',
   'Prout is supplied as a public-domain extract; Keller is linked in German. Initial scrolling playback tempo: crotchet = 63, after Keller. Scrolling playback joins ties and retains the closing chord tones; expressive timing is omitted.',
  ],
  scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f02.krn'},
 },
};
export default study;
