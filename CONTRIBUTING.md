# Adding and maintaining analyses

## Work identity and files

Create a directory under `content/fugues` using the book and number, for example `wtc-i-01`. The identifier remains stable if the title, key spelling or edition changes. Use one directory per fugue; do not put unpublished works in `content/catalogue.json`.

Each directory contains:

| File or directory | Purpose |
| --- | --- |
| `metadata.json` | ID, book, number, BWV, key, titles, description, document links and explicit public file list |
| `study.ts` | A default export satisfying `FugueData` in `lib/fugues/types.ts` |
| `analysis.ts` | Work-specific analytical text and structural/tonal events; organisation may vary |
| `data/` | Prepared note events, playback notes, annotated SVG systems and thematic examples |
| `sources/` | Original encodings and `NOTICE.txt` with edition and transcription credits |
| `pdf/` | Companion scores and any historical analysis extracts selected for publication |
| `scripts/` | Notation preparation and PDF generation specific to this work |
| `README.md` | Analytical conventions, sources and regeneration instructions |

The current work is an example of the file contract, not an analytical template. A fugue may have different formal divisions, several subjects, one or no recurring countersubject, different textures or different notation requirements. Define its material list and descriptions accordingly. Empty thematic-example or tonal-event lists are supported. The shared viewer currently lays out subject material, countersubjects and cells in three lanes within each voice; genuinely simultaneous independent subjects in one voice may need a later layout extension.

## Data conventions

All numerical score times use crotchets: a minim lasts `2`, a quaver `.5`. Each bar records its number, onset, duration and the crotchet length of its notated beat. This accommodates changing bar lengths and different beat units. Bars must be contiguous and consecutively numbered, starting at score time zero. A pickup can be numbered zero.

Playback tempo has a separate fixed beat unit, initial value and control range. Playback notes must be sorted by onset and have ties joined. Written score notes remain separate and retain their voice index and bar number. Voice indices start at zero. The current synthesiser does not interpret ornaments, tempo changes or expressive timing.

Systems state their first and last bar; they may contain different numbers of bars. Every bar must belong to exactly one system. Whole-score SVGs use unique element IDs and preserve `data-note-id`, `data-time` and, where applicable, `data-annotation-id` on clickable notes. Prefix SVG IDs and internal references by system or example to prevent collisions. SVGs are trusted, reviewed project content.

Each material has an ID, label, colour and role (`subject`, `countersubject` or `cell`). Use lowercase letters, digits and hyphens in IDs. Annotated SVG notes and labels use `material-<id>`, alongside the `note` or `annotation-label` class, so the shared layer controls work. Annotation spans carry an explicit display name: distinctions such as real/tonal answer belong in the work data.

Keep interpretation separate from engraved source facts. Record the basis for countersubject identification, formal divisions and harmonic markers in the work's notes and sources. Use British musical terminology. Credit editors and encoders per work; public source extracts and external analysis links belong in that work's metadata.

## Documents and routes

Use work-relative document links such as `./pdf/annotated-keyboard.pdf`. Add every public PDF to `metadata.json`'s `publicFiles`, along with `sources/NOTICE.txt`. The build places these alongside `fugues/<id>/index.html`; the notice becomes `SOURCE-NOTICES.txt`. Working encodings, intermediate images, scripts and research files are not copied to the public site.

Optional `legacyPages` and `legacyArchive` fields preserve existing download names. New works normally need neither. All local links must resolve within the packaged collection, which uses relative paths and requires no chosen domain name.

## Build and review

1. Add the finished work's ID to `content/catalogue.json`.
2. Run `npm run build`. This regenerates `lib/fugues/catalogue.ts`; do not edit that generated file by hand.
3. Run `npm run check`. This validates score spans and voice indices, checks static rendering and local links, and tests playback and shared layouts. Keep work-specific regression checks for important musical facts.
4. Review the musical analysis and all regenerated score pages. Structural checks do not establish the correctness of an interpretation or the visual quality of new notation.
5. Run `python3 scripts/package_release.py` to create the public directory and ZIP. Publish only the generated release when publication is authorised.

For GitHub Pages, `npm run build:pages` runs the build, checks and packaging sequence above. The manual workflow in `.github/workflows/pages.yml` publishes only `output/release`, from the repository's default branch. Keep all internal links relative and retain the generated directory structure so project-site subdirectories work.

`npm run dev` builds the static collection and opens a local HTTP server at `http://127.0.0.1:5173`. Rebuild after edits to refresh the files. Shared styles are in `styles/`; `vite.config.ts` configures the browser build.

Generated data can be committed so ordinary builds need no notation tools. Keep temporary notation, source scans and test results under the ignored `tmp/<id>` directory. Public files should contain no local paths, personal notes or conversational text. Retain source attribution and necessary third-party licence notices.
