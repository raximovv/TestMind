// How many RIASEC items do we actually need, and what should we REPORT?
//
// The Big Five side of TestMind taught us the expensive lesson: the archetype
// (top-2 of 5 traits) only agrees with itself about half the time on a retake,
// and adding items barely moves it, because the instability comes from students
// whose 2nd and 3rd traits are genuinely close -- not from measurement error.
// Before building a career module on the same shape, measure it.
//
// Two questions, one simulation:
//   1. 30 core items, or all 48? What does the extra 18 buy?
//   2. Is a 3-letter Holland code more stable than a single label?
//
//     node riasec_sim.js
//
// MODEL. Real RIASEC scores are not independent -- they sit on Holland's
// hexagon, where adjacent interests (R-I, I-A, ...) correlate and opposite ones
// (R-S, I-E, A-C) do not. So a student is generated as:
//     elevation    how much they like everything (a real, large effect)
//   + direction    where on the hexagon their interests point, and how strongly
//   + unique       what is left over per scale
// which reproduces the circumplex rather than assuming it away.
//
// NOISE is calibrated to the published reliabilities of the O*NET Interest
// Profiler short forms: alpha .74-.81 at 5 items per scale, .78-.85 at 8-10.
// Solving alpha = s2t / (s2t + s2i/k) at k=5, alpha=.78 gives the item variance
// used below; it lands at .85 for k=8, matching the published figure.

const N = 200000;
const SD_TRUE = 1.00;
const SD_ITEM = SD_TRUE * 1.187;      // -> alpha .78 at k=5, .85 at k=8

// Weights of the three sources of true score. Elevation is deliberately large:
// "likes most things" is one of the most reliable findings in interest data,
// and it is exactly what makes a single top-letter label unstable.
const W_ELEV = 0.55, W_DIR = 0.85, W_UNIQ = 0.45;

const SCALES = ['R', 'I', 'A', 'S', 'E', 'C'];
const ANG = SCALES.map((_, i) => (i * Math.PI) / 3);   // hexagon, 60 deg apart

// mulberry32 rather than the LCG used in the Big Five sims. An LCG's low bits
// are badly correlated, and the first pass of this simulation produced rankings
// between gate settings that moved around more than the sample size allowed --
// which is exactly what a weak generator looks like when a rare event (an exact
// 3-letter code) is being counted.
let seed = 987654321;
function rnd(){
  seed = (seed + 0x6D2B79F5) | 0;
  let t = seed;
  t = Math.imul(t ^ (t >>> 15), t | 1);
  t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
  return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
}
function gauss(){ const u = 1 - rnd(), v = rnd(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }

function student(){
  const elev = gauss(), phi = rnd() * 2 * Math.PI, amp = Math.abs(gauss());
  const truth = ANG.map(a =>
    W_ELEV * elev + W_DIR * amp * Math.cos(a - phi) + W_UNIQ * gauss());
  return {
    truth,
    // Answer k items on scale s. Each item is the true score plus item noise.
    ask: (s, k) => { let sum = 0; for (let i = 0; i < k; i++) sum += truth[s] + SD_ITEM * gauss(); return sum / k; },
  };
}

const order = v => [0,1,2,3,4,5].sort((a,b) => v[b] - v[a]);
const top1  = v => order(v)[0];
const code2 = v => order(v).slice(0, 2).join('');            // the Big Five shape
const code3 = v => order(v).slice(0, 3).join('');            // ordered Holland code
const set3  = v => order(v).slice(0, 3).sort().join('');     // unordered, e.g. SIA == ASI

// gate: run the reserve items only on scales still in contention for the cut
// between 3rd and 4th place -- the boundary the reported code actually depends on.
function measure(s, core, extra, gate){
  const sum = [], cnt = [];
  for (let t = 0; t < 6; t++){ sum.push(s.ask(t, core) * core); cnt.push(core); }
  let mean = sum.map((v, i) => v / cnt[i]);
  let used = 6 * core;
  if (gate !== null){
    const r = order(mean);
    const contested = [];
    for (let i = 0; i < 6; i++)
      if (Math.abs(mean[r[i]] - mean[r[2]]) <= gate || Math.abs(mean[r[i]] - mean[r[3]]) <= gate)
        contested.push(r[i]);
    for (const t of contested){ sum[t] += s.ask(t, extra) * extra; cnt[t] += extra; used += extra; }
    mean = sum.map((v, i) => v / cnt[i]);
  }
  return { mean, used };
}

// Pearson r between the six scores measured now and the six measured again.
// This is the profile as a whole, which is what we are considering REPORTING
// instead of a label, so it has to be measured rather than assumed better.
function profileR(a, b){
  let ma = 0, mb = 0;
  for (let i = 0; i < 6; i++){ ma += a[i]; mb += b[i]; }
  ma /= 6; mb /= 6;
  let num = 0, da = 0, db = 0;
  for (let i = 0; i < 6; i++){
    const x = a[i] - ma, y = b[i] - mb;
    num += x * y; da += x * x; db += y * y;
  }
  return (da && db) ? num / Math.sqrt(da * db) : 0;
}

function run(label, core, extra, gate){
  seed = 987654321;              // every design meets the SAME students, so a
  let items = 0;                 // difference is the design and not sampling
  const hit = { t1: 0, c2: 0, c3: 0, s3: 0 };
  const same = { t1: 0, c2: 0, c3: 0, s3: 0, soft: 0 };
  let rsum = 0;
  for (let n = 0; n < N; n++){
    const st = student();
    const a = measure(st, core, extra, gate);
    const b = measure(st, core, extra, gate);
    items += a.used;
    if (top1(a.mean)  === top1(st.truth))  hit.t1++;
    if (code2(a.mean) === code2(st.truth)) hit.c2++;
    if (code3(a.mean) === code3(st.truth)) hit.c3++;
    if (set3(a.mean)  === set3(st.truth))  hit.s3++;
    if (top1(a.mean)  === top1(b.mean))  same.t1++;
    if (code2(a.mean) === code2(b.mean)) same.c2++;
    if (code3(a.mean) === code3(b.mean)) same.c3++;
    if (set3(a.mean)  === set3(b.mean))  same.s3++;
    // The tolerant version of "same answer": the area we named first is still
    // in their top two on the retake. This is what a careers conversation
    // actually needs, as opposed to an exact string match.
    if (order(b.mean).slice(0, 2).indexOf(top1(a.mean)) !== -1) same.soft++;
    rsum += profileR(a.mean, b.mean);
  }
  const p = x => (100 * x / N).toFixed(1).padStart(5) + '%';
  console.log(
    label.padEnd(26) + (items / N).toFixed(1).padStart(6) +
    '   ' + p(same.t1) + p(same.s3) + p(same.c3) + p(same.soft) +
    (rsum / N).toFixed(2).padStart(7) +
    '  |' + p(hit.t1) + p(hit.s3));
}

console.log('AGREEMENT WITH ITSELF ON A RETAKE, and with the student\'s true profile');
console.log('(' + (N / 1000) + 'k simulated students, each measured twice)\n');
console.log(' '.repeat(26) + ' items' +
            '   |--------- same on a retake ----------|         |-- vs truth --|');
console.log(' '.repeat(26) + '      ' +
            '  top-1   set3  code3   soft  prof r    top-1   set3');
console.log('-'.repeat(96));
run('fixed 30 (core only)',   5, 0, null);
run('fixed 48 (whole bank)',  8, 0, null);
console.log('-'.repeat(96));
run('30 + top-up, gate 0.20', 5, 3, 0.20);
run('30 + top-up, gate 0.35', 5, 3, 0.35);
run('30 + top-up, gate 0.50', 5, 3, 0.50);
run('30 + top-up, gate 0.75', 5, 3, 0.75);
console.log('-'.repeat(96));
// Sanity check on the gate machinery itself: a gate wide enough to catch every
// scale tops all six up to 8 items, so this row MUST reproduce "fixed 48". If
// it does not, the non-monotonic rows above are a bug in the gate, not a
// finding about adaptive testing, and nothing here can be trusted.
run('gate 99 (must equal 48)', 5, 3, 99);
console.log('-'.repeat(96));
console.log('set3   = the three letters ignoring their order (SIA == ASI == IAS).');
console.log('code3  = the exact ordered Holland code.');
console.log('soft   = the area we named first is still in their top two on a retake.');
console.log('prof r = correlation between the six scores now and the six on a retake.');
console.log(`
WHAT THIS SETTLED
  1. Never report an ordered Holland code. "SIA" reproduces itself on a retake
     9-14% of the time at ANY length. Three ranked boundaries have to all land
     correctly; they do not. This is the single most important result here.
  2. Never report one area as a label either. Top-1 agreement is 51% at 48
     items -- the same coin flip as the Big Five archetype. But the area we
     name IS still in the student's top two 76% of the time, so name it as
     "your strongest area" with the near-tie disclosure, not as an identity.
  3. The three areas taken as a SET saturate early: 37.4% at 38 items against
     38.4% at 48. So the adaptive top-up genuinely pays here.
  4. The whole profile is what actually holds still: r = .59 at 30 items,
     .68 at 48. This is the thing to put on the screen.
  5. Chosen design: 30 core + top-up at gate 0.50 = ~41 items, which buys the
     48-item set accuracy (38.2 vs 38.4) for 14% fewer questions.`);
