# -*- coding: utf-8 -*-
"""Generates the four static TestMind pages so the nav and footer can never drift."""
import io, os

OUT = 'C:/Users/Asus/TestMind-site/'

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
           "%3Crect width='64' height='64' rx='14' fill='%230F6E8C'/%3E"
           "%3Cpath d='M15 34 Q15 11 32 11 Q49 11 49 34 Z' fill='%23fff'/%3E"
           "%3Crect x='13' y='38' width='38' height='11' rx='3.5' fill='%23fff'/%3E"
           "%3Cpath d='M32 16 q4 6 0 11 q-4 -5 0 -11z' fill='%230F6E8C'/%3E%3C/svg%3E")

SITE = 'https://testmind-minis.netlify.app'   # one line to change on the .uz domain

NAV_ITEMS = [('index.html', 'Bosh sahifa'), ('obrazlar.html', 'Obrazlar'),
             ('test.html', 'Shaxsiyat testi'),
             ('qanday-ishlaydi.html', 'Qanday ishlaydi'), ('savollar.html', 'Savollar')]


def head(title, desc):
    return u"""<!doctype html>
<html lang="uz">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:type" content="website">
<meta property="og:image" content="%s/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="%s">
<link rel="preload" href="fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="site.css">
</head>
<body>
""" % (title, desc, title, desc, SITE, FAVICON)


def nav(active):
    links = ''
    for href, label in NAV_ITEMS:
        cur = ' aria-current="page"' if href == active else ''
        links += u'\n    <a href="%s"%s>%s</a>' % (href, cur, label)
    return u"""<nav class="nav"><div class="wrap navin">
  <a class="brand" href="index.html">TestMind</a>
  <div class="navlinks">%s
  </div>
  <a class="btn sm" href="test.html" data-cta>Testni boshlash</a>
</div></nav>
""" % links


FOOTER = u"""<footer class="foot"><div class="wrap">
  <div class="footgrid">
    <div class="footcol"><h2>TestMind</h2><ul>
      <li><a href="index.html">Bosh sahifa</a></li>
      <li><a href="obrazlar.html">Oʻnta obraz</a></li>
      <li><a href="qanday-ishlaydi.html">Qanday ishlaydi</a></li>
    </ul></div>
    <div class="footcol"><h2>Test</h2><ul>
      <li><a href="test.html" data-cta>Testni boshlash</a></li>
      <li><a href="savollar.html">Koʻp beriladigan savollar</a></li>
    </ul></div>
    <div class="footcol"><h2>Maʼlumot</h2><ul>
      <li><a href="privacy.html">Maxfiylik</a></li>
      <li><a href="qanday-ishlaydi.html#model">Test qaysi modelga asoslangan</a></li>
      <li><a href="maktablar.html">Maktablar va ota-onalar uchun</a></li>
      <li><a href="ota-onalarga.html">Ota-onalarga xat (chop etish uchun)</a></li>
    </ul></div>
    <div class="footcol"><h2>Bogʻlanish</h2><ul>
      <li><a href="mailto:raximovrahim1@gmail.com">raximovrahim1@gmail.com</a></li>
    </ul>
      <div class="socrow" aria-hidden="true"><span class="soc" title="Telegram"><svg viewBox="0 0 24 24"><path fill="#fff" d="M9.78 18.65l.28-4.23 7.68-6.92c.34-.31-.07-.46-.52-.19L7.74 13.3 3.64 12c-.88-.25-.89-.86.2-1.3l15.97-6.16c.73-.33 1.43.18 1.15 1.3l-2.72 12.81c-.19.91-.74 1.13-1.5.71L12.6 16.3l-1.99 1.93c-.23.23-.42.42-.83.42z"/></svg></span><span class="soc" title="Instagram"><svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="4.6" fill="none" stroke="#fff" stroke-width="1.9"/><circle cx="12" cy="12" r="3.6" fill="none" stroke="#fff" stroke-width="1.9"/><circle cx="16.6" cy="7.4" r="1.15" fill="#fff"/></svg></span><span class="soc" title="Facebook"><svg viewBox="0 0 24 24"><path fill="#fff" d="M13.4 21v-7.1h2.38l.36-2.77H13.4V9.35c0-.8.22-1.35 1.38-1.35h1.47V5.52c-.25-.03-1.13-.11-2.15-.11-2.13 0-3.58 1.3-3.58 3.68v2.05H8.13v2.77h2.39V21z"/></svg></span><span class="soc" title="YouTube"><svg viewBox="0 0 24 24"><path fill="#fff" d="M21.58 8.2a2.47 2.47 0 0 0-1.74-1.75C18.3 6.03 12 6.03 12 6.03s-6.3 0-7.84.42A2.47 2.47 0 0 0 2.42 8.2 25.9 25.9 0 0 0 2 12a25.9 25.9 0 0 0 .42 3.8 2.47 2.47 0 0 0 1.74 1.75c1.54.42 7.84.42 7.84.42s6.3 0 7.84-.42a2.47 2.47 0 0 0 1.74-1.75A25.9 25.9 0 0 0 22 12a25.9 25.9 0 0 0-.42-3.8z"/><path fill="var(--lazur)" d="M10.05 14.85l5.2-2.85-5.2-2.85z"/></svg></span><span class="soc" title="TikTok"><svg viewBox="0 0 24 24"><path fill="#fff" d="M16.6 3c.28 1.9 1.35 3.16 3.4 3.32v2.4c-1.18.11-2.2-.27-3.4-.98v5.55c0 4.05-4.41 5.31-6.18 2.41-1.14-1.87-.44-5.15 3.23-5.28v2.53c-.28.05-.58.12-.85.22-.82.32-1.28 1.14-1.05 1.99.24.88 1.36 1.53 2.26.9.55-.38.7-1 .7-1.66V3z"/></svg></span></div></div>
  </div>
  <div class="footbar">
    <span>© 2026 TestMind</span>
    <span>Natija maslahat xarakteriga ega — tibbiy yoki psixologik tashxis emas.</span>
  </div>
</div></footer>
"""

SCRIPTS = u"""<script src="characters.js"></script>
<script src="site.js"></script>
</body>
</html>
"""

CLOSE = u"""<section class="close">
  <h2>Tayyormisiz?</h2>
  <p>7 daqiqa. Oʻnta obrazdan qaysi biri sizniki?</p>
  <a class="btn big" href="test.html" data-cta>Testni boshlash</a>
</section>
"""

# ---------------------------------------------------------------- home
HOME = u"""<header class="hero" id="top">
  <div style="text-align:center;padding:52px 20px 28px;max-width:760px;margin:0 auto">
    <h1>Siz qaysi obrazsiz?</h1>
    <p class="lead" style="font-size:clamp(16px,2.4vw,19px);margin-bottom:26px">
      50 ta savol, taxminan 7 daqiqa. Yakunida oʻnta obrazdan bittasi sizniki boʻladi —
      kuchli tomonlaringiz bilan birga.</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
      <a class="btn big" href="test.html" data-cta>Testni boshlash</a>
      <a class="btn big ghost" href="obrazlar.html">Obrazlarni koʻrish</a>
    </div>
    <p style="margin:16px 0 0;font-size:13.5px;color:var(--muted)">
      Bepul · Anonim · Roʻyxatdan oʻtish shart emas</p>
  </div>
  <div class="scene" id="scene" aria-hidden="true"></div>
  <p class="scenecap">Registon maydoni · Samarqand</p>
</header>

<section class="alt">
  <div class="wrap">
    <div class="center"><h2>Raqamlarda</h2>
      <p class="lead">TestMind endi ishga tushdi. Bu raqamlarni oʻsib borishini
        shu yerda ochiq koʻrsatib boramiz.</p></div>
    <div class="facts">
      <div class="fact"><div class="factn">0</div><div class="factl">topshirilgan test</div></div>
      <div class="fact"><div class="factn">0</div><div class="factl">bugun topshirilgan</div></div>
      <div class="fact"><div class="factn">0</div><div class="factl">ishtirok etgan maktab</div></div>
      <div class="fact"><div class="factn">0</div><div class="factl">shahar va tuman</div></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="panel">
      <div class="ptext">
        <span class="ptag">Oʻzingizni tushunib oling</span>
        <h2>Nega ayrim ishlar sizga oson, ayrimlari qiyin?</h2>
        <p>Test yakunida qandaydir ball emas, aniq bir obraz olasiz: siz qanday odamsiz,
           nima sizga kuch beradi va qaysi tomoningiz eng kuchli. Uni rasm qilib saqlab,
           doʻstlaringizga yuborishingiz mumkin.</p>
        <a class="btn" href="test.html" data-cta>Testni boshlash</a>
      </div>
      <div class="part" id="vg-result"></div>
    </div>

    <div class="panel flip">
      <div class="ptext">
        <span class="ptag">Boshqalarni tushunib oling</span>
        <h2>Doʻstingiz nega sizdan butunlay boshqacha?</h2>
        <p>Oʻnta obrazning hech biri boshqasidan yaxshi emas. Kimdir davrani jonlantiradi,
           kimdir jimgina eng yaxshi yechimni topadi. Buni bilsangiz, sinfdoshlaringiz bilan
           ham osonroq til topasiz.</p>
        <a class="btn ghost" href="obrazlar.html">Oʻnta obrazni koʻrish</a>
      </div>
      <div class="part" id="vg-others"></div>
    </div>

    <div class="panel">
      <div class="ptext">
        <span class="ptag">Kelajagingizni tanlang</span>
        <h2>Qaysi yoʻnalish sizga mos kelishi mumkin?</h2>
        <p>14–16 yosh — fan, yoʻnalish va kasb haqida oʻylay boshlaydigan payt.
           TestMind sizga javobni aytib bermaydi, lekin qaysi muhitda oʻzingizni
           erkin his qilishingizni koʻrsatadi.</p>
        <a class="btn ghost" href="qanday-ishlaydi.html">Qanday ishlaydi</a>
      </div>
      <div class="part" id="vg-future"></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="center"><h2>Nega TestMind?</h2>
      <p class="lead">Oʻzbek oʻsmirlari uchun, oʻzbek tilida.</p></div>
    <div class="why">
      <div class="wcard"><h3>Ilmiy modelga asoslangan</h3>
        <p>Savollar psixologiyada eng koʻp tekshirilgan «Katta beshlik» (Big Five)
           modelidan olingan.</p></div>
      <div class="wcard"><h3>Tabiiy oʻzbek tilida</h3>
        <p>Savollar tarjima emas — oʻsmirlar kundalik hayotda ishlatadigan tilda
           yozilgan.</p></div>
      <div class="wcard"><h3>Anonim</h3>
        <p>Test ismingizni ham, yoshingizni ham soʻramaydi. Javoblaringiz ismsiz
           saqlanadi va sizga bogʻlab boʻlmaydi — ular faqat testni yaxshilash uchun
           ishlatiladi.</p></div>
      <div class="wcard"><h3>Butunlay bepul</h3>
        <p>Toʻlov yoʻq, obuna yoʻq, roʻyxatdan oʻtish shart emas.</p></div>
    </div>
  </div>
</section>
""" + CLOSE

# ---------------------------------------------------------------- obrazlar
OBRAZLAR = u"""<header class="phead"><div class="wrap">
  <h1>Oʻnta obraz</h1>
  <p class="lead">Oʻnta obraz toʻrtta oilaga boʻlingan. Ular orasida «yomoni» yoʻq —
     shunchaki bir-biridan farq qiladi. Har biriga shu xususiyat bilan tanilgan oʻzbek
     tarixiy siymosi biriktirilgan. Batafsil oʻqish uchun obrazni bosing.</p>
</div></header>

<div id="bands"></div>
""" + CLOSE

# ---------------------------------------------------------------- how it works
QANDAY = u"""<header class="phead"><div class="wrap">
  <h1>Qanday ishlaydi</h1>
  <p class="lead">Uch qadam, ettita daqiqa — va natija darhol ekranda.</p>
</div></header>

<section><div class="wrap">
  <h2>Uch qadam</h2>
  <p class="lead">Boshidan oxirigacha telefonda ham bemalol bajariladi.</p>
  <div class="steps">
    <div class="step"><div class="stepn">1</div>
      <h3>Savollarga javob bering</h3>
      <p>50 ta jumla. Har biriga qanchalik qoʻshilishingizni beshta doiradan birini bosib
         belgilaysiz. Toʻgʻri yoki notoʻgʻri javob yoʻq.</p></div>
    <div class="step"><div class="stepn">2</div>
      <h3>Obrazingizni koʻring</h3>
      <p>Darhol ekranda: obrazingiz, uning tavsifi, eng kuchli tomoningiz va shu xususiyat
         bilan tanilgan tarixiy siymo. Rasm qilib saqlashingiz mumkin.</p></div>
    <div class="step"><div class="stepn">3</div>
      <h3>Batafsil tahlilni oling</h3>
      <p>Xohlasangiz email qoldiring — obrazingiz boʻyicha toʻliq qoʻllanmani tayyor
         boʻlishi bilan yuboramiz. Bu ixtiyoriy.</p></div>
  </div>
</div></section>

<section class="alt" id="model"><div class="wrap">
  <h2>Test qaysi modelga asoslangan?</h2>
  <p class="lead">Qisqacha va ochiq.</p>
  <div class="why">
    <div class="wcard"><h3>Katta beshlik (Big Five)</h3>
      <p>Psixologiyada eng keng tarqalgan va eng koʻp tekshirilgan shaxsiyat modeli.
         U odamni beshta xususiyat boʻyicha tasvirlaydi.</p></div>
    <div class="wcard"><h3>Beshta xususiyat</h3>
      <p>Hissiy barqarorlik, kirishimlilik, yangilikka ochiqlik, kelishuvchanlik va
         masʼuliyatlilik.</p></div>
    <div class="wcard"><h3>Obraz qanday chiqadi</h3>
      <p>Beshtadan eng kuchli ikkitasi olinadi va shu juftlikka mos obraz koʻrsatiladi.
         Shuning uchun jami oʻnta obraz bor.</p></div>
    <div class="wcard"><h3>Nimani vaʼda qilmaymiz</h3>
      <p>Bu tibbiy yoki psixologik tashxis emas va TestMind hali oʻzbek oʻsmirlarida
         alohida tekshirilmagan. Natijani maslahat sifatida qabul qiling.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <h2>Javoblaringiz bilan nima boʻladi?</h2>
  <p class="lead">Ochiq aytamiz.</p>
  <div class="why">
    <div class="wcard"><h3>Ismingiz soʻralmaydi</h3>
      <p>Test ism ham, yosh ham soʻramaydi. Tugmani bosasiz va birinchi savol chiqadi.</p></div>
    <div class="wcard"><h3>Javoblar ismsiz saqlanadi</h3>
      <p>Javoblaringiz ismingizsiz va emailingizsiz saqlanadi. Bu yozuvga alohida
         tasodifiy raqam beriladi, shuning uchun uni sizga bogʻlab boʻlmaydi. U faqat
         testni yaxshilash va oʻzbek oʻsmirlari uchun aniqroq qilish uchun kerak.</p></div>
    <div class="wcard"><h3>Qurilmangizda saqlanadi</h3>
      <p>Testni yarmida toʻxtatsangiz davom ettira olasiz. Natija chiqishi bilan
         javoblar oʻchiriladi.</p></div>
    <div class="wcard"><h3>Batafsil</h3>
      <p><a href="privacy.html">Maxfiylik sahifasini</a> oʻqing — u qisqa va sodda.</p></div>
  </div>
</div></section>
""" + CLOSE

# ---------------------------------------------------------------- faq
SAVOLLAR = u"""<header class="phead"><div class="wrap">
  <h1>Koʻp beriladigan savollar</h1>
  <p class="lead">Qisqa javoblar.</p>
</div></header>

<section><div class="wrap"><div class="faq">
  <details><summary>Test qancha vaqt oladi?</summary>
    <p>50 ta savol, taxminan 7 daqiqa. Yarmida toʻxtasangiz, javoblaringiz shu qurilmada
       saqlanadi va keyin davom ettira olasiz.</p></details>
  <details><summary>Natijam kimgadir koʻrinadimi?</summary>
    <p>Yoʻq. Test ismingizni ham, yoshingizni ham soʻramaydi va natijangiz hech kimga
       koʻrsatilmaydi. Javoblaringiz ismsiz saqlanadi: bu yozuvda ism ham,
       email ham boʻlmaydi va uni sizga bogʻlab boʻlmaydi. Batafsil:
       <a href="privacy.html">Maxfiylik</a>.</p></details>
  <details><summary>Bu test ilmiymi?</summary>
    <p>Savollar «Katta beshlik» modeliga asoslangan — bu psixologiyada eng keng tarqalgan
       va eng koʻp tekshirilgan shaxsiyat modeli. Lekin TestMind tibbiy yoki psixologik
       tashxis emas va hali oʻzbek oʻsmirlarida alohida tekshirilmagan. Natijani maslahat
       sifatida qabul qiling.</p></details>
  <details><summary>Necha yoshdan boshlab topshirsa boʻladi?</summary>
    <p>Test asosan 14–16 yoshdagi oʻsmirlar uchun moʻljallangan. 18 yoshga toʻlmagan
       boʻlsangiz, natijani ota-onangiz yoki oʻqituvchingiz bilan muhokama qilish tavsiya
       etiladi.</p></details>
  <details><summary>Natija haqiqatga qanchalik yaqin?</summary>
    <p>Bu butunlay siz qanday javob berishingizga bogʻliq. «Qanday boʻlishni xohlayman»
       emas, «hozir qandayman» deb javob bersangiz, natija ancha aniqroq chiqadi. Barcha savollarga bir xil javob bersangiz ham natija chiqadi, lekin u sizni aniq aks ettirmaydi — shuning uchun har bir savolga alohida, chin dildan javob bering.</p></details>
  <details><summary>Obrazim keyin oʻzgarishi mumkinmi?</summary>
    <p>Ha. 14–16 yoshda shaxsiyat hali shakllanmoqda. Bu natija — hukm emas, bugungi
       holatingizning surati.</p></details>
  <details><summary>Nega oʻnta obraz?</summary>
    <p>Beshta xususiyatdan eng kuchli ikkitasi olinadi. Beshtadan ikkitani tanlashning
       oʻnta usuli bor — shuning uchun oʻnta obraz.
       <a href="obrazlar.html">Hammasini koʻring</a>.</p></details>
  <details><summary>Testni qayta topshirsam boʻladimi?</summary>
    <p>Ha, istagancha. Lekin natija oʻzgarib turmasligi uchun oʻylab, rostgoʻy javob
       berish yaxshiroq.</p></details>
</div></div></section>
""" + CLOSE

PAGES = [
    ('index.html', 'TestMind — Siz qaysi obrazsiz?',
     u'Oʻzbek tilidagi bepul shaxsiyat testi. 50 ta savol, 7 daqiqa. Yakunida oʻnta obrazdan bittasi sizniki boʻladi.',
     HOME),
    ('obrazlar.html', u'Oʻnta obraz — TestMind',
     u'TestMind oʻnta obrazi: har biri oʻziga xos kuchli tomonlar toʻplami va unga mos oʻzbek tarixiy siymosi.',
     OBRAZLAR),
    ('qanday-ishlaydi.html', u'Qanday ishlaydi — TestMind',
     u'TestMind qanday ishlaydi, qaysi modelga asoslangan va javoblaringiz bilan nima boʻladi.',
     QANDAY),
    ('savollar.html', u'Koʻp beriladigan savollar — TestMind',
     u'TestMind haqida koʻp beriladigan savollarga qisqa javoblar.',
     SAVOLLAR),
]

for fname, title, desc, body in PAGES:
    html = head(title, desc) + nav(fname) + body + FOOTER + SCRIPTS
    io.open(OUT + fname, 'w', encoding='utf-8', newline='').write(html)
    print('wrote %-24s %6d bytes' % (fname, len(html.encode('utf-8'))))

# ---------------------------------------------------------------- privacy
PRIVACY = u"""<header class="phead"><div class="wrap">
  <h1>Maxfiylik</h1>
  <p class="lead">TestMind maʼlumotlaringiz bilan qanday ishlashi haqida qisqa va sodda izoh.</p>
</div></header>

<section><div class="wrap" style="max-width:780px">
  <h2>Nima saqlanadi</h2>
  <p>Test yakunlanganda faqat anonim maʼlumot saqlanadi: 5 ta umumiy ball,
     natija nomi, testga ketgan vaqt va qurilma turi (telefon yoki kompyuter).
     Bu maʼlumotlar yopiq jadvalda saqlanadi va faqat testni yaxshilash uchun ishlatiladi.</p>

  <h2>Nima soʻralmaydi</h2>
  <p>Test ismingizni ham, yoshingizni ham soʻramaydi — shuning uchun ular hech qayerda
     saqlanmaydi. Roʻyxatdan oʻtish ham kerak emas: «Testni boshlash» tugmasini bosasiz
     va birinchi savol chiqadi.</p>

  <h2>Javoblaringiz</h2>
  <p>Test yakunlanganda savollarga bergan javoblaringiz <b>ismsiz</b> saqlanadi.
     Bu yozuvda ism ham, yosh ham, email ham boʻlmaydi.</p>
  <p>Yozuvga alohida tasodifiy raqam beriladi. Bu raqam sizning boshqa
     maʼlumotlaringizga — jumladan, email qoldirgan boʻlsangiz, oʻsha manzilga —
     <b>bogʻlanmaydi</b>. Shu sababli saqlangan javoblardan kim javob berganini
     aniqlab boʻlmaydi.</p>
  <p>Buni nima uchun saqlaymiz: TestMind savollari oʻzbek oʻsmirlarida hali
     tekshirilmagan. Qaysi savol yaxshi ishlashini faqat real javoblar koʻrsatadi.
     Maʼlumot boshqa hech kimga berilmaydi va sotilmaydi.</p>

  <h2>Email qoldirsangiz</h2>
  <p>Natija sahifasida email manzilingizni qoldirish — ixtiyoriy. Uni faqat oʻzingiz yozib,
     tugmani bosgandagina yuboriladi; sahifani ochganingizda hech narsa yuborilmaydi.</p>
  <p>Email qoldirsangiz, u natijangiz nomi bilan birga saqlanadi — shu sababli
     bu maʼlumot anonim boʻlmaydi. Undan faqat sizga soʻralgan qoʻllanmani yuborish uchun
     foydalanamiz. Emailingizni hech kimga bermaymiz va sotmaymiz.</p>
  <p>Istalgan vaqtda oʻchirishimizni soʻrashingiz mumkin — quyidagi manzilga yozing.
     18 yoshga toʻlmagan boʻlsangiz, email qoldirishdan oldin ota-onangiz yoki
     oʻqituvchingiz bilan maslahatlashing.</p>

  <h2>Qurilmangizda</h2>
  <p>Testni yarmida toʻxtatsangiz, keyin davom ettirishingiz uchun javoblaringiz vaqtincha
     shu qurilmaning brauzer xotirasida saqlanadi. Natija chiqishi bilan ular avtomatik
     oʻchiriladi.</p>

  <h2>Boshqa saytlar</h2>
  <p>TestMind sahifasi reklama, kuzatuv skriptlari yoki tashqi shriftlarni yuklamaydi — boshqa saytlardan hech narsa chaqirmaydi. Yagona tashqi soʻrov — yuqorida aytilgan anonim maʼlumotni yopiq Google jadvaliga yuborish.</p>

  <h2>Natija haqida</h2>
  <p>Natija maslahat xarakteriga ega, tibbiy yoki ilmiy xulosa emas. Kasb yoki yoʻnalish
     tanlashda uni yagona asos qilib olmang.</p>

  <h2>Yosh</h2>
  <p>Test asosan 14–16 yoshdagi oʻsmirlar uchun moʻljallangan. 18 yoshga toʻlmaganlarga
     ota-onasi yoki oʻqituvchisi bilan maslahatlashgan holda foydalanish tavsiya etiladi.</p>

  <h2>Savollar</h2>
  <p>Savol yoki maʼlumotingizni oʻchirish boʻyicha murojaat:
     <a href="mailto:raximovrahim1@gmail.com">raximovrahim1@gmail.com</a>.</p>
</div></section>
"""

html = head(u'Maxfiylik — TestMind',
            u'TestMind maʼlumotlaringiz bilan qanday ishlashi haqida qisqa izoh.') \
     + nav('privacy.html') + PRIVACY + FOOTER + SCRIPTS
io.open(OUT + 'privacy.html', 'w', encoding='utf-8', newline='').write(html)
print('wrote %-24s %6d bytes' % ('privacy.html', len(html.encode('utf-8'))))

# ---------------------------------------------------------------- schools / parents
MAKTABLAR = u"""<header class="phead"><div class="wrap">
  <h1>Maktablar va ota-onalar uchun</h1>
  <p class="lead">TestMind nima qila oladi, nima qila olmaydi va uni sinfda qanday
     qoʻllash kerak — ochiq va toʻliq.</p>
</div></header>

<section><div class="wrap" style="max-width:820px">
  <h2>Bu nima</h2>
  <p>TestMind — 14–16 yoshdagi oʻsmirlar uchun oʻzbek tilidagi bepul shaxsiyat soʻrovnomasi.
     U «Katta beshlik» (Big Five) modeliga asoslanadi va beshta xususiyatni oʻlchaydi:
     hissiy barqarorlik, kirishimlilik, yangilikka ochiqlik, kelishuvchanlik va
     masʼuliyatlilik. Natija sifatida oʻquvchi eng kuchli ikkita xususiyatiga mos
     obraz oladi.</p>

  <h2>Bu nima emas</h2>
  <p>Bu tibbiy yoki psixologik tashxis emas. U qobiliyatni, aqlni yoki bilimni
     oʻlchamaydi va oʻquvchining kelajakdagi muvaffaqiyatini bashorat qilmaydi.</p>

  <h2>Cheklovlarni ochiq aytamiz</h2>
  <div class="why" style="margin-top:14px">
    <div class="wcard"><h3>Oʻzbek oʻsmirlarida tekshirilmagan</h3>
      <p>Savollar xalqaro ochiq manbadagi Big Five soʻrovnomalari asosida tayyorlangan,
         lekin TestMind hali Oʻzbekistonda alohida ilmiy tekshiruvdan oʻtmagan.</p></div>
    <div class="wcard"><h3>Natija qayta topshirilganda oʻzgarishi mumkin</h3>
      <p>Ikkita xususiyat ball boʻyicha yaqin boʻlsa, obraz oʻzgarishi mumkin. Test buni
         yashirmaydi: bunday holatda oʻquvchiga ikkinchi obraz ham koʻrsatiladi.</p></div>
    <div class="wcard"><h3>Oʻz-oʻzini baholashga asoslangan</h3>
      <p>Oʻquvchi oʻzi haqida yozgan javoblar tahlil qilinadi. Kayfiyat, shoshilish yoki
         «yaxshi koʻrinish» istagi natijaga taʼsir qiladi.</p></div>
    <div class="wcard"><h3>Yosh — oʻzgarish davri</h3>
      <p>14–16 yoshda shaxsiyat hali shakllanmoqda. Natija — bugungi surat, doimiy
         xarakteristika emas.</p></div>
  </div>

  <h2>Sinfda qanday oʻtkazish tavsiya etiladi</h2>
  <div class="steps" style="margin-top:14px">
    <div class="step"><div class="stepn">1</div>
      <h3>Oldindan xabar bering</h3>
      <p>Ota-onalarni testdan oldin ogohlantiring va ushbu sahifani ular bilan
         boʻlishing. Ishtirok ixtiyoriy boʻlishi kerak.</p></div>
    <div class="step"><div class="stepn">2</div>
      <h3>Oʻquvchidan ham rozilik soʻrang</h3>
      <p>Oʻsmirga testning maqsadini tushuntiring va rad etish huquqi borligini ayting.
         Majburlangan test ishonchli natija bermaydi.</p></div>
    <div class="step"><div class="stepn">3</div>
      <h3>Natijani suhbat boshlanishi sifatida ishlating</h3>
      <p>«Sen shundaysan» emas, «bu haqida nima deb oʻylaysan?» Natija hukm emas,
         savol tugʻdiruvchi vosita.</p></div>
  </div>

  <h2>Iltimos, bularni qilmang</h2>
  <div class="why" style="margin-top:14px">
    <div class="wcard"><h3>Oʻquvchilarni guruhlarga ajratmang</h3>
      <p>Obraz asosida sinf yoki yoʻnalish taqsimlash uchun foydalanmang. Test bunga
         moʻljallanmagan va bunga yetarli aniqlikka ega emas.</p></div>
    <div class="wcard"><h3>Natijani shaxsiy hujjatga kiritmang</h3>
      <p>Obraz oʻquvchining rasmiy tavsifnomasi yoki hujjatining bir qismi boʻlmasligi kerak.</p></div>
    <div class="wcard"><h3>Ochiq taqqoslamang</h3>
      <p>Natijalarni sinf oldida solishtirish yoki «kim yaxshiroq» degan savolni
         qoʻyish zararli. Obrazlar orasida yaxshi-yomon yoʻq.</p></div>
    <div class="wcard"><h3>Kasb tanlashda yagona asos qilmang</h3>
      <p>Natija qiziqish, imkoniyat va real tajriba bilan birga koʻrib chiqilishi kerak.</p></div>
  </div>

  <h2>Maʼlumotlar bilan nima boʻladi</h2>
  <p>Test oʻquvchidan ism ham, yosh ham <b>soʻramaydi</b>. Test yakunida faqat anonim
     maʼlumot saqlanadi: beshta umumiy ball, obraz nomi, sarflangan vaqt va qurilma turi.</p>
  <p>Oʻquvchining savollarga bergan javoblari ham <b>ismsiz</b> saqlanadi: yozuvda
     ism ham, yosh ham, email ham boʻlmaydi va unga alohida tasodifiy raqam beriladi, yaʼni uni
     oʻquvchining boshqa maʼlumotlariga bogʻlab boʻlmaydi. Bu maʼlumot faqat testni
     oʻzbek oʻsmirlari uchun aniqroq qilish uchun ishlatiladi va hech kimga
     berilmaydi. Sinfda oʻtkazishdan oldin bu haqda ota-onalarga xabar berishingizni
     soʻraymiz — tayyor xat saytda bor.</p>
  <p>Agar oʻquvchi <b>oʻz xohishi bilan</b> email qoldirsa, u anonim boʻlmaydi — buni
     <a href="privacy.html">Maxfiylik</a> sahifasida ochiq yozganmiz. 18 yoshgacha
     boʻlganlarga email qoldirishdan oldin kattalar bilan maslahatlashish tavsiya etiladi.</p>
  <p>Sayt reklama va kuzatuv skriptlarini ishlatmaydi va boshqa saytlardan hech narsa yuklamaydi. Yagona tashqi soʻrov — yuqorida aytilgan anonim maʼlumotni yopiq Google jadvaliga yuborish.</p>

  <h2>Bogʻlanish</h2>
  <p>Savollar, takliflar yoki maʼlumotni oʻchirish boʻyicha:
     <a href="mailto:raximovrahim1@gmail.com">raximovrahim1@gmail.com</a>.
     Maktabingizda oʻtkazishni rejalashtirsangiz, yozing — yordam beramiz.</p>
</div></section>
"""

html = head(u'Maktablar va ota-onalar uchun — TestMind',
            u'TestMind nima qila oladi, nima qila olmaydi va uni sinfda qanday qoʻllash kerak.') \
     + nav('maktablar.html') + MAKTABLAR + FOOTER + SCRIPTS
io.open(OUT + 'maktablar.html', 'w', encoding='utf-8', newline='').write(html)
print('wrote %-24s %6d bytes' % ('maktablar.html', len(html.encode('utf-8'))))

# ---------------------------------------------------------------- parent letter
XAT = '<header class="phead noprint"><div class="wrap">\n  <h1>Ota-onalarga xat</h1>\n  <p class="lead">Sinfda test oʻtkazishdan oldin ota-onalarni xabardor qilish uchun tayyor\n     matn. Chop eting yoki nusxalab yuboring — tugma faqat xatni chiqaradi.</p>\n  <p><button class="btn" id="printLetter">Xatni chop etish</button></p>\n</div></header>\n\n<section><div class="wrap" style="max-width:760px">\n  <div class="letter" id="letter">\n    <p class="lt-to">Hurmatli ota-onalar,</p>\n\n    <p>Farzandingiz oʻqiydigan sinfda <b>TestMind</b> nomli shaxsiyat soʻrovnomasini\n       oʻtkazishni rejalashtiryapmiz. Quyida u haqida qisqacha maʼlumot.</p>\n\n    <p><b>Bu nima?</b> 50 ta savoldan iborat, taxminan 7 daqiqa davom etadigan\n       soʻrovnoma. U psixologiyada keng qoʻllanadigan «Katta beshlik» modeliga\n       asoslangan va oʻquvchiga oʻzining kuchli tomonlarini tanishga yordam beradi.</p>\n\n    <p><b>Bu nima emas.</b> Bu imtihon emas, baho qoʻyilmaydi. Bu tibbiy yoki psixologik\n       tashxis ham emas. Natija oʻquvchining qobiliyatini yoki kelajakdagi\n       muvaffaqiyatini oʻlchamaydi va uning hujjatlariga kiritilmaydi.</p>\n\n    <p><b>Maʼlumotlar.</b> Test farzandingizdan ism ham, yosh ham soʻramaydi. Test\n       yakunida faqat anonim maʼlumot saqlanadi: umumiy ballar va natija nomi.\n       Savollarga bergan javoblari ham ismsiz saqlanadi: bu yozuvda\n       ism ham, yosh ham, email ham boʻlmaydi va unga alohida tasodifiy raqam beriladi,\n       yaʼni uni farzandingizga bogʻlab boʻlmaydi. Bu maʼlumot faqat testni\n       yaxshilash uchun ishlatiladi va hech kimga berilmaydi.</p>\n\n    <p><b>Ishtirok ixtiyoriy.</b> Farzandingiz xohlamasa, qatnashmasligi mumkin va bu\n       hech qanday tarzda bahosiga taʼsir qilmaydi.</p>\n\n    <p>Batafsil maʼlumot va maxfiylik siyosati saytda mavjud: <b class="lt-host">testmind-minis.netlify.app</b></p>\n\n    <p>Savollaringiz boʻlsa, sinf rahbariga yoki\n       <b>raximovrahim1@gmail.com</b> manziliga murojaat qiling.</p>\n\n    <div class="lt-sign">\n      <div><span class="lt-line"></span>Sinf rahbari</div>\n      <div><span class="lt-line"></span>Sana</div>\n    </div>\n\n    <hr class="lt-hr">\n\n    <p class="lt-small"><b>Rozilik.</b> Quyidagini toʻldirib qaytaring:</p>\n    <p class="lt-small">Men, ____________________________________, farzandim\n       ____________________________________ ning TestMind soʻrovnomasida\n       ishtirok etishiga:</p>\n    <p class="lt-small">&#9744; roziman &nbsp;&nbsp;&nbsp; &#9744; rozi emasman</p>\n    <div class="lt-sign">\n      <div><span class="lt-line"></span>Imzo</div>\n      <div><span class="lt-line"></span>Sana</div>\n    </div>\n  </div>\n</div></section>\n'

html = head(u'Ota-onalarga xat — TestMind',
            u'Sinfda TestMind oʻtkazishdan oldin ota-onalarni xabardor qilish uchun tayyor xat.') \
     + nav('maktablar.html') + XAT + FOOTER + SCRIPTS
io.open(OUT + 'ota-onalarga.html', 'w', encoding='utf-8', newline='').write(html)
print('wrote %-24s %6d bytes' % ('ota-onalarga.html', len(html.encode('utf-8'))))
