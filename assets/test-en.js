/* English rendering of the instrument and the test page.
 *
 * Same contract as test-ru.js: the fifty items are in the SAME order as ITEMS in
 * test.html and carry no keying of their own. The trait letter and the reverse
 * flag stay in test.html, so a translation cannot change what an item measures
 * or which way it scores, and a list of the wrong length is refused outright
 * rather than applied half way.
 *
 * NOTE ON VALIDITY: a translation of the Uzbek instrument, not a separately
 * validated English one. Fine for self-reflection, which is what TestMind
 * offers; results in different languages are not strictly comparable.
 *
 * Written for Uzbek students who read English comfortably: plain wording, no
 * idioms that assume growing up in an English-speaking country.
 */
var TEST_EN = {

  items: [
    'I make new friends easily.',
    'I have a very vivid imagination.',
    'I trust people easily.',
    'I worry a lot, even about small things.',
    'I do the tasks I am given properly.',
    'I get annoyed over little things.',
    'I like being in busy, crowded places.',
    'Art and creativity matter a lot in my life.',
    'I sometimes use other people for my own benefit.',
    'I keep my room and my home clean and tidy.',
    'My mood often drops and I feel sad.',
    'I like helping other people.',
    'I always keep my word and my promises.',
    'I prefer variety to doing the same thing every day.',
    'I enjoy deep books that make me think.',
    'I make a careful plan before starting anything.',
    'I do not open up to people quickly; I keep my inner world to myself.',
    'I am not very interested in what other people are feeling.',
    'I tell the truth in any situation.',
    'My life feels the same every day and a little dull.',
    'I argue against other people to get my own view across.',
    'I try to achieve more than is expected of me.',
    'I am often dissatisfied with myself.',
    'I think the world is made of different points of view, not only of "facts" and "mistakes".',
    'I stay calm even in an accident or a difficult situation.',
    'I wait for other people to act rather than making the first move myself.',
    'Reading or listening to poetry does not give me much pleasure.',
    'I leave my things scattered around and my room untidy.',
    'I rarely get nervous.',
    'I get around the rules and the order that society has set.',
    'I take on the leading role in a group or a team.',
    'I find abstract, theoretical and philosophical ideas hard to understand.',
    'I rely on tried and tested methods rather than unfamiliar experiences.',
    'I genuinely feel for people who are in a hard situation.',
    'I act on chance instead of thinking everything through first.',
    'I very rarely get upset or go around in a bad mood.',
    'I like new adventures with plenty of risk in them.',
    'I really enjoy life and every day of it.',
    'I do not feel awkward or shy even in uncomfortable situations.',
    'I find very sensitive and emotional people hard to understand.',
    'I suspect there is always a hidden motive behind what people do.',
    'I cannot keep the word and the promises I have given.',
    'I do not enjoy crowded, noisy events.',
    'I think about my problems for a long time and cannot get away from them.',
    'I do not throw myself into things with much energy or enthusiasm.',
    'When I get angry I say harsh and hurtful things to other people.',
    'Getting past obstacles and difficulties in life is not hard for me.',
    'I think the decisions of elders and leaders should be respected without question.',
    'I prefer working together in harmony to competing with others.',
    'I do things in a rush.'
  ],

  labels: ['Disagree', 'Slightly disagree', 'Neutral', 'Slightly agree', 'Agree'],

  traits: {ES: 'Emotional stability', E: 'Sociability', O: 'Openness to new things',
           A: 'Agreeableness', C: 'Responsibility'},

  poles: {
    ES: ['Sensitive', 'Calm'],
    E:  ['Reflective', 'Outgoing'],
    O:  ['Practical', 'Explorer'],
    A:  ['Independent', 'Cooperative'],
    C:  ['Flexible', 'Planner']
  },

  texts: {
    ES: {past: 'You may feel emotions more strongly than others do. That is not a flaw: people like this are often perceptive and careful. What matters is choosing a working environment that suits you.',
         orta: 'Like most people, you worry in some situations and stay calm in others. That is normal.',
         yuqori: 'You can stay calm even under stress. Fields that require working under pressure may suit you.'},
    E:  {past: 'You prefer to work independently and in depth. Analysis, programming, research and other fields that reward concentration may be your strength.',
         orta: 'You can work both in a team and on your own. That flexibility is useful in many professions.',
         yuqori: 'Working with people gives you energy. Look at team projects, working with clients, and roles that involve leading.'},
    O:  {past: 'You are comfortable working with clear rules and proven methods. Precision and consistency are valuable qualities in many fields.',
         orta: 'You are open both to new ideas and to proven methods, and you choose depending on the situation.',
         yuqori: 'New ideas and unusual solutions attract you. In creative and research fields that is a real advantage.'},
    A:  {past: 'You say what you think openly and do not avoid competition. Negotiation, critical analysis and competitive environments may suit you.',
         orta: 'You can both support others and stand your ground. That is a useful combination.',
         yuqori: 'Helping people and working together come naturally to you. In teaching, medicine and service work that is a real strength.'},
    C:  {past: 'You prefer a free and flexible way of working. Places that look at results rather than a strict timetable will suit you better. Planning is a skill you can build.',
         orta: 'You pull yourself together for the things that matter and take the rest more freely.',
         yuqori: 'You work in a planned, disciplined way and finish what you start. That is the single biggest factor in success in almost any field.'}
  },

  disclaimer: 'This result is guidance, not a verdict. When choosing a profession or a direction, ' +
              'weigh it together with your own interests and opportunities.',

  steps: [
    {title: 'Take the test',
     text: 'Be yourself and answer honestly. First about you, then about your interests — 65–85 questions, about 12 minutes.'},
    {title: 'See your result',
     text: 'One of the ten characters will be yours — with your strengths, right there on screen.'},
    {title: 'Get your guide',
     text: 'If you like, leave an email at the end and we will send a detailed guide to your character.'}
  ],

  ui: {
    title:       'Free personality test',
    back:        'Back',
    next:        'Next',
    seeResult:   'See the result',
    stepCount:   'Step %1 of %2',
    answerRest:  'Please answer the remaining questions.',
    topupNote:   'Two of your sides came out almost level. A few more questions will settle which of them is stronger.',
    guideLangNote: 'The guide is currently available in Uzbek only.',
    careerResH:  'Your interests',
    careerResSub:'This shows which activities you enjoy — not what you are able to do.',
    careerTop:   'Your strongest area for now is %1. Start looking there.',
    careerTie:   'But %1 is almost as strong — look at that one too.',
    careerCaveat:'Between 13 and 18 interests are still changing. This is a snapshot of today, not a choice for life.',
    careerH:     'Now — your interests',
    careerLede:  'The first part was about your personality. Now we ask which activities you enjoy. There are no right answers here — only whether you would like it or not.',
    careerTopup: 'A few areas came out almost level. A few more questions will settle which of them is stronger.',
    lifeH:       'The full picture',
    lifeSub:     'How your archetype shows up in everyday life.',
    resumeH1:    'Unfinished test',
    resumeP:     'An unfinished test was found on this device. Continue it?',
    resumeCount: '%1 of %2 questions answered.',
    cleared:     'Your answers have been deleted from this device.',
    fcLead:      'Which character should we show for you?',
    fcMale:      'Choose the male character',
    fcFemale:    'Choose the female character',
    fcAge:       'Your age',
    fcPickFirst: 'Please choose a character first.',
    fcAgeRange:  'Enter an age between 7 and 100.',
    shareSave:   'Save as an image',
    shareCopy:   'Copy the link',
    copied:      'Copied ✓',
    copyFailed:  'Could not copy',
    sharePrint:  'Print',
    shareAgain:  'Start again',
    shareMsg:    'I took the TestMind test. My result: "%1".',
    shareInvite: 'Try it yourself: https://%1/',
    capOr:       'or by email',
    capNote:     'You do not need an email to download — it is only for sending the guide to your inbox. ' +
                 'Email is optional and is never given to anyone else. ' +
                 'If you are under 18, talk it over with a parent or a teacher.',
    capSentH:    'Your request has been sent',
    capFailed:   'Could not send. Check your internet connection and try again.',
    sending:     'Sending…',
    tnAgain:     'You also took this test on <b>%1</b>.',
    tnSame:      '<p>All five of your qualities are almost the same. That is a result too — it means you know yourself well.</p>',
    tnArch:      '<p class="tnarch">Back then your character was "%1". A change of character is not a mistake; it is a sign of growth.</p>',
    grew:        'has grown',
    mid:         'Middle',
    strengthLbl: 'Your strength:',
    watchLbl:    'Worth watching:',
    figLbl:      'Someone known for the same quality',
    tieNote:     'Your result is also very close to <b>%1</b> — the difference between the two is very small. ' +
                 'Read both descriptions.',
    guideH:      'Your full guide is ready',
    // The eight-page guides exist in Uzbek only, so the offer says so plainly
    // rather than promising an English PDF that does not exist.
    guideLede:   'An 8-page guide for "%1": your strengths, your growth points, and directions ' +
                 'for school and for the future. The guide is written in Uzbek.',
    guidePdf:    'Download the guide (PDF)',
    guideTg:     'Get it on Telegram',
    emailAria:   'Your email address',
    send:        'Send',
    or:          'or'
  }
};
