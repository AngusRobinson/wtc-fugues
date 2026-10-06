export const voices=['Soprano','Alto','Bass'];
export const themes=[
 {id:'subject',title:'Subject / tonal answer',location:'Bass, bars 1–2',text:'Following Keller, the subject ends on its eighth note, C♯. Its detached four-note head supplies most later entries. The first answer is tonal: its opening three notes transpose up a fifth, the remaining five up a fourth. There is no regular countersubject.'},
 {id:'motif',title:'Scale figure',location:'Bass, bar 8',text:'An ascending semiquaver scale ends with a demisemiquaver turn. It passes successively through the voices and recurs in inversion, often with an altered opening.'},
];
export const formalGroups=[
 {start:1,end:14,startQ:0,endQ:54.5,number:'I',label:'Exposition and successive stretti',range:'1–14',continuation:'Short cadential divisions'},
 {start:14,end:35,startQ:54.5,endQ:140,number:'II',label:'Further stretti and augmentation',range:'14–35',continuation:'Minor-key entries; dominant and tonic pedals'},
];
export const sections=[
 {start:1,end:4,label:'Exposition',entries:'Bass, bar 1 beat 1½ · soprano, beat 3½ · alto inversion, bar 2 beat 1½',detail:'The three complete statements overlap at two-crotchet intervals. The inverted head returns in the bass in bar 3, and the group closes on C♯ in bar 4.'},
 {start:4,end:7,label:'Counter-exposition and diminution',entries:'Soprano, bar 4 beat 1½ · alto, beat 3½ · bass, bar 5 beat 1½',detail:'Only the soprano repeats all eight notes. The answer head follows in the alto, then an adjusted form in the bass. Diminished heads enter successively in the soprano and alto in bar 5 and, inverted, in the bass in bar 6. A cadence in G♯ closes the passage.'},
 {start:7,end:9,label:'Answer heads and scale figure',entries:'Bass, bar 7 beat 1½ · alto, beat 3½ · soprano, bar 8 beat 1½',detail:'The scale figure (d) replaces the expected descending subject tail, first in the bass, then the alto and soprano at two-crotchet intervals. The passage reaches D♯ minor in bar 9.'},
 {start:9,end:12,label:'Two stretto chains',entries:'Inverted heads: bass–alto–soprano, bars 9–10; bass–soprano, bars 10–11, followed by direct alto and bass heads',detail:'The first chain enters at crotchet intervals, as does the second. Inverted heads (hi) alternate with direct heads (h); the scale figure also appears in inversion (di). The second chain crosses the C♯ arrival in bar 11.'},
 {start:12,end:14,label:'Sequential episode',entries:'Bass sequence, bars 12–13',detail:'A sequential bass figure (e) supports suspensions in the upper parts. The sequence reaches A♯ minor in bar 13, then a half-close on E♯ in bar 14.'},
 {start:14,end:19,label:'Renewed stretto and diminution',entries:'Bass, bar 14 beat 3½ · soprano head, beat 4½ · alto, bar 15 beat 1½ · soprano inversion, beat 3½',detail:'Complete eight-note forms return in the bass and alto; the soprano’s complete inversion is tonally adjusted. An isolated bass head in bar 17 precedes diminished inverted heads in alto and bass across bars 18–19, an altered alto head, and a direct bass head.'},
 {start:20,end:24,label:'Second episode',entries:'Soprano sequence, bars 20–21 · bass answer head, bar 24 beat 1½',detail:'The upper line transforms the earlier bass sequence, with diminished motion and demisemiquaver turns. A descending paired-note sequence (f) passes through the alto in bar 21. Further suspensions and scale figures lead to the bass’s return of the answer head.'},
 {start:25,end:28,label:'Augmented heads',entries:'Soprano inversion, bar 25 beat 1½ · alto augmentation, beat 2 · bass head, beat 3½; bass augmentation, bar 27 beat 2',detail:'The first augmented head adjusts its last pitch to F♯ and shortens that note. The second reaches G♯ in bar 28, sustaining it as a dominant pedal. The accompanying scale figure moves between the parts in direct and inverted forms.'},
 {start:28,end:32,label:'Dominant pedal and final stretti',entries:'Soprano, bar 28 · alto, bars 30–31 · bass, bar 31 beat 3½',detail:'C♯ minor colours the dominant pedal. The soprano decorates an inverted head with an intervening semiquaver, then gives a direct head. Two successive inverted heads in the alto lead to a final bass head and a dominant prolongation.'},
 {start:33,end:35,label:'Tonic pedal and close',entries:'Diminished soprano heads, bars 33–34',detail:'The tonic pedal begins at bar 33 beat 3 beneath a suspended fourth. Additional parts fill out the closing texture. The final soprano E♯ completes the tonic major triad.'},
];
export const tonalEvents=[
 {id:'c4',bar:4,q:12,key:'C♯ major',short:'C♯',roman:'I',type:'cadence',evidence:'C♯ in the bass and E♯ in the alto resolve the preceding G♯ dominant.'},
 {id:'g7',bar:7,q:24,key:'G♯ major',short:'G♯',roman:'V',type:'cadence',evidence:'G♯ in the soprano and B♯ in the alto complete the preceding cadential motion.'},
 {id:'d9',bar:9,q:32,key:'D♯ minor',short:'D♯m',roman:'ii',type:'arrival',evidence:'D♯ in the bass sounds beneath two F♯s at the close of the ascending sequence.'},
 {id:'c11',bar:11,q:40,key:'C♯ major',short:'C♯',roman:'I',type:'arrival',evidence:'The voices form C♯–E♯–G♯, with the third in the bass, within the stretto chain.'},
 {id:'a13',bar:13,q:51,key:'A♯ minor',short:'A♯m',roman:'vi',type:'cadence',evidence:'A♯ in the bass supports C♯ and E♯ after E♯–G double sharp.'},
 {id:'e14',bar:14,q:54,key:'E♯ major',short:'E♯',roman:'III',type:'cadence',evidence:'The upper E♯ and G double sharp stand over bass E♯: a half-close in A♯ minor.'},
 {id:'g16',bar:16,q:60,key:'G♯ major',short:'G♯',roman:'V',type:'arrival',evidence:'G♯ in the bass supports B♯ and D♯ as the upper entries continue.'},
 {id:'c17',bar:17,q:64,key:'C♯ major',short:'C♯',roman:'I',type:'arrival',evidence:'E♯ in the soprano and C♯ in the alto precede the bass’s tonic head.'},
 {id:'c21',bar:21,q:83,key:'C♯ major',short:'C♯',roman:'I',type:'cadence',evidence:'The descending sequence reaches C♯ in the bass with E♯ above.'},
 {id:'c23',bar:23,q:88,key:'C♯ major',short:'C♯',roman:'I',type:'arrival',evidence:'C♯ bass and E♯ soprano resolve the preceding G♯–B♯ dominant.'},
 {id:'f23',bar:23,q:90,key:'F♯ major',short:'F♯',roman:'IV',type:'arrival',evidence:'F♯ in the bass supports soprano A♯; the alto’s E♯ suspension follows.'},
 {id:'g25',bar:25,q:96,key:'G♯ major',short:'G♯',roman:'V',type:'cadence',evidence:'B♯ and G♯ close the preceding phrase before the inverted head and augmentation.'},
 {id:'ped28',bar:28,q:108,key:'G♯ dominant pedal',short:'G♯',roman:'V',type:'arrival',evidence:'The augmented bass head reaches its sustained G♯ under B♯ and F♯.'},
 {id:'ped33',bar:33,q:130,key:'C♯ tonic pedal',short:'C♯',roman:'I',type:'arrival',evidence:'Octave Cs sharp begin the tonic pedal; the suspended F♯ resolves to E♯ a crotchet later.'},
 {id:'close',bar:35,q:138,key:'C♯ major',short:'C♯',roman:'I',type:'close',evidence:'The final chord contains C♯, E♯ and G♯ over the sustained tonic pedal.'},
];
