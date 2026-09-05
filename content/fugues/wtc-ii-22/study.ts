import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';

const study:FugueData={
 metadata,
 voices:voices.map((name,i)=>({name,short:['S','A','T','B'][i]})),
 bars:Array.from({length:101},(_,i)=>({number:i+1,start:i*6,duration:6,beatQuarters:2})),
 tempo:{initial:66,min:40,max:100,beatQuarters:2,label:'Minim'},
 initialLoop:[1,26],initialTone:'db25',seekStep:.5,
 score:{events,audio,duration},
 systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[
  {id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},
  {id:'cs1',label:'Countersubject 1',colour:'#a45112',role:'countersubject'},
  {id:'cs2',label:'Countersubject 2',colour:'#843d7c',role:'countersubject'},
  {id:'motif',label:'Recurring cells',colour:'#637878',role:'cell'},
 ],
 annotations:annotated.annotations.map(a=>({...a,name:a.kind==='subject'
  ?([24,96].includes(a.start)?'Real answer':a.inverted?'Subject material, inversion':'Subject')
  :a.kind==='cs1'?'Countersubject 1':a.kind==='cs2'?'Countersubject 2':a.label})),
 notes:{
  examples:'Grey notes belong to the preceding phrase. Examples end at the first crotchet of their final bar.',
  formal:'I ↔ III: successive entries. II ↔ IV: paired stretti. V combines rectus and inversus.',
  formalSource:{label:'Sections after Prout.',href:'./pdf/prout-bwv891-analysis.pdf'},
  map:'● Tonic arrival · ◆ Cadence · ○ Entry context. The final B♭ marks the major closing third. Harmonic readings are based on the score.',
  disposition:'S, A, T, B = soprano, alto, tenor, bass. All seven stretti use a one-minim entry interval. The interval names disregard added octaves: the lower ninth at bar 33 sounds as a sixteenth; the lower seventh at bar 73 as a fourteenth.',
  notation:'S / Si subject material · i inversion · * variant / fragment · > continuation',
  cells:'s = subject tail · c1 = chromatic cell · c2 = detached-crotchet cell · t1 = CS1 tail',
  edition:[
   'Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. The five principal groups follow Prout; the table divides the last group to show the paired stretto separately. Countersubject identification follows Keller; later CS2 variants and the harmonic markers are editorial readings of the score. Subject labels include local melodic adjustments. Playback joins ties; ornaments and expressive timing are omitted.',
   'Prout and Tovey: public-domain extracts, with edition details and scan sources in the PDFs. Keller: external link to the German text.',
  ],
  scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc2f22.krn'},
 },
};
export default study;
