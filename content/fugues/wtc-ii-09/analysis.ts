export const voices=['Soprano','Alto','Tenor','Bass'];
export const formalGroups=[
 {start:1,end:9,startQ:0,endQ:66,number:'I',label:'Exposition',range:'1–9:1',continuation:'B → T → A → S'},
 {start:9,end:16,startQ:66,endQ:120,number:'II',label:'Stretto',range:'9:2–16:1',continuation:'A–T · B–S'},
 {start:16,end:23,startQ:120,endQ:176,number:'III',label:'Chromatic',range:'16–23:1',continuation:'A–S · B–T'},
 {start:23,end:26,startQ:176,endQ:206,number:'IV',label:'Variant',range:'23–26:4',continuation:'S–A · B–T'},
 {start:26,end:35,startQ:206,endQ:274,number:'V',label:'Diminution',range:'26:4–35:2',continuation:'S–A · T–B; A 30:3'},
 {start:35,end:43,startQ:274,endQ:344,number:'VI',label:'Final group',range:'35:2–43',continuation:'A–T–B · S; B 40'},
];
export const themes=[
 {id:'subject',title:'Subject / real answer',location:'Subject: bass, bars 1–2',text:'The six-note subject receives a real answer at the fifth in the tenor, bar 2 beat 3. Later entries shorten the opening note, fill the rising third, or halve the note values.'},
 {id:'cs1',title:'Countersubject',location:'Bass, bars 3–4',text:'The ascending crotchets and the leap down and back form the recurring counterpoint. It also supplies the imitative passage in bars 12–16 and returns in the final group. Adapted statements are marked CS*.'},
 {id:'cs2',title:'Chromatic counterpoint x',location:'Tenor, bars 16–17',text:'The leap up is followed by suspensions and descending chromatic motion. This line returns in the alto and soprano, with changes at its opening. Tovey identifies it as an additional countersubject.'},
 {id:'cs3',title:'Chromatic counterpoint y',location:'Bass, bars 16–17',text:'The slower line ascends through C♯–D–D♯–E, against x. It returns in the tenor and alto. Together, x and y provide recurrent counterpoint to the stretti of bars 16–21.'},
];
export const sections=[
 {start:1,end:9,label:'Exposition and codetta',entries:'Bass 1:1 · tenor 2:3 · alto 4:1 · soprano 5:3',detail:'Subject and real answer alternate at intervals of one and a half bars. The countersubject appears in the bass at bar 3, tenor at bar 4 beat 3 and alto at bar 6. The codetta reaches B major at bar 9.'},
 {start:9,end:16,label:'Paired stretto and episode',entries:'Alto 9:2 → tenor 9:3 · bass 10:3 → soprano 11:1',detail:'The alto’s first note is shortened: its sounding onset precedes the tenor by one minim, within the underlying half-bar scheme. The second pair enters half a bar apart. The countersubject-derived figure (c) passes through soprano, alto, bass and tenor in bars 12–15, closing in C♯ minor at bar 16.'},
 {start:16,end:23,label:'Stretto with chromatic counterpoint',entries:'Alto 16:1 → soprano 17:1 · bass 19:1 → tenor 20:1',detail:'Both pairs enter one bar apart. Chromatic counterpoint x and chromatic counterpoint y recur around the subject in three dispositions: tenor/bass, alto/tenor, soprano/alto. The final tenor entry adapts the subject to F♯ minor and delays its closing note; the cadence arrives at bar 23.'},
 {start:23,end:27,label:'Variation stretto',entries:'Soprano 23:1 → alto 23:2 · bass 25:1 → tenor 25:2',detail:'A passing note fills the rising third and the following note is tied across the bar-line. Each pair enters one minim apart, first at the lower fourth, then at the upper fifth. The two lines return in contrapuntal inversion. Keller treats this as a thematic group; Prout calls it an episode.'},
 {start:26,end:32,label:'Diminution and return of original values',entries:'Soprano 26:4 → alto 27:2 · tenor 28:2 → bass 28:4; bass 30:2 → alto 30:3',detail:'The first two pairs halve the subject’s note values and enter two minims apart. A further diminished entry in the bass has an altered close; the alto overlaps it in the original values, beginning on E at bar 30 beat 3. This is the return of the original subject rhythm, over continuing harmonic motion.'},
 {start:32,end:35,label:'Sequential continuation',entries:'Upper-voice dialogue · ascending bass sequence',detail:'The altered inverted-diminution figure (i) is clearest in the descending upper lines. The bass sequence and chromatic voice-leading lead to the G♯ minor cadence at bar 35. These passages are marked as derived material, rather than exact inverted entries.'},
 {start:35,end:40,label:'Final stretto',entries:'Alto 35:2 → tenor 35:3 → bass 36:3; soprano 37:4',detail:'The shortened alto opening recalls bar 9. The soprano adds an altered inversion-like figure, then the countersubject. Its own subject entry is delayed to beat 4 of bar 37 and has a shortened opening, reaching the fugue’s highest note, A5, in bar 38. The bass rests during the ensuing three-part descent.'},
 {start:40,end:43,label:'Last entry and close',entries:'Answer: bass 40:1 · countersubject variant: alto 40:3½',detail:'The final answer continues down the scale beyond its closing B; the soprano follows with a descending line. Crotchet rests interrupt the inner voices in bar 42. The final E major cadence falls at bar 43 beat 3.'},
];
export const tonalEvents=[
 {id:'b9',bar:9,q:64,key:'B major',short:'B',type:'cadence',evidence:'A♯ in the tenor rises to B; C♯ in the alto resolves to F♯ above the sustained bass B. The soprano settles on D♯. The first stretto follows on beat 2.'},
 {id:'cs16',bar:16,q:120,key:'C♯ minor',short:'C♯m',type:'cadence',evidence:'The G♯ dominant of bar 15, with B♯ and F♯, resolves to C♯ and E at bar 16. The alto subject enters on E within this C♯ minor arrival.'},
 {id:'fs23',bar:23,q:176,key:'F♯ minor',short:'F♯m',type:'cadence',evidence:'E♯ in the soprano resolves to F♯ over bass F♯, with A in the alto and C♯ in the tenor. The ornamented subject begins at the cadence.'},
 {id:'b28',bar:28,q:216,key:'B major',short:'B',type:'cadence',evidence:'The bass F♯ of bar 27 resolves to B as the soprano A♯ rises to B; D♯ in the alto supplies the third. The diminished entries continue through this cadence.'},
 {id:'e30',bar:30,q:236,key:'E major',short:'E',type:'entry',evidence:'The alto begins the subject on E in its original note values. The bass is C♯ and the tenor G♯: this is an entry context, not a tonic cadence.'},
 {id:'e31',bar:31,q:244,key:'E major',short:'E',type:'arrival',evidence:'At beat 3 the bass reaches E under G♯ in the alto and tenor and B in the soprano. This tonic sonority is embedded in the continuing sequence.'},
 {id:'gs35',bar:35,q:272,key:'G♯ minor',short:'G♯m',type:'cadence',evidence:'F𝄪 in the soprano resolves to G♯ while the bass moves from D♯ to G♯. B and D♯ complete the tonic triad; the final group begins on the next minim.'},
 {id:'e43',bar:43,q:340,key:'E major',short:'E',type:'close',evidence:'The bass B moves to E at beat 3. F♯ and D♯ in the upper voices resolve to E and B, with G♯ in the tenor.'},
];
