# -*- coding: utf-8 -*-
"""Builds the printable guide (HTML) for one archetype, ready for make_pdf.js.

The short lines come from characters.js so the PDF can never contradict the
site; the long form comes from guide_content.py. Output is ONE self-contained
file — the two fonts inlined as base64 and nothing else — so it renders the same
over file://, on a server, or inside Chrome's PDF printer with no network at all.

The guides are text. No illustration, no colour, no boxes or rules beyond one
hairline under the running head. See the note above CSS for what went and why.

    python build_guide.py ES|A          # -> build/guide-ishonchli-dost.html
    node   make_pdf.js  ishonchli-dost  # -> ../guides/ishonchli-dost.pdf
"""
import base64, io, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE) + '/'
OUT = os.path.join(HERE, 'build')

sys.path.insert(0, HERE)
from guide_content import COMMON, GUIDES, TRAIT_CARDS

# Printed on the cover and on every page footer, and it is the only place a
# guide names the site — a student who downloads the PDF has no other way back.
# Keep in step with SITE in build_pages.py and SITE_HOST in test.html.
SITE = 'personality.naseebedu.com'

# ---- data straight out of the shipped characters.js -------------------------
dump = subprocess.check_output(['node', '-e', '''
const fs=require('fs'),vm=require('vm');const s={};vm.createContext(s);
vm.runInContext(fs.readFileSync(%r,'utf8'),s);
const out={};
for (const k in s.ARCHETYPES){
  const a=s.ARCHETYPES[k];
  out[k]={name:a.name,slug:a.slug,fam:a.fam,lines:a.lines,strength:a.strength,
          watch:a.watch,figure:a.figure,
          traits:k.split('|').map(x=>s.TRAIT_NAMES[x])};
}
process.stdout.write(JSON.stringify({arch:out,fams:s.FAMILIES}));
''' % (ROOT + 'assets/characters.js')])
data = json.loads(dump.decode('utf-8'))
ARCH, FAMS = data['arch'], data['fams']


def font64(name):
    with open(ROOT + 'assets/fonts/' + name, 'rb') as f:
        return base64.b64encode(f.read()).decode('ascii')


def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


# ---- the print stylesheet ---------------------------------------------------
# A4 pages are fixed boxes, not flowing text: every page is designed, and
# make_pdf.js fails the build if anything overflows its box.
#
# TEXT ONLY, at the founder's request. Gone: the cover artwork and the tinted
# disc behind it, the cover gradient, the logo mark, the numbered circles, the
# bullet dots, the drawn checkboxes, the drop cap, the oversized quote glyph,
# the six kinds of tinted or bordered box, and every colour. What is left is
# black text on white with one hairline, under the running head.
#
# The artwork was also the entire file size -- it was a 2.4-3.1 MB PNG inlined
# as base64 -- so the guides fall from 1-2.5 MB to roughly a tenth of that,
# which is the difference between a download that finishes on a school
# connection and one that does not.
#
# Hierarchy now has to come from type alone, so Bitter stays on the headings
# against Inter on the body. That is not decoration: with no colour and no
# rules, size, weight and typeface are the only things left telling a reader
# where they are in eight pages.
CSS = u"""
@font-face{font-family:'Bitter';src:url(data:font/woff2;base64,%(bitter)s) format('woff2');
           font-weight:100 900;font-style:normal}
@font-face{font-family:'Inter';src:url(data:font/woff2;base64,%(inter)s) format('woff2');
           font-weight:100 900;font-style:normal}
@page{size:A4;margin:0}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{font-family:'Inter',sans-serif;color:#000;font-size:11.2pt;line-height:1.62;
     background:#fff}
.page{position:relative;width:210mm;height:296.8mm;overflow:hidden;background:#fff;
      padding:20mm 19mm 20mm;page-break-after:always;break-after:page;
      display:flex;flex-direction:column}
/* A page is a fixed box, so a short section would leave a dead half-sheet.
   .fill spreads its blocks down the remaining height instead. */
.fill{flex:1;display:flex;flex-direction:column;justify-content:space-between}
.fill>*:last-child{margin-bottom:0}
.page:last-child{page-break-after:auto;break-after:auto}
h1,h2,h3{font-family:'Bitter',Georgia,serif;margin:0;color:#000}
p{margin:0 0 9pt}
b{font-weight:600}

/* running head + foot ---------------------------------------------------- */
/* The one rule left in the document. It earns its place: without it the running
   head reads as the first line of the page's text rather than as furniture. */
.rh{position:absolute;top:10mm;left:19mm;right:19mm;display:flex;
    justify-content:space-between;font-size:8pt;letter-spacing:.06em;
    text-transform:uppercase;border-bottom:.4pt solid #000;padding-bottom:3mm}
.rh .r{font-weight:600}
.rf{position:absolute;bottom:9mm;left:19mm;right:19mm;display:flex;
    justify-content:space-between;font-size:8pt}
.pno{font-weight:600}

/* cover ------------------------------------------------------------------ */
.cover{padding:0}
.cvin{position:absolute;inset:0;padding:24mm 19mm 18mm;display:flex;
      flex-direction:column}
.mark{font-family:'Bitter',serif;font-size:15pt;font-weight:700}
.kick{margin-top:36mm;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;
      font-weight:600}
.cvname{font-size:38pt;line-height:1.06;margin:3mm 0 0}
/* Was a filled pill. A line of small caps says the same thing in text. */
.cvfam{margin-top:5mm;font-size:9.5pt;font-weight:600;letter-spacing:.06em;
       text-transform:uppercase}
/* The measure can run wider now that no illustration occupies the right half. */
.cvlines{margin-top:11mm;max-width:132mm;font-size:12.6pt;line-height:1.6}
.cvlines p{margin:0 0 4mm}
.cvfoot{margin-top:auto;font-size:9pt;display:flex;justify-content:space-between}

/* generic blocks --------------------------------------------------------- */
.h2{font-size:19pt;line-height:1.2;margin-bottom:6mm}
.sub{font-size:10.4pt;margin-bottom:7mm}

/* The numeral was a filled circle; it is now the numeral. */
.num{display:flex;gap:4mm;margin-bottom:4.5mm}
.num .n{flex:0 0 7mm;font-family:'Bitter',serif;font-weight:700;font-size:11pt}
.num h3{font-size:12.2pt;margin-bottom:1.5mm}
.num p{margin:0}

/* Two bordered cards side by side became two stacked blocks: with no border
   there is nothing to hold a column together, and half-width text at 10.6pt
   sets to about 34 characters, which is too narrow to read. */
.cards{margin-bottom:7mm}
.card{margin-bottom:6mm}
.card:last-child{margin-bottom:0}
.card .tag{font-size:8.4pt;letter-spacing:.09em;text-transform:uppercase;
           font-weight:600}
.card h3{font-size:12.6pt;margin:1.5mm 0 2mm}
.card p{margin:0;font-size:10.6pt}

.note{font-size:10.8pt}
.note p{margin:0}

.para p{margin-bottom:6mm;font-size:11.4pt}

.pull{margin-top:auto;padding-top:7mm}
.pull p{margin:0;font-family:'Bitter',serif;font-size:14pt;line-height:1.5}

.str{padding:0 0 6.5mm}
.str h3{font-size:12.6pt;margin-bottom:1.5mm;display:flex;align-items:baseline;gap:3mm}
.str h3 span{font-size:9pt;font-family:'Inter',sans-serif;font-weight:600}
.str p{margin:0}

.grow{margin-bottom:7mm}
.grow h3{font-size:13pt;margin-bottom:2.5mm}
.grow>p{margin-bottom:2.5mm}
.do{margin-top:2.5mm}
.do .lbl{font-size:8.4pt;letter-spacing:.09em;text-transform:uppercase;
         font-weight:700;margin-bottom:1.5mm}
.do p{margin:0;font-size:10.6pt}

.sch{margin-bottom:7.5mm}
.sch h3{font-size:12.4pt;margin-bottom:1.5mm}
.sch p{margin:0}

.fit{margin-bottom:6mm}
.fit h3{font-size:12.2pt;margin-bottom:1.5mm}
.fit p{margin:0}
.warn .lbl{font-family:'Bitter',serif;font-weight:700;margin-bottom:2mm;
           font-size:11.4pt}
.warn p{margin:0;font-size:10.8pt}

.fig{margin-bottom:7mm}
.fig .who{font-family:'Bitter',serif;font-size:13.6pt;font-weight:700}
.fig .yr{font-size:9.4pt;font-weight:600;margin-bottom:2.5mm}
.fig p{margin:0;font-size:10.8pt}

/* The box was drawn with a border; it is now two characters, so it still
   prints as something a student can tick with a pen. */
.chk{display:flex;gap:3mm;align-items:baseline;margin-bottom:4.2mm}
.chk .box{flex:0 0 6mm;font-size:10.8pt}
.chk p{margin:0;font-size:10.8pt}
.last{padding-bottom:34mm}   /* room for the absolutely-placed disclaimer */
.close{padding-top:5mm;font-size:11pt;font-style:italic;margin:0}
.disc{position:absolute;left:19mm;right:19mm;bottom:16mm;font-size:8.6pt}
"""

DISCLAIMER = (u'Bu natija maslahat xarakteriga ega — tibbiy yoki psixologik tashxis '
              u'emas. Test Big Five (Katta beshlik) modeliga asoslangan.')


def build(key):
    a, own = ARCH[key], GUIDES[key]
    # An archetype's own text wins; anything it does not define is shared text.
    g = dict(COMMON)
    g.update(own)
    fam = FAMS[a['fam']]
    pages = []

    def page(inner, cls=''):
        n = len(pages) + 1               # cover is page 1, numbering starts after it
        head = (u'<div class="rh"><span>TestMind · Shaxsiyat qoʻllanmasi</span>'
                u'<span class="r">%s</span></div>' % esc(a['name']))
        foot = (u'<div class="rf"><span>%s</span><span class="pno">%d</span></div>'
                % (SITE, n))
        pages.append(u'<section class="page %s">%s%s%s</section>'
                     % (cls, head, inner, foot))

    # ---- 1. cover ----------------------------------------------------------
    # No logo mark, no illustration, no disc, no gradient. A title page.
    pages.append(u"""<section class="page cover"><div class="cvin">
  <div class="mark">TestMind</div>
  <div class="kick">%s</div>
  <h1 class="cvname">%s</h1>
  <div class="cvfam">%s oilasi</div>
  <div class="cvlines">%s</div>
  <div class="cvfoot"><span>%s</span><span>Bepul · 50 savol · Big Five</span></div>
</div></section>""" % (esc(g['cover_kicker']), esc(a['name']), esc(fam['name']),
                       u''.join(u'<p>%s</p>' % esc(l) for l in a['lines']), SITE))

    # ---- 2. how to read + the two traits -----------------------------------
    howto = u''.join(
        u'<div class="num"><div class="n">%d.</div><div><h3>%s</h3><p>%s</p></div></div>'
        % (i + 1, esc(t), esc(b)) for i, (t, b) in enumerate(g['howto']))
    # The two cards are the archetype's two traits, described once in
    # TRAIT_CARDS — so «Xotirjam» reads identically in all four ES guides.
    cards = u''.join(
        u'<div class="card"><div class="tag">%s</div><h3>%s</h3><p>%s</p></div>'
        % (esc(a['traits'][i]), esc(TRAIT_CARDS[t][0]), esc(TRAIT_CARDS[t][1]))
        for i, t in enumerate(key.split('|')))
    page(u"""<h2 class="h2">Bu qoʻllanmani qanday oʻqish kerak</h2>
%s
<h2 class="h2" style="margin-top:7mm">Ikki kuchli tomoningiz</h2>
<p class="sub">%s</p>
<div class="cards">%s</div>
<div class="note"><p>%s</p></div>""" % (howto, esc(g['traits_intro']), cards,
                                        esc(g['traits_note'])))

    # ---- 3. portrait -------------------------------------------------------
    page(u'<h2 class="h2">%s</h2><div class="para">%s</div>'
         u'<div class="pull"><p>%s</p></div>'
         % (esc(g['portrait_title']),
            u''.join(u'<p>%s</p>' % esc(p) for p in g['portrait']),
            esc(g['portrait_pull'])))

    # ---- 4. strengths ------------------------------------------------------
    strs = u''.join(
        u'<div class="str"><h3>%s <span>%02d</span></h3><p>%s</p></div>'
        % (esc(t), i + 1, esc(b)) for i, (t, b) in enumerate(g['strengths']))
    page(u"""<h2 class="h2">Kuchli tomonlaringiz</h2>
<p class="sub">Bularni siz oʻzingiz sezmasligingiz mumkin — atrofdagilar sezadi.</p>
<div class="fill"><div>%s</div>
<div class="note"><p><b>Bir jumlada:</b> %s</p></div>
<div class="warn"><div class="lbl">Ikkinchi tomoni</div>
<p>%s Keyingi sahifada shu haqda.</p></div></div>"""
         % (strs, esc(a['strength'][0].upper() + a['strength'][1:]), esc(a['watch'])))

    # ---- 5. growth ---------------------------------------------------------
    grow = u''.join(
        u'<div class="grow"><h3>%s</h3><p>%s</p>'
        u'<div class="do"><div class="lbl">Shu hafta sinab koʻring</div><p>%s</p></div></div>'
        % (esc(t), esc(b), esc(act)) for t, b, act in g['growth'])
    page(u"""<h2 class="h2">Oʻsish nuqtalari</h2>
<p class="sub">Bular kamchilik emas — kuchli tomoningizning teskari tomoni.</p>
<div class="fill">%s</div>""" % grow)

    # ---- 6. school + people ------------------------------------------------
    sch = u''.join(
        u'<div class="sch"><h3>%s</h3><p>%s</p></div>'
        % (esc(t), esc(b)) for t, b in g['school'])
    page(u"""<h2 class="h2">Maktabda va odamlar orasida</h2>
<p class="sub">Xuddi shu xususiyatlar kundalik ishda qanday ishlaydi.</p>
%s""" % sch)

    # ---- 7. future ---------------------------------------------------------
    fits = u''.join(u'<div class="fit"><h3>%s</h3><p>%s</p></div>' % (esc(t), esc(b))
                    for t, b in g['future_fits'])
    page(u"""<h2 class="h2">Kelajak yoʻnalishlari</h2>
<p class="sub">%s</p>
<div class="fill"><div>%s</div>
<div class="warn"><div class="lbl">Eʼtibor bering</div><p>%s</p></div>
<div class="note"><p><b>Keyingi qadam.</b> %s</p></div></div>"""
         % (esc(g['future_intro']), fits, esc(g['future_watch']),
            esc(g['future_next'])))

    # ---- 8. figure + practice ---------------------------------------------
    chk = u''.join(u'<div class="chk"><div class="box">[&#8201;]</div><p>%s</p></div>' % esc(c)
                   for c in g['practice'])
    page(u"""<h2 class="h2">Shu xususiyat kimda kuchli boʻlgan</h2>
<div class="fig"><div class="who">%s</div><div class="yr">%s</div><p>%s</p></div>
<h2 class="h2">Ikki haftalik amaliyot</h2>
<p class="sub">%s</p>
<div class="fill"><div>%s</div>
<p class="close">%s</p></div>
<div class="disc">%s</div>""" % (
             esc(a['figure']['who']), esc(a['figure']['years']), esc(g['figure_why']),
             esc(g['practice_intro']), chk, esc(g['closing']), DISCLAIMER), 'last')

    css = CSS % {'bitter': font64('bitter.woff2'), 'inter': font64('inter.woff2'),
                 }
    html = (u'<!doctype html>\n<html lang="uz"><head><meta charset="utf-8">\n'
            u'<title>%s — TestMind qoʻllanma</title>\n<style>%s</style>\n'
            u'</head><body>\n%s\n</body></html>\n'
            % (esc(a['name']), css, u'\n'.join(pages)))

    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    path = os.path.join(OUT, 'guide-%s.html' % a['slug'])
    with io.open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    return path, len(pages)


if __name__ == '__main__':
    keys = sys.argv[1:] or list(GUIDES.keys())
    for k in keys:
        if k not in GUIDES:
            sys.exit('no written guide for %s (add it to guide_content.py)' % k)
        p, n = build(k)
        print('%s  (%d pages)' % (p, n))
