import type {SoundNote} from '../audio';

export interface WorkLink {label:string; href:string}
export interface WorkMetadata {
 id:string; book:number; number:number; bwv:string; key:string;
 title:string; subtitle:string; description:string;
 downloads:WorkLink[]; analyses:WorkLink[];
 publicFiles:string[]; legacyPages?:string[]; legacyArchive?:string;
}
// All times are measured in crotchets, independently of the notated beat.
export interface Bar {number:number; start:number; duration:number; beatQuarters:number}
export interface ScoreEvent extends SoundNote {bar:number}
export interface ScoreSystem {start:number; end:number; svg:string}
export interface Material {id:string; label:string; colour:string; role:'subject'|'countersubject'|'cell'}
export interface Annotation {
 id:string; kind:string; voice:number; start:number; end:number;
 label:string; name:string; inverted:boolean; status:string;
}
export interface TonalEvent {id:string; bar:number; q:number; key:string; short:string; type:string; evidence:string}
export interface FugueData {
 metadata:WorkMetadata;
 voices:{name:string; short:string}[];
 bars:Bar[];
 tempo:{initial:number; min:number; max:number; beatQuarters:number; label:string};
 initialLoop:[number,number]; initialTone?:string; seekStep:number;
 score:{events:ScoreEvent[]; audio:SoundNote[]; duration:number};
 systems:ScoreSystem[];
 materials:Material[]; annotations:Annotation[];
 themes:{id:string; title:string; location:string; text:string}[];
 examples:{id:string; start:number; svg:string}[];
 formalGroups:{start:number; end:number; number:string; label:string; range:string; continuation:string}[];
 sections:{start:number; end:number; label:string; entries:string; detail:string}[];
 tonalEvents:TonalEvent[];
 notes:{examples:string; formal:string; formalSource?:WorkLink; map:string; disposition:string; notation:string; cells:string; edition:string[]; scoreSource:WorkLink};
}
