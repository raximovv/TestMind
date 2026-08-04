// The recommendation engine: correctness, conflicts, missing data, and the
// weighting experiment that chose the shipped numbers.
//
// Loads assets/recommend.js and assets/careers-data.js in a sandbox, so exactly
// the code the browser runs is what gets tested -- there is no second Python
// implementation to drift out of agreement with it.
//
//     node recommend_test.js            checks only
//     node recommend_test.js --weights  also prints the weighting comparison
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const ROOT = path.join(__dirname, '..');
const sandbox = { module: { exports: {} }, console: console };
vm.createContext(sandbox);
vm.runInContext(fs.readFileSync(path.join(ROOT, 'assets/careers-data.js'), 'utf8'), sandbox);
vm.runInContext(fs.readFileSync(path.join(ROOT, 'assets/recommend.js'), 'utf8'), sandbox);
const R = sandbox.module.exports;
const FAMILIES = sandbox.CAREER_FAMILIES;
const CAREERS = sandbox.CAREER_ENTRIES;
const MAJORS = sandbox.MAJOR_ENTRIES;
const NAMES = sandbox.TAXONOMY_NAMES;

let pass = 0, fail = 0;
const ok = (c, m) => { c ? (pass++, console.log('  PASS ' + m)) : (fail++, console.log('  FAIL ' + m)); };

// ---------------------------------------------------------------- helpers
const riasec = o => Object.assign({ R: 3, I: 3, A: 3, S: 3, E: 3, C: 3 }, o);
const vals = o => {                     // centred, as scoreValues() produces
  const base = { income: 0, stability: 0, learning: 0, creativity: 0, helping: 0,
                 leadership: 0, independence: 0, teamwork: 0, balance: 0, meaning: 0 };
  return Object.assign(base, o);
};
const marks = (o, scale) => {           // {subject: 2..5} -> the perf shape
  const out = {};
  for (const k in o) out[k] = { score: ((o[k] - 2) / 3), weight: scale === 'confidence' ? 0.6 : 1.0 };
  return out;
};
const big5 = o => Object.assign({ ES: 3, E: 3, O: 3, A: 3, C: 3 }, o);

function sig(p){
  return R.recSignals(p.riasec || null, p.values || null, p.subjects || null, p.big5 || null);
}
const nm = (kind, key) => NAMES.en[kind][key] || key;
const topN = (rows, n) => rows.slice(0, n).map(r => nm(r.kind || 'careers', r.key));

// ---------------------------------------------------------------- profiles
// Deliberately includes every conflict case the directive names.
const PROFILES = [
  { id: 1, label: 'Investigative + strong maths/CS, wants to learn',
    riasec: riasec({ I: 5, R: 4, C: 4, A: 2, S: 2, E: 2 }),
    values: vals({ learning: 1.2, independence: 0.6, income: 0.3, helping: -0.9, teamwork: -0.8 }),
    subjects: marks({ math: 5, cs: 5, physics: 4, literature: 3 }),
    big5: big5({ O: 4, C: 4, E: 2 }) },

  { id: 2, label: 'CONFLICT: Artistic interests, but maths/physics marks',
    riasec: riasec({ A: 5, S: 4, I: 2, R: 2, C: 2, E: 3 }),
    values: vals({ creativity: 1.3, independence: 0.5, stability: -0.9, income: -0.6 }),
    subjects: marks({ math: 5, physics: 5, cs: 4, art: 3 }),
    big5: big5({ O: 5, C: 3 }) },

  { id: 3, label: 'CONFLICT: Investigative interests, weak maths',
    riasec: riasec({ I: 5, R: 3, C: 3, A: 3, S: 2, E: 2 }),
    values: vals({ learning: 1.4, meaning: 0.5, income: -0.7 }),
    subjects: marks({ math: 2, physics: 3, biology: 4, literature: 4 }),
    big5: big5({ O: 4 }) },

  { id: 4, label: 'CONFLICT: Social interests, strong CS marks',
    riasec: riasec({ S: 5, A: 4, E: 4, I: 3, R: 2, C: 2 }),
    values: vals({ helping: 1.3, teamwork: 0.8, meaning: 0.6, income: -0.8 }),
    subjects: marks({ cs: 5, math: 5, biology: 3 }),
    big5: big5({ E: 4, A: 5 }) },

  { id: 5, label: 'CONFLICT: Enterprising, but wants stability above all',
    riasec: riasec({ E: 5, C: 4, S: 4, I: 2, R: 2, A: 2 }),
    values: vals({ stability: 1.4, balance: 0.8, income: 0.4, independence: -1.1 }),
    subjects: marks({ economics: 4, math: 4, english: 4 }),
    big5: big5({ E: 4, C: 4 }) },

  { id: 6, label: 'Quiet student who wants to run a business (must NOT be blocked)',
    riasec: riasec({ E: 5, C: 4, I: 3, A: 3, S: 2, R: 2 }),
    values: vals({ independence: 1.3, income: 1.0, leadership: 0.7, stability: -1.0 }),
    subjects: marks({ economics: 5, math: 4 }),
    big5: big5({ E: 1, ES: 2, C: 4 }) },

  { id: 7, label: 'Strong interests, NO subject data at all',
    riasec: riasec({ R: 5, I: 4, C: 3, A: 2, S: 2, E: 2 }),
    values: vals({ stability: 0.9, income: 0.7, learning: 0.4, creativity: -0.9 }),
    subjects: null,
    big5: big5({ C: 4 }) },

  { id: 8, label: 'Flat interests, strong subject data only',
    riasec: riasec({}),                               // liked everything equally
    values: vals({}),
    subjects: marks({ math: 5, cs: 5, physics: 5 }),
    big5: big5({}) },

  { id: 9, label: 'Only self-reported confidence, no real marks',
    riasec: riasec({ A: 5, E: 4, I: 3, S: 3, R: 2, C: 2 }),
    values: vals({ creativity: 1.2, independence: 0.6 }),
    subjects: marks({ art: 5, cs: 4, math: 3 }, 'confidence'),
    big5: big5({ O: 5 }) },

  { id: 10, label: 'Interests only — skipped values, subjects and personality',
    riasec: riasec({ C: 5, I: 4, E: 3, R: 3, S: 2, A: 2 }),
    values: null, subjects: null, big5: null },
];

// ============================================================ correctness
console.log('\n== the engine produces a usable ranking for every profile ==');
for (const p of PROFILES){
  const s = sig(p);
  const careers = R.recRank(CAREERS, s, 'career');
  const majors = R.recRank(MAJORS, s, 'major');
  ok(careers.length === Object.keys(CAREERS).length,
     'profile ' + p.id + ': every career scored (' + careers.length + ')');
  ok(majors.length === Object.keys(MAJORS).length,
     'profile ' + p.id + ': every major scored (' + majors.length + ')');
  ok(careers.every(r => r.score >= 0 && r.score <= 1),
     'profile ' + p.id + ': all scores within 0..1');
  ok(new Set(careers.map(r => r.band)).size >= 1, 'profile ' + p.id + ': bands assigned');
}

console.log('\n== missing data is dropped, not scored as zero ==');
{
  const noSub = sig(PROFILES[6]);
  const rows = R.recRank(CAREERS, noSub, 'career');
  ok(rows.every(r => r.used.indexOf('subjects') === -1),
     'no subject data -> the subject term is absent, not 0');
  ok(rows[0].score > 0.3, 'and the student still gets a real ranking (' + rows[0].score.toFixed(2) + ')');

  const only = sig(PROFILES[9]);
  const rows2 = R.recRank(CAREERS, only, 'career');
  ok(rows2.every(r => r.used.length === 1 && r.used[0] === 'riasec'),
     'interests only -> exactly one term used');
  ok(rows2[0].score >= 0 && rows2[0].score <= 1, 'and it still produces a valid score');

  const none = R.recRank(CAREERS, R.recSignals(null, null, null, null), 'career');
  ok(none.length === 0, 'no signals at all -> no recommendations, not a random order');
}

console.log('\n== a flat profile claims nothing ==');
{
  const flat = R.recRelative({ R: 3, I: 3, A: 3, S: 3, E: 3, C: 3 });
  ok(flat === null, 'liking everything equally expresses no preference');
  const s = sig(PROFILES[7]);
  const rows = R.recRank(CAREERS, s, 'career');
  ok(rows.every(r => r.used.indexOf('riasec') === -1),
     'so the interest term is dropped and the marks decide');
  ok(rows[0].family === 'cs' || rows[0].family === 'engineering',
     'strong maths/CS marks lead to a technical family (' + rows[0].family + ')');
}

console.log('\n== personality can never block a career ==');
{
  const quiet = sig(PROFILES[5]);
  const loud = sig({ ...PROFILES[5], big5: big5({ E: 5, ES: 4, C: 4 }) });
  const qRows = R.recRank(CAREERS, quiet, 'career');
  const lRows = R.recRank(CAREERS, loud, 'career');
  const qEnt = qRows.findIndex(r => r.key === 'entrepreneur');
  const lEnt = lRows.findIndex(r => r.key === 'entrepreneur');
  ok(qEnt >= 0 && qEnt < 5,
     'the quiet student still has entrepreneur in the top five (rank ' + (qEnt + 1) + ')');
  ok(Math.abs(qRows[qEnt].score - lRows[lEnt].score) < 0.05,
     'introversion moves entrepreneur by under 5 points ('
     + Math.abs(qRows[qEnt].score - lRows[lEnt].score).toFixed(3) + ')');
  const t = R.recPersonalityTerm(big5({ E: 1, C: 1 }), { E: 1 });
  ok(t >= 0.5, 'the personality term never falls below half (' + t + ')');
}

console.log('\n== majors weight academic performance more heavily than careers ==');
{
  ok(R.REC_WEIGHTS.major.subjects > R.REC_WEIGHTS.career.subjects,
     'subjects: major ' + R.REC_WEIGHTS.major.subjects + ' > career ' + R.REC_WEIGHTS.career.subjects);
  ok(R.REC_WEIGHTS.career.riasec > R.REC_WEIGHTS.major.riasec,
     'interests: career ' + R.REC_WEIGHTS.career.riasec + ' > major ' + R.REC_WEIGHTS.major.riasec);
  for (const kind of ['career', 'major']){
    const w = R.REC_WEIGHTS[kind];
    const sum = w.riasec + w.values + w.subjects + w.personality;
    ok(Math.abs(sum - 1) < 1e-9, kind + ' weights sum to 1.0 (' + sum.toFixed(2) + ')');
    ok(w.personality <= 0.10, kind + ': personality stays a small adjustment (' + w.personality + ')');
    ok(w.riasec >= 0.30, kind + ': interests remain a major signal (' + w.riasec + ')');
  }
  // The same student should be able to get a different lead for major than for
  // career -- otherwise the two models are decoration.
  let differs = 0;
  for (const p of PROFILES){
    const s = sig(p);
    const c = R.recRank(CAREERS, s, 'career')[0];
    const m = R.recRank(MAJORS, s, 'major')[0];
    if (c.family !== m.family) differs++;
  }
  ok(differs > 0, 'career and major leads genuinely diverge for some students (' + differs + '/10)');
}

console.log('\n== values separate careers that interests score identically ==');
{
  const base = { riasec: riasec({ E: 5, C: 4, S: 3, I: 3, R: 2, A: 2 }),
                 subjects: marks({ economics: 4, math: 4 }), big5: big5({}) };
  const indep = R.recRank(CAREERS, sig({ ...base,
    values: vals({ independence: 1.4, income: 0.8, stability: -1.2 }) }), 'career');
  const stable = R.recRank(CAREERS, sig({ ...base,
    values: vals({ stability: 1.4, balance: 0.9, independence: -1.2 }) }), 'career');
  const iEnt = indep.find(r => r.key === 'entrepreneur').score;
  const sEnt = stable.find(r => r.key === 'entrepreneur').score;
  ok(iEnt > sEnt, 'entrepreneur scores higher for a student who wants independence ('
     + iEnt.toFixed(3) + ' vs ' + sEnt.toFixed(3) + ')');
  ok(iEnt - sEnt > 0.03, 'and the difference is large enough to matter ('
     + (iEnt - sEnt).toFixed(3) + ')');
  // A stability-flavoured entry should climb when stability is what the student
  // wants. industrial_engineer carries the engineering family's stability lean.
  const iInd = indep.findIndex(r => r.key === 'industrial_engineer');
  const sInd = stable.findIndex(r => r.key === 'industrial_engineer');
  ok(sInd < iInd, 'industrial engineer rises for the stability-seeking student (rank '
     + (sInd + 1) + ' vs ' + (iInd + 1) + ')');
  // KNOWN LIMITATION, asserted so it is not forgotten: entries that inherit
  // their family's values move together, so values currently discriminate
  // BETWEEN families far more than within one. Only the five ENTRY_VALUES
  // overrides separate siblings. Widening those is the tuning job once real
  // data exists.
  const iGap = iEnt - indep.find(r => r.key === 'operations_manager').score;
  const sGap = sEnt - stable.find(r => r.key === 'operations_manager').score;
  ok(Math.abs(iGap - sGap) < 1e-6,
     'siblings inheriting family values move in lockstep (documented limitation)');
}

console.log('\n== self-reported marks count for less than real ones ==');
{
  const real = R.recSubjectFit(marks({ math: 5, cs: 5 }), { math: 0.5, cs: 0.5 });
  const self = R.recSubjectFit(marks({ math: 5, cs: 5 }, 'confidence'), { math: 0.5, cs: 0.5 });
  ok(Math.abs(real - self) < 1e-9, 'the FIT itself is the same (both are top marks)');
  const mixed = R.recSubjectFit(
    { math: { score: 1.0, weight: 0.6 }, cs: { score: 0.0, weight: 1.0 } },
    { math: 0.5, cs: 0.5 });
  ok(mixed < 0.5, 'but a real low mark outweighs a self-reported high one (' + mixed.toFixed(2) + ')');
  const thin = R.recSubjectFit(marks({ art: 5 }), { math: 0.4, cs: 0.4, physics: 0.2 });
  ok(thin === null, 'a subject the entry does not use contributes nothing at all');
}

console.log('\n== conflicts are detected, not hidden ==');
{
  const p = PROFILES[1];                              // artistic + maths marks
  const s = sig(p);
  const implied = { I: 0.9, R: 0.7, C: 0.6, A: 0.3, S: 0.2, E: 0.2 };
  const c = R.recConflicts(s, implied);
  ok(c.length > 0, 'the artistic/technical split is reported (' + c.length + ' scales)');
  ok(c.some(x => x.scale === 'A' && x.side === 'interest'),
     'and it says the ARTISTIC side is the interest, not the marks');
  const agree = R.recConflicts(sig(PROFILES[0]),
    { I: 1.0, R: 0.7, C: 0.6, A: 0.2, S: 0.1, E: 0.1 });
  ok(agree.length === 0, 'a student whose marks match their interests gets no false conflict');
}

console.log('\n== explanations name the signals that actually decided ==');
{
  const s = sig(PROFILES[0]);
  const row = R.recRank(CAREERS, s, 'career')[0];
  const d = R.recDrivers(row, 'career');
  ok(d.length >= 2, 'more than one driver reported (' + d.length + ')');
  ok(d[0].contribution >= d[d.length - 1].contribution, 'sorted by contribution, not raw value');
  ok(d[0].part === 'riasec' || d[0].part === 'subjects',
     'the lead driver is a real signal, not personality (' + d[0].part + ')');
  const pers = d.find(x => x.part === 'personality');
  ok(!pers || pers.contribution <= 0.08,
     'personality is never the biggest contributor');
}

console.log('\n== no fake precision reaches the caller ==');
{
  const rows = R.recRank(CAREERS, sig(PROFILES[0]), 'career');
  const bands = new Set(rows.map(r => r.band));
  ok([...bands].every(b => ['strong', 'explore', 'alternative'].indexOf(b) >= 0),
     'bands are the three named ones only');
  const tiedRows = R.recRank(CAREERS, sig(PROFILES[9]), 'career');
  ok(tiedRows.length > 0, 'even a single-signal student is banded');
}

// ======================================================== H4: weightings
if (process.argv.indexOf('--weights') !== -1){
  console.log('\n\n================ WEIGHTING COMPARISON ================');
  const SCHEMES = {
    'A directive career hypothesis': { riasec: 0.525, values: 0.225, subjects: 0.225, personality: 0.075 },
    'B interests dominant':          { riasec: 0.60, values: 0.20, subjects: 0.15, personality: 0.05 },
    'C shipped (career)':            { riasec: 0.50, values: 0.22, subjects: 0.20, personality: 0.08 },
    'D evidence-led':                { riasec: 0.40, values: 0.20, subjects: 0.32, personality: 0.08 },
    'E subjects dominant':           { riasec: 0.30, values: 0.15, subjects: 0.47, personality: 0.08 },
    'F no values':                   { riasec: 0.60, values: 0.00, subjects: 0.32, personality: 0.08 },
  };
  const save = JSON.parse(JSON.stringify(R.REC_WEIGHTS));
  console.log('\nTop career family per profile under each scheme:\n');
  const hdr = Object.keys(SCHEMES).map(k => k.slice(0, 14).padEnd(15)).join('');
  console.log('profile'.padEnd(46) + hdr);
  for (const p of PROFILES){
    let line = ('  ' + p.id + ' ' + p.label).slice(0, 45).padEnd(46);
    for (const k in SCHEMES){
      R.REC_WEIGHTS.career = SCHEMES[k];
      const top = R.recRank(CAREERS, sig(p), 'career')[0];
      line += (top ? top.family : '-').padEnd(15);
    }
    console.log(line);
  }
  // How far each scheme moves the ranking away from interests-only, which is
  // the closest thing we have to a ground truth for a fifteen-year-old.
  console.log('\nMean rank shift vs interests-only, and how often subjects override interests:');
  R.REC_WEIGHTS.career = { riasec: 1, values: 0, subjects: 0, personality: 0 };
  const baseline = {};
  for (const p of PROFILES) baseline[p.id] = R.recRank(CAREERS, sig(p), 'career').map(r => r.key);
  for (const k in SCHEMES){
    R.REC_WEIGHTS.career = SCHEMES[k];
    let shift = 0, flips = 0, n = 0;
    for (const p of PROFILES){
      const rank = R.recRank(CAREERS, sig(p), 'career').map(r => r.key);
      for (let i = 0; i < rank.length; i++){
        shift += Math.abs(i - baseline[p.id].indexOf(rank[i])); n++;
      }
      if (rank[0] !== baseline[p.id][0]) flips++;
    }
    console.log('  ' + k.padEnd(32) + 'mean shift ' + (shift / n).toFixed(2).padStart(5)
                + '   top-1 changed for ' + flips + '/10 students');
  }
  R.REC_WEIGHTS.career = save.career; R.REC_WEIGHTS.major = save.major;

  console.log('\n\n================ WHAT EACH STUDENT SEES ================');
  for (const p of PROFILES){
    const s = sig(p);
    const fams = R.recRankFamilies(FAMILIES, s, 3);
    const cs = R.recRank(CAREERS, s, 'career', 4);
    const ms = R.recRank(MAJORS, s, 'major', 4);
    const icon = b => b === 'strong' ? 'STRONG ' : b === 'explore' ? 'EXPLORE' : 'ALT    ';
    console.log('\n--- ' + p.id + '. ' + p.label);
    console.log('    areas  : ' + fams.map(f => NAMES.en.families[f.key] + ' [' + icon(f.band).trim() + ']').join(' | '));
    console.log('    majors : ' + ms.map(m => icon(m.band) + NAMES.en.majors[m.key]).join('\n             '));
    console.log('    careers: ' + cs.map(c => icon(c.band) + NAMES.en.careers[c.key]).join('\n             '));
    const d = R.recDrivers(cs[0], 'career');
    console.log('    why    : ' + d.map(x => x.part + ' ' + x.value.toFixed(2)).join(', '));
  }
}

console.log('\n' + (fail ? fail + ' FAILED, ' : '') + pass + ' checks passed');
process.exit(fail ? 1 : 0);
