export const voices=['Soprano','Alto','Bass'];
export const themes=[
 {id:'subject',title:'Subject / tonal answer',location:'Soprano, bars 1–3',text:'An isolated quaver and three rests precede the rising fourths. Keller includes the continuation towards E major; at the first entry, G♯ replaces the expected final E. The tonal answer alters the first rising fourth, G♯–C♯ becoming C♯–F♯; Keller reads this as a turn back towards A. Cadential endings vary.'},
 {id:'cs1',title:'Semiquaver countersubject',location:'Alto, bars 23–25',text:'There is no regular countersubject in the opening section. This new line combines descending sequences with an ascending scale. Its most substantial return is in the bass, bars 27–28; elsewhere, freely adapted semiquaver figures represent it. Tovey treats it as a second subject.'},
];
export const formalGroups=[
 {start:1,end:20,startQ:0,endQ:90,number:'A',label:'Quaver section',range:'1–20',continuation:'Exposition; second group'},
 {start:21,end:41,startQ:90,endQ:184.5,number:'B',label:'Semiquaver section',range:'21–41',continuation:'Transition; new countersubject'},
 {start:42,end:48,startQ:184.5,endQ:216,number:'a',label:'Return of quaver texture',range:'42–48',continuation:'Alto and bass entries'},
 {start:49,end:54,startQ:216,endQ:241.5,number:'b',label:'Return of semiquaver texture',range:'49–54',continuation:'Cadential reprise'},
];
export const sections=[
 {start:1,end:8,label:'Exposition',entries:'Soprano, bar 1 · alto, bar 2 · bass, bars 4 and 6',detail:'The tonal answer overlaps the subject at one bar’s distance. The bass enters first in the tenor register, then an octave lower with the answer. The rising-fourth figure (q) is continually imitated, taking the place of a regular countersubject.'},
 {start:9,end:15,label:'Second entry group',entries:'Soprano, bar 9 · bass, bar 13',detail:'The soprano repeats the opening subject, now reaching E directly. The bass enters in F♯ minor with its initial note displaced down an octave. The sequential continuation turns towards B minor.'},
 {start:16,end:20,label:'Dominant close',entries:'Bass, bar 16; incomplete and altered',detail:'The rising fourths move from B minor into E major. A recurring cadential phrase (c), beginning in bar 17, gives the first large section its clear close on the downbeat of bar 20.'},
 {start:21,end:28,label:'Semiquaver countersubject and stretto',entries:'Bass, bar 23 · divided upper entries, bar 25 · alto, bar 27',detail:'The semiquaver countersubject enters in the alto at bar 23. In bar 25, the tonal answer begins in the soprano but continues in the alto; the displaced upper variant takes its opening note from the alto before continuing in the soprano. Keller hears a three-voice stretto. The alto’s bar 27 entry uses a real transposition with octave displacement of its opening note.'},
 {start:29,end:32,label:'Expanded intervals',entries:'Bass, bar 29 · soprano, bar 30 · divided entry, bar 31',detail:'The rising fourths expand into sixths against semiquaver figures (s). The high D at the start of bar 31 also begins an altered subject passed to the alto. The bass’s semiquavers continue beneath it.'},
 {start:33,end:41,label:'Minor-key continuation',entries:'Bass, bars 33 and 39',detail:'The D-major entry turns to B minor. A longer semiquaver passage then moves towards F♯ minor; the bass’s bar 39 statement omits the isolated initial note and rests. The close in F♯ minor coincides with the start of the return.'},
 {start:42,end:48,label:'First part of the coda',entries:'Alto, bar 42 · bass, bar 44',detail:'Quavers resume. The alto changes the isolated opening note to F♯ before continuing the subject in A; the bass supplies an altered answer. Bars 46–49 recast the earlier cadential phrase in the tonic.'},
 {start:49,end:54,label:'Second part of the coda',entries:'No further complete subject',detail:'Bars 49–50 recall the expanded-interval passage of bars 29–30. The cadential phrase returns once more from bar 51, with the upper parts inverted relative to its previous appearances and semiquavers added in the bass.'},
];
export const tonalEvents=[
 {id:'e4',bar:4,q:15,key:'E major',short:'E',roman:'V',type:'arrival',evidence:'E and G♯ settle the upper voices before the bass’s subject continuation.'},
 {id:'a9',bar:9,q:36,key:'A major',short:'A',roman:'I',type:'cadence',evidence:'E in the bass resolves to A; the alto’s D suspension resolves to C♯.'},
 {id:'fs13',bar:13,q:54,key:'F♯ minor',short:'F♯m',roman:'vi',type:'cadence',evidence:'The bass C♯ resolves to F♯ under A; G♯ in the alto delays its resolution to F♯.'},
 {id:'b16',bar:16,q:67.5,key:'B minor',short:'Bm',roman:'ii',type:'cadence',evidence:'F♯ resolves to B in the bass, with D in the alto.'},
 {id:'e17',bar:17,q:73,key:'E major',short:'E',roman:'V',type:'arrival',evidence:'E in the bass supports G♯ and B as the cadential phrase begins.'},
 {id:'e20',bar:20,q:85.5,key:'E major',short:'E',roman:'V',type:'cadence',evidence:'B in the bass resolves to E as all three voices converge on the dominant tonic.'},
 {id:'a23',bar:23,q:99,key:'A major',short:'A',roman:'I',type:'cadence',evidence:'The upper leading note resolves to A above C♯ in the alto and the bass’s A entry.'},
 {id:'e25',bar:25,q:108,key:'E major',short:'E',roman:'V',type:'arrival',evidence:'The bass reaches E below G♯ and the isolated E of the upper answer.'},
 {id:'d31',bar:31,q:135,key:'D major',short:'D',roman:'IV',type:'arrival',evidence:'The rising line reaches D over F♯ in the bass.'},
 {id:'d33',bar:33,q:144,key:'D major',short:'D',roman:'IV',type:'cadence',evidence:'The bass enters on D beneath D and F♯ after the preceding dominant harmony.'},
 {id:'b36',bar:36,q:157.5,key:'B minor',short:'Bm',roman:'ii',type:'cadence',evidence:'F♯ in the bass resolves to B; the soprano’s A♯–B confirms the cadence.'},
 {id:'fs42',bar:42,q:184.5,key:'F♯ minor',short:'F♯m',roman:'vi',type:'cadence',evidence:'C♯ in the bass and E♯ in the alto resolve to F♯ in all voices.'},
 {id:'a49',bar:49,q:216,key:'A major',short:'A',roman:'I',type:'cadence',evidence:'The returning cadential phrase closes with all voices on A.'},
 {id:'a54',bar:54,q:238.5,key:'A major',short:'A',roman:'I',type:'close',evidence:'E in the bass and G♯ in the soprano resolve to A, with C♯ in the alto.'},
];
