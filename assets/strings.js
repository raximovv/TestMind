// TestMind — Russian and English text for everything that characters.js and
// site.js render at runtime.
//
// Uzbek is not in here: characters.js already holds it, and it stays the base
// that the other two languages override. A key missing from ru/en therefore
// falls back to Uzbek rather than to an empty page.
//
// Read at build time as well — build_archetypes.py evaluates this file to
// generate the ten obraz-*.html pages in each language, so the page and the
// browser can never disagree about what an archetype is called.
//
// The test itself (test.html) deliberately ignores this file. Translating a
// personality item would change what it measures, so the instrument stays
// Uzbek in all three versions of the site.

var STRINGS = {

ru: {
  ui: {
    strength: 'Сильная сторона: ',
    watch:    'Обратите внимание: ',
    fig:      'Из истории: ',
    figmale:  'Мужской образ:',
    figfemale:'Женский образ:',
    resume:   'Продолжить тест',
    vgYours:  'Ваш образ'
  },
  fam: {
    lead: 'Лидеры',
    crea: 'Творцы',
    care: 'Заботливые',
    base: 'Надёжные'
  },
  famnote: {
    lead: 'Те, за кем идут люди',
    crea: 'Те, кто находит новые идеи и решения',
    care: 'Те, кто замечает окружающих и поддерживает их',
    base: 'Ответственные люди, которые держат слово'
  },
  traits: {
    ES: 'Эмоциональная стабильность',
    E:  'Общительность',
    O:  'Открытость новому',
    A:  'Доброжелательность',
    C:  'Ответственность'
  },
  arch: {
    'ES|E': {
      name: 'Лидер',
      lines: ['Даже когда обстановка накаляется, вы не повышаете голос — поэтому вас слушают.',
              'Когда группа сбивается с пути, направление обычно показываете вы.'],
      strength: 'принимать верные решения под давлением.',
      watch: 'Ваше спокойствие иногда выглядит как безразличие. Не пропустите момент, когда близкие ждут от вас больше чувств.',
      figure: {who: 'Бахоуддин Накшбанд',
               why: 'Вёл людей за собой не принуждением, а собственным примером.'}
    },
    'E|C': {
      name: 'Организатор',
      lines: ['Вы быстро переходите от слов к делу — пока другие ещё обсуждают план, вы уже начали.',
              'И умеете расшевелить остальных.'],
      strength: 'превращать идею в реальность.',
      watch: 'Из-за быстрого старта вы иногда забываете спросить мнение других. Лучшая идея не всегда ваша.',
      figure: {who: 'Нодирабегим',
               why: 'Собрала вокруг себя литературную среду Коканда, строила медресе и мечети.'}
    },
    'ES|O': {
      name: 'Исследователь',
      lines: ['Увидев незнакомое, вы сначала пробуете, а уже потом высказываете мнение.',
              'Но в приключение идёте не вслепую, а хладнокровно.'],
      strength: 'спокойно исследовать незнакомый путь.',
      watch: 'Есть риск быстро увлечься новым и бросить начатое на середине. Попробуйте довести до конца хотя бы одно дело.',
      figure: {who: 'Абу Райхан Беруни',
               why: 'С одинаковым хладнокровием изучал и незнакомые земли, и незнакомые науки.'}
    },
    'E|O': {
      name: 'Творец',
      lines: ['Идеи у вас не заканчиваются, и вы любите рассказывать о них людям.',
              'Стоит вам начать объяснять идею — слушающий тоже загорается.'],
      strength: 'заражать людей новой идеей.',
      watch: 'Идей много, времени мало. Если начать всё сразу, можно не закончить ничего.',
      figure: {who: 'Зебуннисо Бегим',
               why: 'Из дома Бабуридов; под псевдонимом «Махфи» написала целый диван стихов.'}
    },
    'O|C': {
      name: 'Дальновидный',
      lines: ['Вы находите новое решение — и доводите его до конца.',
              'Идея не остаётся в тетради: вы превращаете её в график и шаги.'],
      strength: 'приводить идею в чёткую систему.',
      watch: 'Стремление сделать всё идеально вас замедляет. Иногда «достаточно хорошо» — тоже настоящий результат.',
      figure: {who: 'Мирзо Улугбек',
               why: 'Мечтал сосчитать звёзды, построил обсерваторию и внёс в каталог 1018 из них.'}
    },
    'ES|A': {
      name: 'Надёжный Друг',
      lines: ['Люди доверяют вам свои секреты, потому что рядом с вами чувствуют себя в безопасности.',
              'Если кто-то расстроен, вы обычно замечаете это первым.'],
      strength: 'успокаивать других.',
      watch: 'Помогая всем, легко не оставить времени себе. Научитесь говорить «нет».',
      figure: {who: 'Джахон Отин Увайси',
               why: 'Поэтесса и наставница; учила Нодирабегим искусству стиха.'}
    },
    'E|A': {
      name: 'Душа Команды',
      lines: ['В комнате, куда вы вошли, разговор начинается сам собой.',
              'Вы замечаете того, кто остался в стороне, и зовёте его к себе.'],
      strength: 'объединять людей.',
      watch: 'Стараясь быть хорошим для всех, вы можете так и не сказать своё мнение. Ваше мнение тоже важно.',
      figure: {who: 'Алишер Навои',
               why: 'Писал на родном языке и этим сблизил между собой целый народ.'}
    },
    'O|A': {
      name: 'Добрый Человек',
      lines: ['Новые идеи и забота о людях уживаются в вас вместе.',
              'Увидев проблему, вы прежде всего думаете о людях.'],
      strength: 'находить решение и полезное, и человечное.',
      watch: 'Вы принимаете чужие проблемы как свои. Решать всё в одиночку вовсе не обязательно.',
      figure: {who: 'Абдулла Авлони',
               why: 'Поставил литературу, театр, журналистику и просвещение на службу народу.'}
    },
    'ES|C': {
      name: 'Человек Плана',
      lines: ['Вы составляете план и не отвлекаетесь от него.',
              'Там, где остальные сдались, вы всё ещё работаете.'],
      strength: 'выдерживать длинную дистанцию.',
      watch: 'Когда план рушится, вам тяжело. Иногда сменить путь — не поражение.',
      figure: {who: 'Мухаммад аль-Хорезми',
               why: 'Разложил сложную задачу на точные шаги — слово «алгоритм» осталось от его имени.'}
    },
    'A|C': {
      name: 'Человек Слова',
      lines: ['Вы думаете, прежде чем пообещать, — потому что обещанное выполняете.',
              'Поэтому важное дело чаще всего поручают именно вам.'],
      strength: 'держать своё слово.',
      watch: 'Взваливая на себя всё, вы несёте лишний груз. Просить помощи — тоже сила.',
      figure: {who: 'Имам Бухари',
               why: 'Строго проверял каждое предание и включал в свод только достоверные.'}
    }
  },
  // Gendered historical figures. Only who/why translate; the dates and the
  // artwork path live once in characters.js. Keyed the same way as `arch`, so an
  // archetype without a pair simply has no entry here.
  figvar: {
    'ES|E': {
      male: {who: 'Бахоуддин Накшбанд',
             why: 'Вёл людей за собой не принуждением, а собственным примером.'},
      female: {who: 'Зульфия',
               why: 'Своей поэзией, стойкостью и спокойной общественной работой показала пример тихой силы и лидерства.'}
    },
    // Nodirabegim's two lines are the ones this archetype already shipped with,
    // copied rather than re-translated so the pair cannot drift from the page.
    'E|C': {
      male: {who: 'Амир Темур',
             why: 'Он создал сильное централизованное государство и опирался в управлении на порядок, чёткую систему и стратегию.'},
      female: {who: 'Нодирабегим',
               why: 'Собрала вокруг себя литературную среду Коканда, строила медресе и мечети.'}
    },
    'ES|O': {
      male: {who: 'Абу Райхан Беруни',
             why: 'С одинаковым хладнокровием изучал и незнакомые земли, и незнакомые науки.'},
      female: {who: 'Гульбадан Бегим',
               why: 'Интересуясь знаниями и путешествиями, она внимательно запечатлела жизнь своей эпохи в «Хумаюн-наме».'}
    },
    'E|O': {
      // years carries a qualifier here, so it is translated too; Zebunniso's is
      // bare numerals and inherits the Uzbek.
      male: {who: 'Камолиддин Бехзод', years: 'ок. 1455–1535/36',
             why: 'Он привнёс в миниатюрную живопись живые образы и новые композиции, оказав сильное влияние на целую художественную школу.'},
      female: {who: 'Зебуннисо Бегим',
               why: 'Из дома Бабуридов; под псевдонимом «Махфи» написала целый диван стихов.'}
    },
    'O|C': {
      male: {who: 'Мирзо Улугбек',
             why: 'Мечтал сосчитать звёзды, построил обсерваторию и внёс в каталог 1018 из них.'},
      female: {who: 'Гавхаршад Бегим', years: 'ок. 1378–1457',
               why: 'Она поддерживала архитектуру, образование и искусство, превращая масштабные культурные идеи в чёткие планы и крупные строительные проекты.'}
    },
    'ES|A': {
      male: {who: 'Абу Али ибн Сина',
             why: 'Как врач и учёный, он направлял свои знания на помощь людям, сохранение их здоровья и благополучия.'},
      female: {who: 'Джахон Отин Увайси',
               why: 'Поэтесса и наставница; учила Нодирабегим искусству стиха.'}
    },
    'E|A': {
      male: {who: 'Алишер Навои',
             why: 'Писал на родном языке и этим сблизил между собой целый народ.'},
      female: {who: 'Тамара Ханум',
               why: 'Через танец и песню она знакомила зрителей с культурой разных народов и объединяла людей на сцене.'}
    },
    'O|A': {
      male: {who: 'Абдулла Авлони',
             why: 'Поставил литературу, театр, журналистику и просвещение на службу народу.'},
      female: {who: 'Мукаррама Тургунбаева',
               why: 'Через искусство танца она несла красоту и доброту, помогая воспитывать многих молодых талантов и развивать искусство.'}
    },
    'ES|C': {
      male: {who: 'Мухаммад аль-Хорезми',
             why: 'Разложил сложную задачу на точные шаги — слово «алгоритм» осталось от его имени.'},
      female: {who: 'Томирис', years: 'VI век до н. э.',
               why: 'Благодаря решительности, сильной воле и мудрым решениям она защищала свой народ и показала пример устойчивого лидерства.'}
    },
    'A|C': {
      male: {who: 'Имам Бухари',
             why: 'Строго проверял каждое предание и включал в свод только достоверные.'},
      female: {who: 'Сарай Мульк Ханум — Бибиханым', years: 'ок. 1341–1408',
               why: 'Как мудрая советница, покровительница просвещения и влиятельная государственная деятельница, она была надёжной опорой для окружающих и общества.'}
    }
  }
},

en: {
  ui: {
    strength: 'Strength: ',
    watch:    'Worth watching: ',
    fig:      'From history: ',
    figmale:  'Male figure:',
    figfemale:'Female figure:',
    resume:   'Resume the test',
    vgYours:  'Your character'
  },
  fam: {
    lead: 'Leaders',
    crea: 'Creators',
    care: 'Carers',
    base: 'Reliable Ones'
  },
  famnote: {
    lead: 'The ones people follow',
    crea: 'The ones who find new ideas and answers',
    care: 'The ones who notice the people around them',
    base: 'Responsible people who keep their word'
  },
  traits: {
    ES: 'Emotional stability',
    E:  'Extraversion',
    O:  'Openness to experience',
    A:  'Agreeableness',
    C:  'Conscientiousness'
  },
  arch: {
    'ES|E': {
      name: 'Leader',
      lines: ['Even when things heat up you do not raise your voice — which is why people listen to you.',
              'When a group loses its way, you are usually the one who points out the direction.'],
      strength: 'making the right call under pressure.',
      watch: 'Your calm can read as indifference. Do not miss the moment when the people close to you want more feeling from you.',
      figure: {who: 'Bahouddin Naqshband',
               why: 'Led people by his own example rather than by compulsion.'}
    },
    'E|C': {
      name: 'Organiser',
      lines: ['You move from talk to action quickly — while others are still discussing the plan, you have started.',
              'And you can get the people around you moving too.'],
      strength: 'turning an idea into something real.',
      watch: 'Because you start fast, you sometimes forget to ask what others think. The best idea will not always be yours.',
      figure: {who: 'Nodirabegim',
               why: 'Built the literary circle of Kokand around her, and had madrasas and mosques constructed.'}
    },
    'ES|O': {
      name: 'Explorer',
      lines: ['When you meet something unfamiliar you try it first and give your opinion afterwards.',
              'But you go into an adventure clear-headed, not blindly.'],
      strength: 'exploring an unknown path without losing your nerve.',
      watch: 'There is a risk of getting caught up in the next new thing and abandoning what you started. Try carrying one thing all the way through.',
      figure: {who: 'Abu Rayhan Biruni',
               why: 'Studied unfamiliar lands and unfamiliar sciences with the same composure.'}
    },
    'E|O': {
      name: 'Creator',
      lines: ['Your ideas never run out, and you like telling people about them.',
              'Once you start explaining an idea, whoever is listening gets interested too.'],
      strength: 'making a new idea catch on.',
      watch: 'Many ideas, little time. Start them all at once and none of them may finish.',
      figure: {who: 'Zebunniso Begim',
               why: 'Of the Mughal house; wrote a complete divan of poetry under the pen name "Makhfi".'}
    },
    'O|C': {
      name: 'Visionary',
      lines: ['You find a new answer — and you see it through to the end.',
              'The idea does not stay in the notebook: you turn it into a schedule and a set of steps.'],
      strength: 'giving an idea a clear structure.',
      watch: 'Trying to make everything perfect slows you down. Sometimes "good enough" is a real result too.',
      figure: {who: 'Mirzo Ulugbek',
               why: 'Set out to count the stars, built an observatory, and catalogued 1,018 of them.'}
    },
    'ES|A': {
      name: 'Trusted Friend',
      lines: ['People tell you their secrets, because they feel safe around you.',
              'When someone is upset, you are usually the first to notice.'],
      strength: 'steadying other people.',
      watch: 'Helping everyone makes it easy to leave no time for yourself. Learn to say no as well.',
      figure: {who: 'Jahon Otin Uvaysi',
               why: 'A poet and a teacher; she taught Nodirabegim the craft of verse.'}
    },
    'E|A': {
      name: 'Heart of the Group',
      lines: ['In a room you have walked into, conversation starts on its own.',
              'You notice the person left on the edge of things, and you call them over.'],
      strength: 'bringing people together.',
      watch: 'Trying to be on good terms with everyone, you may never say what you actually think. Your view matters too.',
      figure: {who: 'Alisher Navoi',
               why: 'Wrote in his own language, and in doing so brought a whole people closer together.'}
    },
    'O|A': {
      name: 'Kind Soul',
      lines: ['New ideas and care for people live side by side in you.',
              'When you see a problem, you think about the people first.'],
      strength: 'finding an answer that is both useful and humane.',
      watch: 'You take on other people’s problems as your own. You do not have to solve everything alone.',
      figure: {who: 'Abdulla Avloniy',
               why: 'Put literature, theatre, journalism and education to work for his people.'}
    },
    'ES|C': {
      name: 'Planner',
      lines: ['You make a plan and you do not get pulled away from it.',
              'Where others have given up, you are still working.'],
      strength: 'lasting the distance.',
      watch: 'When the plan breaks, you struggle. Changing route is sometimes not a defeat.',
      figure: {who: 'Muhammad al-Khwarizmi',
               why: 'Broke a complex problem into exact steps — the word "algorithm" comes from his name.'}
    },
    'A|C': {
      name: 'True to Their Word',
      lines: ['You think before you promise — because a promise you make, you keep.',
              'Which is why the thing that matters is usually handed to you.'],
      strength: 'keeping your word.',
      watch: 'Taking every task on yourself means carrying more than your share. Asking for help is also a strength.',
      figure: {who: 'Imam al-Bukhari',
               why: 'Checked every account rigorously and admitted only the reliable ones into his collection.'}
    }
  },
  figvar: {
    'ES|E': {
      male: {who: 'Bahouddin Naqshband',
             why: 'Led people by his own example rather than by compulsion.'},
      female: {who: 'Zulfiya',
               why: 'Showed what quiet strength and leadership look like through her poetry, her endurance and her steady public work.'}
    },
    'E|C': {
      male: {who: 'Amir Temur',
             why: 'He built a strong centralized state and relied on order, clear systems, and strategy in governance.'},
      female: {who: 'Nodirabegim',
               why: 'Built the literary circle of Kokand around her, and had madrasas and mosques constructed.'}
    },
    'ES|O': {
      male: {who: 'Abu Rayhan Biruni',
             why: 'Studied unfamiliar lands and unfamiliar sciences with the same composure.'},
      female: {who: 'Gulbadan Begum',
               why: 'Curious about learning and travel, she carefully recorded the life of her time in the “Humayun-nama.”'}
    },
    'E|O': {
      male: {who: 'Kamal al-Din Behzad', years: 'c. 1455–1535/36',
             why: 'He brought vivid figures and innovative compositions to miniature painting, strongly influencing an entire school of artists.'},
      female: {who: 'Zebunniso Begim',
               why: 'Of the Mughal house; wrote a complete divan of poetry under the pen name "Makhfi".'}
    },
    'O|C': {
      male: {who: 'Mirzo Ulugbek',
             why: 'Set out to count the stars, built an observatory, and catalogued 1,018 of them.'},
      female: {who: 'Gawhar Shad Begum', years: 'c. 1378–1457',
               why: 'She supported architecture, education, and the arts, turning ambitious cultural ideas into clear plans and major building projects.'}
    },
    'ES|A': {
      male: {who: 'Ibn Sina (Avicenna)',
             why: 'As a physician and scholar, he devoted his knowledge to helping people and protecting their health and well-being.'},
      female: {who: 'Jahon Otin Uvaysi',
               why: 'A poet and a teacher; she taught Nodirabegim the craft of verse.'}
    },
    'E|A': {
      male: {who: 'Alisher Navoi',
             why: 'Wrote in his own language, and in doing so brought a whole people closer together.'},
      female: {who: 'Tamara Khanum',
               why: 'Through dance and song, she introduced audiences to the cultures of different peoples and brought people together on stage.'}
    },
    'O|A': {
      male: {who: 'Abdulla Avloniy',
             why: 'Put literature, theatre, journalism and education to work for his people.'},
      female: {who: 'Mukarrama Turgunboyeva',
               why: 'Through the art of dance, she shared beauty and kindness while helping nurture many young talents and develop the arts.'}
    },
    'ES|C': {
      male: {who: 'Muhammad al-Khwarizmi',
             why: 'Broke a complex problem into exact steps — the word "algorithm" comes from his name.'},
      female: {who: 'Tomyris', years: '6th century BCE',
               why: 'With determination, strong will, and wise decisions, she defended her people and showed an example of steady leadership.'}
    },
    'A|C': {
      male: {who: 'Imam al-Bukhari',
             why: 'Checked every account rigorously and admitted only the reliable ones into his collection.'},
      female: {who: 'Saray Mulk Khanum — Bibi Khanum', years: 'c. 1341–1408',
               why: 'As a wise adviser, patron of education, and influential public figure, she provided dependable support to those around her and to society.'}
    }
  }
}

};

// ---------- resolution ----------
// The page's own <html lang> decides the language, so a page and its content can
// never disagree. Anything the language does not define falls through to the
// Uzbek original in characters.js.
function tmLang(){
  var l = (document.documentElement.getAttribute('lang') || 'uz').slice(0, 2);
  return STRINGS[l] ? l : 'uz';
}

function tmUi(key){
  var s = STRINGS[tmLang()];
  var uz = {strength: 'Kuchli tomoni: ', watch: 'Eʼtibor bering: ',
            fig: 'Tarixdan: ', figmale: 'Erkak siymo:', figfemale: 'Ayol siymo:',
            resume: 'Testni davom ettirish',
            vgYours: 'Sizning obrazingiz'};
  return (s && s.ui && s.ui[key]) || uz[key];
}

// The five trait names, in the reader's language. Uzbek is the base, and it is
// the SAME wording the test's own result screen uses -- a sample result that
// named the traits differently from the real one would be worse than no sample.
function tmTrait(t){
  var s = STRINGS[tmLang()];
  var uz = {ES: 'Hissiy barqarorlik', E: 'Kirishimlilik', O: 'Yangilikka ochiqlik',
            A: 'Kelishuvchanlik', C: 'Masʼuliyatlilik'};
  return (s && s.traits && s.traits[t]) || uz[t];
}

function tmFam(f){
  var s = STRINGS[tmLang()];
  return (s && s.fam && s.fam[f]) || FAMILIES[f].name;
}

function tmFamNote(f){
  var s = STRINGS[tmLang()];
  return (s && s.famnote && s.famnote[f]) || FAM_NOTES[f];
}

// Returns the archetype with any translated fields laid over the Uzbek base, so
// a partially translated entry still renders a complete card.
function tmArch(key){
  var base = ARCHETYPES[key], s = STRINGS[tmLang()];
  var t = s && s.arch && s.arch[key];
  if (!t) return base;
  var out = {}, k;
  for (k in base) out[k] = base[k];
  for (k in t) if (k !== 'figure') out[k] = t[k];
  if (t.figure){
    out.figure = {who: t.figure.who || base.figure.who,
                  years: base.figure.years,               // dates do not translate
                  why: t.figure.why || base.figure.why};
  }
  return out;
}
