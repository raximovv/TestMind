// What the taxonomy can and cannot currently answer, measured rather than assumed.
//
// Two questions the recommendation report raised and could not answer from
// inspection:
//   1. Which interest profiles does the populated taxonomy actually serve? A
//      student whose strongest area has no family leading on it still gets a
//      confident-looking recommendation, and that is an artifact of coverage.
//   2. Which work-value dimensions actually move a ranking? Ten dimensions of
//      one item each is weak; if only some of them do any work, those are the
//      ones worth a second item, and the rest can stay single.
//
//     node coverage_audit.js
const fs = require('fs'), path = require('path'), vm = require('vm');

const ROOT = path.join(__dirname, '..');
const sb = { module: { exports: {} }, console: console };
vm.createContext(sb);
vm.runInContext(fs.readFileSync(path.join(ROOT, 'assets/careers-data.js'), 'utf8'), sb);
vm.runInContext(fs.readFileSync(path.join(ROOT, 'assets/recommend.js'), 'utf8'), sb);
const R = sb.module.exports, FAM = sb.CAREER_FAMILIES, CAR = sb.CAREER_ENTRIES;

const SCALES = ['R', 'I', 'A', 'S', 'E', 'C'];
const DIMS = ['income', 'stability', 'learning', 'creativity', 'helping',
              'leadership', 'independence', 'teamwork', 'balance', 'meaning'];

// ------------------------------------------------------------ 1. coverage
console.log('=== which interests the populated taxonomy can serve ===\n');
const lead = {};
for (const f in FAM){
  const p = FAM[f].riasec;
  const top = Object.keys(p).sort((a, b) => p[b] - p[a])[0];
  (lead[top] = lead[top] || []).push(f);
}
for (const s of SCALES){
  const fams = lead[s] || [];
  console.log('  ' + s + '  ' + (fams.length ? 'led by ' + fams.join(', ') : 'NO POPULATED FAMILY LEADS ON THIS'));
}

// A student who is strongest on each scale in turn: what do they get told?
console.log('\n  a student strongest on each scale, everything else neutral:');
for (const s of SCALES){
  const prof = { R: 2, I: 2, A: 2, S: 2, E: 2, C: 2 };
  prof[s] = 5;
  const sig = R.recSignals(prof, null, null, null);
  const rows = R.recRank(CAR, sig, 'career', 1);
  const fams = R.recRankFamilies(FAM, sig, 1);
  const top = rows[0];
  // How much of the top entry's own profile is actually the student's strength?
  const share = (CAR[top.key].riasec[s] || 0);
  console.log('    ' + s + ' -> ' + fams[0].key + ' / ' + top.key +
              '   [' + top.band + ']  but only ' + Math.round(share * 100) +
              '% of that career is ' + s);
}

// ------------------------------------------------- 2. value sensitivity
console.log('\n\n=== which work-value dimensions actually move a ranking ===\n');
// For each dimension: push it to the top of a student's values, push it to the
// bottom, and measure how far the career ranking moves. A dimension that moves
// nothing is a question we are asking for no reason.
const baseRiasec = { R: 3, I: 4, A: 3, S: 3, E: 4, C: 3 };
const flatVals = () => { const v = {}; for (const d of DIMS) v[d] = 0; return v; };

function rankKeys(values){
  return R.recRank(CAR, R.recSignals(baseRiasec, values, null, null), 'career').map(r => r.key);
}
const neutral = rankKeys(flatVals());
const rows = [];
for (const d of DIMS){
  const hi = flatVals(); hi[d] = 1.5;
  const lo = flatVals(); lo[d] = -1.5;
  const a = rankKeys(hi), b = rankKeys(lo);
  let shift = 0;
  for (let i = 0; i < a.length; i++) shift += Math.abs(i - b.indexOf(a[i]));
  const topChanged = a[0] !== b[0];
  rows.push({ d, shift: shift / a.length, topChanged, hiTop: a[0], loTop: b[0] });
}
rows.sort((x, y) => y.shift - x.shift);
console.log('  dimension        mean rank shift   changes the top career?');
for (const r of rows)
  console.log('  ' + r.d.padEnd(16) + r.shift.toFixed(2).padStart(10) + '        ' +
              (r.topChanged ? 'YES  ' + r.hiTop + ' -> ' + r.loTop : 'no'));

const dead = rows.filter(r => r.shift < 0.5);
console.log('\n  ' + dead.length + ' of ' + DIMS.length + ' dimensions barely move anything: ' +
            (dead.map(r => r.d).join(', ') || 'none'));

// -------------------------------------------- 3. within-family separation
console.log('\n\n=== do values separate careers INSIDE a family? ===\n');
for (const f in FAM){
  const keys = Object.keys(CAR).filter(k => CAR[k].family === f);
  const distinct = new Set(keys.map(k => JSON.stringify(CAR[k].values)));
  console.log('  ' + f.padEnd(13) + keys.length + ' careers, ' + distinct.size +
              ' distinct value profiles' + (distinct.size === 1 ? '   <- all inherited, values cannot separate them' : ''));
}
