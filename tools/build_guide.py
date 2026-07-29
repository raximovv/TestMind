# -*- coding: utf-8 -*-
"""Builds the printable guide (HTML) for one archetype, ready for make_pdf.js.

The short lines come from characters.js so the PDF can never contradict the
site; the long form comes from guide_content.py. Output is ONE self-contained
file — fonts inlined as base64, artwork inlined as SVG — so it renders the same
over file://, on a server, or inside Chrome's PDF printer with no network at all.

    python build_guide.py ES|A          # -> build/guide-ishonchli-dost.html
    node   make_pdf.js  ishonchli-dost  # -> ../guides/ishonchli-dost.pdf
"""
import base64, io, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE) + '/'
OUT = os.path.join(HERE, 'build')

sys.path.insert(0, HERE)
from guide_content import COMMON, GUIDES, TRAIT_CARDS

SITE = 'raximovv.github.io/TestMind'

# ---- data straight out of the shipped characters.js -------------------------
dump = subprocess.check_output(['node', '-e', '''
const fs=require('fs'),vm=require('vm');const s={};vm.createContext(s);
vm.runInContext(fs.readFileSync(%r,'utf8'),s);
const out={};
for (const k in s.ARCHETYPES){
  const a=s.ARCHETYPES[k];
  out[k]={name:a.name,slug:a.slug,fam:a.fam,lines:a.lines,strength:a.strength,
          watch:a.watch,figure:a.figure,svg:s.charSvg(k,a.name),
          traits:k.split('|').map(x=>s.TRAIT_NAMES[x])};
}
process.stdout.write(JSON.stringify({arch:out,fams:s.FAMILIES}));
''' % (ROOT + 'assets/characters.js')])
data = json.loads(dump.decode('utf-8'))
ARCH, FAMS = data['arch'], data['fams']


def inline_art(svg):
    """Embed approved raster art so the printable guide stays self-contained."""
    marker = 'href="assets/characters/'
    if marker not in svg:
        return svg
    start = svg.index(marker) + len('href="')
    end = svg.index('"', start)
    rel = svg[start:end]
    path = os.path.join(ROOT, *rel.split('/'))
    with open(path, 'rb') as f:
        uri = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('ascii')
    return svg[:start] + uri + svg[end:]


for _a in ARCH.values():
    _a['svg'] = inline_art(_a['svg'])


def font64(name):
    with open(ROOT + 'assets/fonts/' + name, 'rb') as f:
        return base64.b64encode(f.read()).decode('ascii')


def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


# ---- the print stylesheet ---------------------------------------------------
# A4 pages are fixed boxes, not flowing text: every page is designed, and
# make_pdf.js fails the build if anything overflows its box.
CSS = u"""
@font-face{font-family:'Bitter';src:url(data:font/woff2;base64,%(bitter)s) format('woff2');
           font-weight:100 900;font-style:normal}
@font-face{font-family:'Inter';src:url(data:font/woff2;base64,%(inter)s) format('woff2');
           font-weight:100 900;font-style:normal}
@page{size:A4;margin:0}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
html,body{margin:0;padding:0}
body{font-family:'Inter',sans-serif;color:#152730;font-size:11.2pt;line-height:1.62;
     background:#fff}
.page{position:relative;width:210mm;height:296.8mm;overflow:hidden;background:#fff;
      padding:20mm 19mm 20mm;page-break-after:always;break-after:page;
      display:flex;flex-direction:column}
/* A page is a fixed box, so a short section would leave a dead half-sheet.
   .fill spreads its blocks down the remaining height instead. */
.fill{flex:1;display:flex;flex-direction:column;justify-content:space-between}
.fill>*:last-child{margin-bottom:0}
.page:last-child{page-break-after:auto;break-after:auto}
h1,h2,h3{font-family:'Bitter',Georgia,serif;margin:0;color:#0A4F66}
p{margin:0 0 9pt}
b{font-weight:600}

/* running head + foot ---------------------------------------------------- */
.rh{position:absolute;top:10mm;left:19mm;right:19mm;display:flex;
    justify-content:space-between;font-size:8pt;letter-spacing:.06em;
    text-transform:uppercase;color:#8CA2AA;border-bottom:1px solid #E3EBED;
    padding-bottom:3mm}
.rh .r{color:%(fam)s;font-weight:600}
.rf{position:absolute;bottom:9mm;left:19mm;right:19mm;display:flex;
    justify-content:space-between;font-size:8pt;color:#9DB0B7}
.pno{font-weight:600;color:%(fam)s}

/* cover ------------------------------------------------------------------ */
.cover{padding:0;background:linear-gradient(165deg,%(soft)s 0%%,#FFFFFF 62%%)}
.cvin{position:absolute;inset:0;padding:22mm 19mm 18mm;display:flex;
      flex-direction:column}
.mark{display:flex;align-items:center;gap:3.4mm;font-family:'Bitter',serif;
      font-size:15pt;font-weight:700;color:#0A4F66}
.mark svg{width:9mm;height:9mm}
.kick{margin-top:30mm;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;
      color:%(fam)s;font-weight:600}
.cvname{font-size:38pt;line-height:1.06;margin:3mm 0 0;color:#12303C}
.cvfam{display:inline-block;margin-top:5mm;padding:2mm 5mm;border-radius:99px;
       background:%(fam)s;color:#fff;font-size:9.5pt;font-weight:600}
.cvlines{margin-top:9mm;max-width:98mm;font-size:12.6pt;line-height:1.6;color:#2C444E}
.cvlines p{margin:0 0 4mm}
/* the figure anchors the lower-right quarter; the disc behind it keeps the
   page from reading as an empty sheet with a sticker in the corner */
.cvdisc{position:absolute;right:4mm;bottom:30mm;width:114mm;height:114mm;
        border-radius:50%%;background:%(soft)s;opacity:.85}
.cvart{position:absolute;right:24mm;bottom:41mm;width:82mm}
.cvart svg{width:100%%;height:auto;display:block}
.cvfoot{margin-top:auto;font-size:9pt;color:#5B7078;border-top:1px solid #D7E2E4;
        padding-top:4mm;display:flex;justify-content:space-between;position:relative}

/* generic blocks --------------------------------------------------------- */
.h2{font-size:19pt;line-height:1.2;margin-bottom:2mm}
.sub{color:#5B7078;font-size:10.4pt;margin-bottom:7mm}
.rule{height:3px;width:16mm;background:%(fam)s;border-radius:2px;margin:0 0 6mm}

.num{display:flex;gap:6mm;margin-bottom:3.4mm}
.num .n{flex:0 0 8mm;height:8mm;border-radius:50%%;background:%(soft)s;color:%(fam)s;
        font-weight:700;font-size:11pt;display:flex;align-items:center;
        justify-content:center;font-family:'Bitter',serif}
.num h3{font-size:12.2pt;margin-bottom:1.5mm}
.num p{margin:0;color:#33474F}

.cards{display:flex;gap:6mm;margin-bottom:6mm}
.card{flex:1;border:1px solid #DDE7E9;border-left:3px solid %(fam)s;border-radius:3mm;
      padding:5mm 5.5mm 4.5mm;background:#FBFDFD}
.card .tag{font-size:8.4pt;letter-spacing:.09em;text-transform:uppercase;
           color:%(fam)s;font-weight:600}
.card h3{font-size:12.6pt;margin:1.5mm 0 2.5mm}
.card p{margin:0;font-size:10.6pt;color:#33474F}

.note{background:%(soft)s;border-radius:3mm;padding:5.5mm 6mm;font-size:10.8pt;
      color:#25404A}
.note p{margin:0}

.para p{margin-bottom:6mm;font-size:11.4pt}
.para p:first-child::first-letter{font-family:'Bitter',serif;font-size:26pt;
      float:left;line-height:.86;padding:1mm 2.4mm 0 0;color:%(fam)s;font-weight:700}

.pull{margin-top:auto;border-top:1px solid #E3EBED;padding-top:7mm;display:flex;gap:6mm}
.pull .q{font-family:'Bitter',serif;font-size:30pt;line-height:.8;color:%(fam)s}
.pull p{margin:0;font-family:'Bitter',serif;font-size:14pt;line-height:1.5;
        color:#1C3844}

.str{border-top:1px solid #E3EBED;padding:6.5mm 0}
.str:first-of-type{border-top:0;padding-top:0}
.str h3{font-size:12.6pt;margin-bottom:1.5mm;display:flex;align-items:baseline;gap:3mm}
.str h3 span{font-size:9pt;color:%(fam)s;font-family:'Inter',sans-serif;font-weight:600}
.str p{margin:0;color:#33474F}

.grow{margin-bottom:7mm}
.grow h3{font-size:13pt;margin-bottom:2.5mm}
.grow>p{color:#33474F}
.do{border:1px dashed %(fam)s;border-radius:3mm;padding:4.5mm 5.5mm;
    background:#FBFDFD;margin-top:3mm}
.do .lbl{font-size:8.4pt;letter-spacing:.09em;text-transform:uppercase;
         color:%(fam)s;font-weight:700;margin-bottom:1.5mm}
.do p{margin:0;font-size:10.6pt;color:#25404A}

.sch{display:flex;gap:5mm;margin-bottom:7.5mm;align-items:flex-start}
.sch .dot{flex:0 0 3mm;height:3mm;border-radius:50%%;background:%(fam)s;margin-top:2.6mm}
.sch h3{font-size:12.4pt;margin-bottom:1.5mm}
.sch p{margin:0;color:#33474F}

.fit{border-left:3px solid %(soft)s;padding:0 0 0 6mm;margin-bottom:6mm}
.fit h3{font-size:12.2pt;margin-bottom:1.5mm}
.fit p{margin:0;color:#33474F}
.warn{border:1px solid #E8D9B4;background:#FDF8EC;border-radius:3mm;padding:5.5mm 6mm}
.warn .lbl{font-family:'Bitter',serif;font-weight:700;color:#8A6520;margin-bottom:2mm;
           font-size:11.4pt}
.warn p{margin:0;font-size:10.8pt;color:#4A3D22}

.fig{background:%(soft)s;border-radius:3mm;padding:6mm 6.5mm;margin-bottom:7mm}
.fig .who{font-family:'Bitter',serif;font-size:13.6pt;font-weight:700;color:#12303C}
.fig .yr{font-size:9.4pt;color:%(fam)s;font-weight:600;margin-bottom:3mm}
.fig p{margin:0;font-size:10.8pt;color:#26414B}

.chk{display:flex;gap:4mm;align-items:flex-start;margin-bottom:4.2mm}
.chk .box{flex:0 0 4.6mm;height:4.6mm;border:1.6px solid %(fam)s;border-radius:1.2mm;
          margin-top:1mm}
.chk p{margin:0;font-size:10.8pt}
.last{padding-bottom:34mm}   /* room for the absolutely-placed disclaimer */
.close{border-top:1px solid #E3EBED;padding-top:5mm;font-size:11pt;
       color:#33474F;font-style:italic;margin:0}
.disc{position:absolute;left:19mm;right:19mm;bottom:16mm;font-size:8.6pt;color:#8CA2AA;
      border-top:1px solid #E3EBED;padding-top:3mm}
"""

MARK = (u'<svg viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0F6E8C"/>'
        u'<path d="M15 34 Q15 11 32 11 Q49 11 49 34 Z" fill="#fff"/>'
        u'<rect x="13" y="38" width="38" height="11" rx="3.5" fill="#fff"/>'
        u'<path d="M32 16 q4 6 0 11 q-4 -5 0 -11z" fill="#0F6E8C"/></svg>')

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
    pages.append(u"""<section class="page cover"><div class="cvin">
  <div class="mark">%s TestMind</div>
  <div class="kick">%s</div>
  <h1 class="cvname">%s</h1>
  <div><span class="cvfam">%s oilasi</span></div>
  <div class="cvlines">%s</div>
  <div class="cvdisc"></div>
  <div class="cvart">%s</div>
  <div class="cvfoot"><span>%s</span><span>Bepul · 50 savol · Big Five</span></div>
</div></section>""" % (MARK, esc(g['cover_kicker']), esc(a['name']), esc(fam['name']),
                       u''.join(u'<p>%s</p>' % esc(l) for l in a['lines']),
                       a['svg'], SITE))

    # ---- 2. how to read + the two traits -----------------------------------
    howto = u''.join(
        u'<div class="num"><div class="n">%d</div><div><h3>%s</h3><p>%s</p></div></div>'
        % (i + 1, esc(t), esc(b)) for i, (t, b) in enumerate(g['howto']))
    # The two cards are the archetype's two traits, described once in
    # TRAIT_CARDS — so «Xotirjam» reads identically in all four ES guides.
    cards = u''.join(
        u'<div class="card"><div class="tag">%s</div><h3>%s</h3><p>%s</p></div>'
        % (esc(a['traits'][i]), esc(TRAIT_CARDS[t][0]), esc(TRAIT_CARDS[t][1]))
        for i, t in enumerate(key.split('|')))
    page(u"""<h2 class="h2">Bu qoʻllanmani qanday oʻqish kerak</h2><div class="rule"></div>
%s
<h2 class="h2" style="margin-top:7mm">Ikki kuchli tomoningiz</h2>
<p class="sub">%s</p>
<div class="cards">%s</div>
<div class="note"><p>%s</p></div>""" % (howto, esc(g['traits_intro']), cards,
                                        esc(g['traits_note'])))

    # ---- 3. portrait -------------------------------------------------------
    page(u'<h2 class="h2">%s</h2><div class="rule"></div><div class="para">%s</div>'
         u'<div class="pull"><div class="q">&#8220;</div><p>%s</p></div>'
         % (esc(g['portrait_title']),
            u''.join(u'<p>%s</p>' % esc(p) for p in g['portrait']),
            esc(g['portrait_pull'])))

    # ---- 4. strengths ------------------------------------------------------
    strs = u''.join(
        u'<div class="str"><h3>%s <span>%02d</span></h3><p>%s</p></div>'
        % (esc(t), i + 1, esc(b)) for i, (t, b) in enumerate(g['strengths']))
    page(u"""<h2 class="h2">Kuchli tomonlaringiz</h2><div class="rule"></div>
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
    page(u"""<h2 class="h2">Oʻsish nuqtalari</h2><div class="rule"></div>
<p class="sub">Bular kamchilik emas — kuchli tomoningizning teskari tomoni.</p>
<div class="fill">%s</div>""" % grow)

    # ---- 6. school + people ------------------------------------------------
    sch = u''.join(
        u'<div class="sch"><div class="dot"></div><div><h3>%s</h3><p>%s</p></div></div>'
        % (esc(t), esc(b)) for t, b in g['school'])
    page(u"""<h2 class="h2">Maktabda va odamlar orasida</h2><div class="rule"></div>
<p class="sub">Xuddi shu xususiyatlar kundalik ishda qanday ishlaydi.</p>
%s""" % sch)

    # ---- 7. future ---------------------------------------------------------
    fits = u''.join(u'<div class="fit"><h3>%s</h3><p>%s</p></div>' % (esc(t), esc(b))
                    for t, b in g['future_fits'])
    page(u"""<h2 class="h2">Kelajak yoʻnalishlari</h2><div class="rule"></div>
<p class="sub">%s</p>
<div class="fill"><div>%s</div>
<div class="warn"><div class="lbl">Eʼtibor bering</div><p>%s</p></div>
<div class="note"><p><b>Keyingi qadam.</b> %s</p></div></div>"""
         % (esc(g['future_intro']), fits, esc(g['future_watch']),
            esc(g['future_next'])))

    # ---- 8. figure + practice ---------------------------------------------
    chk = u''.join(u'<div class="chk"><div class="box"></div><p>%s</p></div>' % esc(c)
                   for c in g['practice'])
    page(u"""<h2 class="h2">Shu xususiyat kimda kuchli boʻlgan</h2><div class="rule"></div>
<div class="fig"><div class="who">%s</div><div class="yr">%s</div><p>%s</p></div>
<h2 class="h2">Ikki haftalik amaliyot</h2><div class="rule"></div>
<p class="sub">%s</p>
<div class="fill"><div>%s</div>
<p class="close">%s</p></div>
<div class="disc">%s</div>""" % (
             esc(a['figure']['who']), esc(a['figure']['years']), esc(g['figure_why']),
             esc(g['practice_intro']), chk, esc(g['closing']), DISCLAIMER), 'last')

    css = CSS % {'bitter': font64('bitter.woff2'), 'inter': font64('inter.woff2'),
                 'fam': fam['c'], 'soft': fam['soft']}
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
