export const voices=['Soprano','Alto','Tenor','Bass'];
export const themes=[
 {id:'subject',title:'Subject / real answer',location:'Bass, bars 1–2',text:'The real answer transposes the subject up a fifth without tonal alteration. The demisemiquaver head is followed by a sixth leap and a dotted descent. There is no regular countersubject.'},
 {id:'motif',title:'Derived figures',location:'Episode figure: soprano, bar 9',text:'The descending semiquaver sequence (e) augments the last four demisemiquavers of the head. Complete head fragments (h) recur independently; the closing bars develop the dotted tail (d).'},
];
export const formalGroups=[
 {start:1,end:8,number:'I',label:'Exposition and additional entries',range:'1–8',continuation:'B · T · A · S; B · S'},
 {start:9,end:16,number:'II',label:'Episode and middle entries',range:'9–16',continuation:'G-major group; E-minor bass entry'},
 {start:17,end:27,number:'III',label:'Episodic development and close',range:'17–27',continuation:'Head imitation; dotted conclusion'},
];
export const sections=[
 {start:1,end:6,label:'Exposition',entries:'Subject: bass, bar 1 · real answer: tenor, bar 2 · subject: alto, bar 4 · answer: soprano, bar 5; all on beat 2',detail:'The one-bar link in bar 3 delays the alto entry. The parts enter from lowest to highest; the exposition closes in A major at bar 6. The accompanying material is free rather than a recurring countersubject.'},
 {start:6,end:9,label:'Additional entries',entries:'Subject: bass, bar 7 beat 2 · subject: soprano, bar 8 beat 2, B minor',detail:'Demisemiquaver subject-head fragments (h) enter in the tenor during bar 6. The low bass entry restores D major. The subsequent soprano statement leads to B minor at bar 9. Prout describes these as an irregular, incomplete counter-exposition.'},
 {start:9,end:11,label:'First episode',entries:'Head fragments: bass, bars 9–11 beat 1',detail:'The augmented episode figure (e) descends in the soprano while the bass interjects the head. Successive first-inversion harmonies descend by thirds, leading to G major at bar 11.'},
 {start:11,end:17,label:'Second entry group',entries:'Soprano, bar 11 · alto, bar 12 · soprano, bar 13 · tenor, bar 14 · bass, bar 15; all on beat 2',detail:'The G-major group alternates subject and answer forms. The bass fragment at bar 13 starts a beat before the soprano entry and leaps an octave after its head; it is not counted as a complete entry. The final complete subject enters in E minor in the bass and is followed by a cadential extension to bar 17.'},
 {start:17,end:21,label:'Inverted episode and head imitation',entries:'Head fragments in all four parts during bar 20',detail:'The second episode inverts the disposition of the first: the augmented figure lies in the bass, the head in the soprano. The sequence gains an extra bar. In bar 20 the head passes successively through soprano, alto, bass and tenor. These are imitations of the head, not a stretto of complete subjects.'},
 {start:21,end:27,label:'Tonic close and coda',entries:'Head fragments: outer voices, bars 23–24 · dotted tail: all parts, bars 25–26',detail:'The cadence in bar 21 establishes D major. The episode figure returns briefly above the bass head. The head fragments become continuous in bar 24; the dotted tail (d) then supplies the chordal conclusion, with contrary motion between the outer parts. No complete subject returns.'},
];
export const tonalEvents=[
 {id:'a3',bar:3,q:8,key:'A major',short:'A',roman:'V',type:'cadence',evidence:'The tenor answer closes on C♯ over A in the bass.'},
 {id:'a6',bar:6,q:20,key:'A major',short:'A',roman:'V',type:'cadence',evidence:'The soprano answer closes on C♯ over three A notes; G♯ in the alto resolves to A.'},
 {id:'d7',bar:7,q:25,key:'D major',short:'D',roman:'I',type:'arrival',evidence:'The bass subject enters on low D under A, D and F♯, restoring the tonic after the dominant close.'},
 {id:'b9',bar:9,q:32,key:'B minor',short:'Bm',roman:'vi',type:'cadence',evidence:'F♯ and A♯ in the approach resolve to B; D supplies the minor third in the soprano.'},
 {id:'g11',bar:11,q:40,key:'G major',short:'G',roman:'IV',type:'cadence',evidence:'G–D–G–B closes the sequence in G major. The soprano subject begins one crotchet later.'},
 {id:'e15',bar:15,q:57,key:'E minor',short:'Em',roman:'ii',type:'arrival',evidence:'The last complete subject begins on E in the bass beneath G, B and E.'},
 {id:'e17',bar:17,q:64,key:'E minor',short:'Em',roman:'ii',type:'cadence',evidence:'The B dominant with D♯ resolves to E minor. The following episode begins on this cadence.'},
 {id:'d21',bar:21,q:80,key:'D major',short:'D',roman:'I',type:'cadence',evidence:'The A dominant resolves to D and F♯ at the beginning of bar 21.'},
 {id:'d27',bar:27,q:104,key:'D major',short:'D',roman:'I',type:'close',evidence:'The two-crotchet A dominant in bar 26 resolves to D–F♯–A–D, held for the final bar.'},
];
