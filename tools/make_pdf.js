// Renders a built guide (tools/build/guide-<slug>.html) to ../guides/<slug>.pdf
// with real Chrome, and refuses to write a PDF whose content overflows a page.
//
//   python build_guide.py ES|A
//   node   make_pdf.js  ishonchli-dost
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const HERE = __dirname.replace(/\\/g, '/');
const OUTDIR = path.posix.join(path.posix.dirname(HERE), 'guides');

const BUILD = path.posix.join(HERE, 'build');

async function render(browser, slug) {
  const src = path.posix.join(BUILD, 'guide-' + slug + '.html');
  if (!fs.existsSync(src)) { console.error('missing ' + src + ' — run build_guide.py first'); return false; }

  const page = await browser.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push(String(e)));
  await page.goto('file:///' + src, { waitUntil: 'load', timeout: 60000 });
  await page.evaluate(() => document.fonts.ready);   // no text may be measured on a fallback font

  // Every page is a fixed box; content that spills would be silently clipped.
  const boxes = await page.evaluate(() => [...document.querySelectorAll('.page')].map((el, i) => ({
    i: i + 1, over: el.scrollHeight - el.clientHeight,
  })));
  const spill = boxes.filter(b => b.over > 1);
  if (spill.length || errors.length) {
    spill.forEach(b => console.log('  ' + slug + ' page ' + b.i + ': OVERFLOW +' + b.over + 'px'));
    if (errors.length) console.log('  ' + slug + ' errors: ' + errors.join(' | '));
    await page.close();
    return false;
  }

  if (!fs.existsSync(OUTDIR)) fs.mkdirSync(OUTDIR, { recursive: true });
  const out = path.posix.join(OUTDIR, slug + '.pdf');
  const buf = await page.pdf({ printBackground: true, preferCSSPageSize: true,
                               displayHeaderFooter: false });
  await page.close();

  // Chrome stamps /CreationDate and /ModDate into every PDF, so a rebuild with no
  // content change still produces a different file — which would churn ~750 KB per
  // guide through git for nothing. Compare with those two fields blanked out and
  // only write when the guide itself actually changed.
  const same = fs.existsSync(out) && strip(fs.readFileSync(out)) === strip(buf);
  if (same) { console.log('  --  ' + slug + '.pdf unchanged'); return true; }

  fs.writeFileSync(out, buf);
  console.log('  ok  ' + slug + '.pdf  (' + boxes.length + ' pages, ' +
              (buf.length / 1024).toFixed(0) + ' KB)');
  return true;
}

/** A PDF's bytes with the two timestamp fields neutralised.
 *  Buffer.from is required: page.pdf() hands back a Uint8Array, whose toString()
 *  ignores the encoding argument and would never compare equal to a file read. */
function strip(buf) {
  return Buffer.from(buf).toString('latin1')
    .replace(/\/CreationDate \(D:[^)]*\)/g, '/CreationDate ()')
    .replace(/\/ModDate \(D:[^)]*\)/g, '/ModDate ()');
}

(async () => {
  // No argument = every guide that has been built.
  const slugs = process.argv.length > 2 ? process.argv.slice(2)
    : fs.readdirSync(BUILD).filter(f => /^guide-.*\.html$/.test(f))
        .map(f => f.replace(/^guide-|\.html$/g, ''));
  if (!slugs.length) { console.error('nothing built — run build_guide.py first'); process.exit(1); }

  const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new', args: ['--no-sandbox'] });
  let bad = 0;
  for (const s of slugs) if (!await render(browser, s)) bad++;
  await browser.close();

  console.log('\n' + (slugs.length - bad) + '/' + slugs.length + ' written to ' + OUTDIR);
  if (bad) { console.error('fix the overflow above — those PDFs were NOT written'); process.exit(1); }
})();
