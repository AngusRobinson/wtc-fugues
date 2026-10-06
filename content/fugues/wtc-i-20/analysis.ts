export const voices=['Soprano','Alto','Tenor','Bass','Pedal'];
export const themes=[
 {id:'subject',title:'Subject / real answer',location:'Alto, bars 1–4',text:'A lower-neighbour figure leads through rising sequences to F, then drops a seventh to G♯. The detached third G♯–E interrupts the motion before the semiquaver continuation closes in A minor. The soprano’s real answer transposes the subject up a fifth.'},
 {id:'cs1',title:'Exposition countersubject',location:'Alto, bars 4–7',text:'Descending quavers frame a development of the subject’s semiquaver figure. The opening accompanies the bass entry an octave higher, with an altered continuation, and returns with the tenor answer. Its scale component persists after the exposition; a fixed complete countersubject does not.'},
];
export const formalGroups=[
 {start:1,end:14,startQ:0,endQ:54.5,number:'I',label:'Exposition',range:'1–14',continuation:'Alto · soprano · bass · tenor'},
 {start:14,end:27,startQ:54.5,endQ:106.5,number:'II',label:'Inverted entries',range:'14–27',continuation:'Soprano · tenor · bass · alto'},
 {start:27,end:43,startQ:106.5,endQ:168.5,number:'III',label:'Direct octave stretti',range:'27–43',continuation:'Three pairs; episode 39–42'},
 {start:43,end:65,startQ:168.5,endQ:260,number:'IV',label:'Octave stretti',range:'43–65',continuation:'Overlaps group V'},
 {start:64,end:73,startQ:254.5,endQ:288.5,number:'V',label:'Fifth stretti',range:'64–73',continuation:'Both forms'},
 {start:73,end:87,startQ:288.5,endQ:348,number:'VI',label:'Mixed stretti',range:'73–87',continuation:'Five parts from bar 80'},
];
export const sections=[
 {start:1,end:14,label:'Exposition',entries:'Alto, bar 1 · soprano, bar 4 · bass, bar 8 · tenor, bar 11',detail:'All four entries begin on the second quaver. A one-bar link separates the first pair from the bass entry. The countersubject begins in the alto at bar 4 beat 2; its descending scale figure (d) returns in the soprano with the bass subject and in the alto with the tenor answer. Parallel thirds in the upper voices intensify bars 11–12.'},
 {start:14,end:27,label:'Inverted entries',entries:'Soprano, bar 14 beat 3½ · tenor, bar 18 beat 1½ · bass, bar 21 beat 1½ · alto, bar 24 beat 1½',detail:'The inverted subject turns the original downward seventh into an upward seventh. Tonal adaptation changes its intervals and cadential tails. In bars 15–16, the ascending scale figure (di) passes between alto and tenor above its descending form in the bass. An anticipatory subject-head figure (h) in the alto, bar 17, precedes the actual tenor entry.'},
 {start:27,end:39,label:'Direct octave stretti',entries:'Soprano/tenor, bars 27–28 · alto/bass, bars 31–32 · tenor/alto, bars 36–37',detail:'Each follower enters two crotchets after the leader. The first two pairs place the follower an octave below; the third inverts their disposition, with the follower an octave above. A minor, E minor and A minor provide the principal contexts. Head fragments between the pairs are not additional full entries.'},
 {start:39,end:42,label:'Episode',entries:'Descending sequence, then imitation in the inner voices',detail:'The subject-tail figure (t) passes from tenor to alto in bars 41–42 and continues in the bass. The soprano rests through the episode. The passage prepares C major and the next stretto group.'},
 {start:43,end:47,label:'Major-mode octave stretto',entries:'Soprano and bass, bar 43, beats 1½ and 3½',detail:'The subject appears in C major; the bass follows two octaves below at the established half-bar distance. The free parts take up fragments of the semiquaver continuation.'},
 {start:48,end:60,label:'Inverted octave stretti',entries:'Alto/tenor, bars 48–49 · bass/soprano, bar 53 · soprano/alto, bars 57–58',detail:'The same half-bar spacing now governs the inverted subject. The octave relationship is expanded across the outer voices in bar 53. In bar 59 the alto changes the subject’s upward third into F♯–B, a fourth. The altered tails continue the sequence beyond the thematic core.'},
 {start:61,end:65,label:'Transition and overlap',entries:'Bass and tenor fragments, bars 62–63',detail:'An incomplete inverted stretto leads towards D minor. The upper voices continue across the first entry of group V, then fall silent in bar 65. Keller’s formal groups overlap at this point.'},
 {start:64,end:70,label:'Fifth stretti',entries:'Bass/tenor, bars 64–65 · soprano/alto, bars 67–68',detail:'The direct subject in the bass is followed a fifth above by the tenor. The soprano’s inverted subject overlaps their endings; the alto follows a fifth below. These dispositions arise from double counterpoint at the twelfth: the earlier lower-octave follower becomes an upper-fifth follower, with tonal adjustments.'},
 {start:70,end:72,label:'Transition to F major',entries:'Cadential extension after the inverted pair',detail:'The dense thematic combination relaxes into a sequential passage. A cadence in F major at bar 72 beat 3½ prepares the last formal group.'},
 {start:73,end:79,label:'Inverted and mixed stretti',entries:'Bass/alto, bar 73 · tenor, bar 76 · alto and soprano, bar 77',detail:'The bass and alto give the inverted subject two octaves apart. The tenor’s next inverted entry receives a direct response a bar later, a ninth above, in the alto. The soprano adds a third entry two crotchets later, then deflects its continuation into a descending sequence.'},
 {start:80,end:83,label:'Coda: interrupted cadences',entries:'Alto, bar 80 beat 3½ · soprano, bar 81 beat 1½',detail:'The first fermata arrests the texture on E7/D. Chordal support and a fifth-stretto fragment lead to a second pause on B7/F♯ in bar 82. The return to A minor clears the way for the tonic pedal from bar 83 beat 3.'},
 {start:83,end:87,label:'Pedal and final mixed stretto',entries:'Inverted bass/tenor, bars 83–84 · direct soprano/alto, bars 84–85',detail:'Four subject fragments accumulate above the sustained pedal, paired in contrary motion. The tenor changes register within its fragment; the upper continuations expand into chords. The final cadence is in A major. The long pedal is retained in both scores; sustaining it may require a pedal-board or an additional player.'},
];
export const tonalEvents=[
 {id:'a8',bar:8,q:28,key:'A minor',short:'Am',roman:'i',type:'cadence',evidence:'The link closes on A in the alto and C in the soprano, before the bass subject.'},
 {id:'e11',bar:11,q:42,key:'E minor',short:'Em',roman:'v',type:'arrival',evidence:'The answer is supported by E in alto and bass and G in the soprano.'},
 {id:'e14',bar:14,q:54,key:'E major',short:'E',roman:'V',type:'cadence',evidence:'The exposition ends on E with G♯ in the alto; this dominant close precedes the first inverted entry.'},
 {id:'g18',bar:18,q:68,key:'G major',short:'G',roman:'VII',type:'cadence',evidence:'The first inverted entry leads to G, B and D at the bar line.'},
 {id:'d20',bar:20,q:79.5,key:'D minor',short:'Dm',roman:'iv',type:'cadence',evidence:'The tenor reaches D over A and F before the next inverted entry.'},
 {id:'c23',bar:23,q:91,key:'C major',short:'C',roman:'III',type:'entry',evidence:'The bass inversion moves from D minor towards C major. The local C harmony is followed immediately by its seventh and a move towards F; this is a tonal context, not an independent cadence.'},
 {id:'a27',bar:27,q:106,key:'A minor',short:'Am',roman:'i',type:'cadence',evidence:'The leading-note harmony resolves onto A in both outer voices, with C in the tenor.'},
 {id:'e35',bar:35,q:136,key:'E minor',short:'Em',roman:'v',type:'cadence',evidence:'The bass subject closes on E beneath E and G in the upper voices.'},
 {id:'c43',bar:43,q:168.5,key:'C major',short:'C',roman:'III',type:'arrival',evidence:'The preceding dominant resolves to C, E and G as the soprano enters.'},
 {id:'c48',bar:48,q:188,key:'C major',short:'C',roman:'III',type:'cadence',evidence:'The major-mode stretto and its continuation close on C, E and G.'},
 {id:'d64',bar:64,q:254.5,key:'D minor',short:'Dm',roman:'iv',type:'arrival',evidence:'D, F and A support the new bass entry at the end of the preceding inverted fragments.'},
 {id:'a67',bar:67,q:266.5,key:'A minor',short:'Am',roman:'i',type:'arrival',evidence:'The bass moves to A under C and the soprano’s E as the inverted pair begins.'},
 {id:'f72',bar:72,q:286.5,key:'F major',short:'F',roman:'VI',type:'cadence',evidence:'The sequence resolves to F, A and C before the final formal group.'},
 {id:'g76',bar:76,q:300,key:'G minor',short:'Gm',roman:'vii',type:'cadence',evidence:'F♯ in the bass resolves to a sustained G under B♭ and D.'},
 {id:'a83',bar:83,q:328,key:'A minor',short:'Am',roman:'i',type:'cadence',evidence:'The post-fermata continuation reaches A with C and E.'},
 {id:'am83',bar:83,q:330,key:'A major',short:'A',roman:'I',type:'arrival',evidence:'The tonic pedal begins under C♯ and E; minor-mode thematic fragments follow above it.'},
 {id:'a87',bar:87,q:346,key:'A major',short:'A',roman:'I',type:'close',evidence:'The final moving voices reach the major tonic over the retained pedal and soprano A.'},
];
