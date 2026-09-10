# -*- coding: utf-8 -*-
u"""English text for the Work Importance bank. TEXT ONLY: the value each card
belongs to, its letter and its position live in wil_content.py and are paired
BY POSITION.

This is the published O*NET Work Importance Locator wording with the repeated
stem lifted out: the original prints "On my ideal job it is important that..."
on all twenty cards, which is right on paper and wrong on a phone. Nothing else
is reworded, because the point of using a public domain instrument is being able
to say the items are the instrument's.
"""

LEVELS = [
    u'Not important',
    u'Slightly important',
    u'Middle',
    u'Quite important',
    u'Important',
]

NAMES = {
    'achievement':   u'Achievement',
    'independence':  u'Independence',
    'recognition':   u'Recognition',
    'relationships': u'Relationships',
    'support':       u'Support',
    'conditions':    u'Working conditions',
}

LEADS = {
    'achievement':   u'Work should leave you with a sense of having achieved something.',
    'independence':  u'You want to make your own decisions.',
    'recognition':   u'Your work should be seen and valued.',
    'relationships': u'People, and a clear conscience, matter to you.',
    'support':       u'You want managers who stand behind you.',
    'conditions':    u'Conditions and security matter to you.',
}

STEM = u'On my ideal job it is important that:'

CARDS = [
    u'I could make use of my abilities',
    u'I would be treated fairly by the company',
    u'I could be busy all the time',
    u'the job would give me a chance to advance',
    u'I could give directions and instructions to others',
    u'the work could give me a feeling of accomplishment',
    u'my pay would compare well with that of other workers',
    u'my co workers would be easy to get along with',
    u'I could try out my own ideas',
    u'I could work alone',
    u'I would never be pressured to do things that go against my sense of right and wrong',
    u'I could receive recognition for the work I do',
    u'I could make decisions on my own',
    u'the job would provide steady employment',
    u'I could do things for other people',
    u'my supervisors would back up their workers with management',
    u'my supervisors would train their workers well',
    u'I could do something different every day',
    u'the job would have good working conditions',
    u'I could plan my work with little supervision',
]

TITLE = u'What matters most'
BLURB = (u'Twenty things a job can offer. Place each card at the importance '
         u'level that feels right to you; any level can contain any number.')
