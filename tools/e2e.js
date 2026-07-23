// Drives the real test page through a full run in real Chrome and checks the result.
// Served over http://localhost:8765 so characters.js loads exactly as it does live.
const puppeteer = require('puppeteer-core');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const URL = 'http://localhost:8765/test.html';
let pass = 0, fail = 0;
const ok = (c, m) => { c ? (pass++, console.log('  PASS ' + m)) : (fail++, console.log('  FAIL ' + m)); };

let browser;
async function open() {
  const p = await browser.newPage();
  await p.setViewport({ width: 390, height: 844 });
  const errs = [];
  p.on('pageerror', e => errs.push(String(e)));
  p.on('console', m => { if (m.type() === 'error') errs.push('console: ' + m.text()); });
  await p.setRequestInterception(true);
  p.on('request', r => r.url().indexOf('script.google.com') !== -1
    ? r.respond({ status: 200, body: '{"ok":true}' }) : r.continue());
  await p.goto(URL, { waitUntil: 'networkidle2', timeout: 60000 });
  // Clear a draft left by an earlier page, then reload: boot() has already run,
  // and with a draft in place it shows the resume screen instead of question 1.
  await p.evaluate(() => localStorage.clear());
  await p.reload({ waitUntil: 'networkidle2' });
  return { p, errs };
}

// Answer every question through the real UI, page by page.
async function fullRun(pattern) {
  const { p, errs } = await open();
  const total = await p.evaluate(() => ITEMS.length);
  for (let page = 0; page < Math.ceil(total / 5); page++) {
    for (let i = page * 5; i < Math.min((page + 1) * 5, total); i++) {
      await p.evaluate((i, v) => {
        document.querySelector('input[name=q' + i + '][value="' + v + '"]').click();
      }, i, pattern(i));
    }
    const next = await p.$('#nextBtn');
    if (next) { await next.click(); await new Promise(r => setTimeout(r, 60)); }
  }
  await new Promise(r => setTimeout(r, 300));
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

  console.log('\n== full run through the real UI ==');
  {
    const { p, errs } = await fullRun(i => (i % 5) + 1);
    ok(errs.length === 0, 'no JS errors (' + (errs[0] || 'none') + ')');
    const r = await p.evaluate(() => ({
      hero: !!document.querySelector('.hero'),
      shapes: document.querySelectorAll('.herotop svg path,.herotop svg circle,.herotop svg rect,.herotop svg ellipse').length,
      name: (document.querySelector('.archname') || {}).textContent || '',
      lines: document.querySelectorAll('.archlines li').length,
      strength: !!document.querySelector('.strength'),
      deep: !!document.querySelector('details.deep'),
      deepOpen: document.querySelector('details.deep').hasAttribute('open'),
      heroText: document.querySelector('.hero').textContent,
      traits: document.querySelectorAll('details.deep .trait').length,
      btns: !!document.getElementById('shareBtn') && !!document.getElementById('againBtn'),
      capture: !!document.getElementById('capEmail')
    }));
    ok(r.hero, 'hero card rendered');
    ok(r.shapes > 25, 'character artwork present (' + r.shapes + ' shapes)');
    ok(r.name.length > 3, 'archetype name shown: ' + r.name);
    ok(r.lines === 2, 'two description lines');
    ok(r.strength, 'strength line shown');
    ok(r.deep && !r.deepOpen, 'the five scores start hidden behind a closed toggle');
    ok(!/\d\.\d\s*\/\s*5/.test(r.heroText), 'no "x.x / 5" score leaks into the hero');
    ok(r.traits === 5, 'all 5 traits inside the toggle');
    ok(r.btns && r.capture, 'share, restart and email capture all present');
    await p.close();
  }

  console.log('\n== the test is already running when the page loads ==');
  {
    const { p } = await open();
    ok(!(await p.$('#startBtn')), 'no start button to press');
    ok(!!(await p.$('#nextBtn')), 'question 1 is on screen immediately');
    ok((await p.$$('.item')).length === 5, 'the first five questions are rendered');
    ok((await p.$$('.step')).length === 3, 'the three step cards sit above them');
    ok((await p.$$('.stepart svg')).length === 3, 'each step card carries its own artwork');
    const nums = await p.$$eval('.stepnum', els => els.map(e => e.textContent.trim()));
    ok(nums.join('|') === 'QADAM 1|QADAM 2|QADAM 3', 'steps numbered in order: ' + nums.join('|'));
    ok((await p.$$('#app input, #app textarea, #app select[name]')).length === 25,
      'the only inputs are the 5 questions x 5 circles - nothing to fill in');
    const txt = await p.$eval('#app', e => e.textContent);
    ok(!/Ismingiz|Yoshingiz/.test(txt), 'never asks for a name or an age');
    ok(await p.evaluate(() => !('name' in state) && !('age' in state)),
      'state carries no name and no age');
    // open() wipes localStorage after load, so answer one question to write a draft.
    await p.click('input[name=q0][value="3"]');
    ok(await p.evaluate(() => {
      const d = JSON.parse(localStorage.getItem('testmind_draft_v1'));
      return d && !('name' in d) && !('age' in d);
    }), 'the saved draft carries no name and no age');
    await p.close();
  }

  console.log('\n== answering advances, and fades the question behind you ==');
  {
    const { p, errs } = await open();
    const stamp = () => p.evaluate(() => { window.__t = document.querySelector('.card'); });
    await stamp();
    await p.click('input[name=q0][value="4"]');
    await new Promise(r => setTimeout(r, 450));
    ok(await p.evaluate(() => document.getElementById('item-0').classList.contains('done')),
      'the answered question is dimmed');
    ok(await p.evaluate(() => !document.getElementById('item-1').classList.contains('done')),
      'the next question is not');
    ok(await p.evaluate(() => window.__t === document.querySelector('.card')),
      'the page was not re-rendered - only that one row changed');
    ok(await p.evaluate(() => {
      const r = document.getElementById('item-1').getBoundingClientRect();
      return r.top >= 0 && r.bottom <= innerHeight;
    }), 'question 2 was brought into view');

    // Editing an earlier answer must NOT throw them down the page.
    await p.evaluate(() => document.getElementById('item-2').scrollIntoView({block:'center'}));
    await new Promise(r => setTimeout(r, 120));
    const before = await p.evaluate(() => window.scrollY);
    await p.click('input[name=q0][value="2"]');
    await new Promise(r => setTimeout(r, 400));
    ok(Math.abs(await p.evaluate(() => window.scrollY) - before) < 12,
      're-answering an earlier question leaves them where they were');
    ok(await p.evaluate(() => state.answers[0] === 2), 'the edit still took effect');

    // Tapping the chosen circle again clears it, and un-dims the row.
    await p.click('input[name=q0][value="2"]');
    await new Promise(r => setTimeout(r, 150));
    ok(await p.evaluate(() => state.answers[0] === 0), 'tapping the chosen circle clears it');
    ok(await p.evaluate(() => !document.getElementById('item-0').classList.contains('done')),
      'a cleared question is no longer dimmed');
    ok(errs.length === 0, 'no JS errors (' + (errs.join(' | ') || 'none') + ')');
    await p.close();
  }

  console.log('\n== finishing a page moves to the next one ==');
  {
    const { p } = await open();
    for (let i = 0; i < 5; i++) await answer(p, i, 4);
    await new Promise(r => setTimeout(r, 700));
    ok(await p.evaluate(() => state.page === 1), 'the last answer on a page advances it');
    ok((await p.$$('.step')).length === 3, 'the three step cards stay on every step, not just the first');
    ok((await p.$$('.item.done')).length === 0, 'the new page starts with nothing dimmed');
    await p.close();
  }

  console.log('\n== archetypes, art and scoring ==');
  {
    const { p } = await open();
    const r = await p.evaluate(() => {
      const keys = Object.keys(ARCHETYPES), bad = [], fams = {};
      keys.forEach(function (k) {
        const a = ARCHETYPES[k];
        if (!a.name || !a.fam || !a.strength) bad.push(k + ':copy');
        if (!Array.isArray(a.lines) || a.lines.length !== 2) bad.push(k + ':lines');
        if (!FAMILIES[a.fam]) bad.push(k + ':family');
        if (!TM_ART[k]) bad.push(k + ':art');
        const svg = charSvg(k);
        if (!svg || svg.indexOf('<svg') !== 0 || svg.length < 1500) bad.push(k + ':svg');
        if (/undefined|null/.test(svg)) bad.push(k + ':svg-undefined');
        fams[a.fam] = (fams[a.fam] || 0) + 1;
      });
      const props = keys.map(function (k) { return TM_ART[k].prop; });

      const flat = function (v) { return new Array(ITEMS.length).fill(v); };
      const sN = scoreAnswers(flat(3)), sA = scoreAnswers(flat(5));
      const sM = scoreAnswers(ITEMS.map(function (it) {
        return it.d === 'N' ? (it.r ? 5 : 1) : (it.r ? 1 : 5);
      }));
      const T = ['ES', 'E', 'O', 'A', 'C'];
      const missing = {}, seen = {};
      for (let t = 0; t < 4000; t++) {
        const a = ITEMS.map(function () { return 1 + Math.floor(Math.random() * 5); });
        const s = scoreAnswers(a), key = archetypeKeyOf(s);
        seen[key] = 1;
        if (!ARCHETYPES[key] || !TM_ART[key]) missing[key] = 1;
        for (let z = 0; z < T.length; z++) {
          if (s[T[z]] < 1 || s[T[z]] > 5) missing['range:' + T[z]] = 1;
        }
      }
      const every = function (o, f) { return T.every(f); };
      return {
        n: keys.length, bad: bad, fams: fams, uniqProps: Object.keys(props.reduce(
          function (m, x) { m[x] = 1; return m; }, {})).length,
        neutral: every(sN, function (k) { return Math.abs(sN[k] - 3) < 1e-9; }),
        agreeAll: every(sA, function (k) { return Math.abs(sA[k] - 3) < 1e-9; }),
        max: every(sM, function (k) { return Math.abs(sM[k] - 5) < 1e-9; }),
        emptyES: scoreAnswers(flat(0)).ES,
        missing: Object.keys(missing), seen: Object.keys(seen).length
      };
    });
    ok(r.n === 10, '10 archetypes defined');
    ok(r.bad.length === 0, 'all 10 have copy + family + art + svg (' + (r.bad.join(', ') || 'clean') + ')');
    ok(Object.keys(r.fams).length === 4, 'four families used: ' + JSON.stringify(r.fams));
    ok(r.uniqProps === 10, 'every archetype holds a different object');
    ok(r.neutral, 'all-neutral answers -> exactly 3.0 on every trait');
    ok(r.agreeAll, 'agreeing with everything -> flat 3.0 (straightlining protection)');
    ok(r.max, 'max profile -> 5.0 on every trait');
    ok(r.emptyES === 0, 'no answers -> ES is 0, not 6');
    ok(r.missing.length === 0, '4000 random respondents: every result maps to real art, all scores in 1..5 ('
      + (r.missing.join(',') || 'clean') + ')');
    console.log('  distinct archetypes reached by random data:', r.seen);
    await p.close();
  }

  console.log('\n== restart ==');
  {
    const { p } = await fullRun(function () { return 4; });
    await p.click('#againBtn');
    await new Promise(r => setTimeout(r, 150));
    ok(await p.evaluate(() => state.page === 0), 'restart returns to the first page');
    ok((await p.$$('.step')).length === 3, 'the opener is shown again');
    ok((await p.$$('.item.done')).length === 0, 'no answers carried over');
    ok(await p.evaluate(() => statsSent === false && abandonSent === false && leadSent === false),
      'all send-once flags reset for the next student');
    await p.close();
  }

  await browser.close();
  console.log('\n' + (fail ? 'FAILED ' + fail : 'ALL ' + pass + ' CHECKS PASSED'));
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error('CRASH', e); process.exit(1); });
