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
    resume:   'Продолжить тест'
  },
  fam: {
    lead: 'Лидеры',
    crea: 'Творцы',
    care: 'Заботливые',
    base: 'Опоры'
  },
  famnote: {
    lead: 'Те, за кем идут люди',
    crea: 'Те, кто находит новые идеи и решения',
    care: 'Те, кто замечает окружающих и поддерживает их',
    base: 'Люди, которые держат слово'
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
      name: 'Спокойный Лидер',
      lines: ['Даже когда обстановка накаляется, вы не повышаете голос — поэтому вас слушают.',
              'Когда группа сбивается с пути, направление обычно показываете вы.'],
      strength: 'принимать верные решения под давлением.',
      watch: 'Ваше спокойствие иногда выглядит как безразличие. Не пропустите момент, когда близкие ждут от вас больше чувств.',
      figure: {who: 'Бахоуддин Накшбанд',
               why: 'Вёл людей за собой не принуждением, а собственным примером.'}
    },
    'E|C': {
      name: 'Энергичный Организатор',
      lines: ['Вы быстро переходите от слов к делу — пока другие ещё обсуждают план, вы уже начали.',
              'И умеете расшевелить остальных.'],
      strength: 'превращать идею в реальность.',
      watch: 'Из-за быстрого старта вы иногда забываете спросить мнение других. Лучшая идея не всегда ваша.',
      figure: {who: 'Нодирабегим',
               why: 'Собрала вокруг себя литературную среду Коканда, строила медресе и мечети.'}
    },
    'ES|O': {
      name: 'Спокойный Исследователь',
      lines: ['Увидев незнакомое, вы сначала пробуете, а уже потом высказываете мнение.',
              'Но в приключение идёте не вслепую, а хладнокровно.'],
      strength: 'спокойно исследовать незнакомый путь.',
      watch: 'Есть риск быстро увлечься новым и бросить начатое на середине. Попробуйте довести до конца хотя бы одно дело.',
      figure: {who: 'Абу Райхан Беруни',
               why: 'С одинаковым хладнокровием изучал и незнакомые земли, и незнакомые науки.'}
    },
    'E|O': {
      name: 'Энергичный Творец',
      lines: ['Идеи у вас не заканчиваются, и вы любите рассказывать о них людям.',
              'Стоит вам начать объяснять идею — слушающий тоже загорается.'],
      strength: 'заражать людей новой идеей.',
      watch: 'Идей много, времени мало. Если начать всё сразу, можно не закончить ничего.',
      figure: {who: 'Зебуннисо Бегим',
               why: 'Из дома Бабуридов; под псевдонимом «Махфи» написала целый диван стихов.'}
    },
    'O|C': {
      name: 'Творческий Стратег',
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
      name: 'Творческий Гуманист',
      lines: ['Новые идеи и забота о людях уживаются в вас вместе.',
              'Увидев проблему, вы прежде всего думаете о людях.'],
      strength: 'находить решение и полезное, и человечное.',
      watch: 'Вы принимаете чужие проблемы как свои. Решать всё в одиночку вовсе не обязательно.',
      figure: {who: 'Анбар Отин',
               why: 'В своих стихах писала о жизни простых людей и женщин.'}
    },
    'ES|C': {
      name: 'Устойчивый Стратег',
      lines: ['Вы составляете план и не отвлекаетесь от него.',
              'Там, где остальные сдались, вы всё ещё работаете.'],
      strength: 'выдерживать длинную дистанцию.',
      watch: 'Когда план рушится, вам тяжело. Иногда сменить путь — не поражение.',
      figure: {who: 'Мухаммад аль-Хорезми',
               why: 'Разложил сложную задачу на точные шаги — слово «алгоритм» осталось от его имени.'}
    },
    'A|C': {
      name: 'Надёжная Опора',
      lines: ['Вы думаете, прежде чем пообещать, — потому что обещанное выполняете.',
              'Поэтому важное дело чаще всего поручают именно вам.'],
      strength: 'держать своё слово.',
      watch: 'Взваливая на себя всё, вы несёте лишний груз. Просить помощи — тоже сила.',
      figure: {who: 'Дилшод Барно',
               why: 'На протяжении пятидесяти лет научила читать и писать 891 девочку.'}
    }
  }
},

en: {
  ui: {
    strength: 'Strength: ',
    watch:    'Worth watching: ',
    fig:      'From history: ',
    resume:   'Resume the test'
  },
  fam: {
    lead: 'Leaders',
    crea: 'Creators',
    care: 'Carers',
    base: 'Anchors'
  },
  famnote: {
    lead: 'The ones people follow',
    crea: 'The ones who find new ideas and answers',
    care: 'The ones who notice the people around them',
    base: 'The ones who keep their word'
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
      name: 'Calm Leader',
      lines: ['Even when things heat up you do not raise your voice — which is why people listen to you.',
              'When a group loses its way, you are usually the one who points out the direction.'],
      strength: 'making the right call under pressure.',
      watch: 'Your calm can read as indifference. Do not miss the moment when the people close to you want more feeling from you.',
      figure: {who: 'Bahouddin Naqshband',
               why: 'Led people by his own example rather than by compulsion.'}
    },
    'E|C': {
      name: 'Driven Organiser',
      lines: ['You move from talk to action quickly — while others are still discussing the plan, you have started.',
              'And you can get the people around you moving too.'],
      strength: 'turning an idea into something real.',
      watch: 'Because you start fast, you sometimes forget to ask what others think. The best idea will not always be yours.',
      figure: {who: 'Nodirabegim',
               why: 'Built the literary circle of Kokand around her, and had madrasas and mosques constructed.'}
    },
    'ES|O': {
      name: 'Calm Explorer',
      lines: ['When you meet something unfamiliar you try it first and give your opinion afterwards.',
              'But you go into an adventure clear-headed, not blindly.'],
      strength: 'exploring an unknown path without losing your nerve.',
      watch: 'There is a risk of getting caught up in the next new thing and abandoning what you started. Try carrying one thing all the way through.',
      figure: {who: 'Abu Rayhan Biruni',
               why: 'Studied unfamiliar lands and unfamiliar sciences with the same composure.'}
    },
    'E|O': {
      name: 'Spirited Creator',
      lines: ['Your ideas never run out, and you like telling people about them.',
              'Once you start explaining an idea, whoever is listening gets interested too.'],
      strength: 'making a new idea catch on.',
      watch: 'Many ideas, little time. Start them all at once and none of them may finish.',
      figure: {who: 'Zebunniso Begim',
               why: 'Of the Mughal house; wrote a complete divan of poetry under the pen name "Makhfi".'}
    },
    'O|C': {
      name: 'Creative Strategist',
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
      name: 'Creative Humanitarian',
      lines: ['New ideas and care for people live side by side in you.',
              'When you see a problem, you think about the people first.'],
      strength: 'finding an answer that is both useful and humane.',
      watch: 'You take on other people’s problems as your own. You do not have to solve everything alone.',
      figure: {who: 'Anbar Otin',
               why: 'Wrote in her poetry about the lives of ordinary people and of women.'}
    },
    'ES|C': {
      name: 'Steady Strategist',
      lines: ['You make a plan and you do not get pulled away from it.',
              'Where others have given up, you are still working.'],
      strength: 'lasting the distance.',
      watch: 'When the plan breaks, you struggle. Changing route is sometimes not a defeat.',
      figure: {who: 'Muhammad al-Khwarizmi',
               why: 'Broke a complex problem into exact steps — the word "algorithm" comes from his name.'}
    },
    'A|C': {
      name: 'Dependable Anchor',
      lines: ['You think before you promise — because a promise you make, you keep.',
              'Which is why the thing that matters is usually handed to you.'],
      strength: 'keeping your word.',
      watch: 'Taking every task on yourself means carrying more than your share. Asking for help is also a strength.',
      figure: {who: 'Dilshod Barno',
               why: 'Over fifty years, taught 891 girls to read and write.'}
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
            fig: 'Tarixdan: ', resume: 'Testni davom ettirish'};
  return (s && s.ui && s.ui[key]) || uz[key];
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
