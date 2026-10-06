export const voices=['Soprano','Alto','Bass'];
export const themes=[
 {id:'subject',title:'Subject / tonal answer',location:'Alto, bars 1–5',text:'The opening mordent figure gives way to continuous semiquavers. The answer is tonal: G–F–G–C becomes C–B–C–G, changing the opening whole tone to a semitone and the falling fifth to a fourth.'},
 {id:'tail',title:'Derived accompaniment',location:'Alto, bars 5–8',text:'There is no independent regular countersubject. The semiquaver accompaniment continues the subject’s closing figure and supplies much of the episodic material; its opening occasionally returns with the subject.'},
];
export const formalGroups=[
 {start:1,end:21,startQ:0,endQ:40.5,number:'I',label:'Exposition and episode',range:'1–21',continuation:'A · S · B; episode from 13'},
 {start:21,end:39,startQ:40.5,endQ:76.5,number:'II',label:'Second group and episode',range:'21–39',continuation:'A · S; episode from 29'},
 {start:39,end:68,startQ:76.5,endQ:134.5,number:'III',label:'Third group and episode',range:'39–68',continuation:'B · A · S; episode from 55'},
 {start:68,end:83,startQ:134.5,endQ:166,number:'IV',label:'Coda: partial entries',range:'68–83',continuation:'B · A · S'},
];
export const sections=[
 {start:1,end:13,label:'Exposition',entries:'Alto, bar 1 · soprano, bar 5 · bass, bar 9',detail:'Each entry begins on the second quaver. The semiquaver accompaniment (c) continues in the preceding voice, while the third voice completes the harmony. The exposition ends on the first semiquaver of bar 13.'},
 {start:13,end:21,label:'First episode',entries:'Subject head in soprano and alto',detail:'The subject head (h) passes between the upper voices at a bar’s distance over the semiquaver figure in the bass. The sequence prepares the alto’s next entry.'},
 {start:21,end:29,label:'Second group',entries:'Alto, bar 21 · soprano, bar 25',detail:'The alto’s subject leads to D minor; the soprano’s answer leads to A minor. The bass falls silent after the first quaver of bar 25, leaving the second entry and following episode in two parts.'},
 {start:29,end:39,label:'Second episode',entries:'Soprano and alto',detail:'The soprano first develops the head over the alto’s semiquavers. From bar 33 the semiquaver figure forms a canon at the fifth, broken off in the cadential approach to the bass entry.'},
 {start:39,end:55,label:'Third group',entries:'Bass, bar 39 · alto, bar 47 · soprano, bar 51',detail:'The bass answer is separated from the upper entries by a four-bar link. Here the running bass is accompanied by new upper parts. The alto restores the original subject; the soprano answers, reaching G major in bar 55.'},
 {start:55,end:68,label:'Third episode',entries:'Soprano and alto above a continuous bass',detail:'The first episode returns a fifth lower, with alterations. From bar 62, descending suspensions in the upper voices continue above the bass’s semiquavers. The cadence is extended into the coda.'},
 {start:68,end:83,label:'Fourth group: coda',entries:'Bass, bar 68 · alto, bar 72 · soprano, bar 76; alto head, bar 79',detail:'Keller’s final group consists of incomplete subject statements. The head persists while its continuation is replaced by the semiquaver figure; the soprano expands it into a rising sequence. A tonic pedal supports the last eight bars, with a fourth part added from bar 80.'},
];
export const tonalEvents=[
 {id:'g9',bar:9,q:16,key:'G major',short:'G',roman:'V',type:'cadence',evidence:'The answer’s B coincides with G in the alto after F♯–G in the bass of the two-part texture.'},
 {id:'c13',bar:13,q:24,key:'C major',short:'C',roman:'I',type:'cadence',evidence:'Two Cs sound over E at the completion of the bass subject.'},
 {id:'d21context',bar:21,q:40.5,key:'D minor',short:'Dm',roman:'ii',type:'entry',evidence:'The alto entry develops towards D minor, established at its close in bar 25.'},
 {id:'d25',bar:25,q:48,key:'D minor',short:'Dm',roman:'ii',type:'cadence',evidence:'The bass reaches D with F in the alto after C♯ in the preceding bar.'},
 {id:'a29',bar:29,q:56,key:'A minor',short:'Am',roman:'vi',type:'cadence',evidence:'G♯ in the alto resolves to A as the soprano reaches C.'},
 {id:'g39context',bar:39,q:76.5,key:'G major',short:'G',roman:'V',type:'entry',evidence:'The returning bass answer begins C–B–C–G, the original dominant form.'},
 {id:'c47',bar:47,q:92,key:'C major',short:'C',roman:'I',type:'cadence',evidence:'The preceding dominant resolves to C in soprano and bass, with E in the alto.'},
 {id:'g55',bar:55,q:108,key:'G major',short:'G',roman:'V',type:'cadence',evidence:'G in alto and bass supports the soprano’s B at the answer’s end.'},
 {id:'c67',bar:67,q:132,key:'C major',short:'C',roman:'I',type:'cadence',evidence:'The soprano resolves B to C above E and G, a tonic first inversion.'},
 {id:'a68',bar:68,q:134,key:'A minor',short:'Am',roman:'vi',type:'arrival',evidence:'The chromatic bass G♯ rises to A beneath two Cs.'},
 {id:'c76',bar:76,q:150,key:'C major',short:'C',roman:'I',type:'arrival',evidence:'C in the bass initiates the closing tonic pedal beneath C and E.'},
 {id:'c83',bar:83,q:164,key:'C major',short:'C',roman:'I',type:'close',evidence:'The closing chord contains C, E and G over the sustained tonic.'},
];
