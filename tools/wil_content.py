# -*- coding: utf-8 -*-
u"""Work Importance: twenty cards a student must rank against each other.

WHY A RANKING AND NOT ANOTHER RATING SCALE
------------------------------------------
values.js already asks what a student wants from a job on an importance scale,
and says in its own header why that scale is weak: asked "is a good income
important to you?", almost every teenager says yes. Centring on the student's
own mean rescues some signal, but it cannot create information the answers never
carried.

This bank takes the information a different way. There are five levels, and a
student can put any number of cards in each one. That lets someone say that
many things matter, while still showing which matter more than others.

    values.js   ten dimensions, rated       broad, weak per dimension
    this        six values, ranked          narrow, and the trade offs are real

THE ITEMS ARE THE O*NET WORK IMPORTANCE LOCATOR
-----------------------------------------------
Twenty cards over six work values, published by the US Department of Labor and
in the public domain, which is the reason this one could be used as written when
CAAS and the VIA survey could not. The English is the published wording, lightly
shortened: the original repeats "On my ideal job it is important that..." on
every card, which is right for a printed booklet and wrong for a card a student
drags on a phone. The stem is shown once above the cards instead.

UNEQUAL CARD COUNTS, COMPARABLE AVERAGES
----------------------------------------
The six values do not get four cards each. Achievement has two, working
conditions has six, the rest have three, and that is the published instrument,
not a mistake to correct. The browser averages each value's levels instead of
letting a value win just because it has more statements.
"""

# Five levels. The labels are ordinal, not a rating: "least important" means
# the student considers that card less important than the cards placed above it.
LEVELS = [
    u'Muhim emas',
    u'Biroz muhim',
    u'Oʻrtacha',
    u'Ancha muhim',
    u'Muhim',
]

PER_LEVEL = None

VALUES = ['achievement', 'independence', 'recognition',
          'relationships', 'support', 'conditions']

NAMES = {
    'achievement':   u'Yutuq',
    'independence':  u'Mustaqillik',
    'recognition':   u'Eʼtirof',
    'relationships': u'Munosabatlar',
    'support':       u'Qoʻllab-quvvatlash',
    'conditions':    u'Ish sharoitlari',
}

LEADS = {
    'achievement':   u'Ishingiz sizga natija va yutuq hissini berishi kerak.',
    'independence':  u'Oʻz qaroringizni oʻzingiz qabul qilishingiz kerak.',
    'recognition':   u'Mehnatingiz koʻrinishi va qadrlanishi kerak.',
    'relationships': u'Odamlar bilan munosabat va vijdon sizga muhim.',
    'support':       u'Rahbariyat sizni qoʻllab-quvvatlashi kerak.',
    'conditions':    u'Ishning sharoiti va barqarorligi sizga muhim.',
}

STEM = u'Ideal ishimda men uchun quyidagilar muhim:'

# Card letter -> (value, text). The letters are the published card labels and are
# kept because they are how the instrument is documented; nothing shows them.
CARDS = [
    ('A', 'achievement',   u'Qobiliyatlarimni ishga sola olsam'),
    ('B', 'support',       u'Kompaniya menga adolatli munosabatda boʻlsa'),
    ('C', 'conditions',    u'Doim band boʻlib ishlasam'),
    ('D', 'recognition',   u'Ishda oʻsish imkoni boʻlsa'),
    ('E', 'recognition',   u'Boshqalarga koʻrsatma va yoʻnalish bera olsam'),
    ('F', 'achievement',   u'Ish menga yutuq hissini bersa'),
    ('G', 'conditions',    u'Maoshim boshqa xodimlarnikidan qolishmasa'),
    ('H', 'relationships', u'Hamkasblarim bilan til topishish oson boʻlsa'),
    ('I', 'independence',  u'Oʻz gʻoyalarimni sinab koʻra olsam'),
    ('J', 'conditions',    u'Yolgʻiz ishlay olsam'),
    ('K', 'relationships', u'Vijdonimga qarshi ish qilishga hech qachon majbur qilinmasam'),
    ('L', 'recognition',   u'Qilgan ishim uchun eʼtirof olsam'),
    ('M', 'independence',  u'Qarorlarni oʻzim qabul qila olsam'),
    ('N', 'conditions',    u'Ish barqaror va doimiy boʻlsa'),
    ('O', 'relationships', u'Boshqa odamlar uchun foydali ish qila olsam'),
    ('P', 'support',       u'Rahbarlarim xodimlarini rahbariyat oldida qoʻllasa'),
    ('Q', 'support',       u'Rahbarlarim xodimlarini yaxshi oʻrgatsa'),
    ('R', 'conditions',    u'Har kuni boshqacha ish qila olsam'),
    ('S', 'conditions',    u'Ish sharoitlari yaxshi boʻlsa'),
    ('T', 'independence',  u'Ishimni deyarli nazoratsiz oʻzim rejalashtira olsam'),
]

TITLE = u'Eng muhimi nima'
BLURB = (u'Ish bera oladigan yigirmata narsa. Har bir kartani oʻzingiz uchun '
         u'muhimlik darajasiga qoʻying; bir darajaga istagancha karta qoʻyish '
         u'mumkin.')


def _counts():
    counts = {}
    for _letter, value, _text in CARDS:
        counts[value] = counts.get(value, 0) + 1
    return counts


import wil_content_ru as _ru
import wil_content_en as _en

BY_LANG = {'uz': None, 'ru': _ru, 'en': _en}


def _mod(lang):
    return BY_LANG[lang]


def cards_for(lang):
    u"""[(letter, value, text)] keyed from the Uzbek original, paired by position."""
    if lang == 'uz':
        return [(l, v, t) for l, v, t in CARDS]
    tr = _mod(lang).CARDS
    if len(tr) != len(CARDS):
        raise ValueError('%s has %d cards, Uzbek has %d' % (lang, len(tr), len(CARDS)))
    return [(CARDS[i][0], CARDS[i][1], tr[i]) for i in range(len(CARDS))]


def levels_for(lang):
    return LEVELS if lang == 'uz' else _mod(lang).LEVELS


def names_for(lang):
    return NAMES if lang == 'uz' else _mod(lang).NAMES


def leads_for(lang):
    return LEADS if lang == 'uz' else _mod(lang).LEADS


def stem_for(lang):
    return STEM if lang == 'uz' else _mod(lang).STEM


def title_for(lang):
    return (TITLE, BLURB) if lang == 'uz' else (_mod(lang).TITLE, _mod(lang).BLURB)
