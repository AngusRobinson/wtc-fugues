export const voices=['Soprano','Alto','Bass'];
export const formalGroups=[
 {start:1,end:19,number:'I',label:'Exposition',range:'1–19',continuation:'S → A → B; first episode'},
 {start:20,end:37,number:'II',label:'Inversion',range:'20–37',continuation:'Aᶦ → Sᶦ → Bᶦ; second episode'},
 {start:38,end:50,number:'III',label:'Minor entries',range:'38–50',continuation:'S → Aᶦ in E minor'},
 {start:51,end:69,endQ:205.5,number:'IV',label:'Stretti',range:'51–69:2',continuation:'S → B; A → S'},
 {start:69,end:86,startQ:205.5,number:'V',label:'Final group',range:'69:2–86',continuation:'Bᶦ; Aᶦ → Bᶦ → S; coda'},
];
export const themes=[
 {id:'subject',title:'Subject / real answer',location:'Subject: soprano, bars 1–5',text:'The real answer enters in the alto at bar 5. The subject combines a turning semiquaver figure with two rising sevenths, reaching C and E above the dominant. Inverted entries begin at bar 20; the later stretti omit one or both of the leap-bars.'},
 {id:'cs1',title:'Countersubject',location:'Soprano, from 6:2',text:'A rising semiquaver sequence leads to a descending turn and a suspension. The countersubject accompanies the exposition and returns inverted with the inverted subject. Later statements are abridged; it is absent from the stretti.'},
 {id:'motif',title:'Episode: triple counterpoint',location:'Soprano, alto and bass, bars 17–19',text:'The rising-third figure (p), slower line (q) and semiquaver figure (r) form triple counterpoint. Their order from top to bottom is p–q–r here, r–q–p at 31, q–p–r at 48 and r–p–q at 65. The slower line is varied. The semiquaver figure originates in the codetta, bars 9–10; the scale figure (d) joins it at 34.'},
];
export const sections=[
 {start:1,end:15,label:'Exposition',entries:'Subject: soprano 1 · real answer: alto 5 · subject: bass 11',detail:'The countersubject enters in the soprano at 6:2 and in the alto at 12:2. The two-part codetta at 9–10 introduces the semiquaver figure and its inversion before the bass enters.'},
 {start:15,end:19,label:'Episode 1',entries:'Triple counterpoint: p–q–r, bars 17–19',detail:'The codetta material passes into the bass. At 17 the three episode lines form a descending sequence, leading to the inverted entry at 20.'},
 {start:20,end:31,label:'Counter-exposition',entries:'Inverted subject: alto 20 · soprano 24 · bass 28',detail:'The inverted countersubject accompanies in bass, alto and soprano respectively. The first two subjects adjust their endings; the bass omits the final bar. The music cadences in D major at 25 before returning towards G.'},
 {start:31,end:37,label:'Episode 2',entries:'Triple counterpoint: r–q–p, bars 31–33',detail:'Soprano and bass invert the disposition of the first episode; the alto’s slower line is detached. At 34–37 the scale figure and semiquaver figure pass between the outer voices, with both melodic and contrapuntal inversion.'},
 {start:38,end:47,label:'E minor pair',entries:'Subject: soprano 38 · inverted subject: alto 43',detail:'The alto takes the abridged countersubject at 40; the soprano gives its inversion at 44:2. After its last note at 40 the bass is absent until 47. The alto subject omits its final bar; the episode begins at 46.'},
 {start:48,end:59,label:'Episode 3 and first stretto',entries:'Triple counterpoint: q–p–r, 48–50 · soprano 51 · bass 52',detail:'The slower episode line rises to the soprano. In B minor, soprano and bass omit the subject’s second bar; the bass breaks off after the remaining leap-bar. Episode 4, from 54, develops the codetta’s semiquaver figure.'},
 {start:60,end:69,label:'Second stretto and episode 5',entries:'Subject: alto 60:2 · soprano 61:2 · triple counterpoint: r–p–q, 65–67',detail:'The lower voice now leads in D major. Its shortened subject reaches its closing note; the soprano omits both leap-bars and adapts the close. In the following episode the slower line moves to the bass and is rhythmically varied.'},
 {start:69,end:76,label:'Inverted bass and episode 6',entries:'Inverted subject: bass 69:2 · countersubject: alto 70',detail:'The tonic-region return begins with a curtailed inverted subject. Bars 73–76 recall the scale and semiquaver figures from 34–37, with their positions and directions altered.'},
 {start:77,end:86,label:'Final stretto and coda',entries:'Inverted entries: alto 77 · bass 78 · direct subject: soprano 79',detail:'The alto breaks off; the bass sequences the inverted head. The soprano enters a third above the original pitch and continues freely, with the alto initially in parallel thirds. The coda begins at 82. A G major cadence at 83 leads to the tonic pedal and added voices of 84–86.'},
];
export const tonalEvents=[
 {id:'d10',bar:10,q:27,key:'D major',short:'D',roman:'V',type:'cadence',evidence:'The alto’s C♯ rises to D as the soprano’s G resolves to F♯: a two-part D major cadence within the codetta.'},
 {id:'g20',bar:20,q:57,key:'G major',short:'G',roman:'I',type:'arrival',evidence:'The descending episode reaches B in the bass and G in the soprano. The inverted subject begins on D in the alto over this first-inversion tonic.'},
 {id:'d25',bar:25,q:72,key:'D major',short:'D',roman:'V',type:'cadence',evidence:'The bass moves from A to D, the alto’s C♯ resolves to D and the soprano reaches F♯. The cadence overlaps the inverted answer.'},
 {id:'e39',bar:39,q:114,key:'E minor',short:'Em',roman:'vi',type:'cadence',evidence:'The E minor subject begins at 38 over G in the bass. At 39 the bass moves from B to E while the soprano reaches G, confirming E minor.'},
 {id:'b51',bar:51,q:150,key:'B minor',short:'Bm',roman:'iii',type:'arrival',evidence:'D in the bass, B in the alto and F♯ in the soprano form a first-inversion B minor tonic. The soprano subject follows one semiquaver later.'},
 {id:'d60',bar:60,q:178.5,key:'D major',short:'D',roman:'V',type:'cadence',evidence:'The bass C♯ rises to D as the alto enters on D and the soprano reaches F♯. This tonic arrival begins the second stretto on beat 2.'},
 {id:'g69',bar:69,q:205.5,key:'G major',short:'G',roman:'I',type:'entry',evidence:'The bass restores the inverted subject on D, in the form previously heard in the tonic region. The onset is a bare D octave; the marker identifies the entry context, not a G major cadence.'},
 {id:'g83',bar:83,q:246,key:'G major',short:'G',roman:'I',type:'cadence',evidence:'The bass moves from D to G, the soprano’s F♯ rises to G and the alto reaches B. The subsequent tonic pedal supports the expanded closing texture.'},
];
