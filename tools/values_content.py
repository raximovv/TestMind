# -*- coding: utf-8 -*-
u"""Work Values — what a student wants FROM a job, not what they are like.

THE CONSTRUCT, AND THE MISTAKE THIS FILE EXISTS TO AVOID
--------------------------------------------------------
    value       "Kelajakdagi ishimda yangi narsalarni oʻrganish men uchun muhim."
    NOT a value "Men yangi narsalarni tez oʻrganaman."

The first says what the student WANTS from future work. The second is an ability
claim and belongs to the personality bank. Mixing them produces a scale that
correlates with Openness and measures nothing new -- three instruments, two
constructs. values_check.py enforces the sentence shape.

TEN DIMENSIONS, ONE ITEM EACH -- AND WHY THAT IS ACCEPTED
---------------------------------------------------------
Ten items means a single item per dimension, which is psychometrically weak: a
one-item scale has no internal reliability at all and a misread question moves a
whole dimension. The alternative inside a ten-item budget is five dimensions of
two items, which is more reliable but halves the number of things a career can
be matched on.

Breadth wins here because of what this signal is FOR. Values are used to
separate careers that RIASEC scores identically -- an entrepreneur and an
operations manager are both Enterprising, and it is independence versus
stability that tells them apart. A precise score on five dimensions cannot make
that distinction; a rough score on ten can.

The cost is paid honestly elsewhere:
  - values carry a LOW weight in the recommendation engine;
  - no value score is ever shown to a student as a number;
  - the profile is read as a RANKING, never as absolute strength.

RANKING, NOT LEVEL
------------------
A teenager asked "is a good income important to you?" says yes. So does the next
one. Absolute levels are almost meaningless here -- nearly everything is rated
important. What carries information is which values a student puts ABOVE their
own average, so scoring centres each student on their own mean before anything
downstream reads it. A student who marks all ten "very important" therefore ends
with a flat profile and no values signal, which is the honest outcome.
"""

LABELS = [
    u'Umuman muhim emas',
    u'Unchalik muhim emas',
    u'Oʻrtacha',
    u'Muhim',
    u'Juda muhim',
]

# key -> the short name shown on the result
DIMENSIONS = [
    'income', 'stability', 'learning', 'creativity', 'helping',
    'leadership', 'independence', 'teamwork', 'balance', 'meaning',
]

NAMES = {
    'income':       u'Daromad',
    'stability':    u'Barqarorlik',
    'learning':     u'Oʻrganish',
    'creativity':   u'Ijod erkinligi',
    'helping':      u'Odamlarga yordam',
    'leadership':   u'Yetakchilik',
    'independence': u'Mustaqillik',
    'teamwork':     u'Jamoada ishlash',
    'balance':      u'Hayot muvozanati',
    'meaning':      u'Foydali ish',
}

# One item per dimension, in the order they are asked. Every sentence is about
# the FUTURE JOB, never about the student's character.
ITEMS = [
    ('income',       u'Kelajakdagi ishimda yaxshi daromad olish men uchun muhim.'),
    ('learning',     u'Kelajakdagi ishimda doim yangi narsa oʻrganib borish men uchun muhim.'),
    ('helping',      u'Ishim orqali odamlarga yordam bera olish men uchun muhim.'),
    ('independence', u'Ishimni oʻzim rejalashtirib, mustaqil ishlay olish men uchun muhim.'),
    ('stability',    u'Ishimning barqaror va ishonchli boʻlishi men uchun muhim.'),
    ('creativity',   u'Ishimda oʻz gʻoyalarimni erkin ifodalay olish men uchun muhim.'),
    ('teamwork',     u'Jamoada, odamlar bilan birga ishlash men uchun muhim.'),
    ('leadership',   u'Ishimda qaror qabul qilish va jamoani boshqarish men uchun muhim.'),
    ('balance',      u'Ishdan tashqari oilam va shaxsiy hayotimga vaqt qolishi men uchun muhim.'),
    ('meaning',      u'Ishim jamiyatga foyda keltirishi men uchun muhim.'),
]

INTRO_H = u'Endi — kelajakdagi ishingiz'
INTRO_P = (u'Oxirgi qism. Kelajakdagi ishingizda nima muhim boʻlishini soʻraymiz. '
           u'Bu qobiliyat haqida emas — faqat siz nimani xohlaysiz.')

import values_content_ru as _ru
import values_content_en as _en

BY_LANG = {'uz': None, 'ru': _ru, 'en': _en}


def items_for(lang):
    u"""[(dimension, text)] keyed from the Uzbek original, paired by position."""
    if lang == 'uz':
        return [(d, t) for d, t in ITEMS]
    tr = BY_LANG[lang].ITEMS
    if len(tr) != len(ITEMS):
        raise ValueError('%s value list is %d, Uzbek is %d' % (lang, len(tr), len(ITEMS)))
    return [(ITEMS[i][0], tr[i]) for i in range(len(ITEMS))]


def labels_for(lang):
    return LABELS if lang == 'uz' else BY_LANG[lang].LABELS


def names_for(lang):
    return NAMES if lang == 'uz' else BY_LANG[lang].NAMES


def intro_for(lang):
    if lang == 'uz':
        return (INTRO_H, INTRO_P)
    return (BY_LANG[lang].INTRO_H, BY_LANG[lang].INTRO_P)
