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
    # ---- agriculture
    'agronomist': ('agriculture', {'C': 0.15, 'I': 0.35, 'R': 0.5}, {'biology': 0.5, 'chemistry': 0.3, 'geography': 0.2}, 'either'),
    'ecologist': ('agriculture', {'I': 0.45, 'R': 0.3, 'S': 0.25}, {'biology': 0.5, 'chemistry': 0.2, 'geography': 0.3}, 'higher'),
    'farm_manager': ('agriculture', {'C': 0.2, 'E': 0.35, 'R': 0.45}, {'biology': 0.4, 'chemistry': 0.3, 'geography': 0.3}, 'either'),
    'food_technologist': ('agriculture', {'C': 0.2, 'I': 0.45, 'R': 0.35}, {'biology': 0.4, 'chemistry': 0.5, 'geography': 0.1}, 'higher'),
    'veterinarian': ('agriculture', {'I': 0.35, 'R': 0.35, 'S': 0.3}, {'biology': 0.6, 'chemistry': 0.3, 'geography': 0.1}, 'higher'),
    # ---- architecture
    'architect': ('architecture', {'A': 0.5, 'I': 0.2, 'R': 0.3}, {'art': 0.4, 'math': 0.3, 'physics': 0.3}, 'higher'),
    'industrial_designer': ('architecture', {'A': 0.5, 'I': 0.2, 'R': 0.3}, {'art': 0.4, 'math': 0.3, 'physics': 0.3}, 'higher'),
    'interior_designer': ('architecture', {'A': 0.7, 'E': 0.1, 'R': 0.2}, {'art': 0.6, 'math': 0.2, 'physics': 0.2}, 'either'),
    'landscape_designer': ('architecture', {'A': 0.6, 'I': 0.1, 'R': 0.3}, {'art': 0.4, 'biology': 0.3, 'geography': 0.3}, 'either'),
    'urban_planner': ('architecture', {'A': 0.3, 'C': 0.3, 'I': 0.4}, {'art': 0.3, 'geography': 0.4, 'math': 0.3}, 'higher'),
    # ---- arts
    'actor': ('arts', {'A': 0.7, 'E': 0.2, 'S': 0.1}, {'art': 0.5, 'literature': 0.5}, 'either'),
    'animator': ('arts', {'A': 0.7, 'I': 0.2, 'R': 0.1}, {'art': 0.6, 'cs': 0.3, 'literature': 0.1}, 'either'),
    'artist': ('arts', {'A': 0.85, 'E': 0.05, 'I': 0.1}, {'art': 0.8, 'literature': 0.2}, 'either'),
    'fashion_designer': ('arts', {'A': 0.75, 'E': 0.15, 'R': 0.1}, {'art': 0.7, 'economics': 0.15, 'literature': 0.15}, 'either'),
    'graphic_designer': ('arts', {'A': 0.7, 'E': 0.1, 'R': 0.2}, {'art': 0.7, 'cs': 0.15, 'literature': 0.15}, 'either'),
    'musician': ('arts', {'A': 0.85, 'E': 0.05, 'S': 0.1}, {'art': 0.7, 'literature': 0.3}, 'either'),
    # ---- business
    'business_analyst': ('business', {'C': 0.4, 'E': 0.2, 'I': 0.4}, {'cs': 0.2, 'economics': 0.4, 'math': 0.4}, 'higher'),
    'entrepreneur': ('business', {'A': 0.1, 'C': 0.2, 'E': 0.7}, {}, 'either'),
    'marketing_manager': ('business', {'A': 0.3, 'E': 0.5, 'S': 0.2}, {}, 'either'),
    'operations_manager': ('business', {'C': 0.5, 'E': 0.3, 'R': 0.2}, {}, 'either'),
    'product_manager': ('business', {'E': 0.4, 'I': 0.3, 'S': 0.3}, {}, 'higher'),
    'sales_manager': ('business', {'C': 0.1, 'E': 0.6, 'S': 0.3}, {}, 'either'),
    # ---- cs
    'ai_engineer': ('cs', {'C': 0.1, 'I': 0.7, 'R': 0.2}, {'cs': 0.4, 'math': 0.5, 'physics': 0.1}, 'higher'),
    'cybersecurity': ('cs', {'C': 0.4, 'I': 0.5, 'R': 0.1}, {}, 'either'),
    'data_scientist': ('cs', {'A': 0.1, 'C': 0.3, 'I': 0.6}, {'cs': 0.3, 'economics': 0.2, 'math': 0.5}, 'higher'),
    'frontend_developer': ('cs', {'A': 0.4, 'I': 0.4, 'R': 0.2}, {'art': 0.3, 'cs': 0.5, 'math': 0.2}, 'either'),
    'mobile_developer': ('cs', {'A': 0.3, 'I': 0.4, 'R': 0.3}, {}, 'either'),
    'software_engineer': ('cs', {'C': 0.2, 'I': 0.5, 'R': 0.3}, {}, 'either'),
    'systems_analyst': ('cs', {'C': 0.4, 'E': 0.2, 'I': 0.4}, {}, 'higher'),
    # ---- education
    'methodologist': ('education', {'C': 0.4, 'I': 0.25, 'S': 0.35}, {}, 'higher'),
    'primary_teacher': ('education', {'A': 0.15, 'C': 0.1, 'S': 0.75}, {}, 'either'),
    'school_principal': ('education', {'C': 0.2, 'E': 0.4, 'S': 0.4}, {}, 'higher'),
    'teacher': ('education', {'A': 0.2, 'C': 0.1, 'S': 0.7}, {}, 'higher'),
    'tutor': ('education', {'E': 0.15, 'I': 0.25, 'S': 0.6}, {}, 'either'),
    'university_lecturer': ('education', {'A': 0.1, 'I': 0.45, 'S': 0.45}, {}, 'higher'),
    # ---- engineering
    'civil_engineer': ('engineering', {'C': 0.3, 'I': 0.2, 'R': 0.5}, {}, 'higher'),
    'electrical_engineer': ('engineering', {'C': 0.1, 'I': 0.5, 'R': 0.4}, {}, 'higher'),
    'industrial_engineer': ('engineering', {'C': 0.4, 'E': 0.3, 'R': 0.3}, {}, 'higher'),
    'mechanical_engineer': ('engineering', {'C': 0.1, 'I': 0.4, 'R': 0.5}, {}, 'higher'),
    'robotics_engineer': ('engineering', {'A': 0.1, 'I': 0.5, 'R': 0.4}, {'cs': 0.4, 'math': 0.2, 'physics': 0.4}, 'higher'),
    'technician': ('engineering', {'C': 0.3, 'R': 0.7}, {}, 'college'),
    # ---- finance
    'accountant': ('finance', {'C': 0.7, 'E': 0.1, 'I': 0.2}, {}, 'either'),
    'auditor': ('finance', {'C': 0.6, 'E': 0.1, 'I': 0.3}, {}, 'higher'),
    'banker': ('finance', {'C': 0.4, 'E': 0.4, 'S': 0.2}, {}, 'either'),
    'financial_analyst': ('finance', {'C': 0.4, 'E': 0.1, 'I': 0.5}, {'cs': 0.1, 'economics': 0.4, 'math': 0.5}, 'higher'),
    'investment_analyst': ('finance', {'C': 0.2, 'E': 0.3, 'I': 0.5}, {'cs': 0.1, 'economics': 0.4, 'math': 0.5}, 'higher'),
    'tax_specialist': ('finance', {'C': 0.7, 'E': 0.2, 'I': 0.1}, {}, 'either'),
    # ---- hospitality
    'chef': ('hospitality', {'A': 0.4, 'E': 0.2, 'R': 0.4}, {'biology': 0.3, 'chemistry': 0.4, 'economics': 0.3}, 'college'),
    'event_manager': ('hospitality', {'A': 0.3, 'E': 0.45, 'S': 0.25}, {'art': 0.3, 'economics': 0.3, 'english': 0.4}, 'either'),
    'hotel_manager': ('hospitality', {'C': 0.2, 'E': 0.45, 'S': 0.35}, {'economics': 0.3, 'english': 0.5, 'geography': 0.2}, 'either'),
    'restaurant_manager': ('hospitality', {'C': 0.3, 'E': 0.45, 'S': 0.25}, {'economics': 0.4, 'english': 0.3, 'geography': 0.3}, 'either'),
    'tour_guide': ('hospitality', {'A': 0.2, 'E': 0.35, 'S': 0.45}, {'english': 0.4, 'geography': 0.4, 'history': 0.2}, 'either'),
    'travel_agent': ('hospitality', {'C': 0.25, 'E': 0.4, 'S': 0.35}, {'economics': 0.1, 'english': 0.5, 'geography': 0.4}, 'either'),
    # ---- law
    'diplomat': ('law', {'E': 0.4, 'I': 0.25, 'S': 0.35}, {'english': 0.4, 'history': 0.35, 'literature': 0.25}, 'higher'),
    'judge': ('law', {'C': 0.45, 'E': 0.25, 'S': 0.3}, {'economics': 0.25, 'history': 0.4, 'literature': 0.35}, 'higher'),
    'lawyer': ('law', {'C': 0.3, 'E': 0.4, 'S': 0.3}, {'economics': 0.3, 'history': 0.4, 'literature': 0.3}, 'higher'),
    'legal_advisor': ('law', {'C': 0.45, 'E': 0.3, 'I': 0.25}, {'economics': 0.35, 'history': 0.35, 'literature': 0.3}, 'either'),
    'notary': ('law', {'C': 0.7, 'E': 0.1, 'S': 0.2}, {}, 'higher'),
    'prosecutor': ('law', {'C': 0.35, 'E': 0.45, 'S': 0.2}, {'economics': 0.3, 'history': 0.4, 'literature': 0.3}, 'higher'),
    # ---- logistics
    'construction_manager': ('logistics', {'C': 0.3, 'E': 0.35, 'R': 0.35}, {'geography': 0.2, 'math': 0.4, 'physics': 0.4}, 'higher'),
    'electrician': ('logistics', {'C': 0.2, 'E': 0.1, 'R': 0.7}, {'geography': 0.1, 'math': 0.4, 'physics': 0.5}, 'college'),
    'logistician': ('logistics', {'C': 0.45, 'E': 0.25, 'R': 0.3}, {'geography': 0.4, 'math': 0.4, 'physics': 0.2}, 'either'),
    'supply_chain_manager': ('logistics', {'C': 0.4, 'E': 0.35, 'R': 0.25}, {'economics': 0.3, 'geography': 0.3, 'math': 0.4}, 'higher'),
    'surveyor': ('logistics', {'C': 0.35, 'I': 0.2, 'R': 0.45}, {'geography': 0.4, 'math': 0.4, 'physics': 0.2}, 'college'),
    'warehouse_manager': ('logistics', {'C': 0.5, 'E': 0.2, 'R': 0.3}, {'geography': 0.3, 'math': 0.5, 'physics': 0.2}, 'college'),
    # ---- media
    'copywriter': ('media', {'A': 0.6, 'E': 0.25, 'I': 0.15}, {'art': 0.1, 'english': 0.3, 'literature': 0.6}, 'either'),
    'editor': ('media', {'A': 0.45, 'C': 0.35, 'S': 0.2}, {'english': 0.3, 'history': 0.1, 'literature': 0.6}, 'higher'),
    'journalist': ('media', {'A': 0.4, 'E': 0.35, 'S': 0.25}, {'english': 0.3, 'history': 0.2, 'literature': 0.5}, 'either'),
    'photographer': ('media', {'A': 0.7, 'E': 0.1, 'R': 0.2}, {'art': 0.6, 'literature': 0.2, 'physics': 0.2}, 'either'),
    'smm_specialist': ('media', {'A': 0.4, 'C': 0.2, 'E': 0.4}, {'art': 0.2, 'english': 0.4, 'literature': 0.4}, 'either'),
    'tv_producer': ('media', {'A': 0.4, 'C': 0.2, 'E': 0.4}, {'art': 0.3, 'english': 0.3, 'literature': 0.4}, 'higher'),
    # ---- medicine
    'dentist': ('medicine', {'I': 0.25, 'R': 0.4, 'S': 0.35}, {'biology': 0.5, 'chemistry': 0.4, 'physics': 0.1}, 'higher'),
    'doctor': ('medicine', {'I': 0.4, 'R': 0.2, 'S': 0.4}, {'biology': 0.5, 'chemistry': 0.4, 'physics': 0.1}, 'higher'),
    'lab_technician': ('medicine', {'C': 0.4, 'I': 0.5, 'R': 0.1}, {'biology': 0.4, 'chemistry': 0.5, 'math': 0.1}, 'college'),
    'nurse': ('medicine', {'C': 0.2, 'R': 0.2, 'S': 0.6}, {}, 'college'),
    'paramedic': ('medicine', {'C': 0.2, 'R': 0.4, 'S': 0.4}, {}, 'college'),
    'pharmacist': ('medicine', {'C': 0.4, 'I': 0.4, 'S': 0.2}, {'biology': 0.4, 'chemistry': 0.5, 'math': 0.1}, 'higher'),
    'surgeon': ('medicine', {'I': 0.35, 'R': 0.4, 'S': 0.25}, {'biology': 0.5, 'chemistry': 0.3, 'physics': 0.2}, 'higher'),
    # ---- psychology
    'hr_specialist': ('psychology', {'C': 0.2, 'E': 0.35, 'S': 0.45}, {'economics': 0.35, 'history': 0.3, 'literature': 0.35}, 'either'),
    'psychologist': ('psychology', {'A': 0.1, 'I': 0.3, 'S': 0.6}, {'biology': 0.4, 'history': 0.3, 'literature': 0.3}, 'higher'),
    'school_counselor': ('psychology', {'C': 0.1, 'I': 0.2, 'S': 0.7}, {}, 'higher'),
    'social_worker': ('psychology', {'C': 0.15, 'I': 0.1, 'S': 0.75}, {}, 'either'),
    'speech_therapist': ('psychology', {'C': 0.15, 'I': 0.2, 'S': 0.65}, {'biology': 0.4, 'history': 0.2, 'literature': 0.4}, 'higher'),
    'therapist': ('psychology', {'A': 0.1, 'I': 0.25, 'S': 0.65}, {'biology': 0.4, 'history': 0.25, 'literature': 0.35}, 'higher'),
    # ---- science
    'biologist': ('science', {'I': 0.7, 'R': 0.2, 'S': 0.1}, {'biology': 0.6, 'chemistry': 0.3, 'math': 0.1}, 'higher'),
    'chemist': ('science', {'C': 0.1, 'I': 0.7, 'R': 0.2}, {'chemistry': 0.6, 'math': 0.2, 'physics': 0.2}, 'higher'),
    'environmental_scientist': ('science', {'I': 0.5, 'R': 0.3, 'S': 0.2}, {'biology': 0.4, 'chemistry': 0.3, 'geography': 0.3}, 'higher'),
    'geneticist': ('science', {'C': 0.15, 'I': 0.75, 'S': 0.1}, {'biology': 0.6, 'chemistry': 0.3, 'math': 0.1}, 'higher'),
    'physicist': ('science', {'A': 0.1, 'I': 0.8, 'R': 0.1}, {'math': 0.5, 'physics': 0.5}, 'higher'),
    'researcher': ('science', {'A': 0.2, 'C': 0.1, 'I': 0.7}, {}, 'higher'),
    # ---- sport
    'athlete': ('sport', {'E': 0.25, 'R': 0.55, 'S': 0.2}, {'biology': 0.7, 'english': 0.15, 'geography': 0.15}, 'either'),
    'coach': ('sport', {'E': 0.25, 'R': 0.35, 'S': 0.4}, {'biology': 0.6, 'english': 0.3, 'geography': 0.1}, 'either'),
    'fitness_trainer': ('sport', {'E': 0.2, 'R': 0.4, 'S': 0.4}, {'biology': 0.7, 'english': 0.2, 'geography': 0.1}, 'college'),
    'pe_teacher': ('sport', {'E': 0.15, 'R': 0.35, 'S': 0.5}, {'biology': 0.6, 'english': 0.2, 'geography': 0.2}, 'higher'),
    'physiotherapist': ('sport', {'I': 0.25, 'R': 0.3, 'S': 0.45}, {'biology': 0.7, 'english': 0.2, 'geography': 0.1}, 'higher'),
    'sports_manager': ('sport', {'C': 0.3, 'E': 0.5, 'S': 0.2}, {'biology': 0.3, 'economics': 0.4, 'english': 0.3}, 'higher'),
}

MAJORS = {
    # ---- agriculture
    'major_agronomy': ('agriculture', {'C': 0.15, 'I': 0.35, 'R': 0.5}, {'biology': 0.5, 'chemistry': 0.3, 'geography': 0.2}, 'higher'),
    'major_ecology': ('agriculture', {'I': 0.45, 'R': 0.3, 'S': 0.25}, {'biology': 0.5, 'chemistry': 0.2, 'geography': 0.3}, 'higher'),
    'major_food_technology': ('agriculture', {'C': 0.2, 'I': 0.45, 'R': 0.35}, {'biology': 0.4, 'chemistry': 0.5, 'geography': 0.1}, 'higher'),
    'major_veterinary': ('agriculture', {'I': 0.35, 'R': 0.35, 'S': 0.3}, {'biology': 0.6, 'chemistry': 0.3, 'geography': 0.1}, 'higher'),
    # ---- architecture
    'major_architecture': ('architecture', {'A': 0.5, 'I': 0.2, 'R': 0.3}, {'art': 0.4, 'math': 0.3, 'physics': 0.3}, 'higher'),
    'major_interior_design': ('architecture', {'A': 0.7, 'E': 0.1, 'R': 0.2}, {'art': 0.6, 'math': 0.2, 'physics': 0.2}, 'higher'),
    'major_urban_planning': ('architecture', {'A': 0.3, 'C': 0.3, 'I': 0.4}, {'art': 0.3, 'geography': 0.4, 'math': 0.3}, 'higher'),
    # ---- arts
    'major_fine_arts': ('arts', {'A': 0.85, 'E': 0.05, 'I': 0.1}, {'art': 0.8, 'literature': 0.2}, 'higher'),
    'major_graphic_design': ('arts', {'A': 0.7, 'E': 0.1, 'R': 0.2}, {'art': 0.7, 'cs': 0.15, 'literature': 0.15}, 'higher'),
    'major_music': ('arts', {'A': 0.85, 'E': 0.05, 'S': 0.1}, {'art': 0.7, 'literature': 0.3}, 'higher'),
    'major_theatre': ('arts', {'A': 0.7, 'E': 0.2, 'S': 0.1}, {'art': 0.5, 'literature': 0.5}, 'higher'),
    # ---- business
    'major_business_admin': ('business', {'C': 0.3, 'E': 0.5, 'S': 0.2}, {}, 'higher'),
    'major_management': ('business', {'C': 0.2, 'E': 0.6, 'S': 0.2}, {}, 'higher'),
    'major_marketing': ('business', {'A': 0.3, 'E': 0.5, 'S': 0.2}, {}, 'higher'),
    # ---- cs
    'major_cs': ('cs', {'C': 0.2, 'I': 0.5, 'R': 0.3}, {}, 'higher'),
    'major_data_science': ('cs', {'A': 0.1, 'C': 0.3, 'I': 0.6}, {'cs': 0.3, 'economics': 0.2, 'math': 0.5}, 'higher'),
    'major_info_security': ('cs', {'C': 0.4, 'I': 0.5, 'R': 0.1}, {}, 'higher'),
    'major_software_eng': ('cs', {'C': 0.3, 'I': 0.5, 'R': 0.2}, {}, 'higher'),
    # ---- education
    'major_pedagogy': ('education', {'A': 0.2, 'C': 0.1, 'S': 0.7}, {}, 'higher'),
    'major_philology': ('education', {'A': 0.4, 'I': 0.25, 'S': 0.35}, {'english': 0.3, 'history': 0.2, 'literature': 0.5}, 'higher'),
    'major_primary_education': ('education', {'A': 0.15, 'C': 0.1, 'S': 0.75}, {}, 'higher'),
    # ---- engineering
    'major_civil_eng': ('engineering', {'C': 0.3, 'I': 0.2, 'R': 0.5}, {}, 'higher'),
    'major_electrical_eng': ('engineering', {'C': 0.1, 'I': 0.5, 'R': 0.4}, {}, 'higher'),
    'major_mechanical_eng': ('engineering', {'C': 0.1, 'I': 0.4, 'R': 0.5}, {}, 'higher'),
    'major_mechatronics': ('engineering', {'A': 0.1, 'I': 0.5, 'R': 0.4}, {'cs': 0.4, 'math': 0.2, 'physics': 0.4}, 'higher'),
    # ---- finance
    'major_accounting': ('finance', {'C': 0.7, 'E': 0.1, 'I': 0.2}, {}, 'higher'),
    'major_banking': ('finance', {'C': 0.4, 'E': 0.4, 'I': 0.2}, {}, 'higher'),
    'major_economics': ('finance', {'C': 0.3, 'E': 0.2, 'I': 0.5}, {'economics': 0.4, 'geography': 0.1, 'math': 0.5}, 'higher'),
    'major_finance': ('finance', {'C': 0.5, 'E': 0.2, 'I': 0.3}, {}, 'higher'),
    # ---- hospitality
    'major_culinary': ('hospitality', {'A': 0.4, 'E': 0.2, 'R': 0.4}, {'biology': 0.3, 'chemistry': 0.4, 'economics': 0.3}, 'either'),
    'major_hotel_management': ('hospitality', {'C': 0.2, 'E': 0.45, 'S': 0.35}, {'economics': 0.3, 'english': 0.5, 'geography': 0.2}, 'higher'),
    'major_tourism': ('hospitality', {'C': 0.2, 'E': 0.4, 'S': 0.4}, {'economics': 0.2, 'english': 0.5, 'geography': 0.3}, 'higher'),
    # ---- law
    'major_international_relations': ('law', {'E': 0.4, 'I': 0.3, 'S': 0.3}, {'english': 0.4, 'history': 0.35, 'literature': 0.25}, 'higher'),
    'major_law': ('law', {'C': 0.35, 'E': 0.4, 'S': 0.25}, {'economics': 0.3, 'history': 0.4, 'literature': 0.3}, 'higher'),
    'major_political_science': ('law', {'E': 0.35, 'I': 0.4, 'S': 0.25}, {'economics': 0.25, 'history': 0.45, 'literature': 0.3}, 'higher'),
    # ---- logistics
    'major_construction_management': ('logistics', {'C': 0.3, 'E': 0.35, 'R': 0.35}, {'geography': 0.2, 'math': 0.4, 'physics': 0.4}, 'higher'),
    'major_logistics': ('logistics', {'C': 0.45, 'E': 0.25, 'R': 0.3}, {'geography': 0.4, 'math': 0.4, 'physics': 0.2}, 'higher'),
    'major_transport': ('logistics', {'C': 0.4, 'E': 0.2, 'R': 0.4}, {'geography': 0.3, 'math': 0.4, 'physics': 0.3}, 'higher'),
    # ---- media
    'major_journalism': ('media', {'A': 0.4, 'E': 0.35, 'S': 0.25}, {'english': 0.3, 'history': 0.2, 'literature': 0.5}, 'higher'),
    'major_media_communications': ('media', {'A': 0.4, 'E': 0.4, 'S': 0.2}, {'art': 0.2, 'english': 0.4, 'literature': 0.4}, 'higher'),
    'major_pr': ('media', {'A': 0.3, 'E': 0.5, 'S': 0.2}, {'economics': 0.2, 'english': 0.4, 'literature': 0.4}, 'higher'),
    # ---- medicine
    'major_dentistry': ('medicine', {'I': 0.25, 'R': 0.4, 'S': 0.35}, {'biology': 0.5, 'chemistry': 0.4, 'physics': 0.1}, 'higher'),
    'major_medicine': ('medicine', {'I': 0.4, 'R': 0.2, 'S': 0.4}, {'biology': 0.5, 'chemistry': 0.4, 'physics': 0.1}, 'higher'),
    'major_nursing': ('medicine', {'C': 0.2, 'R': 0.2, 'S': 0.6}, {}, 'either'),
    'major_pharmacy': ('medicine', {'C': 0.4, 'I': 0.4, 'S': 0.2}, {'biology': 0.4, 'chemistry': 0.5, 'math': 0.1}, 'higher'),
    # ---- psychology
    'major_psychology': ('psychology', {'A': 0.1, 'I': 0.3, 'S': 0.6}, {'biology': 0.4, 'history': 0.3, 'literature': 0.3}, 'higher'),
    'major_social_work': ('psychology', {'C': 0.15, 'I': 0.1, 'S': 0.75}, {}, 'higher'),
    'major_special_education': ('psychology', {'A': 0.1, 'I': 0.2, 'S': 0.7}, {'biology': 0.35, 'history': 0.3, 'literature': 0.35}, 'higher'),
    # ---- science
    'major_biology': ('science', {'I': 0.7, 'R': 0.2, 'S': 0.1}, {'biology': 0.6, 'chemistry': 0.3, 'math': 0.1}, 'higher'),
    'major_biotechnology': ('science', {'C': 0.15, 'I': 0.65, 'R': 0.2}, {'biology': 0.5, 'chemistry': 0.4, 'math': 0.1}, 'higher'),
    'major_chemistry': ('science', {'C': 0.1, 'I': 0.7, 'R': 0.2}, {'chemistry': 0.6, 'math': 0.2, 'physics': 0.2}, 'higher'),
    'major_physics': ('science', {'A': 0.1, 'I': 0.8, 'R': 0.1}, {'math': 0.5, 'physics': 0.5}, 'higher'),
    # ---- sport
    'major_physical_education': ('sport', {'E': 0.15, 'R': 0.35, 'S': 0.5}, {'biology': 0.6, 'english': 0.2, 'geography': 0.2}, 'higher'),
    'major_physiotherapy': ('sport', {'I': 0.25, 'R': 0.3, 'S': 0.45}, {'biology': 0.7, 'english': 0.2, 'geography': 0.1}, 'higher'),
    'major_sports_science': ('sport', {'I': 0.4, 'R': 0.35, 'S': 0.25}, {'biology': 0.7, 'english': 0.2, 'geography': 0.1}, 'higher'),
}


# ------------------------------------------------------ work-value associations
# What each family tends to OFFER, on the ten work-value dimensions. Weights sum
# to 1.0 and are deliberately coarse -- they exist to separate careers that
# RIASEC scores identically. An entrepreneur and an operations manager are both
# Enterprising; independence against stability is what tells them apart, and
# that is the whole reason this signal is collected at all.
#
# Tunable in one place on purpose. These are judgements, not measurements, and
# the first real student data should be allowed to move them.
FAMILY_VALUES = {
    'cs':          {'learning': .35, 'independence': .25, 'creativity': .20, 'income': .20},
    'engineering': {'learning': .30, 'stability': .25, 'income': .25, 'teamwork': .20},
    'business':    {'income': .30, 'leadership': .30, 'independence': .25, 'creativity': .15},
    'finance':     {'income': .40, 'stability': .35, 'learning': .25},
    'medicine':    {'helping': .40, 'meaning': .25, 'learning': .20, 'stability': .15},
    'science':     {'learning': .45, 'independence': .30, 'meaning': .25},
    'architecture':{'creativity': .45, 'independence': .25, 'meaning': .15, 'income': .15},
    'psychology':  {'helping': .45, 'meaning': .30, 'learning': .25},
    'law':         {'income': .25, 'meaning': .25, 'leadership': .25, 'stability': .25},
    'education':   {'helping': .35, 'meaning': .30, 'balance': .20, 'stability': .15},
    'media':       {'creativity': .40, 'independence': .25, 'meaning': .20, 'teamwork': .15},
    'agriculture': {'meaning': .30, 'independence': .25, 'stability': .25, 'balance': .20},
    'logistics':   {'stability': .35, 'income': .25, 'teamwork': .20, 'balance': .20},
    'arts':        {'creativity': .50, 'independence': .30, 'meaning': .20},
    'hospitality': {'teamwork': .35, 'helping': .25, 'income': .20, 'creativity': .20},
    'sport':       {'teamwork': .30, 'balance': .25, 'helping': .25, 'meaning': .20},
}

# EVERY entry carries its own profile. Inheritance was the default while three
# families existed; across sixteen it would have meant siblings moving in
# lockstep, and values would have discriminated between families only. Writing
# them now costs a line each; retrofitting 150 entries later would not.
ENTRY_VALUES = {
    # ---- agriculture
    'agronomist': {'balance': 0.2, 'independence': 0.25, 'meaning': 0.3, 'stability': 0.25},
    'ecologist': {'balance': 0.1, 'independence': 0.25, 'learning': 0.2, 'meaning': 0.45},
    'farm_manager': {'balance': 0.2, 'income': 0.25, 'independence': 0.35, 'stability': 0.2},
    'food_technologist': {'income': 0.2, 'learning': 0.3, 'meaning': 0.2, 'stability': 0.3},
    'veterinarian': {'helping': 0.35, 'independence': 0.2, 'learning': 0.2, 'meaning': 0.25},
    # ---- architecture
    'architect': {'creativity': 0.45, 'income': 0.15, 'independence': 0.25, 'meaning': 0.15},
    'industrial_designer': {'creativity': 0.45, 'income': 0.2, 'independence': 0.25, 'learning': 0.1},
    'interior_designer': {'creativity': 0.5, 'income': 0.2, 'independence': 0.3},
    'landscape_designer': {'balance': 0.15, 'creativity': 0.45, 'independence': 0.25, 'meaning': 0.15},
    'urban_planner': {'creativity': 0.25, 'leadership': 0.2, 'meaning': 0.35, 'stability': 0.2},
    # ---- arts
    'actor': {'creativity': 0.5, 'independence': 0.2, 'meaning': 0.15, 'teamwork': 0.15},
    'animator': {'creativity': 0.5, 'income': 0.1, 'independence': 0.2, 'learning': 0.2},
    'artist': {'creativity': 0.55, 'independence': 0.3, 'meaning': 0.15},
    'fashion_designer': {'creativity': 0.5, 'income': 0.15, 'independence': 0.25, 'leadership': 0.1},
    'graphic_designer': {'creativity': 0.5, 'income': 0.15, 'independence': 0.25, 'teamwork': 0.1},
    'musician': {'creativity': 0.55, 'independence': 0.3, 'meaning': 0.15},
    # ---- business
    'business_analyst': {'income': 0.25, 'learning': 0.3, 'stability': 0.3, 'teamwork': 0.15},
    'entrepreneur': {'income': 0.3, 'independence': 0.35, 'leadership': 0.25, 'stability': 0.1},
    'marketing_manager': {'creativity': 0.35, 'income': 0.2, 'leadership': 0.25, 'teamwork': 0.2},
    'operations_manager': {'income': 0.2, 'leadership': 0.3, 'stability': 0.3, 'teamwork': 0.2},
    'product_manager': {'creativity': 0.2, 'leadership': 0.3, 'learning': 0.25, 'teamwork': 0.25},
    'sales_manager': {'income': 0.4, 'independence': 0.15, 'leadership': 0.2, 'teamwork': 0.25},
    # ---- cs
    'ai_engineer': {'creativity': 0.1, 'income': 0.2, 'independence': 0.25, 'learning': 0.45},
    'cybersecurity': {'income': 0.25, 'learning': 0.3, 'meaning': 0.15, 'stability': 0.3},
    'data_scientist': {'income': 0.25, 'independence': 0.3, 'learning': 0.45},
    'frontend_developer': {'creativity': 0.4, 'income': 0.15, 'independence': 0.2, 'learning': 0.25},
    'mobile_developer': {'creativity': 0.35, 'income': 0.15, 'independence': 0.2, 'learning': 0.3},
    'software_engineer': {'creativity': 0.2, 'income': 0.2, 'independence': 0.25, 'learning': 0.35},
    'systems_analyst': {'income': 0.2, 'learning': 0.3, 'stability': 0.25, 'teamwork': 0.25},
    # ---- education
    'methodologist': {'balance': 0.15, 'learning': 0.25, 'meaning': 0.3, 'stability': 0.3},
    'primary_teacher': {'balance': 0.2, 'helping': 0.4, 'meaning': 0.3, 'stability': 0.1},
    'school_principal': {'helping': 0.2, 'leadership': 0.35, 'meaning': 0.25, 'stability': 0.2},
    'teacher': {'balance': 0.2, 'helping': 0.35, 'meaning': 0.3, 'stability': 0.15},
    'tutor': {'balance': 0.2, 'helping': 0.3, 'income': 0.2, 'independence': 0.3},
    'university_lecturer': {'helping': 0.15, 'independence': 0.2, 'learning': 0.4, 'meaning': 0.25},
    # ---- engineering
    'civil_engineer': {'income': 0.25, 'meaning': 0.2, 'stability': 0.3, 'teamwork': 0.25},
    'electrical_engineer': {'income': 0.25, 'learning': 0.35, 'stability': 0.25, 'teamwork': 0.15},
    'industrial_engineer': {'balance': 0.2, 'income': 0.25, 'stability': 0.3, 'teamwork': 0.25},
    'mechanical_engineer': {'income': 0.25, 'learning': 0.3, 'stability': 0.25, 'teamwork': 0.2},
    'robotics_engineer': {'creativity': 0.25, 'income': 0.15, 'independence': 0.2, 'learning': 0.4},
    'technician': {'balance': 0.2, 'income': 0.25, 'stability': 0.35, 'teamwork': 0.2},
    # ---- finance
    'accountant': {'balance': 0.2, 'income': 0.25, 'stability': 0.4, 'teamwork': 0.15},
    'auditor': {'income': 0.25, 'independence': 0.2, 'meaning': 0.2, 'stability': 0.35},
    'banker': {'income': 0.35, 'leadership': 0.15, 'stability': 0.3, 'teamwork': 0.2},
    'financial_analyst': {'income': 0.35, 'independence': 0.15, 'learning': 0.3, 'stability': 0.2},
    'investment_analyst': {'income': 0.45, 'independence': 0.2, 'leadership': 0.1, 'learning': 0.25},
    'tax_specialist': {'balance': 0.2, 'income': 0.25, 'meaning': 0.15, 'stability': 0.4},
    # ---- hospitality
    'chef': {'creativity': 0.4, 'income': 0.2, 'independence': 0.15, 'teamwork': 0.25},
    'event_manager': {'creativity': 0.3, 'income': 0.15, 'leadership': 0.25, 'teamwork': 0.3},
    'hotel_manager': {'helping': 0.2, 'income': 0.2, 'leadership': 0.3, 'teamwork': 0.3},
    'restaurant_manager': {'income': 0.3, 'leadership': 0.3, 'stability': 0.15, 'teamwork': 0.25},
    'tour_guide': {'balance': 0.2, 'helping': 0.25, 'independence': 0.25, 'teamwork': 0.3},
    'travel_agent': {'balance': 0.2, 'helping': 0.25, 'income': 0.25, 'teamwork': 0.3},
    # ---- law
    'diplomat': {'income': 0.2, 'leadership': 0.25, 'learning': 0.25, 'meaning': 0.3},
    'judge': {'income': 0.15, 'leadership': 0.2, 'meaning': 0.35, 'stability': 0.3},
    'lawyer': {'income': 0.3, 'independence': 0.2, 'leadership': 0.25, 'meaning': 0.25},
    'legal_advisor': {'balance': 0.2, 'income': 0.3, 'independence': 0.15, 'stability': 0.35},
    'notary': {'balance': 0.2, 'income': 0.25, 'independence': 0.15, 'stability': 0.4},
    'prosecutor': {'income': 0.15, 'leadership': 0.25, 'meaning': 0.35, 'stability': 0.25},
    # ---- logistics
    'construction_manager': {'income': 0.3, 'leadership': 0.3, 'stability': 0.2, 'teamwork': 0.2},
    'electrician': {'balance': 0.15, 'income': 0.3, 'independence': 0.25, 'stability': 0.3},
    'logistician': {'balance': 0.2, 'income': 0.25, 'stability': 0.35, 'teamwork': 0.2},
    'supply_chain_manager': {'income': 0.25, 'leadership': 0.3, 'stability': 0.3, 'teamwork': 0.15},
    'surveyor': {'balance': 0.2, 'income': 0.2, 'independence': 0.25, 'stability': 0.35},
    'warehouse_manager': {'balance': 0.15, 'income': 0.25, 'stability': 0.4, 'teamwork': 0.2},
    # ---- media
    'copywriter': {'balance': 0.1, 'creativity': 0.45, 'income': 0.15, 'independence': 0.3},
    'editor': {'creativity': 0.35, 'independence': 0.25, 'meaning': 0.2, 'stability': 0.2},
    'journalist': {'creativity': 0.3, 'independence': 0.25, 'learning': 0.15, 'meaning': 0.3},
    'photographer': {'balance': 0.1, 'creativity': 0.5, 'income': 0.1, 'independence': 0.3},
    'smm_specialist': {'creativity': 0.4, 'income': 0.2, 'independence': 0.25, 'teamwork': 0.15},
    'tv_producer': {'creativity': 0.35, 'income': 0.15, 'leadership': 0.3, 'teamwork': 0.2},
    # ---- medicine
    'dentist': {'helping': 0.3, 'income': 0.3, 'independence': 0.2, 'stability': 0.2},
    'doctor': {'helping': 0.4, 'learning': 0.2, 'meaning': 0.25, 'stability': 0.15},
    'lab_technician': {'balance': 0.2, 'learning': 0.25, 'meaning': 0.2, 'stability': 0.35},
    'nurse': {'helping': 0.45, 'meaning': 0.25, 'stability': 0.1, 'teamwork': 0.2},
    'paramedic': {'helping': 0.4, 'meaning': 0.3, 'stability': 0.1, 'teamwork': 0.2},
    'pharmacist': {'balance': 0.15, 'helping': 0.3, 'learning': 0.2, 'stability': 0.35},
    'surgeon': {'helping': 0.35, 'income': 0.15, 'learning': 0.25, 'meaning': 0.25},
    # ---- psychology
    'hr_specialist': {'helping': 0.3, 'leadership': 0.2, 'stability': 0.2, 'teamwork': 0.3},
    'psychologist': {'helping': 0.45, 'learning': 0.25, 'meaning': 0.3},
    'school_counselor': {'balance': 0.15, 'helping': 0.45, 'meaning': 0.3, 'teamwork': 0.1},
    'social_worker': {'helping': 0.5, 'meaning': 0.35, 'teamwork': 0.15},
    'speech_therapist': {'balance': 0.15, 'helping': 0.45, 'meaning': 0.3, 'stability': 0.1},
    'therapist': {'balance': 0.1, 'helping': 0.45, 'independence': 0.15, 'meaning': 0.3},
    # ---- science
    'biologist': {'independence': 0.3, 'learning': 0.4, 'meaning': 0.3},
    'chemist': {'income': 0.1, 'independence': 0.3, 'learning': 0.4, 'meaning': 0.2},
    'environmental_scientist': {'balance': 0.1, 'independence': 0.2, 'learning': 0.3, 'meaning': 0.4},
    'geneticist': {'independence': 0.25, 'learning': 0.45, 'meaning': 0.3},
    'physicist': {'independence': 0.3, 'learning': 0.5, 'meaning': 0.2},
    'researcher': {'independence': 0.3, 'learning': 0.45, 'meaning': 0.25},
    # ---- sport
    'athlete': {'income': 0.25, 'independence': 0.3, 'meaning': 0.25, 'teamwork': 0.2},
    'coach': {'balance': 0.2, 'helping': 0.3, 'meaning': 0.2, 'teamwork': 0.3},
    'fitness_trainer': {'balance': 0.2, 'helping': 0.3, 'income': 0.2, 'independence': 0.3},
    'pe_teacher': {'balance': 0.25, 'helping': 0.35, 'meaning': 0.25, 'stability': 0.15},
    'physiotherapist': {'balance': 0.15, 'helping': 0.4, 'meaning': 0.25, 'stability': 0.2},
    'sports_manager': {'balance': 0.15, 'income': 0.3, 'leadership': 0.3, 'teamwork': 0.25},
    # ---- agriculture
    'major_agronomy': {'balance': 0.2, 'independence': 0.25, 'meaning': 0.3, 'stability': 0.25},
    'major_ecology': {'balance': 0.1, 'independence': 0.25, 'learning': 0.2, 'meaning': 0.45},
    'major_food_technology': {'income': 0.2, 'learning': 0.3, 'meaning': 0.2, 'stability': 0.3},
    'major_veterinary': {'helping': 0.35, 'independence': 0.2, 'learning': 0.2, 'meaning': 0.25},
    # ---- architecture
    'major_architecture': {'creativity': 0.45, 'income': 0.15, 'independence': 0.25, 'meaning': 0.15},
    'major_interior_design': {'creativity': 0.5, 'income': 0.2, 'independence': 0.3},
    'major_urban_planning': {'creativity': 0.25, 'leadership': 0.2, 'meaning': 0.35, 'stability': 0.2},
    # ---- arts
    'major_fine_arts': {'creativity': 0.55, 'independence': 0.3, 'meaning': 0.15},
    'major_graphic_design': {'creativity': 0.5, 'income': 0.15, 'independence': 0.25, 'teamwork': 0.1},
    'major_music': {'creativity': 0.55, 'independence': 0.3, 'meaning': 0.15},
    'major_theatre': {'creativity': 0.5, 'independence': 0.2, 'meaning': 0.15, 'teamwork': 0.15},
    # ---- business
    'major_business_admin': {'income': 0.3, 'leadership': 0.3, 'stability': 0.2, 'teamwork': 0.2},
    'major_management': {'income': 0.25, 'independence': 0.2, 'leadership': 0.35, 'teamwork': 0.2},
    'major_marketing': {'creativity': 0.35, 'income': 0.2, 'leadership': 0.25, 'teamwork': 0.2},
    # ---- cs
    'major_cs': {'creativity': 0.15, 'income': 0.2, 'independence': 0.25, 'learning': 0.4},
    'major_data_science': {'income': 0.25, 'independence': 0.3, 'learning': 0.45},
    'major_info_security': {'income': 0.25, 'learning': 0.3, 'meaning': 0.15, 'stability': 0.3},
    'major_software_eng': {'creativity': 0.15, 'income': 0.25, 'independence': 0.25, 'learning': 0.35},
    # ---- education
    'major_pedagogy': {'balance': 0.2, 'helping': 0.35, 'meaning': 0.3, 'stability': 0.15},
    'major_philology': {'balance': 0.15, 'creativity': 0.3, 'learning': 0.35, 'meaning': 0.2},
    'major_primary_education': {'balance': 0.2, 'helping': 0.4, 'meaning': 0.3, 'stability': 0.1},
    # ---- engineering
    'major_civil_eng': {'income': 0.25, 'meaning': 0.2, 'stability': 0.3, 'teamwork': 0.25},
    'major_electrical_eng': {'income': 0.25, 'learning': 0.35, 'stability': 0.25, 'teamwork': 0.15},
    'major_mechanical_eng': {'income': 0.25, 'learning': 0.3, 'stability': 0.25, 'teamwork': 0.2},
    'major_mechatronics': {'creativity': 0.25, 'income': 0.15, 'independence': 0.2, 'learning': 0.4},
    # ---- finance
    'major_accounting': {'balance': 0.2, 'income': 0.3, 'stability': 0.4, 'teamwork': 0.1},
    'major_banking': {'income': 0.35, 'leadership': 0.1, 'stability': 0.35, 'teamwork': 0.2},
    'major_economics': {'income': 0.3, 'independence': 0.15, 'learning': 0.35, 'meaning': 0.2},
    'major_finance': {'income': 0.4, 'independence': 0.1, 'learning': 0.2, 'stability': 0.3},
    # ---- hospitality
    'major_culinary': {'creativity': 0.4, 'income': 0.2, 'independence': 0.15, 'teamwork': 0.25},
    'major_hotel_management': {'helping': 0.2, 'income': 0.2, 'leadership': 0.3, 'teamwork': 0.3},
    'major_tourism': {'balance': 0.2, 'helping': 0.25, 'income': 0.25, 'teamwork': 0.3},
    # ---- law
    'major_international_relations': {'income': 0.2, 'leadership': 0.2, 'learning': 0.3, 'meaning': 0.3},
    'major_law': {'income': 0.3, 'leadership': 0.25, 'meaning': 0.3, 'stability': 0.15},
    'major_political_science': {'independence': 0.15, 'leadership': 0.2, 'learning': 0.3, 'meaning': 0.35},
    # ---- logistics
    'major_construction_management': {'income': 0.3, 'leadership': 0.3, 'stability': 0.2, 'teamwork': 0.2},
    'major_logistics': {'balance': 0.2, 'income': 0.25, 'stability': 0.35, 'teamwork': 0.2},
    'major_transport': {'balance': 0.15, 'income': 0.3, 'stability': 0.35, 'teamwork': 0.2},
    # ---- media
    'major_journalism': {'creativity': 0.3, 'independence': 0.25, 'learning': 0.15, 'meaning': 0.3},
    'major_media_communications': {'creativity': 0.35, 'income': 0.2, 'independence': 0.2, 'teamwork': 0.25},
    'major_pr': {'creativity': 0.3, 'income': 0.2, 'leadership': 0.3, 'teamwork': 0.2},
    # ---- medicine
    'major_dentistry': {'helping': 0.3, 'income': 0.3, 'independence': 0.2, 'stability': 0.2},
    'major_medicine': {'helping': 0.4, 'learning': 0.2, 'meaning': 0.25, 'stability': 0.15},
    'major_nursing': {'helping': 0.45, 'meaning': 0.25, 'stability': 0.1, 'teamwork': 0.2},
    'major_pharmacy': {'balance': 0.15, 'helping': 0.3, 'learning': 0.2, 'stability': 0.35},
    # ---- psychology
    'major_psychology': {'helping': 0.45, 'learning': 0.25, 'meaning': 0.3},
    'major_social_work': {'helping': 0.5, 'meaning': 0.35, 'teamwork': 0.15},
    'major_special_education': {'balance': 0.2, 'helping': 0.5, 'meaning': 0.3},
    # ---- science
    'major_biology': {'independence': 0.3, 'learning': 0.4, 'meaning': 0.3},
    'major_biotechnology': {'income': 0.15, 'independence': 0.15, 'learning': 0.4, 'meaning': 0.3},
    'major_chemistry': {'income': 0.1, 'independence': 0.3, 'learning': 0.4, 'meaning': 0.2},
    'major_physics': {'independence': 0.3, 'learning': 0.5, 'meaning': 0.2},
    # ---- sport
    'major_physical_education': {'balance': 0.25, 'helping': 0.35, 'meaning': 0.25, 'stability': 0.15},
    'major_physiotherapy': {'balance': 0.15, 'helping': 0.4, 'meaning': 0.25, 'stability': 0.2},
    'major_sports_science': {'balance': 0.15, 'helping': 0.25, 'learning': 0.35, 'meaning': 0.25},
}


def values_of(key):
    u"""Work-value profile for a career or major, inherited from its family."""
    if key in ENTRY_VALUES:
        return ENTRY_VALUES[key]
    fam = (CAREERS.get(key) or MAJORS.get(key))[0]
    return FAMILY_VALUES[fam]


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
