# WTC I, no. 23: Fugue in B major, BWV 868

Four voices, 34 bars, 4/4. All times and printed beats are crotchets. The source is Kroll's Bach-Gesellschaft text, encoded by David Huron and revised by Craig Sapp. The original Humdrum file is unchanged.

## Analytical decisions

Keller, pp. 111–112, divides the fugue into two equal halves, 1–17 and 18–34. Each contains a four-entry group and a later pair. The first half has tenor, alto, soprano, bass, then tenor and alto; the second has inverted soprano and alto, direct bass and tenor, then alto and soprano. The harmonic cadence at 18 overlaps the start of the second half.

The answer is tonal. Compared with a strict fifth transposition, notes 2–5 are lowered, while the rising continuation returns to the fifth relationship; the precise semitone offsets are checked against the score. The subject model includes its closing B at bar 3. Later statements include that terminal note or its adapted equivalent and any tied continuation. The soprano at 5 and alto at 29 decorate the close. The alto at 16 decorates the penultimate G sharp and ends on A sharp. The tenor at 24 starts on E within C-sharp minor and decorates its ending.

The soprano inversion at 18 reverses the diatonic intervals of the first thirteen notes; its last note is adapted. The alto at 20 transposes the interior of that inversion down a fourth, adjusting the first and last notes. Both are labelled variants. The bass's direct return begins at 21:3½, before the inverted alto has finished, rather than at the bar 22 often used to identify it in general accounts. The earlier tenor return starts at 11:3½. The other entries begin at beat 1½.

Prout describes the countersubject as complete in the exposition and once later, at 31–32, with fragments elsewhere. Tovey stresses its structural importance and identifies the episode material. Four full countersubject spans are marked, with adapted continuations labelled CS*. The seven-note descending opening is marked c where its diatonic shape and rhythm recur. The six-note figure at the end of alto bar 7 is marked e, and its exact diatonic inversions ei. These short matches identify recurring figures, not complete subject entries. Episode spans and cadence readings were checked against the score; entry-key markers do not imply a tonic chord at each subject onset.

## Reproduction and checks

Run `prepare_score.py`, `analyse_materials.py`, `engrave.py`, `prepare_pdf_images.mjs`, then `build_pdfs.py --prout FULL_PROUT_SCAN.pdf --tovey FULL_TOVEY_BOOK_I_SCAN.pdf`. Python requires Verovio 6.3, ReportLab and pypdf; SVG rasterisation uses Sharp. Intermediate files go to `tmp/wtc-i-23` at the repository root.

The parser independently verifies all 876 written pitches and onsets against Verovio. Both staff arrangements retain all 49 ties; playback joins them into 827 sounding events across 136 crotchets. The full-bar rests are encoded as measure rests. In bars 24–28 the high tenor uses treble clef in the open score and moves to the upper staff in the keyboard arrangement. The checks cover the tonal answer, inverted pair, subject entries, countersubject disposition, annotation bounds, closing B-major chord and printed score completeness.

The extracts preserve Prout's printed pp. 50–51 and Tovey's printed p. 151, including adjoining commentary. Keller is linked externally. The NBS recording is Diego Ares, YouTube `2I3hdaTQvcA`, with the fugue starting at 1:31 according to the official chapter marker. Scrolling playback starts at crotchet = 60, following Keller; ornaments and expressive timing are omitted.
