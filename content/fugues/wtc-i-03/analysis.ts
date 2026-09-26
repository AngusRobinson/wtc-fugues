export const voices=['Soprano','Alto','Bass'];
export const themes=[
 {id:'subject',title:'Subject / tonal answer',location:'Soprano, bars 1–3',text:'The tonal answer changes the opening G♯–A♯ second into C♯–E♯, a third. The remaining notes are transposed down a fourth. Later entries sometimes divide or decorate the opening quaver.'},
 {id:'cs1',title:'Countersubject 1',location:'Soprano, bar 3 beat 3 to bar 5',text:'The semiquaver line combines a turn, a sustained note and falling thirds. Its lead-in and cadence vary; the rolling thirds also supply much of the episodic material.'},
 {id:'cs2',title:'Countersubject 2',location:'Soprano, bar 5 beat 2 to bar 7',text:'The sustained and syncopated line first appears above the bass subject. Subject, CS1 and CS2 combine in triple counterpoint; four distinct dispositions occur in bars 5, 19, 24–26 and 26–28.'},
];
export const formalGroups=[
 {start:1,end:22,startQ:0,endQ:87,number:'I',label:'Exposition and minor entries',range:'1–22',continuation:'S · A · B; S; B · A'},
 {start:22,end:42,startQ:87,endQ:165.5,number:'II',label:'Middle entries and extended episode',range:'22–42',continuation:'S · A; outer-voice duet'},
 {start:42,end:55,startQ:165.5,endQ:220,number:'III',label:'Return of the exposition and coda',range:'42–55',continuation:'S · A · B; S'},
];
export const sections=[
 {start:1,end:7,label:'Exposition',entries:'Subject: soprano, bar 1 · tonal answer: alto, bar 3 · subject: bass, bar 5; all begin on beat 2½',detail:'CS1 passes from soprano to alto. The soprano introduces CS2 at bar 5 beat 2, just before the bass entry. The subject closes at the opening of bar 7; CS2 delays the consonant tonic until the following quaver.'},
 {start:7,end:12,label:'First episode and additional answer',entries:'Answer*: soprano, bar 10 beat 2½ · CS1: alto',detail:'The episode sets the dialogue figure (e), derived from the subject, against an inversion of the rolling-third figure (d) from CS1. The upper voices cross in imitation. The additional answer has a decorated opening; CS2 is absent.'},
 {start:12,end:22,label:'Minor-key entries',entries:'Answer form: bass, bar 14 beat 2½, A♯ minor · subject: alto, bar 19 beat 2½, E♯ minor',detail:'Bars 12–14 place the direct rolling-third figure in the soprano over the lower voices’ dialogue. The A♯ minor entry has CS1 in the soprano and no CS2. Bars 16–19 develop the end of the first episode. At bar 19, CS2 lies above the subject and CS1 below it; the ensuing cadential extension closes in E♯ minor at bar 22 beat 3.'},
 {start:22,end:28,label:'Dominant and tonic entries',entries:'Answer*: soprano, bar 24 beat 4½ · subject: alto, bar 26 beat 4½',detail:'The subject-head figure (h) is sequenced in the soprano during the two-part link. The entries restore G♯ major and C♯ major, with CS1 respectively in bass and soprano, and CS2 in alto and bass. Together with bars 5 and 19, these supply four dispositions of the three themes in triple counterpoint.'},
 {start:28,end:42,label:'Extended episode',entries:'No complete subject entry; outer-voice duet from bar 35',detail:'Bars 28–30 invert the disposition of bars 12–14, placing the rolling thirds in the bass. From bar 30 beat 3 the soprano takes their inversion while the lower parts develop the dialogue. The alto drops out after bar 34. The duet sequences the subject head in the soprano, then the bass, against a new descending figure; it runs directly into the returning subject.'},
 {start:42,end:48,label:'Return of the exposition',entries:'Subject: soprano, bar 42 · answer*: alto, bar 44 · subject: bass, bar 46; all on beat 2½',detail:'The opening entry order returns with fuller accompaniment. The bass has a variant of CS1 beneath the first entry and a variant of CS2 beneath the answer. At bar 46 the original disposition of all three themes returns. The F♯/F𝄪 differences in CS1 are retained from the edition.'},
 {start:48,end:55,label:'Episode, final subject and coda',entries:'Subject*: soprano, bar 51 beat 4½ · CS1*: alto',detail:'After the additional half-bar at the opening of bar 48, the first episode returns a fifth lower. The final subject overlaps the interrupted cadence at bar 53 beat 3. The coda recalls the subject’s disjunct quavers in the upper line; extra notes fill out the closing texture.'},
];
export const tonalEvents=[
 {id:'gs5',bar:5,q:16,key:'G♯ major',short:'G♯',roman:'V',type:'cadence',evidence:'The answer closes on G♯ beneath B♯; F𝄪 in the alto resolves to G♯.'},
 {id:'cs7',bar:7,q:24.5,key:'C♯ major',short:'C♯',roman:'I',type:'arrival',evidence:'The bass reaches C♯ at beat 1, but the soprano retains D♯. Its move to G♯ on the next quaver completes C♯–E♯–G♯.'},
 {id:'gs12',bar:12,q:44,key:'G♯ major',short:'G♯',roman:'V',type:'cadence',evidence:'The additional answer ends over G♯ in the bass, with B♯ in the alto.'},
 {id:'ds14',bar:14,q:52,key:'D♯ minor',short:'D♯m',roman:'ii',type:'cadence',evidence:'C𝄪 in the approach leads to D♯ octaves under F♯. This local cadence precedes the entry directed towards A♯ minor.'},
 {id:'as14',bar:14,q:53.5,key:'A♯ minor',short:'A♯m',roman:'vi',type:'entry',evidence:'The bass uses the answer form, beginning on D♯ and closing in A♯ minor at bar 16.'},
 {id:'as16',bar:16,q:60,key:'A♯ minor',short:'A♯m',roman:'vi',type:'cadence',evidence:'The entry closes on A♯ in the bass beneath C♯. G𝄪 in the preceding bass line supplies the leading note.'},
 {id:'es19',bar:19,q:73.5,key:'E♯ minor',short:'E♯m',roman:'iii',type:'entry',evidence:'The alto subject begins on B♯, the dominant of E♯ minor; the group receives a full cadential close in bar 22.'},
 {id:'es22',bar:22,q:86,key:'E♯ minor',short:'E♯m',roman:'iii',type:'cadence',evidence:'The B♯ dominant resolves to E♯–G♯–E♯ at beat 3. The soprano leading note D𝄪 resolves into the tonic.'},
 {id:'gs26',bar:26,q:102,key:'G♯ major',short:'G♯',roman:'V',type:'cadence',evidence:'The soprano answer closes on G♯ above D♯ and B♯: a first-inversion tonic in G♯ major.'},
 {id:'cs28',bar:28,q:110,key:'C♯ major',short:'C♯',roman:'I',type:'cadence',evidence:'G♯ in the bass moves to C♯ beneath the alto’s closing C♯ and the soprano’s E♯.'},
 {id:'cs42',bar:42,q:165.5,key:'C♯ major',short:'C♯',roman:'I',type:'entry',evidence:'The subject returns in the tonic form, but begins over D♯ in the bass; this marker identifies the entry’s key, not a tonic chord at its onset.'},
 {id:'cs44',bar:44,q:172,key:'C♯ major',short:'C♯',roman:'I',type:'cadence',evidence:'The returning subject closes on C♯ over E♯ in the bass, a first-inversion tonic.'},
 {id:'gs46',bar:46,q:180,key:'G♯ major',short:'G♯',roman:'V',type:'cadence',evidence:'The answer ends on G♯, doubled in the bass, below B♯ in the soprano.'},
 {id:'as53',bar:53,q:210,key:'A♯ minor',short:'A♯m',roman:'vi',type:'cadence',evidence:'The dominant moves to A♯ in the bass under C♯ and E♯: an interrupted cadence in C♯ major, not a new modulation to A♯ minor.'},
 {id:'cs55',bar:55,q:218,key:'C♯ major',short:'C♯',roman:'I',type:'close',evidence:'The bass G♯ resolves to C♯ at beat 3; the additional upper notes complete the C♯ major chord.'},
];
