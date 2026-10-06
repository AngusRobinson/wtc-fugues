import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 metadata,recording:{youtubeId:'NLTNyhpMEEM',startSeconds:129,performer:'Benjamin Alard',instrument:'Harpsichord',source:{label:'Netherlands Bach Society',href:'https://www.bachvereniging.nl/en/bwv/bwv-861'}},
 voices:voices.map((name,i)=>({name,short:'SATB'[i]})),bars:Array.from({length:34},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{initial:56,min:40,max:76,beatQuarters:1,label:'Crotchet'},initialLoop:[1,8],initialTone:'dm4',seekStep:.5,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{id:'subject',label:'Subject / answer',colour:'#244f91',role:'subject'},{id:'cs1',label:'Countersubject',colour:'#a45112',role:'countersubject'},{id:'motif',label:'Derived figures',colour:'#637878',role:'cell'}],annotations:annotated.annotations,
 notes:{examples:'',formal:'The overview distinguishes the exposition, the intervening entry groups and the closing stretto. Keller’s emphasis falls on the derivation of the countersubject and the two widely spaced stretti.',formalSource:{label:'Keller, pp. 91–92.',href:'https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv861.pdf#page=2'},map:'● Arrival · ◆ Cadence',disposition:'S soprano · A alto · T tenor · B bass. Beats are crotchets.',notation:'S subject · A tonal answer · CS countersubject · * variant / fragment · > continuation',cells:'t subject-tail figure · ti inversion',edition:['Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Keller’s thematic reading is primary; Prout and Tovey provide complementary formal and contrapuntal observations.','Voice labels follow the separated score staves. The additional middle part in bars 33–34 shares the alto stave in the open score. Bar references and entry voices are checked against the score; Prout’s printed first-stretto reference to bar 12 should read bar 17.'],scoreSource:{label:'Score source',href:'https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f16.krn'}},
};export default study;
