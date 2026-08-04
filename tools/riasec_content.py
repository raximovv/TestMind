# -*- coding: utf-8 -*-
u"""The career-interest item bank (RIASEC) — Uzbek original.

WHAT THIS MEASURES, AND WHY IT IS NOT THE BIG FIVE
--------------------------------------------------
The Big Five test measures personality. This measures *interests*, and for the
question a student is actually asking -- "what should I study, what should I
become" -- interests are the better instrument: they predict educational and
occupational choice better than personality does, and they add information over
and above both personality and ability. TestMind's Big Five result should end up
supporting this one, not the other way round.

Six scales, from Holland's model:
    R  Realistic      hands, tools, machines, outdoors
    I  Investigative  analysing, researching, working things out
    A  Artistic       creating, designing, performing
    S  Social         teaching, helping, caring for people
    E  Enterprising   persuading, leading, selling, organising people
    C  Conventional   records, numbers, order, procedure

PROVENANCE AND LICENCE
----------------------
Item format and the six-scale structure follow the O*NET Interest Profiler
(U.S. Department of Labor, Employment and Training Administration), which is
released under a Creative Commons Attribution 4.0 International Licence and may
therefore be used commercially with attribution. The RIASEC model itself is
Holland (1959, 1997).

The items below are NOT translations of the O*NET items. They are written fresh
in the same activity-statement style, because the official bank is written for
American adults choosing an occupation ("Lay brick or tile", "Build kitchen
cabinets") and reads as a list of foreign job duties to an Uzbek fourteen-year-
old. An item a student cannot picture themselves doing measures nothing. Every
item here names an activity a teenager in Uzbekistan can actually imagine.

What we must NOT use: the brief public-domain RIASEC marker scales of Armstrong,
Allison & Rounds (2008) are free to researchers and practitioners for
NON-COMMERCIAL use only. TestMind is sold to schools. They are off limits, and
they are the first thing a search turns up, so this is written down here rather
than left to memory.

NO REVERSE-KEYED ITEMS -- ON PURPOSE
------------------------------------
The Big Five bank balances forward and reverse items so that a student who
agrees with everything lands on a flat 3.0 instead of a fake profile. Interest
inventories do not work that way and should not: "I would dislike repairing an
engine" is a different and worse question than "I would like to repair an
engine". Straightlining is handled instead by the scoring, which ranks the six
scales against each other -- a student who likes everything gets six high scores
and therefore no strong code, which is the honest answer. riasec_check.py
asserts this.

THE BANK IS 8 ITEMS PER SCALE, USED ADAPTIVELY
----------------------------------------------
    core     5 per scale = 30 items   everyone answers these
    reserve  3 per scale = 18 items   only for the scales still in contention

marked with late=1. Same shape as the Big Five test's CORE_PLAN / RESERVE split,
for the same reason: a student whose top interests are already clear should not
sit through eighteen more questions to be told what item 30 already said.
"""

# The response scale is Like/Dislike, NOT agreement. A student is being asked
# whether they would enjoy the activity, not whether the sentence is true of
# them, and the labels have to say so or the item means something else.
LABELS = [
    u'Umuman yoqmaydi',
    u'Unchalik yoqmaydi',
    u'Farqi yoʻq',
    u'Yoqadi',
    u'Juda yoqadi',
]

SCALES = ['R', 'I', 'A', 'S', 'E', 'C']

SCALE_NAMES = {
    'R': u'Amaliy ish',
    'I': u'Tadqiqot',
    'A': u'Ijod',
    'S': u'Odamlarga yordam',
    'E': u'Tashabbus va yetakchilik',
    'C': u'Tartib va aniqlik',
}

# One line each, written to be read by a fifteen-year-old, not by a careers
# adviser. These appear under the result, so they say what the scale means in
# terms of what the student would be DOING.
SCALE_LEADS = {
    'R': u'Qoʻl bilan ishlash, texnika, asbob-uskuna va ochiq havodagi ish.',
    'I': u'Sabab izlash, tahlil qilish, murakkab masalani yechish.',
    'A': u'Yaratish, chizish, yozish, dizayn va sahna.',
    'S': u'Odamlarga oʻrgatish, yordam berish va gʻamxoʻrlik qilish.',
    'E': u'Ishontirish, boshqarish, sotish va tashkil qilish.',
    'C': u'Hujjat, hisob, tartib va aniq qoidalar bilan ishlash.',
}

# ---------------------------------------------------------------- the items
#
# (scale, text, late) -- late=1 means reserve, asked only when that scale is
# still contested after the core. Five core items come first in each block so
# the split is visible on the page rather than hidden in a flag.

ITEMS = [
    # ---- R: Realistic -------------------------------------------------
    ('R', u'Buzilgan velosiped yoki mototsiklni tuzatish', 0),
    ('R', u'Yogʻochdan stol, javon yoki kursi yasash', 0),
    ('R', u'Buzilgan telefonni ochib, ichidagi qismlarni koʻrish', 0),
    ('R', u'Bogʻda daraxt va sabzavot yetishtirish', 0),
    ('R', u'Uydagi elektr simini ulash yoki rozetka oʻrnatish', 0),
    ('R', u'Qurilishda gʻisht terish yoki devor suvash', 1),
    ('R', u'Traktor yoki yuk mashinasini boshqarish', 1),
    ('R', u'Kun boʻyi ochiq havoda jismoniy ishlash', 1),

    # ---- I: Investigative ---------------------------------------------
    ('I', u'Laboratoriyada tajriba oʻtkazish', 0),
    ('I', u'Murakkab matematik masalani yechish', 0),
    ('I', u'Kasallikning sababini aniqlash uchun tahlil qilish', 0),
    ('I', u'Bir narsa nima uchun shunday ishlashini oxirigacha tushunish', 0),
    ('I', u'Yulduzlar, sayyoralar va koinotni oʻrganish', 0),
    ('I', u'Raqamlar va statistikani tahlil qilib xulosa chiqarish', 1),
    ('I', u'Yangi dori yoki vaksina ustida ishlash', 1),
    ('I', u'Tabiat hodisalarini kuzatib, ulardagi qonuniyatni izlash', 1),

    # ---- A: Artistic ---------------------------------------------------
    ('A', u'Rasm chizish yoki portret ishlash', 0),
    ('A', u'Musiqa asbobida kuy ijro etish yoki qoʻshiq yozish', 0),
    ('A', u'Hikoya, sheʼr yoki ssenariy yozish', 0),
    ('A', u'Video suratga olish va montaj qilish', 0),
    ('A', u'Kiyim yoki bezak dizaynini oʻylab topish', 0),
    ('A', u'Teatr yoki kinoda rol oʻynash', 1),
    ('A', u'Xona yoki bino ichki koʻrinishini loyihalash', 1),
    ('A', u'Raqs yoki sahna harakatini qoʻyish', 1),

    # ---- S: Social -----------------------------------------------------
    ('S', u'Kichik bolalarga dars berish', 0),
    ('S', u'Sinfdoshingizga tushunmagan mavzuni tushuntirish', 0),
    ('S', u'Qiynalayotgan odamni tinglab, unga yordam berish', 0),
    ('S', u'Kasal yoki keksa odamga qarash', 0),
    ('S', u'Koʻngilli boʻlib xayriya ishlarida qatnashish', 0),
    ('S', u'Nogironligi bor bolalar bilan ishlash', 1),
    ('S', u'Urishib qolgan ikki odamni yarashtirish', 1),
    ('S', u'Sport toʻgaragida bolalarga murabbiylik qilish', 1),

    # ---- E: Enterprising -----------------------------------------------
    ('E', u'Oʻz biznesingizni ochish va uni boshqarish', 0),
    ('E', u'Mahsulot sotish va mijoz bilan kelishuvga erishish', 0),
    ('E', u'Guruhga rahbarlik qilib, ishni odamlarga taqsimlash', 0),
    ('E', u'Koʻpchilik oldida nutq soʻzlab, ularni ishontirish', 0),
    ('E', u'Katta tadbir tashkil qilib, unga homiy topish', 0),
    ('E', u'Bahsda oʻz fikringizni oxirigacha himoya qilish', 1),
    ('E', u'Yangi gʻoyani odamlarga tanishtirib, ularni jalb qilish', 1),
    ('E', u'Reklama kampaniyasini oʻylab topish va yuritish', 1),

    # ---- C: Conventional ------------------------------------------------
    ('C', u'Hujjatlarni tartibga solib, joy-joyiga qoʻyish', 0),
    ('C', u'Pul hisobini yuritish va hisobot tayyorlash', 0),
    ('C', u'Jadval va roʻyxatlarni toʻldirib borish', 0),
    ('C', u'Maʼlumotlarni bazaga xatosiz kiritish', 0),
    ('C', u'Ish jadvalini tuzib, muddatlarni nazorat qilish', 0),
    ('C', u'Omborda mahsulot hisobini olib borish', 1),
    ('C', u'Kutubxonada kitoblarni tizimga solish', 1),
    ('C', u'Belgilangan qoidaga qatʼiy amal qilib ish yuritish', 1),
]

CORE_PER_SCALE = 5
RESERVE_PER_SCALE = 3

# Shown under the result and on any page that carries the test. Required by the
# CC-BY licence, and it is also the strongest credibility line we have in front
# of a school: this is the framework the American public system uses.
ATTRIBUTION = (
    u'Savollar Holland (RIASEC) qiziqish modeli va AQSH Mehnat vazirligining '
    u'O*NET Interest Profiler uslubi asosida tayyorlangan (CC BY 4.0). '
    u'Savollar oʻzbek oʻsmirlari uchun alohida yozilgan.'
)


# --------------------------------------------------------------- translations
#
# Same contract as life_content.py: a translation carries TEXT ONLY. The scale
# keying and the core/reserve split live here in the Uzbek original and are
# paired onto translated text by position, so a translation cannot silently
# move an item from Realistic to Social or promote a reserve item into the core.
import riasec_content_ru as _ru
import riasec_content_en as _en

BY_LANG = {'uz': None, 'ru': _ru, 'en': _en}


def items_for(lang):
    u"""[(scale, text, late)] in the requested language, keyed from the Uzbek."""
    if lang == 'uz':
        return [(s, t, l) for s, t, l in ITEMS]
    tr = BY_LANG[lang].ITEMS
    if len(tr) != len(ITEMS):
        raise ValueError('%s item list is %d, Uzbek is %d'
                         % (lang, len(tr), len(ITEMS)))
    return [(ITEMS[i][0], tr[i], ITEMS[i][2]) for i in range(len(ITEMS))]


def labels_for(lang):
    return LABELS if lang == 'uz' else BY_LANG[lang].LABELS


def scale_names_for(lang):
    return SCALE_NAMES if lang == 'uz' else BY_LANG[lang].SCALE_NAMES


def scale_leads_for(lang):
    return SCALE_LEADS if lang == 'uz' else BY_LANG[lang].SCALE_LEADS


def attribution_for(lang):
    return ATTRIBUTION if lang == 'uz' else BY_LANG[lang].ATTRIBUTION
