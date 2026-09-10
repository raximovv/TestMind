# -*- coding: utf-8 -*-
u"""Russian text for the school subjects bank. TEXT ONLY: which facet an item
belongs to, whether it is reverse scored and the order it is asked in all live
in school_content.py and are paired BY POSITION. The subject NAMES are not here
either: they come from subjects.py, which already had them in three languages.

The frames say "по предмету «Математика»" rather than declining the subject
name. A frame that needs the prepositional case would have to be written eleven
times instead of once, and "по Родному языку и литературе" is exactly the kind
of agreement error nobody catches in review.
"""

LABELS = [
    u'Не согласен',
    u'Скорее не согласен',
    u'Нейтрально',
    u'Скорее согласен',
    u'Согласен',
]


FACETS = [
    (u'Что вам по силам',
     u'Даже самые трудные темы по предмету «{s}» мне по силам.'),
    (u'Что вам нравится',
     u'Уроки по предмету «{s}» я жду с нетерпением.'),
    (u'Что даётся вам тяжело',
     u'Даже когда я подготовился, уроки по предмету «{s}» вызывают у меня тревогу.'),
]

TITLE = u'Каким ощущается школа'
BLURB = (u'Одиннадцать школьных предметов и три вопроса к каждому: что вам по '
         u'силам, что вам нравится и что даётся тяжело. Это не про оценки.')
