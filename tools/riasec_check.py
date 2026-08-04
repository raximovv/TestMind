# -*- coding: utf-8 -*-
u"""Checks the RIASEC bank before anything is built from it.

An item bank fails silently. A list of the wrong length, an item keyed to the
wrong scale, a translation with two lines swapped -- all of these score every
student wrongly and look completely normal on screen. So the bank is asserted
here, and build_riasec_js.py refuses to emit anything until this passes.

    python riasec_check.py
"""
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import riasec_content as rc

LANGS = ['uz', 'ru', 'en']

fails = []
passes = []


def ok(cond, msg):
    (passes if cond else fails).append(msg)
    print(('  PASS ' if cond else '  FAIL ') + msg)


print('== structure ==')
ok(len(rc.ITEMS) == 48, 'bank is 48 items (%d)' % len(rc.ITEMS))
ok(len(rc.SCALES) == 6, 'six scales')

per = {}
core = {}
for s, t, late in rc.ITEMS:
    per[s] = per.get(s, 0) + 1
    if not late:
        core[s] = core.get(s, 0) + 1

for s in rc.SCALES:
    ok(per.get(s) == 8, '%s has 8 items (%s)' % (s, per.get(s)))
    ok(core.get(s) == rc.CORE_PER_SCALE,
       '%s has %d core items (%s)' % (s, rc.CORE_PER_SCALE, core.get(s)))

ok(sum(1 for i in rc.ITEMS if not i[2]) == 30, 'core plan is 30 items')
ok(sum(1 for i in rc.ITEMS if i[2]) == 18, 'reserve is 18 items')

# Every scale must contribute equally to the core, or a scale with more core
# items would score systematically higher than one with fewer and the ranking --
# which is the whole output -- would be decided by the bank, not the student.
ok(len(set(core.values())) == 1, 'every scale carries the same core weight')

print('\n== no reverse-keyed items (deliberate for an interest inventory) ==')
NEG = re.compile(u'yoqmaydi|yomon koʻr|не нравится|dislike|would not', re.I)
neg = [t for s, t, l in rc.ITEMS if NEG.search(t)]
ok(not neg, 'no item is phrased as a dislike -> ' + (neg[0] if neg else 'none'))

print('\n== translations ==')
for lang in LANGS:
    items = rc.items_for(lang)
    ok(len(items) == 48, '%s: 48 items' % lang)
    ok(len(rc.labels_for(lang)) == 5, '%s: 5 response labels' % lang)
    ok(sorted(rc.scale_names_for(lang).keys()) == sorted(rc.SCALES),
       '%s: all six scales named' % lang)
    ok(sorted(rc.scale_leads_for(lang).keys()) == sorted(rc.SCALES),
       '%s: all six scales have a lead line' % lang)
    # Keying must survive translation -- items_for pairs by position, so this
    # confirms the pairing rather than assuming it.
    ok([i[0] for i in items] == [i[0] for i in rc.ITEMS],
       '%s: scale keying identical to the Uzbek' % lang)
    ok([i[2] for i in items] == [i[2] for i in rc.ITEMS],
       '%s: core/reserve split identical to the Uzbek' % lang)
    blank = [t for s, t, l in items if not t or not t.strip()]
    ok(not blank, '%s: no empty item' % lang)
    dupes = [t for t in set(x[1] for x in items)
             if [x[1] for x in items].count(t) > 1]
    ok(not dupes, '%s: no duplicated item -> %s' % (lang, dupes[:1] or 'none'))

print('\n== script hygiene ==')
CYR = re.compile(u'[Ѐ-ӿ]')
LAT = re.compile(u'[A-Za-z]')
for lang, want_cyr in (('uz', False), ('ru', True), ('en', False)):
    bad = []
    for s, t, l in rc.items_for(lang):
        if want_cyr and not CYR.search(t):
            bad.append(t)
        if not want_cyr and CYR.search(t):
            bad.append(t)          # the mixed-script bug that hit life_content
    ok(not bad, '%s: no wrong-script item -> %s' % (lang, bad[:1] or 'none'))

print('\n== attribution is present in every language ==')
for lang in LANGS:
    a = rc.attribution_for(lang)
    ok(bool(a and a.strip()), '%s: attribution text exists' % lang)
    ok('O*NET' in a, '%s: credits O*NET as CC-BY requires' % lang)

print('\n' + ('%d FAILED, ' % len(fails) if fails else '')
      + '%d checks passed' % len(passes))
sys.exit(1 if fails else 0)
