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

}
