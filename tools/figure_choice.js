/* Answering the figure-choice dialog, for the test suites.
 *
 * Since 2026-08-02 the last question is not the last step: an archetype with two
 * illustrations asks which one to draw, in a modal appended to <body> over the
 * finished page. renderReport() opens that modal and returns -- it does not paint
 * the report -- so any suite that calls renderReport() and then looks for the
 * result finds the question page still sitting there and fails in a way that
 * looks nothing like the actual cause.
 *
 * Two things to know when driving the test from a suite:
 *   - the modal lives OUTSIDE #app, so `.item` elements remain in the DOM behind
 *     it; "there are still questions on screen" is not a way to detect the end.
 *   - the page is adaptive, so questions are not at predictable item indices.
 *     Read `state.plan`, or read the ids off the page.
 */
'use strict';

/** Answer the dialog if it is open. Resolves true when it was. */
async function settleFigureChoice(p, gender, age) {
  if (!(await p.$('.fcwrap'))) return false;
  await p.click('.fcopt input[value="' + (gender || 'female') + '"]');
  await p.type('#fcage', String(age || 15));
  await new Promise(r => setTimeout(r, 80));
  await p.click('#fcgo');
  await new Promise(r => setTimeout(r, 500));
  return true;
}

/** Finish the test from wherever it is: renderReport, then the dialog. */
async function finishToReport(p, answers) {
  await p.evaluate(pattern => {
    state.answers = ITEMS.map((x, i) => (pattern ? pattern[i] : (i % 5) + 1));
    renderReport();
  }, answers || null);
  await new Promise(r => setTimeout(r, 250));
  await settleFigureChoice(p);
}

/** The ITEMS indices currently on screen, in the order they are shown. */
async function questionsOnPage(p) {
  return p.evaluate(() => Array.prototype.map.call(
    document.querySelectorAll('#app .item'), e => parseInt(e.id.slice(5), 10)));
}

module.exports = { settleFigureChoice, finishToReport, questionsOnPage };
