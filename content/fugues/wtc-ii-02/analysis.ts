export const voices=['Soprano','Alto','Tenor','Bass'];
export const themes=[
 {id:'subject',title:'Subject / tonal answer',location:'Alto, bars 1–2',text:'The compact subject moves from dominant to tonic and ends with a semiquaver turn. The first answer is tonal: the opening G is answered by C, while the remaining notes transpose up a fifth. There is no regular countersubject.'},
 {id:'motif',title:'Derived semiquaver figure',location:'Tenor, bar 5',text:'The subject’s head is rearranged within an ascending semiquaver line. The soprano inverts the whole bar in bar 6; the alto continues the figure, with alterations, in bar 7.'},
];
export const formalGroups=[
 {start:1,end:14,startQ:0,endQ:52.5,number:'I',label:'Exposition and further entries',range:'1–14',continuation:'Three voices; G minor cadence'},
 {start:14,end:28,startQ:52.5,endQ:112,number:'II',label:'Stretti, augmentation and inversion',range:'14–28',continuation:'Bass enters in 19; coda from 23'},
];
export const sections=[
 {start:1,end:5,label:'Exposition',entries:'Alto, bar 1 · soprano, bar 2 · tenor, bar 4',detail:'The first three entries begin on the second quaver. A one-bar link separates the answer from the tenor’s subject. Following Keller, the lowest sounding part remains the tenor until the fourth voice enters in bar 19.'},
 {start:5,end:7,label:'Derived episode',entries:'Tenor, bar 5 · soprano, bar 6 · alto, bar 7',detail:'The semiquaver figure (e) and its inversion (ei) develop the subject’s opening. These figures replace a fixed countersubject and pass between the parts.'},
 {start:7,end:14,label:'Further entries and sequential continuation',entries:'Tenor, bar 7 · soprano, bar 8 · alto, bar 10 · tenor, bar 11 beat 3½',detail:'The tenor and alto answers use B natural. The soprano’s entry delays its first note by a semiquaver and extends into a sequence. Subject-derived writing continues in the lowest part; the tenor’s F minor entry precedes a cadence in G minor.'},
 {start:14,end:16,label:'Triple stretto',entries:'Soprano, bar 14 beat 1½ · alto, beat 2 · tenor, bar 15 beat 1½',detail:'The subject combines with its augmentation in the alto and a tonally adjusted inverted form in the tenor. The augmented statement ends as the alto’s next answer begins.'},
 {start:16,end:19,label:'Successive stretti',entries:'Alto, bar 16 beat 1½ · soprano, beat 3½ · tenor, bar 17 beat 1½; soprano, bar 17 beat 3¾ · alto, bar 18 beat 1¾',detail:'The first chain enters at two-crotchet intervals; the next soprano–alto pair keeps the same distance despite its shortened opening notes. Chromatic adjustments sharpen the succession of harmonies. The source retains A natural in the tenor and D natural in the soprano in bar 18.'},
 {start:19,end:23,label:'Entry of the bass',entries:'Bass augmentation, bar 19 beat 2 · inversion, bar 21 beat 1¾ · answer, bar 22 beat 1½',detail:'The reserved fourth voice enters with the augmented subject, then gives its adjusted inversion and a direct answer without a long interruption. The soprano inverts the subject’s tail (ti) above the augmentation. The passage closes in C minor halfway through bar 23.'},
 {start:23,end:28,label:'Coda',entries:'Alto–soprano, bar 23 · soprano–alto, bars 24–25 · tenor, bar 25 beat 3½ · bass, bar 26 beat 1½',detail:'The upper voices enter a crotchet apart, reversing their order in the second pair. The tenor follows at two crotchets’ distance. An altered bass inversion and an alto head (h) coincide in bar 26. Detached chords interrupt the imitative texture before the final C minor chord.'},
];
export const tonalEvents=[
 {id:'g3',bar:3,q:8,key:'G minor',short:'Gm',roman:'v',type:'cadence',evidence:'The answer’s B♭ coincides with G in the alto after the preceding dominant preparation.'},
 {id:'c5',bar:5,q:16,key:'C minor',short:'Cm',roman:'i',type:'cadence',evidence:'Two Cs sound above the tenor’s E♭ at the end of its subject.'},
 {id:'g8',bar:8,q:28,key:'G major',short:'G',roman:'V',type:'arrival',evidence:'The altered answer ends on B natural with D in the alto; G follows in the lowest part.'},
 {id:'f10',bar:10,q:36,key:'F minor',short:'Fm',roman:'iv',type:'arrival',evidence:'The soprano’s sequential continuation reaches A♭ above F in alto and tenor.'},
 {id:'g14',bar:14,q:52,key:'G minor',short:'Gm',roman:'v',type:'cadence',evidence:'The first part closes on three Gs, resolving the preceding D–F♯ dominant.'},
 {id:'c16',bar:16,q:60,key:'C minor',short:'Cm',roman:'i',type:'arrival',evidence:'The inverted tenor statement reaches C beneath E♭ in the upper voices.'},
 {id:'f18',bar:18,q:68,key:'F major',short:'F',roman:'IV',type:'arrival',evidence:'The tenor’s G rises to A natural beneath F in the soprano, within the chromatic stretto.'},
 {id:'c23',bar:23,q:90,key:'C minor',short:'Cm',roman:'i',type:'cadence',evidence:'The dominant resolves to C in three parts with E♭ in the tenor.'},
 {id:'c24',bar:24,q:94,key:'C major',short:'C',roman:'I',type:'arrival',evidence:'The alto’s E natural sounds with C and G, turning towards F minor.'},
 {id:'f25',bar:25,q:96,key:'F minor',short:'Fm',roman:'iv',type:'arrival',evidence:'F in the alto coincides with the soprano’s A♭ as the subject shifts to F minor.'},
 {id:'c28',bar:28,q:108,key:'C minor',short:'Cm',roman:'i',type:'close',evidence:'The final chord retains E♭ above C and G.'},
];
