export const voices=['Soprano','Alto','Tenor','Bass'];
export const themes=[
 {id:'subject',title:'Subject / real answer',location:'Tenor, bars 1–4',text:'Three ascending thirds overlap, with increasing rhythmic activity, before the line descends to the tonic. The alto’s answer transposes the subject exactly a fifth higher; only the duration of its final note changes. Later entries include diatonic inversion and an ornamented opening.'},
 {id:'cs1',title:'Countersubject',location:'Tenor, bars 4–7',text:'The paired quavers descend against the rising answer. Their first notes are commonly tied across crotchet beats. The continuation takes up the subject’s rising quaver figure. The quaver pairs persist outside complete countersubject statements, including passages beneath the inverted subject.'},
];
export const formalGroups=[
 {start:1,end:20,startQ:0,endQ:118,number:'I',label:'Exposition and modulation to the dominant',range:'1–20',continuation:'T · A · B; episode; S'},
 {start:20,end:40,startQ:118,endQ:240,number:'II',label:'Direct and inverted entries; close',range:'20–40',continuation:'A inverted · S · T · B inverted; S'},
];
export const sections=[
 {start:1,end:11,label:'First three entries',entries:'Tenor, bar 1 beat 2 · alto, bar 4 beat 2 · bass, bar 8 beat 2',detail:'The countersubject passes from tenor to alto. Rising quavers (q), drawn from the subject’s third ascent, link the answer to the bass entry. The third entry closes in F♯ minor.'},
 {start:11,end:15,label:'Episode before the fourth entry',entries:'Rising quavers in the upper three voices',detail:'Sequential imitation prolongs the exposition before the soprano enters. Sighing quaver pairs (s), derived from the countersubject, appear as the episode approaches its close.'},
 {start:15,end:18,label:'Fourth exposition entry',entries:'Soprano, bar 15 beat 2',detail:'The soprano gives the subject in the tonic, with the countersubject in the bass. The alto and tenor continue material from the preceding episode.'},
 {start:18,end:20,label:'Modulating episode',entries:'Rising quavers and countersubject-derived pairs',detail:'The episode moves to C♯ minor. The cadence on beat 4 of bar 20 closes Keller’s first part; the next entry begins one crotchet later.'},
 {start:20,end:23,label:'First inverted entry',entries:'Alto, bar 20 beat 5',detail:'The subject is inverted diatonically, with the same rhythm and overlapping third groups. The harmony moves through B minor towards F♯ minor. A complete countersubject is absent, although its paired quavers continue in the bass.'},
 {start:23,end:25,label:'Link',entries:'Rising quavers in soprano and tenor',detail:'The short episode resumes the subject-derived quavers and prepares the ornamented soprano entry.'},
 {start:25,end:28,label:'Ornamented entry',entries:'Soprano, bar 25 beat 2',detail:'Four quavers replace the opening two crotchets; from the long E onwards, the subject follows the opening answer an octave higher. The alto gives the countersubject. The entry closes in C♯ minor, after which the soprano reaches the fugue’s highest register.'},
 {start:29,end:32,label:'Tenor entry',entries:'Tenor, bar 29 beat 2',detail:'The original subject returns in the tenor. Above it, the soprano alters the countersubject’s opening with two semiquavers. The texture descends towards the subsequent bass entry.'},
 {start:32,end:35,label:'Second inverted entry',entries:'Bass, bar 32 beat 2',detail:'The inverted subject passes through B minor and returns to F♯ minor. The upper parts develop the countersubject’s quaver pairs without a complete statement.'},
 {start:35,end:37,label:'Episode',entries:'Imitation of the quaver pairs',detail:'The paired quavers pass through the voices and lead to the final soprano entry. This is derived counterpoint, rather than a further complete subject entry.'},
 {start:37,end:40,label:'Final entry and close',entries:'Soprano, bar 37 beat 2',detail:'The subject returns over harmony that initially withholds the tonic. The alto gives an altered, incomplete countersubject, partly doubled a sixth below by the tenor. A sustained dominant precedes the final F♯ major chord.'},
];
export const tonalEvents=[
 {id:'cs7',bar:7,q:36,key:'C♯ minor',short:'C♯m',roman:'v',type:'cadence',evidence:'The answer and countersubject converge on C♯ after the tenor’s B♯.'},
 {id:'fs11',bar:11,q:60.5,key:'F♯ minor',short:'F♯m',roman:'i',type:'cadence',evidence:'Over F♯ in bass and alto, the tenor’s B suspension resolves to A.'},
 {id:'fs18',bar:18,q:102,key:'F♯ minor',short:'F♯m',roman:'i',type:'cadence',evidence:'The fourth entry closes on F♯ with A and C♯ in the inner voices.'},
 {id:'cs20',bar:20,q:117,key:'C♯ minor',short:'C♯m',roman:'v',type:'cadence',evidence:'The bass G♯–C♯ and soprano B♯–C♯ close beneath E in the alto.'},
 {id:'fs22',bar:22,q:129,key:'F♯ minor',short:'F♯m',roman:'i',type:'arrival',evidence:'The inverted entry reaches F♯ above A in the bass.'},
 {id:'fs25',bar:25,q:145,key:'F♯ minor',short:'F♯m',roman:'i',type:'arrival',evidence:'The bass E♯ rises to F♯ under A in the soprano and C♯ in the alto.'},
 {id:'cs28',bar:28,q:162,key:'C♯ minor',short:'C♯m',roman:'v',type:'cadence',evidence:'The bass G♯–C♯ and alto B♯–C♯ close in C♯ octaves.'},
 {id:'fs29',bar:29,q:171,key:'F♯ minor',short:'F♯m',roman:'i',type:'arrival',evidence:'C♯ dominant harmony resolves to F♯ above A in the tenor.'},
 {id:'fs32',bar:32,q:186,key:'F♯ minor',short:'F♯m',roman:'i',type:'cadence',evidence:'The tenor entry closes on F♯ beneath A and F♯ in the upper voices.'},
 {id:'bm34',bar:34,q:198,key:'B minor',short:'Bm',roman:'iv',type:'arrival',evidence:'The inverted bass subject reaches B beneath B and D in the upper voices.'},
 {id:'fs35',bar:35,q:204,key:'F♯ minor',short:'F♯m',roman:'i',type:'arrival',evidence:'The bass returns to F♯ beneath A; the alto’s retained G♯ subsequently resolves to F♯.'},
 {id:'fs40',bar:40,q:234,key:'F♯ major',short:'F♯',roman:'I',type:'close',evidence:'The final tonic chord contains A♯ in the tenor.'},
];
