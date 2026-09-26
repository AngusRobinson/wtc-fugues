export const voices=['Soprano','Alto','Tenor','Bass'];
export const formalGroups=[
 {start:1,end:17,number:'I',label:'First half',range:'1–17',continuation:'T → A → S → B; T → A'},
 {start:18,end:34,number:'II',label:'Second half',range:'18–34',continuation:'Sᶦ → Aᶦ → B → T; A → S'},
];
export const themes=[
 {id:'subject',title:'Subject / tonal answer',location:'Subject: tenor, bars 1–3',text:'The subject begins after a quaver rest and ranges a fourth above and below B. The alto gives a tonal answer in bar 3: its opening intervals change before the rising run resumes. Later entries decorate the ending; the soprano and alto present inversions in bars 18 and 20.'},
 {id:'cs1',title:'Countersubject',location:'Tenor, bars 3–5',text:'A descending semiquaver scale turns into an upward run and a syncopated continuation. The countersubject accompanies the three later entries in the exposition and returns in the alto at bar 31. Its continuation varies; elsewhere, fragments of its opening are marked c.'},
 {id:'motif',title:'Episode figure',location:'Alto, end of bar 7',text:'Six semiquavers dip down, return, then climb. The inverted form, ei, turns up and then descends. This figure passes between the voices in the three related episodes, and the tenor recalls it just before the final chord.'},
];
export const sections=[
 {start:1,end:9,label:'Exposition',entries:'Tenor 1:1½ · alto 3:1½ · soprano 5:1½ · bass 7:1½',detail:'Subject and tonal answer alternate. The previous voice takes the countersubject, whose later continuations are adapted. The bass answer closes on F♯ at bar 9; the tenor has already fallen silent.'},
 {start:9,end:13,label:'Episode and tenor return',entries:'Episode 9–11 · subject: tenor 11:3½',detail:'The episode exchanges its three lines among soprano, alto and bass. The tenor returns on the second quaver of beat 3, repeating the subject in B major. The other voices develop the countersubject’s rhythm.'},
 {start:13,end:18,label:'Related episode and alto entry',entries:'Episode from 13:3 · subject: alto 16:1½',detail:'The episode returns with the voices redistributed. The alto subject in F♯ major decorates its long penultimate note and closes on A♯ instead of F♯. The first half reaches an F♯ major cadence at bar 18.'},
 {start:18,end:22,label:'Inverted pair',entries:'Soprano 18:1½ · alto 20:1½',detail:'The soprano turns the subject upside down in its highest register. The alto responds with an adjusted inverted form. Both endings are adapted; the bass is absent for most of this passage, leaving a three-part texture.'},
 {start:21,end:26,label:'Direct entries',entries:'Bass 21:3½ · tenor 24:1½',detail:'The bass restores the original subject before the alto’s inverted entry has finished. The tenor follows in C♯ minor, beginning on E and decorating the close. The descending bass reaches C♯2 in bar 25, before the C♯ minor cadence at bar 26.'},
 {start:26,end:29,label:'Third episode',entries:'Soprano, tenor and bass',detail:'The first episode returns with the tenor taking the earlier alto line. The semiquaver figure passes through bass, soprano and bass again, bringing the music back towards B major.'},
 {start:29,end:34,label:'Final pair and close',entries:'Subject: alto 29:1½ · tonal answer: soprano 31:1½',detail:'The countersubject returns in the alto under the last answer. After the soprano’s closing F♯, the tenor recalls the inverted episode figure. The final B major chord places D♯, the third, at the top.'},
];
export const tonalEvents=[
 {id:'fs9',bar:9,q:32,key:'F♯ major',short:'F♯',roman:'V',type:'cadence',evidence:'The bass answer resolves from G♯ to F♯, while E♯ in the soprano rises to F♯. The alto supplies A♯.'},
 {id:'b11',bar:11,q:42.5,key:'B major',short:'B',roman:'I',type:'entry',evidence:'The tenor restates the subject on B after the episode. The other voices continue moving: this marker identifies the entry’s key, rather than a tonic cadence.'},
 {id:'fs18',bar:18,q:68,key:'F♯ major',short:'F♯',roman:'V',type:'cadence',evidence:'The bass moves from C♯ to F♯. F♯ in the soprano, A♯ in the alto and C♯ in the tenor complete the tonic chord, just before the inverted subject begins.'},
 {id:'b20',bar:20,q:76,key:'B major',short:'B',roman:'I',type:'cadence',evidence:'The tenor reaches B2 and the soprano resolves E to D♯. The alto’s tied C♯ resolves to B on the second quaver, which also begins its inverted entry.'},
 {id:'cs24',bar:24,q:92.5,key:'C♯ minor',short:'C♯m',roman:'ii',type:'entry',evidence:'The tenor subject begins on E, the third of C♯ minor. Its B♯ and the subsequent G♯ dominant lead towards the cadence at bar 26; the entry itself is not a tonic chord.'},
 {id:'cs26',bar:26,q:100,key:'C♯ minor',short:'C♯m',roman:'ii',type:'cadence',evidence:'The bass G♯ resolves to C♯2 and the soprano B♯ rises to C♯. E in the tenor supplies the minor third.'},
 {id:'b29',bar:29,q:112,key:'B major',short:'B',roman:'I',type:'cadence',evidence:'The bass A♯ rises to B and the tenor reaches D♯. The soprano’s C♯ suspension resolves to B on the second quaver as the alto subject enters.'},
 {id:'b34',bar:34,q:132,key:'B major',short:'B',roman:'I',type:'close',evidence:'The bass F♯ moves to B; the alto A♯ rises to B. D♯ in the soprano and F♯ in the tenor complete the final chord.'},
];
