# -*- coding: utf-8 -*-
u"""Asserts the subject model, especially the ways it can be fed bad data.

The recommendation engine will run on whatever a school actually has: partial
mark sheets, a mix of five-point and hundred-point scales, blanks, typos, and
subjects that do not exist. None of that may produce a confident wrong answer.

    python subjects_check.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import subjects as sj

fails, passes = [], []
def ok(cond, msg):
    (passes if cond else fails).append(msg)
    print(('  PASS ' if cond else '  FAIL ') + msg)

print('== structure ==')
ok(len(sj.SUBJECTS) == 11, '11 subjects (%d)' % len(sj.SUBJECTS))
ok(len(set(sj.SUBJECT_KEYS)) == 11, 'keys are unique')
for lang in ('uz', 'ru', 'en'):
    n = sj.names_for(lang)
    ok(sorted(n.keys()) == sorted(sj.SUBJECT_KEYS), '%s: every subject named' % lang)
    ok(all(v.strip() for v in n.values()), '%s: no blank name' % lang)
for key, aff in sj.SUBJECTS:
    total = sum(aff.values())
    ok(abs(total - 1.0) < 1e-9, '%s: RIASEC affinity sums to 1.0 (%.2f)' % (key, total))
    ok(all(s in 'RIASEC' for s in aff), '%s: only real RIASEC scales' % key)

print('\n== normalisation ==')
ok(sj.normalise(5, 'mark_five') == 1.0, 'a 5 on the five-point scale is 1.0')
ok(sj.normalise(2, 'mark_five') == 0.0, 'a 2 is 0.0')
ok(abs(sj.normalise(100, 'mark_hundred') - 1.0) < 1e-9, '100/100 is 1.0')
ok(abs(sj.normalise(50, 'mark_hundred') - 0.5) < 1e-9, '50/100 is 0.5')
ok(sj.normalise(5, 'confidence') == 1.0, 'confidence 5 is 1.0')
# The two mark scales must agree about what "top of the scale" means, or a
# school using percentages would score systematically differently from one
# using 2-5 for the same student.
ok(sj.normalise(5, 'mark_five') == sj.normalise(100, 'mark_hundred'),
   'the two mark scales agree at the top')

print('\n== missing data is NOT zero ==')
ok(sj.normalise(None, 'mark_five') is None, 'None stays None')
ok(sj.normalise('', 'mark_five') is None, 'empty string is missing, not 0')
ok(sj.normalise('abc', 'mark_five') is None, 'a malformed value is missing, not 0')
ok(sj.normalise(1, 'mark_five') == 0.0, 'an out-of-range 1 clamps to the floor')
ok(sj.normalise(7, 'mark_five') == 1.0, 'an out-of-range 7 clamps to the ceiling')

print('\n== reading a real, messy mark sheet ==')
perf = sj.read_performance([
    {'subject': 'math', 'value': 5, 'scale': 'mark_five'},
    {'subject': 'physics', 'value': 88, 'scale': 'mark_hundred'},
    {'subject': 'art', 'value': 4, 'scale': 'confidence'},
    {'subject': 'chemistry', 'value': '', 'scale': 'mark_five'},     # blank
    {'subject': 'astrology', 'value': 5, 'scale': 'mark_five'},      # not a subject
    {'subject': 'history', 'value': 4, 'scale': 'martian'},          # not a scale
    None,                                                            # junk row
])
ok(sorted(perf.keys()) == ['art', 'math', 'physics'], 'only usable rows survive')
ok(perf['math']['score'] == 1.0, 'the 5 came through')
ok(perf['art']['weight'] < perf['math']['weight'],
   'self-reported confidence is worth less than a real mark (%.1f vs %.1f)'
   % (perf['art']['weight'], perf['math']['weight']))
later = sj.read_performance([
    {'subject': 'math', 'value': 3, 'scale': 'confidence'},
    {'subject': 'math', 'value': 5, 'scale': 'mark_five'},
])
ok(later['math']['scale'] == 'mark_five', 'a real mark overrides an earlier self-report')

print('\n== what the marks imply about interests ==')
ok(sj.interest_profile_from_subjects({}) == {}, 'no data -> no profile, not a flat one')
sci = sj.read_performance([
    {'subject': 'physics', 'value': 5, 'scale': 'mark_five'},
    {'subject': 'math', 'value': 5, 'scale': 'mark_five'},
    {'subject': 'literature', 'value': 2, 'scale': 'mark_five'},
])
p = sj.interest_profile_from_subjects(sci)
ok(p.get('I', 0) > p.get('A', 0),
   'strong maths+physics, weak literature -> Investigative over Artistic (%.2f vs %.2f)'
   % (p.get('I', 0), p.get('A', 0)))
art = sj.interest_profile_from_subjects(sj.read_performance([
    {'subject': 'art', 'value': 5, 'scale': 'mark_five'},
    {'subject': 'literature', 'value': 5, 'scale': 'mark_five'},
    {'subject': 'math', 'value': 2, 'scale': 'mark_five'},
]))
ok(art.get('A', 0) > art.get('I', 0), 'and the reverse student comes out Artistic')
ok(all(0.0 <= v <= 1.0 for v in p.values()), 'every implied score stays in 0..1')
# One subject must not silently become a whole profile.
one = sj.interest_profile_from_subjects(sj.read_performance([
    {'subject': 'art', 'value': 5, 'scale': 'mark_five'}]))
ok(set(one.keys()) == {'A', 'R'}, 'a single subject only speaks for its own scales')

print('\n' + ('%d FAILED, ' % len(fails) if fails else '') + '%d checks passed' % len(passes))
sys.exit(1 if fails else 0)
