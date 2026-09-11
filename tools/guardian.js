// The parental acknowledgment on the sign-up dialog.
//
// The point of the box is that it BLOCKS, so most of this is about proving that
// nothing reaches Supabase until it is ticked -- and that it is not in the way
// of someone who already has an account.
//
//   node tools/guardian.js
const puppeteer = require('./node_modules/puppeteer-core');

const CHROME = process.env.CHROME || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const BASE = process.env.BASE || 'http://localhost:8765/';

let pass = 0, fail = 0;
const ok = (c, m) => { c ? (pass++, console.log('  PASS ' + m)) : (fail++, console.log('  FAIL ' + m)); };
const wait = (ms) => new Promise((r) => setTimeout(r, ms));

const LANGS = [
  ['uz', '18 yoshga to', 'Davom etish uchun'],
  ['ru', '\u0415\u0441\u043b\u0438 \u043c\u043d\u0435', '\u041e\u0442\u043c\u0435\u0442\u044c\u0442\u0435'],
  ['en', 'If I am under 18', 'Please tick this box'],
];

// Open the dialog in one mode and report what the reader is shown.
async function open(page, mode) {
  await page.evaluate((m) => { authMode = m; renderAuth(true); }, mode);
  await wait(220);
  return page.evaluate(() => {
    const box = document.getElementById('authGuardian');
    const label = box && box.closest('.authcheck');
    const r = label ? label.getBoundingClientRect() : null;
    return {
      present: !!box,
      text: label ? label.textContent.trim() : '',
      // The whole sentence is the target, not just the 20px square.
      targetW: r ? r.width : 0, targetH: r ? r.height : 0,
      // It sits above the button it guards.
      aboveButton: label
        ? label.getBoundingClientRect().bottom
          <= document.getElementById('authGo').getBoundingClientRect().top + 1
        : null,
    };
  });
}

(async () => {
  const browser = await puppeteer.launch({
    executablePath: CHROME, headless: 'new',
    args: ['--no-sandbox', '--blink-settings=preferredColorScheme=1'],
  });

  for (const [lang, sentence, errText] of LANGS) {
    const page = await browser.newPage();
    await page.setViewport({ width: 1100, height: 900 });

    // Every call Supabase would receive, refused and counted.
    const calls = [];
    await page.setRequestInterception(true);
    page.on('request', (r) => {
      if (r.url().indexOf('supabase.co') >= 0) { calls.push(r.url()); return r.abort(); }
      r.continue();
    });
    const errors = [];
    page.on('pageerror', (e) => errors.push(String(e)));
    // A Google sign-in leaves the page, so navigations are counted too.
    let navigated = 0;
    page.on('framenavigated', (f) => { if (f === page.mainFrame()) navigated++; });

    await page.goto(BASE + 'test.html?lang=' + lang, { waitUntil: 'networkidle0' });
    await wait(250);
    navigated = 0;

    console.log('\n== ' + lang + ' ==');

    // ---- sign-up: the box is there and says the right thing ---------------
    const up = await open(page, 'signup');
    ok(up.present, 'sign-up shows the acknowledgment');
    ok(up.text.indexOf(sentence) === 0, `in ${lang} ("${up.text.slice(0, 46)}...")`);
    ok(up.aboveButton === true, 'it sits above the button it guards');
    ok(up.targetH >= 20 && up.targetW > 200,
       `the whole sentence is the tap target (${up.targetW.toFixed(0)}x${up.targetH.toFixed(0)})`);

    // ---- submitting without it -------------------------------------------
    await page.type('#authEmail', 'nm-guardian-test@example.com');
    await page.type('#authPass', 'correcthorse');
    calls.length = 0;
    await page.click('#authGo');
    await wait(400);
    const blocked = await page.evaluate(() => ({
      err: document.getElementById('authErr').textContent.trim(),
      ok: document.getElementById('authErr').classList.contains('ok'),
      focused: document.activeElement && document.activeElement.id,
      buttonEnabled: !document.getElementById('authGo').disabled,
    }));
    ok(calls.length === 0, `nothing is sent to Supabase (${calls.length} calls)`);
    ok(blocked.err.indexOf(errText) === 0, `it says why ("${blocked.err}")`);
    ok(!blocked.ok, 'and says it as an error, not a confirmation');
    ok(blocked.focused === 'authGuardian', 'focus moves to the box');
    ok(blocked.buttonEnabled, 'the button is still usable, not stuck disabled');

    // ---- the Google button is behind the same gate ------------------------
    calls.length = 0;
    navigated = 0;
    await page.click('#authGoogle');
    await wait(500);
    const g = await page.evaluate(() => ({
      disabled: document.getElementById('authGoogle').disabled,
      err: document.getElementById('authErr').textContent.trim(),
    }));
    ok(navigated === 0 && calls.length === 0, 'Google does not leave the page either');
    ok(!g.disabled, 'and the Google button is not left dead');
    ok(g.err.indexOf(errText) === 0, 'with the same explanation');

    // ---- ticking it lets the sign-up through ------------------------------
    await page.click('#authGuardian');
    calls.length = 0;
    await page.click('#authGo');
    await wait(700);
    ok(calls.length > 0 && calls.some((u) => u.indexOf('/auth/v1/signup') >= 0),
       `ticked, the sign-up is attempted (${calls.length} call${calls.length === 1 ? '' : 's'})`);

    // ---- sign-in is not asked ---------------------------------------------
    const inMode = await open(page, 'signin');
    ok(!inMode.present, 'sign-in does not ask -- the account was acknowledged when it was made');

    ok(!errors.length, 'no page errors' + (errors.length ? ': ' + errors[0] : ''));
    await page.close();
  }

  // ---- dark mode and a phone --------------------------------------------
  for (const [theme, w, h] of [['dark', 1100, 900], ['light', 390, 780]]) {
    const page = await browser.newPage();
    await page.setViewport({ width: w, height: h, isMobile: w < 500, deviceScaleFactor: 2 });
    await page.setRequestInterception(true);
    page.on('request', (r) => (r.url().indexOf('supabase.co') >= 0 ? r.abort() : r.continue()));
    await page.goto(BASE + 'test.html', { waitUntil: 'networkidle0' });
    await page.evaluate((t) => localStorage.setItem('naseebmind_theme_v1', t), theme);
    await page.reload({ waitUntil: 'networkidle0' });
    await wait(250);
    await open(page, 'signup');
    const seen = await page.evaluate(() => {
      const box = document.getElementById('authGuardian');
      const label = box.closest('.authcheck');
      const cs = getComputedStyle(label);
      const r = label.getBoundingClientRect();
      const dialog = document.querySelector('.authdialog').getBoundingClientRect();
      return {
        color: cs.color, accent: getComputedStyle(box).accentColor,
        // Inside the dialog, not spilling out of it.
        inside: r.left >= dialog.left - 1 && r.right <= dialog.right + 1,
        // And the button below it is still reachable without scrolling past.
        buttonVisible: document.getElementById('authGo').getBoundingClientRect().bottom
                       <= window.innerHeight + 1,
      };
    });
    console.log(`\n== ${theme} @ ${w}px ==`);
    ok(seen.inside, `the row stays inside the dialog (colour ${seen.color}, accent ${seen.accent})`);
    ok(seen.buttonVisible, 'the sign-up button is still on screen below it');
    await page.screenshot({ path: `tools/build/guardian-${theme}-${w}.png` });
    await page.close();
  }

  console.log('\n  ' + pass + ' passed' + (fail ? ', ' + fail + ' FAILED' : ''));
  await browser.close();
  process.exit(fail ? 1 : 0);
})();
