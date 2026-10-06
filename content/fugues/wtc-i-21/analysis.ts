export const voices=['Soprano','Alto','Bass'];
export const themes=[
 {id:'subject',title:'Subject / tonal answer',location:'Soprano, bars 1–5',text:'A four-bar phrase, articulated a–a–b–b, resolves on D in bar 5. The answer is tonal: its first and third notes are B♭ rather than the C of a real transposition; the remainder transposes down a fourth. The subject itself is never inverted as a whole.'},
 {id:'cs1',title:'First countersubject',location:'Soprano, bars 5–9',text:'The subject’s closing D also begins the accompaniment. The opening semiquavers lead into two syncopated phrases and repeated quavers. This countersubject recurs with adapted openings in triple counterpoint with the subject and second countersubject.'},
 {id:'cs2',title:'Second countersubject',location:'Soprano, bars 9–13',text:'Short semiquaver figures, separated by rests, complete the three-part combination. Four of its six possible vertical dispositions occur. The episodic continuations retain recognisable parts of both countersubjects.'},
];
export const formalGroups=[
 {start:1,end:22,startQ:0,endQ:63.5,number:'I',label:'Exposition, additional answer and episode',range:'1–22',continuation:'S · A · B · S'},
 {start:22,end:48,startQ:63.5,endQ:144,number:'II',label:'Two paired groups and coda',range:'22–48',continuation:'A / B · S / A'},
];
export const sections=[
 {start:1,end:13,label:'Exposition',entries:'Soprano, bar 1 · alto, bar 5 · bass, bar 9',detail:'Each entry begins on the second quaver. The first countersubject accompanies the alto; the second appears in the soprano against the bass entry, completing the triple counterpoint.'},
 {start:13,end:17,label:'Additional answer',entries:'Soprano, bar 13, second quaver',detail:'The answer rises above the first countersubject in the bass and second countersubject in the alto. The three materials invert their previous disposition. The final A continues directly into the episode.'},
 {start:17,end:22,label:'First episode',entries:'Sequential continuation, then two voices',detail:'The semiquaver tail (b) continues in the soprano; the two countersubjects invert their positions below it. From bar 19, the bass introduces the inverted quaver head (ai). The five-bar span ends on the dominant of G minor.'},
 {start:22,end:30,label:'First pair',entries:'Alto, bar 22 · bass, bar 26',detail:'The alto gives the subject in G minor, followed by the bass’s tonal answer-form leading into C minor. Both entries retain the two countersubjects. Their openings adapt to the preceding continuation.'},
 {start:30,end:35,label:'Second episode',entries:'Inverted head above the semiquaver tail',detail:'The soprano takes the inverted quaver head over the bass’s semiquaver sequence. In bars 33–34 the semiquavers return to the soprano, above paired quaver lines. This is a free inversion and extension of the earlier episodic material.'},
 {start:35,end:37,label:'Incomplete answer',entries:'Alto, bar 35, second quaver',detail:'Only the first two bars of the answer are given. The accompanying countersubjects prepare the next complete entry. Following Keller, this passage is distinguished from a full statement.'},
 {start:37,end:45,label:'Second pair',entries:'Soprano, bar 37 · alto, bar 41',detail:'The soprano gives the subject in E♭ major; the alto’s answer-form returns to B♭ major. The first entry places the first countersubject in the alto and second in the bass, adding the fourth vertical disposition of the triple counterpoint.'},
 {start:45,end:48,label:'Coda',entries:'Subject tail in the alto',detail:'Bars 45–46 invert the material of bars 43–44: the alto retains the semiquaver tail, the bass takes the repeated quavers and the soprano the second countersubject. The final cadence follows in bar 48.'},
];
export const tonalEvents=[
 {id:'f9',bar:9,q:24.5,key:'F major',short:'F',roman:'V',type:'cadence',evidence:'F in the entering bass completes A–C in the upper parts at the end of the tonal answer.'},
 {id:'bb13',bar:13,q:36,key:'B♭ major',short:'B♭',roman:'I',type:'cadence',evidence:'The subject resolves to D in the bass beneath F and B♭.'},
 {id:'f17',bar:17,q:48,key:'F major',short:'F',roman:'V',type:'cadence',evidence:'The bass reaches F beneath F and A, closing the additional answer.'},
 {id:'gd22',bar:22,q:63,key:'D major',short:'D',roman:'III',type:'arrival',evidence:'D in the bass and F♯ in the soprano close the descending sequence on the dominant of G minor.'},
 {id:'g26',bar:26,q:75,key:'G minor',short:'Gm',roman:'vi',type:'cadence',evidence:'G in the bass supports B♭ and D at the end of the alto subject.'},
 {id:'c30',bar:30,q:87,key:'C minor',short:'Cm',roman:'ii',type:'cadence',evidence:'The bass resolves to E♭ beneath G and C, closing the answer in first inversion.'},
 {id:'c35',bar:35,q:102,key:'C minor',short:'Cm',roman:'ii',type:'cadence',evidence:'C in bass and alto supports E♭ in the soprano after the chromatic sequence.'},
 {id:'eb37context',bar:37,q:108.5,key:'E♭ major',short:'E♭',roman:'IV',type:'entry',evidence:'The soprano entry is in E♭; its opening is not marked as an independent cadence.'},
 {id:'eb41',bar:41,q:120,key:'E♭ major',short:'E♭',roman:'IV',type:'cadence',evidence:'E♭ in the bass supports B♭ and G as the soprano subject closes.'},
 {id:'bb45',bar:45,q:132,key:'B♭ major',short:'B♭',roman:'I',type:'cadence',evidence:'B♭ in the bass supports D and F at the alto answer’s close.'},
 {id:'bb48',bar:48,q:141,key:'B♭ major',short:'B♭',roman:'I',type:'close',evidence:'The final F dominant resolves to B♭ in the outer parts and D in the alto.'},
];
