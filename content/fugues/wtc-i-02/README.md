# WTC I, no. 2: Fugue in C minor, BWV 847

Three voices, 31 bars, 4/4. The study uses Kroll's 1866 Bach-Gesellschaft text, encoded by David Huron and revised by Craig Sapp. The original Humdrum file is retained unchanged. See [source notices](sources/NOTICE.txt).

## Analytical decisions and source comparison

The principal division is at bar 15, following Keller (pp. 45-47). His printed endpoint “32” on p. 46 is inconsistent with this 31-bar score; the study uses 31. Prout (1910, pp. 14-16) instead places the middle section at bar 9 and the final section at bar 20, with a coda at bar 29. These are different formal readings, not discrepancies in the notes.

The first quaver counterpoint begins in the alto at bar 3 beat 3½. The preceding descending scale is labelled separately, following Keller. Prout begins his countersubject on B natural at bar 3 beat 1½, including the scale. Consequently, Prout describes a transfer from soprano to alto at bars 26-27; under the present boundary the quaver CS1 remains in the alto.

CS2 names the recurring second counterpoint in Keller's account. Prout declines this designation because the passages differ. Its first appearance is in the alto, bars 7-9; later spans are explicitly marked as variants. The labels do not imply an invariant second melody or all six permutations of strict triple counterpoint.

| Entry | Voice | First note | Form | Closing note |
| --- | --- | --- | --- | --- |
| 1.1½ | Alto | C5 | Subject | E-flat4, 3.1 |
| 3.1½ | Soprano | G5 | Tonal answer | B-flat4, 5.1 |
| 7.1½ | Bass | C4 | Subject | E-flat3, 9.1 |
| 11.1½ | Soprano | E-flat5 | Subject in relative major | G4, 13.1 |
| 15.1½ | Alto | G4 | Answer form in G minor | B-flat3, 17.1 |
| 20.1½ | Soprano | C5 | Subject | E-flat4, 22.1 |
| 26.3½ | Bass | C3 | Subject, displaced | E-flat2, 28.3 |
| 29.3½ | Soprano | C5 | Subject over tonic pedal | E-natural4, 31.3 |

Pitch names use middle C = C4; beats are crotchets. Entries include their closing notes. There is no stretto of complete entries. The subject-head fragments in the episodes are not counted as additional entries.

Harmonic arrivals were read from the score independently. In particular, the G entry at bar 15 is distinguished from the G minor cadence at bar 17; the half-bar displacement of the last two entries is explicit; the major third appears at bar 31 beat 3. The sequential harmonies of bars 22-26 are not presented as a series of structural modulations.

Prout's observations on the episodes were checked against the corresponding note patterns: bars 5-6 return in contrapuntal inversion in 17-19; the upper parts of 9-11 are inverted in 22-25. Scale runs and subject-head cells are selectively marked, with variants distinguished from complete statements. The quaver counterpoint in thirds in bars 13-15 and the added soprano head-fragments in bars 17-19 are also marked.

Tovey (1924, p. 9; scan page 29) recognises two countersubjects and five of the six permutations of triple counterpoint. Like Prout, he includes the descending scale in the first countersubject. His account connects the episodes through derivation, contrapuntal inversion and recapitulation, and stresses independent phrasing of all three themes. The study retains Keller’s boundary for CS1 and explicitly marks variants of CS2. The source link opens at the commentary, immediately before the score.

## Reproduction and checks

The work-local scripts prepare note data, identify analytical spans, engrave both staff arrangements and the three examples, render print images, and build the two annotated PDFs plus the Prout extract. Python requires Verovio, ReportLab and pypdf; image rendering uses the project's Sharp dependency. Run `prepare_score.py`, `analyse_materials.py`, `engrave.py`, `prepare_pdf_images.mjs`, then `build_pdfs.py --prout PATH_TO_COMPLETE_PROUT_SCAN.pdf`. Full source scans are build inputs, not public site files.

`check_analysis.py` verifies all eight subject shapes and entry positions, both tonal-answer mutations, the first counterpoint's recurring contour, the second counterpoint's variant status, harmonic evidence and the final pedal. The engraving pipeline verifies the complete set of 770 note identifiers and 16 ties in both staff arrangements, as well as every sounding pitch and onset. The two bass Cs each sustain for ten crotchets from bar 29 beat 3. Only the principal D of the added soprano chord in bar 30 is coloured as subject.

Written pitches are checked independently against the MEI key and accidental spelling. Gestural accidentals are then made explicit because Verovio 6.3's MIDI lookup omits key-signature alterations for this import. The original notation is retained; additional accidental cancellations are calculated where the keyboard version puts two voices on one stave.

Final review: every page of both annotated scores and the Prout extract was visually inspected. Single-note continuations retain their colour but omit repeated labels to avoid collisions. The collection build, TypeScript, rendered-page, audio, link and musical checks pass for both published studies.
