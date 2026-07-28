# -*- coding: utf-8 -*-
"""The written PDF guide: shared text once, then one entry per archetype.

Only the short lines on the website are generated from characters.js; the long
form below is hand-written, because it is the actual product a student takes
away. Keep the voice: talking TO a school student aged 10–18, second person, concrete
school examples, no jargon, no verdicts. Every «oʻsish nuqtasi» must end with
one small thing they can do this week — advice without an action is just a
compliment.

Three layers, so the same sentence is never written twice:

  COMMON       — identical on all ten guides (how to read it, the closing
                 pointers). Change it once, all ten change.
  TRAIT_CARDS  — one card per Big Five trait. An archetype is a pair of
                 traits, so its two cards are looked up here; that is why
                 «Xotirjam» reads the same in all four ES guides.
  GUIDES       — what is genuinely specific to the pair.

THE ONE RULE: if a sentence would be true of any student, cut it.

This is not style advice. The reason personality tests have a poor reputation is
the Barnum effect — vague, flattering statements feel accurate to everyone, which
is why horoscopes work and why "you sometimes doubt yourself" is worthless. A
guide earns its credibility sentence by sentence, by saying things that would be
WRONG for another archetype.

Concretely, when writing the remaining guides:
  - Name the situation: a group project, the ten minutes before an exam, a friend
    who went quiet — not "social situations".
  - Every growth point ends with one action doable this week. Advice without an
    action is just a compliment.
  - Prefer a sentence that could be wrong. "You find it hard to say no" is worth
    more than "you value harmony", because a student can disagree with it.
  - No praise that costs nothing. Delete anything of the form "you are special
    in your own way".
"""

# --------------------------------------------------------------------------
# Shared by all ten
# --------------------------------------------------------------------------
COMMON = {

'cover_kicker': u'Shaxsiyat qoʻllanmasi',
'portrait_title': u'Siz kundalik hayotda',

'howto': [
    (u'Bu — hukm emas, oyna.',
     u'Bu yerda «siz shundaysiz, boshqacha boʻla olmaysiz» degan gap yoʻq. '
     u'Bu — bugungi suratingiz. 10–18 yoshda shaxsiyat hali shakllanmoqda, '
     u'shuning uchun bir yildan keyin ayrim javoblaringiz oʻzgarishi tabiiy.'),
    (u'«Yaxshi» yoki «yomon» tur yoʻq.',
     u'Har bir obrazning kuchli tomoni ham, ehtiyot boʻladigan joyi ham bor. '
     u'Sizniki boshqalarnikidan yaxshiroq ham, yomonroq ham emas — boshqacha.'),
    (u'Hammasi toʻgʻri kelmasligi mumkin.',
     u'Test 50 ta savolga asoslangan, u sizni toʻliq bilmaydi. Oʻzingizga mos '
     u'kelgan joylarini oling, mos kelmaganini chetga qoʻying — bu ham natija.'),
    (u'Eng foydali qismi — amaliyot.',
     u'Oxirgi sahifadagi kichik vazifalar shu qoʻllanmaning maʼnosi. '
     u'Oʻqib qoʻyish bilan hech narsa oʻzgarmaydi; bitta narsani sinab '
     u'koʻrish bilan oʻzgaradi.'),
],

'traits_intro': u'Obrazingiz beshta xususiyatdan eng kuchli chiqqan ikkitasidan '
                u'tugʻiladi. Qolgan uchtasi ham sizda bor — shunchaki bu ikkisi '
                u'ulardan sal oldinda.',

'future_intro': u'Quyidagilar — buyruq emas, yoʻnalish. Shaxsiyat kasb tanlashning '
                u'faqat bitta qismi; qolgani — nima qiziq va nimaga imkoningiz bor. '
                u'Roʻyxatdagi biror narsa sizni qiziqtirmasa, bemalol tashlab keting.',

'future_next': u'Bu qoʻllanma sizning shaxsiyatingiz haqida. Kasb tanlash uchun '
               u'ikkinchi qism ham kerak: nima sizga qiziq. TestMind yaqin '
               u'orada shu savolga qaratilgan alohida test qoʻshadi. Shu '
               u'paytgacha oddiy mashq: soʻnggi bir oyda vaqtingiz qanday '
               u'oʻtganini sezmay qolgan uchta ishni yozib qoʻying.',

'practice_intro': u'Ikki hafta. Kuniga bir necha daqiqa. Hammasini emas, '
                  u'bajarganingizni belgilang — bittasi ham natija.',
}


# --------------------------------------------------------------------------
# One card per trait — an archetype shows the two that came out strongest
# --------------------------------------------------------------------------
TRAIT_CARDS = {

'ES': (u'Xotirjam',
       u'Sizni tez chiqarib yuborish qiyin. Kutilmagan narsa boʻlganda ham '
       u'bir necha soniya toʻxtab, keyin harakat qilasiz. Atrofdagilar '
       u'shovqin koʻtarganda sizning ovozingiz baland chiqmaydi — va aynan '
       u'shuning uchun sizni eshitishadi.'),

'E': (u'Kirishimli',
      u'Odamlar sizga quvvat beradi, olib qoʻymaydi. Notanish davraga '
      u'kirish, birinchi boʻlib gap boshlash, koʻpchilik oldida gapirish '
      u'sizga boshqalarga qaraganda oson.'),

'O': (u'Kashfiyotchi',
      u'Yangi narsa sizni qoʻrqitmaydi, qiziqtiradi. «Buni boshqacha qilsa '
      u'boʻlmaydimi?» degan savol sizda oʻz-oʻzidan tugʻiladi va siz '
      u'javobini izlab koʻrasiz.'),

'A': (u'Hamkor',
      u'Odamlarning holatini ilgʻaysiz. Kim xafa boʻlganini, kim gapirmay '
      u'qolganini koʻpincha birinchi boʻlib siz sezasiz. Yordam berish '
      u'sizga majburiyat emas, tabiiy tuyuladi.'),

'C': (u'Rejali',
      u'Boshlagan ishni oxiriga yetkazasiz. Tartib va aniqlik sizni '
      u'bosmaydi, aksincha — qulaylik beradi. Vaʼda qilingan muddat siz '
      u'uchun taxmin emas.'),
}


# --------------------------------------------------------------------------
# What is specific to each pair
# --------------------------------------------------------------------------
GUIDES = {

# ============================================================ ES|A ==========
'ES|A': {
'traits_note': u'Bu ikkisi bir joyga tushganda «ishonchli odam» chiqadi: '
               u'his qiladigan, lekin vahima qilmaydigan odam. Bunday odam '
               u'har qanday sinfda kam boʻladi.',

'portrait': [
    u'Sinfda kimdir jim boʻlib qolsa, buni koʻpchilik sezmaydi. Siz sezasiz. '
    u'Baʼzan hatto nima boʻlganini bilmaysiz ham — shunchaki «bugun u '
    u'boshqacha» degan tuygʻu paydo boʻladi. Bu tasodif emas: siz odamlarning '
    u'ovoz ohangi, yuzi va sukutiga eʼtibor berasiz.',

    u'Janjal chiqsa, siz odatda oʻrtada qolasiz. Ikkala tomonni ham '
    u'tushunasiz va shuning uchun «kim haq» degan savolga javob berish sizga '
    u'ogʻir. Koʻpincha vaziyatni yumshatishga urinasiz: mavzuni oʻzgartirasiz, '
    u'hazil qilasiz yoki oddiygina jim turasiz. Bu — kuch, lekin har doim ham '
    u'yechim emas.',

    u'Imtihon oldidan atrofdagilar hayajonlanadi, qoʻllari qaltiraydi. Sizda '
    u'ham hayajon bor, lekin u sizni boshqarmaydi. Aynan shuning uchun '
    u'doʻstlaringiz oxirgi daqiqada sizdan «tinchlantirib yubor» deb soʻraydi.',

    u'Sizga sir aytishadi. Bu tekinga kelmagan: siz eshitgan narsangizni '
    u'tarqatmagansiz va ustidan kulmagansiz. Odamlar buni eslab qoladi.',

    u'Lekin oʻzingiz haqingizda kam gapirasiz. «Mendan ham soʻrasin edi» deb '
    u'kutasiz, soʻramasa — indamaysiz. Natijada boshqalar sizni doim '
    u'«hammasi joyida» deb oʻylaydi. Ular yomon niyatda emas — ular '
    u'shunchaki bilmaydi.',
],
'portrait_pull': u'Siz odamlarga eʼtibor berasiz. Shu eʼtiborning kichik bir '
                 u'qismini oʻzingizga qaratsangiz, hech kimdan hech narsa '
                 u'tortib olmaysiz.',

'strengths': [
    (u'Odamlarni tinchlantira olasiz',
     u'Siz gapirganda ovoz balandligi tushadi. Bu oʻrgatiladigan narsa emas, '
     u'sizda bor. Guruh ishida, janjaldan keyin, imtihon oldidan — bu '
     u'koʻrinmas, lekin juda qimmatli hissa.'),
    (u'Sizga ishonsa boʻladi',
     u'Vaʼda bersangiz, bajarasiz. Kichik narsalarda ham. Odamlar buni '
     u'sanab yurmaydi, lekin his qiladi — va shuning uchun muhim ishni '
     u'sizga topshiradi.'),
    (u'Bosim ostida boshingizni yoʻqotmaysiz',
     u'Hamma shoshib qolganda siz «shoshmang, avval nima boʻlganini '
     u'aniqlaylik» deya olasiz. Bu koʻnikma katta hayotda pul turadi.'),
    (u'Chin dildan tinglaysiz',
     u'Koʻpchilik tinglayotgandek koʻrinadi, aslida oʻz navbatini kutadi. '
     u'Siz haqiqatan eshitasiz. Bu sizni kam uchraydigan doʻst qiladi.'),
],

'growth': [
    (u'«Yoʻq» deyishni oʻrganing',
     u'Sizdan soʻrashadi — siz rozi boʻlasiz. Yana soʻrashadi — yana rozi '
     u'boʻlasiz. Bir kuni charchaganingizni sezasiz, lekin gapirmaysiz, '
     u'chunki «xafa boʻlishadi» deb oʻylaysiz. Aslida «yoʻq» deyish '
     u'doʻstlikni buzmaydi; aytilmagan norozilik buzadi.',
     u'Shu hafta bitta iltimosga shunday javob bering: «Kechirasiz, bugun '
     u'ulgurmayman». Izoh bermang, kechirim soʻrab uzoq gapirmang. '
     u'Bir marta. Va nima boʻlishini kuzating.'),

    (u'Oʻz fikringizni ovoz chiqarib ayting',
     u'Nizodan qochish uchun siz koʻpincha oʻz fikringizni ichingizda '
     u'qoldirasiz. Muammo shundaki, keyinchalik odamlar sizning fikringizni '
     u'umuman bilmaydi va qarorlar siz ishtirok etmagan holda qabul '
     u'qilinadi. Rozi boʻlmaslik — hurmatsizlik emas.',
     u'Shu hafta bir marta: «Men biroz boshqacha oʻylayman...» deb boshlang. '
     u'Darsdami, doʻstlar davrasidami — farqi yoʻq. Gapni oxirigacha ayting.'),

    (u'Xotirjamlik — hech narsa his qilmaslik degani emas',
     u'Siz tashqaridan tinch koʻrinasiz va odamlar «unga hech narsa taʼsir '
     u'qilmaydi» deb oʻylaydi. Aslida sizda ham charchoq, ranj, xafagarchilik '
     u'bor — faqat ular jim yigʻiladi. Yigʻilgan narsa bir kuni kutilmagan '
     u'joyda chiqadi.',
     u'Har kuni kechqurun 2 daqiqa: bitta daftarga «Bugun nima his qildim?» '
     u'deb bitta jumla yozing. Chiroyli yozish shart emas. Bir hafta yozib '
     u'koʻring — takrorlanadigan narsani sezasiz.'),
],

'school': [
    (u'Guruh ishida',
     u'Siz odatda jamoani ushlab turasiz. Xavf ham shunda: ish sekin-asta '
     u'sizga toʻplanadi, chunki soʻrash sizdan oson. Ish boshida rollarni '
     u'ovoz chiqarib boʻlib oling — «men buni olaman, sen buni» deb.'),
    (u'Imtihon va nazoratda',
     u'Xotirjamlik bu yerda katta ustunlik. Faqat bitta odat qoʻshing: '
     u'atrofga qaramang. Kimdir tez yozayotgani sizning bilimingiz haqida '
     u'hech narsa demaydi.'),
    (u'Qanday oʻrganganingiz maʼqul',
     u'Siz tushuntirganingizda yaxshi oʻzlashtirasiz. Mavzuni oʻrganganingizdan '
     u'keyin uni doʻstingizga (yoki boʻsh xonaga) 3 daqiqa ovoz chiqarib '
     u'tushuntiring. Qayerda toʻxtab qolsangiz — oʻsha joyni bilmaysiz.'),
    (u'Toʻqnashuv boʻlganda',
     u'Sizning odatingiz — vaziyatni yumshatish. Bu koʻp holatda toʻgʻri, '
     u'lekin har doim emas: baʼzan masala hal boʻlmay, faqat koʻmilib '
     u'qoladi. Yumshatishdan oldin bitta savol bering: «Bu haqiqatan hal '
     u'boʻldimi yoki shunchaki jim boʻldikmi?»'),
    (u'Doʻstlik va oila',
     u'Siz odamlar uchun xavfsiz joysiz. Buni saqlang, lekin bir tomonlama '
     u'qilib qoʻymang: sizni ham soʻraydigan, sizni ham eshitadigan '
     u'odamlarga yaqin turing. Ota-onangiz sizga koʻp ishonadi — shuning '
     u'uchun ular sizga kamroq savol berishi mumkin. Kerak boʻlsa, oʻzingiz '
     u'ayting.'),
],

'future_fits': [
    (u'Odamlar bilan ishlaydigan yoʻnalishlar',
     u'Taʼlim, tibbiyot va hamshiralik, psixologiya, ijtimoiy ish, '
     u'reabilitatsiya. Sizning tinglash va tinchlantirish koʻnikmangiz '
     u'bu sohalarda asosiy ish quroli.'),
    (u'Jamoa va muvofiqlashtirish',
     u'Loyiha koordinatori, HR, mijozlar bilan ishlash, jamoada bogʻlovchi '
     u'rol. Odamlar orasidagi ishonchni saqlash — alohida kasb.'),
    (u'Bosim ostidagi muhitlar',
     u'Tez tibbiy yordam, dispetcherlik, xavfsizlik, uchuvchi-navigator kabi '
     u'yoʻnalishlar. Vahima qilmaslik u yerda hayot saqlaydi.'),
    (u'Uzoq muddatli, sabr talab qiladigan ishlar',
     u'Tadqiqot, arxiv, sifat nazorati, buxgalteriya, dasturlashda '
     u'qoʻllab-quvvatlash. Bir ishni oxirigacha, shovqinsiz olib borish '
     u'hamma ham eplaydigan narsa emas.'),
],
'future_watch': u'Sizga eng qiyin boʻladigan muhit — doimiy raqobat va qattiq '
                u'muzokara talab qiladigan joylar. Bu «siz uddalay olmaysiz» '
                u'degani emas; shunchaki u yerda ortiqcha energiya sarflaysiz. '
                u'Agar shunday yoʻnalish sizni qiziqtirsa, «yoʻq» deyish va '
                u'oʻz fikrini himoya qilish koʻnikmasini oldindan mashq qiling.',

'figure_why': u'Uvaysiy shoira sifatida tanilgan, lekin uni bugungacha eslab '
              u'kelinayotgan sabab faqat sheʼrlari emas. U Qoʻqon saroyida '
              u'Nodirabegimga ustozlik qilgan — yaʼni oʻz bilimini boshqa '
              u'odamning oʻsishiga sarflagan. Bu sizga tanish boʻlishi kerak: '
              u'oʻzini oldinga surmasdan, atrofidagilarni koʻtarish. Bunday '
              u'odamlarning ismi kamroq eshitiladi, lekin ular boʻlmasa '
              u'hech kim koʻtarilmaydi.',

'practice': [
    u'Bitta iltimosga «yoʻq» deb javob berdim.',
    u'Bir marta «men boshqacha oʻylayman» dedim va sababini aytdim.',
    u'Bir hafta davomida har kuni bitta jumla — bugungi kayfiyatim — yozdim.',
    u'Bir mavzuni doʻstimga ovoz chiqarib tushuntirdim.',
    u'Guruh ishida rollarni boshida boʻlib oldim.',
    u'Menga yordam kerak boʻlganda, oʻzim soʻradim.',
    u'Bir kun faqat oʻzim uchun biror narsa qildim (aybdorlik hissisiz).',
],
'closing': u'Sizning kuchingiz baland ovozda emas. Shuning uchun uni sezmay '
           u'qolish oson — hatto oʻzingizga ham. Bu qoʻllanmani bir oydan keyin '
           u'yana bir marta oching: qaysi biri toʻgʻri chiqqanini oʻzingiz '
           u'koʻrasiz.',
},


# ============================================================ ES|E ==========
'ES|E': {
'traits_note': u'Bu ikkisi birga kelganda yetakchi chiqadi — baqiradigan '
               u'emas, ishonch uygʻotadigani. Odamlar sizga ergashadi, '
               u'chunki siz sarosimaga tushmaysiz.',

'portrait': [
    u'Guruh adashib qolganda — kim nima qilishini bilmay, hamma bir-biriga '
    u'qarab turganda — koʻpincha birinchi boʻlib siz gapirasiz. Buni maxsus '
    u'oʻylab qilmaysiz; shunchaki jimlik sizni boshqalarchalik '
    u'noqulay ahvolga solmaydi.',

    u'Vaziyat qizib ketganda ovozingiz koʻtarilmaydi. Boshqalar bir-birining '
    u'gapini boʻlayotganda siz kutasiz, keyin bir jumla aytasiz — va shu bir '
    u'jumla koʻpincha ishlaydi. Bu sehr emas: baland ovoz orasida tinch ovoz '
    u'boshqacha eshitiladi.',

    u'Odamlar bilan tanishish sizga ogʻir emas. Yangi sinfga, yangi toʻgaragga '
    u'borsangiz, bir haftada bir necha odamni bilib olasiz. Notanish odamga '
    u'birinchi boʻlib gap qotish sizni charchatmaydi.',

    u'Sizdan koʻpincha maslahat soʻrashadi. Nafaqat doʻstlaringiz — baʼzan '
    u'sizdan kattaroqlar ham. Chunki siz vaziyatni bahslashmasdan, '
    u'ayblamasdan tushuntira olasiz.',

    u'Lekin xotirjamligingiz baʼzan boshqacha koʻrinadi. Kimdir yigʻlab '
    u'turganda sizning tinch turishingiz «unga farqi yoʻq ekan» degan '
    u'taassurot qoldiradi. Siz beparvo emassiz — shunchaki tashqi '
    u'koʻrinishingiz ichkaridagini koʻrsatmaydi.',
],
'portrait_pull': u'Odamlar sizga ergashishi — imtiyoz emas, masʼuliyat. '
                 u'Ergashayotganlar sizning nima his qilayotganingizni ham '
                 u'bilishga haqli.',

'strengths': [
    (u'Bosim ostida toʻgʻri qaror qabul qilasiz',
     u'Hamma shoshib qolganda sizning fikringiz ishlashda davom etadi. '
     u'Bu juda kam uchraydigan narsa va katta hayotda eng qadrlanadigan '
     u'sifatlardan biri.'),
    (u'Sizni eshitishadi',
     u'Ovozingizni koʻtarmasdan ham eʼtiborni tortasiz. Baqirib gapiradigan '
     u'odam bir kunda unutiladi; tinch va aniq gapiradigan odam esdan '
     u'chiqmaydi.'),
    (u'Yangi odamlar bilan tez til topasiz',
     u'Notanish muhitga kirish sizni qoʻrqitmaydi. Bu koʻnikma keyinchalik '
     u'ish, oʻqish, sayohat — hamma joyda eshik ochadi.'),
    (u'Guruhga yoʻnalish bera olasiz',
     u'Siz «kel, avval shuni qilaylik» deya olasiz va odamlar qarshilik '
     u'koʻrsatmaydi, chunki siz buyruq berayotgandek eshitilmaysiz.'),
],

'growth': [
    (u'Hissiyotingizni ham koʻrsating',
     u'Sizning xotirjamligingiz kuch, lekin u devorga aylanib qolishi ham '
     u'mumkin. Yaqin odamlar baʼzan sizdan tashvish emas, hamdardlik kutadi. '
     u'«Men ham xavotirdaman» degan bitta jumla ularni sizga yaqinlashtiradi.',
     u'Shu hafta yaqin bir odamga oʻzingiz haqingizda bitta rost gap ayting: '
     u'nimadan xursandsiz yoki nimadan charchadingiz. Bitta jumla yetarli.'),

    (u'Hamma javobni oʻzingiz bermang',
     u'Siz tez javob topasiz, shuning uchun guruh sizga qarab qoladi va '
     u'sekin-asta oʻylashni toʻxtatadi. Yetakchining ishi javob berish emas, '
     u'javob chiqishiga sharoit yaratish.',
     u'Keyingi guruh ishida oʻz fikringizni oxirida ayting. Avval ikki '
     u'kishidan «sen qanday oʻylaysan?» deb soʻrang.'),

    (u'Gapirishdan koʻra koʻproq tinglang',
     u'Gapirish sizga oson, shuning uchun jimlikni siz toʻldirasiz. Lekin '
     u'jimlik baʼzan boshqa birovga kerak boʻladi — u fikrini yigʻayotgan '
     u'boʻladi. Uch soniya kutish koʻp narsani oʻzgartiradi.',
     u'Bitta suhbatda oʻzingizni sanang: nechta savol berdingiz? Maqsad — '
     u'kamida uchta savol.'),
],

'school': [
    (u'Guruh ishida',
     u'Rahbarlik odatda sizga tushadi. Yaxshi — lekin rolni almashtirib '
     u'turing: bir marta oddiy ijrochi boʻlib koʻring. Boshqalarning qanday '
     u'ishlashini shunda tushunasiz.'),
    (u'Taqdimot va chiqishlarda',
     u'Bu sizning maydoningiz. Faqat tayyorgarlikni tashlab qoʻymang — '
     u'sizga oson kelgani uchun oxirgi kunga qoldirish vasvasasi katta.'),
    (u'Imtihon va nazoratda',
     u'Hayajon sizni kam bosadi, shuning uchun asosiy xavf — «men bilaman-ku» '
     u'deb yetarlicha tayyorlanmaslik. Xotirjamlik bilimning oʻrnini '
     u'bosmaydi.'),
    (u'Toʻqnashuv boʻlganda',
     u'Siz vositachi boʻla olasiz va koʻpincha shu rolni olasiz. Faqat bir '
     u'narsani unutmang: siz ham tomonlardan biri boʻlishingiz mumkin. '
     u'Har doim «betaraf hakam» boʻlish shart emas.'),
    (u'Doʻstlik va oila',
     u'Sizning atrofingizda odam koʻp. Xavf shundaki, koʻp tanish orasida '
     u'chin doʻst yoʻqolib qolishi mumkin. Yiliga bir-ikki odam bilan '
     u'chuqurroq munosabat butun bir davradan qimmatroq.'),
],

'future_fits': [
    (u'Yetakchilik va boshqaruv',
     u'Loyiha rahbari, tadbirkorlik, jamoa boshqaruvi, davlat xizmati. '
     u'Odamlarni qaror atrofida birlashtira olish — oʻrganish qiyin boʻlgan '
     u'koʻnikma.'),
    (u'Taʼlim va murabbiylik',
     u'Oʻqituvchilik, trenerlik, sport murabbiysi. Sinf oldida tinch turish '
     u'va eʼtiborni ushlab qolish — bu ishning yarmi.'),
    (u'Muzokara va vakillik',
     u'Huquq, diplomatiya, savdo va sotuv, jamoatchilik bilan aloqa. '
     u'Bosim ostida ovozni koʻtarmaslik bu yerda ustunlik.'),
    (u'Favqulodda vaziyatlar',
     u'Tez tibbiy yordam, qutqaruv xizmati, dispetcherlik, xavfsizlik. '
     u'Sarosimaga tushmaydigan odam bu sohalarda oltin qadrida.'),
],
'future_watch': u'Sizga eng zerikarli tuyuladigan joy — uzoq vaqt yolgʻiz, '
                u'jimjit va bir xil ish. Bunday ish sizning kuchli '
                u'tomonlaringizni umuman ishlatmaydi. Agar shunday yoʻnalish '
                u'sizni baribir qiziqtirsa, ichida odamlar bilan ishlaydigan '
                u'qismini toping — masalan, natijani boshqalarga tushuntirish.',

'figure_why': u'Bahouddin Naqshband oʻz davrining eng nufuzli odamlaridan '
              u'boʻlgan, lekin na lashkari, na taxti bor edi. Odamlar unga '
              u'majburlanganidan emas, uning oʻzini tutishiga qarab '
              u'ergashgan. «Dil ba yor-u, dast ba kor» — koʻngil maqsadda, '
              u'qoʻl ishda. Yetakchilikning bu turi baland ovoz talab '
              u'qilmaydi; u faqat izchillik talab qiladi.',

'practice': [
    u'Guruh ishida oʻz fikrimni oxirida aytdim.',
    u'Bitta suhbatda kamida uchta savol berdim.',
    u'Yaqin bir odamga oʻzim haqimda rost bir gap aytdim.',
    u'Bir marta yetakchi emas, oddiy ijrochi boʻldim.',
    u'Chiqishga oldindan tayyorlandim (oxirgi kunga qoldirmadim).',
    u'Kimdir gapirayotganda uch soniya kutdim, boʻlmadim.',
    u'Bitta odam bilan chuqurroq suhbatlashdim — davra bilan emas.',
],
'closing': u'Odamlar sizni kuchli deb biladi. Kuchli boʻlish — hech narsa his '
           u'qilmaslik degani emas. Eng yaxshi yetakchilar oʻz '
           u'zaifligini koʻrsatishdan qoʻrqmaydiganlar boʻladi.',
},


# ============================================================ E|C ===========
'E|C': {
'traits_note': u'Kirishimlilik gʻoyani odamlarga yetkazadi, masʼuliyatlilik '
               u'esa uni oxiriga yetkazadi. Koʻp odamda birinchisi bor, '
               u'ikkinchisi yoʻq. Sizda ikkalasi ham bor — shuning uchun '
               u'sizning rejangiz qogʻozda qolmaydi.',

'portrait': [
    u'Muhokama hali davom etayotganda siz allaqachon birinchi qadamni qilib '
    u'boʻlgan boʻlasiz. Boshqalar «qanday qilsak ekan» deb turganda siz '
    u'«men roʻyxat tuzdim» deysiz. Kutish sizni charchatadi.',

    u'Atrofdagilarni harakatga sola olasiz. Sizning gʻayratingiz yuqumli: '
    u'siz boshlaganingizni koʻrgan odam ham qoʻzgʻaladi. Sinfda tadbir '
    u'boʻlsa, uni tashkil qiladigan odam koʻpincha siz boʻlasiz.',

    u'Tartib sizga qulaylik beradi. Daftar, jadval, roʻyxat, muddat — bular '
    u'siz uchun ogʻirlik emas, aksincha xotirjamlik. Nima qilish kerakligini '
    u'bilsangiz, tinch ishlaysiz.',

    u'Sizning eng katta zavqingiz — tugatilgan ish. Boshlangan, lekin '
    u'tashlab qoʻyilgan narsa sizni bezovta qiladi. Shuning uchun siz koʻp '
    u'ishni oxirigacha olib borasiz.',

    u'Lekin tezligingiz baʼzan boshqalarni ortda qoldiradi. Siz allaqachon '
    u'qaror qilib boʻlgansiz, ular esa hali oʻylayapti. Ular sekin emas — '
    u'ular boshqa tezlikda ishlaydi, va ularning fikri ham kerak.',
],
'portrait_pull': u'Tez boshlash — ustunlik. Lekin notoʻgʻri yoʻnalishda tez '
                 u'yurgan odam adashgan joyiga hammadan oldin yetib boradi.',

'strengths': [
    (u'Gʻoyani haqiqatga aylantirasiz',
     u'Gap bilan ish orasidagi masofani siz boshqalardan tez bosib '
     u'oʻtasiz. Koʻpchilikda «qilsak boʻlardi» deb qoladigan narsa sizda '
     u'qilingan boʻladi.'),
    (u'Odamlarni qoʻzgʻata olasiz',
     u'Sizning ishtiyoqingiz atrofga oʻtadi. Bu — jamoani harakatga '
     u'keltiradigan eng arzon va eng kuchli vosita.'),
    (u'Boshlagan ishingizni tugatasiz',
     u'Bu oddiy koʻrinadi, lekin aslida kam uchraydi. Muddatga qadar '
     u'topshirilgan ish sizni ishonchli odam sifatida tanitadi.'),
    (u'Tartib sola olasiz',
     u'Chalkash vaziyatni siz qadamlarga boʻla olasiz. Bu koʻnikma har '
     u'qanday jamoada darhol sezilib qoladi.'),
],

'growth': [
    (u'Boshlashdan oldin soʻrang',
     u'Siz tez harakat qilasiz va shu tezlikda boshqalarning fikrini '
     u'soʻrashni unutasiz. Natijada ish qilinadi — lekin jamoa oʻzini '
     u'chetda qolgandek his qiladi. Eng yaxshi gʻoya har doim ham '
     u'sizniki emas.',
     u'Keyingi ishni boshlashdan oldin bitta savol bering: «Boshqa yoʻli '
     u'bormi?» Va javobni oxirigacha eshiting — gapini boʻlmang.'),

    (u'Toʻxtash ham ish',
     u'Siz doim bandsiz va bu sizga yoqadi. Lekin uzluksiz harakat bir kuni '
     u'toʻxtab qolish bilan tugaydi. Dam olish — dangasalik emas, ishning '
     u'bir qismi.',
     u'Haftada bitta kunni belgilang: oʻsha kuni birorta reja tuzmaysiz. '
     u'Ogʻir tuyulsa — aynan shuning uchun kerak.'),

    (u'Hammasini oʻzingiz qilmang',
     u'«Oʻzim qilganim tezroq» — bu toʻgʻri, lekin faqat bugun. Ish '
     u'boʻlishib berilmasa, jamoa oʻrganmaydi va butun yuk sizda qoladi.',
     u'Keyingi guruh ishida bitta vazifani toʻliq boshqa odamga bering va '
     u'ustidan turmang. U sizchalik qilmasligi mumkin — mayli.'),
],

'school': [
    (u'Guruh ishida',
     u'Siz tashkilotchisiz va bu jamoaga foyda. Faqat rejani boshida '
     u'koʻrsating: kim nima qiladi, qachongacha. Odamlar qarshi emas — '
     u'ular shunchaki sizning boshingizdagini koʻrmaydi.'),
    (u'Rejalashtirish',
     u'Sizga jadval yarashadi. Katta vazifani kichik qadamlarga boʻling va '
     u'har biriga muddat qoʻying — bu sizning tabiiy uslubingiz, undan '
     u'toʻliq foydalaning.'),
    (u'Imtihon va nazoratda',
     u'Tayyorgarlikni oldindan boshlaysiz — bu katta ustunlik. Faqat '
     u'oxirgi kecha ham «yana bir marta» deb oʻtirmang: charchagan miya '
     u'yaxshi ishlamaydi.'),
    (u'Toʻqnashuv boʻlganda',
     u'Tez gapirganingiz uchun baʼzan qattiq eshitilasiz. Siz xafa '
     u'qilmoqchi emassiz, lekin qarshi tomon buni bilmaydi. Muhim gapdan '
     u'oldin bir soniya toʻxtang.'),
    (u'Doʻstlik va oila',
     u'Siz doim band boʻlganingiz uchun yaqinlaringiz sizdan vaqt kutadi. '
     u'Reja tuzishni bilasiz — shu koʻnikmani ular uchun ham ishlating: '
     u'haftada bir marta, jadvalga yozilgan holda.'),
],

'future_fits': [
    (u'Loyiha va boshqaruv',
     u'Loyiha menejeri, operatsiyalar, tadbirkorlik, startap. Gʻoyani '
     u'muddatga, byudjetga va odamlarga boʻlish — aynan sizning ishingiz.'),
    (u'Tadbir va ishlab chiqarish',
     u'Tadbirlar tashkil qilish, prodyuserlik, logistika, qurilish '
     u'boshqaruvi. Koʻp qism, koʻp odam, aniq muddat.'),
    (u'Savdo va rivojlantirish',
     u'Sotuv, biznesni rivojlantirish, marketing. Odamlar bilan gaplashish '
     u'ham, natijani sanash ham kerak boʻlgan joy.'),
    (u'Sport va murabbiylik',
     u'Murabbiylik, jismoniy tarbiya, jamoa sportlari. Intizom va '
     u'ruhlantirish bir joyda kerak boʻladi.'),
],
'future_watch': u'Sizga eng ogʻir keladigan muhit — qaror sekin qabul '
                u'qilinadigan, hamma narsa uzoq kelishiladigan joylar. U '
                u'yerda siz tez zerikasiz va asabiylashasiz. Agar shunday '
                u'sohaga tushsangiz, oʻzingizga kichik, tez tugaydigan '
                u'vazifalar toping — aks holda gʻayratingiz sizni '
                u'charchatadi.',

'figure_why': u'Nodirabegim faqat sheʼr yozgan emas. U Qoʻqonda adabiy '
              u'muhitni uyushtirgan, madrasa va masjidlar qurdirgan, '
              u'shoirlarni bir joyga toʻplagan. Yaʼni u gʻoyani gʻoya '
              u'holida qoldirmagan — binoga, maktabga, jamoaga aylantirgan. '
              u'Sizning kuchingiz ham aynan shu yerda: fikrni koʻzga '
              u'koʻrinadigan narsaga aylantirishda.',

'practice': [
    u'Ishni boshlashdan oldin «boshqa yoʻli bormi?» deb soʻradim.',
    u'Bitta vazifani boshqa odamga toʻliq topshirdim.',
    u'Bir kun hech qanday reja tuzmadim.',
    u'Guruh ishida rejani boshida yozib koʻrsatdim.',
    u'Kimningdir gapini boʻlmasdan oxirigacha eshitdim.',
    u'Yaqin odamim bilan oldindan kelishilgan vaqt oʻtkazdim.',
    u'Bitta ishni «yetarlicha yaxshi» holatida tugatdim.',
],
'closing': u'Siz koʻp ish qila olasiz — bu allaqachon maʼlum. Endi ikkinchi '
           u'savol muhimroq: qaysi ishni? Tez yurish bilan toʻgʻri yoʻnalish '
           u'bir xil narsa emas.',
},


# ============================================================ ES|O ==========
'ES|O': {
'traits_note': u'Ochiqlik sizni notanish yoʻlga olib chiqadi, xotirjamlik '
               u'esa u yerda boshni yoʻqotmaslikka yordam beradi. '
               u'Qiziquvchan odam koʻp; sovuqqoni kam.',

'portrait': [
    u'Notanish narsani koʻrsangiz, avval fikr bildirmaysiz — sinab '
    u'koʻrasiz. Boshqalar «bu ishlamaydi» deb turganda siz ochib, '
    u'buzib, qaytadan yigʻib koʻrasiz. Xulosa keyin keladi.',

    u'Xavf sizni qoʻrqitmaydi, lekin siz koʻzni yumib sakraydigan odam '
    u'ham emassiz. Yangi narsaga kirishdan oldin oʻzingizcha hisob-kitob '
    u'qilasiz. Shuning uchun sizning tavakkalingiz koʻpincha oqlanadi.',

    u'Savol berish sizga tabiiy. «Nega shunday?», «Boshqacha boʻlsa nima '
    u'boʻladi?» — bu savollar sizda oʻz-oʻzidan tugʻiladi va javob '
    u'topilmaguncha yoqangizni qoʻyib yubormaydi.',

    u'Yolgʻiz ishlash sizni bezovta qilmaydi. Kutubxonada, xonada, '
    u'ustaxonada soatlab oʻtira olasiz. Aksincha, uzoq shovqin sizni '
    u'toliqtiradi.',

    u'Lekin qiziqishingiz tez koʻchadi. Bir narsani chala qoldirib, '
    u'ikkinchisiga oʻtib ketasiz — chunki yangisi hozir qiziqroq. Bir '
    u'yildan keyin ortga qarasangiz, boshlangan, lekin tugatilmagan '
    u'ishlar roʻyxati uzun boʻladi.',
],
'portrait_pull': u'Boshlash oson, tugatish qiyin. Tugatilgan bitta ish '
                 u'boshlangan oʻnta ishdan koʻproq narsa oʻrgatadi.',

'strengths': [
    (u'Notanish yoʻlni xotirjam tekshirasiz',
     u'Koʻpchilik notanish narsadan qochadi yoki unga koʻr-koʻrona '
     u'tashlanadi. Siz uchinchi yoʻlni tanlaysiz: sekin, bosqichma-bosqich '
     u'tekshirasiz.'),
    (u'Xatodan qoʻrqmaysiz',
     u'Ishlamagan urinish sizni tushkunlikka solmaydi — u siz uchun '
     u'maʼlumot. Bu aynan tadqiqotchining fikrlash tarzi.'),
    (u'Mustaqil ishlay olasiz',
     u'Sizga doimiy nazorat kerak emas. Vazifani tushunsangiz, oʻzingiz '
     u'olib ketasiz. Bu koʻnikma katta hayotda juda qadrlanadi.'),
    (u'Boshqalar koʻrmagan bogʻlanishni koʻrasiz',
     u'Turli sohalardan bilim yigʻasiz va ularni bir-biriga ulaysiz. '
     u'Yangi yechimlar koʻpincha shu yerdan chiqadi.'),
],

'growth': [
    (u'Bittasini oxirigacha olib boring',
     u'Yangi narsa doim qiziqroq tuyuladi — bu tuygʻu aldaydi. Chala '
     u'qolgan ish sizga hech narsa oʻrgatmaydi; oxirigacha borgan ish esa '
     u'eng qiyin, eng foydali qismini koʻrsatadi.',
     u'Hozir boshlangan ishlaringizdan bittasini tanlang va shu hafta uni '
     u'tugating. Kichik boʻlsin — muhimi tugatilgan boʻlsin.'),

    (u'Topganingizni odamlarga ayting',
     u'Siz koʻp narsa bilib olasiz, lekin oʻzingizda saqlaysiz. Natijada '
     u'atrofdagilar sizning nima bilishingizni bilmaydi va sizga mos ish '
     u'taklif qilinmaydi.',
     u'Shu hafta oʻrgangan bitta narsangizni bir odamga tushuntiring — '
     u'doʻstingizga, ukangizga yoki oʻqituvchingizga.'),

    (u'Zerikarli qism ham ishning bir boʻlagi',
     u'Har qanday qiziqarli ishning ichida takrorlanadigan, zerikarli '
     u'qismi bor: mashq, tekshirish, qayta yozish. Siz oʻsha yerda '
     u'toʻxtab qolasiz. Aslida mahorat aynan shu yerda tugʻiladi.',
     u'Zerikarli deb qoldirgan bitta ishni tanlang va unga 25 daqiqa '
     u'ajrating — taymer qoʻyib. Faqat 25 daqiqa.'),
],

'school': [
    (u'Qanday oʻrganganingiz maʼqul',
     u'Yod olish sizga ogʻir, tushunish esa oson. Yangi mavzuni «nega '
     u'shunday?» degan savol bilan boshlang — javobni topsangiz, qolgani '
     u'oʻzidan-oʻzi yodda qoladi.'),
    (u'Imtihon va nazoratda',
     u'Siz mavzuni tushunasiz, lekin talab qilingan shaklda yozishni '
     u'eʼtiborsiz qoldirishingiz mumkin. Bir marta shartni oxirigacha '
     u'oʻqing — koʻp ball shu yerda yoʻqoladi.'),
    (u'Guruh ishida',
     u'Siz gʻoya va yechim keltirasiz, lekin muvofiqlashtirishni '
     u'yoqtirmaysiz. Buni ochiq ayting: «men shu qismini olaman» deb '
     u'kelishib olish hammaga qulay.'),
    (u'Loyiha va tanlovlar',
     u'Fan olimpiadalari, ilmiy loyihalar, robototexnika, dasturlash '
     u'musobaqalari — sizning maydoningiz. Ular aynan tugatishni ham '
     u'oʻrgatadi.'),
    (u'Doʻstlik va oila',
     u'Siz yolgʻiz vaqtni qadrlaysiz va bu normal. Faqat yaqinlaringizga '
     u'buni tushuntiring: «men xafa emasman, shunchaki oʻylayapman». Aks '
     u'holda sukutingiz sovuqlik deb tushuniladi.'),
],

'future_fits': [
    (u'Fan va tadqiqot',
     u'Fizika, biologiya, kimyo, matematika, tibbiy tadqiqot. Savol '
     u'berish va sabr bilan tekshirish — bu ishning oʻzagi.'),
    (u'Muhandislik va texnologiya',
     u'Dasturlash, robototexnika, elektronika, sunʼiy intellekt. Buzib '
     u'koʻrish va qaytadan yigʻish shu yerda kasbga aylanadi.'),
    (u'Maʼlumot bilan ishlash',
     u'Maʼlumotlar tahlili, kiberxavfsizlik, geologiya, meteorologiya. '
     u'Sovuqqonlik va qiziquvchanlik ikkalasi ham talab qilinadi.'),
    (u'Dala va sayohat ishlari',
     u'Arxeologiya, ekologiya, geografiya, jurnalistika-tadqiqot. '
     u'Notanish sharoitda tinch ishlay olish kam uchraydigan sifat.'),
],
'future_watch': u'Sizga eng ogʻir keladigan joy — har kuni bir xil, '
                u'oʻzgarmaydigan va qatʼiy qoidalar bilan bogʻlangan ish. '
                u'U yerda siz tez soʻnasiz. Agar shunday sohani tanlasangiz, '
                u'ichidan oʻrganiladigan, yangilanadigan qismini toping — '
                u'aks holda bir yildan keyin ketgingiz keladi.',

'figure_why': u'Beruniy Hindistonga borganda u yerdagi odamlarni «notoʻgʻri» '
              u'deb baholamagan — ularning tilini oʻrgangan, kitoblarini '
              u'oʻqigan, keyin yozgan. U Yer sharining oʻlchamini hisoblagan, '
              u'yuzlab dorivor oʻsimlikni tavsiflagan, oʻnlab fanni birga '
              u'olib borgan. Notanish narsani hukm qilishdan oldin tekshirib '
              u'koʻrish — bu sizga tanish yondashuv.',

'practice': [
    u'Boshlangan bitta ishimni oxirigacha tugatdim.',
    u'Oʻrgangan narsamni bir odamga tushuntirdim.',
    u'Zerikarli qismga taymer qoʻyib 25 daqiqa ishladim.',
    u'Imtihon shartini oxirigacha oʻqib chiqdim.',
    u'Guruh ishida qaysi qismni olishimni ochiq aytdim.',
    u'Yaqinimga «men shunchaki oʻylayapman» deb tushuntirdim.',
    u'Bitta yangi narsani boshlashdan oldin bir hafta kutdim.',
],
'closing': u'Sizda savol koʻp — bu boylik. Faqat javob topilgandan keyin '
           u'toʻxtamang: topilgan javobni oxirigacha olib borish sizni '
           u'qiziquvchi odamdan mutaxassisga aylantiradi.',
},


# ============================================================ E|O ===========
'E|O': {
'traits_note': u'Yangilikka ochiqlik gʻoyani tugʻdiradi, kirishimlilik uni '
               u'odamlarga olib chiqadi. Shuning uchun sizning gʻoyangiz '
               u'daftarda qolmaydi — u tarqaladi.',

'portrait': [
    u'Sizda gʻoya tugamaydi. Bittasini aytib boʻlmasingizdan ikkinchisi '
    u'kelib qoladi. Baʼzan oʻzingiz ham ulgurmaysiz — shuning uchun '
    u'gapirasiz, chunki gapirganda gʻoya aniqroq boʻlib qoladi.',

    u'Siz tushuntira boshlaganingizda tinglayotgan odam qiziqib qoladi. '
    u'Bu koʻnikma emas, holat: sizning qiziqishingiz yuqumli. Xuddi shu '
    u'sabab odamlar sizni yodda saqlaydi.',

    u'Bir xillik sizni bosadi. Har kuni bir xil yoʻl, bir xil tartib, bir '
    u'xil suhbat — bir haftadan keyin siz oʻzgartirish qidira '
    u'boshlaysiz. Bu injiqlik emas, tabiiy ehtiyoj.',

    u'Notanish odam bilan gaplashish sizga oson. Yangi davra, yangi joy, '
    u'yangi mavzu — hammasi sizni charchatmaydi, aksincha uygʻotadi.',

    u'Lekin boshlangan ishlar koʻpayib ketadi. Har biri boshida juda '
    u'qiziq, oʻrtasida esa ogʻirlashadi — va aynan oʻsha payt yangi gʻoya '
    u'paydo boʻladi. Natijada koʻp narsa yarim yoʻlda qoladi.',
],
'portrait_pull': u'Gʻoya arzon, ijro qimmat. Dunyoni gʻoya oʻzgartirmaydi — '
                 u'oxirigacha olib borilgan gʻoya oʻzgartiradi.',

'strengths': [
    (u'Gʻoyani odamlarga yuqtira olasiz',
     u'Siz gapirganda odamlar ishonadi va qoʻshilishni xohlaydi. Bu '
     u'jamoani harakatga keltiradigan eng qimmatli narsalardan biri.'),
    (u'Yangi yechim topasiz',
     u'Hamma bir yoʻlni koʻrayotganda siz uchtasini koʻrasiz. Chalkash '
     u'vaziyatda bu ustunlikka aylanadi.'),
    (u'Odamlarni bogʻlaysiz',
     u'Siz koʻp odamni bilasiz va kimni kim bilan tanishtirish kerakligini '
     u'sezasiz. Bu koʻnikmaning qiymati yillar oʻtgani sari oshadi.'),
    (u'Notanish vaziyatda tez moslashasiz',
     u'Yangi muhit sizni sekinlashtirmaydi. Yangi maktab, yangi jamoa, '
     u'yangi shahar — siz tez oʻrnashasiz.'),
],

'growth': [
    (u'Bir vaqtda uchtadan koʻp ish tutmang',
     u'Gʻoya koʻp, vaqt kam. Hammasini birdan boshlasangiz, hech biri '
     u'tugamaydi va oxirida oʻzingizni «hech narsa qilmadim» deb his '
     u'qilasiz — bu adolatsiz, chunki siz juda koʻp ishladingiz.',
     u'Hozirgi boshlangan ishlaringizni bir varaqqa yozing va faqat '
     u'uchtasiga belgi qoʻying. Qolganini «keyinroq» roʻyxatiga oʻtkazing '
     u'— oʻchirmang, kechiktiring.'),

    (u'Tugatish uchun kichkina qiling',
     u'Sizning rejalaringiz katta boʻladi, shuning uchun tugatish uzoq. '
     u'Kichik versiyani tugatgan odam katta versiyani ham tugatadi; '
     u'aksincha emas.',
     u'Bitta gʻoyangizni oling va uning eng kichik shaklini shu hafta '
     u'tugating: bitta post, bitta chizma, bitta sahifa.'),

    (u'Tanqid — sizga emas, gʻoyaga',
     u'Gʻoya sizga yaqin boʻlgani uchun uni tanqid qilishsa, oʻzingizni '
     u'tanqid qilingandek his qilasiz. Aslida gʻoyani yaxshilash uchun '
     u'aynan shu tanqid kerak.',
     u'Keyingi gʻoyangizni bir odamga aytib, undan «bunda nima ishlamaydi?» '
     u'deb soʻrang. Javobni yozib oling va bahslashmang.'),
],

'school': [
    (u'Guruh ishida',
     u'Siz gʻoya va ruh berasiz — bu koʻp. Faqat kim nima qilishini '
     u'yozib qoʻyadigan odam ham kerak. Agar oʻzingiz emas boʻlsangiz, '
     u'oʻsha odamni toping va unga rahmat ayting.'),
    (u'Taqdimot va chiqishlarda',
     u'Bu sizning maydoningiz. Faqat mavzudan chetga chiqib ketmang — '
     u'oldindan uchta asosiy fikringizni yozib qoʻying va shulardan '
     u'chiqmang.'),
    (u'Qanday oʻrganganingiz maʼqul',
     u'Bir joyda uzoq oʻtirish sizga ogʻir. 25 daqiqa ishlab, 5 daqiqa '
     u'tanaffus qiling. Mavzuni birovga tushuntirib ham oʻrganing — bu '
     u'sizga eng tabiiy usul.'),
    (u'Imtihon va nazoratda',
     u'Asosiy xavf — tayyorgarlikni oxirgi kunga qoldirish, chunki oldin '
     u'boshqa qiziqroq narsalar bor edi. Kalendarga uch marta kichik '
     u'tayyorgarlik yozib qoʻying.'),
    (u'Doʻstlik va oila',
     u'Sizning atrofingizda odam koʻp va bu yaxshi. Faqat vaʼdalarga '
     u'ehtiyot boʻling: hayajonda berilgan vaʼda keyin ogʻirlik boʻlib '
     u'qaytadi. Ishonchingiz aynan shu yerda sinaladi.'),
],

'future_fits': [
    (u'Media va ijod',
     u'Jurnalistika, kontent, video, dizayn, reklama, yozuvchilik. Gʻoyani '
     u'topish ham, uni odamlarga yetkazish ham kerak.'),
    (u'Marketing va brend',
     u'Marketing, PR, ijtimoiy tarmoqlar, brend boshqaruvi. Odamlarni '
     u'qiziqtira olish — bu yerda toʻgʻridan-toʻgʻri kasb.'),
    (u'Taʼlim va targʻibot',
     u'Oʻqituvchilik, trenerlik, ilm-fan targʻiboti. Zerikarli mavzuni '
     u'qiziqarli qilish kamdan-kam odamning qoʻlidan keladi.'),
    (u'Tadbirkorlik',
     u'Startap, kichik biznes, ijodiy loyihalar. Yangi gʻoya va odamlarni '
     u'ishontirish — boshlangʻich kapitalning yarmi.'),
],
'future_watch': u'Sizga eng ogʻir keladigan joy — bir xil, qatʼiy jadval '
                u'bilan boradigan va yolgʻiz bajariladigan ish. U yerda '
                u'sizning eng kuchli tomonlaringiz ishlamaydi. Agar shunday '
                u'sohaga borsangiz, oʻzingizga odamlar bilan ishlaydigan '
                u'yoki yangilanib turadigan qismini shart qilib qoʻying.',

'figure_why': u'Zebunniso Begim saroyda tugʻilgan, lekin oson yoʻldan '
              u'yurmagan. U «Maxfiy» taxallusi bilan yozgan va butun bir '
              u'devon qoldirgan — yaʼni gʻoyani gapirib qoʻymay, yozib, '
              u'toʻplab, oxirigacha olib borgan. Uning kutubxonasi va '
              u'atrofidagi olimlar davrasi ham shundan: u odamlarni '
              u'gʻoya atrofiga yigʻa olgan.',

'practice': [
    u'Boshlangan ishlarimni yozib chiqdim va faqat uchtasini tanladim.',
    u'Bitta gʻoyamning eng kichik shaklini tugatdim.',
    u'Bir odamdan «bunda nima ishlamaydi?» deb soʻradim.',
    u'Chiqishdan oldin uchta asosiy fikrimni yozib qoʻydim.',
    u'25 daqiqa taymer bilan ishladim.',
    u'Hayajonda vaʼda berishdan oldin bir kun oʻyladim.',
    u'Bir mavzuni birovga tushuntirib oʻrgandim.',
],
'closing': u'Sizni eslab qolishadi — bu allaqachon shunday. Endi ikkinchi '
           u'qadam: eslab qolinadigan gʻoyani tugatilgan ishga aylantirish. '
           u'Shundan keyin sizni nafaqat eslashadi, balki kutishadi ham.',
},


# ============================================================ O|C ===========
'O|C': {
'traits_note': u'Yangilikka ochiqlik gʻoyani topadi, masʼuliyatlilik uni '
               u'qadamlarga boʻladi. Bu juda kuchli birikma: koʻp odam '
               u'yo orzu qiladi, yo bajaradi — siz ikkalasini qila olasiz.',

'portrait': [
    u'Sizda gʻoya paydo boʻlganda birinchi savolingiz «qanday qilib?» '
    u'boʻladi. Shuning uchun sizning gʻoyangiz tez orada roʻyxatga, '
    u'chizmaga yoki jadvalga aylanadi.',

    u'Ish qanday qilinishi kerakligi haqida sizning oʻz fikringiz bor. '
    u'Tayyor yoʻriqnomani koʻrsangiz ham, uni yaxshilash yoʻlini '
    u'oʻylaysiz. Bu sizni baʼzan qaysar qilib koʻrsatadi.',

    u'Boshlagan ishingizni tashlab ketmaysiz. Qiziqish soʻnsa ham '
    u'oxiriga yetkazasiz, chunki tugatilmagan ish sizni bezovta qiladi.',

    u'Sifat siz uchun muhim. «Boʻldi, shu ham yetadi» degan gapni qabul '
    u'qilishingiz qiyin. Shuning uchun sizning ishingiz koʻpincha '
    u'boshqalarnikidan puxtaroq chiqadi.',

    u'Lekin xuddi shu sifat talabi sizni sekinlashtiradi. Tugagan '
    u'ishni yana bir marta koʻrib chiqasiz, keyin yana. Baʼzan '
    u'topshirilmagan mukammal ish topshirilgan yaxshi ishdan yomonroq.',
],
'portrait_pull': u'Mukammal — yaxshining dushmani. Tugatilmagan aʼlo ish '
                 u'hech kimga foyda keltirmaydi.',

'strengths': [
    (u'Gʻoyani tizimga sola olasiz',
     u'Chalkash fikrni siz aniq qadamlarga boʻlasiz. Bu kamdan-kam '
     u'uchraydigan birikma va uni har qanday jamoa qidiradi.'),
    (u'Boshlagan ishingizni tugatasiz',
     u'Qiziqish soʻngan joyda koʻpchilik toʻxtaydi. Siz davom etasiz — '
     u'shuning uchun sizning natijangiz bor.'),
    (u'Puxta ishlaysiz',
     u'Sizning ishingizni ikki marta tekshirish shart emas. Bu ishonch '
     u'yillar davomida toʻplanadi va katta imkoniyatlar ochadi.'),
    (u'Uzoqni koʻra olasiz',
     u'Siz faqat bugungi qadamni emas, oxirgi natijani ham koʻrasiz. '
     u'Reja tuzganda bu farqni darhol sezish mumkin.'),
],

'growth': [
    (u'«Yetarlicha yaxshi» ham natija',
     u'Mukammallikka intilish sizni oldinga emas, orqaga tortishi mumkin. '
     u'Hech kim koʻrmagan mukammal ish — ishlamagan ish. Koʻpincha '
     u'80 foiz tayyor natija bugun 100 foizdan bir oydan keyin '
     u'foydaliroq.',
     u'Bitta ishga oldindan muddat qoʻying va oʻsha muddatda topshiring '
     u'— holati qanday boʻlsa shundayligicha. Bir marta sinab koʻring.'),

    (u'Odamlarni ishga qoʻshing',
     u'Siz yolgʻiz ishlashni afzal koʻrasiz, chunki oʻzingiz qilganingiz '
     u'aniqroq chiqadi. Lekin yolgʻiz olib boriladigan ishning hajmi '
     u'chegaralangan, va boshqalar sizdan oʻrganmaydi.',
     u'Keyingi loyihada bitta qismni boshqa odamga bering va uning '
     u'usuliga aralashmang. Natijani baholang, yoʻlni emas.'),

    (u'Reja buzilsa — bu ham reja',
     u'Sizning rejangiz aniq, shuning uchun u buzilganda siz ortiqcha '
     u'qiynalasiz. Aslida hech bir reja toʻliq bajarilmaydi; yaxshi reja '
     u'— oʻzgarishga joy qoldirgani.',
     u'Keyingi rejangizga «B varianti» degan bitta qator qoʻshing. Bir '
     u'jumla yetarli: ishlamasa nima qilaman.'),
],

'school': [
    (u'Loyiha va tanlovlar',
     u'Olimpiada, ilmiy loyiha, robototexnika, dasturlash tanlovlari — '
     u'sizning maydoningiz. Gʻoya ham, ijro ham talab qilinadi.'),
    (u'Rejalashtirish',
     u'Katta vazifani qadamlarga boʻlish sizning tabiiy uslubingiz. '
     u'Shuni qogʻozga chiqaring — boshingizdagi reja jamoaga koʻrinmaydi.'),
    (u'Imtihon va nazoratda',
     u'Tayyorgarlik sizda yaxshi. Asosiy xavf — bitta savolga haddan '
     u'ortiq vaqt sarflash. Vaqtni boʻlib oling va oʻtib keting; '
     u'qaytib kelasiz.'),
    (u'Guruh ishida',
     u'Sizning meʼyoringiz baland va bu boshqalarga bosim boʻlib '
     u'tuyulishi mumkin. Talabni tushuntiring: «men buni shunday '
     u'qilmoqchiman, chunki...» — shunda u injiqlik emas, sabab '
     u'boʻlib eshitiladi.'),
    (u'Doʻstlik va oila',
     u'Siz ishga berilib ketganingizda odamlar chetda qolib ketadi. '
     u'Ular sizdan xafa boʻlmaydi — shunchaki uzoqlashadi. Vaqtni '
     u'jadvalga yozishni bilasiz; ularni ham yozing.'),
],

'future_fits': [
    (u'Muhandislik va texnologiya',
     u'Dasturlash, mexanika, elektronika, sunʼiy intellekt, meʼmorchilik. '
     u'Yangi yechim ham, aniq ijro ham talab qilinadi.'),
    (u'Dizayn va mahsulot',
     u'Sanoat dizayni, UX, mahsulot boshqaruvi. Gʻoyani ishlaydigan '
     u'narsaga aylantirish — shu ishning taʼrifi.'),
    (u'Fan va tadqiqot',
     u'Fizika, matematika, biotexnologiya, tibbiy tadqiqot. Sabr va '
     u'aniqlik bu yerda gʻoyadan kam emas.'),
    (u'Tahlil va tizim',
     u'Maʼlumotlar tahlili, moliya, logistika, sifat nazorati. Chalkash '
     u'katta tizimni tartibga sola olish kam uchraydigan qobiliyat.'),
],
'future_watch': u'Sizga eng ogʻir keladigan joy — natija noaniq, qoidalar '
                u'har kuni oʻzgaradigan va hech narsa oxirigacha '
                u'yetkazilmaydigan muhit. Bunday joyda siz asabiylashasiz. '
                u'Agar shunday sohaga tushsangiz, oʻzingizga kichik, '
                u'tugaydigan vazifalar ajratib oling.',

'figure_why': u'Ulugʻbek yulduzlarni sanashni orzu qilgan — bu gʻoya. '
              u'Lekin u orzu bilan qolmagan: Samarqandda rasadxona '
              u'qurdirgan, asboblar yasattirgan, olimlarni yigʻgan va '
              u'1018 ta yulduzni roʻyxatga olgan. Uning jadvali Yevropada '
              u'ham asrlar davomida ishlatilgan. Orzuni oʻlchov va '
              u'jadvalga aylantirish — bu sizning yoʻlingiz.',

'practice': [
    u'Bitta ishni belgilangan muddatda, «yetarlicha yaxshi» holida topshirdim.',
    u'Loyihaning bir qismini boshqa odamga berdim va aralashmadim.',
    u'Rejamga «B varianti» qatorini qoʻshdim.',
    u'Imtihonda bitta savolda tiqilib qolmay, oʻtib ketdim.',
    u'Meʼyorimni jamoaga sababi bilan tushuntirdim.',
    u'Yaqinlarim uchun vaqtni jadvalga yozdim va bajardim.',
    u'Boshingizdagi rejani qogʻozga chiqarib, boshqalarga koʻrsatdim.',
],
'closing': u'Sizda gʻoya ham, intizom ham bor — bu kamdan-kam uchraydi. '
           u'Endi eng qiyin koʻnikma qoldi: qachon toʻxtashni bilish. '
           u'Tugatilgan ish mukammal ishdan koʻra koʻproq narsa oʻzgartiradi.',
},


# ============================================================ E|A ===========
'E|A': {
'traits_note': u'Kirishimlilik odamlarni yigʻadi, kelishuvchanlik ularni '
               u'birga ushlab turadi. Shuning uchun siz shunchaki '
               u'«hammaga tanish» odam emassiz — siz jamoani jamoa '
               u'qiladigan odamsiz.',

'portrait': [
    u'Siz kirgan xonada suhbat oʻzidan-oʻzi boshlanib ketadi. Buni '
    u'oʻylab qilmaysiz: shunchaki birov bilan gaplashasiz, keyin '
    u'yana birov qoʻshiladi va bir zumda davra paydo boʻladi.',

    u'Chetda qolgan odamni sezasiz. Yangi kelgan oʻquvchi, jimgina '
    u'oʻtirgan bola — koʻzingiz ularga tushadi va siz ularni yoningizga '
    u'chaqirasiz. Koʻpchilik buni umuman payqamaydi.',

    u'Odamlar bilan boʻlish sizga quvvat beradi. Uzoq yolgʻizlik esa '
    u'sizni sekin-asta boʻshashtiradi. Siz uchun dam olish — uxlash '
    u'emas, koʻpincha suhbat.',

    u'Janjal sizga jismonan ogʻir tuyuladi. Kimdir sizdan xafa boʻlsa, '
    u'buni bir kun emas, bir hafta oʻylab yurasiz. Shuning uchun siz '
    u'kelishishga birinchi boʻlib borasiz.',

    u'Lekin hamma bilan yaxshi boʻlishga urinib, oʻz fikringizni '
    u'aytmay qoʻyasiz. Suhbatda hammaga qoʻshilasiz, keyin uyda '
    u'«aslida men boshqacha oʻylagandim» deb oʻtirasiz. Sizning '
    u'fikringiz ham xuddi shunday muhim.',
],
'portrait_pull': u'Hammaga yoqish — maqsad emas. Sizni chin dildan '
                 u'yoqtiradigan odamlar sizning haqiqiy fikringizni '
                 u'eshitgandan keyin ham qoladi.',

'strengths': [
    (u'Odamlarni birlashtirasiz',
     u'Bir-birini bilmagan odamlar siz orqali tanishadi. Bu koʻzga '
     u'koʻrinmaydigan, lekin har qanday jamoada eng kerakli ish.'),
    (u'Chetda qolganni koʻrasiz',
     u'Bu shunchaki mehribonlik emas — bu eʼtibor. Koʻp odam qarab '
     u'turadi, lekin koʻrmaydi.'),
    (u'Muhitni yumshata olasiz',
     u'Tarang vaziyatda sizning bitta hazilingiz yoki bitta iliq '
     u'gapingiz butun xonani boʻshashtiradi.'),
    (u'Odamlar sizga ochiladi',
     u'Sizga gapirish oson. Shuning uchun siz koʻp narsani bilib '
     u'qolasiz — va shuning uchun ishonchni saqlash sizning zimmangizda.'),
],

'growth': [
    (u'Oʻz fikringizni ayting',
     u'Kelishmovchilikdan qochish uchun siz koʻpincha jim qolasiz yoki '
     u'qoʻshilib qoʻya qolasiz. Muammo shuki, keyin oʻzingizdan '
     u'norozi boʻlasiz — va bu norozilik sekin toʻplanadi.',
     u'Shu hafta bir marta: «Men boshqacha oʻylayman» deb boshlang va '
     u'sababini ayting. Bir marta. Munosabat buzilmasligini koʻrasiz.'),

    (u'Hamma sizni yoqtirmasligi mumkin — bu normal',
     u'Siz hammaga yaxshi boʻlishga urinasiz, lekin bu imkonsiz. '
     u'Kimdir sizni sababsiz yoqtirmasligi mumkin va bu siz haqingizda '
     u'hech narsa demaydi.',
     u'Roʻyxat tuzing: sizga chin dildan yaqin 5 ta odam. Shu haftada '
     u'shu beshtasiga eʼtibor bering, qolganiga emas.'),

    (u'Yolgʻiz qolishni ham oʻrganing',
     u'Doim odamlar orasida boʻlsangiz, oʻz fikringizni eshitish '
     u'imkoni qolmaydi. Baʼzi savollarga javob faqat jimlikda topiladi.',
     u'Haftada bir marta 30 daqiqa: telefon uzoqda, yolgʻiz. Yurish, '
     u'yozish yoki shunchaki oʻtirish. Birinchi marta ogʻir boʻladi.'),
],

'school': [
    (u'Guruh ishida',
     u'Siz jamoani ushlab turasiz va hech kimni chetda qoldirmaysiz. '
     u'Faqat bir narsaga eʼtibor bering: ishning oʻzi ham bajarilishi '
     u'kerak. Yaxshi muhit natijaning oʻrnini bosmaydi.'),
    (u'Taqdimot va chiqishlarda',
     u'Odamlar oldida gapirish sizga oson. Bu katta ustunlik — undan '
     u'foydalaning va guruh nomidan chiqishni oʻz zimmangizga oling.'),
    (u'Qanday oʻrganganingiz maʼqul',
     u'Yolgʻiz oʻqish sizni tez zeriktiradi. Doʻstingiz bilan navbatma-navbat '
     u'tushuntirib oʻqing — sizga eng tabiiy va eng samarali usul.'),
    (u'Toʻqnashuv boʻlganda',
     u'Siz kelishishga birinchi borasiz va bu yaxshi sifat. Faqat '
     u'kechirim soʻrash bilan rozi boʻlishni aralashtirmang: '
     u'«uzr» deyish «sen haqsan» degani emas.'),
    (u'Doʻstlik va oila',
     u'Siz doʻstlikka koʻp kuch berasiz. Baʼzan bir tomonlama boʻlib '
     u'qoladi — siz doim qoʻngʻiroq qilasiz, siz doim soʻraysiz. Bir '
     u'oy kuzating: kim sizni oʻzi qidiradi?'),
],

'future_fits': [
    (u'Taʼlim va tarbiya',
     u'Oʻqituvchilik, maktabgacha taʼlim, trenerlik, mentorlik. Odamni '
     u'koʻra bilish bu ishning yarmi.'),
    (u'Odamlar bilan ishlash',
     u'HR, mijozlar bilan ishlash, mehmondoʻstlik, savdo, ijtimoiy ish. '
     u'Notanish odam bilan tez til topish — toʻgʻridan-toʻgʻri kasbiy '
     u'koʻnikma.'),
    (u'Tibbiyot va yordam',
     u'Hamshiralik, shifokorlik, psixologiya, reabilitatsiya. Bemor '
     u'bilan gaplasha bilish davolashning bir qismi.'),
    (u'Tadbir va jamoat ishlari',
     u'Tadbirlar tashkil qilish, jamoatchilik bilan aloqa, ijtimoiy '
     u'loyihalar, koʻngillilik. Odamlarni bir maqsad atrofida yigʻish.'),
],
'future_watch': u'Sizga eng ogʻir keladigan joy — kun boʻyi yolgʻiz, jim '
                u'va odamlarsiz oʻtadigan ish. U yerda siz bir necha '
                u'oydan keyin soʻnasiz. Agar shunday yoʻnalishni tanlasangiz, '
                u'jamoada ishlaydigan yoki natijani odamlarga taqdim '
                u'qiladigan qismini oʻzingizga shart qilib qoʻying.',

'figure_why': u'Navoiy fors tilida yozish odat boʻlgan davrda oʻz tilida '
              u'yozgan — chunki u odamlar bir-birini tushunishini '
              u'xohlagan. U shoirlarni, olimlarni, meʼmorlarni qoʻllagan, '
              u'ularga yordam bergan, ularni bir-biri bilan tanishtirgan. '
              u'Uning eng katta ishi bitta kitob emas, balki oʻzi atrofida '
              u'yaratgan muhit edi. Bu sizga tanish tuygʻu boʻlsa kerak.',

'practice': [
    u'Bir marta «men boshqacha oʻylayman» dedim va sababini aytdim.',
    u'Menga chin dildan yaqin 5 odamni yozib chiqdim.',
    u'Haftada bir marta 30 daqiqa yolgʻiz vaqt oʻtkazdim.',
    u'Guruh ishida natijani ham tekshirdim, faqat muhitni emas.',
    u'Bir oy kuzatdim: kim meni oʻzi qidiradi.',
    u'Kechirim soʻramasdan oʻz fikrimda qoldim.',
    u'Doʻstim bilan navbatma-navbat tushuntirib dars tayyorladim.',
],
'closing': u'Siz odamlarni yaqinlashtirasiz — bu kamdan-kam uchraydigan '
           u'sovgʻa. Faqat oʻzingizni ham oʻsha odamlar roʻyxatiga '
           u'kiriting. Sizga gʻamxoʻrlik qiladigan odam ham kerak.',
},


# ============================================================ O|A ===========
'O|A': {
'traits_note': u'Yangilikka ochiqlik yechim izlaydi, kelishuvchanlik esa '
               u'«bu odamga qanday taʼsir qiladi?» deb soʻraydi. Shuning '
               u'uchun sizning yechimlaringiz nafaqat aqlli, balki '
               u'insoniy ham boʻladi.',

'portrait': [
    u'Muammoni koʻrganingizda birinchi oʻylaydiganingiz — odamlar. '
    u'«Buni qanday tuzatish mumkin?» degan savoldan oldin sizda '
    u'«bu kimga ogʻir boʻlyapti?» degan savol tugʻiladi.',

    u'Sizda gʻoya koʻp, lekin ular koʻpincha bir yoʻnalishda: biror '
    u'narsani odamlar uchun qulayroq, adolatliroq yoki chiroyliroq '
    u'qilish. Sof texnik masala sizni kamroq qiziqtiradi.',

    u'Siz odamlarning holatini tez ilgʻaysiz va shu bilan birga '
    u'ularning oʻrnida boʻlishni tasavvur qila olasiz. Bu ikkisi '
    u'birga kelganda kuchli narsa chiqadi — lekin ogʻir ham boʻladi.',

    u'Boshqalarning muammosi sizga yopishib qoladi. Kimdir sizga '
    u'dardini aytsa, siz uni uyingizgacha olib ketasiz va kechqurun '
    u'ham oʻsha haqda oʻylaysiz.',

    u'Gʻoyalaringiz koʻpincha oxirigacha borib yetmaydi. Boshida '
    u'ilhom koʻp, lekin reja va muddat sizga tabiiy emas. Natijada '
    u'yaxshi fikrlar daftarda qoladi.',
],
'portrait_pull': u'Hammaning ogʻrigʻini oʻz zimmangizga olsangiz, hech '
                 u'kimga yordam bera olmay qolasiz. Yordam beradigan '
                 u'odamning ham quvvati tugaydi.',

'strengths': [
    (u'Foydali va insoniy yechim topasiz',
     u'Siz «ishlaydimi?» va «odamga yaxshimi?» degan ikkala savolni '
     u'birga soʻraysiz. Koʻp yechim aynan ikkinchi savol soʻralmagani '
     u'uchun buziladi.'),
    (u'Odamning oʻrniga oʻzingizni qoʻya olasiz',
     u'Bu koʻnikma dizayndan tortib tibbiyotgacha hamma joyda kerak '
     u'va uni oʻrgatish juda qiyin.'),
    (u'Yangi narsadan qoʻrqmaysiz',
     u'Notanish gʻoya sizni qiziqtiradi. Bu ochiqlik sizni butun umr '
     u'oʻrganib yuradigan odam qiladi.'),
    (u'Ishonch uygʻotasiz',
     u'Odamlar sizga ochiladi, chunki siz hukm qilmaysiz. Bu sizga '
     u'boshqalar koʻrmagan maʼlumotni beradi.'),
],

'growth': [
    (u'Boshqaning yukini oʻzingizga olmang',
     u'Birovni tinglash bilan uning muammosini oʻz zimmangizga olish — '
     u'ikki xil narsa. Birinchisi yordam beradi, ikkinchisi ikkalangizni '
     u'ham charchatadi.',
     u'Keyingi safar birov dardini aytganda shunday soʻrang: «Men '
     u'qanday yordam bera olaman?» Javobini kutinng — koʻpincha '
     u'shunchaki tinglash yetarli boʻladi.'),

    (u'Gʻoyani birinchi qadamga aylantiring',
     u'Sizning fikrlaringiz yaxshi, lekin ular koʻpincha «bir kun '
     u'qilaman» holatida qoladi. Katta reja emas — bitta kichik qadam '
     u'yetarli.',
     u'Daftardagi bitta gʻoyangizni oling va uning eng kichik birinchi '
     u'qadamini shu hafta bajaring: bitta xabar yozing, bitta odamdan '
     u'soʻrang, bitta sahifa chizing.'),

    (u'Oʻzingizni ham roʻyxatga qoʻshing',
     u'Siz boshqalarga kerakli narsani sezasiz, lekin oʻzingizga nima '
     u'kerakligini kam oʻylaysiz. Bu olijanoblik emas — bu odat, va '
     u'uni oʻzgartirish mumkin.',
     u'Har kuni kechqurun bitta savolga javob yozing: «Bugun menga '
     u'nima kerak edi?» Bir hafta yozing va oʻqib chiqing.'),
],

'school': [
    (u'Guruh ishida',
     u'Siz gʻoya ham berasiz, muhitni ham saqlaysiz. Faqat muddat va '
     u'vazifalarni yozadigan odam ham kerak — bu siz boʻlmasangiz, '
     u'ochiq ayting va oʻshanday odamni toping.'),
    (u'Qanday oʻrganganingiz maʼqul',
     u'Sizga «nega bu muhim?» degan savol javob berilsa, mavzu '
     u'ochiladi. Har bir yangi mavzuni real hayotdagi bitta odam '
     u'bilan bogʻlab koʻring.'),
    (u'Imtihon va nazoratda',
     u'Siz mavzuni tushunasiz, lekin talab qilingan shakl sizga '
     u'ikkinchi darajali tuyuladi. Baholar aynan shu yerda '
     u'yoʻqoladi — shartni oxirigacha oʻqing.'),
    (u'Toʻqnashuv boʻlganda',
     u'Siz ikkala tomonni ham tushunasiz va shuning uchun qiynalasiz. '
     u'Hammani rozi qilishga urinmang — baʼzan halol javob '
     u'yumshoq javobdan foydaliroq.'),
    (u'Doʻstlik va oila',
     u'Sizga koʻp dard aytishadi. Bu ishonch belgisi, lekin quvvat '
     u'talab qiladi. Oʻzingizga ham gapiradigan odam toping: '
     u'tinglovchi ham tinglanishi kerak.'),
],

'future_fits': [
    (u'Taʼlim va psixologiya',
     u'Oʻqituvchilik, maktab psixologi, maxsus taʼlim, mentorlik. '
     u'Odamni tushunish va yangi usul izlash birga kerak.'),
    (u'Ijtimoiy loyihalar',
     u'Nodavlat tashkilotlar, koʻngillilik, jamoat sogʻligʻi, '
     u'huquqni himoya qilish. Muammoni odamlar tomonidan koʻrish — '
     u'bu ishning asosi.'),
    (u'Odamga qaratilgan dizayn',
     u'UX/UI dizayn, xizmat dizayni, arxitektura, ilovalar. «Bu '
     u'odamga qulaymi?» degan savol butun kasbning oʻzagi.'),
    (u'Tibbiyot va reabilitatsiya',
     u'Shifokorlik, hamshiralik, logopediya, terapiya. Yangi usullar '
     u'ham, insoniy munosabat ham talab qilinadi.'),
],
'future_watch': u'Sizga eng ogʻir keladigan joy — natija faqat raqam bilan '
                u'oʻlchanadigan, qattiq raqobatli va odamlar hisobga '
                u'olinmaydigan muhitlar. U yerda siz oʻzingizni notoʻgʻri '
                u'joyda his qilasiz. Agar shunday sohaga borsangiz, ichida '
                u'odamlarga tegishli qismini toping va oʻshani oʻz '
                u'zimmangizga oling.',

'figure_why': u'Anbar Otin oʻz davrida saroy shoirlari haqida emas, oddiy '
              u'odamlar — ayollar, kambagʻallar, koʻrinmay qolganlar '
              u'haqida yozgan. Buning uchun uni maqtashmagan. U kim '
              u'haqida yozishni tanlaganida osonini emas, kerakligini '
              u'tanlagan. Muammoni odamlar tomonidan koʻrish — siz '
              u'uchun ham xuddi shunday tabiiy.',

'practice': [
    u'Birov dardini aytganda «qanday yordam bera olaman?» deb soʻradim.',
    u'Bitta gʻoyamning birinchi kichik qadamini bajardim.',
    u'Bir hafta har kuni «bugun menga nima kerak edi?» deb yozdim.',
    u'Bir marta yumshoq emas, halol javob berdim.',
    u'Imtihon shartini oxirigacha oʻqidim.',
    u'Oʻzim gapiradigan bitta odam topdim va gapirdim.',
    u'Guruh ishida muddatlarni yozadigan odamni aniqlab oldim.',
],
'closing': u'Siz dunyoni odamlar orqali koʻrasiz — bu kamdan-kam '
           u'uchraydigan qarash. Faqat esda tuting: siz ham oʻsha '
           u'odamlardan birisiz.',
},


# ============================================================ ES|C ==========
'ES|C': {
'traits_note': u'Xotirjamlik uzoq yoʻlda asabni saqlaydi, masʼuliyatlilik '
               u'esa yoʻldan chalgʻitmaydi. Bu birikma tez natija '
               u'bermaydi — lekin u eng uzoqqa boradigan birikma.',

'portrait': [
    u'Siz reja tuzasiz va rejadan chalgʻimaysiz. Atrofda nima '
    u'boʻlmasin, oʻz ishingizni davom ettirasiz. Buni maxsus '
    u'qilmaysiz — shunchaki boshqacha ishlashni bilmaysiz.',

    u'Boshqalar taslim boʻlgan joyda siz hali ishlab turasiz. Uzoq '
    u'muddatli ish — imtihonga uch oy tayyorgarlik, bir yillik '
    u'loyiha — sizni qoʻrqitmaydi.',

    u'Shovqin va tartibsizlik sizni chalgʻitadi, lekin sarosimaga '
    u'solmaydi. Siz shunchaki chetga chiqib, oʻz ishingizni '
    u'qilishda davom etasiz.',

    u'Vaʼda bergan muddatingizni bajarasiz. Odamlar buni bilib '
    u'qolgan va shuning uchun sizga eng muhim ishlarni ishonishadi.',

    u'Lekin reja buzilganda qiynalasiz. Kutilmagan oʻzgarish — '
    u'imtihon sanasi surildi, jamoadan biri ketdi — sizni '
    u'boshqalardan koʻra koʻproq bezovta qiladi, garchi tashqaridan '
    u'buni koʻrsatmasangiz ham.',
],
'portrait_pull': u'Yoʻlni oʻzgartirish — magʻlubiyat emas. Xarita '
                 u'notoʻgʻri boʻlsa, xaritaga sodiq qolish aql emas.',

'strengths': [
    (u'Uzoq masofaga chidaysiz',
     u'Koʻpchilik boshlaydi, oz qismi tugatadi. Sizning ustunligingiz '
     u'tezlikda emas — davomiylikda. Katta natijalar aynan shunday '
     u'quriladi.'),
    (u'Sizga ishonsa boʻladi',
     u'Aytgan muddatingizda ishni topshirasiz. Bu oddiy koʻrinadi, '
     u'lekin bu bitta sifat butun karyerani koʻtaradi.'),
    (u'Bosim sizni buzmaydi',
     u'Muddat yaqinlashganda ham sizning ishingiz sifati tushmaydi. '
     u'Bu tibbiyotdan muhandislikkacha hamma joyda qadrlanadi.'),
    (u'Tartib sola olasiz',
     u'Chalkash vaziyatni siz bosqichlarga boʻlasiz va oldinga '
     u'yurasiz. Atrofdagilar buni koʻrib xotirjam boʻladi.'),
],

'growth': [
    (u'Rejani oʻzgartirishni oʻrganing',
     u'Sizning kuchingiz — rejaga sodiqlik. Lekin sharoit oʻzgarganda '
     u'eski rejaga yopishib qolish xuddi shu kuchni zaiflikka '
     u'aylantiradi. Yaxshi reja — tuzatiladigan reja.',
     u'Hozirgi rejalaringizdan bittasini oling va ataylab bitta '
     u'qismini oʻzgartiring. Noqulay boʻladi — maqsad ham shu.'),

    (u'Dam olishni jadvalga yozing',
     u'Siz toʻxtamaysiz, chunki toʻxtash sizga vaqt isrofidek '
     u'tuyuladi. Aslida dam olmagan odam sekin ishlaydi va buni '
     u'oʻzi sezmaydi.',
     u'Haftalik jadvalingizga «hech narsa qilmaslik» uchun ikki soat '
     u'yozing — xuddi dars kabi, oʻchirib boʻlmaydigan qilib.'),

    (u'Boshqalar boshqacha ishlaydi',
     u'Sizga tartibsiz koʻringan odam aslida boshqa uslubda '
     u'ishlayotgan boʻlishi mumkin. Ular sizga oʻxshamagani uchun '
     u'ularni ishonchsiz deb hisoblash — xato.',
     u'Guruh ishida bitta odamning uslubiga aralashmang. Faqat '
     u'natijani va muddatni kelishib oling.'),
],

'school': [
    (u'Imtihon va nazoratda',
     u'Bu sizning maydoningiz: oldindan tayyorlanish va bosim '
     u'ostida sifatni saqlash. Faqat kutilmagan savol chiqsa '
     u'ortiqcha qiynalmang — birinchi javobingiz koʻpincha '
     u'toʻgʻri boʻladi.'),
    (u'Rejalashtirish',
     u'Katta maqsadni oylik va haftalik qadamlarga boʻlish sizga '
     u'tabiiy. Buni doʻstlaringizga ham oʻrgating — bu ular uchun '
     u'katta yordam.'),
    (u'Guruh ishida',
     u'Siz ishonchli boʻgʻinsiz. Faqat butun yukni oʻz zimmangizga '
     u'olmang: «men bajaraman» deyish oson, lekin jamoa shunda '
     u'oʻrganmaydi.'),
    (u'Kutilmagan oʻzgarishda',
     u'Jadval oʻzgarganda birinchi reaksiyangiz — asabiylashish. '
     u'Bir kun kuting, keyin yangi reja tuzing. Bir kunlik pauza '
     u'koʻp narsani hal qiladi.'),
    (u'Doʻstlik va oila',
     u'Siz ishga berilib ketganingizda odamlar chetda qoladi va '
     u'buni sezmaysiz. Yaqinlaringiz uchun vaqtni ham xuddi dars '
     u'kabi jadvalga yozing.'),
],

'future_fits': [
    (u'Muhandislik va texnika',
     u'Qurilish, mashinasozlik, energetika, dasturlash. Uzoq '
     u'loyihalar va aniq talablar sizga qulay.'),
    (u'Moliya va huquq',
     u'Buxgalteriya, audit, moliyaviy tahlil, huquqshunoslik. '
     u'Diqqat va izchillik bu yerda asosiy talab.'),
    (u'Tibbiyot va farmatsevtika',
     u'Shifokorlik, laboratoriya, farmatsevtika. Bosim ostida '
     u'xato qilmaslik — kasbning oʻzagi.'),
    (u'Logistika va boshqaruv',
     u'Taʼminot zanjiri, ishlab chiqarish boshqaruvi, davlat '
     u'xizmati, harbiy xizmat. Katta tizimni barqaror ushlab '
     u'turish.'),
],
'future_watch': u'Sizga eng ogʻir keladigan joy — talablar har kuni '
                u'oʻzgaradigan, natija noaniq va hamma narsa oxirgi '
                u'daqiqada hal boʻladigan muhit. Bunday joyda siz '
                u'tinch koʻrinasiz, lekin ichingizdan charchaysiz. '
                u'Bunday sohani tanlasangiz, oʻzingizga oʻzgarmaydigan '
                u'kichik tartiblar yarating.',

'figure_why': u'Al-Xorazmiy murakkab masalani bir zarba bilan hal '
              u'qilmagan — uni takrorlanadigan, aniq qadamlarga '
              u'boʻlgan. Shu darajada aniq boʻlganki, bugungi butun '
              u'dasturlash uning nomidan olingan soʻz bilan ataladi: '
              u'algoritm. Katta natija shovqindan emas, tartibdan '
              u'chiqadi — bu sizning ishlash uslubingiz.',

'practice': [
    u'Rejamning bitta qismini ataylab oʻzgartirdim.',
    u'Jadvalimga dam olish uchun ikki soat yozdim va bajardim.',
    u'Guruhdagi bir odamning uslubiga aralashmadim.',
    u'Kutilmagan oʻzgarishdan keyin bir kun kutib, yangi reja tuzdim.',
    u'Yaqinlarim uchun vaqtni jadvalga yozdim.',
    u'Butun yukni oʻzim olmadim — bir qismini boʻlishdim.',
    u'Rejalashtirish usulimni bir doʻstimga oʻrgatdim.',
],
'closing': u'Sizning kuchingiz bir kunda koʻrinmaydi — u bir yilda '
           u'koʻrinadi. Shuning uchun boshqalar bilan bugungi kun '
           u'boʻyicha oʻlchanmang. Uzoq yoʻlda siz oldinda boʻlasiz.',
},


# ============================================================ A|C ===========
'A|C': {
'traits_note': u'Kelishuvchanlik odamlarni koʻradi, masʼuliyatlilik '
               u'soʻzida turadi. Bu ikkisi birga kelganda «tayanch» '
               u'chiqadi — atrofdagilar bilmagan holda suyanadigan odam.',

'portrait': [
    u'Vaʼda berishdan oldin oʻylaysiz. Chunki siz uchun aytilgan gap '
    u'— bajarilishi shart boʻlgan gap. Koʻpchilik osongina «ha, '
    u'qilaman» deydi; siz avval ulgurasizmi-yoʻqmi, shuni oʻylaysiz.',

    u'Shuning uchun muhim ish koʻpincha aynan sizga topshiriladi. '
    u'Oʻqituvchi ham, doʻstlaringiz ham buni oʻzlari sezmagan holda '
    u'qiladi — sizga ishonish oson.',

    u'Odamlarning holatiga eʼtiborlisiz. Kimdir ulgurmayotganini '
    u'koʻrsangiz, soʻramasa ham yordamga tushasiz. Bu sizga '
    u'majburiyat emas, oddiy narsa boʻlib tuyuladi.',

    u'Tartib va aniqlik sizni tinchlantiradi. Nima qilish '
    u'kerakligini bilsangiz, xotirjam ishlaysiz. Chalkashlik esa '
    u'sizni bezovta qiladi.',

    u'Lekin yuk sekin-asta sizga toʻplanadi. Har bir alohida ish '
    u'kichik koʻrinadi va siz rad etolmaysiz. Bir kuni ortga '
    u'qarasangiz, hammasini yolgʻiz koʻtarib yurgan boʻlasiz — va '
    u'buni hech kim bilmaydi ham.',
],
'portrait_pull': u'Yordam soʻrash zaiflik emas. Yolgʻiz koʻtarilgan yuk '
                 u'bir kuni tushadi — va u tushganda hech kim '
                 u'tayyor boʻlmaydi.',

'strengths': [
    (u'Soʻzingizda turasiz',
     u'Aytgan ishingizni bajarasiz. Bu bitta sifat sizni butun umr '
     u'olib yuradi — bugungi sinfda ham, kelajakdagi ishda ham.'),
    (u'Odamlarni koʻrasiz',
     u'Kim qiynalayotganini, kim ulgurmayotganini sezasiz. Bu '
     u'eʼtibor har qanday jamoani mustahkam qiladi.'),
    (u'Puxta ishlaysiz',
     u'Sizning ishingizni qayta tekshirish shart emas. Bu ishonch '
     u'juda sekin toʻplanadi va juda qadrlanadi.'),
    (u'Tinchlik olib kelasiz',
     u'Siz bor jamoada kamroq janjal, kamroq chalkashlik boʻladi. '
     u'Buni odamlar koʻrmaydi — lekin siz yoʻq boʻlsangiz darhol '
     u'sezishadi.'),
],

'growth': [
    (u'Yordam soʻrashni oʻrganing',
     u'Siz hammaga yordam berasiz, lekin oʻzingiz soʻramaysiz — '
     u'chunki «bezovta qilmay» deb oʻylaysiz. Aslida odamlar sizga '
     u'yordam berishdan xursand boʻladi; siz ularga bu imkonni '
     u'bermayapsiz.',
     u'Shu hafta bitta ishda ochiq yordam soʻrang. Kichik boʻlsin: '
     u'«shu joyini tushuntirib yuborasanmi?» Bir marta.'),

    (u'Ishni boʻlishing va nazorat qilmang',
     u'«Oʻzim qilganim aniqroq» — bu koʻpincha toʻgʻri. Lekin '
     u'shuning uchun yuk hech qachon kamaymaydi va jamoa '
     u'oʻrganmaydi.',
     u'Keyingi guruh ishida bitta vazifani toʻliq boshqa odamga '
     u'bering va ustidan turmang. Natija sizchalik boʻlmasligi '
     u'mumkin — mayli.'),

    (u'Qilgan ishingizni ayting',
     u'Siz jimgina ishlaysiz va maqtanishni yoqtirmaysiz. Natijada '
     u'sizning hissangiz koʻrinmay qoladi va boshqalar sizga '
     u'yana koʻproq ish beradi.',
     u'Ish tugagach bir jumla ayting: «men shu qismini qildim». '
     u'Maqtanish emas — maʼlumot.'),
],

'school': [
    (u'Guruh ishida',
     u'Siz eng ishonchli boʻgʻinsiz va hamma buni biladi. Aynan '
     u'shuning uchun ish sizga toʻplanadi. Boshida rollarni yozib '
     u'boʻlib oling — keyin emas, boshida.'),
    (u'Imtihon va nazoratda',
     u'Tayyorgarlik sizda yaxshi. Xavf — boshqalarga yordam berib, '
     u'oʻz tayyorgarligingizni oxirgi kunga qoldirish. Avval '
     u'oʻzingiznikini bajaring.'),
    (u'Qanday oʻrganganingiz maʼqul',
     u'Sizga aniq reja va bosqichlar yarashadi. Mavzuni birovga '
     u'tushuntirish ham sizga yaxshi ishlaydi — siz buni allaqachon '
     u'qilib yurgan boʻlsangiz kerak.'),
    (u'Toʻqnashuv boʻlganda',
     u'Siz nizodan qochasiz va koʻpincha oʻzingiz yon berasiz. '
     u'Yon berish bir marta — yaxshi; har safar — odat. Farqni '
     u'sezib turing.'),
    (u'Doʻstlik va oila',
     u'Sizga tayanishadi. Bu yaxshi, lekin ikki tomonlama boʻlishi '
     u'kerak. Bir oy kuzating: qiyin kuningizda siz kimga '
     u'qoʻngʻiroq qilasiz?'),
],

'future_fits': [
    (u'Tibbiyot va parvarish',
     u'Hamshiralik, shifokorlik, farmatsevtika, reabilitatsiya. '
     u'Aniqlik va odamga eʼtibor birga kerak boʻladigan soha.'),
    (u'Taʼlim',
     u'Oʻqituvchilik, maktabgacha taʼlim, maxsus taʼlim, kutubxona. '
     u'Sabr va izchillik bu ishning asosi.'),
    (u'Boshqaruv va hujjat ishi',
     u'Buxgalteriya, ofis boshqaruvi, HR, notariat, sifat nazorati. '
     u'Ishonchli odam bu joylarda oltin qadrida.'),
    (u'Xizmat va yordam koʻrsatish',
     u'Mijozlarni qoʻllab-quvvatlash, ijtimoiy ish, davlat '
     u'xizmatlari. Odam bilan ishlash ham, tartib ham talab '
     u'qilinadi.'),
],
'future_watch': u'Sizga eng ogʻir keladigan joy — doimiy raqobat, qattiq '
                u'muzokara va oʻz hissangizni baland ovozda talab qilish '
                u'kerak boʻlgan muhitlar. U yerda sizning ishingiz '
                u'koʻrinmay qolishi mumkin. Bunday sohani tanlasangiz, '
                u'qilgan ishingizni yozib borish odatini oldindan '
                u'shakllantiring.',

'figure_why': u'Dilshod Barno ellik yil davomida 891 nafar qizga oʻqish '
              u'va yozishni oʻrgatgan. Ellik yil — bu ilhom emas, bu '
              u'izchillik. Uning nomi mashhur boʻlmagan, lekin oʻsha '
              u'891 ta hayot oʻzgargan. Katta ishlar koʻpincha '
              u'shunday qilinadi: har kuni, jimgina, oxirigacha.',

'practice': [
    u'Bitta ishda ochiq yordam soʻradim.',
    u'Bitta vazifani boshqa odamga berdim va ustidan turmadim.',
    u'Ish tugagach «men shu qismini qildim» dedim.',
    u'Guruh ishida rollarni boshida yozib boʻlib oldim.',
    u'Avval oʻz tayyorgarligimni bajardim, keyin yordam berdim.',
    u'Bir marta yon bermay, oʻz fikrimda qoldim.',
    u'Qiyin kunimda bir odamga oʻzim qoʻngʻiroq qildim.',
],
'closing': u'Sizga suyanishadi va bu bejiz emas. Faqat bitta narsani '
           u'unutmang: tayanch ham tayanchga muhtoj. Yordam soʻragan '
           u'kuningiz sizning ishonchingiz kamaymaydi — ortadi.',
},

}
