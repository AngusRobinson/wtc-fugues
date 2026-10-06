export const voices=['Soprano','Alto','Tenor','Bass'];
export const themes=[
 {id:'subject',title:'Subject / tonal answer',location:'Tenor, bars 1–4',text:'The subject rises from the dominant to the octave and descends through chromatic inflections to the tonic. The tonal answer begins on F instead of G; its remaining notes transpose the subject a fifth higher. This altered opening occurs only in the first answer.'},
 {id:'cs1',title:'First main countersubject',location:'Tenor, bars 4–7',text:'Four semiquaver ascents oppose the subject’s predominantly descending crotchets. The preceding link supplies the episodic figure. This countersubject accompanies every later entry except the E♭ major entry, where only fragments remain.'},
 {id:'cs2',title:'Second main countersubject',location:'Tenor, bars 7–10',text:'The descending line and its semiquaver continuation combine with subject and first countersubject in triple counterpoint. It divides between alto and tenor under the soprano entry in bars 13–16, and moves above both other themes in bars 28–30.'},
 {id:'cs3',title:'Additional countersubject',location:'Alto, bars 28–30',text:'Tovey identifies a third countersubject, heard only twice. Its first appearance is divided between tenor and alto in bars 13–16; the second lies in the alto above the first main countersubject. Keller’s account centres on the two main countersubjects.'},
];
export const formalGroups=[
 {start:1,end:18,number:'I',label:'Interrupted exposition',range:'1–18',continuation:'T · A · B; episode; S; episode'},
 {start:19,end:33,number:'II',label:'Separated minor-key entries',range:'19–33',continuation:'T; episode; B; episode'},
 {start:34,end:46,number:'III',label:'Major-key entries',range:'34–46',continuation:'A; episode; T; episode'},
 {start:47,end:58,number:'IV',label:'Closing minor-key entries',range:'47–58',continuation:'S; episode; B; coda'},
];
export const sections=[
 {start:1,end:10,label:'Opening entries',entries:'Tenor, bar 1 beat 2 · alto, bar 4 beat 2 · bass, bar 7 beat 2',detail:'The tonal answer accompanies the first main countersubject. The bass enters with the subject while the alto takes that countersubject and the tenor introduces the second. The short link figure (e) preceding the first countersubject supplies the episodes; its later rising figure is marked r.'},
 {start:10,end:13,label:'Episode',entries:'Imitation of the link figure in alto, tenor and bass',detail:'The sequence descends while the ascending link figure passes between the voices. This diatonic passage interrupts the exposition before the soprano has entered.'},
 {start:13,end:16,label:'Fourth entry',entries:'Soprano, bar 13 beat 2; subject, rather than answer',detail:'The bass supplies the first main countersubject. The second and the additional countersubject divide between alto and tenor. The soprano prolongs its penultimate G before resolving briefly to F in bar 16.'},
 {start:16,end:19,label:'Episode',entries:'Ascending sequence of the inverted link figure (ei)',detail:'The descending form of the link figure is sequenced upwards. Alto and bass imitate it beneath the soprano; the tenor is silent before its entry.'},
 {start:19,end:22,label:'C minor entry',entries:'Tenor, bar 19 beat 2',detail:'The subject now begins on G without the opening answer’s tonal alteration. The first main countersubject lies in the soprano and the second in the alto, both above the subject.'},
 {start:22,end:27,label:'Episode',entries:'Descending sequence; bass silent',detail:'The inverted link figure continues in a different disposition of the upper parts. The extended passage prepares the return of the subject in the lowest register.'},
 {start:27,end:30,label:'F minor entry',entries:'Bass, bar 27 beat 4',detail:'The first main countersubject lies in the tenor, the second in the soprano and the additional countersubject in the alto. Relative to bars 13–16, the subject moves from above the two main countersubjects to below them: the combination is in triple counterpoint.'},
 {start:30,end:34,label:'Episode',entries:'Link figure in bass, imitated by tenor',detail:'A new soprano line accompanies a return to the ascending link figure. The alto falls silent, leaving space for the next entry.'},
 {start:34,end:37,label:'A♭ major entry',entries:'Alto, bar 34 beat 2',detail:'The subject is adapted to the major mode, though its chromatic descent remains. The soprano gives the first main countersubject with a varied opening. The ensuing harmony turns towards F minor.'},
 {start:37,end:40,label:'Episode',entries:'Rising countersubject figure in soprano; imitation in alto',detail:'The rising semiquaver figure (r) develops against the inverted link figure in the bass. The tenor remains absent until its entry.'},
 {start:40,end:43,label:'E♭ major entry',entries:'Tenor, bar 40 beat 4',detail:'The major-mode subject begins later in the bar than the earlier tenor entries. The regular countersubjects give way to freer accompanying lines; fragments of the first persist in alto and bass.'},
 {start:43,end:47,label:'Four-part episode',entries:'Expanded treatment of the ascending link figure',detail:'This is the only four-voice episode. Towards its close the soprano descends to B3, so that its entry on G5 is separated by a wide change of register.'},
 {start:47,end:50,label:'C minor entry',entries:'Soprano, bar 47 beat 2',detail:'The first main countersubject lies in the alto and a varied second countersubject in the tenor. The bass withdraws. The soprano again delays the final resolution of its subject.'},
 {start:50,end:53,label:'Episode',entries:'Return of the inverted link figure',detail:'The episode recalls bars 16–19 in C minor, with a changed continuation that returns to F minor. The bass remains silent before its final entry.'},
 {start:53,end:58,label:'Final entry and coda',entries:'Bass, bar 53 beat 2; first main countersubject in soprano',detail:'The last subject repeats the lowest bass register. Its closing F supports B♭ minor harmony before the coda; the final cadence closes in F major. Keller hears a sustained opposition of thematic passages and episodes, without a separate concluding intensification.'},
];
export const tonalEvents=[
 {id:'c7',bar:7,q:24,key:'C minor',short:'Cm',roman:'v',type:'cadence',evidence:'The answer falls D–C while the tenor rises B–C, converging on C.'},
 {id:'f10',bar:10,q:36,key:'F minor',short:'Fm',roman:'i',type:'cadence',evidence:'The bass G–F and alto E–F close with A♭ in the tenor.'},
 {id:'f16',bar:16,q:60.5,key:'F minor',short:'Fm',roman:'i',type:'arrival',evidence:'The soprano’s prolonged G resolves to F over F–A♭–C in the other voices.'},
 {id:'c19',bar:19,q:72.5,key:'C minor',short:'Cm',roman:'v',type:'arrival',evidence:'The soprano F resolves to E♭ over C in the bass and G in the alto.'},
 {id:'c22',bar:22,q:84,key:'C minor',short:'Cm',roman:'v',type:'cadence',evidence:'The tenor D–C and soprano B–C close with E♭ in the alto.'},
 {id:'f30',bar:30,q:118,key:'F minor',short:'Fm',roman:'i',type:'cadence',evidence:'The bass reaches F beneath A♭–C–F at the close of its entry.'},
 {id:'ab34',bar:34,q:133,key:'A♭ major',short:'A♭',roman:'III',type:'arrival',evidence:'E♭ dominant-seventh harmony resolves to A♭ major over C as the alto begins its major-mode subject.'},
 {id:'eb40',bar:40,q:159.5,key:'E♭ major',short:'E♭',roman:'VII',type:'arrival',evidence:'Following B♭ dominant harmony, the soprano settles on E♭ over G–B♭–G.'},
 {id:'eb43',bar:43,q:170,key:'E♭ major',short:'E♭',roman:'VII',type:'cadence',evidence:'The B♭ dominant resolves to E♭, with G in the soprano and B♭ in the alto.'},
 {id:'c48',bar:48,q:190.25,key:'C minor',short:'Cm',roman:'v',type:'arrival',evidence:'After the dominant resolves to C and G, E♭ in the alto completes the minor triad.'},
 {id:'c50',bar:50,q:196.5,key:'C minor',short:'Cm',roman:'v',type:'arrival',evidence:'The soprano’s D resolves to C above the tenor E♭ and alto G.'},
 {id:'f53',bar:53,q:208.5,key:'F minor',short:'Fm',roman:'i',type:'arrival',evidence:'The soprano B♭ falls to A♭ over F in tenor and alto, before dominant harmony supports the final subject entry.'},
 {id:'f58',bar:58,q:228,key:'F major',short:'F',roman:'I',type:'close',evidence:'The dominant pedal resolves to F with A natural in the tenor.'},
];
