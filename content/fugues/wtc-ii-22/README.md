# WTC II, no. 22: Fugue in B-flat minor, BWV 891

The complete analysis is assembled in `study.ts`. Formal divisions, thematic descriptions and harmonic evidence are in `analysis.ts`; titles, document links and the public asset list are in `metadata.json`.

## Analytical conventions

S / Si identify the 24 principal subject statements. CS1 is the chromatic countersubject; CS2 is the less consistent second counterpoint identified by Keller. An asterisk marks variants or fragments. Lower-case labels identify selected recurring cells: s, c1, c2 and t1. Local melodic adjustments are included within subject labels.

Prout's five principal groups head the diagram. The table divides the last group to show the paired stretto separately. Cadences, tonic arrivals and thematic entry contexts have distinct markers. The keyboard score places soprano and alto on the upper stave and tenor and bass on the lower, retaining independent stem directions, rests and ties. Voice prefixes identify the analytical labels.

## Notation and PDF generation

Prepared JSON and SVG data are included, so ordinary site builds do not require notation software. The engraving scripts in this work's `scripts` directory are specific to BWV 891. Install Python packages `verovio==6.3.0`, `reportlab` and `pypdf` to regenerate the notation. Image preparation uses Sharp.

Run these commands from the project root, in the relevant sequence:

```sh
python3 content/fugues/wtc-ii-22/scripts/analyze_materials.py
python3 content/fugues/wtc-ii-22/scripts/engrave_annotations.py
python3 content/fugues/wtc-ii-22/scripts/engrave_themes.py
```

For the four-stave PDF:

```sh
node content/fugues/wtc-ii-22/scripts/prepare_pdf_images.mjs
python3 content/fugues/wtc-ii-22/scripts/build_score_pdf.py
```

For the two-stave PDF:

```sh
python3 content/fugues/wtc-ii-22/scripts/engrave_keyboard.py
node content/fugues/wtc-ii-22/scripts/prepare_keyboard_images.mjs
python3 content/fugues/wtc-ii-22/scripts/build_keyboard_pdf.py
```

PDFs are written to this work's `pdf` directory. Intermediate engravings and images go to `tmp/wtc-ii-22` at the project root. The score contains 1,828 written notes, 76 ties and 101 bars. The keyboard transformation preserves the encoded pitches and rhythmic values. Inspect every page of regenerated PDFs before release.

To rebuild the historical extracts, place the complete scans named `prout-bach-48.pdf` and `tovey-bach-ii.pdf` in `tmp/wtc-ii-22/source-scans`, then run `python3 content/fugues/wtc-ii-22/scripts/build_source_extracts.py`. A different directory can be supplied with `--source-dir`. The script records the scan URLs and page indices.

`prepare_score.py` and `finalize_score.py` retain the original source-conversion workflow, including unused early engraving windows. These windows are not imported by the shared viewer.

After changing data or documents, run `npm run build`, `npm run check` and `python3 scripts/package_release.py` to refresh and verify public copies.

## Sources and rights

The musical source is Kroll's public-domain Bach-Gesellschaft edition (1866), encoded in Humdrum by David Huron and revised by Craig Sapp. Huron and Sapp are credited for the digital transcription. The original encoding and MEI retain their source notices as a record of provenance.

Prout's 1910 text and editorial notes, and the original Tovey commentary from the 1924 edition, are public-domain source extracts under the ordinary UK term. Tovey's fugue commentary begins near the foot of p. 156; the preceding prelude commentary is retained. Both extracts preserve the original page images and footnotes and include bibliographic details and a scan-source link.

Keller's text is linked, without reproduction or translation. Keller died in 1967; the usual UK term runs through 2037. Online availability does not grant translation or republication rights.

- [Score encoding](https://github.com/humdrum-tools/bach-wtc-fugues)
- [Keller](https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv891.pdf)
- [Tovey edition record](https://imslp.org/wiki/Das_wohltemperierte_Klavier_II%2C_BWV_870-893_(Bach%2C_Johann_Sebastian))
- [UK copyright duration](https://www.gov.uk/copyright/how-long-copyright-lasts)
