# -*- coding: utf-8 -*-
u"""Life-area detail for the archetype pages: Oilada, Maktabda, Munosabatlarda,
plus suggested directions and the historical figure.

THE ONE RULE, same as guide_content.py: if a sentence would be true of any
student, cut it. "You are a good friend" is worthless. "Yarim tunda ham
telefoningiz ochiq" is worth reading, because a different archetype would not
have it written about them.

Each area has five strengths and five weaknesses, each a short bolded label plus
one concrete sentence. The weaknesses are written as things that happen TO the
reader, never as faults — a 13-year-old reading "you are a coward" stops reading,
and stops trusting the strengths too.


ON THE PERCENTAGES
------------------
The percentage beside each direction is NOT a measured job-fit probability.
No such measurement exists for Uzbek adolescents — establishing it is the
entire point of the data this site collects.

What the number actually is: a weighted sum of the archetype's trait profile.
Each direction carries trait weights that sum to 1.0; a trait the archetype is
defined by counts as HIGH, the other three as MID, and the percentage is the
weighted average. So it is reproducible, it moves in the right direction when
the weights change, and anyone can check it — but it is a description of the
archetype, not a prediction about a career.

Keep `DISCLAIMER` under the list. The site tells schools in writing that the
test does not predict success and must not be the sole basis for choosing a
career; a bare "84%" next to a job title contradicts that in the reader's mind
whatever the surrounding text says.
"""

# Trait level used for the weighted sum. HIGH is the archetype's two defining
# traits; MID is the other three, which are not low — they are simply not what
# this archetype is named for.
#
# The gap between them has to be wide enough that the weights actually separate
# the directions. A first pass used 0.88 / 0.55 and every caring profession came
# out at 80% — a ranking where nothing ranks is worse than no ranking.
HIGH, MID = 0.92, 0.42

DISCLAIMER = (u'Bu foizlar — sizning ikkita eng kuchli xususiyatingiz shu '
              u'yoʻnalishga qanchalik mos kelishini koʻrsatadi. Bu bashorat emas: '
              u'qiziqishingiz, imkoniyatingiz va real tajribangiz undan muhimroq.')

# ---------------------------------------------------------------- result screen
# The two labels above belong to the ARCHETYPE PAGE, which a visitor reads on its
# own and where a ranked list is the whole point of the page.
#
# The RESULT SCREEN is a different situation and needs different words. There the
# same directions land a single scroll above «Yoʻnalishlar», which ranks careers
# from interests, values and marks — four signals, of which personality is 8%.
# Two ranked career lists on one screen, built from almost disjoint evidence,
# disagree for most students: measured over 3,600 simulated students the two
# top picks matched 9.4% of the time against a 6.3% chance baseline.
#
# So on the result screen this block stops ranking and stops claiming fit. It
# says what it can honestly say -- these traits are valued in these areas -- and
# hands the actual recommendation to the section that has the evidence for it.
RESULT_CAREER_TITLE = u'Bu xususiyatlar qayerda qoʻl keladi'

RESULT_NOTE = (u'Bu — tavsiya emas va tartiblangan roʻyxat ham emas: shu '
               u'xususiyatlar qadrlanadigan sohalar, xolos. Sizga mos kasblar '
               u'quyida, «Yoʻnalishlar» boʻlimida — u qiziqishlaringizga va '
               u'baholaringizga ham qaraydi.')

AREA_TITLES = {
    'family':  (u'Oilada',        u'Uyda va yaqinlaringiz orasida'),
    'school':  (u'Maktabda',      u'Darsda, imtihonda va sinfdoshlar orasida'),
    'friends': (u'Munosabatlarda', u'Doʻstlik va yaqin munosabatlarda'),
}

STRONG_LABEL = u'Kuchli taraflaringiz'
WEAK_LABEL = u'Eʼtibor beradigan tomonlaringiz'
CAREER_TITLE = u'Sizga mos kelishi mumkin boʻlgan yoʻnalishlar'


def pct(key, weights):
    u"""Weighted trait average for one direction, as a whole percent."""
    defining = set(key.split('|'))
    total = sum(w * (HIGH if t in defining else MID) for t, w in weights.items())
    return int(round(total * 100))


LIFE = {

# ---------------------------------------------------------------- Ishonchli Doʻst
'ES|A': {
 'family': {
  'strong': [
   (u'Uydagi tinchlik',
    u'Janjal chiqqanda ovozingizni koʻtarmaysiz. Koʻpincha vaziyatni yumshatadigan '
    u'birinchi odam aynan siz boʻlasiz.'),
   (u'Sirdosh',
    u'Aka-ukangiz yoki opa-singlingiz muammosini birinchi boʻlib sizga aytadi — '
    u'chunki siz uni kattalarga yetkazmasligingizni biladi.'),
   (u'Soʻralmagan yordam',
    u'Kimningdir charchaganini koʻrsangiz, iltimos qilinishini kutmaysiz. '
    u'Idishlarni yuvib qoʻygan odam odatda siz boʻlasiz.'),
   (u'Kattalar bilan sabr',
    u'Buvingiz yoki bobongiz bir voqeani uchinchi marta aytsa ham zerikmay '
    u'tinglaysiz. Bu koʻpchilikda yoʻq.'),
   (u'Uydagi vaʼda',
    u'Oilaga bergan soʻzingizni eslab qolasiz. Kichkina vaʼdani ham unutmaysiz.'),
  ],
  'weak': [
   (u'Oʻz ehtiyojingizni yashirish',
    u'«Menga hech narsa kerak emas» deb aytaverib, haqiqatan kerak boʻlganda ham '
    u'soʻramay qoʻyasiz.'),
   (u'Mavzuni oʻzgartirish',
    u'Kelishmovchilikni hal qilish oʻrniga gapni boshqa yoqqa burasiz. Muammo '
    u'yoʻqolmaydi — yigʻilib boradi.'),
   (u'Hammaning yukini olish',
    u'«Menga osonroq» deb uy ishlarini oʻzingiz qilib qoʻyasiz, keyin charchoq '
    u'sababini tushunmaysiz.'),
   (u'Ranjiganini bildirmaslik',
    u'Xafa boʻlganingizda jim boʻlasiz. Oilangiz nega jim boʻlganingizni bilmaydi '
    u'va sizni tushunmagandek koʻrinadi.'),
   (u'«Yoʻq» deyolmaslik',
    u'Oʻz rejangiz buzilsa ham har bir iltimosni bajarasiz. Keyin oʻzingizga '
    u'vaqt qolmaganidan siqilasiz.'),
  ],
 },
 'school': {
  'strong': [
   (u'Guruh ishida tayanch',
    u'Jamoa topshirigʻida hech kim qoʻl urmagan qismni oxirida siz tugatasiz.'),
   (u'Sinfdoshlar ishonchi',
    u'Boshqalar bilan til topa olmaydigan oʻquvchi ham sizga ochiladi, chunki siz '
    u'hukm qilmaysiz.'),
   (u'Imtihonda xotirjamlik',
    u'Atrofdagilar hayajonlanganda siz odatdagi tezligingizda ishlaysiz. Bilganingizni '
    u'unutib qoʻymaysiz.'),
   (u'Oʻqituvchi bilan munosabat',
    u'Qarshilik koʻrsatmaysiz va vaʼdangizda turasiz — shuning uchun masʼuliyatli '
    u'topshiriq koʻpincha sizga beriladi.'),
   (u'Sekin, lekin uzluksiz',
    u'Bir kechada emas, har kuni ozgina. Yil oxirida natija shu tarzda toʻplanadi.'),
  ],
  'weak': [
   (u'Savol bermaslik',
    u'Tushunmagan joyingizni soʻrashdan tortinasiz — «sinfni ushlab qolaman» deb '
    u'oʻylaysiz. Keyin oʻsha mavzu qiyinlashib qoladi.'),
   (u'Oʻzini past baholash',
    u'Ishingizni sinfdoshingiznikidan yomonroq deb hisoblaysiz. Koʻpincha bu '
    u'notoʻgʻri boʻladi.'),
   (u'Yetakchilikdan chekinish',
    u'Guruh boshligʻi boʻlishni boshqaga berasiz, hatto jamoa sizni tanlagan '
    u'boʻlsa ham.'),
   (u'Bahsda taslim',
    u'Kimdir qatʼiy ohangda gapirsa, toʻgʻri javobingizni ham himoya qilmaysiz.'),
   (u'Yordam oʻrniga bajarib berish',
    u'Tushuntirish oʻrniga oʻzingiz qilib qoʻyasiz. Ular oʻrganmaydi, siz esa '
    u'ikki karra ishlaysiz.'),
  ],
 },
 'friends': {
  'strong': [
   (u'Haqiqiy tinglovchi',
    u'Javobingizni tayyorlab turmaysiz — chinakam eshitasiz. Buni odamlar darrov '
    u'sezadi.'),
   (u'Sir sizda qoladi',
    u'Sizga aytilgan gap boshqa hech kimga yetib bormaydi. Doʻstlaringiz buni '
    u'sinab koʻrgan.'),
   (u'Yarashtiruvchi',
    u'Ikki doʻstingiz urishib qolsa, ular orasida gaplashadigan odam koʻpincha '
    u'siz boʻlasiz.'),
   (u'Uzoq doʻstlik',
    u'Sizning doʻstligingiz yillar davom etadi. Aloqani birinchi boʻlib uzmaysiz.'),
   (u'Hukm qilmaslik',
    u'Xato qilgan odam ham sizga aytishdan qoʻrqmaydi. Shuning uchun sizga '
    u'aytiladi.'),
  ],
  'weak': [
   (u'Foydalanilib qolish',
    u'Yaxshiligingizni bilgan odam undan foydalanishi mumkin — va siz buni '
    u'koʻpincha oxirgi boʻlib sezasiz.'),
   (u'Chegara yoʻqligi',
    u'Yarim tunda ham telefoningiz ochiq. Oʻzingizga dam beradigan vaqt qolmaydi.'),
   (u'Xafalikni yigʻish',
    u'Ranjiganingizni aytmay yuraverasiz, keyin birdan uzoqlashasiz. Doʻstingiz '
    u'sababini tushunmaydi.'),
   (u'Hammaga yoqishga urinish',
    u'Oʻz fikringizni aytmay, koʻpchilikning fikriga qoʻshilaverasiz. Sizning '
    u'fikringiz ham kerak edi.'),
   (u'Oʻzingizga vaqt qoldirmaslik',
    u'Doʻstlaringizga shu qadar berilasizki, yolgʻiz qolish sizga aybdek '
    u'tuyuladi. Aslida dam olish ham kerak.'),
  ],
 },
 # Weights describe what the WORK demands, not what the archetype has. That is
 # what makes the ranking mean anything: teaching needs a voice in front of a
 # class (E) and medicine needs procedure (C), and neither is what this
 # archetype is named for, so both sit below counselling.
 'careers': [
  (u'Psixolog va maslahatchi', {'A': .40, 'ES': .40, 'O': .20},
   u'Odamlar sizga sirini aytadi, va siz ularning gapini boʻlmay eshitasiz. '
   u'Bosim ostida xotirjam qolish esa bu ishda majburiy.'),
  (u'Ijtimoiy ish va HR', {'A': .40, 'ES': .30, 'E': .30},
   u'Jamoadagi keskinlikni boshqalardan oldin sezasiz va odamlarni '
   u'yarashtirasiz. Faqat bu yerda oʻz fikringizni ham aytish kerak boʻladi.'),
  (u'Logoped va maxsus pedagogika', {'A': .35, 'ES': .35, 'C': .30},
   u'Natija oylab koʻrinmaydigan ishda ham taslim boʻlmaysiz. Bu yerda '
   u'sabr iqtidordan muhimroq.'),
  (u'Tibbiyot va hamshiralik', {'ES': .35, 'A': .30, 'C': .35},
   u'Shoshilinch holat sizni sarosimaga solmaydi va bemorga insoniy '
   u'munosabatda boʻlasiz. Qatʼiy tartib-qoidaga koʻnikish esa mehnat talab '
   u'qiladi.'),
  (u'Oʻqituvchilik va tarbiya', {'A': .35, 'ES': .20, 'E': .25, 'C': .20},
   u'Tushunmagan bolaga uchinchi marta ham birinchi martadagidek tushuntira '
   u'olasiz. Lekin sinf oldida ovoz chiqarish siz uchun eng qiyini boʻladi.'),
 ],
},

# --------------------------------------------------------------------- Yetakchi
'ES|E': {
 'family': {
  'strong': [
   (u'Bosim ostida qaror', u'Uyda kutilmagan muammo chiqsa, hamma sizga qaraydi — '
    u'chunki siz sarosimaga tushmaysiz.'),
   (u'Mehmon kutish', u'Uyga odam kelganda suhbatni siz boshlaysiz va hech kim '
    u'chetda qolmaydi.'),
   (u'Janjalni toʻxtatish', u'Ovozingizni koʻtarmay bir gap aytasiz va tortishuv '
    u'tinadi. Buni oilangiz biladi.'),
   (u'Kichiklarga namuna', u'Ukalaringiz sizga taqlid qiladi, siz aytmasangiz ham.'),
   (u'Ishonchli yelka', u'Muhim oilaviy suhbatga sizni ham chaqirishadi, garchi '
    u'yoshingiz kichik boʻlsa ham.'),
  ],
  'weak': [
   (u'Befarqdek koʻrinish', u'Xotirjamligingiz «unga farqi yoʻq» degan taassurot '
    u'qoldiradi. Yaqinlaringiz sizdan koʻproq hissiyot kutadi.'),
   (u'Oʻz tashvishini aytmaslik', u'Hammaning muammosini eshitasiz, oʻzingiznikini '
    u'hech kimga aytmaysiz.'),
   (u'Soʻralmasdan boshqarish', u'Vaziyatni tez oʻz qoʻlingizga olasiz — baʼzan '
    u'oilangiz shunchaki tinglashingizni kutayotgan boʻladi.'),
   (u'«Sen bardoshlisan» yorligʻi', u'Sizdan hech kim holingizni soʻramay qoʻyadi, '
    u'chunki doim yaxshi koʻrinasiz.'),
   (u'Hissiy suhbatdan qochish', u'Yigʻi va koʻz yosh boʻlgan joyda oʻzingizni '
    u'noqulay his qilasiz va mavzuni amaliy tomonga burasiz.'),
  ],
 },
 'school': {
  'strong': [
   (u'Sinf oldida gapirish', u'Taqdimotda ovozingiz titramaydi. Koʻpchilik uchun '
    u'bu eng qiyin narsa.'),
   (u'Guruh yetakchisi', u'Jamoa adashib qolganda yoʻnalishni koʻrsatadigan odam '
    u'siz boʻlasiz.'),
   (u'Imtihonda barqarorlik', u'Bilganingizni hayajondan unutmaysiz — bu bilimdan '
    u'kam ahamiyatli emas.'),
   (u'Nizoni hal qilish', u'Sinfdoshlar urishib qolsa, oʻqituvchi sizni chaqiradi.'),
   (u'Oʻqituvchilar ishonchi', u'Masʼuliyatli topshiriq koʻpincha sizga beriladi.'),
  ],
  'weak': [
   (u'Guruh ishini oʻzlashtirish', u'«Tezroq boʻladi» deb hammasini oʻzingiz '
    u'qilasiz. Jamoa hech narsa oʻrganmaydi.'),
   (u'Yordam soʻramaslik', u'Tushunmaganingizni tan olish sizga yetakchilikni '
    u'yoʻqotishdek tuyuladi.'),
   (u'Jim oʻquvchini bosib qoʻyish', u'Siz gapirganingizda tortinchoq sinfdoshingiz '
    u'umuman gapirmay qoʻyadi.'),
   (u'Sekin darsda zerikish', u'Mavzu takrorlanganda eʼtiboringiz soʻnadi va '
    u'oddiy joyini oʻtkazib yuborasiz.'),
   (u'Xato qilishdan qoʻrqish', u'Hamma sizga qaraydi degan fikr yangi narsani '
    u'sinab koʻrishingizga xalaqit beradi.'),
  ],
 },
 'friends': {
  'strong': [
   (u'Davra tashkilotchisi', u'Uchrashuv boʻlishi yoki boʻlmasligi koʻpincha '
    u'sizga bogʻliq.'),
   (u'Vahimasiz maslahat', u'Doʻstingiz sarosimaga tushganda siz aniq nima '
    u'qilishni aytasiz.'),
   (u'Yangi odam bilan oson', u'Notanish davraga kirib ketish sizga qiyin emas.'),
   (u'Adolatli hakam', u'Ikki tomonni ham eshitasiz, keyin gapirasiz.'),
   (u'Vaʼdaga sodiq', u'Kelaman deganingizda kelasiz. Buni doʻstlaringiz sanaydi.'),
  ],
  'weak': [
   (u'Zaifligini koʻrsatmaslik', u'Doʻstlaringiz sizning ham qiynalishingizni '
    u'tasavvur qilolmaydi.'),
   (u'Hammani bir masofada tutish', u'Koʻp odam bilan yaxshimisiz, lekin juda '
    u'yaqin doʻst kam.'),
   (u'Yordam soʻrash qiyinligi', u'Doim beruvchi tomon boʻlasiz, olishni bilmaysiz.'),
   (u'Boshqarib yuborish', u'Doʻstona uchrashuv ham sizning rejangiz boʻyicha '
    u'oʻtadi — baʼzan boshqalar ham tanlashni xohlaydi.'),
   (u'Hissiy suhbatni qisqartirish', u'Doʻstingiz dardini aytganda tezda yechim '
    u'taklif qilasiz, u esa faqat eshitilishini kutgandi.'),
  ],
 },
 'careers': [
  (u'Boshqaruv va menejment', {'E': .45, 'ES': .45, 'C': .10},
   u'Bosim ostida qaror qabul qilish va odamlarni ergashtirish — bu ishning '
   u'kundalik mazmuni. Rejalashtirish tomonini alohida oʻrganishingiz kerak.'),
  (u'Huquq va advokatura', {'ES': .40, 'E': .35, 'C': .25},
   u'Qarshi tomon ovozini koʻtarganda ham siz koʻtarmaysiz. Sud zalida bu '
   u'ustunlik. Hujjat bilan ishlash esa sabr talab qiladi.'),
  (u'Diplomatiya va xalqaro munosabatlar', {'ES': .45, 'E': .40, 'A': .15},
   u'Keskin suhbatni yumshata olasiz va notanish muhitda tez moslashasiz.'),
  (u'Favqulodda xizmat va tibbiyot', {'ES': .50, 'C': .30, 'E': .20},
   u'Hamma sarosimaga tushganda sizning boshingiz ishlashda davom etadi.'),
  (u'Oʻqituvchilik va murabbiylik', {'A': .40, 'E': .35, 'ES': .25},
   u'Sinf oldida turish sizga oson. Faqat har bir oʻquvchining hissiy '
   u'holatini payqash ustida ishlashingiz kerak boʻladi.'),
 ],
},

# ------------------------------------------------------------------ Tashkilotchi
'E|C': {
 'family': {
  'strong': [
   (u'Uydagi tadbir sizdan', u'Tugʻilgan kun yoki mehmon — reja, roʻyxat va '
    u'vaqt jadvali sizda tayyor.'),
   (u'Aytilgan ish bajariladi', u'Onangiz soʻragan narsani esdan chiqarmaysiz.'),
   (u'Boshqalarni harakatga solish', u'Uyda hamma yotgan kunda ham siz turib '
    u'ish boshlaysiz va bu yuqadi.'),
   (u'Oldindan oʻylash', u'Kerakli narsa tugashidan oldin olib qoʻyasiz.'),
   (u'Katta ishni boʻlaklash', u'Bahorgi tozalash sizda bir kunda emas, '
    u'rejali oʻtadi.'),
  ],
  'weak': [
   (u'Buyruq ohangi', u'Shoshilganingizda iltimos emas, koʻrsatma berib '
    u'yuborasiz. Uyda bu ranjitadi.'),
   (u'Sekinroqlarga sabrsizlik', u'Ukangiz sekin qilayotgan ishni tortib olib '
    u'oʻzingiz bajarasiz.'),
   (u'Fikr soʻramaslik', u'Rejani tuzib boʻlgach eʼlon qilasiz — oilangiz '
    u'muhokamaga ulgurmaydi.'),
   (u'Dam olishni bilmaslik', u'Bekor oʻtirgan kuningiz oʻzingizni aybdor '
    u'his qilasiz.'),
   (u'Tartibsizlikdan asabiylashish', u'Boshqalarning betartibligi sizni haddan '
    u'tashqari bezovta qiladi.'),
  ],
 },
 'school': {
  'strong': [
   (u'Loyihani boshlab yuborish', u'Guruh hali muhokama qilayotganda siz '
    u'birinchi qadamni tashlagan boʻlasiz.'),
   (u'Muddatga ulgurish', u'Topshiriqni oxirgi kechaga qoldirmaysiz.'),
   (u'Sinf tadbirlari', u'Bayram yoki musobaqa boʻlsa, uyushtirish sizga '
    u'topshiriladi.'),
   (u'Aniq taqsimot', u'Jamoada kim nima qilishini siz belgilaysiz va chalkashlik '
    u'boʻlmaydi.'),
   (u'Gapdan ishga tez oʻtish', u'Rejani qogʻozda qoldirmaysiz.'),
  ],
  'weak': [
   (u'Hammasini oʻzingiz qilish', u'Ishonmaganingiz uchun jamoaning ishini ham '
    u'tortib olasiz, keyin charchaysiz.'),
   (u'Boshqa yechimni eshitmaslik', u'Sizning rejangiz tayyor boʻlgani uchun '
    u'yaxshiroq taklifni oʻtkazib yuborasiz.'),
   (u'Reja buzilganda asabiylashish', u'Dars jadvali kutilmaganda oʻzgarsa, '
    u'kayfiyatingiz tushadi.'),
   (u'Haddan ortiq yuklama', u'Bir vaqtda uchta toʻgarakka yozilib, hech biriga '
    u'ulgurmay qolasiz.'),
   (u'Natijaga qarab baholash', u'Sinfdoshingizning harakatini emas, faqat '
    u'natijasini koʻrasiz.'),
  ],
 },
 'friends': {
  'strong': [
   (u'Reja sizdan chiqadi', u'«Qayerga boramiz?» degan savolga javob beradigan '
    u'odam siz boʻlasiz.'),
   (u'Aytgan vaqtda kelish', u'Kechikmaysiz va doʻstlaringiz shunga ishonadi.'),
   (u'Energiya berish', u'Siz kelganingizda davra jonlanadi.'),
   (u'Doʻstga amaliy yordam', u'Achinish oʻrniga nima qilish kerakligini '
    u'aytasiz va yordam berasiz.'),
   (u'Yangi tanishuv', u'Doʻstlar doirangiz tez kengayadi.'),
  ],
  'weak': [
   (u'Rejani majburlash', u'Doʻstlaringiz boshqacha xohlasa ham sizning '
    u'variantingiz gʻolib chiqadi.'),
   (u'Qatʼiyatsizlarga sabrsizlik', u'«Bilmadim» deb turgan doʻstingizga '
    u'jahlingiz chiqadi.'),
   (u'Chuqur suhbatga vaqt yoʻq', u'Doim harakatdasiz — jimgina oʻtirib '
    u'gaplashish siyrak boʻladi.'),
   (u'Faqat ish boʻyicha yaqinlik', u'Doʻstlik ham loyihaga oʻxshab qoladi.'),
   (u'Yordamni qabul qilmaslik', u'«Oʻzim uddalayman» deysiz, hatto uddalay '
    u'olmasangiz ham.'),
  ],
 },
 'careers': [
  (u'Loyiha boshqaruvi', {'C': .45, 'E': .45, 'ES': .10},
   u'Rejani odamlarga taqsimlash va muddatni ushlab turish — sizda tabiiy.'),
  (u'Tadbirkorlik va biznes', {'E': .45, 'C': .40, 'O': .15},
   u'Gapdan ishga tez oʻtasiz va boshqalarni ham qoʻzgʻata olasiz. Yangi '
   u'gʻoya izlash tomonini rivojlantirishingiz kerak.'),
  (u'Tadbir va logistika', {'C': .45, 'E': .35, 'ES': .20},
   u'Yuzta mayda detalni bir vaqtda ushlab turish sizni charchatmaydi.'),
  (u'Savdo va mijozlar bilan ishlash', {'E': .45, 'A': .30, 'C': .25},
   u'Notanish odam bilan gaplashish va kelishuvni oxiriga yetkazish.'),
  (u'Sport murabbiyligi', {'E': .35, 'C': .30, 'ES': .20, 'A': .15},
   u'Mashgʻulot rejasini tuzasiz va jamoani harakatga solasiz.'),
 ],
},

# ----------------------------------------------------------------- Kashfiyotchi
'ES|O': {
 'family': {
  'strong': [
   (u'Oʻzgarishga koʻnikish', u'Koʻchish yoki yangi maktab sizni boshqalarcha '
    u'qiynamaydi.'),
   (u'Uyga yangilik olib kirish', u'Oilangiz bilmagan kitob, taom yoki gʻoyani '
    u'siz topib kelasiz.'),
   (u'Tinch savol berish', u'Kattalardan «nega shunday?» deb soʻrashdan '
    u'tortinmaysiz, lekin bahslashmaysiz.'),
   (u'Vahimasizlik', u'Uyda muammo boʻlganda ham kayfiyatingiz keskin tushmaydi.'),
   (u'Oila tarixiga qiziqish', u'Bobongizning hikoyalarini eshitishni '
    u'chinakam yoqtirasiz.'),
  ],
  'weak': [
   (u'Boshlanganini tashlab qoʻyish', u'Uyda boshlagan ishingiz yarmida qoladi '
    u'va oilangiz buni sanay boshlaydi.'),
   (u'Kundalik yumushga befarqlik', u'Bir xil takrorlanadigan uy ishlari sizga '
    u'chidab boʻlmas darajada zerikarli.'),
   (u'Rejaga bogʻlanmaslik', u'Oilaviy rejaga «balki» deb javob berasiz va '
    u'ishonchsiz koʻrinasiz.'),
   (u'Uzoqlashib qolish', u'Oʻz qiziqishingizga sho''ngʻib, kunlab '
    u'gaplashmay qoʻyishingiz mumkin.'),
   (u'Hissiyotni kam koʻrsatish', u'Yaqinlaringiz sizni sovuq deb oʻylashi mumkin.'),
  ],
 },
 'school': {
  'strong': [
   (u'Yangi fanni tez olish', u'Notanish mavzu sizni qoʻrqitmaydi, qiziqtiradi.'),
   (u'Mustaqil oʻrganish', u'Oʻqituvchi aytmagan manbani ham topib oʻqiysiz.'),
   (u'Qiyin masalada xotirjamlik', u'Yechilmagan masala sizni asabiylashtirmaydi.'),
   (u'Tadqiqot ishlari', u'Loyiha va referatda oʻzingizga xos yoʻl topasiz.'),
   (u'Turli qarashni koʻrish', u'Bitta javob bilan cheklanmaysiz.'),
  ],
  'weak': [
   (u'Takrorlashga chidamaslik', u'Bilgan mavzuni yana bir marta yozish sizga '
    u'azob. Shu sababli baho pasayadi.'),
   (u'Tugatilmagan topshiriq', u'Qiziqarli qismini qilib, qolganini tashlaysiz.'),
   (u'Qiziqishlar tarqoqligi', u'Bir vaqtda beshta narsani oʻrganib, birortasini '
    u'chuqurlashtirmaysiz.'),
   (u'Yod olishga qarshilik', u'Sabab tushuntirilmagan qoidani yodlash '
    u'sizga toʻgʻri kelmaydi.'),
   (u'Kam koʻrinish', u'Bilsangiz ham qoʻl koʻtarmaysiz, oʻqituvchi sizni '
    u'past baholashi mumkin.'),
  ],
 },
 'friends': {
  'strong': [
   (u'Qiziqarli suhbatdosh', u'Siz bilan gaplashgan odam yangi narsa bilib qoladi.'),
   (u'Turlicha odamlar bilan', u'Sizning doʻstlaringiz bir-biriga umuman oʻxshamaydi.'),
   (u'Dramaga aralashmaslik', u'Guruhdagi janjal sizni ichiga tortmaydi.'),
   (u'Sarguzashtga tayyor', u'Doʻstingiz gʻalati taklif qilsa, birinchi boʻlib '
    u'siz roziligini bildirasiz.'),
   (u'Hukm qilmaslik', u'Odamning gʻayrioddiy tanlovini ham tabiiy qabul qilasiz.'),
  ],
  'weak': [
   (u'Aloqani uzib qoʻyish', u'Yozmay qoʻyasiz va doʻstingiz sizni yoʻqotgandek '
    u'his qiladi.'),
   (u'Yuzaki qolish', u'Koʻp tanish bor, lekin haqiqiy yaqin doʻst kam.'),
   (u'Qiziqish tugagach uzoqlashish', u'Doʻstlik ham sizda yangi mavzuga '
    u'oʻxshab oʻtib ketishi mumkin.'),
   (u'Hissiy javob kutilganda', u'Doʻstingiz qaygʻurganda nima deyishni '
    u'bilmay qolasiz.'),
   (u'Sodiqlikni koʻrsatmaslik', u'Sizga doʻstlik muhim, lekin buni tashqaridan '
    u'bilib boʻlmaydi.'),
  ],
 },
 'careers': [
  (u'Ilmiy tadqiqot', {'O': .45, 'ES': .30, 'C': .25},
   u'Javobi nomaʼlum savol ustida oylab ishlash sizni charchatmaydi.'),
  (u'IT va dasturlash', {'O': .45, 'ES': .35, 'C': .20},
   u'Yangi texnologiyani oʻzingiz oʻrganib olasiz va xato sizni qoʻrqitmaydi.'),
  (u'Jurnalistika va tadqiqotchilik', {'O': .40, 'ES': .30, 'E': .30},
   u'Notanish odam va notanish joy siz uchun muammo emas.'),
  (u'Geologiya, geografiya, ekspeditsiya', {'O': .45, 'ES': .40, 'C': .15},
   u'Noqulay sharoit va nomaʼlumlik sizni boshqalarchalik bezovta qilmaydi.'),
  (u'Meʼmorchilik va dizayn', {'O': .45, 'C': .40, 'E': .15},
   u'Yangi shakl topasiz. Uni oxirigacha chizib chiqish esa intizom talab qiladi.'),
 ],
},

# ---------------------------------------------------------------------- Ijodkor
'E|O': {
 'family': {
  'strong': [
   (u'Uyga jon kiritish', u'Siz uyda boʻlsangiz, jimlik boʻlmaydi.'),
   (u'Gʻoya taklif qilish', u'Dam olish kunini qiziqarli oʻtkazish rejasi '
    u'sizdan chiqadi.'),
   (u'Hikoya qilish', u'Oddiy kunni ham quvnoq qilib gapirib bera olasiz.'),
   (u'Kichiklar bilan oʻyin', u'Ukalaringiz siz bilan zerikmaydi.'),
   (u'Ochiqlik', u'Boshingizdan oʻtganini oiladan yashirmaysiz.'),
  ],
  'weak': [
   (u'Tugallanmagan ish', u'Boshlagan loyihalaringiz uyning burchagida yigʻilib '
    u'qoladi.'),
   (u'Uy yumushini unutish', u'Qiziq narsa chiqsa, aytilgan ishni esdan '
    u'chiqarasiz.'),
   (u'Gapni boʻlish', u'Hayajonlanganingizda boshqalarning gapini kesib '
    u'oʻtasiz.'),
   (u'Uyda tinch oʻtirolmaslik', u'Oilaviy sokin kechalar sizga zerikarli tuyuladi.'),
   (u'Tartib bilan orangiz', u'Xonangiz doim tartibsiz va bu janjal sababi boʻladi.'),
  ],
 },
 'school': {
  'strong': [
   (u'Taqdimot va chiqish', u'Sahnada oʻzingizni erkin his qilasiz.'),
   (u'Ijodiy topshiriq', u'Erkin mavzu berilsa, sizning ishingiz esda qoladi.'),
   (u'Munozarada', u'Fikr almashish sizga zavq beradi.'),
   (u'Sinfni qiziqtirish', u'Sizning savolingiz butun darsni jonlantiradi.'),
   (u'Yangi gʻoyani yuqtirish', u'Loyihaga sinfdoshlaringizni qiziqtira olasiz.'),
  ],
  'weak': [
   (u'Muddatga ulgurmaslik', u'Gʻoya koʻp, tugatilgan ish kam.'),
   (u'Chalgʻish', u'Darsda fikringiz boshqa narsaga ketib qoladi.'),
   (u'Mashqqa chidamaslik', u'Bir xil misolni oʻn marta yechish sizga ogʻir.'),
   (u'Tartibsiz daftar', u'Yozganingizni keyin oʻzingiz topolmaysiz.'),
   (u'Baho pasayishi', u'Bilim bor, lekin topshirilmagan ish sabab natija past.'),
  ],
 },
 'friends': {
  'strong': [
   (u'Davra markazi', u'Siz kelganingizda kayfiyat koʻtariladi.'),
   (u'Odamlarni bogʻlash', u'Turli doʻstlaringizni bir-biri bilan tanishtirasiz.'),
   (u'Zerikarli boʻlmaslik', u'Siz bilan bir kun ham bir xil oʻtmaydi.'),
   (u'Ilhomlantirish', u'Doʻstingiz tashlab qoʻygan orzusini siz esga solasiz.'),
   (u'Tez yaqinlashish', u'Notanish odam bilan bir kunda til topasiz.'),
  ],
  'weak': [
   (u'Koʻp tanish, kam yaqin', u'Hamma sizni biladi, lekin sizni chinakam '
    u'biladigan kam.'),
   (u'Vaʼdani unutish', u'Uchrashuvni belgilab, keyin esdan chiqarasiz.'),
   (u'Suhbatni egallash', u'Gapirishni shunchalik yoqtirasizki, eshitishga '
    u'vaqt qolmaydi.'),
   (u'Tez sovish', u'Yangi davra topilsa, eski doʻstlar chetda qoladi.'),
   (u'Yolgʻizlikdan qochish', u'Yolgʻiz qolmaslik uchun sizga toʻgʻri '
    u'kelmaydigan davraga ham borasiz.'),
  ],
 },
 'careers': [
  (u'Dizayn va vizual ijod', {'O': .45, 'E': .45, 'C': .10},
   u'Gʻoyangiz tugamaydi va uni odamlarga koʻrsatishdan qoʻrqmaysiz.'),
  (u'Media, blogerlik, jurnalistika', {'E': .45, 'O': .40, 'ES': .15},
   u'Kamera yoki mikrofon oldida tabiiy qolasiz.'),
  (u'Marketing va reklama', {'E': .40, 'O': .40, 'C': .20},
   u'Yangi gʻoyani odamlarga yuqtirish — bu kasbning butun mazmuni.'),
  (u'Aktyorlik va sahna', {'E': .40, 'O': .30, 'ES': .30},
   u'Odamlar oldida oʻzingizni erkin his qilasiz.'),
  (u'Ijodiy fanlar oʻqituvchisi', {'E': .35, 'A': .35, 'O': .30},
   u'Darsni hech kim uxlab oʻtkazmaydi. Faqat jurnal va hujjat sizni '
   u'zeriktiradi.'),
 ],
},

# ---------------------------------------------------------- Uzoqni Koʻzlovchi
'O|C': {
 'family': {
  'strong': [
   (u'Amaliy yechim topish', u'Uydagi buzilgan narsani siz oʻzingizcha '
    u'tuzatib qoʻyasiz.'),
   (u'Aytilgan ish bajariladi', u'Vaʼda bergan boʻlsangiz, eslatish shart emas.'),
   (u'Uzoqni oʻylash', u'Kelasi yilgi imtihon haqida bugundan gapirasiz.'),
   (u'Tartib', u'Sizning burchagingiz uyning eng tartibli joyi.'),
   (u'Yaxshilashga intilish', u'Bir marta qilingan ishni keyingi safar '
    u'yaxshiroq qilasiz.'),
  ],
  'weak': [
   (u'Mukammallik talabi', u'Oʻzingizga ham, oilangizga ham juda baland '
    u'talab qoʻyasiz.'),
   (u'Boshqacha usulni tanqid', u'Onangiz boshqacha qilsa, «notoʻgʻri» deb '
    u'aytib yuborasiz.'),
   (u'Qaror oʻzgarmasligi', u'Bir marta rejalashtirgan narsangizni oʻzgartirish '
    u'sizga ogʻir.'),
   (u'Dam olishni bilmaslik', u'Bekorchilik sizga vaqtni behuda sarflashdek '
    u'tuyuladi.'),
   (u'Hissiyot oʻrniga vazifa', u'Yaqiningiz qaygʻurganda unga reja tuzib '
    u'berasiz, quchoqlash oʻrniga.'),
  ],
 },
 'school': {
  'strong': [
   (u'Loyiha oxirigacha', u'Boshlagan ishingizni tugatasiz — sinfda bu kam.'),
   (u'Original yechim', u'Hammadan boshqacha, lekin ishlaydigan yoʻl topasiz.'),
   (u'Aniq rejalashtirish', u'Katta topshiriqni haftalarga boʻlasiz.'),
   (u'Yuqori sifat', u'Sizning ishingiz koʻrinishidan ham puxta.'),
   (u'Mustaqil ishlash', u'Nazorat kerak emas.'),
  ],
  'weak': [
   (u'Mukammallik sekinlashtiradi', u'Yetarlicha yaxshi ishni ham qayta '
    u'qilaverib, muddatdan chiqasiz.'),
   (u'Oʻzini qattiq tanqid', u'Bitta xato butun ishni bekor qilgandek tuyuladi.'),
   (u'Jamoa bilan qiyinchilik', u'Sinfdoshingiz sizchalik jiddiy emasligi '
    u'sizni asabiylashtiradi.'),
   (u'Yordam soʻramaslik', u'Yolgʻiz qilishni afzal koʻrasiz, garchi ikki '
    u'barobar koʻp vaqt ketsa ham.'),
   (u'Ortiqcha yuklanish', u'Dam olmay ishlab, imtihon oldidan charchab qolasiz.'),
  ],
 },
 'friends': {
  'strong': [
   (u'Ishonchli soʻz', u'Aytgan vaqtingizda kelasiz va aytganingizni qilasiz.'),
   (u'Oʻylangan sovgʻa', u'Sizning sovgʻangiz tasodifiy boʻlmaydi.'),
   (u'Amaliy maslahat', u'Doʻstingiz muammosiga aniq qadamlar taklif qilasiz.'),
   (u'Kam, lekin chuqur', u'Doʻstlaringiz kam, ammo yillar davom etadi.'),
   (u'Aytganini eslash', u'Doʻstingiz oʻtgan oyda aytgan gapini esda tutasiz.'),
  ],
  'weak': [
   (u'Vaqt topolmaslik', u'Rejangiz zich va doʻstlarga oʻrin qolmaydi.'),
   (u'Tanlovlarini baholash', u'Doʻstingizning yengil qarorini ichingizda '
    u'maʼqullamaysiz va bu sezilib qoladi.'),
   (u'Rejasiz uchrashuvdan noqulaylik', u'«Hozir chiq» degan taklif sizni '
    u'bezovta qiladi.'),
   (u'Yumshoq boʻlolmaslik', u'Toʻgʻri gapni juda toʻgʻri aytib yuborasiz.'),
   (u'Doiraning torligi', u'Yangi odam qoʻshilishi sizga koʻp vaqt oladi.'),
  ],
 },
 'careers': [
  (u'Muhandislik va texnika', {'O': .45, 'C': .45, 'ES': .10},
   u'Yangi yechim topasiz va uni chizmagacha, hisobgacha olib borasiz.'),
  (u'Meʼmorchilik', {'O': .40, 'C': .40, 'E': .20},
   u'Gʻoya va oʻlchov bir odamda birga boʻlishi shart — bu siz.'),
  (u'Dasturlash va tizim loyihalash', {'O': .40, 'C': .40, 'ES': .20},
   u'Murakkab masalani aniq qadamlarga boʻlish sizga tabiiy.'),
  (u'Ilmiy tadqiqot', {'O': .45, 'C': .35, 'ES': .20},
   u'Uzoq muddatli, natijasi kechikadigan ish sizni qoʻrqitmaydi.'),
  (u'Mahsulot va loyiha dizayni', {'O': .35, 'E': .35, 'C': .30},
   u'Gʻoyani jadvalga aylantirasiz. Jamoaga tushuntirish tomonini '
   u'rivojlantirishingiz kerak.'),
 ],
},

# ----------------------------------------------------------- Jamoaning Yuragi
'E|A': {
 'family': {
  'strong': [
   (u'Uydagi iliqlik', u'Siz boʻlgan xonada hamma oʻzini qulay his qiladi.'),
   (u'Hech kim chetda qolmaydi', u'Jim oʻtirgan qarindoshni suhbatga siz '
    u'tortasiz.'),
   (u'Aloqani saqlash', u'Uzoq qarindoshlarga qoʻngʻiroq qiladigan odam siz.'),
   (u'Mehmondorchilik', u'Uyga kelgan odam oʻzini begona his qilmaydi.'),
   (u'Kayfiyat koʻtarish', u'Uydagi ogʻir kunni yengillashtira olasiz.'),
  ],
  'weak': [
   (u'Janjaldan qochish', u'Kelishmovchilikni ochiq gapirish oʻrniga hazil '
    u'bilan chetlab oʻtasiz.'),
   (u'Oʻz fikrini aytmaslik', u'Rozilikni saqlash uchun oʻz xohishingizdan '
    u'voz kechasiz.'),
   (u'Hamma bilan yaxshi boʻlish', u'Ikki qarindosh urishsa, ikkalasiga ham '
    u'«haqsan» deysiz.'),
   (u'Tashqarida koʻproq', u'Uy jimjit boʻlsa, doʻstlarnikiga ketasiz.'),
   (u'Charchaganini yashirish', u'Kayfiyatingiz yoʻq kunda ham quvnoq '
    u'koʻrinasiz.'),
  ],
 },
 'school': {
  'strong': [
   (u'Sinfni bogʻlash', u'Sinfdagi guruhlar orasida koʻprik boʻlasiz.'),
   (u'Yangi oʻquvchini qabul qilish', u'Sinfga kelgan yangi bolani birinchi '
    u'boʻlib siz kutib olasiz.'),
   (u'Jamoa ruhi', u'Guruh ishida hamma ishtirok etishini taʼminlaysiz.'),
   (u'Oʻqituvchi bilan iliq', u'Darsni ochiq va samimiy qilib yuborasiz.'),
   (u'Tadbirda faol', u'Sinf tadbirisiz siz tasavvur qilinmaydi.'),
  ],
  'weak': [
   (u'Suhbat darsdan ustun', u'Gaplashib, mavzuni oʻtkazib yuborasiz.'),
   (u'Bahsdan qochish', u'Notoʻgʻri javobni ham tuzatmaysiz, xafa boʻlmasin deb.'),
   (u'Oʻz ishini himoya qilmaslik', u'Bahoyingiz noadolatli qoʻyilsa ham '
    u'indamaysiz.'),
   (u'Diqqatning tarqoqligi', u'Atrofda odam boʻlsa, dars ikkinchi oʻringa '
    u'tushadi.'),
   (u'Yolgʻiz oʻqiy olmaslik', u'Yakka oʻtirib takrorlash sizga ogʻir.'),
  ],
 },
 'friends': {
  'strong': [
   (u'Doʻst koʻp', u'Turli davralarda oʻzingiznikisiz.'),
   (u'Chetdagini koʻrish', u'Davrada jim qolgan odamni sezasiz va yoningizga '
    u'chaqirasiz.'),
   (u'Quvonchni ulashish', u'Doʻstingizning yutugʻiga oʻzingiznikidan koʻra '
    u'koʻproq quvonasiz.'),
   (u'Yarashtirish', u'Urishgan ikki doʻstni yana bir dasturxonga oʻtqazasiz.'),
   (u'Xotira', u'Tugʻilgan kunlarni eslab qolasiz.'),
  ],
  'weak': [
   (u'Hammaga ulgurmaslik', u'Doʻst koʻp boʻlgani uchun hech biriga yetarli '
    u'vaqt qolmaydi.'),
   (u'«Yoʻq» deyolmaslik', u'Charchagan boʻlsangiz ham taklifni rad etmaysiz.'),
   (u'Tez ranjish', u'Oddiy hazilni ham shaxsiy qabul qilib qoʻyasiz.'),
   (u'Nizoni bostirish', u'Muammoni gaplashish oʻrniga yopib qoʻyasiz, u esa '
    u'qaytadi.'),
   (u'Yoqish uchun oʻzgarish', u'Har davrada biroz boshqacha boʻlasiz va '
    u'oʻzingizni yoʻqotasiz.'),
  ],
 },
 'careers': [
  (u'Oʻqituvchilik va tarbiya', {'E': .45, 'A': .45, 'C': .10},
   u'Sinfni birlashtirish va har bir bolani koʻrish — sizning kuchingiz.'),
  (u'HR va jamoa bilan ishlash', {'E': .45, 'A': .40, 'ES': .15},
   u'Odamlar orasidagi keskinlikni sezasiz va hal qilasiz.'),
  (u'Jurnalistika va muloqot', {'E': .45, 'O': .30, 'A': .25},
   u'Notanish odam sizga ochiladi — bu suhbat olishning yarmi.'),
  (u'Mehmondoʻstlik va turizm', {'E': .40, 'A': .35, 'C': .25},
   u'Odamni qulay his qildirish sizda oʻz-oʻzidan chiqadi.'),
  (u'Jamoat tashkilotlari va volontyorlik', {'A': .35, 'E': .30, 'O': .20, 'C': .15},
   u'Odamlarni bir maqsad atrofida yigʻa olasiz.'),
 ],
},

# ------------------------------------------------------------ Mehribon Inson
'O|A': {
 'family': {
  'strong': [
   (u'Kayfiyatni sezish', u'Onangiz charchaganini u aytmasdan bilasiz.'),
   (u'Ijodiy gʻamxoʻrlik', u'Sizning sovgʻangiz sotib olingan emas, oʻylab '
    u'topilgan boʻladi.'),
   (u'Hech kimni ayblamaslik', u'Uydagi xatoni kimningdir aybi deb qidirmaysiz.'),
   (u'Boshqacha fikrni tinglash', u'Kattalar bilan bahslashmay, ularni '
    u'tushunishga harakat qilasiz.'),
   (u'Uyni chiroyli qilish', u'Xonani, dasturxonni siz oʻzgacha bezaysiz.'),
  ],
  'weak': [
   (u'Oilaning dardini oʻziga olish', u'Uydagi muammo sizni boshqalardan '
    u'koʻra koʻproq ezadi.'),
   (u'Amaliy tomondan uzoq', u'Pul, jadval va rejaga eʼtiborsizsiz.'),
   (u'Toʻqnashuvdan qochish', u'Norozi boʻlsangiz ham ochiq aytmaysiz.'),
   (u'Ideallashtirish', u'Oilangizni mukammal deb tasavvur qilasiz, kamchilik '
    u'koʻrsangiz qattiq ranjiysiz.'),
   (u'Ichiga yopilish', u'Xafa boʻlganingizda xonangizga kirib ketasiz.'),
  ],
 },
 'school': {
  'strong': [
   (u'Ijodiy loyiha', u'Erkin topshiriqda ishingiz esda qoladigan boʻladi.'),
   (u'Qiynalgan sinfdoshga yordam', u'Tushunmagan bolani hech kim bilmagan '
    u'holda oʻrgatasiz.'),
   (u'Axloqiy savollar', u'«Bu adolatlimi?» degan savolni siz berasiz.'),
   (u'Raqobatsizlik', u'Baho uchun talashmaysiz, sinf tinch boʻladi.'),
   (u'Estetik did', u'Daftar, taqdimot va rasm sizda chiroyli chiqadi.'),
  ],
  'weak': [
   (u'Tanqidga taʼsirchanlik', u'Oʻqituvchining kichik tanbehi ham kayfiyatingizni '
    u'kunlab buzadi.'),
   (u'Tartibsizlik', u'Muddat va jadval sizni chalkashtiradi.'),
   (u'Qiziqmagan fanni tashlash', u'Yoqmagan fanga umuman kuch sarflamaysiz.'),
   (u'Oʻzini past baholash', u'Matematikada qiynalsangiz, ijodiy '
    u'iqtidoringizni ham kamsitasiz.'),
   (u'Ovoz chiqarmaslik', u'Yaxshi gʻoyangiz bor, lekin sinf oldida aytmaysiz.'),
  ],
 },
 'friends': {
  'strong': [
   (u'Chuqur suhbat', u'Yuzaki gap sizga qiziq emas, siz asosiy narsani soʻraysiz.'),
   (u'Hukmsiz qabul', u'Doʻstingiz eng uyaladigan narsasini ham sizga aytadi.'),
   (u'Sezgirlik', u'Ovoz ohangidan kayfiyatni bilasiz.'),
   (u'Oʻziga xos yaqinlik', u'Sizning doʻstligingiz boshqalarnikiga oʻxshamaydi.'),
   (u'Kechirimlilik', u'Xatoni uzoq eslab yurmaysiz.'),
  ],
  'weak': [
   (u'Ogʻriqni oʻziga olish', u'Doʻstingizning muammosi sizni uning oʻzidan '
    u'koʻra koʻproq qiynaydi.'),
   (u'Odamni ideallashtirish', u'Odamni mukammal deb bilasiz, keyin haqiqatni '
    u'koʻrib qattiq hafsalangiz pir boʻladi.'),
   (u'Uzoqlashib ketish', u'Ranjiganingizda tushuntirmay, jimgina yoʻqolasiz.'),
   (u'Chegara qoʻyolmaslik', u'Doʻstingiz uchun oʻz vaqtingizni butunlay '
    u'berasiz.'),
   (u'Nizodan qochish', u'Muammoni aytish oʻrniga munosabatni sovutasiz.'),
  ],
 },
 'careers': [
  (u'Psixologiya va terapiya', {'A': .45, 'O': .45, 'ES': .10},
   u'Odamni tushunish va yangi yondashuv izlash bir joyda kerak boʻladi.'),
  (u'Ijtimoiy ish va nodavlat tashkilotlar', {'A': .45, 'O': .35, 'C': .20},
   u'Muammoni koʻrganingizda avval odamlar haqida oʻylaysiz.'),
  (u'Sanʼat va art-terapiya', {'O': .45, 'A': .35, 'E': .20},
   u'Ijod orqali odamga yordam berish — ikkala kuchingiz birga ishlaydi.'),
  (u'Maxsus pedagogika', {'A': .40, 'C': .35, 'O': .25},
   u'Har bolaga alohida yoʻl kerak — siz uni topa olasiz.'),
  (u'Adabiyot va tarjima', {'O': .40, 'A': .30, 'C': .30},
   u'Soʻz orqali odamning ichki dunyosini yetkazish sizga yaqin.'),
 ],
},

# ---------------------------------------------------------------- Rejali Inson
'ES|C': {
 'family': {
  'strong': [
   (u'Vaʼda = bajarilgan ish', u'Oilangiz sizga eslatmaydi, chunki keragi yoʻq.'),
   (u'Inqirozda xotirjam', u'Uyda ogʻir vaziyat boʻlsa, siz vahima qilmaysiz.'),
   (u'Uzoqni rejalashtirish', u'Kelasi yil haqida bugundan gapiradigan odam siz.'),
   (u'Tejamkorlik', u'Pulni oʻylab sarflaysiz, kichkina yoshdan.'),
   (u'Kichiklarga tayanch', u'Ukalaringiz darsda qiynalsa sizga keladi.'),
  ],
  'weak': [
   (u'Reja buzilganda', u'Kutilmagan oʻzgarish sizni boshqalardan koʻra '
    u'koʻproq bezovta qiladi, tashqaridan bilinmasa ham.'),
   (u'Hissiyotni aytmaslik', u'Sevgi va tashvishni soʻz bilan emas, ish bilan '
    u'koʻrsatasiz — oilangiz buni har doim ham tushunmaydi.'),
   (u'Dam olishni kechiktirish', u'«Avval ish» deb, hech qachon dam olmaysiz.'),
   (u'Qatʼiylik', u'Bir marta qaror qilgan narsangizni oʻzgartirish qiyin.'),
   (u'Yordam soʻramaslik', u'Ogʻir boʻlsa ham oʻzingiz koʻtarasiz.'),
  ],
 },
 'school': {
  'strong': [
   (u'Uzoq masofaga chidash', u'Uch oylik tayyorgarlik sizni qoʻrqitmaydi.'),
   (u'Imtihonda barqaror', u'Hayajon bilimingizni oʻchirmaydi.'),
   (u'Jadval boʻyicha oʻqish', u'Har kuni ozgina — va yil oxirida natija koʻrinadi.'),
   (u'Ishonchli jamoadosh', u'Sizga topshirilgan qism albatta tayyor boʻladi.'),
   (u'Tartibli daftar', u'Yozganingizni istalgan vaqtda topasiz.'),
  ],
  'weak': [
   (u'Oʻzgarishga qarshilik', u'Oʻqituvchi usulini oʻzgartirsa, siz qiynalasiz.'),
   (u'Yangilikdan qochish', u'Sinovdan oʻtgan usulni afzal koʻrib, yangisini '
    u'sinamaysiz.'),
   (u'Savol bermaslik', u'Tushunmaganingizni oʻzingiz hal qilishga urinasiz.'),
   (u'Mukammallik bosimi', u'Toʻrt baho sizni boshqalardan koʻra koʻproq '
    u'tushkunlikka soladi.'),
   (u'Ijodiy topshiriqda qiyinchilik', u'«Xohlaganingizni qiling» degan '
    u'topshiriq sizni chalkashtiradi.'),
  ],
 },
 'friends': {
  'strong': [
   (u'Soʻzida turish', u'Aytgan vaqtingizda kelasiz — har safar.'),
   (u'Sirni saqlash', u'Sizga aytilgan gap sizda qoladi.'),
   (u'Qiyinchilikda yoningizda', u'Doʻstingizga ogʻir kunda birinchi boʻlib '
    u'siz kelasiz.'),
   (u'Uzoq doʻstlik', u'Bolalikdagi doʻstingiz hali ham doʻstingiz.'),
   (u'Vahimasiz', u'Doʻstingiz sarosimaga tushganda siz aniq gapirasiz.'),
  ],
  'weak': [
   (u'Rejasizlikdan noqulaylik', u'«Hozir chiqamizmi?» degan taklif sizni '
    u'bezovta qiladi.'),
   (u'Doira torligi', u'Yangi doʻst orttirishga shoshilmaysiz.'),
   (u'Oʻz dardini aytmaslik', u'Doʻstlaringiz sizning ham qiynalishingizni '
    u'bilmaydi.'),
   (u'Sovuq koʻrinish', u'Hissiyotni kam koʻrsatganingiz uchun sizni befarq '
    u'deb oʻylashadi.'),
   (u'Kechirishga qiyinchilik', u'Vaʼdasida turmagan odamni uzoq eslab yurasiz.'),
  ],
 },
 'careers': [
  (u'Muhandislik va qurilish', {'C': .50, 'ES': .40, 'O': .10},
   u'Uzoq muddatli, aniqlik talab qiladigan ish sizga toʻgʻri keladi.'),
  (u'Moliya va buxgalteriya', {'C': .55, 'ES': .30, 'A': .15},
   u'Diqqat va barqarorlik — bu ishning ikki asosiy talabi.'),
  (u'Tibbiyot va jarrohlik', {'ES': .40, 'C': .35, 'A': .25},
   u'Bosim ostida qoʻlingiz titramaydi va tartibga qatʼiy amal qilasiz.'),
  (u'Huquq va notariat', {'C': .40, 'E': .35, 'ES': .25},
   u'Hujjat bilan sinchkov ishlash sizni zeriktirmaydi.'),
  (u'Logistika va ishlab chiqarish', {'C': .35, 'E': .25, 'ES': .25, 'A': .15},
   u'Katta tizimni jadval boʻyicha yuritish sizning maydoningiz.'),
 ],
},

# ---------------------------------------------------------- Soʻzida Turuvchi
'A|C': {
 'family': {
  'strong': [
   (u'Aytilmasa ham qilish', u'Uydagi ishni koʻrsangiz, buyruq kutmaysiz.'),
   (u'Vaʼdaga sodiqlik', u'Kichkina vaʼdani ham unutmaysiz.'),
   (u'Kattalarga gʻamxoʻrlik', u'Buvi-bobongiz eng koʻp sizga suyanadi.'),
   (u'Uy tartibi', u'Siz boʻlgan joyda hech narsa yoʻqolmaydi.'),
   (u'Sokin borliq', u'Baland gapirmasangiz ham, siz yoʻq boʻlsangiz darrov '
    u'sezilasiz.'),
  ],
  'weak': [
   (u'Hamma yukni olish', u'Uy ishlarining koʻpi sizda toʻplanib qoladi va '
    u'siz indamaysiz.'),
   (u'Aybdorlik hissi', u'Biror ishni qilolmasangiz, oʻzingizni uzoq ayblaysiz.'),
   (u'«Yoʻq» deyolmaslik', u'Charchagan boʻlsangiz ham rad eta olmaysiz.'),
   (u'Oʻz ehtiyojini oxirgi qoʻyish', u'Hammaning ishi bitgach, oʻzingizga '
    u'vaqt qolmaydi.'),
   (u'Maqtovni kutish va kutmaslik', u'Qilgan ishingiz sezilmasa xafa '
    u'boʻlasiz, lekin buni aytmaysiz.'),
  ],
 },
 'school': {
  'strong': [
   (u'Ishonib topshiriladi', u'Sinf pulini yoki muhim hujjatni sizga berishadi.'),
   (u'Muddatni buzmaslik', u'Topshiriq har doim vaqtida.'),
   (u'Sinfdoshga yordam', u'Tushuntirib berishdan zerikmaysiz.'),
   (u'Sokin izchillik', u'Koʻzga tashlanmasangiz ham, natijangiz barqaror.'),
   (u'Jamoada ishonchli boʻgʻin', u'Sizning qismingiz albatta tayyor boʻladi.'),
  ],
  'weak': [
   (u'Ortiqcha yuk', u'Guruhning ishini oxirida siz tugatasiz — har safar.'),
   (u'Oʻzini koʻrsatmaslik', u'Qilgan ishingizni boshqa birov oʻziniki qilib '
    u'aytsa ham indamaysiz.'),
   (u'Xato qilishdan qoʻrqish', u'Kimnidir umidsizlikka solishdan '
    u'qoʻrqasiz va shu sabab tavakkal qilmaysiz.'),
   (u'Savol bermaslik', u'Vaqt olib qoʻyaman deb tushunmaganingizni soʻramaysiz.'),
   (u'Yetakchilikdan qochish', u'Sizga ishonishsa ham, boshliqlikni boshqaga '
    u'berasiz.'),
  ],
 },
 'friends': {
  'strong': [
   (u'Tayanch doʻst', u'Ogʻir kunda birinchi boʻlib sizga qoʻngʻiroq qilishadi.'),
   (u'Sir saqlash', u'Sizdan hech narsa chiqmaydi.'),
   (u'Eslab qolish', u'Doʻstingizning imtihon sanasini oʻzidan yaxshiroq bilasiz.'),
   (u'Xolis maslahat', u'Yoqimli emas, foydali gapni aytasiz — lekin yumshoq.'),
   (u'Uzoq sodiqlik', u'Doʻstlikni birinchi boʻlib uzmaysiz.'),
  ],
  'weak': [
   (u'Foydalanilish', u'Yaxshiligingizni bilgan odam undan foydalanadi, siz '
    u'esa sezmaganga olasiz.'),
   (u'Chegara yoʻqligi', u'Har qanday vaqtda yordamga tayyorsiz — oʻzingizga '
    u'zarar boʻlsa ham.'),
   (u'Xafalikni yigʻish', u'Ranjishlarni ichingizda toʻplaysiz, keyin birdan '
    u'uzoqlashasiz.'),
   (u'Oʻz muammosini aytmaslik', u'Doʻstlaringiz sizni doim yaxshi deb '
    u'oʻylaydi.'),
   (u'Rad eta olmaslik', u'Toʻgʻri kelmaydigan taklifga ham rozi boʻlasiz.'),
  ],
 },
 'careers': [
  (u'Hamshiralik va tibbiy yordam', {'A': .45, 'C': .45, 'ES': .10},
   u'Gʻamxoʻrlik va aniqlik bir vaqtda kerak — ikkalasi ham sizda bor.'),
  (u'Buxgalteriya va boshqaruv hisobi', {'C': .55, 'A': .30, 'ES': .15},
   u'Sinchkovlik va halollik bu ishning asosi.'),
  (u'Boshlangʻich sinf oʻqituvchisi', {'A': .40, 'E': .30, 'C': .30},
   u'Sabr va izchillik — kichik bolalar bilan ishlashning butun mazmuni.'),
  (u'Kutubxona, arxiv, hujjatchilik', {'C': .40, 'A': .35, 'O': .25},
   u'Tartib va ishonch talab qilinadigan sokin ish sizga yaqin.'),
  (u'Ijtimoiy himoya va gʻamxoʻrlik xizmatlari', {'A': .40, 'C': .25, 'ES': .20, 'E': .15},
   u'Odamga ham, hujjatga ham eʼtiborli boʻlish kerak boʻlgan soha.'),
 ],
},

}


# ---------------------------------------------------------------- translations
#
# Uzbek is the original. A translation carries TEXT ONLY: the trait weights that
# produce the direction percentages stay in LIFE above, and the builder pairs
# them onto the translated names by position. So a translation cannot move a
# number, and it cannot silently reorder the directions either -- `careers` in a
# translation is (name, why), with no weights to disagree about.
#
# An archetype missing from a translation simply has no life section on that
# language's page, exactly as an archetype missing from LIFE has none anywhere.
# That is what lets the content land one archetype at a time. What is NOT
# allowed is a half-written one: check_translation() below refuses a translated
# archetype whose bullet counts differ from the Uzbek, because that ships a page
# with three of five strengths on it and nothing says so.
import life_content_ru as _ru
import life_content_en as _en

LIFE_BY_LANG = {'uz': LIFE, 'ru': _ru.LIFE, 'en': _en.LIFE}

LABELS = {
    'uz': {
        'strong': STRONG_LABEL, 'weak': WEAK_LABEL, 'career': CAREER_TITLE,
        'disclaimer': DISCLAIMER, 'areas': AREA_TITLES,
        'result_career': RESULT_CAREER_TITLE, 'result_note': RESULT_NOTE,
    },
    'ru': _ru.LABELS,
    'en': _en.LABELS,
}


def check_translation(key, lang):
    u"""Raise unless the translated entry has the same shape as the Uzbek one."""
    if lang == 'uz':
        return
    base, tr = LIFE[key], LIFE_BY_LANG[lang][key]
    for area in ('family', 'school', 'friends'):
        if (area in base) != (area in tr):
            raise ValueError('%s/%s: area %r present in one language only' % (key, lang, area))
        if area not in base:
            continue
        for kind in ('strong', 'weak'):
            if len(base[area][kind]) != len(tr[area][kind]):
                raise ValueError('%s/%s: %s.%s has %d entries, Uzbek has %d'
                                 % (key, lang, area, kind, len(tr[area][kind]), len(base[area][kind])))
    if len(base.get('careers', [])) != len(tr.get('careers', [])):
        raise ValueError('%s/%s: %d directions, Uzbek has %d'
                         % (key, lang, len(tr.get('careers', [])), len(base.get('careers', []))))


def careers_for(key, lang):
    u"""(name, weights, why) rows. Weights always come from the Uzbek entry."""
    base = LIFE[key]['careers']
    if lang == 'uz':
        return [(n, w, why) for n, w, why in base]
    tr = LIFE_BY_LANG[lang][key]['careers']
    return [(tr[i][0], base[i][1], tr[i][1]) for i in range(len(base))]
