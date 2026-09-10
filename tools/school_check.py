# -*- coding: utf-8 -*-
u"""Asserts the school subjects bank.

The failures worth catching here are the silent ones. A cost item that is not
reverse scored reads perfectly well and quietly turns dread into evidence FOR a
subject. A rotation that does not actually rotate looks fine in a diff and puts
mathematics three times in a row on screen. Neither shows up as a crash.

    python school_check.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import school_content as sc
import subjects

fails, passes = [], []


def ok(cond, msg):
    (passes if cond else fails).append(msg)
    print(('  PASS ' if cond else '  FAIL ') + msg)


LANGS = ('uz', 'ru', 'en')
# Every typographic dash. The site has none and is checked for none; a bank
# added later is exactly how one gets back in.
DASHES = re.compile(u'[‐-―−]')

print('== structure ==')
ok(sc.SUBJECTS == list(subjects.SUBJECT_KEYS), 'subject list is subjects.py, in its order')
ok(len(sc.SUBJECTS) == len(set(sc.SUBJECTS)), 'subjects are unique')
ok(len(sc.FACETS) == 3, 'three facets (%d)' % len(sc.FACETS))
ok(sorted(sc.REVERSE) == sorted(f for f, _, _ in sc.FACETS), 'every facet has a reverse flag')
ok(sc.REVERSE['cost'] is True, 'cost is reverse scored')
ok(not sc.REVERSE['ability'] and not sc.REVERSE['interest'],
   'ability and interest are not reverse scored')
ok(len(sc.LABELS) == 5, 'five response labels')

expected = len(sc.SUBJECTS) * len(sc.FACETS)

print('\n== the rotation actually rotates ==')
uz = sc.items_for('uz')
ok(len(uz) == expected, '%d items (%d subjects x %d facets)'
   % (expected, len(sc.SUBJECTS), len(sc.FACETS)))
gaps = []
last = {}
for i, item in enumerate(uz):
    if item['s'] in last:
        gaps.append(i - last[item['s']])
    last[item['s']] = i
ok(gaps and min(gaps) >= len(sc.SUBJECTS) - 1,
   'at least %d questions between one subject and the next (min %d)'
   % (len(sc.SUBJECTS) - 1, min(gaps) if gaps else 0))

print('\n== every subject is asked on every facet, exactly once ==')
pairs = [(item['s'], item['f']) for item in uz]
ok(len(pairs) == len(set(pairs)), 'no subject and facet pair is asked twice')
want = set((s, f) for s in sc.SUBJECTS for f, _, _ in sc.FACETS)
ok(set(pairs) == want, 'every subject and facet pair is asked')

print('\n== translations ==')
for lang in LANGS:
    items = sc.items_for(lang)
    ok(len(items) == expected, '%s: %d items' % (lang, len(items)))
    ok([(i['s'], i['f']) for i in items] == pairs,
       '%s: subject and facet keying identical to the Uzbek' % lang)
    ok([i['r'] for i in items] == [i['r'] for i in uz],
       '%s: reverse flags identical to the Uzbek' % lang)
    ok(len(sc.labels_for(lang)) == 5, '%s: five labels' % lang)
    names = sc.names_for(lang)
    ok(sorted(names) == sorted(sc.SUBJECTS), '%s: every subject named' % lang)
    ok(all(v.strip() for v in names.values()), '%s: no blank subject name' % lang)

    texts = [i['t'] for i in items]
    ok(len(set(texts)) == len(texts), '%s: no two items share wording' % lang)
    ok(all(t.strip() for t in texts), '%s: no blank item' % lang)
    # The subject has to appear in its own question, or the frame lost its slot.
    ok(all(names[i['s']] in i['t'] for i in items),
       '%s: every question names the subject it scores' % lang)

    head, blurb = sc.title_for(lang)
    ok(bool(head.strip()) and bool(blurb.strip()), '%s: title and blurb present' % lang)
    sections = sc.sections_for(lang)
    ok(len(sections) == 3 and all(h.strip() for _, h in sections),
       '%s: three section headings' % lang)

print('\n== no typographic dashes ==')
for lang in LANGS:
    head, blurb = sc.title_for(lang)
    strings = ([i['t'] for i in sc.items_for(lang)] + list(sc.labels_for(lang))
               + list(sc.names_for(lang).values()) + [h for _, h in sc.sections_for(lang)]
               + [head, blurb])
    bad = [s for s in strings if DASHES.search(s)]
    ok(not bad, '%s: none (%s)' % (lang, bad[0] if bad else 'clean'))

print('\n%d passed, %d failed' % (len(passes), len(fails)))
sys.exit(1 if fails else 0)
