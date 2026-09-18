# WTC II, no. 9: Fugue in E major, BWV 878

Four voices, 43 bars, 4/2. Beats on the page are minims; data and playback use crotchets internally. The source is Kroll's Bach-Gesellschaft text, encoded by David Huron and revised by Craig Sapp. The source encoding is unchanged.

## Source comparison and analytical decisions

The six principal groups follow Keller, with boundaries placed at the actual entries. The variation begins in bar 23, and diminution enters at bar 26 beat 4 before the preceding pair has finished. These overlaps are audible in the score and explicit in the diagram. The closing group follows the G-sharp minor cadence, beginning at bar 35 beat 2.

Prout separates exposition, counter-exposition, middle and final sections. He calls bars 23-26 an episode based on the transformed subject; Keller's thematic grouping and Tovey's variation stretto are preferred here. This is a difference of analytical approach, not an error in the notes.

The first answer is real: its six pitches are an exact transposition of the subject by seven semitones. Subsequent local alterations do not change that classification. All 27 selected complete entries or adapted statements are marked separately from derived figures. The ornamented version fills the rising third; five entries use diminished values. The bass entry beginning at bar 30 beat 2 alters its last note.

The alto enters at bar 9 beat 2, and again at bar 35 beat 2, with a shortened first note. The tenor follows one minim later. Source descriptions of a half-bar stretto refer to the unshortened model: the diagram instead gives sounding onsets. The second pair in bars 10-11 is half a bar apart. The final soprano subject begins on beat 4 of bar 37, with another shortened first note, and reaches A5 in bar 38.

The main countersubject first appears in the bass at bar 3. Its ascending crotchets, leap and continuation recur with alterations, including the tenor return at bar 11 beat 4 noted by Prout. Derived sequential phrases are labelled c*, rather than represented as unchanged countersubject statements. The additional countersubjects of bars 16-20 are marked x and y, following Tovey. They combine with the subject in triple counterpoint, in the dispositions alto/tenor/bass, soprano/alto/tenor and bass/soprano/alto (subject/x/y). Adaptations at their beginnings and in their continuations are marked rather than silently treated as exact repetitions.

Prout describes inverted diminution during the final approach and in the last stretto. Tovey discusses the altered intervals and proposes octave changes in the soprano at bar 35. Those changes are not adopted. The markings i* identify related figures in the transmitted score; none is counted as an exact, complete inverted entry. Tovey also disputes an E natural in editions of bar 19; the supplied Kroll-based encoding already gives E sharp in the soprano at beat 3¾. No further alteration has been made on that basis.

Harmonic markers identify the cadences in B (9), C-sharp minor (16), F-sharp minor (23), B (28), G-sharp minor (35), and E (43). The E subject at bar 30 beat 3 is explicitly an entry context over C-sharp minor harmony; the tonic sonority at bar 31 beat 3 is a passing arrival within the sequence, not a structural cadence.

## Reproduction and verification

Run the work-local scripts in this order: `prepare_score.py`, `analyse_materials.py`, `engrave.py`, `prepare_pdf_images.mjs`, and `build_pdfs.py --prout FULL_PROUT_SCAN.pdf --tovey FULL_TOVEY_BOOK_II_SCAN.pdf`. Python requires Verovio 6.3, ReportLab and pypdf; image rendering uses the project's Sharp dependency. Generated intermediates live in `tmp/` and are not published.

The pitch and onset check compares the source parser with Verovio, including explicit gestural accidentals and tied chromatic notes across bar-lines. Both staff arrangements preserve all 802 written notes and 52 ties; playback contains 750 sounding events. `check_analysis.py` checks subject shapes, the real answer, diminution, shortened openings, the chromatic pair, harmonic resolutions and the register climax.

The PDF extracts preserve Prout's printed pp. 64-66 and Tovey's pp. 56-57, including adjoining commentary; bibliographic footers link to their complete scans. Keller is linked externally. The release contains only the study page, four PDFs and the source notice.
