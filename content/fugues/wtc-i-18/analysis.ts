export const voices=['Soprano','Alto','Tenor','Bass'];
export const themes=[
 {id:'subject',title:'Subject / tonal answer',location:'Tenor, bars 1–3',text:'A neighbour-note figure surrounds G♯ before the ascending tritone G♯–C double sharp leads to D♯. Repeated quavers complete the modulation to D♯ minor. The tonal answer changes its transposition after the first note, passing through C♯ minor and returning to G♯ minor while preserving the tritone.'},
 {id:'cs1',title:'Main countersubject',location:'Tenor, bars 3–5',text:'The tied opening note gives way to an ascending line of quavers and semiquavers. Rests articulate the cadence. Its later forms sometimes change the opening; its continuation generates the upper line of the first type of episode.'},
 {id:'cs2',title:'Second countersubject',location:'Tenor, bars 5–7',text:'A broad rising-and-falling line extends across the cadence as a suspension. Keller relates it to an augmentation of the subject’s opening figure. Its descending continuation forms a recurring sequence of suspensions.'},
];
export const formalGroups=[
 {start:1,end:14,startQ:0,endQ:56,number:'I',label:'Exposition and additional answer',range:'1–14',continuation:'T · A · S · B; T'},
 {start:15,end:20,startQ:56,endQ:80,number:'II',label:'Three-entry group',range:'15–20',continuation:'B · T · A'},
 {start:21,end:31,startQ:80,endQ:124,number:'III',label:'Tritone episodes and two entries',range:'21–31',continuation:'S · B'},
 {start:32,end:41,startQ:124,endQ:164,number:'IV',label:'Isolated closing entries',range:'32–41',continuation:'T; S'},
];
export const sections=[
 {start:1,end:9,label:'Exposition',entries:'Tenor, bar 1 · alto, bar 3 · soprano, bar 5 · bass, bar 7',detail:'The four entries begin on beat 2 at regular two-bar intervals. The main countersubject passes from tenor to alto and soprano. The tenor adds the second countersubject to the third entry, prolonging the close in D♯ minor.'},
 {start:9,end:11,label:'First episodic type',entries:'Repeated quavers in bass; detached chords in the middle voices',detail:'The subject’s repeated-quaver figure (r) combines with the main-countersubject figure (e). The inner voices punctuate the sequence with chords. The passage passes through B major and returns to D♯ minor.'},
 {start:11,end:13,label:'Additional answer',entries:'Tenor, bar 11 beat 2',detail:'The soprano gives the main countersubject and the alto the second. Their sustained notes overlap the following cadence in G♯ minor.'},
 {start:13,end:15,label:'Episode',entries:'Main-countersubject figure above repeated quavers',detail:'A descending suspension sequence (p), derived from the second countersubject, occupies the alto. The repeated quavers move into the tenor as the harmony turns to C♯ minor.'},
 {start:15,end:17,label:'Bass entry',entries:'Bass, bar 15 beat 2',detail:'A direct transposition begins on C♯ and closes on G♯. The alto adapts the main countersubject’s opening; the soprano supplies the second countersubject.'},
 {start:17,end:21,label:'Tenor and alto entries',entries:'Tenor, bar 17 · alto, bar 19',detail:'The tenor subject is followed by the alto’s tonal answer. The latter combines with the main countersubject in the tenor and the second in the bass: bars 11–12 are redistributed in triple counterpoint at the octave, with changed cadential durations.'},
 {start:21,end:24,label:'Second episodic type',entries:'Tritone figure (t) in bass and alto',detail:'The figure leading through the subject’s tritone is expanded into a sequential exchange. Keller derives this episode from the subject; its suspensions also connect it with the second countersubject. The sequence prepares A♯ minor.'},
 {start:24,end:28,label:'Two-entry group',entries:'Soprano, bar 24 · bass, bar 26',detail:'The soprano subject moves from D♯ towards A♯ minor. The bass then gives an answer-form associated with B major. The regular countersubjects are absent; freer lines obscure the otherwise frequent cadential divisions.'},
 {start:28,end:32,label:'Composite episode',entries:'Tritone figure, then the first episodic combination',detail:'The tritone sequence returns in the upper voices. From bar 30, the main-countersubject figure, descending suspensions and repeated quavers resume, leading back to G♯ minor.'},
 {start:32,end:34,label:'Isolated tenor entry',entries:'Tenor, bar 32 beat 2',detail:'B♯ replaces the subject’s B natural. The alto gives an altered main countersubject and the soprano the second. Keller notes the resulting cross-relation with B natural in the soprano.'},
 {start:34,end:37,label:'Episode',entries:'Suspension sequence and repeated quavers',detail:'The thematic components move through E major towards C♯ minor. The passage prepares a final real transposition rather than the exposition’s tonal answer.'},
 {start:37,end:41,label:'Final entry and close',entries:'Soprano, bar 37 beat 2½',detail:'The initial crotchet is shortened to a quaver. The subject moves from C♯ towards G♯ minor; only a fragment of the main countersubject remains in the alto. The subsequent cadential extension closes with a minor tonic chord.'},
];
export const tonalEvents=[
 {id:'ds3',bar:3,q:8,key:'D♯ minor',short:'D♯m',roman:'v',type:'arrival',evidence:'The unaccompanied subject ends on D♯ after C double sharp has established its leading note.'},
 {id:'gs5',bar:5,q:16,key:'G♯ minor',short:'G♯m',roman:'i',type:'cadence',evidence:'The answer and main countersubject converge on G♯.'},
 {id:'ds7',bar:7,q:24,key:'D♯ minor',short:'D♯m',roman:'v',type:'cadence',evidence:'The soprano and alto close on D♯ while the second countersubject retains G♯ as a suspension.'},
 {id:'gs9',bar:9,q:32,key:'G♯ minor',short:'G♯m',roman:'i',type:'cadence',evidence:'The bass reaches G♯ beneath B, D♯ and G♯.'},
 {id:'b10',bar:10,q:36,key:'B major',short:'B',roman:'III',type:'cadence',evidence:'The repeated bass quavers resolve to B with D♯ and F♯ in the middle voices.'},
 {id:'ds11',bar:11,q:40,key:'D♯ minor',short:'D♯m',roman:'v',type:'cadence',evidence:'The bass A♯–D♯ closes beneath D♯ and F♯.'},
 {id:'gs13',bar:13,q:48,key:'G♯ minor',short:'G♯m',roman:'i',type:'cadence',evidence:'The tenor and soprano reach G♯ while C♯ is retained in the alto before resolving to B.'},
 {id:'cs15',bar:15,q:56,key:'C♯ minor',short:'C♯m',roman:'iv',type:'cadence',evidence:'The tenor and soprano reach C♯; the alto’s F♯ suspension resolves through E.'},
 {id:'gs17',bar:17,q:64,key:'G♯ minor',short:'G♯m',roman:'i',type:'cadence',evidence:'The bass and alto reach G♯ with D♯ in the tenor; the soprano retains C♯ across the cadence before continuing its line.'},
 {id:'ds19',bar:19,q:72,key:'D♯ minor',short:'D♯m',roman:'v',type:'cadence',evidence:'D♯ in tenor and bass supports F♯ in the soprano; the alto retains E♯ before resolving to D♯.'},
 {id:'as24',bar:24,q:93,key:'A♯ minor',short:'A♯m',roman:'ii',type:'entry',evidence:'The soprano entry starts on D♯ and moves towards A♯ minor through G double sharp. This identifies the subject’s modulation, not a tonic arrival on its opening note.'},
 {id:'b28',bar:28,q:108,key:'B major',short:'B',roman:'III',type:'cadence',evidence:'The bass and tenor close on B; E in the alto and C♯ in the soprano delay the upper-part resolution.'},
 {id:'ds30',bar:30,q:116,key:'D♯ minor',short:'D♯m',roman:'v',type:'cadence',evidence:'The soprano and bass reach D♯ while the alto retains G♯, subsequently resolving to F♯.'},
 {id:'gs32',bar:32,q:125,key:'G♯ minor',short:'G♯m',roman:'i',type:'arrival',evidence:'The tenor enters on G♯ above B in the bass and D♯ in the alto.'},
 {id:'ds34',bar:34,q:133,key:'D♯ minor',short:'D♯m',roman:'v',type:'cadence',evidence:'The soprano suspension resolves to F♯ with A♯ in the alto and D♯ in the bass.'},
 {id:'e36',bar:36,q:141.5,key:'E major',short:'E',roman:'VI',type:'arrival',evidence:'The upper voices reach G♯ above E in the bass and B in the tenor.'},
 {id:'cs37',bar:37,q:144,key:'C♯ minor',short:'C♯m',roman:'iv',type:'arrival',evidence:'C♯ in bass and soprano supports G♯ in the tenor while the alto continues its moving figure.'},
 {id:'gs41',bar:41,q:160,key:'G♯ minor',short:'G♯m',roman:'i',type:'close',evidence:'The final dominant resolves to G♯, B natural and D♯.'},
];
