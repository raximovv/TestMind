// Does the result screen show the life analysis in the student's own language?
//
// The section used to be Uzbek-only and gated behind `TLANG === 'uz'`; it now
// loads a per-language pack asynchronously, which introduces two ways to fail
// that a static check cannot see: the pack never arrives, or it arrives after
// the report is already painted and nothing fills the slot. So this drives a
// real browser to the report in all three languages and reads what is on screen.
const puppeteer = require('puppeteer-core');
const path = require('path');
const { settleFigureChoice, finishToReport } = require('./figure_choice');

const BASE = 'http://localhost:8765/test.html';
const CHROME = process.env.CHROME ||
  'C:/Program Files/Google/Chrome/Application/chrome.exe';

// One bullet taken from each language's pack. Present on screen => that
// language's file was the one fetched and rendered.
const MARKER = {
  uz: 'Kuchli taraflaringiz',
  ru: 'Ваши сильные стороны',
  en: 'Your strengths',
};
const HEADING = { uz: 'Toʻliq tahlil', ru: 'Полный разбор', en: 'The full picture' };

// The directions block above «Yoʻnalishlar» must disclaim itself in words, not
// only by having dropped its numbers -- a reader who meets a list of jobs reads
// it as advice unless told otherwise. POINTER is the name of the section that
// IS allowed to rank, which the note has to hand off to.
const NOT_A_REC = { uz: /tavsiya emas/, ru: /не рекомендация/, en: /not a recommendation/ };
const POINTER = { uz: 'Yoʻnalishlar', ru: 'Направления', en: 'Directions' };

let pass = 0, fail = 0;
function check(name, ok, extra){
  if (ok) { console.log('  PASS ' + name); pass++; }
  else { console.log('  FAIL ' + name + (extra ? '  -> ' + extra : '')); fail++; }
}

async function run(){
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new' });
  for (const lang of ['uz', 'ru', 'en']){
    console.log('\n== ' + lang + ' ==');
    const p = await browser.newPage();
    const requested = [];
    p.on('request', r => { if (/life-\w+\.js/.test(r.url())) requested.push(path.basename(r.url())); });
    await p.goto(BASE + '?lang=' + lang, { waitUntil: 'networkidle0' });

    await finishToReport(p, new Array(60).fill(4));
    await settleFigureChoice(p, 'male', 15).catch(() => {});
    await p.waitForSelector('.lifefull', { timeout: 8000 }).catch(() => {});

    const got = await p.evaluate(() => {
      const slot = document.getElementById('lifeslot');
      return {
        slot: !!slot,
        text: slot ? slot.textContent : '',
        heads: document.querySelectorAll('.lifefull .lifehead').length,
        careers: document.querySelectorAll('.lifefull .career').length,
        pcts: [].map.call(document.querySelectorAll('.lifefull .carpct'), e => e.textContent),
        bars: document.querySelectorAll('.lifefull .carbar').length,
        note: (document.querySelector('.lifefull .cardisc') || {}).textContent || '',
      };
    });

    check('only the ' + lang + ' pack was fetched',
      requested.length === 1 && requested[0] === 'life-' + lang + '.js', requested.join(',') || 'none');
    check('the slot exists in the report', got.slot);
    check('heading is in ' + lang, got.text.indexOf(HEADING[lang]) >= 0);
    check('bullets are in ' + lang, got.text.indexOf(MARKER[lang]) >= 0);
    check('no other language leaked in',
      Object.keys(MARKER).filter(l => l !== lang).every(l => got.text.indexOf(MARKER[l]) < 0));
    check('four life headings', got.heads === 4, String(got.heads));
    check('five directions', got.careers === 5, String(got.careers));
    // The directions here must not rank or score anything: «Yoʻnalishlar» is one
    // scroll below and ranks careers from four signals rather than two traits.
    check('no fit percentage on any direction', got.pcts.length === 0, got.pcts.join(' '));
    check('no fit bar on any direction', got.bars === 0, String(got.bars));
    check('the note says it is not a recommendation', NOT_A_REC[lang].test(got.note), got.note.slice(0, 60));
    check('the note points at the ranked section', got.note.indexOf(POINTER[lang]) >= 0, got.note.slice(-60));
    await p.close();
  }

  // These directions used to carry a percentage, and the check here was that the
  // number came out identical in all three languages. There is no number now, so
  // the invariant that replaces it is the one that makes "this is not a ranking"
  // true rather than merely asserted: the same student gets the same COUNT of
  // directions everywhere, and within each language they are in alphabetical
  // order, which no reader can mistake for a ranking.
  const got = {};
  for (const lang of ['uz', 'ru', 'en']){
    const p = await browser.newPage();
    await p.goto(BASE + '?lang=' + lang, { waitUntil: 'networkidle0' });
    await finishToReport(p, new Array(60).fill(4));
    await settleFigureChoice(p, 'male', 15).catch(() => {});
    await p.waitForSelector('.lifefull', { timeout: 8000 }).catch(() => {});
    got[lang] = await p.evaluate(() =>
      [].map.call(document.querySelectorAll('.lifefull .carname'), e => e.textContent));
    await p.close();
  }
  console.log('\n== directions are unranked, and the same set in every language ==');
  check('uz count == ru count', got.uz.length === got.ru.length,
    got.uz.length + ' vs ' + got.ru.length);
  check('uz count == en count', got.uz.length === got.en.length,
    got.uz.length + ' vs ' + got.en.length);
  for (const lang of ['uz', 'ru', 'en'])
    check(lang + ' directions are alphabetical, not ranked',
      got[lang].join('|') === got[lang].slice().sort().join('|'), got[lang].join(', '));

  // A pack that arrives AFTER the report is already on screen. This is the whole
  // reason the slot exists, and on a school connection it is the normal case.
  console.log('\n== pack arrives after the report is painted ==');
  {
    const p = await browser.newPage();
    await p.setRequestInterception(true);
    p.on('request', r => {
      if (/life-\w+\.js/.test(r.url())) setTimeout(() => r.continue(), 3000);
      else r.continue();
    });
    await p.goto(BASE + '?lang=ru', { waitUntil: 'domcontentloaded' });
    await finishToReport(p, new Array(60).fill(4));
    await settleFigureChoice(p, 'male', 15).catch(() => {});
    const before = await p.evaluate(() => ({
      report: !!document.querySelector('#shareBox'),
      life: !!document.querySelector('.lifefull'),
      slotEmpty: (document.getElementById('lifeslot') || {}).innerHTML === '',
    }));
    check('report is usable before the pack lands', before.report);
    check('no half-drawn section while waiting', !before.life && before.slotEmpty);
    await p.waitForSelector('.lifefull', { timeout: 10000 }).catch(() => {});
    const after = await p.evaluate(() => ({
      life: !!document.querySelector('.lifefull'),
      ru: (document.getElementById('lifeslot') || {}).textContent.indexOf('Ваши сильные стороны') >= 0,
    }));
    check('section fills itself in on arrival', after.life);
    check('and it is the right language', after.ru);
    await p.close();
  }

  // A pack that never arrives at all: the report must stand on its own, with no
  // heading hanging over an empty box.
  console.log('\n== pack never arrives ==');
  {
    const p = await browser.newPage();
    await p.setRequestInterception(true);
    p.on('request', r => { if (/life-\w+\.js/.test(r.url())) r.abort(); else r.continue(); });
    await p.goto(BASE + '?lang=uz', { waitUntil: 'domcontentloaded' });
    await finishToReport(p, new Array(60).fill(4));
    await settleFigureChoice(p, 'male', 15).catch(() => {});
    const got = await p.evaluate(() => ({
      report: !!document.querySelector('#shareBox'),
      guide: !!document.getElementById('capture'),
      life: !!document.querySelector('.lifefull'),
      heading: !!document.querySelector('.lifetop'),
    }));
    check('the rest of the report still renders', got.report && got.guide);
    check('no life section', !got.life);
    check('and no orphan heading over an empty box', !got.heading);
    await p.close();
  }

  await browser.close();
  console.log('\n' + (fail ? fail + ' FAILED, ' : '') + pass + ' checks passed');
  process.exit(fail ? 1 : 0);
}

run().catch(e => { console.error(e); process.exit(1); });
