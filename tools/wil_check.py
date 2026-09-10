# -*- coding: utf-8 -*-
u"""Asserts the Work Importance bank.

The bank must have five meaningful levels and twenty distinct cards. Unequal
numbers of cards per value are expected; the browser averages each value's
levels so no value wins merely because it has more statements.

    python wil_check.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wil_content as wc

fails, passes = [], []


def ok(cond, msg):
    (passes if cond else fails).append(msg)
    print(('  PASS ' if cond else '  FAIL ') + msg)


LANGS = ('uz', 'ru', 'en')
DASHES = re.compile(u'[‐-―−]')

print('== the sort can be completed ==')
ok(len(wc.LEVELS) == 5, 'five levels (%d)' % len(wc.LEVELS))
ok(len(wc.CARDS) == 20, 'twenty cards can be placed (%d)' % len(wc.CARDS))

print('\n== structure ==')
letters = [l for l, _, _ in wc.CARDS]
ok(len(letters) == len(set(letters)), 'card letters are unique')
ok(letters == sorted(letters), 'card letters are in order')
values = [v for _, v, _ in wc.CARDS]
ok(set(values) == set(wc.VALUES), 'every value is carried by at least one card')
ok(len(wc.VALUES) == len(set(wc.VALUES)), 'values are unique')

print('\n== unequal card counts are expected ==')
counts = {}
for value in values:
    counts[value] = counts.get(value, 0) + 1
print('    cards per value: %s' % counts)
ok(all(counts.get(v, 0) > 0 for v in wc.VALUES),
   'every value has at least one card for averaging')

print('\n== translations ==')
uz = wc.cards_for('uz')
for lang in LANGS:
    cards = wc.cards_for(lang)
    ok(len(cards) == len(wc.CARDS), '%s: %d cards' % (lang, len(cards)))
    ok([(l, v) for l, v, _ in cards] == [(l, v) for l, v, _ in uz],
       '%s: letter and value keying identical to the Uzbek' % lang)
    ok(len(wc.levels_for(lang)) == 5, '%s: five level labels' % lang)

    names = wc.names_for(lang)
    ok(sorted(names) == sorted(wc.VALUES), '%s: every value named' % lang)
    leads = wc.leads_for(lang)
    ok(sorted(leads) == sorted(wc.VALUES), '%s: every value has a lead line' % lang)
    ok(all(v.strip() for v in list(names.values()) + list(leads.values())),
       '%s: no blank name or lead' % lang)

    texts = [t for _, _, t in cards]
    ok(len(set(texts)) == len(texts), '%s: no two cards share wording' % lang)
    ok(all(t.strip() for t in texts), '%s: no blank card' % lang)
    # The stem carries the sentence; a card that ends in a full stop has been
    # written as a standalone sentence and will read as a duplicate of the stem.
    ok(not any(t.rstrip().endswith('.') for t in texts),
       '%s: cards continue the stem rather than restating it' % lang)
    ok(wc.stem_for(lang).rstrip().endswith(':'),
       '%s: the stem introduces the cards' % lang)

    head, blurb = wc.title_for(lang)
    ok(bool(head.strip()) and bool(blurb.strip()), '%s: title and blurb present' % lang)

print('\n== no typographic dashes ==')
for lang in LANGS:
    head, blurb = wc.title_for(lang)
    strings = ([t for _, _, t in wc.cards_for(lang)] + list(wc.levels_for(lang))
               + list(wc.names_for(lang).values()) + list(wc.leads_for(lang).values())
               + [wc.stem_for(lang), head, blurb])
    bad = [s for s in strings if DASHES.search(s)]
    ok(not bad, '%s: none (%s)' % (lang, bad[0] if bad else 'clean'))

print('\n%d passed, %d failed' % (len(passes), len(fails)))
sys.exit(1 if fails else 0)
