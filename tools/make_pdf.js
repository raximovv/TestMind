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
  await page.pdf({ path: out, printBackground: true, preferCSSPageSize: true,
                   displayHeaderFooter: false });
  await page.close();
  console.log('  ok  ' + slug + '.pdf  (' + boxes.length + ' pages, ' +
              (fs.statSync(out).size / 1024).toFixed(0) + ' KB)');
  return true;
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
