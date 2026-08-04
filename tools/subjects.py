# -*- coding: utf-8 -*-
u"""School subjects, and how a student's performance in them is represented.

WHY THIS IS NOT ANOTHER QUESTIONNAIRE
-------------------------------------
The obvious move is a twenty-item "which subjects suit you" self-report. That
would be the third self-report instrument in a row, and it would be the weakest:
the best available predictor of how a student will do in a subject is how they
are already doing in that subject. So this module models PERFORMANCE first and
treats self-report as a fallback that is explicitly worth less.

THREE WAYS PERFORMANCE CAN ARRIVE
---------------------------------
    mark_five     2..5    the ordinary Uzbek school mark
    mark_hundred  0..100  used by some schools and by national testing
    confidence    1..5    "how well do you do in this subject?" -- FALLBACK ONLY

All three normalise to 0..1 so the recommendation engine never has to know which
one it was given. A `confidence` reading is deliberately down-weighted (see
SOURCE_WEIGHT): a student who believes they are good at physics and a student
with a 5 in physics are not the same evidence, and pretending otherwise is how a
recommendation engine ends up flattering people.

MISSING DATA IS THE NORMAL CASE
-------------------------------
Most students will supply a few subjects, not eleven. Nothing here requires a
complete set: `normalise()` returns None for absent data and the engine
renormalises over whatever it actually has. A subject nobody entered must not
count as a zero -- that would read "bad at chemistry" when the truth is "did not
say".

SUBJECT -> RIASEC
-----------------
Each subject carries the interest scales it actually draws on. This is what lets
the engine notice agreement and disagreement between what a student ENJOYS and
what they are GOOD AT -- which is the interesting case and the one worth showing
them. Weights are small and deliberately blunt: they express "physics is an
investigative subject with a realistic streak", not a measurement.
"""

SCALES = {
    'mark_five':    {'min': 2.0, 'max': 5.0},
    'mark_hundred': {'min': 0.0, 'max': 100.0},
    'confidence':   {'min': 1.0, 'max': 5.0},
}

# A real mark counts for more than a student's opinion of themselves. Used by
# the engine to weight each subject's contribution, not to alter the value.
SOURCE_WEIGHT = {
    'mark_five': 1.0,
    'mark_hundred': 1.0,
    'confidence': 0.6,
}

# key, RIASEC affinity. Keys are stable identifiers and never shown to a student.
SUBJECTS = [
    ('math',      {'I': 0.6, 'C': 0.4}),
    ('physics',   {'I': 0.6, 'R': 0.4}),
    ('cs',        {'I': 0.5, 'R': 0.3, 'C': 0.2}),
    ('biology',   {'I': 0.7, 'S': 0.3}),
    ('chemistry', {'I': 0.7, 'R': 0.3}),
    ('economics', {'E': 0.5, 'C': 0.3, 'I': 0.2}),
    ('english',   {'S': 0.4, 'A': 0.3, 'E': 0.3}),
    ('literature',{'A': 0.6, 'S': 0.4}),
    ('history',   {'I': 0.4, 'S': 0.3, 'A': 0.3}),
    ('geography', {'I': 0.4, 'R': 0.3, 'S': 0.3}),
    ('art',       {'A': 0.8, 'R': 0.2}),
]

NAMES = {
    'uz': {
        'math': u'Matematika', 'physics': u'Fizika', 'cs': u'Informatika',
        'biology': u'Biologiya', 'chemistry': u'Kimyo', 'economics': u'Iqtisodiyot',
        'english': u'Ingliz tili', 'literature': u'Ona tili va adabiyot',
        'history': u'Tarix', 'geography': u'Geografiya', 'art': u'Tasviriy sanʼat',
    },
    'ru': {
        'math': u'Математика', 'physics': u'Физика', 'cs': u'Информатика',
        'biology': u'Биология', 'chemistry': u'Химия', 'economics': u'Экономика',
        'english': u'Английский язык', 'literature': u'Родной язык и литература',
        'history': u'История', 'geography': u'География', 'art': u'Изобразительное искусство',
    },
    'en': {
        'math': u'Mathematics', 'physics': u'Physics', 'cs': u'Computer Science',
        'biology': u'Biology', 'chemistry': u'Chemistry', 'economics': u'Economics',
        'english': u'English', 'literature': u'Native language and literature',
        'history': u'History', 'geography': u'Geography', 'art': u'Art and design',
    },
}

SUBJECT_KEYS = [k for k, _ in SUBJECTS]
AFFINITY = dict(SUBJECTS)


def normalise(value, scale):
    u"""A raw mark on any supported scale -> 0..1, or None when there is no data.

    None is not zero. A subject the student never entered must not be read as a
    subject they are bad at; the engine drops it and renormalises instead.
    """
    if value is None or value == '':
        return None
    if scale not in SCALES:
        raise ValueError('unknown scale %r' % (scale,))
    try:
        v = float(value)
    except (TypeError, ValueError):
        return None                       # malformed input is missing input
    lo, hi = SCALES[scale]['min'], SCALES[scale]['max']
    if v < lo: v = lo                     # clamp rather than reject: a 1 on a
    if v > hi: v = hi                     # 2..5 scale is a typo, not an opinion
    return (v - lo) / (hi - lo)


def read_performance(entries):
    u"""[{subject, value, scale}] -> {subject: {'score': 0..1, 'weight': w}}.

    Unknown subjects and unusable values are dropped silently -- this is fed by a
    school's own data in whatever shape it arrives, and one bad row must not cost
    a student their whole report. Later entries for the same subject win, so a
    real mark can overwrite a confidence answer.
    """
    out = {}
    for e in entries or []:
        key = (e or {}).get('subject')
        if key not in AFFINITY:
            continue
        scale = e.get('scale') or 'mark_five'
        if scale not in SCALES:
            continue
        score = normalise(e.get('value'), scale)
        if score is None:
            continue
        out[key] = {'score': score, 'weight': SOURCE_WEIGHT[scale], 'scale': scale}
    return out


def interest_profile_from_subjects(perf):
    u"""What a student's MARKS imply about their interests, on the RIASEC scales.

    Not a substitute for the interest test -- it is the second opinion. Where
    this agrees with the answered profile the recommendation is on firmer
    ground; where it disagrees, that disagreement is the single most useful
    thing the report can point at ("you enjoy this, but the marks are elsewhere").

    Returns {} when there is no performance data at all, rather than a flat
    profile that would look like a finding.
    """
    if not perf:
        return {}
    sums, weights = {}, {}
    for key, rec in perf.items():
        for scale, w in AFFINITY[key].items():
            contrib = w * rec['weight']
            sums[scale] = sums.get(scale, 0.0) + rec['score'] * contrib
            weights[scale] = weights.get(scale, 0.0) + contrib
    return dict((s, sums[s] / weights[s]) for s in sums if weights[s] > 0)


def names_for(lang):
    return NAMES.get(lang) or NAMES['uz']
