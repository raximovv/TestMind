// Keyboard behaviour and the copy-share button, including its failure modes.
// The 1-5 shortcut was removed on purpose; this suite now guards that it stays
// removed WITHOUT taking native radio-group arrow keys down with it.
const puppeteer = require('puppeteer-core');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const URL = 'http://localhost:8765/test.html';
let pass = 0, fail = 0;
const ok = (c, m) => { c ? (pass++, console.log('  PASS ' + m)) : (fail++, console.log('  FAIL ' + m)); };

let browser;
async function open() {
  const p = await browser.newPage();
  await p.setViewport({ width: 1280, height: 900 });
  await p.setRequestInterception(true);
  p.on('request', r => r.url().indexOf('script.google.com') !== -1
    ? r.respond({ status: 200, body: '{"ok":true}' }) : r.continue());
  const errs = [];
  p.on('pageerror', e => errs.push(String(e)));
  await p.goto(URL, { waitUntil: 'networkidle2', timeout: 60000 });
  // clear a leftover draft and reload, or boot() shows the resume screen instead
  await p.evaluate(() => localStorage.clear());
  await p.reload({ waitUntil: 'networkidle2' });
  await new Promise(r => setTimeout(r, 150));
  return { p, errs };
}

// Answer through the real pointer path, from where the app actually puts the
// question: centred in the viewport, clear of the fixed step bar.
async function answer(p, i, v) {
  await p.evaluate(i => {
    const el = document.getElementById('item-' + i);
    if (el) el.scrollIntoView({ block: 'center' });
  }, i);
  await new Promise(r => setTimeout(r, 90));
  await p.click('input[name=q' + i + '][value="' + v + '"]');
  await new Promise(r => setTimeout(r, 140));
}

(async () => {
  browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new', args: ['--no-sandbox'] });

  console.log('\n== the 1-5 shortcut is gone ==');
  {
    const { p, errs } = await open();
    await p.keyboard.type('12345');
    await new Promise(r => setTimeout(r, 200));
    ok(await p.evaluate(() => state.answers.every(v => v === 0)), 'typing digits answers nothing');
    ok(await p.evaluate(() => typeof keyHandler === 'undefined'),
      'no document-level key handler is installed at all');
    ok(errs.length === 0, 'no JS errors (' + (errs[0] || 'none') + ')');
    await p.close();
  }

  console.log('\n== arrow keys still work (an accessibility floor, not a shortcut) ==');
  {
    const { p } = await open();
    await p.focus('input[name=q0][value="1"]');
    await p.keyboard.press('ArrowRight');
    await new Promise(r => setTimeout(r, 150));
    ok(await p.evaluate(() => state.answers[0] === 2), 'arrow key selects an option');
    ok(await p.evaluate(() => document.activeElement.name === 'q0'),
      'and does NOT fling them onward mid-choice');
    await p.keyboard.press('ArrowRight');
    await new Promise(r => setTimeout(r, 150));
    ok(await p.evaluate(() => state.answers[0] === 3), 'they can keep moving along the scale');
    await p.close();
  }

  console.log('\n== the step bar (hidden on step 1, appears from step 2) ==');
  {
    const { p } = await open();
    ok((await p.$$('.qnum')).length === 0, 'no "1." "2." numbers on the questions');
    ok(!(await p.$('.kbhint')), 'the keyboard hint is gone');
    ok(!(await p.$('.stepbar')), 'no step bar on step 1 - nothing to go back to, no progress yet');

    for (let i = 0; i < 5; i++) await answer(p, i, 4);
    await new Promise(r => setTimeout(r, 900));
    ok(!!(await p.$('.stepbar')), 'the step bar appears once step 1 is finished');
    const bar = await p.$eval('.stepbar', e => e.textContent.replace(/\s+/g, ' ').trim());
    ok(!/Boshladik|Yaxshi|marrada|Miyangiz|qoldi/.test(bar) && bar.indexOf('/ 50') === -1,
      'no motivational line, no x/50, no time estimate: "' + bar + '"');
    ok(bar.indexOf('Qadam 2 / 10') !== -1, 'shows the step they are on now: "' + bar + '"');
    ok(bar.indexOf('Qadam 1 / 10') === -1, 'never shows step 1 in the bar');
    ok(await p.$eval('.stepbar', e => getComputedStyle(e).position) === 'static',
      'the bar stays put in the page, it does not follow the screen');
    ok(await p.evaluate(() => {
      const b = document.querySelector('.stepbar').getBoundingClientRect();
      const c = document.querySelector('.card').getBoundingClientRect();
      return b.bottom <= c.top + 1;
    }), 'and it sits above the questions');
    ok(await p.$eval('.backlink', e => e.tagName === 'BUTTON'), 'the back link is a real button now');
    ok(await p.$eval('#pfill', e => e.style.width) === '10%', '5 of 50 answered fills 10%');

    // The bug that killed the pinned version: a bar over the content ate the taps
    // landing under it. Nothing may sit on top of an answer circle now.
    ok(await p.evaluate(() => {
      const circles = [...document.querySelectorAll('.opt .dot')];
      return circles.every(d => {
        const r = d.getBoundingClientRect();
        if (r.top < 0 || r.bottom > innerHeight) return true;   // simply off-screen
        return d.contains(document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2));
      });
    }), 'every visible answer circle receives its own taps');

    await p.click('#prevBtn');
    await new Promise(r => setTimeout(r, 250));
    ok(await p.evaluate(() => state.page === 0), 'the back link goes back a step');
    ok(!(await p.$('.stepbar')), 'and step 1 has no bar again');
    ok(await p.evaluate(() => state.answers.slice(0, 5).every(v => v === 4)),
      'and the answers are still there');

    // The bar belongs to the questions only.
    await p.evaluate(() => { state.answers = ITEMS.map((x, i) => (i % 5) + 1); renderReport(); });
    await new Promise(r => setTimeout(r, 250));
    ok(!(await p.$('.stepbar')), 'no step bar on the result screen');
    await p.close();
  }

  console.log('\n== copy-share ==');
  {
    const { p } = await open();
    await p.evaluate(() => {
      state.answers = ITEMS.map((x, i) => (i % 5) + 1);
      renderReport();
    });
    await new Promise(r => setTimeout(r, 250));
    // Headless Chrome refuses real clipboard writes, so stub the API and check what
    // OUR code hands it. The actual paste still needs a check on a real device.
    await p.evaluate(() => {
      window.__copied = null;
      navigator.clipboard.writeText = function (s) { window.__copied = s; return Promise.resolve(); };
    });
    await p.click('#copyBtn');
    await new Promise(r => setTimeout(r, 300));
    const txt = await p.evaluate(() => window.__copied || '');
    const archName = await p.evaluate(() => document.querySelector('.archname').textContent);
    ok(txt.length > 0, 'something was handed to the clipboard');
    ok(/TestMind/.test(txt), 'message mentions TestMind');
    ok(txt.indexOf('raximovv.github.io/TestMind') !== -1, 'message contains the link');
    ok(txt.indexOf(archName) !== -1, 'message names their archetype: ' + archName);
    ok(txt.length > 40 && txt.indexOf('Dilnoza') === -1, 'message does NOT leak their name');
    ok(/Nusxalandi/.test(await p.$eval('#copyBtn', b => b.textContent)), 'button confirms the copy');

    console.log('\n== a refused clipboard is reported, not faked ==');
    await new Promise(r => setTimeout(r, 2400));
    await p.evaluate(() => {
      navigator.clipboard.writeText = function () { return Promise.reject(new Error('denied')); };
    });
    await p.click('#copyBtn');
    await new Promise(r => setTimeout(r, 300));
    ok(/boʻlmadi/.test(await p.$eval('#copyBtn', b => b.textContent)),
       'button says it failed rather than claiming success');
    await p.close();
  }

  await browser.close();
  console.log('\n' + (fail ? 'FAILED ' + fail : 'ALL ' + pass + ' CHECKS PASSED'));
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error('CRASH', e); process.exit(1); });
