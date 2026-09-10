# -*- coding: utf-8 -*-
u"""English text for the school subjects bank. TEXT ONLY: which facet an item
belongs to, whether it is reverse scored and the order it is asked in all live
in school_content.py and are paired BY POSITION. The subject NAMES are not here
either: they come from subjects.py, which already had them in three languages.
"""

LABELS = [
    u'Disagree',
    u'Slightly disagree',
    u'Neutral',
    u'Slightly agree',
    u'Agree',
]


FACETS = [
    (u'What you can do',
     u'I can handle even the hard parts of {s}.'),
    (u'What you enjoy',
     u'{s} lessons are something I look forward to.'),
    (u'What it costs you',
     u'{s} makes me anxious, even when I have prepared.'),
]

TITLE = u'How school feels'
BLURB = (u'Eleven school subjects, asked three ways: what you can do, what you '
         u'enjoy, and what it costs you. Not your marks.')
