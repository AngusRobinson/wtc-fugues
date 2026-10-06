export const voices=['Soprano','Alto','Bass'];
export const themes=[
 {id:'subject',title:'Subject / real answer',location:'Alto, bars 1–2',text:'Ascending triplets give way to a chromatic descent in quavers and a cadential tail. The first answer is real, transposing the two-bar subject up a fifth. Its final E resolves to A at the beginning of the link.'},
 {id:'cs1',title:'Countersubject',location:'Alto, bars 3–4',text:'An ascending semiquaver line opposes the subject’s chromatic descent. Its leaps and cadential continuation recur in the soprano with the bass entry, then in the bass beneath the later stretti.'},
 {id:'motif',title:'Episodic semiquaver figure',location:'Alto, bar 7',text:'Neighbour-note semiquavers combine with the countersubject’s closing figure in the episodes. Their sequential development alternates with imitation of the subject’s triplet head.'},
];
export const formalGroups=[
 {start:1,end:8,startQ:0,endQ:28,number:'I',label:'Exposition',range:'1–8',continuation:'Three entries and inverted-head link'},
 {start:8,end:18,startQ:28,endQ:70,number:'II',label:'Episodes and two close stretti',range:'8–18',continuation:'Direct forms, then inversion'},
 {start:18,end:25,startQ:70,endQ:96,number:'III',label:'Extended episode',range:'18–24',continuation:'Triplet dialogue; descending sequences'},
 {start:25,end:27,startQ:96,endQ:108,number:'IV',label:'Final entry group',range:'25–27',continuation:'Alto head; soprano subject and bass countersubject'},
];
export const sections=[
 {start:1,end:8,label:'Exposition',entries:'Alto, bar 1 · soprano, bar 3 · bass, bar 6',detail:'The countersubject begins in the alto at bar 3 beat 3¼, then accompanies the bass entry in the soprano. The intervening link, bar 5, inverts the triplet head (hi) in alto and soprano at two-crotchet intervals.'},
 {start:8,end:10,label:'First episode',entries:'Semiquaver figure in bass, soprano and alto',detail:'The episodic semiquaver figure (e), introduced in the alto in bar 7, combines with the countersubject’s closing figure (t). The sequence approaches F major in bar 9 but turns back to D minor; following Keller, this is not treated as an established modulation.'},
 {start:10,end:12,label:'Incomplete bass entry and soprano statement',entries:'Bass, bar 10 · soprano, bar 10 beat 4',detail:'The bass abandons the subject before the soprano enters. The intervening triplet dialogue gives an impression of stretto without a complete overlapping bass statement. The soprano’s chromatic continuation (c) extends beyond its first descent.'},
 {start:12,end:14,label:'Second episode',entries:'Semiquaver figure in alto, bass and soprano',detail:'The earlier episodic material returns above a descending bass. The soprano’s octave transfer at the end of bar 13 prepares the next entry from above.'},
 {start:14,end:17,label:'Direct stretto',entries:'Alto, bar 14 · soprano, beat 2 · bass countersubject, beat 4¼',detail:'The two upper entries begin a crotchet apart, the soprano a fifth above. Their continuations are adjusted and extended; the countersubject enters in the bass while the upper voices descend chromatically.'},
 {start:17,end:18,label:'Inverted stretto',entries:'Alto, bar 17 · bass, beat 2',detail:'The same crotchet distance returns in the lower fifth. The inverted triplet head descends, then the chromatic line ascends. Both statements break off, leading into G minor.'},
 {start:18,end:21,label:'Triplet dialogue',entries:'Direct heads in bass and soprano, bar 18; shorter inverted figures in all voices',detail:'The G minor heads lead into an extended episode. Inverted triplet figures combine with their following quavers, passing through the parts as the harmony moves through C, F and B♭.'},
 {start:21,end:24,label:'Sequential descent',entries:'Bass triplets, bar 21 · semiquaver exchanges, bars 22–24',detail:'The triplet head rises in the soprano against descending bass sequences. The semiquaver figure returns, then the two lower parts invert their positions in the final descending sequence, reaching the low register from which the closing entries begin.'},
 {start:25,end:27,label:'Final entry group',entries:'Alto, bar 25 · soprano, beat 3 · bass countersubject, bar 26 beat 1¼',detail:'The alto breaks away after the triplet head and prolonged A. The soprano continues the subject above the returning countersubject in the bass. The final cadence closes on bare octaves of D, without a major or minor third.'},
];
export const tonalEvents=[
 {id:'d6',bar:6,q:20,key:'D minor',short:'Dm',roman:'i',type:'arrival',evidence:'The bass enters on D beneath soprano D and alto F after the link’s C♯.'},
 {id:'f9',bar:9,q:34,key:'F major approach',short:'F',roman:'III',type:'entry',evidence:'F in the bass and A in the alto suggest F major; the soprano’s E delays the consonance and the passage turns back towards D minor.'},
 {id:'d10',bar:10,q:36,key:'D minor',short:'Dm',roman:'i',type:'cadence',evidence:'C♯ in the soprano rises to D as the bass reaches D and the alto F.'},
 {id:'f12',bar:12,q:44,key:'F major',short:'F',roman:'III',type:'arrival',evidence:'The descending sequence reaches F in the bass and A in the soprano.'},
 {id:'d12',bar:12,q:46,key:'D major',short:'D',roman:'I',type:'arrival',evidence:'Bass and alto D support F♯ in the soprano, a local major inflection within the sequence.'},
 {id:'bb13',bar:13,q:48.5,key:'B♭ major',short:'B♭',roman:'VI',type:'arrival',evidence:'Bass B♭ supports D and F after the preceding D-minor sonority.'},
 {id:'d14',bar:14,q:52,key:'D minor',short:'Dm',roman:'i',type:'cadence',evidence:'The lower Ds support soprano F as the direct stretto begins.'},
 {id:'a15',bar:15,q:59.5,key:'A minor',short:'Am',roman:'v',type:'arrival',evidence:'The bass resolves G♯ to A beneath E and C.'},
 {id:'g18',bar:18,q:70,key:'G minor',short:'Gm',roman:'iv',type:'arrival',evidence:'G in the bass supports D and B♭ as the direct head succeeds the inverted statement.'},
 {id:'c20',bar:20,q:76,key:'C major',short:'C',roman:'VII',type:'arrival',evidence:'The triplet sequence reaches C in the bass and alto with E in the soprano.'},
 {id:'f20',bar:20,q:78,key:'F major',short:'F',roman:'III',type:'arrival',evidence:'F bass and alto A continue the descending sequential progression.'},
 {id:'bb21',bar:21,q:80,key:'B♭ major',short:'B♭',roman:'VI',type:'arrival',evidence:'B♭ in the lower parts supports soprano D at the next sequential step.'},
 {id:'d24',bar:24,q:92,key:'D minor',short:'Dm',roman:'i',type:'cadence',evidence:'The upper Ds and bass F resolve the preceding dominant preparation.'},
 {id:'d25',bar:25,q:96,key:'D minor',short:'Dm',roman:'i',type:'arrival',evidence:'The alto begins on D above bass F after the descending episode.'},
 {id:'close',bar:27,q:106,key:'D minor, third omitted',short:'D',roman:'i',type:'close',evidence:'All three voices close on D; the final sonority contains no third.'},
];
