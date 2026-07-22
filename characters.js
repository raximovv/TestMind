// TestMind — archetype definitions and character artwork.
// Shared by the landing page (index.html) and the test (test.html), so the ten
// characters can never drift apart between the two.

// ---------- Shareable archetype ----------
// Derived from the user's two STRONGEST traits, so every one of the 10 results is
// something a teenager is happy to post. No combination produces a negative label.
// The ten are grouped into four families purely for colour + a sense of belonging.
var FAMILIES = {
  lead: {name:'Yetakchilar',  c:'#0F6E8C', soft:'#E1EEF2'},
  crea: {name:'Ijodkorlar',   c:'#6B4FA8', soft:'#EDE7F7'},
  care: {name:'Gʻamxoʻrlar',  c:'#237A5E', soft:'#E2F1EC'},
  base: {name:'Tayanchlar',   c:'#A2731F', soft:'#F6EEDC'}
};

// Human-readable trait names, shared by the test and the archetype pages.
var TRAIT_NAMES = {ES:'Hissiy barqarorlik', E:'Kirishimlilik', O:'Yangilikka ochiqlik',
                   A:'Kelishuvchanlik', C:'Masʼuliyatlilik'};

var ARCHETYPES = {
  'ES|E': {ikat2:'#0A5670', ikat3:'#E8C25A', name:'Xotirjam Yetakchi', slug:'xotirjam-yetakchi', fam:'lead',
    lines:['Vaziyat qizib ketganda ham ovozingizni koʻtarmaysiz — shuning uchun odamlar sizga quloq soladi.',
           'Guruh adashib qolganda yoʻnalishni koʻrsatadigan odam odatda siz boʻlasiz.'],
    strength:'bosim ostida toʻgʻri qaror qabul qilish.',
    watch:'Xotirjamligingiz baʼzan befarqlikdek koʻrinadi. Yaqinlaringiz sizdan koʻproq hissiyot kutayotganini sezmay qolmang.',
    figure:{who:'Bahouddin Naqshband', years:'1318–1389', why:'Odamlarni majburlab emas, oʻz namunasi bilan ergashtirgan.'}},

  'E|C':  {ikat2:'#12667F', ikat3:'#F0DCA8', name:'Gʻayratli Tashkilotchi', slug:'gayratli-tashkilotchi', fam:'lead',
    lines:['Gapdan ishga tez oʻtasiz — rejani boshqalar hali muhokama qilayotganda siz boshlab yuborgan boʻlasiz.',
           'Atrofdagilarni ham harakatga sola olasiz.'],
    strength:'gʻoyani haqiqatga aylantirish.',
    watch:'Tez boshlaganingiz uchun baʼzan boshqalarning fikrini soʻrashni unutasiz. Eng yaxshi gʻoya doim sizniki boʻlmasligi mumkin.',
    figure:{who:'Nodirabegim', years:'1792–1842', why:'Qoʻqonda adabiy muhitni uyushtirgan, madrasa va masjidlar qurdirgan.'}},

  'ES|O': {ikat2:'#563C8C', ikat3:'#E8C25A', name:'Xotirjam Kashfiyotchi', slug:'xotirjam-kashfiyotchi', fam:'crea',
    lines:['Notanish narsani koʻrsangiz avval sinab koʻrasiz, keyin fikr bildirasiz.',
           'Lekin sarguzashtga koʻzni yumib emas, sovuqqonlik bilan kirasiz.'],
    strength:'notanish yoʻlni xotirjam tekshirib koʻrish.',
    watch:'Yangi narsaga tez qiziqib, boshlagan ishingizni yarmida tashlab qoʻyish xavfi bor. Bittasini oxirigacha olib borib koʻring.',
    figure:{who:'Abu Rayhon Beruniy', years:'973–1048', why:'Notanish oʻlkalarni ham, notanish fanlarni ham sovuqqonlik bilan oʻrgangan.'}},

  'E|O':  {ikat2:'#6B4CA6', ikat3:'#F2E3B0', name:'Gʻayratli Ijodkor', slug:'gayratli-ijodkor', fam:'crea',
    lines:['Gʻoyalaringiz tugamaydi va ularni odamlarga gapirib berishni yaxshi koʻrasiz.',
           'Bir gʻoyani tushuntira boshlasangiz, tinglayotgan odam ham qiziqib qoladi.'],
    strength:'yangi gʻoyani odamlarga yuqtirish.',
    watch:'Gʻoya koʻp, vaqt kam. Hammasini birdan boshlasangiz, hech biri tugamasligi mumkin.',
    figure:{who:'Zebunniso Begim', years:'1638–1702', why:'Boburiylar xonadonidan; «Maxfiy» taxallusi bilan butun bir devon yozgan.'}},

  'O|C':  {ikat2:'#463178', ikat3:'#E0C070', name:'Ijodkor Strateg', slug:'ijodkor-strateg', fam:'crea',
    lines:['Yangi yechim topasiz — va uni oxiriga ham yetkazasiz.',
           'Gʻoyani daftarda qoldirmaysiz — jadvalga, qadamlarga aylantirasiz.'],
    strength:'gʻoyani aniq tizimga solish.',
    watch:'Hammasini mukammal qilishga urinish sizni sekinlashtiradi. Baʼzan «yetarlicha yaxshi» ham haqiqiy natija.',
    figure:{who:'Mirzo Ulugʻbek', years:'1394–1449', why:'Yulduzlarni sanashni orzu qilgan, rasadxona qurgan va 1018 tasini roʻyxatga olgan.'}},

  'ES|A': {ikat2:'#24735A', ikat3:'#EBD79A', name:'Ishonchli Doʻst', slug:'ishonchli-dost', fam:'care',
    lines:['Odamlar sizga sirini aytadi, chunki yoningizda oʻzini xavfsiz his qiladi.',
           'Kimdir xafa boʻlsa, koʻpincha birinchi boʻlib siz sezasiz.'],
    strength:'boshqalarni tinchlantira olish.',
    watch:'Boshqalarga yordam berib, oʻzingizga vaqt qoldirmaslik oson. «Yoʻq» deyishni ham oʻrganing.',
    figure:{who:'Jahonotin Uvaysiy', years:'1781–1845', why:'Shoira va ustoz; Nodirabegimga sheʼr ilmini oʻrgatgan.'}},

  'E|A':  {ikat2:'#19614A', ikat3:'#E8C25A', name:'Jamoaning Yuragi', slug:'jamoaning-yuragi', fam:'care',
    lines:['Siz kirgan xonada suhbat oʻzidan-oʻzi boshlanib ketadi.',
           'Chetda qolgan odamni sezasiz va yoningizga chaqirasiz.'],
    strength:'odamlarni birlashtirish.',
    watch:'Hamma bilan yaxshi boʻlishga urinib, oʻz fikringizni aytmay qoʻyishingiz mumkin. Sizning fikringiz ham muhim.',
    figure:{who:'Alisher Navoiy', years:'1441–1501', why:'Oʻz tilida yozib, butun bir xalqni bir-biriga yaqinlashtirgan.'}},

  'O|A':  {ikat2:'#337E68', ikat3:'#E5D49C', name:'Ijodkor Insonparvar', slug:'ijodkor-insonparvar', fam:'care',
    lines:['Yangi gʻoyalar va odamlarga gʻamxoʻrlik sizda birga yashaydi.',
           'Muammoni koʻrganingizda avval odamlar haqida oʻylaysiz.'],
    strength:'foydali va insoniy yechim topish.',
    watch:'Boshqalarning muammosini oʻzingizniki qilib olasiz. Hammasini yolgʻiz hal qilishingiz shart emas.',
    figure:{who:'Anbar Otin', years:'1870–1915', why:'Sheʼrlarida oddiy odamlarning va ayollarning hayoti haqida yozgan.'}},

  'ES|C': {ikat2:'#8E621A', ikat3:'#F3E3BE', name:'Barqaror Strateg', slug:'barqaror-strateg', fam:'base',
    lines:['Reja tuzasiz va rejadan chalgʻimaysiz.',
           'Boshqalar taslim boʻlgan joyda siz hali ishlab turasiz.'],
    strength:'uzoq masofaga chidash.',
    watch:'Reja buzilganda qiynalasiz. Baʼzan yoʻlni oʻzgartirish — magʻlubiyat emas.',
    figure:{who:'Muhammad al-Xorazmiy', years:'783–850', why:'Murakkab masalani aniq qadamlarga boʻlgan — «algoritm» soʻzi uning nomidan qolgan.'}},

  'A|C':  {ikat2:'#A5771F', ikat3:'#F5E6C0', name:'Ishonchli Tayanch', slug:'ishonchli-tayanch', fam:'base',
    lines:['Vaʼda berishdan oldin oʻylaysiz — chunki bergan vaʼdangizni bajarasiz.',
           'Shuning uchun muhim ish koʻpincha aynan sizga topshiriladi.'],
    strength:'soʻzida turish.',
    watch:'Hamma ishni oʻz zimmangizga olib, ortiqcha yuk koʻtarib yurasiz. Yordam soʻrash ham kuch.',
    figure:{who:'Dilshod Barno', years:'1800–1905', why:'Ellik yil davomida 891 nafar qizga oʻqish va yozishni oʻrgatgan.'}}
};

// ---------- Character illustrations ----------
// Flat vector, Uzbek dress (doʻppi, chopon, belbogʻ, roʻmol). All ten are built from
// one body so the set reads as a family; only colours, headwear and the held object
// change. Drawn inline as SVG so the page stays a single file with no image requests.
var INK = '#2B2733';

// Uzbek ikat, known locally as abr ("cloud"): the yarn is dyed before weaving, so
// every band has a soft, feathered edge instead of a crisp one. Between the bands
// sit bodom (almond) motifs. Each character needs its own pattern id, because a
// page inlines all ten SVGs at once and duplicate ids would collide.
function ikatPattern(id, base, band, motif){
  var teeth = '', y;
  for (y = -2; y < 28; y += 6.5){
    teeth += 'M3.2 ' + y + ' l-2.7 2.7 2.7 2.7 z ';
    teeth += 'M9.8 ' + (y + 3.25) + ' l2.7 2.7 -2.7 2.7 z ';
  }
  return '<pattern id="' + id + '" width="20" height="26" patternUnits="userSpaceOnUse">'
    + '<rect width="20" height="26" fill="' + base + '"/>'
    + '<rect x="3.2" y="0" width="6.6" height="26" fill="' + band + '"/>'
    + '<path d="' + teeth + '" fill="' + band + '"/>'
    + '<path d="M15.6 6.5 q2.9 5.2 0 10.4 q-2.9 -5.2 0 -10.4z" fill="' + motif + '"/>'
    + '<path d="M15.6 20 q1.7 2.8 0 5.6 q-1.7 -2.8 0 -5.6z" fill="' + motif + '" opacity=".65"/>'
    + '</pattern>';
}

function tmFigure(o){
  var skin = o.skin || '#F0C69C', skinD = o.skinD || '#DCA97B';
  var robe = o.robe, robeD = o.robeD, sash = o.sash;
  var pid = 'ikat-' + (o.uid || 'x');
  var cloth = 'url(#' + pid + ')';
  var s = '', i;

  s += '<defs>' + ikatPattern(pid, robe, o.ikat2 || robeD, o.ikat3 || '#E8C25A') + '</defs>';

  s += '<ellipse cx="100" cy="241" rx="52" ry="7" fill="#0B2027" opacity=".10"/>';
  s += '<rect x="83" y="186" width="15" height="46" rx="7" fill="#3C4C55"/>'
     + '<rect x="102" y="186" width="15" height="46" rx="7" fill="#3C4C55"/>';
  s += '<rect x="73" y="225" width="27" height="13" rx="6.5" fill="#28363D"/>'
     + '<rect x="100" y="225" width="27" height="13" rx="6.5" fill="#28363D"/>';

  if (o.head === 'hair'){
    s += '<path d="M64 60 Q64 20 100 20 Q136 20 136 60 V110 Q136 118 128 116 L124 60 H76 L72 116 Q64 118 64 110 Z" fill="'+(o.hair||'#332D38')+'"/>';
  }

  s += '<path d="M90 72 h20 v24 q-10 6 -20 0 z" fill="'+skinD+'"/>';
  // chopon in ikat cloth
  s += '<path d="M68 94 Q100 84 132 94 L148 202 Q149 209 142 209 H58 Q51 209 52 202 Z" fill="'+cloth+'"/>';
  s += '<path d="M86 90 Q100 82 114 90 L100 114 Z" fill="'+skinD+'"/>';
  // plain binding down the front opening, as a real chopon has
  s += '<path d="M97 112 h6 l5 97 h-16 z" fill="'+robeD+'"/>';
  s += '<path d="M86 90 Q100 82 114 90 L110 95 Q100 88 90 95 Z" fill="'+robeD+'"/>';

  // tumor - the triangular amulet worn against the evil eye
  if (o.head === 'romol' || o.head === 'hair'){
    s += '<path d="M88 95 Q100 101 112 95" stroke="#C9A227" stroke-width="1.5" fill="none"/>'
       + '<path d="M100 100 l6.5 11.5 h-13 z" fill="#C9A227"/>'
       + '<circle cx="100" cy="106" r="1.9" fill="#8A6520"/>';
  }

  // belbogʻ
  s += '<path d="M60 150 H140 L143 170 H57 Z" fill="'+sash+'"/>';
  s += '<path d="M58 165 H142 L143 170 H57 Z" fill="#0B2027" opacity=".13"/>';

  s += '<g transform="rotate(10 78 100)"><rect x="69" y="100" width="18" height="64" rx="9" fill="'+cloth+'"/>'
     + '<rect x="69" y="144" width="18" height="7" fill="'+robeD+'"/></g>';
  s += '<g transform="rotate(-10 122 100)"><rect x="113" y="100" width="18" height="64" rx="9" fill="'+cloth+'"/>'
     + '<rect x="113" y="144" width="18" height="7" fill="'+robeD+'"/></g>';
  s += '<circle cx="67" cy="161" r="9.5" fill="'+skin+'"/><circle cx="133" cy="161" r="9.5" fill="'+skin+'"/>';

  s += '<circle cx="71" cy="60" r="6.5" fill="'+skinD+'"/><circle cx="129" cy="60" r="6.5" fill="'+skinD+'"/>';
  s += '<rect x="71" y="30" width="58" height="56" rx="23" fill="'+skin+'"/>';

  if (o.head === 'doppi'){
    // Chust doʻppi: black ground, four white qalampir pods, sixteen arches on the band.
    // The whole cap sits high on the crown - the band must clear the eyebrows at y=50.
    var cap = o.cap || '#141C33', capD = o.capD || '#0B1124';
    s += '<path d="M68 40 Q68 6 100 6 Q132 6 132 40 Z" fill="'+cap+'"/>';
    // qalampir: a curved pepper pod, mirrored in pairs the way they sit round the crown
    var pods = '', px = [80, 93.3, 106.7, 120];
    for (i = 0; i < 4; i++){
      var dir = i < 2 ? 1 : -1;
      pods += '<g transform="translate(' + px[i] + ',12) scale(' + dir + ',1)">'
            + '<path d="M0 0 c5 3.4 6.6 10 2.6 14.4 c-2.2 2.4 -6 1.8 -7 -1.2 '
            + 'c-1.8 -5.4 0.2 -10.8 4.4 -13.2 z"/>'
            + '<path d="M-0.4 0.4 q2.6 -2.4 4.6 -1.6 q-1.8 2 -4.6 2.6 z"/></g>';
    }
    s += '<g fill="#F4F7F8" opacity=".94">' + pods + '</g>';
    s += '<rect x="65" y="32" width="70" height="13" rx="3" fill="'+capD+'"/>';
    var arcs = '';
    for (i = 0; i < 16; i++) arcs += 'M' + (66.5 + i * 4.25) + ' 42.6 q2.125 -4.6 4.25 0 ';
    s += '<path d="'+arcs+'" stroke="#F4F7F8" stroke-width="1.3" fill="none" opacity=".92"/>';
  } else if (o.head === 'romol'){
    s += '<path d="M62 104 V60 Q62 18 100 18 Q138 18 138 60 V104 Q129 109 122 102 V60 Q122 40 100 40 Q78 40 78 60 V102 Q71 109 62 104 Z" fill="'+o.scarf+'"/>';
    s += '<path d="M78 60 Q78 40 100 40 Q122 40 122 60" stroke="'+o.scarfD+'" stroke-width="4.5" fill="none"/>';
    // small bodom motifs, as on a printed roʻmol
    s += '<g fill="'+(o.scarfM||'#F3E6C4')+'" opacity=".75">'
       + '<path d="M70 70 q2.4 4 0 8 q-2.4 -4 0 -8z"/><path d="M70 88 q2.4 4 0 8 q-2.4 -4 0 -8z"/>'
       + '<path d="M130 70 q2.4 4 0 8 q-2.4 -4 0 -8z"/><path d="M130 88 q2.4 4 0 8 q-2.4 -4 0 -8z"/>'
       + '<path d="M100 24 q2.4 4 0 8 q-2.4 -4 0 -8z"/><path d="M85 28 q2.4 4 0 8 q-2.4 -4 0 -8z"/>'
       + '<path d="M115 28 q2.4 4 0 8 q-2.4 -4 0 -8z"/></g>';
  } else {
    s += '<path d="M69 56 Q70 26 100 26 Q130 26 131 56 Q124 40 100 40 Q76 40 69 56 Z" fill="'+(o.hair||'#332D38')+'"/>';
    if (o.band) s += '<path d="M68 46 Q100 34 132 46 L132 52 Q100 40 68 52 Z" fill="'+o.band+'"/>';
    // earrings, visible only when the hair is uncovered
    s += '<circle cx="70" cy="67" r="2.3" fill="#C9A227"/><circle cx="130" cy="67" r="2.3" fill="#C9A227"/>';
  }

  s += '<circle cx="88" cy="59" r="3.5" fill="'+INK+'"/><circle cx="112" cy="59" r="3.5" fill="'+INK+'"/>';
  s += '<path d="M82.5 50 q5.5 -3.5 11 0" stroke="'+INK+'" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
     + '<path d="M106.5 50 q5.5 -3.5 11 0" stroke="'+INK+'" stroke-width="2.6" fill="none" stroke-linecap="round"/>';
  s += '<path d="M92 71 q8 6.5 16 0" stroke="'+INK+'" stroke-width="2.8" fill="none" stroke-linecap="round"/>';
  s += '<ellipse cx="80" cy="67" rx="5.5" ry="3.5" fill="#E0805C" opacity=".28"/>'
     + '<ellipse cx="120" cy="67" rx="5.5" ry="3.5" fill="#E0805C" opacity=".28"/>';

  // Props are nudged down so the held object sits below the belbogʻ rather than on it.
  return s + (o.prop ? '<g transform="translate(0,12)">' + o.prop + '</g>' : '');
}

// Held objects. Three are deliberately Uzbek: the piyola, the doira and the non.
var TM_PROPS = {
  compass:
    '<g transform="translate(137,154)"><circle r="20" fill="#F4F7F8" stroke="#C08A2E" stroke-width="4"/>'
    + '<circle r="13.5" fill="#E3EFF3"/><path d="M0 -11 L5 0 L0 4 L-5 0 Z" fill="#C0392B"/>'
    + '<path d="M0 11 L5 0 L0 -4 L-5 0 Z" fill="#8FA3AB"/><circle r="2.6" fill="'+INK+'"/></g>',

  clipboard:
    '<g transform="translate(137,150) rotate(6)">'
    + '<rect x="-17" y="-23" width="34" height="46" rx="4" fill="#F4F7F8" stroke="#8FA3AB" stroke-width="2"/>'
    + '<rect x="-9" y="-28" width="18" height="9" rx="3.5" fill="#C08A2E"/>'
    + '<path d="M-10 -8 l4 4 8 -9" stroke="#2E8B6B" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    + '<path d="M-10 4 l4 4 8 -9" stroke="#2E8B6B" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    + '<path d="M-10 16 h20" stroke="#C6D3D8" stroke-width="3" stroke-linecap="round"/></g>',

  telescope:
    '<g fill="#E8C25A"><path d="M174 92 l2.8 6.6 6.6 2.8 -6.6 2.8 -2.8 6.6 -2.8 -6.6 -6.6 -2.8 6.6 -2.8z"/>'
    + '<path d="M189 66 l2.2 5 5 2.2 -5 2.2 -2.2 5 -2.2 -5 -5 -2.2 5 -2.2z"/></g>'
    + '<g transform="translate(141,156) rotate(35) scale(1.2)">'
    + '<path d="M-7.5 14 L7.5 14 L11.5 -32 L-11.5 -32 Z" fill="#33456E"/>'
    + '<rect x="-14" y="-40" width="28" height="12" rx="4" fill="#E8C25A"/>'
    + '<rect x="-9.5" y="9" width="19" height="10" rx="3" fill="#E8C25A"/>'
    + '<path d="M-9.5 -8 h19" stroke="#5B71A8" stroke-width="4"/></g>',

  palette:
    '<g transform="translate(135,154)"><ellipse rx="22" ry="17" fill="#EEDCBC" stroke="#B99B6E" stroke-width="2"/>'
    + '<circle cx="10" cy="7" r="4.5" fill="#F1F6F7"/><circle cx="-11" cy="-6" r="4" fill="#C0392B"/>'
    + '<circle cx="0" cy="-9" r="4" fill="#2E8B6B"/><circle cx="11" cy="-5" r="4" fill="#0F6E8C"/>'
    + '<circle cx="-13" cy="5" r="4" fill="#C08A2E"/></g>'
    + '<g transform="translate(158,116) rotate(28)"><rect x="-2.6" y="-26" width="5.2" height="30" rx="2" fill="#B98E4A"/>'
    + '<path d="M-4 4 h8 l-2 9 h-4z" fill="#7E5FB8"/></g>',

  book:
    '<g transform="translate(152,44)"><circle r="12.5" fill="#F2D479"/>'
    + '<rect x="-5" y="10" width="10" height="8" rx="2.5" fill="#B98E4A"/>'
    + '<g stroke="#C08A2E" stroke-width="2.6" stroke-linecap="round">'
    + '<path d="M-13 -14 l-5 -5"/><path d="M13 -14 l5 -5"/><path d="M0 -19 v-7"/></g></g>'
    + '<g transform="translate(137,154) scale(1.12)">'
    + '<path d="M-23 -14 q11.5 -6 23 0 q11.5 -6 23 0 v30 q-11.5 -6 -23 0 q-11.5 -6 -23 0z" fill="#B23A48"/>'
    + '<path d="M-19.5 -11 q9.75 -5 19.5 0 q9.75 -5 19.5 0 v25 q-9.75 -5 -19.5 0 q-9.75 -5 -19.5 0z" '
    + 'fill="#F8FAFB" stroke="#8FA3AB" stroke-width="1.6" stroke-linejoin="round"/>'
    + '<path d="M0 -11 v25" stroke="#8FA3AB" stroke-width="2"/>'
    + '<g stroke="#C6D3D8" stroke-width="1.8" stroke-linecap="round">'
    + '<path d="M-15 -1 h11"/><path d="M-15 5 h11"/><path d="M4 -1 h11"/><path d="M4 5 h11"/></g></g>',

  piyola:
    '<g transform="translate(136,148) scale(1.35)">'
    + '<g stroke="#8FA3AB" stroke-width="2" fill="none" opacity=".6" stroke-linecap="round">'
    + '<path d="M-7 -14 q5 -7 0 -13"/><path d="M7 -14 q5 -7 0 -13"/></g>'
    + '<path d="M-18 -4 a18 17 0 0 0 36 0z" fill="#F8FAFB" stroke="#0F6E8C" stroke-width="2.2"/>'
    + '<g fill="#0F6E8C"><circle cx="-7" cy="3" r="2.6"/><circle cx="4" cy="5" r="2.6"/></g>'
    + '<ellipse cy="-4" rx="18" ry="5.5" fill="#E3EFF3" stroke="#0F6E8C" stroke-width="2.2"/>'
    + '<ellipse cy="15" rx="13" ry="4" fill="#E3EFF3" stroke="#0F6E8C" stroke-width="2.2"/></g>',

  doira:
    '<g transform="translate(139,148) rotate(-12)"><circle r="27" fill="#C9A227" stroke="#8F6520" stroke-width="5"/>'
    + '<circle r="21.5" fill="#F0E2C4"/><circle r="21.5" fill="none" stroke="#DCC69C" stroke-width="2"/>'
    + '<g fill="none" stroke="#8F6520" stroke-width="2"><circle cx="0" cy="-30" r="4"/><circle cx="26" cy="-15" r="4"/>'
    + '<circle cx="26" cy="15" r="4"/><circle cx="0" cy="30" r="4"/><circle cx="-26" cy="15" r="4"/>'
    + '<circle cx="-26" cy="-15" r="4"/></g></g>',

  sprout:
    '<g transform="translate(136,154) scale(1.25)">'
    + '<path d="M0 -6 v-20" stroke="#2E8B6B" stroke-width="3.2" stroke-linecap="round"/>'
    + '<path d="M0 -15 q-13 -2 -14 -13 q13 0 14 13z" fill="#43A582"/>'
    + '<path d="M0 -21 q13 -2 14 -13 q-13 0 -14 13z" fill="#2E8B6B"/>'
    + '<path d="M-14 -2 h28 l-4 22 h-20z" fill="#C08A2E"/>'
    + '<rect x="-16" y="-8" width="32" height="8" rx="2.5" fill="#A8762A"/></g>',

  rook:
    '<g transform="translate(136,152) scale(1.12)">'
    + '<path d="M-15 -22 v10 h4 v14 l-5 16 h32 l-5 -16 v-14 h4 v-10 h-6 v5 h-6 v-5 h-6 v5 h-6 v-5z" '
    + 'fill="#F8FAFB" stroke="#2F4550" stroke-width="3" stroke-linejoin="round"/>'
    + '<path d="M-11 2 h22" stroke="#2F4550" stroke-width="3"/>'
    + '<path d="M4 -12 h7 v14 l5 16 h-9 l-4 -16z" fill="#2F4550" opacity=".13"/></g>',

  non:
    '<g transform="translate(136,152)"><circle r="25" fill="#E2BC7A" stroke="#B98E4A" stroke-width="3"/>'
    + '<circle r="13" fill="#CFA25C"/>'
    + '<g fill="#A8763C"><circle r="2.2"/><circle cx="-6" cy="-5" r="1.9"/><circle cx="6" cy="-5" r="1.9"/>'
    + '<circle cx="-6" cy="5" r="1.9"/><circle cx="6" cy="5" r="1.9"/></g>'
    + '<g fill="#F4E3C4"><circle cx="-18" cy="-6" r="1.7"/><circle cx="-12" cy="-15" r="1.7"/>'
    + '<circle cx="0" cy="-19" r="1.7"/><circle cx="12" cy="-15" r="1.7"/><circle cx="18" cy="-6" r="1.7"/>'
    + '<circle cx="18" cy="7" r="1.7"/><circle cx="8" cy="17" r="1.7"/><circle cx="-8" cy="17" r="1.7"/>'
    + '<circle cx="-18" cy="7" r="1.7"/></g></g>'
};

var TM_ART = {
  'ES|E': {head:'doppi', robe:'#12718F', robeD:'#0B5670', sleeve:'#0E6280', sash:'#C08A2E', prop:'compass'},
  'E|C':  {head:'romol', scarf:'#1B7E9C', scarfD:'#0B5670', robe:'#2A94B4', robeD:'#17708C', sleeve:'#1E829F', sash:'#C08A2E', prop:'clipboard'},
  'ES|O': {head:'doppi', cap:'#3A2C63', capD:'#2B2049', robe:'#7E5FB8', robeD:'#5D4490', sleeve:'#6E509F', sash:'#C9A227', prop:'telescope'},
  'E|O':  {head:'hair',  hair:'#3A2F42', band:'#C08A2E', robe:'#9878CC', robeD:'#725598', sleeve:'#8567B8', sash:'#C9A227', prop:'palette'},
  'O|C':  {head:'doppi', cap:'#2B2049', capD:'#1E1636', robe:'#6B54A0', robeD:'#4E3C78', sleeve:'#5D4890', sash:'#C08A2E', prop:'book'},
  'ES|A': {head:'romol', scarf:'#2E8B6B', scarfD:'#1F6650', robe:'#3FA07C', robeD:'#2A7660', sleeve:'#348B6E', sash:'#C08A2E', prop:'piyola'},
  'E|A':  {head:'doppi', robe:'#2E8B6B', robeD:'#1F6650', sleeve:'#277A5E', sash:'#C9A227', prop:'doira'},
  'O|A':  {head:'hair',  hair:'#2F2A35', robe:'#57A88A', robeD:'#3B8068', sleeve:'#4A9679', sash:'#7E5FB8', prop:'sprout'},
  'ES|C': {head:'doppi', cap:'#143F4E', capD:'#0C2F3C', robe:'#C08A2E', robeD:'#946420', sleeve:'#AC7727', sash:'#0F6E8C', prop:'rook'},
  'A|C':  {head:'romol', scarf:'#B2503A', scarfD:'#8B3A28', robe:'#D9A544', robeD:'#A97D2A', sleeve:'#C69235', sash:'#0F6E8C', prop:'non'}
};

var TM_UID = 0;
// width/height are required for the canvas share card to rasterise this in Firefox.
function charSvg(key, alt){
  var o = TM_ART[key]; if (!o) return '';
  var a = {}; for (var k in o) a[k] = o[k];
  a.prop = TM_PROPS[o.prop] || '';
  // Per-INSTANCE, not per-key: a page can draw the same character more than once
  // (the hero scene and a vignette both use O|C), and two <pattern> elements
  // sharing an id is invalid HTML.
  a.uid = key.replace(/[^A-Za-z0-9]/g, '-').toLowerCase() + '-' + (++TM_UID);
  return '<svg xmlns="http://www.w3.org/2000/svg" width="200" height="250" viewBox="0 0 200 250" '
       + 'role="img" aria-label="' + (alt || '') + '">' + tmFigure(a) + '</svg>';
}
