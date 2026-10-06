export const voices=['Soprano','Alto','Tenor','Bass'];
export const themes=[
 {id:'subject',title:'Subject / real answer',location:'Tenor, bars 1–2',text:'Three repeated quavers lead to a sustained leap and a four-note tail. The first answer is real: every pitch transposes up a fifth, with the sustained fifth note shortened before a quaver rest. There is no regular countersubject.'},
 {id:'motif',title:'Subject-tail figure',location:'Tenor, bar 3',text:'The four-note tail (b) supplies the accompanying imitation and the episodes. Its rising fourth and descending steps recur across the bar, often joined into longer sequences.'},
];
export const formalGroups=[
 {start:1,end:27,startQ:0,endQ:106.5,number:'I',label:'Exposition and first stretti',range:'1–27',continuation:'Cadence in F♯ minor'},
 {start:27,end:50,startQ:106.5,endQ:200,number:'II',label:'Closer stretti and return',range:'27–50',continuation:'Octaves · rising sixths · descending thirds'},
];
export const sections=[
 {start:1,end:10,label:'Exposition and appendix',entries:'Tenor, bar 1 · alto, bar 2 beat 3½ · soprano, bar 5 · bass, bar 6',detail:'The entries begin on the second quaver except the alto’s later start. A one-bar link follows the answer; the soprano and bass then overlap at one bar’s distance. The imitative continuation in bars 7–10 remains part of Keller’s opening division.'},
 {start:10,end:13,label:'Minor-key entries',entries:'Alto, bar 10 beat 1½ · soprano, bar 11 beat 3½',detail:'The subject appears in E minor and B minor. Its four-note tail (b) continues independently in the other parts, connecting entries with the surrounding sequential writing.'},
 {start:14,end:16,label:'Two-voice stretto',entries:'Alto, bar 14 beat 1½ · soprano, beat 3½',detail:'The answer and subject overlap at two crotchets’ distance. Their D major cadence in bar 16 gives way immediately to a new episode.'},
 {start:16,end:21,label:'Episode',entries:'Imitation of the tail in all four voices',detail:'The tail is linked into ascending and descending sequences. The bass’s long notes and later quaver motion support suspensions in the upper voices; the passage returns to A major before the next entry group.'},
 {start:21,end:27,label:'Three-voice stretto and closing answer',entries:'Tenor, bar 21 beat 1½ · soprano, bar 22 beat 1½ · alto, beat 3½ · bass, bar 25 beat 1½',detail:'The entry distances contract from four crotchets to two. The tenor and soprano endings are adjusted chromatically. A separate bass answer completes the group, leading to the F♯ minor cadence at bar 27 beat 3.'},
 {start:27,end:29,label:'Stretto in octaves',entries:'Bass, bar 27 beat 3½ · soprano, beat 4½ · alto, bar 28 beat 1½',detail:'The three voices enter a crotchet apart on A in successive registers. The alto breaks off after the first falling leap; the bass and soprano continue the complete subject.'},
 {start:29,end:33,label:'Episode',entries:'Tail sequences; approach to G major',detail:'The imitative texture recalls the exposition’s appendix, now extended through the subdominant. A G major arrival in bar 33 precedes the next stretto.'},
 {start:33,end:35,label:'Stretto in ascending sixths',entries:'Tenor, bar 33 beat 1½ · alto, beat 2½ · soprano, beat 3½',detail:'D–B–G begins a chain of entries a crotchet apart in rising sixths. Each voice completes the subject; C natural in the soprano’s tail accommodates the local harmony.'},
 {start:35,end:40,label:'Episode and return to D',entries:'Upper-part imitation over the descending bass scale, bars 38–40',detail:'The tenor rests while the other voices spread apart. The bass descends from D4 to D2 in continuous quavers, reaching the tonic on bar 40’s downbeat.'},
 {start:40,end:44,label:'Tonic entry and chromatic answer',entries:'Tenor, bar 40 beat 1½ · bass, bar 43 beat 1½ · tenor head, bar 44 beat 1½',detail:'The isolated tonic subject interrupts the continuous tail imitation. The bass’s next answer includes D♯–E–F natural; the incomplete tenor head prepares the final four-voice stretto.'},
 {start:44,end:47,label:'Four-voice stretto in descending thirds',entries:'Soprano, bar 44 beat 3½ · alto, beat 4½ · tenor, bar 45 beat 1½ · bass, beat 2½',detail:'A–F♯–D–B follows at crotchet intervals from the top voice downwards. All four parts complete the subject. The first three notes remain distinct as the sustained notes and tails cross.'},
 {start:47,end:50,label:'Coda',entries:'Four-note tail in all voices',detail:'The coda resumes the episodic texture, moving through G major and D major before the final cadence. The final chord arrives at bar 50 beat 3.'},
];
export const tonalEvents=[
 {id:'a4',bar:4,q:12,key:'A major',short:'A',roman:'V',type:'arrival',evidence:'Tenor A and alto C♯ follow the G♯ leading note at the end of the answer.'},
 {id:'a7',bar:7,q:26,key:'A major',short:'A',roman:'V',type:'arrival',evidence:'The soprano’s G♯ resolves to A above C♯ in the bass and E in the alto.'},
 {id:'d8',bar:8,q:29,key:'D major',short:'D',roman:'I',type:'arrival',evidence:'The sequential continuation reaches D in the bass and tenor with F♯ in the soprano.'},
 {id:'a10',bar:10,q:36,key:'A major',short:'A',roman:'V',type:'cadence',evidence:'Bass A supports C♯ and E at the end of the opening appendix.'},
 {id:'e11',bar:11,q:42,key:'E minor',short:'Em',roman:'ii',type:'arrival',evidence:'E and G above the held B bass mark the end of the alto’s minor-key subject.'},
 {id:'b13',bar:13,q:48,key:'B minor',short:'Bm',roman:'vi',type:'cadence',evidence:'Bass B resolves A♯ and supports the complete B–D–F♯ triad.'},
 {id:'a14',bar:14,q:52,key:'A major',short:'A',roman:'V',type:'arrival',evidence:'A in the bass sounds beneath C♯ and E before the two-voice stretto.'},
 {id:'d16',bar:16,q:60,key:'D major',short:'D',roman:'I',type:'cadence',evidence:'Octave Ds in the bass and tenor support F♯ in the soprano.'},
 {id:'a20',bar:20,q:78.5,key:'A major',short:'A',roman:'V',type:'arrival',evidence:'The alto’s D suspension resolves to C♯ above bass A, tenor E and soprano A.'},
 {id:'fs25',bar:25,q:96.5,key:'F♯ minor',short:'F♯m',roman:'iii',type:'arrival',evidence:'The bass’s F♯ completes the F♯–A–C♯ sonority as its answer begins.'},
 {id:'fs27',bar:27,q:106,key:'F♯ minor',short:'F♯m',roman:'iii',type:'cadence',evidence:'The C♯ dominant resolves to F♯ with A in the alto; this closes Keller’s first part.'},
 {id:'a29',bar:29,q:113,key:'A major',short:'A',roman:'V',type:'cadence',evidence:'The octave stretto reaches A in the bass and alto with soprano C♯.'},
 {id:'g33',bar:33,q:128,key:'G major',short:'G',roman:'IV',type:'arrival',evidence:'The upper Gs and alto D sound above B in the bass, after the D dominant preparation.'},
 {id:'d40',bar:40,q:156,key:'D major',short:'D',roman:'I',type:'cadence',evidence:'The two-octave bass descent reaches D2 beneath D and F♯ in the upper parts.'},
 {id:'a44',bar:44,q:174,key:'A major',short:'A',roman:'V',type:'arrival',evidence:'The chromatic bass answer ends on C♯ beneath A and two Es.'},
 {id:'g47',bar:47,q:186,key:'G major',short:'G',roman:'IV',type:'arrival',evidence:'G in bass and tenor supports soprano B as the coda turns towards the subdominant.'},
 {id:'d48',bar:48,q:190,key:'D major',short:'D',roman:'I',type:'arrival',evidence:'D bass, F♯ tenor and A soprano form the tonic triad within the coda.'},
 {id:'close',bar:50,q:198,key:'D major',short:'D',roman:'I',type:'close',evidence:'D–F♯–A completes the final cadence on the second minim beat.'},
];
