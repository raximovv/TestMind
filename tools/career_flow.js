// The two-section test: everything that only breaks at the seam.
//
// e2e walks a clean run start to finish, which the career block already passes.
// What it cannot see is what happens AROUND that block: a student who closes the
// tab inside it, a draft written by the old 50-item build, a result page reached
// with the career section half answered, a tie that has to be disclosed, and a
// language switched mid-test. Each of those is a place where the personality
// scores could be corrupted or the career section could silently vanish, and
// every one of them would look completely normal on screen.
//
//     node career_flow.js
const puppeteer = require('puppeteer-core');
const { settleFigureChoice } = require('./figure_choice');

const CHROME = process.env.CHROME || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PAGE = 'http://localhost:8765/test.html';

let pass = 0, fail = 0;
const ok = (c, m) => { c ? (pass++, console.log('  PASS ' + m)) : (fail++, console.log('  FAIL ' + m)); };

// Answer the personality section forward until the career block starts, leaving
// the career questions untouched. Runs INSIDE the page, so it is installed on
// window rather than closed over from here.
const INSTALL = () => {
  window.TO_CAREER = function(){
    for (var g = 0; g < 40; g++){
      var c = careerStartsAt();
      if (c >= 0){ state.page = Math.floor(c / PAGE_SIZE); renderPage(); return true; }
      for (var k = 0; k < state.plan.length; k++)
        if (!state.answers[state.plan[k]]) state.answers[state.plan[k]] = 3 + (k % 3);
      if (!extendPlan()) return false;
    }
    return false;
  };
};

async function open(browser, lang){
  const p = await browser.newPage();
  await p.setViewport({ width: 390, height: 844 });
  const errs = [];
  p.on('pageerror', e => errs.push(String(e)));
  await p.goto(PAGE + (lang ? '?lang=' + lang : ''), { waitUntil: 'networkidle0' });
  await p.evaluate(INSTALL);
  p.__errs = errs;
  p.__reinstall = () => p.evaluate(INSTALL);   // after any reload/navigation
  return p;
}

(async () => {
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new', args: ['--no-sandbox'] });

  // ---------------------------------------------------------------- resume
  // The draft now has to carry `stage` as well as `plan`. Without it a resumed
  // student is handed the career core a second time, or the test ends early.
  console.log('\n== a student who leaves inside the career block comes back to it ==');
  {
    const p = await open(browser);
    const before = await p.evaluate(() => {
      localStorage.clear();
      TO_CAREER();
      const c = careerStartsAt();
      // answer the first three career questions, then "close the tab"
      for (let k = c; k < c + 3; k++) state.answers[state.plan[k]] = 4;
      saveDraft();
      return { stage: state.stage, plan: state.plan.length, page: state.page,
               answered: state.answers.filter(v => v > 0).length, careerAt: c };
    });
    await p.reload({ waitUntil: 'networkidle0' });
    await p.__reinstall();
    const after = await p.evaluate(() => {
      const d = loadDraft();
      return d && { stage: d.stage, plan: d.plan.length,
                    answered: d.answers.filter(v => v > 0).length };
    });
    ok(!!after, 'the draft survives a reload');
    ok(after && after.plan === before.plan, 'plan length preserved (' + (after && after.plan) + ')');
    ok(after && after.stage === before.stage, 'stage preserved (' + (after && after.stage) + ')');
    ok(after && after.answered === before.answered,
       'every answer preserved, career ones included (' + (after && after.answered) + ')');
    // and resuming must not re-append the career core
    const resumed = await p.evaluate(() => {
      const d = loadDraft();
      state.answers = d.answers.slice(); state.plan = d.plan.slice();
      state.stage = d.stage; state.page = 0;
      const wasPlan = state.plan.length;
      const grew = extendPlan();
      return { wasPlan, nowPlan: state.plan.length, grew,
               careerItems: state.plan.filter(i => ITEMS[i].sec === 'c').length };
    });
    ok(resumed.careerItems === 30 || resumed.careerItems === 48,
       'career block appears exactly once after resume (' + resumed.careerItems + ' items)');
    ok(p.__errs.length === 0, 'no JS errors (' + (p.__errs[0] || 'none') + ')');
    await p.close();
  }

  // ------------------------------------------------------------ old drafts
  // A draft written by the 50-item build indexes an ITEMS array that no longer
  // exists. It must be discarded, not replayed against the new bank.
  console.log('\n== a draft from the old 50-item build is discarded, not misread ==');
  {
    const p = await open(browser);
    const r = await p.evaluate(() => {
      localStorage.setItem('testmind_draft_v1', JSON.stringify({
        answers: new Array(50).fill(3), page: 4,
        plan: [0,1,2,3,4,5,6,7,8,9], aid: 'old', ts: Date.now()
      }));
      const d = loadDraft();
      return { d: d, items: ITEMS.length };
    });
    ok(r.d === null, 'the stale draft is rejected (bank is now ' + r.items + ' items)');
    ok(p.__errs.length === 0, 'no JS errors (' + (p.__errs[0] || 'none') + ')');
    await p.close();
  }

  console.log('\n== a corrupted stage is repaired rather than trusted ==');
  {
    const p = await open(browser);
    const r = await p.evaluate(() => {
      localStorage.clear();
      TO_CAREER();
      saveDraft();
      const raw = JSON.parse(localStorage.getItem('testmind_draft_v1'));
      raw.stage = 'banana';
      localStorage.setItem('testmind_draft_v1', JSON.stringify(raw));
      const d = loadDraft();
      return d && { stage: d.stage, plan: d.plan.length };
    });
    ok(!!r, 'the draft still loads');
    ok(r && typeof r.stage === 'number' && r.stage >= 0 && r.stage <= 3,
       'stage repaired to a real value (' + (r && r.stage) + ')');
    // derived from a plan that already contains career items => career core done
    ok(r && r.stage === 2, 'derived stage says the career core has already been asked');
    await p.close();
  }

  // ------------------------------------------------- partial / missing data
  console.log('\n== the result page with the career block half answered ==');
  {
    const p = await open(browser);
    await p.evaluate(() => {
      localStorage.clear();
      TO_CAREER();
      const c = careerStartsAt();
      for (let k = c; k < c + 10; k++) state.answers[state.plan[k]] = 4;  // 10 of 30
      renderReport();
    });
    await settleFigureChoice(p).catch(() => {});
    await new Promise(r => setTimeout(r, 300));
    const r = await p.evaluate(() => ({
      career: !!document.querySelector('.cfull'),
      hero: !!document.querySelector('.hero'),
      answered: careerAnswered(state.answers)
    }));
    ok(r.hero, 'the personality result still renders');
    ok(!r.career, 'NO interest profile from ' + r.answered + ' answers');
    ok(p.__errs.length === 0, 'no JS errors (' + (p.__errs[0] || 'none') + ')');
    await p.close();
  }

  console.log('\n== ...and with no career answers at all ==');
  {
    const p = await open(browser);
    await p.evaluate(() => {
      localStorage.clear();
      for (let k = 0; k < state.plan.length; k++) state.answers[state.plan[k]] = 3 + (k % 3);
      renderReport();
    });
    await settleFigureChoice(p).catch(() => {});
    await new Promise(r => setTimeout(r, 300));
    const r = await p.evaluate(() => ({
      career: !!document.querySelector('.cfull'),
      hero: !!document.querySelector('.hero'),
      guide: !!document.getElementById('capture')
    }));
    ok(r.hero && r.guide, 'the rest of the report is intact');
    ok(!r.career, 'no interest profile, no empty bars');
    await p.close();
  }

  // ------------------------------------------------------------------ ties
  console.log('\n== near-tie disclosure ==');
  {
    const p = await open(browser);
    const tie = await p.evaluate(() => {
      localStorage.clear();
      TO_CAREER();
      // A and S identical, everything else clearly lower.
      const pref = { R: 2, I: 2, A: 5, S: 5, E: 2, C: 1 };
      for (let g = 0; g < 10; g++){
        for (let k = 0; k < state.plan.length; k++){
          const qi = state.plan[k];
          if (ITEMS[qi].sec === 'c') state.answers[qi] = pref[ITEMS[qi].s];
        }
        if (!extendPlan()) break;
      }
      renderReport();
      return null;
    });
    await settleFigureChoice(p).catch(() => {});
    await new Promise(r => setTimeout(r, 300));
    const r = await p.evaluate(() => {
      const tops = [].map.call(document.querySelectorAll('.ctop'), e => e.textContent);
      const names = [].map.call(document.querySelectorAll('.cprof .carname'), e => e.textContent);
      return { tops, names, body: tops.join(' ') };
    });
    ok(r.names.length === 6, 'all six areas shown (' + r.names.length + ')');
    ok(r.body.indexOf(r.names[1]) !== -1,
       'the tied second area is named in the disclosure');
    ok(r.tops.length >= 2, 'the age caveat is present as well');
    await p.close();
  }

  console.log('\n== a clear winner gets NO tie disclosure ==');
  {
    const p = await open(browser);
    await p.evaluate(() => {
      localStorage.clear();
      TO_CAREER();
      const pref = { R: 1, I: 1, A: 5, S: 1, E: 1, C: 1 };
      for (let g = 0; g < 10; g++){
        for (let k = 0; k < state.plan.length; k++){
          const qi = state.plan[k];
          if (ITEMS[qi].sec === 'c') state.answers[qi] = pref[ITEMS[qi].s];
        }
        if (!extendPlan()) break;
      }
      renderReport();
    });
    await settleFigureChoice(p).catch(() => {});
    await new Promise(r => setTimeout(r, 300));
    const r = await p.evaluate(() => {
      const names = [].map.call(document.querySelectorAll('.cprof .carname'), e => e.textContent);
      const first = (document.querySelector('.ctop') || {}).textContent || '';
      return { second: names[1], first };
    });
    ok(r.first.indexOf(r.second) === -1,
       'the runner-up is NOT named when it is not close');
    await p.close();
  }

  // --------------------------------------------------------- no Holland code
  // A hard product rule, so it is asserted rather than trusted to review.
  console.log('\n== no ordered Holland code anywhere on the result ==');
  {
    const p = await open(browser);
    await p.evaluate(() => {
      localStorage.clear();
      TO_CAREER();
      const pref = { R: 5, I: 4, A: 3, S: 2, E: 2, C: 1 };
      for (let g = 0; g < 10; g++){
        for (let k = 0; k < state.plan.length; k++){
          const qi = state.plan[k];
          if (ITEMS[qi].sec === 'c') state.answers[qi] = pref[ITEMS[qi].s];
        }
        if (!extendPlan()) break;
      }
      renderReport();
    });
    await settleFigureChoice(p).catch(() => {});
    await new Promise(r => setTimeout(r, 300));
    const txt = await p.evaluate(() => (document.querySelector('.cfull') || {}).textContent || '');
    ok(!/\b[RIASEC]{3}\b/.test(txt), 'no three-letter code printed');
    await p.close();
  }

  // ------------------------------------------------------ score isolation
  console.log('\n== career answers never touch the Big Five scores ==');
  {
    const p = await open(browser);
    const r = await p.evaluate(() => {
      const only = new Array(ITEMS.length).fill(0);
      for (let i = CAREER_START; i < ITEMS.length; i++) only[i] = 5;
      const s = scoreAnswers(only);
      // ...and personality answers must not move the interest profile
      const pers = new Array(ITEMS.length).fill(0);
      for (let i = 0; i < CAREER_START; i++) pers[i] = 5;
      const c = scoreCareer(pers);
      return { s, c };
    });
    ok(Object.keys(r.s).every(k => r.s[k] === 0),
       'Big Five from career answers alone is all zero');
    ok(Object.keys(r.c).every(k => r.c[k] === 0),
       'interest profile from personality answers alone is all zero');
    await p.close();
  }

  // -------------------------------------------------------- language switch
  console.log('\n== switching language mid-test keeps the answers ==');
  {
    const p = await open(browser, 'uz');
    const before = await p.evaluate(() => {
      localStorage.clear();
      TO_CAREER();
      const c = careerStartsAt();
      for (let k = c; k < c + 5; k++) state.answers[state.plan[k]] = 4;
      saveDraft();
      return { answered: state.answers.filter(v => v > 0).length, plan: state.plan.length };
    });
    await p.goto(PAGE + '?lang=ru', { waitUntil: 'networkidle0' });
    await p.__reinstall();
    const after = await p.evaluate(() => {
      const d = loadDraft();
      return d && { answered: d.answers.filter(v => v > 0).length, plan: d.plan.length,
                    lang: document.documentElement.getAttribute('lang') };
    });
    ok(!!after, 'the draft survives the language change');
    ok(after && after.answered === before.answered,
       'no answers lost (' + (after && after.answered) + ' of ' + before.answered + ')');
    ok(after && after.plan === before.plan, 'the plan is unchanged');
    ok(after && after.lang === 'ru', 'the page really did switch to ru');
    await p.close();
  }

  // ------------------------------------------------ guide language disclosure
  // The PDF guides are Uzbek-only. A Russian student was previously told "Ваше
  // полное руководство готово", offered "Скачать руководство (PDF)", and handed
  // a document in a language they may not read. The warning has to appear BEFORE
  // the button, and before the email field, since both deliver the same file.
  console.log('\n== the Uzbek-only guide is disclosed on RU/EN before the download ==');
  for (const [lang, must] of [['uz', null], ['ru', 'узбекск'], ['en', 'Uzbek']]) {
    const p = await open(browser, lang);
    await p.evaluate(() => {
      localStorage.clear();
      for (let k = 0; k < state.plan.length; k++) state.answers[state.plan[k]] = 3 + (k % 3);
      renderReport();
    });
    await settleFigureChoice(p).catch(() => {});
    await new Promise(r => setTimeout(r, 300));
    const r = await p.evaluate(() => {
      const note = document.querySelector('.caplang');
      const btn = document.querySelector('.btn.pdf');
      if (!note) return { has: false };
      // "before" means earlier in document order, not merely present somewhere.
      return { has: true, text: note.textContent,
               beforeBtn: !!(btn && (note.compareDocumentPosition(btn) & 4)) };
    });
    if (must === null){
      ok(!r.has, lang + ': no note (the guide is already in this language)');
    } else {
      ok(r.has, lang + ': the note is shown');
      ok(r.has && r.text.indexOf(must) !== -1,
         lang + ': it names the language -> "' + (r.text || '') + '"');
      ok(r.has && r.beforeBtn, lang + ': it appears BEFORE the download button');
    }
    await p.close();
  }

  await browser.close();
  console.log('\n' + (fail ? fail + ' FAILED, ' : '') + pass + ' checks passed');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error('CRASH', e); process.exit(1); });
