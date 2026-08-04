# -*- coding: utf-8 -*-
u"""Asserts the Work Values bank — above all that it is measuring values.

The failure this file exists to catch is not a crash. It is an item that reads
like a personality statement ("I learn new things quickly") slipping into a
values bank, where it would correlate with Openness, add nothing, and look
entirely reasonable to anyone reviewing the list.

    python values_check.py
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import values_content as vc

fails, passes = [], []
def ok(cond, msg):
    (passes if cond else fails).append(msg)
    print(('  PASS ' if cond else '  FAIL ') + msg)

LANGS = ('uz', 'ru', 'en')

print('== structure ==')
ok(8 <= len(vc.ITEMS) <= 10, 'between 8 and 10 items (%d)' % len(vc.ITEMS))
ok(len(vc.DIMENSIONS) == len(set(vc.DIMENSIONS)), 'dimensions are unique')
asked = [d for d, _ in vc.ITEMS]
ok(sorted(asked) == sorted(vc.DIMENSIONS), 'every dimension is asked exactly once')
ok(len(vc.LABELS) == 5, 'five response labels')

print('\n== the items are VALUES, not personality statements ==')
# A value item talks about the job/work. A personality item talks about the
# student's own qualities. The marker phrase differs per language and is the
# cheapest reliable discriminator we have.
MARK = {
    'uz': re.compile(u'ish', re.I),                     # ish / ishim / ishimda
    'ru': re.compile(u'работ', re.I),                   # работа / работе / работать
    'en': re.compile(u'\\bjob\\b|\\bwork\\b', re.I),
}
IMPORT = {
    'uz': re.compile(u'muhim', re.I),
    'ru': re.compile(u'важно', re.I),
    'en': re.compile(u'matters to me', re.I),
}
for lang in LANGS:
    for dim, text in vc.items_for(lang):
        ok(bool(MARK[lang].search(text)),
           '%s/%s: names the job or the work' % (lang, dim))
        ok(bool(IMPORT[lang].search(text)),
           '%s/%s: phrased as importance, not as ability' % (lang, dim))

print('\n== translations ==')
for lang in LANGS:
    items = vc.items_for(lang)
    ok(len(items) == len(vc.ITEMS), '%s: %d items' % (lang, len(items)))
    ok([d for d, _ in items] == [d for d, _ in vc.ITEMS],
       '%s: dimension keying identical to the Uzbek' % lang)
    ok(len(vc.labels_for(lang)) == 5, '%s: five labels' % lang)
    n = vc.names_for(lang)
    ok(sorted(n.keys()) == sorted(vc.DIMENSIONS), '%s: every dimension named' % lang)
    ok(all(v.strip() for v in n.values()), '%s: no blank name' % lang)
    texts = [t for _, t in items]
    ok(len(set(texts)) == len(texts), '%s: no duplicated item' % lang)
    ok(all(t.strip() for t in texts), '%s: no empty item' % lang)
    h, p = vc.intro_for(lang)
    ok(bool(h and h.strip() and p and p.strip()), '%s: section intro present' % lang)

print('\n== script hygiene ==')
CYR = re.compile(u'[Ѐ-ӿ]')
for lang, want in (('uz', False), ('ru', True), ('en', False)):
    bad = [t for _, t in vc.items_for(lang) if bool(CYR.search(t)) != want]
    ok(not bad, '%s: no wrong-script item -> %s' % (lang, bad[:1] or 'ok'))

print('\n' + ('%d FAILED, ' % len(fails) if fails else '') + '%d checks passed' % len(passes))
sys.exit(1 if fails else 0)
