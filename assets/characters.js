// TestMind — archetype definitions and character artwork.
// Shared by the landing page (index.html) and the test (test.html), so the ten
// characters can never drift apart between the two.

// ---------- Shareable archetype ----------
// Derived from the user's two STRONGEST traits, so every one of the 10 results is
// something a teenager is happy to post. No combination produces a negative label.
// The ten are grouped into four families purely for colour + a sense of belonging.
var FAMILIES = {
  lead: {name:'Yetakchilar',  c:'#0F6E8C', soft:'#E1EEF2', dark:'#12262F', lit:'#5FB4CE'},
  crea: {name:'Ijodkorlar',   c:'#6B4FA8', soft:'#EDE7F7', dark:'#221B36', lit:'#A98BE0'},
  care: {name:'Gʻamxoʻrlar',  c:'#237A5E', soft:'#E2F1EC', dark:'#12271F', lit:'#5FC2A0'},
  base: {name:'Tayanchlar',   c:'#A2731F', soft:'#F6EEDC', dark:'#2B2213', lit:'#D9AE52'}
};

// One line describing each family. Lives here beside FAMILIES rather than in
// site.js, because the archetype-page generator needs it too.
var FAM_NOTES = {
  lead:'Odamlarni ortidan ergashtiradiganlar',
  crea:'Yangi gʻoya va yechim topadiganlar',
  care:'Atrofdagilarni koʻradigan va qoʻllab-quvvatlaydiganlar',
  base:'Vaʼdasida turadigan, ishonchli odamlar'
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
    figure:{who:'Abdulla Avloniy', years:'1878–1934', why:'Adabiyot, teatr, jurnalistika va taʼlimni xalq manfaatiga xizmat qildirgan.'}},

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

// A hand, not a dot. `flip` is 1 for the left hand and -1 for the right, so the
// thumb always points inwards towards the body.
function tmHand(cx, cy, flip, skin, skinD){
  return '<g transform="translate(' + cx + ',' + cy + ') scale(' + flip + ',1)">'
       + '<circle r="9.5" fill="' + skin + '"/>'
       + '<path d="M4 -6.5 q6.5 0.5 6 5.5 q-0.5 4.5 -6 3.5z" fill="' + skin + '"/>'
       + '<path d="M4.4 -5.6 q4.6 0.8 4.4 4.4" stroke="' + skinD
       + '" stroke-width="1.2" fill="none" opacity=".7"/></g>';
}

// TEMPORARY (2026-07-29, at the founder's request): render every archetype as a
// male figure in a doʻppi. Set to false to bring back the roʻmol and uncovered-hair
// variants — nothing was deleted, TM_ART still carries scarf and hair colours.
//
// Worth revisiting: about half the students taking this are girls, and a result
// card that shows an adult man to all of them is a card they are less likely to
// share. Sharing is how this spreads.
var ALL_MALE = true;

// ---- faces -----------------------------------------------------------------
// Until now every figure got one hardcoded face — the same two dots, the same
// arc for a mouth — so ten characters read as one man in ten different coats.
// The costume was already varied; the face was doing none of the work.
//
// Eyes, brows and mouth are the only three marks that still register at the
// ~0.5 scale a card thumbnail draws at, so those are what vary. Each set is
// chosen for the trait pair it belongs to rather than for variety alone: the
// Xotirjam ones sit level and unhurried, the Gʻayratli ones are wide open, and
// the two thinkers actually look like they are looking at something.
//
// Costume, build and props stay in TM_ART. This is expression only.
var TM_EYE = {
  round:  function(x){ return '<circle cx="'+x+'" cy="59" r="3.5" fill="'+INK+'"/>'; },
  // a catchlight is the cheapest way to read as "lit up" without changing size
  wide:   function(x){ return '<circle cx="'+x+'" cy="58.8" r="4.4" fill="'+INK+'"/>'
                            + '<circle cx="'+(x+1.5)+'" cy="57.3" r="1.5" fill="#F4F7F8"/>'; },
  narrow: function(x){ return '<ellipse cx="'+x+'" cy="59" rx="3.9" ry="2.6" fill="'+INK+'"/>'; },
  // closed and curved up — someone already laughing, no pupil at all
  glad:   function(x){ return '<path d="M'+(x-4.2)+' 60.4 q4.2 -5.2 8.4 0" stroke="'+INK+'"'
                            + ' stroke-width="2.7" fill="none" stroke-linecap="round"/>'; },
  // a lid line over the dot reads as attention; without it the same dot is blank
  keen:   function(x){ return '<circle cx="'+x+'" cy="59.6" r="3.4" fill="'+INK+'"/>'
                            + '<path d="M'+(x-4)+' 55.2 q4 -1.9 8 0" stroke="'+INK+'"'
                            + ' stroke-width="2.1" fill="none" stroke-linecap="round"/>'; }
};

// Left and right path, split on the pipe. `set` drops the inner ends toward the
// nose — at this stroke weight that reads as concentration, not as anger.
var TM_BROW = {
  soft:     {w:2.6, d:'M82.5 50 q5.5 -3.5 11 0|M106.5 50 q5.5 -3.5 11 0'},
  straight: {w:2.6, d:'M82.5 49.6 h11|M106.5 49.6 h11'},
  raised:   {w:2.5, d:'M82.5 47.6 q5.5 -4.2 11 0|M106.5 47.6 q5.5 -4.2 11 0'},
  set:      {w:2.9, d:'M82.5 47.8 q5.5 -1.6 11 2.2|M117.5 47.8 q-5.5 -1.6 -11 2.2'},
  heavy:    {w:3.6, d:'M82.5 50 q5.5 -3.2 11 0|M106.5 50 q5.5 -3.2 11 0'}
};

// Path only — the colour is decided per figure, see the mouth note in tmFigure.
var TM_MOUTH = {
  smile: {w:2.8, d:'M92 71 q8 6.5 16 0'},
  wide:  {w:2.8, d:'M90 70.5 q10 8 20 0'},
  soft:  {w:2.6, d:'M93.5 71.5 q6.5 4.2 13 0'},
  level: {w:2.6, d:'M93.5 72 q6.5 2 13 0'},
  // the one open mouth in the set — a lens, not an outline, so it holds at size
  grin:  {fill:true, d:'M90 70.5 q10 9.5 20 0 q-10 3.5 -20 0z'}
};

// All ten combinations are distinct — no two archetypes share a face.
var TM_FACE = {
  'ES|E': {eyes:'narrow', brow:'straight', mouth:'smile', blush:.20},
  'E|C':  {eyes:'wide',   brow:'set',      mouth:'wide',  blush:.30},
  'ES|O': {eyes:'keen',   brow:'raised',   mouth:'soft',  blush:.22},
  'E|O':  {eyes:'wide',   brow:'raised',   mouth:'grin',  blush:.34},
  'O|C':  {eyes:'keen',   brow:'set',      mouth:'level', blush:.16},
  'ES|A': {eyes:'glad',   brow:'soft',     mouth:'smile', blush:.30},
  'E|A':  {eyes:'glad',   brow:'raised',   mouth:'grin',  blush:.34},
  'O|A':  {eyes:'round',  brow:'soft',     mouth:'soft',  blush:.28},
  'ES|C': {eyes:'narrow', brow:'straight', mouth:'level', blush:.14},
  'A|C':  {eyes:'round',  brow:'heavy',    mouth:'smile', blush:.24}
};

function tmFigure(o){
  // Before anything is drawn: the uncovered-hair block runs early, so a later
  // override would leave the hair behind the body still rendered.
  // fem:true opts an entry out of the blanket flag — used where the archetype is
  // paired with a woman from history and a bearded man would read as an error.
  if (ALL_MALE && !o.fem && o.head !== 'doppi') o = shallowCopy(o, {head: 'doppi'});
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

  var gold = o.gold || '#D9AE52', goldD = o.goldD || '#A8762A';

  s += '<path d="M90 72 h20 v24 q-10 6 -20 0 z" fill="'+skinD+'"/>';
  // chopon in ikat cloth
  // Build and hem drive the outline. w spreads the shoulders and the skirt; hem
  // is where the coat stops. Both survive being shrunk to a thumbnail, which the
  // ikat and the cap embroidery do not.
  var bw = o.build === 'stocky' ? 1.10 : (o.build === 'narrow' ? 0.91 : 1);
  var hem = o.hem === 'long' ? 216 : (o.hem === 'short' ? 196 : 206);
  var sx = function(x){ return (100 + (x - 100) * bw).toFixed(1); };
  s += '<path d="M' + sx(68) + ' 94 Q100 84 ' + sx(132) + ' 94 L' + sx(148) + ' ' + (hem - 7)
     + ' Q' + sx(149) + ' ' + hem + ' ' + sx(142) + ' ' + hem
     + ' H' + sx(58) + ' Q' + sx(51) + ' ' + hem + ' ' + sx(52) + ' ' + (hem - 7) + ' Z" fill="'+cloth+'"/>';
  // the koʻylak worn under the chopon shows as a white V at the throat
  s += '<path d="M86 90 Q100 82 114 90 L100 114 Z" fill="#F4F7F8"/>';
  s += '<path d="M86 90 Q100 82 114 90 L100 114 Z" fill="'+INK+'" opacity=".05"/>';

  // Zarhal jiyak — the gold braid down the front opening, round the hem and at
  // the cuffs. It is the most recognisable thing about a good chopon and the
  // difference between a festival coat and a work one. Drawn before the belbogʻ
  // so the sash correctly covers the middle of the placket.
  s += '<path d="M' + sx(53.8) + ' ' + (hem - 8) + ' H' + sx(146.2) + ' L' + sx(148) + ' ' + (hem - 7)
     + ' Q' + sx(149) + ' ' + hem + ' ' + sx(142) + ' ' + hem + ' H' + sx(58)
     + ' Q' + sx(51) + ' ' + hem + ' ' + sx(52) + ' ' + (hem - 7) + ' Z" fill="'+gold+'"/>';
  s += '<path d="M96 110 h8 l' + (5 * bw).toFixed(1) + ' ' + (hem - 8 - 110)
     + ' h-' + (18 * bw).toFixed(1) + ' z" fill="'+gold+'"/>';
  var leaf = '';
  for (i = 0; i < 9; i++) leaf += '<path d="M100 ' + (117 + i * 9) + ' q3.8 3.3 0 6.6 q-3.8 -3.3 0 -6.6z"/>';
  s += '<g fill="'+goldD+'" opacity=".8">' + leaf + '</g>';
  s += '<path d="M86 90 Q100 82 114 90 L110 95 Q100 88 90 95 Z" fill="'+gold+'"/>';

  // tumor - the triangular amulet worn against the evil eye
  if (o.head === 'romol' || o.head === 'hair'){
    s += '<path d="M88 95 Q100 101 112 95" stroke="#C9A227" stroke-width="1.5" fill="none"/>'
       + '<path d="M100 100 l6.5 11.5 h-13 z" fill="#C9A227"/>'
       + '<circle cx="100" cy="106" r="1.9" fill="#8A6520"/>';
  }

  // belbogʻ
  s += '<path d="M60 150 H140 L143 170 H57 Z" fill="'+sash+'"/>';
  s += '<path d="M58 165 H142 L143 170 H57 Z" fill="#0B2027" opacity=".13"/>';

  // Arm poses. 'rest' is both arms down; 'greet' brings the right hand to the
  // chest (the ordinary Uzbek greeting); 'raise' lifts it in an open-handed wave.
  // The held object stays where it is, so a prop never ends up in mid-air.
  var pose = o.pose || 'rest';
  function sleeve(rot, x){
    return '<g transform="rotate(' + rot + ' ' + (x + 9) + ' 100)">'
      + '<rect x="' + x + '" y="100" width="18" height="64" rx="9" fill="' + cloth + '"/>'
      + '<rect x="' + x + '" y="143" width="18" height="8" fill="' + gold + '"/>'
      + '<rect x="' + x + '" y="147.5" width="18" height="2" fill="' + goldD + '" opacity=".5"/></g>';
  }
  s += sleeve(10, 69);                       // left arm is always down
  if (pose === 'greet'){
    // Two segments. The forearm's far end after rotate(108) about the elbow is
    // (106,132); the hand goes there, so it can never float free of the sleeve.
    s += '<g transform="rotate(14 122 104)">'
       + '<rect x="113" y="100" width="18" height="40" rx="9" fill="' + cloth + '"/></g>';
    s += '<g transform="rotate(108 131 140)">'
       + '<rect x="122" y="132" width="18" height="34" rx="9" fill="' + cloth + '"/>'
       + '<rect x="122" y="157" width="18" height="8" fill="' + gold + '"/>'
       + '<rect x="122" y="161.5" width="18" height="2" fill="' + goldD + '" opacity=".5"/></g>';
    s += tmHand(67, 161, 1, skin, skinD) + tmHand(106, 132, -1, skin, skinD);
  } else if (pose === 'raise'){
    // The raised arm ends in the same hand every other pose uses; it used to
    // carry an extended index finger instead.
    //
    // That finger was also hiding a bug. The hand sat at (146,96) while the
    // sleeve, after the rotation, ended somewhere else entirely — a hand
    // floating clear of its own sleeve, which only became obvious once the
    // finger stopped drawing the eye. It is placed like every other hand now:
    // on the sleeve tip, pulled ~3 back along the arm so the cuff and the hand
    // overlap rather than butt together.
    //
    // The angle went from -74 to -125 at the same time. At -74 the arm reached
    // sideways far enough to land on whoever stood to the right in the Registan
    // scene; -125 lifts it into an actual raised hand, 45 units higher and 7
    // narrower, clearing both the neighbour and this figure's own doʻppi.
    s += '<g transform="rotate(-125 122 108)">' + sleeve(0, 113) + '</g>';
    s += tmHand(67, 161, 1, skin, skinD) + tmHand(165, 78, -1, skin, skinD);
  } else {
    s += sleeve(-10, 113);
    s += tmHand(67, 161, 1, skin, skinD) + tmHand(133, 161, -1, skin, skinD);
  }

  s += '<circle cx="71" cy="60" r="6.5" fill="'+skinD+'"/><circle cx="129" cy="60" r="6.5" fill="'+skinD+'"/>';
  s += '<rect x="71" y="30" width="58" height="56" rx="23" fill="'+skin+'"/>';

  // ---- regional cap styles ----
  // chust   black ground, four white qalampir pods, arched band   (Fergana)
  // sanama  dense coloured surface stitching over the crown       (Kitob/Shahrisabz)
  //         NB 'iroqi' was used here before and is wrong: that is a
  //         women's skullcap of Sogdian origin, not a men's style.
  // zardozi gold couching on velvet, the formal one               (Buxoro)
  // chizma  outlined bodom medallions, lighter ground             (Samarqand)
  if (o.head === 'doppi'){
    var style = o.dstyle || 'chust';
    // Chust doʻppi: black ground, four white qalampir pods, sixteen arches on the band.
    // The whole cap sits high on the crown - the band must clear the eyebrows at y=50.
    var cap = o.cap || '#141C33', capD = o.capD || '#0B1124';
    // Crown height is the top third of the silhouette — the most visible
    // difference of all at thumbnail size.
    var top = o.crown === 'tall' ? 2 : (o.crown === 'low' ? 16 : 9);
    var cw = o.crown === 'tall' ? 30 : (o.crown === 'low' ? 34 : 32);
    var tw = cw - 7;                       // the flat top is narrower than the base
    // Four panels: flat top, angled sides, and a seam where the front facet meets
    // the side one. A dome would be the Kazakh takyia; this packs flat.
    s += '<path d="M' + (100 - cw) + ' 41 L' + (100 - tw) + ' ' + top
       + ' Q100 ' + (top - 1.5) + ' ' + (100 + tw) + ' ' + top
       + ' L' + (100 + cw) + ' 41 Z" fill="'+cap+'"/>';
    s += '<path d="M' + (100 - cw) + ' 41 L' + (100 - tw) + ' ' + top
       + ' L' + (100 - tw + 10) + ' ' + (top + 0.6) + ' L' + (100 - cw + 10) + ' 41 Z" '
       + 'fill="'+capD+'" opacity=".45"/>';
    s += '<path d="M' + (100 + cw) + ' 41 L' + (100 + tw) + ' ' + top + '" stroke="'+capD
       + '" stroke-width="1" opacity=".5" fill="none"/>';
    // qalampir: a curved pepper pod, mirrored in pairs the way they sit round the crown
    var pods = '', px = [80, 93.3, 106.7, 120];
    for (i = 0; i < 4; i++){
      var dir = i < 2 ? 1 : -1;
      pods += '<g transform="translate(' + px[i] + ',12) scale(' + dir + ',1)">'
            + '<path d="M0 0 c5 3.4 6.6 10 2.6 14.4 c-2.2 2.4 -6 1.8 -7 -1.2 '
            + 'c-1.8 -5.4 0.2 -10.8 4.4 -13.2 z"/>'
            + '<path d="M-0.4 0.4 q2.6 -2.4 4.6 -1.6 q-1.8 2 -4.6 2.6 z"/></g>';
    }
    if (style === 'chust') s += '<g fill="#F4F7F8" opacity=".94">' + pods + '</g>';
    s += '<rect x="65" y="32" width="70" height="13" rx="3" fill="'+capD+'"/>';
    var band = '', bi;
    if (style === 'sanama'){
      // rows of tiny cross-stitch, the busiest of the four
      var cross = '', cx2, cy2;
      for (cy2 = 12; cy2 < 34; cy2 += 6){
        for (cx2 = 72; cx2 < 130; cx2 += 6.4){
          cross += 'M' + cx2 + ' ' + cy2 + ' l3 3 M' + (cx2 + 3) + ' ' + cy2 + ' l-3 3 ';
        }
      }
      s += '<path d="' + cross + '" stroke="' + (o.stitch || '#E8C25A') +
           '" stroke-width="1.15" opacity=".9" fill="none" stroke-linecap="round"/>';
      for (bi = 0; bi < 10; bi++)
        band += 'M' + (67 + bi * 6.8) + ' 43.4 l3.4 -4 l3.4 4 ';
      s += '<path d="' + band + '" stroke="#F4F7F8" stroke-width="1.35" fill="none" opacity=".9"/>';
    } else if (style === 'zardozi'){
      // gold couching: a medallion flanked by scrolls, no white at all
      var g2 = o.stitch || '#D9AE52';
      s += '<g fill="none" stroke="' + g2 + '" stroke-width="1.5" stroke-linecap="round">'
         + '<path d="M100 14 q7 5 0 11 q-7 -6 0 -11z"/>'
         + '<path d="M84 20 q5 4 0 8 q-5 -4 0 -8z"/><path d="M116 20 q-5 4 0 8 q5 -4 0 -8z"/>'
         + '<path d="M74 27 q4 3 0 6 q-4 -3 0 -6z"/><path d="M126 27 q-4 3 0 6 q4 -3 0 -6z"/></g>';
      for (bi = 0; bi < 9; bi++)
        band += 'M' + (68 + bi * 7.5) + ' 38.6 q3.75 6 7.5 0 ';
      s += '<path d="' + band + '" stroke="' + g2 + '" stroke-width="1.5" fill="none" opacity=".95"/>';
    } else if (style === 'chizma'){
      // outlined bodom medallions rather than solid pods
      s += '<g fill="none" stroke="' + (o.stitch || '#F2E3B0') + '" stroke-width="1.3">'
         + '<path d="M100 12 q6.5 6 0 12 q-6.5 -6 0 -12z"/>'
         + '<path d="M82 17 q5.5 5 0 10 q-5.5 -5 0 -10z"/><path d="M118 17 q-5.5 5 0 10 q5.5 -5 0 -10z"/>'
         + '<circle cx="100" cy="18" r="1.8"/></g>';
      for (bi = 0; bi < 12; bi++)
        band += 'M' + (66.5 + bi * 5.7) + ' 41.8 h3.4 ';
      s += '<path d="' + band + '" stroke="#F4F7F8" stroke-width="1.6" fill="none" opacity=".9"/>';
    } else {
      // Sixteen arches, the traditional count — described as a fortress
      // protecting the wearer. Not an arbitrary number.
      var arcs = '';
      for (i = 0; i < 16; i++) arcs += 'M' + (66.5 + i * 4.25) + ' 42.6 q2.125 -4.6 4.25 0 ';
      s += '<path d="'+arcs+'" stroke="#F4F7F8" stroke-width="1.3" fill="none" opacity=".92"/>';
    }
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

  // A beard is what separates a grown man from a round-faced boy at this size —
  // three lengths so ten bearded figures do not read as ten copies.
  if (o.beard && !o.fem){
    var bc = o.beardc || '#4B4149', bd = o.beard;
    var drop = bd === 'long' ? 102 : (bd === 'short' ? 90 : 96);
    s += '<path d="M72 57 C72 ' + drop + ' 84 ' + (drop + 2) + ' 100 ' + (drop + 2)
       + ' C116 ' + (drop + 2) + ' 128 ' + drop + ' 128 57 '
       + 'C124 74 114 79 100 79 C86 79 76 74 72 57z" fill="'+bc+'"/>';
    s += '<path d="M87 64 q13 -6 26 0 q-4 8 -13 8 q-9 0 -13 -8z" fill="'+bc+'"/>';
  }
  // Expression. Falls back to the face every figure used to share, so a figure
  // drawn without a TM_FACE entry still comes out as it did before.
  var f = o.face || {};
  var eye = TM_EYE[f.eyes] || TM_EYE.round;
  var brow = TM_BROW[f.brow] || TM_BROW.soft;
  var bpath = brow.d.split('|');
  var blush = f.blush == null ? 0.28 : f.blush;
  s += eye(88) + eye(112);
  s += '<g stroke="'+INK+'" stroke-width="'+brow.w+'" fill="none" stroke-linecap="round">'
     + '<path d="'+bpath[0]+'"/><path d="'+bpath[1]+'"/></g>';
  // An ink mouth inside an ink-dark beard is invisible, which is why eight of
  // the ten used to look alike no matter what the mouth did — only the two
  // unbearded faces ever showed it. On a bearded face the mouth is the gap in
  // the beard, so it is drawn light and reads at card size.
  var mouth = TM_MOUTH[f.mouth] || TM_MOUTH.smile;
  var mc = (o.beard && !o.fem) ? '#F7F0E4' : INK;
  s += mouth.fill
     ? '<path d="'+mouth.d+'" fill="'+mc+'"/>'
     : '<path d="'+mouth.d+'" stroke="'+mc+'" stroke-width="'+mouth.w+'" fill="none" stroke-linecap="round"/>';
  s += '<ellipse cx="80" cy="67" rx="5.5" ry="3.5" fill="#E0805C" opacity="'+blush+'"/>'
     + '<ellipse cx="120" cy="67" rx="5.5" ry="3.5" fill="#E0805C" opacity="'+blush+'"/>';

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
  'ES|E': {build:'normal', crown:'tall', hem:'long', dstyle:'zardozi', stitch:'#E8C25A', pose:'raise', beard:'full', beardc:'#332E38', head:'doppi', robe:'#12718F', robeD:'#0B5670', sleeve:'#0E6280', sash:'#C08A2E', prop:'compass'},
  'E|C':  {fem:true, build:'stocky', crown:'low',  hem:'short', dstyle:'chust', pose:'greet', beard:'short', beardc:'#4E4038', cap:'#141C33', capD:'#0B1124', head:'romol', scarf:'#1B7E9C', scarfD:'#0B5670', robe:'#2A94B4', robeD:'#17708C', sleeve:'#1E829F', sash:'#C08A2E', prop:'clipboard'},
  'ES|O': {build:'narrow', crown:'mid',  hem:'long', dstyle:'chizma', stitch:'#E8D9A8', pose:'rest', beard:'full', beardc:'#8C8794', head:'doppi', cap:'#3A2C63', capD:'#2B2049', robe:'#7E5FB8', robeD:'#5D4490', sleeve:'#6E509F', sash:'#C9A227', prop:'telescope'},
  'E|O':  {fem:true, build:'narrow', crown:'tall', hem:'short', dstyle:'sanama', stitch:'#F2C46A', pose:'greet', beard:'short', beardc:'#463A46', cap:'#2B2049', capD:'#1E1636', head:'hair',  hair:'#3A2F42', band:'#C08A2E', robe:'#9878CC', robeD:'#725598', sleeve:'#8567B8', sash:'#C9A227', prop:'palette'},
  'O|C':  {build:'normal', crown:'tall', hem:'normal', dstyle:'zardozi', stitch:'#D9AE52', pose:'rest', beard:'long', beardc:'#6E6672', head:'doppi', cap:'#2B2049', capD:'#1E1636', robe:'#6B54A0', robeD:'#4E3C78', sleeve:'#5D4890', sash:'#C08A2E', prop:'book'},
  'ES|A': {build:'stocky', crown:'mid',  hem:'long', dstyle:'chust', pose:'greet', beard:'full', beardc:'#6A5140', cap:'#173F35', capD:'#0E2C24', head:'romol', scarf:'#2E8B6B', scarfD:'#1F6650', robe:'#3FA07C', robeD:'#2A7660', sleeve:'#348B6E', sash:'#C08A2E', prop:'piyola'},
  'E|A':  {build:'stocky', crown:'tall', hem:'normal', dstyle:'sanama', stitch:'#7FD8B4', pose:'raise', beard:'short', beardc:'#8A6A4E', head:'doppi', robe:'#2E8B6B', robeD:'#1F6650', sleeve:'#277A5E', sash:'#C9A227', prop:'doira'},
  'O|A':  {build:'narrow', crown:'low',  hem:'normal', dstyle:'chizma', stitch:'#BFE8D4', pose:'rest', beard:'full', beardc:'#4A3B33', cap:'#1D4A3D', capD:'#12352B', head:'hair',  hair:'#2F2A35', robe:'#57A88A', robeD:'#3B8068', sleeve:'#4A9679', sash:'#7E5FB8', prop:'sprout'},
  // The two gold robes need a trim that is not also gold, or the braid disappears
  // into the cloth. Ivory braid on a gold chopon is the traditional pairing.
  'ES|C': {build:'normal', crown:'low',  hem:'long', dstyle:'chust', pose:'rest', beard:'long', beardc:'#A39CA0', head:'doppi', cap:'#143F4E', capD:'#0C2F3C', robe:'#C08A2E', robeD:'#946420', sleeve:'#AC7727', sash:'#0F6E8C', gold:'#F5EAD0', goldD:'#B9945A', prop:'rook'},
  'A|C':  {build:'stocky', crown:'low',  hem:'normal', dstyle:'zardozi', stitch:'#F0DCA8', pose:'greet', beard:'full', beardc:'#7B4A34', cap:'#5A2A1E', capD:'#40190F', head:'romol', scarf:'#B2503A', scarfD:'#8B3A28', robe:'#D9A544', robeD:'#A97D2A', sleeve:'#C69235', sash:'#0F6E8C', gold:'#F5EAD0', goldD:'#B9945A', prop:'non'}
};

// Approved raster characters. The other nine continue through the original
// vector renderer until their one-by-one review is complete.
// WebP, not PNG: the source art is ~500 KB apiece as PNG, which arrived a full
// two seconds after the rest of the hero scene had drawn, so the row appeared
// with holes in it and then filled in. q95 WebP is a quarter of that and the
// difference is invisible at the size these render.
var TM_RASTER_ART = {
  'E|C': 'assets/characters/gayratli-tashkilotchi.webp',
  'E|A': 'assets/characters/jamoaning-yuragi.webp',
  'ES|C': 'assets/characters/barqaror-strateg.webp',
  'ES|E': 'assets/characters/xotirjam-yetakchi.webp',
  'ES|O': 'assets/characters/xotirjam-kashfiyotchi.webp',
  'E|O': 'assets/characters/gayratli-ijodkor.webp',
  'O|C': 'assets/characters/ijodkor-strateg.webp',
  'ES|A': 'assets/characters/ishonchli-dost.webp',
  'O|A': 'assets/characters/ijodkor-insonparvar.webp'
};

// Where the <image> sits inside the shared 200x250 box.
//
// The default assumes the artwork is drawn on a 0.800 canvas like the box, so it
// fills it exactly. Art delivered on a taller canvas does NOT: xMidYMid meet
// fits it by height and centres it, which shrinks the figure and lifts its feet
// clear of the line every other character stands on -- Barqaror Strateg arrived
// at 1024x1536 (0.667) and rendered visibly smaller than the figure beside him,
// floating about 15 units above the ground.
//
// Fixing that by re-canvassing the PNG would mean altering approved artwork, so
// the placement moves instead: the numbers below scale and offset the image so
// the FIGURE inside it -- not the canvas around it -- lands in the same band as
// everyone else. Measured from the alpha channel, not guessed. Anything without
// an entry keeps the old behaviour exactly, which is what keeps an approval from
// disturbing the characters already signed off.
var TM_RASTER_FIT_DEFAULT = {x: 0, y: 0, w: 200, h: 250};
var TM_RASTER_FIT = {
  // Both delivered on a 1024x1536 canvas. Each lands its figure at top 8.25 /
  // bottom 242.0 -- the same band as Jamoaning Yuragi, which fills its box
  // exactly and is the reference the others are matched to. x differs because
  // each figure sits differently within its own canvas.
  'ES|C': {x: -1.6, y: -4.0, w: 176.3, h: 264.4},
  'ES|E': {x: 17.1, y: -3.8, w: 176.6, h: 265.0},
  // Topmost ink here is the raised astrolabe, so the y that puts his feet on the
  // shared line is also what keeps the astrolabe from being cut off at y=0.
  'ES|O': {x: 7.3, y: -2.5, w: 174.6, h: 261.9},
  // Her flowing robe makes this figure 84% of its canvas width where the others
  // are 60-75%, so she reads wider than her neighbours. That is the artwork, not
  // the placement: matching on height is what keeps every character the same
  // stature with its feet on one line, and matching on width instead would have
  // made her shorter than everyone else.
  'E|O': {x: 17.6, y: -2.9, w: 175.5, h: 263.2},
  // Topmost ink is the turban plume rather than the head, so the figure reaches
  // higher in its canvas than the others and needs a positive y to sit right.
  'O|C': {x: 18.0, y: 2.2, w: 171.3, h: 257.0},
  // Narrowest figure in the set: she stands square with her arms in, filling
  // 48% of her canvas width where G'ayratli Ijodkor's robe fills 84%. Height is
  // still the invariant, so she reads slimmer than her neighbours rather than
  // shorter -- which is the artwork, not the fit.
  'ES|A': {x: -2.8, y: -5.6, w: 175.4, h: 263.0},
  'O|A': {x: 22.7, y: -8.6, w: 175.6, h: 263.4}
};

function tmAssetPath(path){
  // characters.js is shared from the repository root. Runtime-generated markup
  // on /ru/ and /en/ pages must climb back to that root; build-time generators
  // have no document and localize the same path themselves.
  try {
    var lang = document.documentElement.getAttribute('lang');
    if (lang === 'ru' || lang === 'en') return '../' + path;
  } catch (e) {}
  return path;
}

function charRasterSrc(key){
  return TM_RASTER_ART[key] ? tmAssetPath(TM_RASTER_ART[key]) : '';
}

function shallowCopy(o, over){
  var out = {}, k;
  for (k in o) out[k] = o[k];
  for (k in over) out[k] = over[k];
  return out;
}

var TM_UID = 0;
// width/height are required for the canvas share card to rasterise this in Firefox.
function charSvg(key, alt){
  var o = TM_ART[key]; if (!o) return '';
  // Per-INSTANCE, not per-key: a page can draw the same character more than once
  // (the hero scene and a vignette both use O|C), and two <pattern> elements
  // sharing an id is invalid HTML.
  //
  // Counted before the raster branch on purpose. When it sat after, approving a
  // character shifted the counter for every figure drawn after it, so the ids in
  // all thirty generated pages renumbered and the diff for a one-character change
  // touched two dozen unrelated files. The ids are internal and always emitted
  // beside the url(#…) that uses them, so the churn was harmless — just noise
  // that hid the real change.
  var uid = key.replace(/[^A-Za-z0-9]/g, '-').toLowerCase() + '-' + (++TM_UID);
  var raster = charRasterSrc(key);
  if (raster) {
    var f = TM_RASTER_FIT[key] || TM_RASTER_FIT_DEFAULT;
    return '<svg xmlns="http://www.w3.org/2000/svg" width="200" height="250" viewBox="0 0 200 250" '
         + 'role="img" aria-label="' + (alt || '') + '">'
         + '<image href="' + raster + '" x="' + f.x + '" y="' + f.y + '" '
         + 'width="' + f.w + '" height="' + f.h + '" '
         + 'preserveAspectRatio="xMidYMid meet"/></svg>';
  }
  var a = {}; for (var k in o) a[k] = o[k];
  a.prop = TM_PROPS[o.prop] || '';
  a.face = TM_FACE[key] || {};
  a.uid = uid;
  return '<svg xmlns="http://www.w3.org/2000/svg" width="200" height="250" viewBox="0 0 200 250" '
       + 'role="img" aria-label="' + (alt || '') + '">' + tmFigure(a) + '</svg>';
}
