export const voices = ['Soprano','Alto','Tenor','Bass'];
// Prout's five principal groups; the spans include their following links/episodes.
export const formalGroups = [
 {start:1,end:26,number:'I',label:'Exposition',range:'1–21',continuation:'Episode 21–26'},
 {start:27,end:41,number:'II',label:'Direct stretto',range:'27–37',continuation:'Episode 37–41'},
 {start:42,end:66,number:'III',label:'Inverted entries',range:'42–62',continuation:'Episode 62–66'},
 {start:67,end:79,number:'IV',label:'Inverted stretto',range:'67–77',continuation:'Link 78–79'},
 {start:80,end:101,number:'V',label:'Mixed forms',range:'80–101',continuation:'Episode 84–88 · coda from 93'}
];
export const sections = [
 {start:1,end:26,label:'Exposition and episode',entries:'A 1 · S 5 · B 11 · T 17',detail:'Exposition through bar 21; sequential continuation in bars 21–26. CS1 remains in the alto at bar 11, while CS2 enters in the soprano.'},
 {start:27,end:41,label:'Stretto: rectus',entries:'T → A 27 · S → B 33',detail:'Imitation at the upper seventh (bar 27) and lower ninth (bar 33). The two pairs reverse the vertical disposition of the counterpoint.'},
 {start:42,end:66,label:'Inverted entries and episode',entries:'T 42 · A 46 · S 52 · B 58',detail:'Successive inverted entries in all four voices. CS1 is also inverted, with omissions and altered continuations; bars 62–66 form the intervening sequence.'},
 {start:67,end:79,label:'Stretto: inversus',entries:'T → S 67 · A → B 73',detail:'The inverted subject is imitated at the upper ninth and lower seventh. The one-minim entry interval is retained.'},
 {start:80,end:95,label:'Stretto: mixed forms',entries:'Sⁱ → T 80 · B → Aⁱ 89',detail:'Each pair combines rectus and inversus. The intervening passage passes through E♭ minor before the B♭ minor return at bar 89. Prout places the start of the coda at bar 93.'},
 {start:96,end:101,label:'Paired stretto within the coda',entries:'S + A 96.1 · Tⁱ + Bⁱ 96.2',detail:'Soprano and alto enter in parallel sixths; tenor and bass follow one minim later in inversion, in thirds. The closing chord has D♮.'}
];
export const themes = [
 {id:'subject',title:'Subject / real answer',location:'Subject: alto, bars 1–5',text:'The real answer enters in the soprano at bar 5, a perfect fifth higher, with A♮ replacing A♭ at its close. The bass entry likewise closes on D♮. The quaver continuation and closing cell s also occur outside complete entries.'},
 {id:'cs1',title:'Countersubject 1',location:'Alto, bars 5–9',text:'Two chromatic ascents (c1), followed by a sustained note and the turn/suspension figure t1. The alto repeats CS1 at bar 11; inverted versions accompany the entries from bar 42.'},
 {id:'cs2',title:'Countersubject 2',location:'Soprano, bars 11–15',text:'Keller’s second counterpoint; Prout identifies only the chromatic countersubject. The crotchet–rest cell c2 coincides with the subject’s quaver continuation. Later variants and detached cells are marked separately.'}
];
// Locations are crotchet offsets from the first bar. Evidence refers to the score,
// distinguishing entry context, tonic harmony, cadential arrival and final mode.
export const tonalEvents = [
 {id:'f7',bar:7,q:36,key:'F minor',short:'Fm',roman:'v',type:'arrival',evidence:'The answer starts at bar 5. E♮–G at the end of bar 6 resolves to F–A♭ at bar 7. The implied C dominant resolves to the F minor tonic.'},
 {id:'bb11',bar:11,q:60,key:'B♭ minor',short:'B♭m',roman:'i',type:'entry',evidence:'The bass restates the B♭ minor subject at bar 11. This marks the thematic return; the chromatic alto counterpoint initially introduces D♮.'},
 {id:'f17',bar:17,q:96,key:'F minor',short:'Fm',roman:'v',type:'arrival',evidence:'E♮ and B♭ in the approach give way to F–A♭–C at bar 17. The tonic arrives in first inversion under the tenor answer.'},
 {id:'db25',bar:25,q:144,key:'D♭ major',short:'D♭',roman:'III',type:'cadence',evidence:'The sequence in bars 21–24 reaches A♭–C–E♭, then D♭ in the bass at bar 25. The soprano’s E♭ resolves to D♭.'},
 {id:'bb27',bar:27,q:156,key:'B♭ minor',short:'B♭m',roman:'i',type:'cadence',evidence:'The F dominant at the end of bar 26 resolves to B♭ at bar 27. The soprano’s C resolves to B♭ as the tenor begins the stretto.'},
 {id:'db33',bar:33,q:192,key:'D♭ major',short:'D♭',roman:'III',type:'arrival',evidence:'After the two-part link in bars 31–32, D♭–F supports the soprano entry at bar 33. The bass follows at the lower ninth.'},
 {id:'bb42',bar:42,q:246,key:'B♭ minor',short:'B♭m',roman:'i',type:'cadence',evidence:'F and A♮ in the approach resolve to B♭–D♭–F at bar 42, coinciding with the first inverted entry.'},
 {id:'eb48',bar:48,q:282,key:'E♭ minor',short:'E♭m',roman:'iv',type:'arrival',evidence:'The inverted alto entry begins at bar 46 over a B♭ tonic. D♮ in bar 47 leads to E♭–G♭–B♭ at bar 48; the E♭ minor cadence is reiterated at bar 50.'},
 {id:'gb54',bar:54,q:318,key:'G♭ major',short:'G♭',roman:'VI',type:'arrival',evidence:'The soprano entry at bar 52 begins over D♭. G♭–B♭–D♭ is reached at bar 54, followed by the D♭ dominant with C♭ and F♮ in bar 55.'},
 {id:'ab60',bar:60,q:354,key:'A♭ minor',short:'A♭m',roman:'vii',type:'arrival',evidence:'The bass entry begins at bar 58. A♭–C♭–E♭ is stated at bar 60, initially over C♭ and then over A♭ on beat 3.'},
 {id:'eb65',bar:65,q:384,key:'E♭ minor',short:'E♭m',roman:'iv',type:'cadence',evidence:'The sequence in bars 62–64 reaches B♭ with D♮ and A♭; this resolves to E♭–G♭–B♭ at bar 65.'},
 {id:'bb67',bar:67,q:396,key:'B♭ minor',short:'B♭m',roman:'i',type:'cadence',evidence:'F–A♮–E♭ in bar 66 resolves to B♭–D♭–F at bar 67. The tenor’s inverted entry coincides with the tonic arrival.'},
 {id:'f73',bar:73,q:432,key:'F minor',short:'Fm',roman:'v',type:'arrival',evidence:'E♮ with B♭ at the end of bar 72 resolves to F–A♭–C at bar 73, where the alto starts the next inverted stretto.'},
 {id:'ab82',bar:82,q:486,key:'A♭ major',short:'A♭',roman:'VII',type:'arrival',evidence:'The mixed stretto starts over E♭7/D♭ at bar 80. A♭ major is prolonged through inversions before the root-position A♭–C–E♭ at bar 82.'},
 {id:'eb87',bar:87,q:516,key:'E♭ minor',short:'E♭m',roman:'iv',type:'arrival',evidence:'The continuation in bars 84–86 introduces G♭ and D♮. D♮ rises to E♭ at bar 87 over the E♭–G♭–B♭ triad.'},
 {id:'bb89',bar:89,q:528,key:'B♭ minor',short:'B♭m',roman:'i',type:'cadence',evidence:'The F dominant in bar 88 resolves to B♭–D♭–F at bar 89, coinciding with the bass entry. The alto enters in inversion one minim later.'},
 {id:'bb101',bar:101,q:600,key:'B♭ major',short:'B♭',roman:'I',type:'close',evidence:'The final F dominant resolves to B♭–D♮–F at bar 101. D♮ supplies the major closing third; this is a change of mode at the final cadence.'}
];
