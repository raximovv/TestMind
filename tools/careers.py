# -*- coding: utf-8 -*-
u"""Career families, careers and university majors — the structured layer.

THE CONTRACT (same one life_content.py and riasec_content.py use)
-----------------------------------------------------------------
Everything that DECIDES something lives here and is language-neutral: the
family an entry belongs to, its RIASEC profile, the school subjects it draws
on, the education level it needs. Everything a student READS lives in
careers_text_{uz,ru,en}.py and is paired on by key.

A translation therefore cannot move a career onto another profile, promote it
into another family, or change which subjects matter. It can only change words.

WHAT IS DELIBERATELY NOT HERE
-----------------------------
No long occupation descriptions. The temptation is to write two paragraphs per
job and end up with 150 essays nobody validated; the structure is what the
recommendation engine needs, and one honest sentence per entry is what a student
needs. Descriptions can grow later without touching this file.

No salary data, no employment forecasts, no "demand" ratings. We have no Uzbek
labour-market data, and inventing it would be the most damaging thing on the
page: a fifteen-year-old will believe a number.

RIASEC PROFILES
---------------
Each entry carries the two or three Holland scales it actually draws on, summing
to 1.0. These are blunt on purpose. They say "software engineering is mostly
investigative with a realistic streak", which is defensible, rather than
claiming a measured weighting, which is not.

EDUCATION LEVEL
---------------
    'higher'      a university degree is the normal route
    'college'     a college / technical qualification is enough to start
    'either'      both routes are genuinely common
Used to make sure the result never implies university is the only door.
"""

# ---------------------------------------------------------------- families
# key -> RIASEC profile of the family as a whole. Used to rank the FAMILIES on
# the result, which is the level a fifteen-year-old can actually act on; the
# individual careers underneath are examples, not a ranking.
FAMILIES = {
    'cs':          {'I': 0.5, 'R': 0.3, 'C': 0.2},
    'engineering': {'R': 0.5, 'I': 0.4, 'C': 0.1},
    'business':    {'E': 0.6, 'C': 0.2, 'S': 0.2},
    'finance':     {'C': 0.5, 'I': 0.3, 'E': 0.2},
    'medicine':    {'S': 0.4, 'I': 0.4, 'R': 0.2},
    'science':     {'I': 0.7, 'R': 0.2, 'A': 0.1},
    'architecture':{'A': 0.5, 'R': 0.3, 'I': 0.2},
    'psychology':  {'S': 0.6, 'I': 0.3, 'A': 0.1},
    'law':         {'E': 0.4, 'C': 0.3, 'S': 0.3},
    'education':   {'S': 0.7, 'A': 0.2, 'C': 0.1},
    'media':       {'A': 0.5, 'E': 0.3, 'S': 0.2},
    'agriculture': {'R': 0.5, 'I': 0.3, 'C': 0.2},
    'logistics':   {'R': 0.4, 'C': 0.4, 'E': 0.2},
    'arts':        {'A': 0.8, 'E': 0.1, 'S': 0.1},
    'hospitality': {'E': 0.4, 'S': 0.4, 'C': 0.2},
    'sport':       {'R': 0.4, 'S': 0.3, 'E': 0.3},
}

# The school subjects each family leans on. Keys are subjects.SUBJECT_KEYS.
# Weights sum to 1.0 within a family and are used to score performance fit.
FAMILY_SUBJECTS = {
    'cs':          {'math': 0.4, 'cs': 0.4, 'physics': 0.2},
    'engineering': {'physics': 0.4, 'math': 0.4, 'cs': 0.2},
    'business':    {'economics': 0.4, 'math': 0.3, 'english': 0.3},
    'finance':     {'math': 0.5, 'economics': 0.4, 'cs': 0.1},
    'medicine':    {'biology': 0.5, 'chemistry': 0.4, 'physics': 0.1},
    'science':     {'physics': 0.3, 'chemistry': 0.3, 'biology': 0.2, 'math': 0.2},
    'architecture':{'art': 0.4, 'math': 0.3, 'physics': 0.3},
    'psychology':  {'biology': 0.4, 'literature': 0.3, 'history': 0.3},
    'law':         {'history': 0.4, 'literature': 0.3, 'economics': 0.3},
    'education':   {'literature': 0.4, 'history': 0.3, 'english': 0.3},
    'media':       {'literature': 0.5, 'english': 0.3, 'art': 0.2},
    'agriculture': {'biology': 0.5, 'chemistry': 0.3, 'geography': 0.2},
    'logistics':   {'math': 0.4, 'geography': 0.3, 'physics': 0.3},
    'arts':        {'art': 0.7, 'literature': 0.3},
    'hospitality': {'english': 0.5, 'geography': 0.3, 'economics': 0.2},
    'sport':       {'biology': 0.6, 'geography': 0.2, 'english': 0.2},
}

# ------------------------------------------------------- careers and majors
# key: (family, riasec, subjects, education)
# `subjects` here narrows the family default where an individual entry really
# differs -- an empty dict means "the family's subjects apply".
CAREERS = {
    # ---- Computer Science & AI
    'software_engineer': ('cs', {'I': 0.5, 'R': 0.3, 'C': 0.2}, {}, 'either'),
    'ai_engineer':       ('cs', {'I': 0.7, 'R': 0.2, 'C': 0.1}, {'math': 0.5, 'cs': 0.4, 'physics': 0.1}, 'higher'),
    'data_scientist':    ('cs', {'I': 0.6, 'C': 0.3, 'A': 0.1}, {'math': 0.5, 'cs': 0.3, 'economics': 0.2}, 'higher'),
    'cybersecurity':     ('cs', {'I': 0.5, 'C': 0.4, 'R': 0.1}, {}, 'either'),
    'mobile_developer':  ('cs', {'I': 0.4, 'R': 0.3, 'A': 0.3}, {}, 'either'),
    'frontend_developer':('cs', {'A': 0.4, 'I': 0.4, 'R': 0.2}, {'cs': 0.5, 'art': 0.3, 'math': 0.2}, 'either'),
    'systems_analyst':   ('cs', {'I': 0.4, 'C': 0.4, 'E': 0.2}, {}, 'higher'),

    # ---- Engineering & Robotics
    'civil_engineer':      ('engineering', {'R': 0.5, 'C': 0.3, 'I': 0.2}, {}, 'higher'),
    'mechanical_engineer': ('engineering', {'R': 0.5, 'I': 0.4, 'C': 0.1}, {}, 'higher'),
    'electrical_engineer': ('engineering', {'R': 0.4, 'I': 0.5, 'C': 0.1}, {}, 'higher'),
    'robotics_engineer':   ('engineering', {'R': 0.4, 'I': 0.5, 'A': 0.1}, {'physics': 0.4, 'cs': 0.4, 'math': 0.2}, 'higher'),
    'industrial_engineer': ('engineering', {'C': 0.4, 'R': 0.3, 'E': 0.3}, {}, 'higher'),
    'technician':          ('engineering', {'R': 0.7, 'C': 0.3}, {}, 'college'),

    # ---- Business & Entrepreneurship
    'entrepreneur':      ('business', {'E': 0.7, 'C': 0.2, 'A': 0.1}, {}, 'either'),
    'product_manager':   ('business', {'E': 0.4, 'I': 0.3, 'S': 0.3}, {}, 'higher'),
    'business_analyst':  ('business', {'I': 0.4, 'C': 0.4, 'E': 0.2}, {'math': 0.4, 'economics': 0.4, 'cs': 0.2}, 'higher'),
    'marketing_manager': ('business', {'E': 0.5, 'A': 0.3, 'S': 0.2}, {}, 'either'),
    'operations_manager':('business', {'C': 0.5, 'E': 0.3, 'R': 0.2}, {}, 'either'),
    'sales_manager':     ('business', {'E': 0.6, 'S': 0.3, 'C': 0.1}, {}, 'either'),
}

MAJORS = {
    # ---- Computer Science & AI
    'major_cs':            ('cs', {'I': 0.5, 'R': 0.3, 'C': 0.2}, {}, 'higher'),
    'major_software_eng':  ('cs', {'I': 0.5, 'C': 0.3, 'R': 0.2}, {}, 'higher'),
    'major_data_science':  ('cs', {'I': 0.6, 'C': 0.3, 'A': 0.1}, {'math': 0.5, 'cs': 0.3, 'economics': 0.2}, 'higher'),
    'major_info_security': ('cs', {'I': 0.5, 'C': 0.4, 'R': 0.1}, {}, 'higher'),

    # ---- Engineering & Robotics
    'major_civil_eng':     ('engineering', {'R': 0.5, 'C': 0.3, 'I': 0.2}, {}, 'higher'),
    'major_mechanical_eng':('engineering', {'R': 0.5, 'I': 0.4, 'C': 0.1}, {}, 'higher'),
    'major_electrical_eng':('engineering', {'I': 0.5, 'R': 0.4, 'C': 0.1}, {}, 'higher'),
    'major_mechatronics':  ('engineering', {'R': 0.4, 'I': 0.5, 'A': 0.1}, {'physics': 0.4, 'cs': 0.4, 'math': 0.2}, 'higher'),

    # ---- Business & Entrepreneurship
    'major_management':    ('business', {'E': 0.6, 'C': 0.2, 'S': 0.2}, {}, 'higher'),
    'major_marketing':     ('business', {'E': 0.5, 'A': 0.3, 'S': 0.2}, {}, 'higher'),
    'major_business_admin':('business', {'E': 0.5, 'C': 0.3, 'S': 0.2}, {}, 'higher'),
}

FAMILY_KEYS = sorted(FAMILIES.keys())
EDUCATION_LEVELS = ('higher', 'college', 'either')


def _unpack(table, key):
    fam, riasec, subs, edu = table[key]
    return {'family': fam, 'riasec': riasec,
            'subjects': subs or FAMILY_SUBJECTS[fam], 'education': edu}


def career(key):  return _unpack(CAREERS, key)
def major(key):   return _unpack(MAJORS, key)

def careers_in(family):
    return [k for k in sorted(CAREERS) if CAREERS[k][0] == family]

def majors_in(family):
    return [k for k in sorted(MAJORS) if MAJORS[k][0] == family]


def populated_families():
    u"""Families that actually have entries yet.

    The sixteen families are all defined so the engine and the result page can be
    built against the finished shape, but only some carry careers and majors so
    far. Anything ranking families must skip the empty ones rather than offer a
    student a heading with nothing under it.
    """
    return [f for f in FAMILY_KEYS if careers_in(f) or majors_in(f)]
