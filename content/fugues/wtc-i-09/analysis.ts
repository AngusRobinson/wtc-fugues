export const voices=['Soprano','Alto','Bass'];
export const themes=[
 {id:'subject',title:'Subject / tonal answer',location:'Alto, bars 1–3',text:'Following Keller, the subject extends to D♯ at the beginning of bar 3, overlapping the soprano answer. The answer begins as a real transposition a fifth higher, but its continuation replaces A♯ with A natural and turns back towards E major: the extended answer is tonal. Prout’s shorter subject, ending on E at bar 2 beat 3, has a real answer.'},
 {id:'cs1',title:'Countersubject continuation',location:'Alto, bars 2–3',text:'Prout identifies this semiquaver continuation as the countersubject. Its opening overlaps Keller’s longer subject; the orange spans begin after that shared passage. It recurs in fragments and sequences, with altered endings, rather than accompanying every entry intact.'},
];
export const formalGroups=[
 {start:1,end:12,startQ:0,endQ:48,number:'I',label:'Exposition and counter-exposition',range:'1–12',continuation:'A · S · B; S · A · B'},
 {start:13,end:16,startQ:48,endQ:64,number:'II',label:'C♯ minor',range:'13–16',continuation:'Central episode'},
 {start:17,end:29,startQ:64,endQ:116,number:'III',label:'Return and final entries',range:'17–29',continuation:'B · S · A; final soprano entry'},
];
export const sections=[
 {start:1,end:6,label:'Exposition',entries:'Alto, bar 1 beat 2½ · soprano, bar 2 beat 2½ · bass, bar 3 beat 4½',detail:'The entries overlap when the subject is read through its modulating continuation, as Keller proposes. Prout places the subject boundary two beats earlier and treats the following semiquavers as the countersubject. The leaping quaver figure (q) in bars 5–6 passes from soprano to alto above the bass’s continuing semiquavers.'},
 {start:6,end:12,label:'Counter-exposition',entries:'Soprano, bar 6 beat 4½ · alto, bar 7 beat 4½ · bass, bar 9 beat 4½',detail:'Each voice takes the other entry type: subject in the soprano, answer in alto and bass. The bass answer redirects its continuation towards C♯ minor. The upper parts add suspensions as the semiquaver continuation (c) passes into episodic sequences.'},
 {start:12,end:17,label:'Central minor-key passage',entries:'Varied soprano subject, bar 12 beat 2 · alto subject, bar 16 beat 2½',detail:'The soprano lengthens the initial quaver to a dotted crotchet and shortens the following crotchet to a quaver. This anticipates Keller’s central span, bars 13–16. Its semiquavers continue over a descending suspension sequence (p) in the alto. The low alto entry closes this span and leads into a two-part continuation.'},
 {start:17,end:22,label:'Tonic return',entries:'Bass, bar 19 beat 2½ · varied soprano answer, bar 20 · alto, bar 21 beat 2½',detail:'The bass’s return completes the E major harmony after the two-part passage. The soprano replaces the answer’s initial quaver with a rising semiquaver approach beginning on the second semiquaver of bar 20; the following C♯ crotchet remains in its usual position. The alto then restores the subject’s opening rhythm.'},
 {start:22,end:25,label:'Episode in double counterpoint',entries:'Earlier soprano semiquavers in the alto; earlier alto suspensions in the soprano',detail:'The two upper parts invert their disposition from bars 13–16, in double counterpoint at the fifteenth, with transposition and local alterations. The new bass moves in quavers. The suspension sequence subsequently passes into the bass beneath the final soprano entry.'},
 {start:25,end:29,label:'Final entry and cadential fragments',entries:'Extended soprano subject, bar 25 beat 2½ · alto head, bar 27 beat 3½ · incomplete bass answer, bar 28 beat 1½',detail:'The soprano’s semiquaver continuation is redirected and extended. The bass in bar 27 contains four altered subject-head allusions (h), with leaps replacing the earlier scalar motion. The alto briefly recalls the head; the last bass answer dissolves into the final cadence rather than completing the subject.'},
];
export const tonalEvents=[
 {id:'b3',bar:3,q:8,key:'B major',short:'B',roman:'V',type:'arrival',evidence:'The subject’s extended continuation reaches D♯ under B in the soprano, after C♯–D♯–E–F♯ motion; this is the dominant region identified by Keller, rather than a full cadence.'},
 {id:'b5',bar:5,q:18,key:'B major',short:'B',roman:'V',type:'cadence',evidence:'The soprano A♯ resolves to B above B in the alto and D♯ in the bass, completing the bass subject’s extended span.'},
 {id:'cs11',bar:11,q:41,key:'C-sharp minor',short:'C♯m',roman:'vi',type:'cadence',evidence:'The bass B♯ rises to C♯ with E and G♯ above, establishing C♯ minor before the varied soprano entry.'},
 {id:'cs13',bar:13,q:49,key:'C-sharp minor',short:'C♯m',roman:'vi',type:'arrival',evidence:'The bass reaches C♯ beneath E in the soprano, confirming the central minor-key region after the preceding first-inversion harmony.'},
 {id:'cs17',bar:17,q:64,key:'C-sharp minor',short:'C♯m',roman:'vi',type:'cadence',evidence:'G♯ in the bass moves to C♯ and the alto B♯ rises to C♯, with E in the soprano.'},
 {id:'e19',bar:19,q:73.5,key:'E major',short:'E',roman:'I',type:'arrival',evidence:'The returning bass adds E beneath G♯ and B, completing the tonic harmony after the two-part passage.'},
 {id:'b21',bar:21,q:81,key:'B major',short:'B',roman:'V',type:'cadence',evidence:'F♯ in the bass moves to B beneath D♯ in the soprano; A♯ in the preceding semiquaver line has confirmed the dominant key.'},
 {id:'e25',bar:25,q:97,key:'E major',short:'E',roman:'I',type:'cadence',evidence:'B in the bass moves to E, under G♯ in the soprano and B in the alto, just before the final subject entry.'},
 {id:'e29',bar:29,q:112,key:'E major',short:'E',roman:'I',type:'close',evidence:'The final dominant resolves to E in the outer voices and G♯ in the alto.'},
];
