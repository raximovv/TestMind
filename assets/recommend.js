// TestMind — transparent career and major recommendation.
//
// No model, no AI, no learned weights. Every number here can be traced by hand,
// which matters more than sophistication: a school will be asked "why did it say
// that about my child", and the answer has to be a sentence, not a matrix.
//
// FOUR SIGNALS, AND WHY EACH IS SHAPED THE WAY IT IS
// --------------------------------------------------
// interests (RIASEC)  what the student currently enjoys      -- dominant
// values              what they want FROM a job              -- separates ties
// subjects            what they can already demonstrate      -- evidence
// personality         how they tend to work                  -- context only
//
// IPSATIVE, NOT ABSOLUTE. Interests and values are read RELATIVE to the
// student's own range, not on the raw 1..5. A teenager who likes everything and
// one who likes nothing would otherwise be ranked by how enthusiastic they are
// rather than by what they actually prefer. Subject marks are the exception:
// a 5 is a 5, so those stay absolute.
//
// PERSONALITY CANNOT BLOCK A CAREER. This is a product rule, and it is enforced
// arithmetically rather than by good intentions: the personality term
// contributes between HALF its weight and ALL of it, never zero. A quiet student
// therefore loses at most a few percent against entrepreneur -- they can never
// be ruled out of it. See personalityTerm().
//
// MISSING DATA IS NOT ZERO. A signal that was not collected is dropped and the
// remaining weights are renormalised, so a student who skipped the subject
// section is ranked on interests and values alone rather than being told they
// are bad at everything.
//
// NO PERCENTAGES ARE SHOWN. Scores exist to ORDER things. A "87% suitable"
// number would be false precision built on a ten-item value scale and a handful
// of self-entered marks, so the UI gets bands instead: strong / worth exploring
// / alternative.

var REC_WEIGHTS = {
  // Interests lead for careers: what a person enjoys doing predicts occupational
  // choice better than what they are currently graded on at fifteen.
  career: { riasec: 0.50, values: 0.22, subjects: 0.20, personality: 0.08 },
  // Majors invert the middle two. Admission and survival in a degree depend on
  // demonstrated academic performance far more than a career does, and a major
  // is a narrower, more academic commitment than "work in this area".
  major:  { riasec: 0.36, values: 0.12, subjects: 0.44, personality: 0.08 }
};

// A part is only counted when it has data. These are the minimums below which a
// signal is treated as absent rather than weak.
var REC_MIN_SUBJECT_WEIGHT = 0.15;   // of an entry's subject weights, must be covered

function recKeys(o){ var k = [], x; for (x in o) if (o.hasOwnProperty(x)) k.push(x); return k; }

/** Rescale a profile to 0..1 across the student's OWN range.
 *  Returns null when the student has no spread at all (liked everything the
 *  same), because a flat profile expresses no preference and must not be
 *  allowed to masquerade as one. */
function recRelative(profile){
  var keys = recKeys(profile || {});
  if (keys.length < 2) return null;
  var lo = Infinity, hi = -Infinity, i, v;
  for (i = 0; i < keys.length; i++){
    v = profile[keys[i]];
    if (v < lo) lo = v;
    if (v > hi) hi = v;
  }
  if (hi - lo < 1e-9) return null;
  var out = {};
  for (i = 0; i < keys.length; i++) out[keys[i]] = (profile[keys[i]] - lo) / (hi - lo);
  return out;
}

/** Weighted overlap between a student's relative profile and an entry's profile.
 *  The entry's weights sum to 1, so the result is already 0..1. */
function recOverlap(rel, entryProfile){
  if (!rel) return null;
  var keys = recKeys(entryProfile), sum = 0, w = 0, i, k;
  for (i = 0; i < keys.length; i++){
    k = keys[i];
    if (!(k in rel)) continue;
    sum += entryProfile[k] * rel[k];
    w += entryProfile[k];
  }
  return w > 0 ? sum / w : null;
}

/** How well the student's marks cover what this entry leans on.
 *  Absolute, not relative: a 5 in mathematics means the same for everyone.
 *  Null when the student entered nothing relevant -- silence is not a low mark. */
function recSubjectFit(perf, entrySubjects){
  if (!perf) return null;
  var keys = recKeys(entrySubjects), sum = 0, w = 0, covered = 0, i, k, rec;
  for (i = 0; i < keys.length; i++){
    k = keys[i];
    rec = perf[k];
    if (!rec) continue;
    // A self-reported answer counts less than a real mark; `weight` carries that.
    var ew = entrySubjects[k] * (rec.weight === undefined ? 1 : rec.weight);
    sum += ew * rec.score;
    w += ew;
    covered += entrySubjects[k];
  }
  if (w <= 0 || covered < REC_MIN_SUBJECT_WEIGHT) return null;
  // Shrink toward neutral in proportion to how much of the entry we could
  // actually see. Without this, an entry needing three subjects the student
  // supplied two of scores a perfect 1.00 and ties with one whose every
  // requirement was covered -- a student with 5s in maths, CS and physics tied
  // finance (which ignores physics) with computer science. Partial evidence is
  // now worth proportionally less, and symmetrically: a poor mark on thin
  // coverage is also less damning than a poor mark on full coverage.
  return 0.5 + (sum / w - 0.5) * covered;
}

/** Personality's contribution, deliberately bounded away from zero.
 *
 *  Big Five is 1..5 per trait. Two traits are used, and only where there is a
 *  defensible link: Extraversion against how much an entry is about persuading
 *  and leading (its Enterprising weight), Conscientiousness against how much it
 *  is about order and procedure (its Conventional weight).
 *
 *  The return is 0.5..1.0, never 0..1. That is the whole mechanism behind
 *  "personality must not block a career": at full weight 0.08 the most
 *  personality can ever move an entry is 4 percentage points, and it can only
 *  ever add. A quiet student stays eligible for entrepreneur. */
function recPersonalityTerm(big5, entryRiasec){
  if (!big5 || big5.E === undefined) return null;
  var e = (big5.E - 1) / 4;                       // 0..1
  var c = (big5.C - 1) / 4;
  var wE = entryRiasec.E || 0, wC = entryRiasec.C || 0;
  var w = wE + wC;
  if (w <= 0) return 0.75;                        // no defensible link: neutral
  var fit = (wE * e + wC * c) / w;                // 0..1
  return 0.5 + 0.5 * fit;                         // 0.5..1
}

/** Score one entry. Returns {score, parts, used} or null when nothing applied. */
function recScoreEntry(entry, signals, weights){
  var parts = {}, total = 0, wsum = 0;

  var riasec = recOverlap(signals.riasecRel, entry.riasec);
  if (riasec !== null){ parts.riasec = riasec; total += weights.riasec * riasec; wsum += weights.riasec; }

  var values = recOverlap(signals.valuesRel, entry.values);
  if (values !== null){ parts.values = values; total += weights.values * values; wsum += weights.values; }

  var subj = recSubjectFit(signals.subjects, entry.subjects);
  if (subj !== null){ parts.subjects = subj; total += weights.subjects * subj; wsum += weights.subjects; }

  var pers = recPersonalityTerm(signals.big5, entry.riasec);
  if (pers !== null){ parts.personality = pers; total += weights.personality * pers; wsum += weights.personality; }

  if (wsum <= 0) return null;                     // no signal at all
  return { score: total / wsum, parts: parts, used: recKeys(parts) };
}

/** Turn a student's raw scores into the shapes the scorer wants, once. */
function recSignals(riasec, values, subjects, big5){
  return {
    riasecRel: recRelative(riasec),
    valuesRel: recRelative(values),
    subjects: (subjects && recKeys(subjects).length) ? subjects : null,
    big5: big5 || null
  };
}

// Banding is by GAP FROM THE BEST, not by position in the whole range.
// Measured over 96 careers, the five that get displayed sit within 0.00-0.20 of
// the top score while the full range is ~0.90 -- so a range-based cut put every
// displayed row in the top quartile and every dot came out green, which told the
// reader nothing. What a student can act on is "how much weaker is this than the
// strongest one", and these thresholds come from that measured spread.
var REC_BAND_STRONG = 0.04;
var REC_BAND_EXPLORE = 0.10;

/** Band a ranked row. `worst` is still needed to detect the degenerate case
 *  where nothing separates anything, in which case nothing is claimed. */
function recBand(score, best, worst){
  if (best - worst < 1e-6) return 'explore';      // everything tied: claim nothing
  var gap = best - score;
  if (gap <= REC_BAND_STRONG) return 'strong';
  if (gap <= REC_BAND_EXPLORE) return 'explore';
  return 'alternative';
}

/** Rank every entry in a table. `kind` is 'career' or 'major'. */
function recRank(table, signals, kind, limit){
  var weights = REC_WEIGHTS[kind], keys = recKeys(table), rows = [], i, r;
  for (i = 0; i < keys.length; i++){
    r = recScoreEntry(table[keys[i]], signals, weights);
    if (r) rows.push({ key: keys[i], score: r.score, parts: r.parts,
                       used: r.used, family: table[keys[i]].family,
                       education: table[keys[i]].education });
  }
  if (!rows.length) return [];
  rows.sort(function(a, b){ return (b.score - a.score) || (a.key < b.key ? -1 : 1); });
  var best = rows[0].score, worst = rows[rows.length - 1].score;
  for (i = 0; i < rows.length; i++) rows[i].band = recBand(rows[i].score, best, worst);
  return limit ? rows.slice(0, limit) : rows;
}

/** Rank the FAMILIES, which is the level a fifteen-year-old can act on. */
function recRankFamilies(families, signals, limit){
  var keys = recKeys(families), rows = [], i, r;
  for (i = 0; i < keys.length; i++){
    r = recScoreEntry(families[keys[i]], signals, REC_WEIGHTS.career);
    if (r) rows.push({ key: keys[i], score: r.score, parts: r.parts, used: r.used });
  }
  rows.sort(function(a, b){ return (b.score - a.score) || (a.key < b.key ? -1 : 1); });
  if (rows.length){
    var best = rows[0].score, worst = rows[rows.length - 1].score;
    for (i = 0; i < rows.length; i++) rows[i].band = recBand(rows[i].score, best, worst);
  }
  return limit ? rows.slice(0, limit) : rows;
}

/** Which signals actually drove this row, strongest first.
 *  Contribution, not raw part value: a part scoring 0.9 at weight 0.08 mattered
 *  less than one scoring 0.6 at weight 0.5, and the explanation must say so. */
function recDrivers(row, kind){
  var w = REC_WEIGHTS[kind], out = [], k;
  for (k in row.parts) if (row.parts.hasOwnProperty(k))
    out.push({ part: k, contribution: row.parts[k] * w[k], value: row.parts[k] });
  out.sort(function(a, b){ return b.contribution - a.contribution; });
  return out;
}

/** Signals that disagree, which is the most useful thing a report can surface.
 *  Returns [] when they agree -- a conflict claimed where none exists is worse
 *  than none reported. */
function recConflicts(signals, subjectImplied){
  var out = [];
  var a = signals.riasecRel, b = recRelative(subjectImplied || {});
  if (!a || !b) return out;
  var k, gap;
  for (k in a) if (a.hasOwnProperty(k) && b.hasOwnProperty(k)){
    gap = a[k] - b[k];
    if (gap >= 0.5) out.push({ scale: k, side: 'interest', gap: gap });
    else if (gap <= -0.5) out.push({ scale: k, side: 'marks', gap: -gap });
  }
  out.sort(function(x, y){ return y.gap - x.gap; });
  return out;
}

if (typeof module !== 'undefined' && module.exports){
  module.exports = {
    REC_WEIGHTS: REC_WEIGHTS, recRelative: recRelative, recOverlap: recOverlap,
    recSubjectFit: recSubjectFit, recPersonalityTerm: recPersonalityTerm,
    recScoreEntry: recScoreEntry, recSignals: recSignals, recBand: recBand,
    REC_BAND_STRONG: REC_BAND_STRONG, REC_BAND_EXPLORE: REC_BAND_EXPLORE,
    recRank: recRank, recRankFamilies: recRankFamilies,
    recDrivers: recDrivers, recConflicts: recConflicts
  };
}
