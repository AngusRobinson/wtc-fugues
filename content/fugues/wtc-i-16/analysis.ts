export const voices=['Soprano','Alto','Tenor','Bass'];
export const themes=[
 {id:'subject',title:'Subject / tonal answer',location:'Alto, bars 1–2',text:'The head begins on the dominant, leaps down a sixth and approaches the tonic chromatically. After a quaver rest, a semiquaver figure rises to the fourth degree and settles on the third. The tonal answer begins on G rather than A; its remaining notes lie a fifth higher.'},
 {id:'cs1',title:'Countersubject',location:'Alto, bars 3–4',text:'The subject’s second figure is inverted to form the opening; the continuation freely inverts and adapts the head. The result is a continuous phrase. It accompanies the later entries, with alteration or curtailment in the stretti, but is absent from the final tenor statement.'},
];
export const formalGroups=[
 {start:1,end:12,startQ:0,endQ:44.5,number:'I',label:'Exposition and first episode',range:'1–12',continuation:'A · S · B · T; episode'},
 {start:12,end:28,startQ:44.5,endQ:108.5,number:'II',label:'Major-key entries, stretto and return',range:'12–28',continuation:'B♭ / F; stretto; C minor / G minor'},
 {start:28,end:34,startQ:108.5,endQ:136,number:'III',label:'Closing stretto and coda',range:'28–34',continuation:'S · T · B; A · T'},
];
export const sections=[
 {start:1,end:8,label:'Exposition',entries:'Alto, bar 1 · soprano, bar 2 beat 3½ · bass, bar 5 · tenor, bar 6 beat 3½',detail:'Entries beginning at the start of a bar enter after a quaver rest. The countersubject passes through alto, soprano and bass. A short codetta between the second and third entries sequences the subject-tail figure (t).'},
 {start:8,end:12,label:'First episode',entries:'Subject-tail figure and its inversion (ti)',detail:'The two forms of the tail supply sequential and imitative material. The episode passes through G minor before cadencing in B♭ major.'},
 {start:12,end:16,label:'Major-key entry group',entries:'Alto, bar 12 · bass, bar 13 beat 3½ · soprano, bar 15',detail:'The first entry is in B♭ major; the next two establish F major. The countersubject appears twice in the tenor and then in the bass. The soprano’s return restores four active voices.'},
 {start:17,end:19,label:'First stretto',entries:'Bass, bar 17 · alto, bar 17 beat 3½',detail:'The alto follows the bass after two crotchets, initially a twelfth higher. Both subjects adapt to the changing harmony. The soprano gives the countersubject. Keller singles out this widely spaced combination, together with the closing stretto, as a principal culmination.'},
 {start:19,end:20,label:'Short episode',entries:'Descending tail figures in the upper voices',detail:'The texture contracts to three voices and turns towards C minor. The descending figures continue the subject-derived material.'},
 {start:20,end:24,label:'Minor-key entries',entries:'Bass, bar 20 · soprano, bar 21 beat 3½ · alto, bar 23 beat 1½',detail:'The first two entries establish C minor. The alto then gives the answer-form in G minor, inserting D as a passing semiquaver between C and E♭. The countersubject moves from alto to bass and then, with alteration, to soprano.'},
 {start:24,end:28,label:'Extended episode',entries:'Tail figures and their inversions',detail:'Sequential exchanges between the three active voices return to the dominant of G minor. The tenor remains silent until the closing stretto.'},
 {start:28,end:30,label:'Closing stretto',entries:'Soprano, bar 28 · tenor, bar 28 beat 3½ · bass, bar 29',detail:'Successive entries are two crotchets apart. The tenor follows an octave below the soprano; the bass adds an incomplete entry another octave lower. The soprano changes its final note, while the alto gives a curtailed countersubject above it. The disposition reworks the earlier stretto in double counterpoint at the twelfth, as Tovey observes.'},
 {start:30,end:34,label:'Final entries and close',entries:'Alto, bar 31 beat 3½ · tenor, bar 33',detail:'The bass accompanies the alto entry with the countersubject. At bar 33 the middle texture divides, making five parts for the final tenor statement. Its final B natural supplies the major third of the closing tonic chord.'},
];
export const tonalEvents=[
 {id:'dm4',bar:4,q:12,key:'D minor',short:'Dm',roman:'v',type:'cadence',evidence:'The countersubject C♯–D closes beneath F in the answer.'},
 {id:'gm6',bar:6,q:22,key:'G minor',short:'Gm',roman:'i',type:'cadence',evidence:'F♯ resolves to G in the soprano above the subject’s B♭ and D in the alto.'},
 {id:'gm10',bar:10,q:38,key:'G minor',short:'Gm',roman:'i',type:'arrival',evidence:'G in bass and soprano supports B♭ in the tenor.'},
 {id:'bb12',bar:12,q:44,key:'B♭ major',short:'B♭',roman:'III',type:'cadence',evidence:'The bass F–B♭ and soprano A–B♭ close beneath D in the tenor.'},
 {id:'f15',bar:15,q:56.5,key:'F major',short:'F',roman:'VII',type:'arrival',evidence:'The alto’s B♭ suspension resolves to A over F in the tenor and A in the bass.'},
 {id:'f16',bar:16,q:62,key:'F major',short:'F',roman:'VII',type:'cadence',evidence:'The bass E–F closes beneath A and C in the upper parts.'},
 {id:'bb18',bar:18,q:70,key:'B♭ major',short:'B♭',roman:'III',type:'arrival',evidence:'The soprano A–B♭ resolves above D in the bass and F in the tenor.'},
 {id:'cm21',bar:21,q:82,key:'C minor',short:'Cm',roman:'iv',type:'cadence',evidence:'B natural rises to C in the alto above E♭ in the bass and G in the soprano.'},
 {id:'cm23',bar:23,q:88,key:'C minor',short:'Cm',roman:'iv',type:'cadence',evidence:'The bass B natural–C closes beneath E♭ and G.'},
 {id:'gm24',bar:24,q:94,key:'G minor',short:'Gm',roman:'i',type:'cadence',evidence:'The bass D–G resolves beneath B♭ and G in the upper voices.'},
 {id:'d28',bar:28,q:108,key:'D major',short:'D',roman:'V',type:'cadence',evidence:'The episode ends on D in bass and alto with F♯ in the soprano.'},
 {id:'g34',bar:34,q:134,key:'G major',short:'G',roman:'I',type:'close',evidence:'The final tenor B natural completes the G major chord.'},
];
