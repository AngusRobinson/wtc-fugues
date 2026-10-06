export const voices=['Soprano','Alto','Bass'];
export const themes=[
 {id:'subject',title:'Subject / tonal answer',location:'Alto, anacrusis and bars 1–4',text:'The four-bar phrase begins on the dominant. Its tonal answer substitutes F for the opening C, then continues a fifth higher. The end flows into semiquaver continuation rather than forming a sharply separated thematic close.'},
 {id:'cs1',title:'Countersubject',location:'Alto, bars 5–7',text:'The semiquaver line leads to a sustained note. It accompanies the early entries, continues independently after the bass subject and is subsequently divided between alto and bass. The later stretti displace it.'},
];
export const formalGroups=[
 {start:0,end:36,startQ:0,endQ:54,number:'I',label:'Exposition and counter-exposition',range:'1–36',continuation:'A · S · B; S · A · B · A'},
 {start:36,end:72,startQ:54,endQ:108,number:'II',label:'Minor-key stretti and closing development',range:'36–72',continuation:'D minor · G minor · F major'},
];
export const sections=[
 {start:0,end:17,label:'Exposition',entries:'Alto, opening upbeat · soprano, bar 4 beat 3 · bass, bar 9 beat 3',detail:'The alto continues with the countersubject beneath the tonal answer. After the intervening link, the soprano supplies it to the bass entry. Its continuation in the bass supports the upper parts’ quaver movement before the next group.'},
 {start:17,end:31,label:'Counter-exposition and first stretto',entries:'Soprano, bar 17 beat 3 · alto, bar 21 beat 3 · bass, bar 25 beat 3 · alto, bar 27 beat 3',detail:'The additional alto entry overlaps the bass at two bars’ distance. The countersubject divides between alto and bass in bars 18–20; in bar 26 its opening is inverted in the soprano. A shortened continuation accompanies the additional alto entry.'},
 {start:31,end:36,label:'Episode',entries:'Descending semiquavers in the upper parts; rising quavers in the bass',detail:'The descending semiquaver tail (d), from the subject’s third bar, passes between the upper parts. The rising quaver figure (hi) in the bass inverts the descending head motif (h). A head allusion in the bass leads to the D minor group.'},
 {start:36,end:46,label:'D minor stretto',entries:'Soprano, bar 36 beat 3 · alto, bar 38 beat 3 · bass, bar 40 beat 3',detail:'The subject descends through the three voices at two-bar intervals, in successive lower octaves. The endings adapt to the overlapping entries. A further head allusion in the soprano accompanies the bass entry before the cadence in bar 46.'},
 {start:46,end:56,label:'G minor stretto',entries:'Bass, bar 46 beat 3 · alto, bar 48 beat 3 · soprano, bar 50 beat 3',detail:'The disposition reverses: the subject now rises through the voices, again at two-bar intervals. Its third bar is ornamented, and the soprano approaches its opening note through two semiquavers. The soprano’s C♯ in bar 54 is retained.'},
 {start:56,end:64,label:'Ascending-scale development',entries:'Rising quavers in the bass, then the upper parts from bar 60',detail:'Keller relates the ascending scale to inversion of the subject’s first bar. It expands the earlier rising quaver figure and combines with the descending semiquaver tail. The scale passes into the soprano as the tonic return approaches.'},
 {start:64,end:72,label:'Closing entries',entries:'Soprano, last semiquaver of bar 64 · alto, bar 65 beat 3',detail:'The soprano shortens the upbeat and ornaments the head. The alto’s altered entry follows closely and, in Keller’s reading, expands into the closing passage. The rising quaver scale returns in the bass before the final cadence.'},
];
export const tonalEvents=[
 {id:'c8',bar:8,q:11,key:'C major',short:'C',roman:'V',type:'cadence',evidence:'The alto B rises to C beneath E in the soprano, confirming the dominant key.'},
 {id:'c17',bar:17,q:24.5,key:'C major',short:'C',roman:'V',type:'arrival',evidence:'The bass B–C and alto F–E establish C major beneath a repeated D in the soprano, which resolves to C as the bass moves onward.'},
 {id:'f21',bar:21,q:30.5,key:'F major',short:'F',roman:'I',type:'arrival',evidence:'The bass rises from E to F beneath A in the soprano, returning to tonic harmony before the alto answer.'},
 {id:'f31',bar:31,q:45.5,key:'F major',short:'F',roman:'I',type:'arrival',evidence:'The bass E–F completes F major beneath the alto A; the soprano G is held over and subsequently falls to F.'},
 {id:'d36',bar:36,q:54,key:'D minor',short:'Dm',roman:'vi',type:'entry',evidence:'The soprano begins the D minor stretto over the dominant A; this identifies the entry’s key, rather than a tonic arrival on its opening note.'},
 {id:'d46',bar:46,q:68,key:'D minor',short:'Dm',roman:'vi',type:'cadence',evidence:'The parts converge on D at the close of the first three-part stretto.'},
 {id:'g46',bar:46,q:69,key:'G minor',short:'Gm',roman:'ii',type:'entry',evidence:'The bass begins the G minor group on its dominant D. The following E♭ and F♯ distinguish this group’s minor-key form.'},
 {id:'g56',bar:56,q:83,key:'G minor',short:'Gm',roman:'ii',type:'cadence',evidence:'The parts converge on G after the second three-part stretto.'},
 {id:'f64',bar:64,q:95,key:'F major',short:'F',roman:'I',type:'arrival',evidence:'The bass E–F and alto G–A establish tonic harmony beneath the soprano’s continued G and its ensuing semiquaver figure.'},
 {id:'f72',bar:72,q:107,key:'F major',short:'F',roman:'I',type:'close',evidence:'The bass C resolves to F as the alto E rises to F, closing in tonic octaves.'},
];
