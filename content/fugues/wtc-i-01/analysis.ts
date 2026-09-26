export const voices=['Soprano','Alto','Tenor','Bass'];
export const formalGroups=[
 {start:1,end:14,endQ:52,number:'I',label:'Exposition and two entry groups',range:'1–14',continuation:'Exposition 1–7; stretti from 7 and 10; A minor cadence'},
 {start:14,startQ:52,end:27,number:'II',label:'Four-part stretti and close',range:'14–27',continuation:'Closer overlaps; tonic return; pedal from 24'},
];
export const themes=[
 {id:'subject',title:'Subject / real answer',location:'Alto, bars 1–2; real answer: soprano, 2:3½',text:'The subject rises by step, turns around F, then spans a sixth through alternating leaps. It ends on E at 2:3. The soprano answers a fifth higher without changing the intervals. There is no regular countersubject: subsequent entries repeatedly accompany one another.'},
 {id:'motif',title:'Descending semiquaver figure',location:'Alto, bar 2, from 2:2¼',text:'The subject’s final four semiquavers, A–G–F–E, recur independently as d and in ascending inversion as di. They generate much of the accompanying material. Shorter or altered allusions to the opening are marked h*, separately from the subject entries.'},
];
export const sections=[
 {start:1,end:7,label:'Exposition',entries:'Alto 1:1½ · soprano 2:3½ · tenor 4:1½ · bass 5:3½',detail:'The entry order is subject–answer–answer–subject. The tenor repeats the answer at the lower octave rather than restoring the subject. Descending semiquaver figures (d) and their inversions (di) supply the accompaniment; there is no separate episode before the next group.'},
 {start:7,end:10,label:'First stretto group',entries:'Soprano 7:1½ → tenor 7:2½ · alto 9:1½',detail:'Soprano and tenor overlap at one crotchet’s distance, with the answer a twelfth below. The alto then gives an unpaired answer. Prout calls this group a counter-exposition.'},
 {start:10,end:14,label:'Second group and A minor cadence',entries:'Bass 10:3½ → alto 10:4½ · tenor 12:1½',detail:'The bass entry on G is now answered on D, establishing G major as a local tonic. The tenor enters on E with a form directed towards A minor. Its C naturals and the G♯ leading note prepare the cadence at 14, Keller’s principal division.'},
 {start:14,end:16,label:'Four-part stretto',entries:'Alto 14:1½ → tenor 14:2½ → bass 15:1½ → soprano 15:3½',detail:'The four voices enter at successive distances of one, three and two crotchets. The tenor abandons the closing semiquavers; the soprano breaks off after the turn and begins afresh in bar 16. These curtailed entries are marked with an asterisk.'},
 {start:16,end:19,label:'Second four-part stretto',entries:'Soprano 16:2½ → alto 16:3½ → tenor 17:1½ → bass 17:3',detail:'All four entries retain the closing figure. The bass starts with a crotchet rather than a quaver, shifting its later notes by half a beat. The tenor’s chromatic alterations and the bass’s D minor form prevent the passage from remaining a straightforward tonic–dominant exchange.'},
 {start:19,end:24,label:'Further pairs and tonic return',entries:'Tenor 19:1½ → alto 19:2½ · soprano 20:4½ → tenor 21:3½',detail:'The first pair adapts the subject around A and E; the second enters on G and B, at a sixth rather than a fifth. The bass’s altered head at 20:3½ is marked h*. The harmony resolves to C major in first inversion at 23:2, then reaches root-position tonic at 24.'},
 {start:24,end:27,label:'Tonic pedal and coda',entries:'Tenor 24:1½ → alto 24:3½ · soprano head 24:4½',detail:'Over the sustained bass C, the tenor’s C entry and alto’s F entry overlap by two crotchets. The soprano adds an incomplete opening. Subdominant colour persists into bar 27; the final tonic arrives on beat 3 with the soprano’s highest note, C6.'},
];
export const tonalEvents=[
 {id:'g10',bar:10,q:38.5,key:'G major',short:'G',roman:'V',type:'entry',evidence:'The bass begins on G; the alto answers on D one crotchet later, with F♯. This identifies the entry group’s key, not a cadence at the bass onset.'},
 {id:'a12',bar:12,q:44.5,key:'A minor',short:'Am',roman:'vi',type:'entry',evidence:'The tenor enters on E with G♯ and C natural. The entry is directed towards the A minor cadence at 14.'},
 {id:'a14',bar:14,q:52,key:'A minor',short:'Am',roman:'vi',type:'cadence',evidence:'The bass moves E–A; soprano and tenor reach A, with the alto momentarily silent. The new C subject follows on the second quaver.'},
 {id:'d17',bar:17,q:66,key:'D minor',short:'Dm',roman:'ii',type:'entry',evidence:'The bass subject begins D–E–F–G and later reaches B♭. The opening crotchet is prolonged; this is an entry-context marker, not a D minor cadence.'},
 {id:'c23',bar:23,q:89,key:'C major',short:'C',roman:'I',type:'arrival',evidence:'The soprano resolves B–C while the bass descends F–E. E in the tenor and G in the alto complete C major in first inversion.'},
 {id:'c24',bar:24,q:92,key:'C major',short:'C',roman:'I',type:'cadence',evidence:'The bass moves G–C beneath C, E and G in the upper voices. The tonic pedal begins here, before the tenor’s subject entry.'},
 {id:'f24',bar:24,q:94.5,key:'F major',short:'F',roman:'IV',type:'entry',evidence:'The alto begins the subject on F with B♭ in its turn. This marks subdominant colour over the continuing tonic pedal, not a new root-position cadence.'},
 {id:'c27',bar:27,q:106,key:'C major',short:'C',roman:'I',type:'close',evidence:'The soprano reaches C6 and the alto supplies E5 and G5 above the held bass C and tenor C, completing the final tonic.'},
];
