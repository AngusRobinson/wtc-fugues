export const voices=['Soprano','Alto','Tenor','Bass'];
export const themes=[
 {id:'subject',title:'Subject / tonal answer',location:'Tenor, bars 1–2',text:'Triadic quavers outline tonic, subdominant and tonic harmony, ending on the dominant note. The answer is tonal: its second note is A♭ rather than the B♭ of a real transposition. Later versions alter the central leap and the ending.'},
 {id:'cs1',title:'Countersubject',location:'Tenor, bars 2–3',text:'Eight semiquavers are followed by their diatonic inversion. This accompanying phrase is not retained as a complete, regular countersubject throughout: its figures and the following suspension become the principal episodic material. Tovey calls it a countersubject; Prout reserves that term for a more regularly recurring phrase.'},
];
export const formalGroups=[
 {start:1,end:9,startQ:0,endQ:36,number:'I',label:'Exposition and episode',range:'1–9',continuation:'T · B · S · A'},
 {start:10,end:26,startQ:36,endQ:104,number:'II',label:'Three pairs of entries',range:'10–26',continuation:'T / A · T / A · A / S'},
 {start:27,end:35,startQ:104,endQ:140,number:'III',label:'Complete entry group and coda',range:'27–35',continuation:'B · T · A · S; final S'},
];
export const sections=[
 {start:1,end:7,label:'Exposition',entries:'Tenor, bar 1 · bass, bar 2 · soprano, bar 5 · alto, bar 6',detail:'Each entry begins on beat 2. The two-bar codetta before the soprano entry introduces the suspension figure (p) and derived quaver figure (a), alongside the countersubject’s semiquaver figure (e). These components subsequently combine in the episodes.'},
 {start:7,end:10,label:'First episode',entries:'Semiquaver figures and suspensions',detail:'The soprano, alto and bass develop material from the initial accompaniment. The episode closes in A♭ major, preparing the tenor’s return.'},
 {start:10,end:13,label:'First pair: tenor and alto',entries:'Tenor, bar 10 · alto, bar 13',detail:'Between the A♭ major and F minor entries, a three-part sequence combines soprano semiquavers, tenor suspensions and derived quavers in the bass. This combination supplies two later inversions in triple counterpoint.'},
 {start:14,end:17,label:'First inversion of the episode',entries:'Semiquavers in bass · suspensions in soprano · quavers in alto',detail:'The three components return with their registers inverted. The relationship of the semiquaver and quaver lines changes at the twelfth; the suspension line moves above them. A further passage leads from F minor towards B♭ minor.'},
 {start:17,end:18,label:'Second pair',entries:'Tenor, bar 17 · alto, bar 18',detail:'The tenor gives the subject in B♭ minor. The alto’s answer-form changes the middle of the phrase and ends on B♭ rather than the expected supertonic.'},
 {start:19,end:22,label:'Second inversion and incomplete heads',entries:'Semiquavers in alto · suspensions in tenor · quavers in soprano',detail:'The three-part episode returns with inversion at the octave and a small ornament in the quaver line. In bar 21, incomplete answer heads (h) overlap at half-bar distance; these allusions are distinguished from full entries. The passage closes in E♭ major.'},
 {start:23,end:24,label:'Third pair',entries:'Alto, bar 23 · soprano, bar 24',detail:'Both entries replace the subject’s ascending sixth with a minor seventh. The tenor supplies a continuous semiquaver line while the bass remains silent.'},
 {start:25,end:27,label:'Episode',entries:'Sequential semiquavers in the tenor',detail:'The upper voices add derived quaver and suspension figures. The tenor descends to A♭ just as the returning bass begins the final complete entry group.'},
 {start:27,end:31,label:'Final complete group',entries:'Bass, bar 27 · tenor, bar 28 · alto, bar 29 · soprano, bar 30',detail:'All four voices enter successively on beat 2. The bass is in A♭; the altered tenor entry closes in C minor, the alto ends on A♭, and the soprano leads to D♭ major. The accompanying lines develop the episodic material rather than repeat a fixed countersubject.'},
 {start:31,end:35,label:'Coda and final subject',entries:'Soprano, bar 33 beat 4',detail:'Rising chordal sequences extend the climax before the parts descend. The soprano’s final subject returns in A♭ over chordal punctuations and a continuing bass line; the last cadence follows in bar 35.'},
];
export const tonalEvents=[
 {id:'ab5',bar:5,q:17,key:'A♭ major',short:'A♭',roman:'I',type:'arrival',evidence:'The bass and soprano reach A♭ over C in the tenor.'},
 {id:'eb7',bar:7,q:25,key:'E♭ major',short:'E♭',roman:'V',type:'cadence',evidence:'The bass reaches E♭ beneath G and B♭ in the upper voices.'},
 {id:'ab10',bar:10,q:36,key:'A♭ major',short:'A♭',roman:'I',type:'cadence',evidence:'The soprano and alto resolve to A♭ above C in the bass.'},
 {id:'fm14',bar:14,q:52,key:'F minor',short:'Fm',roman:'vi',type:'cadence',evidence:'The alto’s subject ends on C above F in the bass and A♭ in the tenor.'},
 {id:'fm16',bar:16,q:60,key:'F minor',short:'Fm',roman:'vi',type:'cadence',evidence:'The bass C–F and soprano E–F resolve beneath A♭ in the alto.'},
 {id:'bm18',bar:18,q:69,key:'B♭ minor',short:'B♭m',roman:'ii',type:'arrival',evidence:'The soprano A natural resolves to B♭ above D♭ in the bass, with B♭ and F in the inner parts.'},
 {id:'bm19',bar:19,q:72.5,key:'B♭ minor',short:'B♭m',roman:'ii',type:'cadence',evidence:'The bass F–B♭ supports the closing answer; the soprano reaches D♭ after its E♭ suspension and passing C.'},
 {id:'eb23',bar:23,q:88,key:'E♭ major',short:'E♭',roman:'V',type:'cadence',evidence:'The tenor B♭–E♭ and soprano D–E♭ close with G in the alto.'},
 {id:'ab27',bar:27,q:105,key:'A♭ major',short:'A♭',roman:'I',type:'arrival',evidence:'Tenor and returning bass meet on A♭ with C in the alto.'},
 {id:'cm29',bar:29,q:112,key:'C minor',short:'Cm',roman:'iii',type:'cadence',evidence:'The tenor’s B natural rises to C over C in the bass and G in the alto; the soprano retains F before resolving to E♭.'},
 {id:'db31',bar:31,q:120.5,key:'D♭ major',short:'D♭',roman:'IV',type:'cadence',evidence:'The alto’s E♭ resolves to D♭ above D♭ in the bass, F in the soprano and A♭ in the tenor.'},
 {id:'fm32',bar:32,q:124,key:'F minor',short:'Fm',roman:'vi',type:'arrival',evidence:'The rising sequence reaches F in the bass with A♭ and C above.'},
 {id:'ab32',bar:32,q:127,key:'A♭ major',short:'A♭',roman:'I',type:'arrival',evidence:'The descending bass reaches A♭ with C in the upper parts and A♭ in the tenor.'},
 {id:'ab35',bar:35,q:138,key:'A♭ major',short:'A♭',roman:'I',type:'close',evidence:'The final E♭ dominant resolves to A♭, C and E♭.'},
];
