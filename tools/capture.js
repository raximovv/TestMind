// Tests the email capture in real Chrome, with every outbound request intercepted
// so nothing actually reaches the Google Sheet.
const puppeteer = require('puppeteer-core');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PAGE = 'http://localhost:8765/test.html';
let pass = 0, fail = 0;
const ok = (c, m) => { c ? (pass++, console.log('  PASS ' + m)) : (fail++, console.log('  FAIL ' + m)); };

async function session(fakeNetworkFailure) {
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844 });
  const posts = [];
  await page.setRequestInterception(true);
  page.on('request', r => {
    if (r.url().indexOf('script.google.com') !== -1) {
      posts.push({ method: r.method(), body: r.postData() });
      return fakeNetworkFailure ? r.abort('failed') : r.respond({ status: 200, body: '{"ok":true}' });
    }
    r.continue();
  });
  const errors = [];
  page.on('pageerror', e => errors.push(String(e)));
  await page.goto(PAGE, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await new Promise(r => setTimeout(r, 600));
  await page.evaluate(() => {
    localStorage.clear();
    state.answers = ITEMS.map((it, i) => (i % 5) + 1);
    renderReport();
  });
  await new Promise(r => setTimeout(r, 300));
  return { browser, page, posts, errors };
}

(async () => {
  console.log('\n== nothing is sent just by looking at the result ==');
  {
    const { browser, page, posts, errors } = await session(false);
    const completed = posts.filter(p => (p.body || '').indexOf('"completed"') !== -1);
    const leads = posts.filter(p => (p.body || '').indexOf('"lead"') !== -1);
    ok(completed.length === 1, 'the anonymous "completed" row is sent once');
    ok(leads.length === 0, 'NO lead row sent before the student types anything');
    ok((completed[0].body || '').indexOf('Dilnoza') === -1, 'the anonymous row carries no name');
    ok((completed[0].body || '').indexOf('email') === -1, 'the anonymous row carries no email');
    ok(errors.length === 0, 'no JS errors (' + (errors[0] || 'none') + ')');

    console.log('\n== a bad address is rejected client-side ==');
    await page.type('#capEmail', 'not-an-email');
    await page.click('#capBtn');
    await new Promise(r => setTimeout(r, 250));
    ok(posts.filter(p => (p.body || '').indexOf('"lead"') !== -1).length === 0, 'invalid address sends nothing');
    const msg = await page.$eval('#capMsg', e => e.textContent);
    ok(msg.length > 0, 'shows an error message: "' + msg + '"');
    ok(await page.$eval('#capBtn', b => !b.disabled), 'button is re-usable after the error');

    console.log('\n== a good address is sent, once, with the right fields ==');
    await page.$eval('#capEmail', e => e.value = '');
    await page.type('#capEmail', 'dilnoza@example.com');
    await page.click('#capBtn');
    await page.waitForSelector('.capdone', { timeout: 8000 });
    const sent = posts.filter(p => (p.body || '').indexOf('"lead"') !== -1);
    ok(sent.length === 1, 'exactly one lead row sent');
    const body = JSON.parse(sent[0].body);
    ok(body.email === 'dilnoza@example.com', 'email present');
    ok(body.status === 'lead', 'status = lead');
    ok(!!body.archetype, 'archetype present so the right guide can be sent: ' + body.archetype);
    ok(!('age' in body), 'age NOT sent - the test never asks for one');
    ok(!('name' in body) && JSON.stringify(body).indexOf('Dilnoza') === -1, 'name NOT sent');
    ok(!body.answers, 'individual answers NOT sent');
    const done = await page.$eval('#capture', e => e.textContent);
    ok(done.indexOf('dilnoza@example.com') !== -1, 'confirmation shows the address back');
    await browser.close();
  }

  console.log('\n== network failure is reported honestly, not faked as success ==');
  {
    const { browser, page } = await session(true);
    await page.type('#capEmail', 'dilnoza@example.com');
    await page.click('#capBtn');
    await new Promise(r => setTimeout(r, 1200));
    const done = await page.$('.capdone');
    ok(!done, 'does NOT show a success state when the request failed');
    const msg = await page.$eval('#capMsg', e => e.textContent);
    ok(/urinib|tekshirib/.test(msg), 'shows a retry message: "' + msg + '"');
    ok(await page.$eval('#capBtn', b => !b.disabled), 'button re-enabled so they can retry');
    await browser.close();
  }

  console.log('\n' + (fail ? 'FAILED ' + fail : 'ALL ' + pass + ' CHECKS PASSED'));
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error('CRASH', e); process.exit(1); });
