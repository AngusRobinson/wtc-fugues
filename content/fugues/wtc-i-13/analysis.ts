export const voices=['Soprano','Alto','Bass'];
export const themes=[
 {id:'subject',title:'Subject / tonal answer',location:'Soprano, bars 1–3',text:'The two-bar subject ends on the third of the tonic chord. Its tonal answer begins on F♯ instead of G♯, then continues a fifth higher, placed an octave lower. The internal rest divides related halves: the opening four-quaver figure returns in a different order at the close.'},
 {id:'cs1',title:'Main countersubject',location:'Soprano, bars 3–5',text:'Semiquaver figures expand and repeat the subject’s descending line before returning to its opening intervals. Later appearances change the opening and cadence. In bars 15–16 and 31–32, its central passage is inverted against the subject in double counterpoint at the twelfth.'},
 {id:'cs2',title:'Additional countersubject',location:'Bass, bars 12–13',text:'The semiquaver figure from the first episode is inverted and extended into an ascending line above a repeated note. It returns in the soprano against the bass entry in D♯ minor and the alto entry in B major.'},
];
export const formalGroups=[
 {start:1,end:22,startQ:0,endQ:88,number:'I',label:'Exposition and second entry group',range:'1–22',continuation:'S · A · B; S · A · B'},
 {start:23,end:35,startQ:88,endQ:140,number:'II',label:'Head-motif development and closing entries',range:'23–35',continuation:'Episode; A · S; coda'},
];
export const sections=[
 {start:1,end:7,label:'Exposition',entries:'Soprano, bar 1 beat 1½ · alto, bar 3 beat 1½ · bass, bar 5 beat 1½',detail:'The main countersubject passes from soprano to alto. The bass entry substitutes a tonic ending for the subject’s original third. The head motif (a) and descending line provide the principal thematic material.'},
 {start:7,end:11,label:'First episode',entries:'Semiquaver figure (e) in soprano, bass and alto',detail:'The new episodic semiquaver figure combines with derived quaver material. Keller identifies a reordering of the head in the bass at bar 7. The episode moves to the dominant before the next soprano entry.'},
 {start:11,end:13,label:'Soprano entry',entries:'Soprano, bar 11 beat 3½, in F♯ major',detail:'The alto gives the main countersubject below the subject. From bar 12, the bass introduces the additional countersubject, derived by inversion from the first episode’s semiquaver figure.'},
 {start:13,end:15,label:'Head-motif episode',entries:'Imitation of the four-quaver head motif',detail:'The short passage works the subject’s head without complete entries. Its imitative arrangement returns near the close.'},
 {start:15,end:17,label:'Dominant entry',entries:'Alto, bar 15 beat 1½, in C♯ major',detail:'The main countersubject’s central passage lies in the bass, a twelfth below its position against the opening answer. The soprano supplies a freer line. The entry closes in C♯ major.'},
 {start:17,end:20,label:'Episode',entries:'Return of the episodic semiquaver figure',detail:'The first episode’s material recurs in a higher register and passes through A♯ minor towards D♯ minor. The bass then begins the subject on A♯.'},
 {start:20,end:23,label:'Relative-minor entry and cadence',entries:'Bass, bar 20 beat 1½',detail:'The soprano gives the additional countersubject; the alto retains only a fragment of the main one. The subject adapts its descending line to the minor key and ends on D♯. A further cadence completes Keller’s first part.'},
 {start:23,end:28,label:'Extended episode',entries:'Head motif in the upper voices; semiquaver figure in the bass',detail:'The head motif is developed without a complete subject entry. The semiquaver figure subsequently moves above a sequential bass line as the harmony approaches B major.'},
 {start:28,end:30,label:'Subdominant entry',entries:'Alto, bar 28 beat 1½, in B major',detail:'The soprano gives the additional countersubject above a sustained B in the bass. The main countersubject is absent.'},
 {start:30,end:31,label:'Head-motif episode',entries:'Imitation between alto and soprano',detail:'The short episode recalls bars 13–15 with the upper voices inverted and redirects the harmony to F♯ major.'},
 {start:31,end:35,label:'Final entry and coda',entries:'Soprano, bar 31 beat 3½',detail:'The main countersubject returns in the bass. The combination recalls bars 15–17 transposed to the tonic, with the former alto subject now above the accompanying upper line. The coda recalls the first episode and closes in F♯ major.'},
];
export const tonalEvents=[
 {id:'cs5',bar:5,q:16,key:'C♯ major',short:'C♯',roman:'V',type:'cadence',evidence:'The soprano B♯ resolves to C♯ as the answer closes on E♯.'},
 {id:'fs7',bar:7,q:24,key:'F♯ major',short:'F♯',roman:'I',type:'cadence',evidence:'The bass C♯–F♯ and alto E♯–F♯ close beneath A♯ in the soprano.'},
 {id:'cs11',bar:11,q:42,key:'C♯ major',short:'C♯',roman:'V',type:'cadence',evidence:'The bass G♯–C♯ and alto D♯–E♯ close with C♯ in the soprano.'},
 {id:'cs17',bar:17,q:64,key:'C♯ major',short:'C♯',roman:'V',type:'cadence',evidence:'The bass G♯–C♯ resolves beneath E♯ and C♯ in the upper voices.'},
 {id:'as18',bar:18,q:68,key:'A♯ minor',short:'A♯m',roman:'iii',type:'arrival',evidence:'The bass E♯ resolves to A♯ and the alto G double sharp rises to A♯ beneath C♯.'},
 {id:'ds20',bar:20,q:77,key:'D♯ minor',short:'D♯m',roman:'vi',type:'arrival',evidence:'After A♯ dominant harmony, the bass reaches D♯ beneath F♯ in the alto.'},
 {id:'ds22',bar:22,q:84.25,key:'D♯ minor',short:'D♯m',roman:'vi',type:'cadence',evidence:'The bass and soprano reach D♯ at the bar line; the alto G♯ resolves to F♯ a semiquaver later.'},
 {id:'ds23',bar:23,q:88,key:'D♯ minor',short:'D♯m',roman:'vi',type:'cadence',evidence:'The bass A♯–D♯ and alto C double sharp–D♯ close in octaves at the division between Keller’s two parts.'},
 {id:'b28',bar:28,q:110.25,key:'B major',short:'B',roman:'IV',type:'arrival',evidence:'Over B in alto and bass, the soprano E resolves to D♯.'},
 {id:'b30',bar:30,q:116,key:'B major',short:'B',roman:'IV',type:'cadence',evidence:'The soprano A♯–B closes above the bass B and alto D♯.'},
 {id:'fs33',bar:33,q:130,key:'F♯ major',short:'F♯',roman:'I',type:'cadence',evidence:'The bass C♯–F♯ and alto E♯–F♯ close beneath the subject’s A♯.'},
 {id:'fs35',bar:35,q:136,key:'F♯ major',short:'F♯',roman:'I',type:'close',evidence:'The final dominant resolves to F♯ with A♯ in the alto.'},
];
