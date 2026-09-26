export const voices=['Soprano','Alto','Bass'];
export const themes=[
 {id:'subject',title:'Subject / tonal answer',location:'Soprano, bars 1–2',text:'The tonal answer changes the opening B♭–G third to E♭–D, a second. After the rest it answers the subject’s modulation to B♭ with a return to E♭. The subject ends on the first semiquaver of bar 2 beat 3; the following arpeggios supply the episodes.'},
 {id:'cs1',title:'Countersubject',location:'Soprano, bars 3–4',text:'Three descending quavers lead to a turning semiquaver figure and a suspension. The countersubject accompanies every entry except the final answer in bar 34, with intervallic and rhythmic adjustments. It appears both above and below the subject.'},
];
export const formalGroups=[
 {start:1,end:17,startQ:0,endQ:66,number:'I',label:'Exposition and additional answer',range:'1–17',continuation:'S · A · B; soprano answer; chromatic episode'},
 {start:17,end:37,startQ:66,endQ:148,number:'II',label:'Minor-key entries and tonic return',range:'17–37',continuation:'Alto · bass; bass · soprano · alto'},
];
export const sections=[
 {start:1,end:7,label:'Exposition',entries:'Subject: soprano, bar 1 · tonal answer: alto, bar 3 · subject: bass, bar 6',detail:'The subject modulates to B♭; the answer returns to E♭. The arpeggio figure (c), beginning as the subject’s closing link, supplies the two-part passage in bars 4–5. The rising upbeat figure (r) appears above it. The countersubject passes from soprano to alto for the bass entry.'},
 {start:7,end:12,label:'First three-part episode and additional answer',entries:'Additional tonal answer: soprano, bar 11 · countersubject: bass',detail:'The arpeggio figure combines with the rising upbeat and a descending quaver figure (q). The latter augments notes of the arpeggio. The episode leads to the additional soprano answer, with the countersubject below it: a contrapuntal inversion of their original disposition.'},
 {start:12,end:17,label:'Episode in triple counterpoint',entries:'Cyclic permutation of the three episodic lines in bars 13–14',detail:'The combination from bars 8–9 returns in triple counterpoint: the former soprano line moves to the alto, the alto line to the bass, and the bass line to the soprano. Chromatic and cadential adjustments redirect the harmony. In bars 15–17 a descending chromatic sequence leads to C minor.'},
 {start:17,end:22,label:'Minor-key entries',entries:'Tonal answer: alto, bar 17 beat 3 · subject: bass, bar 20 beat 3',detail:'The answer remains in C minor; the bass subject modulates from C minor to G minor. The intervening two-part passage freely inverts the disposition of bars 4–5. The countersubject lies in the soprano for the alto entry and in the alto for the bass entry.'},
 {start:22,end:26,label:'Episode and tonic return',entries:'First-bar subject sequences: soprano, bars 22–23',detail:'The subject-head sequences (h) stop before the second half of the subject and are not counted as complete entries. The subsequent dialogue redistributes the arpeggio and upbeat figures over ascending bass motion. E♭ returns during this episode.'},
 {start:26,end:30,label:'Final entry group',entries:'Tonal answer: bass, bar 26 · varied subject: soprano, bar 29',detail:'The countersubject accompanies the bass answer in the soprano. After another link, the soprano subject begins on A♭ instead of B♭; the remaining notes preserve the subject’s contour and modulation. Its countersubject is in the alto.'},
 {start:30,end:37,label:'Final episode, altered answer and close',entries:'Tonal answer: alto, bar 34; without the countersubject',detail:'The last episode recalls the earlier three-part combination with the bass an octave lower. The final answer replaces G with G♭ in bar 34. Its closing E♭ lies over C in the bass; the coda then reaches the tonic, with a chromatic inner descent in the final bar.'},
];
export const tonalEvents=[
 {id:'b2',bar:2,q:6,key:'B-flat major',short:'B♭',roman:'V',type:'cadence',evidence:'The unaccompanied subject closes melodically on B♭ after A natural and the trilled C; its modulation precedes the answer.'},
 {id:'e4',bar:4,q:14,key:'E-flat major',short:'E♭',roman:'I',type:'cadence',evidence:'The alto answer closes on E♭ under G in the soprano.'},
 {id:'b7',bar:7,q:26,key:'B-flat major',short:'B♭',roman:'V',type:'cadence',evidence:'The bass subject closes on B♭ under D and B♭ in the upper parts.'},
 {id:'e12',bar:12,q:46,key:'E-flat major',short:'E♭',roman:'I',type:'cadence',evidence:'Both upper parts reach E♭ over G in the bass, completing the additional answer.'},
 {id:'c17',bar:17,q:66,key:'C minor',short:'Cm',roman:'vi',type:'cadence',evidence:'G in the bass and B natural in the soprano resolve to C in all three parts; E♭ in the ensuing answer confirms the minor mode.'},
 {id:'c19',bar:19,q:72,key:'C minor',short:'Cm',roman:'vi',type:'cadence',evidence:'The alto answer closes on C under E♭, ending its return to C minor.'},
 {id:'g22',bar:22,q:84,key:'G minor',short:'Gm',roman:'iii',type:'cadence',evidence:'F♯ in the preceding soprano and A in the bass resolve to G, with B♭ in the alto.'},
 {id:'e24',bar:24,q:92,key:'E-flat major',short:'E♭',roman:'I',type:'arrival',evidence:'The sequential bass descent reaches low E♭ below G in the alto.'},
 {id:'e27',bar:27,q:106,key:'E-flat major',short:'E♭',roman:'I',type:'cadence',evidence:'The bass answer closes on E♭ under E♭ and G.'},
 {id:'b30',bar:30,q:118,key:'B-flat major',short:'B♭',roman:'V',type:'cadence',evidence:'The varied soprano subject closes on B♭ above D in the alto and B♭ in the bass.'},
 {id:'c35',bar:35,q:138,key:'C minor',short:'Cm',roman:'vi',type:'arrival',evidence:'The final answer’s E♭ closes over C in the bass, approached chromatically through B natural; this is a local diversion, not a sustained modulation.'},
 {id:'e37',bar:37,q:146,key:'E-flat major',short:'E♭',roman:'I',type:'close',evidence:'Over the E♭ pedal, the added inner part completes D♭–C–C♭–B♭. E♭, G and B♭ settle together on beat 3.'},
];
