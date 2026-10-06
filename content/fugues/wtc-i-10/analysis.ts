export const voices=['Soprano','Bass'];
export const themes=[
 {id:'subject',title:'Subject / real answer',location:'Soprano, bars 1–3',text:'The subject modulates to B minor through an arpeggiated opening and a chromatically descending inner line. The real answer continues towards the second dominant, F♯ major, rather than returning to E minor. Its final A♯ replaces the A natural of an exact transposition.'},
 {id:'cs1',title:'Countersubject',location:'Soprano, bars 3–5',text:'Beginning after the semiquaver rest in bar 3, the countersubject descends through a sixth before its turn and rebound. It recurs with the entries and throughout the first episode, with modal alterations and shortened endings.'},
];
export const formalGroups=[
 {start:1,end:19,startQ:0,endQ:57,number:'I',label:'Exposition and major-key entries',range:'1–19',continuation:'E minor · G major · D major'},
 {start:20,end:38,startQ:57,endQ:114,number:'II',label:'Inverted disposition',range:'20–38',continuation:'A minor · D minor · A minor'},
 {start:39,end:42,startQ:114,endQ:126,number:'III',label:'Coda',range:'39–42',continuation:'Tonic return'},
];
export const sections=[
 {start:1,end:5,label:'Exposition',entries:'Soprano, bar 1 · bass, bar 3',detail:'The subject reaches B minor as the bass enters. The answer continues towards F♯ major, which Keller calls the second dominant. Its raised final note also avoids confirming F♯ minor, as Prout observes. The countersubject follows the soprano’s connecting quaver and semiquaver rest.'},
 {start:5,end:10,label:'First episode',entries:'Countersubject in the bass; semiquaver figure in the soprano',detail:'The episodic semiquaver figure (e) moves above successive forms of the countersubject. The sequence leads to G major at the soprano entry in bar 11.'},
 {start:11,end:19,label:'Major-key entries and second episode',entries:'Soprano, bar 11 · bass, bar 13',detail:'The entries adapt the subject to G major and D major. In bars 15–18 the quaver arpeggio (a), derived from the subject’s opening, alternates between the parts against the descending six-note scale (d), drawn from the countersubject’s sixth. Two groups of three quavers cut across the crotchet pulse. The parts converge in parallel octaves in bar 19.'},
 {start:20,end:29,label:'Return with the parts inverted',entries:'Bass, bar 20 · soprano, bar 22',detail:'The opening entries return with their disposition inverted and transposed, now beginning in A minor. The first episode follows in double counterpoint, with register adjustments. Its altered continuation in bar 29 leads towards D minor.'},
 {start:30,end:38,label:'Minor-key entries and inverted episode',entries:'Bass, bar 30 · soprano, bar 32',detail:'D minor and A minor replace the earlier major-key pair, directing the return to E minor through the subdominant side. The arpeggio and scale episode returns with the parts inverted in bars 34–37. Parallel octaves in bar 38 lead to the tonic.'},
 {start:39,end:42,label:'Coda',entries:'Incomplete soprano subject, bar 39 · altered bass entry, bar 40',detail:'The entries approach stretto at one bar’s distance, but neither completes the subject. The bass replaces the opening arpeggio with a descending third. The final cadence closes in E major; the short arpeggio is followed by the notated rests.'},
];
export const tonalEvents=[
 {id:'b3',bar:3,q:6,key:'B minor',short:'Bm',roman:'v',type:'arrival',evidence:'D in the soprano meets B in the answering bass, completing the subject’s motion to the dominant minor.'},
 {id:'fs5',bar:5,q:12.25,key:'F-sharp major',short:'F♯',roman:'II',type:'arrival',evidence:'F♯ above A♯ follows C♯: the second-dominant harmony identified by Keller, directed towards B minor.'},
 {id:'g11',bar:11,q:30,key:'G major',short:'G',roman:'III',type:'arrival',evidence:'G in the soprano meets B in the bass, following the episode’s approach through D and F♯.'},
 {id:'d13',bar:13,q:36,key:'D major',short:'D',roman:'VII',type:'arrival',evidence:'The bass reaches D beneath F♯ in the soprano at the second major-key entry.'},
 {id:'a20',bar:20,q:57,key:'A minor',short:'Am',roman:'iv',type:'arrival',evidence:'G♯ in parallel octaves rises to A; the following C naturals establish the minor mode.'},
 {id:'e22',bar:22,q:63,key:'E minor',short:'Em',roman:'i',type:'arrival',evidence:'E in the soprano meets G in the bass, answering the A minor entry; this is not the final tonic return.'},
 {id:'d30',bar:30,q:87,key:'D minor',short:'Dm',roman:'vii',type:'arrival',evidence:'A and C♯ give way to D in the bass and F natural in the soprano.'},
 {id:'a32',bar:32,q:93,key:'A minor',short:'Am',roman:'iv',type:'arrival',evidence:'A in the soprano meets C in the bass after the approach through G♯.'},
 {id:'e39',bar:39,q:114,key:'E minor',short:'Em',roman:'i',type:'arrival',evidence:'D♯ octaves resolve to E at the opening of the coda; the ensuing subject head confirms the tonic minor.'},
 {id:'e42',bar:42,q:123,key:'E major',short:'E',roman:'I',type:'close',evidence:'G♯ above the final bass E begins the short arpeggio completing the major tonic.'},
];
