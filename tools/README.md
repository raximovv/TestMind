# TestMind — build & test tooling

Dev-only. None of this is served to visitors; the live site is just the static
files in the repo root. These scripts let site-wide edits stay reproducible and
let the app be verified before shipping.

## What generates what

The **hand-written source** files are: `test.html` (the whole test app — inline
styles + logic), `site.css`, `site.js`, `characters.js` (archetype data + SVG
artwork), the fonts, and `og.png`.

The **static content pages are generated** — do not hand-edit them, edit the
generator and re-run:

- `build_pages.py` → `index.html`, `obrazlar.html`, `qanday-ishlaydi.html`,
  `savollar.html`, `privacy.html`, `maktablar.html`, `ota-onalarga.html`
- `build_archetypes.py` → the ten `obraz-*.html` pages (reads `characters.js`
  via Node, so Node must be on PATH). It imports `build_pages.py` from this
  folder for the shared head/nav/footer.

Both write to the repo root (`OUT` at the top of each script). As of
2026-07-23 both were verified to reproduce every committed page byte-for-byte.

```
python build_pages.py
python build_archetypes.py
```

## The PDF guide

The take-away guide students receive (by email or through the Telegram bot) is
an A4 PDF built the same way — generated, never hand-made:

- `guide_content.py` — the **hand-written** long form, one entry per archetype
  key. This is the actual product; everything else is plumbing. Only `ES|A`
  (Ishonchli Doʻst) is written so far.
- `build_guide.py` → `tools/build/guide-<slug>.html` — a single self-contained
  file (fonts base64-inlined, artwork inlined SVG, no network at all). The name,
  the two lines, the strength/watch and the historical figure are pulled from
  `characters.js`, so the PDF cannot contradict the website.
- `make_pdf.js` → `guides/<slug>.pdf` via headless Chrome.

```
python build_guide.py "ES|A"
node   make_pdf.js  ishonchli-dost
```

Each A4 page is a **fixed box**, not flowing text — the layout is designed per
page. `make_pdf.js` measures every page first and refuses to write the PDF if
anything overflows its box, so a longer sentence can never silently get clipped.
If it reports an overflow, either shorten the text or loosen that page's
spacing; do not raise the page height.

It also skips writing a PDF whose content did not change. Chrome stamps a
timestamp into every PDF it makes, so without that check a rebuild would push
~7.5 MB of identical-but-different files through git each time.

**When writing new guide text, read the rule at the top of `guide_content.py`.**
Short version: if a sentence would be true of any student, cut it.

Tip: to check for drift without touching the repo, copy a script, point its
`OUT` at a temp dir, run it, and `diff` against the committed pages.

## Running the tests

Real Chrome is driven headlessly via `puppeteer-core`. It expects Chrome at
`C:/Program Files/Google/Chrome/Application/chrome.exe` (edit the `CHROME`
constant in each file if yours differs).

```
npm install
# most suites hit a local server — start it from the REPO ROOT in another shell:
#   python -m http.server 8765
npm run test:e2e        # 45 checks — full flow, scoring, archetypes, restart
npm run test:keyboard   # 27 — arrow keys, the removed 1–5 shortcut, step bar, copy-share
npm run test:capture    # 19 — email capture: sent once, no name/age/answers, honest failures
npm run test:autosave   # 9  — answers saved anonymously with a separate id
npm run test:anchor     # 13 — the next question lands under the pointer (0px drift)
npm run audit           # 18 pages × 3 widths, horizontal + vertical overflow
node retest.js          # 14 — «Oʻshanda va hozir» compares against the OLD result
node lowend.js          # 10 — cheap Android: 4x slower CPU, slow 4G, 360px
```

`lowend.js` is the one to run before a school pilot: 89% of Uzbek internet users
are on a phone, and desktop Chrome at a 390px viewport is not the same test —
it has no CPU limit, no latency and no data cost.

`anchor.js` opens the page over `file://` and needs no server; the rest use
`http://localhost:8765/`.

## Changing the domain

Two constants: `SITE` in `build_pages.py` and `SITE_HOST` in `test.html`.
