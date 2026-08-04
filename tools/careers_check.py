# -*- coding: utf-8 -*-
u"""Asserts the career taxonomy's structure before anything is built on it.

Every number in careers.py feeds the recommendation engine. A profile that does
not sum to 1.0, or a subject key that does not exist, produces a ranking that is
quietly wrong and completely plausible on screen.

    python careers_check.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import careers as cr
import subjects as sj

fails, passes = [], []
def ok(cond, msg):
    (passes if cond else fails).append(msg)
    print(('  PASS ' if cond else '  FAIL ') + msg)

BRIEF_FAMILIES = 16

print('== families ==')
ok(len(cr.FAMILIES) == BRIEF_FAMILIES, '%d families (%d)' % (BRIEF_FAMILIES, len(cr.FAMILIES)))
ok(sorted(cr.FAMILY_SUBJECTS.keys()) == sorted(cr.FAMILIES.keys()),
   'every family declares its school subjects')

for fam, prof in sorted(cr.FAMILIES.items()):
    ok(abs(sum(prof.values()) - 1.0) < 1e-9,
       '%s: RIASEC sums to 1.0 (%.2f)' % (fam, sum(prof.values())))
    ok(all(s in 'RIASEC' for s in prof), '%s: only real RIASEC scales' % fam)
    subs = cr.FAMILY_SUBJECTS[fam]
    ok(abs(sum(subs.values()) - 1.0) < 1e-9,
       '%s: subject weights sum to 1.0 (%.2f)' % (fam, sum(subs.values())))
    bad = [s for s in subs if s not in sj.SUBJECT_KEYS]
    ok(not bad, '%s: every subject exists -> %s' % (fam, bad or 'ok'))

print('\n== careers and majors ==')
for label, table, getter in (('career', cr.CAREERS, cr.career),
                             ('major', cr.MAJORS, cr.major)):
    ok(len(table) > 0, '%ss defined (%d)' % (label, len(table)))
    for key in sorted(table):
        e = getter(key)
        ok(e['family'] in cr.FAMILIES, '%s %s: family exists' % (label, key))
        ok(abs(sum(e['riasec'].values()) - 1.0) < 1e-9,
           '%s %s: RIASEC sums to 1.0 (%.2f)' % (label, key, sum(e['riasec'].values())))
        ok(all(s in 'RIASEC' for s in e['riasec']),
           '%s %s: only real RIASEC scales' % (label, key))
        ok(abs(sum(e['subjects'].values()) - 1.0) < 1e-9,
           '%s %s: subject weights sum to 1.0' % (label, key))
        bad = [s for s in e['subjects'] if s not in sj.SUBJECT_KEYS]
        ok(not bad, '%s %s: every subject exists -> %s' % (label, key, bad or 'ok'))
        ok(e['education'] in cr.EDUCATION_LEVELS,
           '%s %s: education level is real (%s)' % (label, key, e['education']))

print('\n== not every road goes through university ==')
# A result that only ever names degrees tells a student who is not going to
# university that there is nothing here for them.
levels = set(cr.career(k)['education'] for k in cr.CAREERS)
ok('college' in levels or 'either' in levels,
   'at least some careers are reachable without a degree (%s)' % sorted(levels))

print('\n== populated families ==')
pop = cr.populated_families()
ok(len(pop) >= 3, 'at least three families carry entries (%d: %s)' % (len(pop), ', '.join(pop)))
for fam in pop:
    ok(len(cr.careers_in(fam)) >= 5,
       '%s: 5+ careers (%d)' % (fam, len(cr.careers_in(fam))))
    ok(len(cr.majors_in(fam)) >= 3,
       '%s: 3+ majors (%d)' % (fam, len(cr.majors_in(fam))))
empty = [f for f in cr.FAMILY_KEYS if f not in pop]
print('  NOTE  %d families still empty: %s' % (len(empty), ', '.join(empty) or 'none'))

print('\n== the taxonomy spans the whole interest space ==')
# If no family leans on a scale, a student strongest in it gets nothing back.
covered = set()
for prof in cr.FAMILIES.values():
    for s, w in prof.items():
        if w >= 0.4: covered.add(s)
missing = [s for s in 'RIASEC' if s not in covered]
ok(not missing, 'every RIASEC scale is the lead scale of some family -> %s' % (missing or 'ok'))

print('\n' + ('%d FAILED, ' % len(fails) if fails else '') + '%d checks passed' % len(passes))
sys.exit(1 if fails else 0)
