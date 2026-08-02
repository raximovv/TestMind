/**
 * TestMind — Google Sheet collector + guide-email sender.
 *
 * WHAT IT DOES
 *  - Logs every submission as a row (unchanged from before).
 *  - status = "lead": when a student typed their email to ask for the guide, it now
 *    ALSO emails them their result AND attaches the 8-page PDF guide, fetched from
 *    SITE_URL/guides/<slug>.pdf. If that fetch fails the email still goes out with
 *    a download link, so nobody is left empty-handed.
 *
 * NOTE: the PDF must be live on the site before this can attach it. Re-run
 * `sendTestEmail` after a site deploy to confirm the attachment arrives.
 *
 * SAFETY
 *  - The email CONTENT lives in this file (the GUIDES object below), keyed by the
 *    archetype name. The website only sends an email + an archetype name; it can
 *    never make this script email arbitrary text, so the open endpoint can't be
 *    turned into a spam cannon.
 *  - A given address gets a given archetype's email only once (dedupe by scanning
 *    prior "lead" rows). Free Gmail also caps you at ~100 sends/day.
 *
 * DEPLOY (do this after pasting)
 *  1. Save.
 *  2. Run `sendTestEmail` once from the editor — Google will ask you to authorize
 *     sending mail; approve it. It sends a sample to your own address so you can
 *     see the result before students do.
 *  3. Deploy -> Manage deployments -> (edit the existing Web App) -> Version: New
 *     version -> Deploy. The URL stays the same, so the site needs no change.
 *  Set SEND_GUIDE_EMAIL = false to keep logging but stop sending.
 */

var SHEET_NAME = 'responses';
var HEADERS = ['server_time', 'id', 'status', 'age', 'answered', 'total',
               'duration_sec', 'device', 'ES', 'E', 'O', 'A', 'C',
               'archetype', 'version', 'email', 'answers'];

var SEND_GUIDE_EMAIL = true;
var SITE_URL = 'https://raximovv.github.io/TestMind';
var FROM_NAME = 'TestMind';
// Bump this whenever you change this file, then open the /exec URL: it reports
// the version, so you can tell in one second whether your new code is really
// deployed instead of guessing from a delivered email.
var SCRIPT_VERSION = 'pdf-v2';

// Four archetypes lost their adjective ("Xotirjam Yetakchi" -> "Yetakchi").
// A student who loaded the page before that deploy still has the old name in
// their tab and will post it hours later, and every row already in the sheet
// carries the old name too -- so the old spelling has to keep resolving. The
// guide slugs did not change, so this only affects the lookup, not the PDFs.
//
// It also carries the Russian and English names. The site posts whatever the
// reader's page called the archetype, so since the RU/EN launch a Russian
// student's row has said "Лидер" -- which matched no key here, so the guide
// email was silently never sent to them. GUIDES stays Uzbek-keyed because the
// PDFs are Uzbek; this only decides which one to send.
var ARCH_ALIASES = {
  "Лидер":                      "Yetakchi",
  "Leader":                     "Yetakchi",
  "Xotirjam Yetakchi":          "Yetakchi",
  "Спокойный Лидер":            "Yetakchi",
  "Calm Leader":                "Yetakchi",
  "Организатор":                "Tashkilotchi",
  "Organiser":                  "Tashkilotchi",
  "Gʻayratli Tashkilotchi":     "Tashkilotchi",
  "Энергичный Организатор":     "Tashkilotchi",
  "Driven Organiser":           "Tashkilotchi",
  "Исследователь":              "Kashfiyotchi",
  "Explorer":                   "Kashfiyotchi",
  "Xotirjam Kashfiyotchi":      "Kashfiyotchi",
  "Спокойный Исследователь":    "Kashfiyotchi",
  "Calm Explorer":              "Kashfiyotchi",
  "Творец":                     "Ijodkor",
  "Creator":                    "Ijodkor",
  "Gʻayratli Ijodkor":          "Ijodkor",
  "Энергичный Творец":          "Ijodkor",
  "Spirited Creator":           "Ijodkor",
  "Дальновидный":               "Uzoqni Koʻzlovchi",
  "Visionary":                  "Uzoqni Koʻzlovchi",
  "Ijodkor Strateg":            "Uzoqni Koʻzlovchi",
  "Творческий Стратег":         "Uzoqni Koʻzlovchi",
  "Creative Strategist":        "Uzoqni Koʻzlovchi",
  "Надёжный Друг":              "Ishonchli Doʻst",
  "Trusted Friend":             "Ishonchli Doʻst",
  "Душа Команды":               "Jamoaning Yuragi",
  "Heart of the Group":         "Jamoaning Yuragi",
  "Добрый Человек":             "Mehribon Inson",
  "Kind Soul":                  "Mehribon Inson",
  "Ijodkor Insonparvar":        "Mehribon Inson",
  "Творческий Гуманист":        "Mehribon Inson",
  "Creative Humanitarian":      "Mehribon Inson",
  "Устойчивый Стратег":         "Barqaror Strateg",
  "Steady Strategist":          "Barqaror Strateg",
  "Надёжная Опора":             "Ishonchli Tayanch",
  "Dependable Anchor":          "Ishonchli Tayanch"
};
function canonicalArch_(name){
  return ARCH_ALIASES[name] || name;
}

// Baked email content, one entry per archetype (generated from characters.js).
var GUIDES = {
  "Yetakchi": {
    "slug": "xotirjam-yetakchi",
    "fam": "Yetakchilar",
    "color": "#0F6E8C",
    "lines": [
      "Vaziyat qizib ketganda ham ovozingizni koʻtarmaysiz — shuning uchun odamlar sizga quloq soladi.",
      "Guruh adashib qolganda yoʻnalishni koʻrsatadigan odam odatda siz boʻlasiz."
    ],
    "strength": "bosim ostida toʻgʻri qaror qabul qilish.",
    "watch": "Xotirjamligingiz baʼzan befarqlikdek koʻrinadi. Yaqinlaringiz sizdan koʻproq hissiyot kutayotganini sezmay qolmang.",
    "figure": {
      "who": "Bahouddin Naqshband",
      "years": "1318–1389",
      "why": "Odamlarni majburlab emas, oʻz namunasi bilan ergashtirgan."
    }
  },
  "Tashkilotchi": {
    "slug": "gayratli-tashkilotchi",
    "fam": "Yetakchilar",
    "color": "#0F6E8C",
    "lines": [
      "Gapdan ishga tez oʻtasiz — rejani boshqalar hali muhokama qilayotganda siz boshlab yuborgan boʻlasiz.",
      "Atrofdagilarni ham harakatga sola olasiz."
    ],
    "strength": "gʻoyani haqiqatga aylantirish.",
    "watch": "Tez boshlaganingiz uchun baʼzan boshqalarning fikrini soʻrashni unutasiz. Eng yaxshi gʻoya doim sizniki boʻlmasligi mumkin.",
    "figure": {
      "who": "Nodirabegim",
      "years": "1792–1842",
      "why": "Qoʻqonda adabiy muhitni uyushtirgan, madrasa va masjidlar qurdirgan."
    }
  },
  "Kashfiyotchi": {
    "slug": "xotirjam-kashfiyotchi",
    "fam": "Ijodkorlar",
    "color": "#6B4FA8",
    "lines": [
      "Notanish narsani koʻrsangiz avval sinab koʻrasiz, keyin fikr bildirasiz.",
      "Lekin sarguzashtga koʻzni yumib emas, sovuqqonlik bilan kirasiz."
    ],
    "strength": "notanish yoʻlni xotirjam tekshirib koʻrish.",
    "watch": "Yangi narsaga tez qiziqib, boshlagan ishingizni yarmida tashlab qoʻyish xavfi bor. Bittasini oxirigacha olib borib koʻring.",
    "figure": {
      "who": "Abu Rayhon Beruniy",
      "years": "973–1048",
      "why": "Notanish oʻlkalarni ham, notanish fanlarni ham sovuqqonlik bilan oʻrgangan."
    }
  },
  "Ijodkor": {
    "slug": "gayratli-ijodkor",
    "fam": "Ijodkorlar",
    "color": "#6B4FA8",
    "lines": [
      "Gʻoyalaringiz tugamaydi va ularni odamlarga gapirib berishni yaxshi koʻrasiz.",
      "Bir gʻoyani tushuntira boshlasangiz, tinglayotgan odam ham qiziqib qoladi."
    ],
    "strength": "yangi gʻoyani odamlarga yuqtirish.",
    "watch": "Gʻoya koʻp, vaqt kam. Hammasini birdan boshlasangiz, hech biri tugamasligi mumkin.",
    "figure": {
      "who": "Zebunniso Begim",
      "years": "1638–1702",
      "why": "Boburiylar xonadonidan; «Maxfiy» taxallusi bilan butun bir devon yozgan."
    }
  },
  "Uzoqni Koʻzlovchi": {
    "slug": "ijodkor-strateg",
    "fam": "Ijodkorlar",
    "color": "#6B4FA8",
    "lines": [
      "Yangi yechim topasiz — va uni oxiriga ham yetkazasiz.",
      "Gʻoyani daftarda qoldirmaysiz — jadvalga, qadamlarga aylantirasiz."
    ],
    "strength": "gʻoyani aniq tizimga solish.",
    "watch": "Hammasini mukammal qilishga urinish sizni sekinlashtiradi. Baʼzan «yetarlicha yaxshi» ham haqiqiy natija.",
    "figure": {
      "who": "Mirzo Ulugʻbek",
      "years": "1394–1449",
      "why": "Yulduzlarni sanashni orzu qilgan, rasadxona qurgan va 1018 tasini roʻyxatga olgan."
    }
  },
  "Ishonchli Doʻst": {
    "slug": "ishonchli-dost",
    "fam": "Gʻamxoʻrlar",
    "color": "#237A5E",
    "lines": [
      "Odamlar sizga sirini aytadi, chunki yoningizda oʻzini xavfsiz his qiladi.",
      "Kimdir xafa boʻlsa, koʻpincha birinchi boʻlib siz sezasiz."
    ],
    "strength": "boshqalarni tinchlantira olish.",
    "watch": "Boshqalarga yordam berib, oʻzingizga vaqt qoldirmaslik oson. «Yoʻq» deyishni ham oʻrganing.",
    "figure": {
      "who": "Jahonotin Uvaysiy",
      "years": "1781–1845",
      "why": "Shoira va ustoz; Nodirabegimga sheʼr ilmini oʻrgatgan."
    }
  },
  "Jamoaning Yuragi": {
    "slug": "jamoaning-yuragi",
    "fam": "Gʻamxoʻrlar",
    "color": "#237A5E",
    "lines": [
      "Siz kirgan xonada suhbat oʻzidan-oʻzi boshlanib ketadi.",
      "Chetda qolgan odamni sezasiz va yoningizga chaqirasiz."
    ],
    "strength": "odamlarni birlashtirish.",
    "watch": "Hamma bilan yaxshi boʻlishga urinib, oʻz fikringizni aytmay qoʻyishingiz mumkin. Sizning fikringiz ham muhim.",
    "figure": {
      "who": "Alisher Navoiy",
      "years": "1441–1501",
      "why": "Oʻz tilida yozib, butun bir xalqni bir-biriga yaqinlashtirgan."
    }
  },
  "Mehribon Inson": {
    "slug": "ijodkor-insonparvar",
    "fam": "Gʻamxoʻrlar",
    "color": "#237A5E",
    "lines": [
      "Yangi gʻoyalar va odamlarga gʻamxoʻrlik sizda birga yashaydi.",
      "Muammoni koʻrganingizda avval odamlar haqida oʻylaysiz."
    ],
    "strength": "foydali va insoniy yechim topish.",
    "watch": "Boshqalarning muammosini oʻzingizniki qilib olasiz. Hammasini yolgʻiz hal qilishingiz shart emas.",
    "figure": {
      "who": "Abdulla Avloniy",
      "years": "1878–1934",
      "why": "Adabiyot, teatr, jurnalistika va taʼlimni xalq manfaatiga xizmat qildirgan."
    }
  },
  "Barqaror Strateg": {
    "slug": "barqaror-strateg",
    "fam": "Tayanchlar",
    "color": "#A2731F",
    "lines": [
      "Reja tuzasiz va rejadan chalgʻimaysiz.",
      "Boshqalar taslim boʻlgan joyda siz hali ishlab turasiz."
    ],
    "strength": "uzoq masofaga chidash.",
    "watch": "Reja buzilganda qiynalasiz. Baʼzan yoʻlni oʻzgartirish — magʻlubiyat emas.",
    "figure": {
      "who": "Muhammad al-Xorazmiy",
      "years": "783–850",
      "why": "Murakkab masalani aniq qadamlarga boʻlgan — «algoritm» soʻzi uning nomidan qolgan."
    }
  },
  "Ishonchli Tayanch": {
    "slug": "ishonchli-tayanch",
    "fam": "Tayanchlar",
    "color": "#A2731F",
    "lines": [
      "Vaʼda berishdan oldin oʻylaysiz — chunki bergan vaʼdangizni bajarasiz.",
      "Shuning uchun muhim ish koʻpincha aynan sizga topshiriladi."
    ],
    "strength": "soʻzida turish.",
    "watch": "Hamma ishni oʻz zimmangizga olib, ortiqcha yuk koʻtarib yurasiz. Yordam soʻrash ham kuch.",
    "figure": {
      "who": "Imom Buxoriy",
      "years": "810–870",
      "why": "Har bir rivoyatni qatʼiy tekshirib, faqat ishonchlisini kitobiga kiritgan."
    }
  }
};

/** Run once from the editor to create the sheet + header row. */
function setup(){
  getSheet_();
  SpreadsheetApp.getActiveSpreadsheet().toast('Sheet "' + SHEET_NAME + '" is ready.');
}

/** Run once from the editor to authorize mail sending + preview the email. */
function sendTestEmail(){
  var me = Session.getActiveUser().getEmail();
  sendGuideEmail_(me, "Ishonchli Doʻst");
  Logger.log('Sent a sample email (' + "Ishonchli Doʻst" + ') to ' + me);
}

function getSheet_(){
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName(SHEET_NAME) || ss.insertSheet(SHEET_NAME);
  if (sh.getLastRow() === 0){
    sh.appendRow(HEADERS);
    sh.getRange(1, 1, 1, HEADERS.length).setFontWeight('bold');
    sh.setFrozenRows(1);
  }
  return sh;
}

function doPost(e){
  var lock = LockService.getScriptLock();
  var toSend = null;
  try {
    lock.waitLock(20000);

    var d = {};
    if (e && e.postData && e.postData.contents) d = JSON.parse(e.postData.contents);

    var sh = getSheet_();
    sh.appendRow([
      new Date(),
      String(d.id || ''),
      String(d.status || ''),
      d.age === 0 || d.age ? d.age : '',
      d.answered === 0 || d.answered ? d.answered : '',
      d.total || '',
      d.durationSec === 0 || d.durationSec ? d.durationSec : '',
      String(d.device || ''),
      d.ES === 0 || d.ES ? d.ES : '',
      d.E  === 0 || d.E  ? d.E  : '',
      d.O  === 0 || d.O  ? d.O  : '',
      d.A  === 0 || d.A  ? d.A  : '',
      d.C  === 0 || d.C  ? d.C  : '',
      String(d.archetype || ''),
      String(d.v || ''),
      String(d.email || ''),
      "'" + String(d.answers || '')      // leading quote keeps Sheets from mangling it
    ]);

    // Decide whether to email — but actually send OUTSIDE the lock (below), so a
    // slow send never blocks another student's submission.
    if (SEND_GUIDE_EMAIL && String(d.status || '') === 'lead'){
      var email = String(d.email || '').trim();
      var arch  = canonicalArch_(String(d.archetype || '').trim());
      if (looksLikeEmail_(email) && GUIDES[arch] && !alreadySentBefore_(sh, email, arch)){
        toSend = { email: email, arch: arch };
      }
    }
  } catch (err) {
    return json_({ ok: false, error: String(err) });
  } finally {
    try { lock.releaseLock(); } catch (ignore) {}
  }

  // A failed send must never turn the whole request into an error.
  if (toSend){
    try { sendGuideEmail_(toSend.email, toSend.arch); } catch (mailErr) {}
  }
  return json_({ ok: true });
}

// True if this email already received this archetype in an EARLIER lead row.
// (The current submission was just appended, so a count above 1 means a prior one.)
function alreadySentBefore_(sh, email, arch){
  var last = sh.getLastRow();
  if (last < 2) return false;
  var vals = sh.getRange(2, 1, last - 1, HEADERS.length).getValues();
  var iStatus = HEADERS.indexOf('status');
  var iArch   = HEADERS.indexOf('archetype');
  var iEmail  = HEADERS.indexOf('email');
  var seen = 0;
  for (var r = 0; r < vals.length; r++){
    if (String(vals[r][iStatus]) === 'lead'
        && String(vals[r][iEmail]).trim().toLowerCase() === email.toLowerCase()
        && canonicalArch_(String(vals[r][iArch]).trim()) === arch){
      seen++;
      if (seen > 1) return true;
    }
  }
  return false;
}

function looksLikeEmail_(v){ return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v); }

function sendGuideEmail_(email, archName){
  var opts = {
    to: email,
    name: FROM_NAME,
    subject: '«' + archName + '» — TestMind natijangiz va qoʻllanmangiz',
    htmlBody: guideEmailHtml_(archName)
  };
  // Attach the 8-page PDF. If fetching it fails for any reason the email must
  // still go out — the body always carries the download link as well.
  var pdf = guidePdf_(archName);
  if (pdf) opts.attachments = [pdf];
  MailApp.sendEmail(opts);
}

function guideUrl_(archName){
  return SITE_URL + '/guides/' + GUIDES[archName].slug + '.pdf';
}

/**
 * Run this from the editor when the email arrives WITHOUT its attachment.
 * Deliberately has no try/catch: guidePdf_ hides failures so a broken fetch can
 * never stop the email, but that also hides WHY. This one lets the error (or
 * the authorization prompt for external requests) reach you.
 */
function testGuideFetch(){
  var url = guideUrl_('Uzoqni Koʻzlovchi');
  var r = UrlFetchApp.fetch(url, { muteHttpExceptions: true });
  var n = r.getBlob().getBytes().length;
  Logger.log('URL   : ' + url);
  Logger.log('HTTP  : ' + r.getResponseCode());
  Logger.log('bytes : ' + n);
  Logger.log(r.getResponseCode() === 200 && n > 10000
    ? 'OK — attachments will work.'
    : 'PROBLEM — the PDF could not be fetched.');
}

function guidePdf_(archName){
  try {
    var r = UrlFetchApp.fetch(guideUrl_(archName), { muteHttpExceptions: true });
    if (r.getResponseCode() !== 200) return null;
    var blob = r.getBlob();
    if (blob.getBytes().length < 10000) return null;   // not a real PDF
    return blob.setName('TestMind-' + GUIDES[archName].slug + '.pdf');
  } catch (err) {
    return null;
  }
}

function esc_(s){
  return String(s).replace(/[&<>"]/g, function(c){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];
  });
}

// Table layout + inline styles only — Gmail strips <style>, external CSS and SVG.
function guideEmailHtml_(name){
  var g = GUIDES[name];
  var c = g.color, soft = '#F1F6F7';
  var lines = '';
  for (var i = 0; i < g.lines.length; i++){
    lines += '<p style="margin:0 0 12px;font-size:16px;line-height:1.55;color:#152730">' + esc_(g.lines[i]) + '</p>';
  }
  return ''
  + '<div style="margin:0;padding:0;background:#EEF3F4">'
  + '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#EEF3F4;padding:24px 12px">'
  + '<tr><td align="center">'
  + '<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#ffffff;border-radius:14px;overflow:hidden;font-family:Arial,Helvetica,sans-serif">'
  + '<tr><td style="height:6px;background:' + c + '"></td></tr>'
  + '<tr><td style="padding:26px 32px 8px">'
  + '<div style="font-family:Georgia,serif;font-weight:bold;font-size:22px;color:' + c + '">TestMind</div>'
  + '<div style="font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:' + c + ';margin-top:14px">' + esc_(g.fam) + '</div>'
  + '<div style="font-family:Georgia,serif;font-size:30px;font-weight:bold;color:' + c + ';line-height:1.15;margin:4px 0 16px">' + esc_(name) + '</div>'
  + lines
  + '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:18px 0 0"><tr>'
  + '<td style="background:' + soft + ';border-radius:10px;padding:14px 16px;font-size:15px;line-height:1.5;color:#152730">'
  + '<b style="color:' + c + '">Kuchli tomoningiz:</b> ' + esc_(g.strength) + '</td></tr></table>'
  + '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:10px 0 0"><tr>'
  + '<td style="background:#FBF3E4;border:1px solid #EBDCBB;border-radius:10px;padding:14px 16px;font-size:15px;line-height:1.5;color:#152730">'
  + '<b style="color:#8A6520">Eʼtibor bering:</b> ' + esc_(g.watch) + '</td></tr></table>'
  + '<div style="margin:22px 0 0;padding-top:16px;border-top:1px solid #E2EBEC">'
  + '<div style="font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;color:#5B7078">Shu xususiyat kimda kuchli boʻlgan</div>'
  + '<div style="font-family:Georgia,serif;font-weight:bold;font-size:17px;color:' + c + ';margin-top:6px">' + esc_(g.figure.who)
  + ' <span style="font-family:Arial;font-weight:normal;font-size:13px;color:#5B7078">' + esc_(g.figure.years) + '</span></div>'
  + '<p style="margin:5px 0 0;font-size:14px;line-height:1.5;color:#5B7078">' + esc_(g.figure.why) + '</p></div>'
  + '<p style="margin:22px 0 14px;font-size:14px;line-height:1.55;color:#5B7078">Toʻliq qoʻllanmangiz — 8 sahifa — shu xatga <b>PDF fayl</b> sifatida biriktirilgan. Ochilmasa, quyidagi tugma orqali yuklab olishingiz mumkin.</p>'
  + '<a href="' + guideUrl_(name) + '" style="display:inline-block;background:' + c + ';color:#ffffff;text-decoration:none;font-size:15px;font-weight:bold;padding:12px 24px;border-radius:10px">Qoʻllanmani yuklab olish (PDF)</a>'
  + '<div style="margin-top:14px"><a href="' + SITE_URL + '/" style="color:' + c + ';font-size:14px">Saytga qaytish</a></div>'
  + '</td></tr>'
  + '<tr><td style="padding:22px 32px 26px;border-top:1px solid #E2EBEC;font-size:12px;line-height:1.6;color:#8A9AA0">'
  + 'Bu xatni oldingiz, chunki TestMind natijangizni koʻrgach, uni email orqali soʻradingiz.<br>'
  + 'Savollar: <a href="mailto:raximovrahim1@gmail.com" style="color:#8A9AA0">raximovrahim1@gmail.com</a><br>'
  + 'Natija maslahat xarakteriga ega — tibbiy yoki psixologik tashxis emas.'
  + '</td></tr>'
  + '</table></td></tr></table></div>';
}

/** Lets you sanity-check the deployment by opening the URL in a browser.
 *  `version` tells you WHICH code the Web App is actually serving — pasting new
 *  code is not enough, the deployment must be re-published as a NEW version, and
 *  without this stamp the only way to notice is to read a delivered email. */
function doGet(){
  return json_({ ok: true, version: SCRIPT_VERSION,
                 msg: 'TestMind collector is live. Post JSON here.' });
}

function json_(obj){
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
