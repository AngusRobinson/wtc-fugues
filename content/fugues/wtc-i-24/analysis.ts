export const voices=['Soprano','Alto','Tenor','Bass'];
export const themes=[
 {id:'subject',title:'Subject / tonal answer',location:'Alto, bars 1–4',text:'Descending triads frame a succession of chromatic appoggiaturas. All twelve pitch classes occur; the subject moves from B minor towards its dominant. The first answer is tonal: its first and fifth notes are B, while notes 2–4 transpose down a fourth and the continuation down a fifth.'},
 {id:'cs1',title:'Countersubject',location:'Alto, bar 4 beat 4 to bar 6',text:'Five descending crotchets lead into a cadential turn. Keller distinguishes this sustained countersubject from its introductory and closing semiquaver figures. Both figures recur independently, and the introductory figure also appears by inversion.'},
];
export const formalGroups=[
 {start:1,end:16,startQ:0,endQ:62,number:'I',label:'Exposition',range:'1–16',continuation:'A · T · B · S'},
 {start:16,end:76,startQ:62,endQ:304,number:'II',label:'Entries, anticipations and episodes',range:'16–76',continuation:'No further complete four-voice group'},
];
export const sections=[
 {start:1,end:9,label:'First entries and codetta',entries:'Alto, bar 1 · tenor, bar 4 · bass, bar 9',detail:'The first two entries begin on the second quaver. The introductory semiquaver figure (e) leads to the crotchet countersubject; the closing semiquaver figure (f) generates the codetta in bars 7–8. The bass enters after this imitative link, against an inversion of the introductory figure in the alto.'},
 {start:12,end:16,label:'Completion of the exposition',entries:'Soprano, bar 13, second quaver',detail:'The closing figure in the bass connects the third and fourth entries. The soprano’s answer retains C♯ as its fifth note in the source reading; the opening B still makes it tonal. The tenor gives the inverted introductory figure, while the bass takes the countersubject.'},
 {start:16,end:24,label:'Episode and anticipated entry',entries:'Alto anticipation, bar 19 · complete subject, bar 21',detail:'The sequential suspension figure (p) in soprano and tenor contrasts with the subject’s chromaticism. The alto’s three-note head (h) in bar 19 anticipates its full entry two bars later. The soprano then takes the countersubject.'},
 {start:24,end:33,label:'Second episodic sequence',entries:'Tenor anticipation, bar 28 · complete subject, bar 30',detail:'The closing figure and suspension sequence return in new dispositions. The tenor repeats the three-note anticipatory procedure before its E minor subject. Its terminal B supports the succeeding two-part link.'},
 {start:34,end:41,label:'Longer anticipations',entries:'Alto, bar 34 · soprano, bar 35 · bass, bar 38',detail:'Nine-note anticipations overlap at a bar’s distance, supported by the introductory figure in the tenor. They prepare the complete bass subject, whose first note is E rather than F♯. Following Keller, these partial statements are distinguished from the full entry.'},
 {start:41,end:50,label:'Anticipations and complete entries',entries:'Heads in soprano, alto and bass, bars 41–43 · tenor, bar 44 · bass, bar 47 beat 3½',detail:'Three overlapping nine-note anticipations lead into the tenor’s complete D major form. The bass’s tonal answer begins late in bar 47. The soprano gives an expanded version of the crotchet countersubject, then its closing semiquaver figure.'},
 {start:50,end:57,label:'Connecting episode and tenor entry',entries:'Tenor, bar 53 beat 3½',detail:'The closing semiquaver figure passes between the voices. The tenor enters in F♯ minor, with the introductory figure in the alto and countersubject in the soprano; the phrase closes towards C♯ minor.'},
 {start:57,end:64,label:'Bass and tenor entries',entries:'Bass, bar 57 beat 3½ · tenor, bar 60 beat 3½',detail:'The bass begins in E major but returns towards B minor. The tenor restores the original subject. Against it the soprano and alto supply new accompanying material; a complete countersubject is not forced onto this passage.'},
 {start:65,end:73,label:'Final episodic sequence and entry',entries:'Tenor anticipation, bar 69 · bass, bar 70',detail:'The suspension sequence returns in the upper voices over the tenor. A nine-note tenor anticipation precedes the final complete bass subject by a bar. The bass begins in E minor and ends within B minor harmony.'},
 {start:73,end:76,label:'Coda',entries:'Alto head, bar 74, second quaver',detail:'The seven-note alto head sounds above the dominant pedal. A fifth part appears in the last two bars; the closing B major chord retains the held F♯. The source’s notes and original slurs are preserved.'},
];
export const tonalEvents=[
 {id:'b7',bar:7,q:24,key:'B minor',short:'Bm',roman:'i',type:'cadence',evidence:'The tenor reaches B beneath D in the alto, completing the opening answer.'},
 {id:'b16',bar:16,q:62,key:'B minor',short:'Bm',roman:'i',type:'cadence',evidence:'B in the soprano and F♯ in the alto resolve above D in tenor and bass.'},
 {id:'fs17',bar:17,q:65,key:'F♯ minor',short:'F♯m',roman:'v',type:'arrival',evidence:'The suspensions above F♯ resolve to A, F♯ and C♯.'},
 {id:'b21',bar:21,q:81,key:'B minor',short:'Bm',roman:'i',type:'cadence',evidence:'The soprano reaches B over B in the bass and D in the entering alto.'},
 {id:'e30',bar:30,q:117,key:'E minor',short:'Em',roman:'iv',type:'arrival',evidence:'The soprano’s F♯ appoggiatura resolves to E above G in the tenor, following E–G in the lower parts.'},
 {id:'cs34',bar:34,q:132,key:'C♯ major',short:'C♯',roman:'II',type:'arrival',evidence:'C♯ in the tenor supports E♯ and G♯: the dominant of F♯ minor.'},
 {id:'d44',bar:44,q:173,key:'D major',short:'D',roman:'III',type:'arrival',evidence:'D in soprano and bass coincides with F♯ in the entering tenor.'},
 {id:'d50',bar:50,q:198,key:'D major',short:'D',roman:'III',type:'cadence',evidence:'D in soprano and bass supports F♯ in the tenor at the bass answer’s end.'},
 {id:'cs56',bar:56,q:223,key:'C♯ minor',short:'C♯m',roman:'ii',type:'arrival',evidence:'The tenor reaches C♯ beneath E and G♯ in the upper voices.'},
 {id:'e57context',bar:57,q:226.5,key:'E major',short:'E',roman:'IV',type:'entry',evidence:'The bass subject begins with B–G♯–E before bending back towards B minor.'},
 {id:'b60',bar:60,q:239,key:'B minor',short:'Bm',roman:'i',type:'arrival',evidence:'The alto resolves to B with D in soprano and tenor, following the bass’s B at beat 3.'},
 {id:'b65',bar:65,q:257,key:'B minor',short:'Bm',roman:'i',type:'cadence',evidence:'A♯ in the lowest sounding part resolves to B beneath D and F♯.'},
 {id:'e70',bar:70,q:277,key:'E minor',short:'Em',roman:'iv',type:'arrival',evidence:'The tenor’s D♯ rises to E as the soprano reaches E and the bass subject reaches G.'},
 {id:'b73',bar:73,q:288,key:'B minor',short:'Bm',roman:'i',type:'cadence',evidence:'The final bass subject closes on D beneath F♯ and two Bs.'},
 {id:'b76',bar:76,q:300,key:'B major',short:'B',roman:'I',type:'close',evidence:'The final chord contains B, D♯ and F♯ in five parts.'},
];
