# The Well-Tempered Clavier: fugue analyses

An extensible collection of musical analyses and annotated scores for the 24 fugues in each book of Bach's *Well-Tempered Clavier*. The available analysis is Book II, no. 22, B-flat minor (BWV 891).

Open `output/site/index.html` for the collection or `output/site/fugues/wtc-ii-22/index.html` for BWV 891. Each analysis works offline, including the score and synthesised playback. Keep the directory structure intact for navigation and PDF links.

The original `output/bach-bflat-minor-fugue-analysis.html` and `output/bach-bflat-minor-fugue.html` filenames remain available, with their existing `output/pdf` links.

## Organisation

- `content/catalogue.json`: IDs of available analyses, ordered by book and number when built.
- `content/fugues/<id>/`: each work's metadata, analytical reading, prepared score data, sources, PDFs and engraving scripts.
- `lib/fugues/`: shared data types, catalogue loader, score-position calculations and validation.
- `components/`: shared study page, analytical diagram, score viewer, controls and collection index.
- `lib/audio.ts`: playback engine, configured by each work's duration, voices and beat unit.
- `scripts/`: collection builds, packaging and checks.
- `output/site/`: generated, portable static collection.

Stable IDs run from `wtc-i-01` to `wtc-i-24` and `wtc-ii-01` to `wtc-ii-24`. The canonical route is `fugues/<id>/`. IDs do not depend on key spelling, display titles or filenames. Only analyses listed in the catalogue appear on the site.

The collection index loads metadata only. Each standalone analysis includes its own score; the routed app imports the requested work on demand. Voice count, bar lengths, tempo unit, system divisions, thematic categories and analytical prose belong to each work's data.

## Build and verification

Use Node 22.13 or later and install the locked dependencies with `npm ci`.

```sh
npm run build
npm run check
python3 scripts/package_release.py
```

The build creates the collection index and a self-contained HTML page for every listed work. Checks cover the existing musical content, playback, document links, identifiers and shared rendering with different voice counts and bar lengths. The packager writes `output/release` and `output/wtc-fugues-public.zip`, using an explicit public file list. BWV 891 also retains its individual `output/bach-bwv891-public.zip` archive.

## GitHub Pages

GitHub Pages uses the static collection. `npm run build:pages` builds it, runs the checks and assembles `output/release`, ready for publication. Relative links support both an account site and a project site under a repository-name subdirectory; no repository name or domain needs to be embedded in the build.

To publish from a GitHub repository:

1. Commit the project source, including `content`, its prepared data and PDFs, `package-lock.json` and `.github/workflows/pages.yml`.
2. In the repository's **Settings → Pages**, set **Source** to **GitHub Actions**.
3. In **Actions**, select **Publish to GitHub Pages**, then **Run workflow** on the repository's default branch.

The workflow builds from source, checks the result and uploads only `output/release`. It runs manually; repeat the last step to publish later changes. Prepared PDFs are used directly, so the hosted build needs no notation software. The deployment's URL appears in the workflow result.

See [GitHub's publishing-source instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) and [custom-workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

The separate `npm run build:site` command retains a server-based app build for other hosts. GitHub Pages uses `build:pages` and the generated HTML files.

## Adding a fugue

See [CONTRIBUTING.md](CONTRIBUTING.md) for the content contract and build steps. Musical decisions and notation preparation remain specific to each work; BWV 891's structural and countersubject readings are not defaults for the collection.

## Sources

Source credits, bibliographic references and analytical conventions are maintained with each work. See [BWV 891 documentation](content/fugues/wtc-ii-22/README.md) and its `sources/NOTICE.txt`. Public releases contain the selected PDFs and source notices, with no working files, source maps, local configuration or test output.
