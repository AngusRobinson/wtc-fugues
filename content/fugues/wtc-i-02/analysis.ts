export const voices=['Soprano','Alto','Bass'];
export const formalGroups=[
 {start:1,end:14,number:'I',label:'Exposition and E♭ entry',range:'1–14',continuation:'A 1 · S 3 · B 7; S 11'},
 {start:15,end:31,number:'II',label:'Second group and coda',range:'15–31',continuation:'A 15 · S 20 · B 26; S 29'},
];
export const themes=[
 {id:'subject',title:'Subject / tonal answer',location:'Subject: alto, bars 1–3',text:'The opening C–G fourth becomes G–C in the tonal answer (bar 3). The subject closes on the third, E♭. Both final entries begin on the second quaver of beat 3; the last closes on E♮.'},
 {id:'cs1',title:'Countersubject 1',location:'Alto, bar 3 beat 3½ to bar 5',text:'Keller separates this quaver counterpoint from the preceding descending scale, d. Prout includes the scale from bar 3 beat 1½ in his countersubject.'},
 {id:'cs2',title:'Countersubject 2',location:'Alto, bar 7 beat 3½ to bar 9',text:'The recurring second counterpoint is less fixed: later variants are marked *. Keller recognises it; Prout regards it as free counterpoint.'},
];
export const sections=[
 {start:1,end:9,label:'Exposition',entries:'Subject: alto, bar 1 · tonal answer: soprano, bar 3 · subject: bass, bar 7',detail:'The first countersubject appears in the alto at bar 3 and the soprano at bar 7; the second enters in the alto at bar 7. The two-part link in bars 5–7 consists of a sequence of the head motif (h) over the ascending form of the scale figure (d). The bass subject closes at the opening of bar 9.'},
 {start:9,end:15,label:'Episode – E♭ entry – episode',entries:'Subject: soprano, bar 11 · CS1: bass · CS2*: alto',detail:'Bars 9–11: h in the upper voices, descending scale sequences in the bass. Bars 13–15 reverse the scale direction in the soprano; the quaver counterpoint (q) in thirds lies below.'},
 {start:15,end:20,label:'G minor entry and episode',entries:'Answer: alto, bar 15 · CS1: soprano · CS2*: bass',detail:'The entry takes the answer form. In bars 17–18, the two lines of bars 5–6 return inverted at the twelfth; from bar 18 beat 3 they are inverted again at the octave. The added soprano doubles the subject-head fragments in thirds and tenths.'},
 {start:20,end:26,label:'Tonic return and episode',entries:'Subject: soprano, bar 20 · CS1: alto · CS2*: bass',detail:'Bars 22–25 invert the upper parts of bars 9–11 over an extended bass sequence; bars 25–26 recall the earlier two-part link.'},
 {start:26,end:29,label:'Bass entry and cadence',entries:'Subject: bass, bar 26 beat 3½ · CS1*: alto · CS2*: soprano',detail:'The scale link remains in the soprano; the quaver CS1 is in the alto from bar 27 beat 1½. Its closing C is delayed to bar 28 beat 3½. The ensuing cadence reaches the tonic pedal in bar 29.'},
 {start:29,end:31,label:'Coda',entries:'Subject*: soprano, bar 29 beat 3½ · tonic pedal from beat 3',detail:'The final subject is supported by added chord tones, without a complete countersubject. E♮ supplies the major third at bar 31 beat 3.'},
];
export const tonalEvents=[
 {id:'g5',bar:5,q:16,key:'G minor',short:'Gm',type:'cadence',evidence:'The answer closes on B♭ over G. F♯ in the alto resolves to G, establishing the dominant minor key.'},
 {id:'c7',bar:7,q:24.5,key:'C minor',short:'Cm',type:'arrival',evidence:'The bass enters on C under E♭ in the soprano and C in the alto. The C minor return follows the sequential link; the opening quaver of the bar still carries F from bar 6.'},
 {id:'eb11',bar:11,q:40,key:'E♭ major',short:'E♭',type:'arrival',evidence:'The B♭ dominant in bar 10 leads to E♭ in the bass with G and E♭ above. The soprano subject begins half a beat after this arrival.'},
 {id:'eb13',bar:13,q:48,key:'E♭ major',short:'E♭',type:'cadence',evidence:'D in the bass resolves to E♭ under B♭ and G. The entry ends and the next episode begins within this bar.'},
 {id:'g15',bar:15,q:56.5,key:'G minor',short:'Gm',type:'entry',evidence:'The alto begins the answer form on G. C minor harmony persists at the opening; the entry is confirmed in G minor at the cadence in bar 17.'},
 {id:'g17',bar:17,q:64,key:'G minor',short:'Gm',type:'cadence',evidence:'The D dominant with F♯ resolves to G–B♭–G. The new episode begins after this cadence.'},
 {id:'c20',bar:20,q:76,key:'C minor',short:'Cm',type:'arrival',evidence:'B♮ in the approach resolves to C above E♭ in the bass: the tonic returns in first inversion. The soprano entry follows on the second quaver.'},
 {id:'c22',bar:22,q:84,key:'C minor',short:'Cm',type:'cadence',evidence:'G–B–F in bar 21 resolves to C–C–E♭. The following sequence passes through F minor, B♭ and E♭ harmonies before returning to the dominant of C; these are not separate structural key sections.'},
 {id:'c29',bar:29,q:114,key:'C minor',short:'Cm',type:'cadence',evidence:'The dominant at beat 2 resolves to C at beat 3. The doubled bass C is tied through the final bar; the subject enters half a beat later.'},
 {id:'C31',bar:31,q:122,key:'C major',short:'C',type:'close',evidence:'The subject’s final E is natural. The resulting C–E–G sonority is the major closing chord, rather than a preceding modulation to C major.'},
];
