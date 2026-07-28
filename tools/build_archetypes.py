# -*- coding: utf-8 -*-
u"""Generates one page per archetype per language — ten pages x three languages.

Driven by characters.js (the Uzbek original) and strings.js (the Russian and
English overlay), which are the same two files the browser loads. Nothing is
retyped here, so a page and the live site cannot disagree about what an
archetype is called.
"""
import io, json, os, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_pages as bp
import life_content as lc
import build_life_js
from i18n import S, LANGS, DIR

OUT = 'C:/Users/Asus/TestMind-site/'

# Pull the data straight out of the shipped files, resolving each language the
# same way strings.js does at runtime: translated field, else the Uzbek base.
dump = subprocess.check_output(['node', '-e', ('''
const fs=require('fs'),vm=require('vm');
const s={document:{documentElement:{getAttribute(){return 'uz';}}}};
vm.createContext(s);
vm.runInContext(fs.readFileSync(%r,'utf8'),s);   // characters.js
vm.runInContext(fs.readFileSync(%r,'utf8'),s);   // strings.js
const LANGS=%s;
const pick=(t,base,k)=>(t&&t[k])||base[k];
const arch={},fams={};
for (const k in s.ARCHETYPES){
  const a=s.ARCHETYPES[k], by={};
  for (const L of LANGS){
    const S=s.STRINGS[L]||{}, t=(S.arch||{})[k]||{}, f=t.figure||{};
    const name=pick(t,a,'name');
    by[L]={name, lines:pick(t,a,'lines'),
           strength:pick(t,a,'strength'), watch:pick(t,a,'watch'),
           figure:{who:f.who||a.figure.who, years:a.figure.years,
                   why:f.why||a.figure.why},
           traits:k.split('|').map(x=>(S.traits||{})[x]||s.TRAIT_NAMES[x]),
           svg:s.charSvg(k,name)};
  }
  arch[k]={slug:a.slug, fam:a.fam, byLang:by};
}
for (const f in s.FAMILIES){
  const F=s.FAMILIES[f], name={}, note={};
  for (const L of LANGS){
    const S=s.STRINGS[L]||{};
    name[L]=(S.fam||{})[f]||F.name;
    note[L]=(S.famnote||{})[f]||s.FAM_NOTES[f];
  }
  fams[f]={c:F.c, soft:F.soft, dark:F.dark, lit:F.lit, name, note};
}
process.stdout.write(JSON.stringify({arch,fams}));
''' % (OUT + 'characters.js', OUT + 'strings.js', json.dumps(LANGS)))])
data = json.loads(dump.decode('utf-8'))
ARCH, FAMS = data['arch'], data['fams']

BODY = u"""<article class="apage" style="--fam:%(famc)s;--famsoft:%(famsoft)s;--famdark:%(famdark)s;--famlit:%(famlit)s">
  <header class="ahero">
    <div class="wrap ahin">
      <div class="aart">%(svg)s</div>
      <div class="ameta">
        <a class="afam" href="obrazlar.html">%(famname)s</a>
        <h1>%(name)s</h1>
        <p class="alead">%(line0)s</p>
        <p class="alead">%(line1)s</p>
      </div>
    </div>
  </header>

  <section><div class="wrap" style="max-width:820px">
    <div class="abox strong"><h2>%(l_strength)s</h2><p>%(strengthcap)s</p></div>
    <div class="abox warn"><h2>%(l_watch)s</h2><p>%(watch)s</p></div>

    <h2 class="asec">%(l_how)s</h2>
    <p>%(how)s</p>
    <p class="amuted">%(hownote)s</p>

    <h2 class="asec">%(l_fig)s</h2>
    <div class="afig"><div class="afigwho">%(figwho)s <span>%(figyears)s</span></div>
      <p>%(figwhy)s</p></div>

    <h2 class="asec">%(l_guide)s</h2>
    <div class="aguide">
      <div>
        <b>%(guideb)s</b>
        <p class="amuted">%(guidep)s%(guidelang)s</p>
      </div>
      <a class="btn" href="guides/%(slug)s.pdf" download>%(guidebtn)s</a>
    </div>

    %(life)s

    <h2 class="asec">%(l_sibs)s</h2>
    <p class="amuted">%(famnote)s</p>
    <div class="sibs">%(sibs)s</div>
  </div></section>
</article>
"""

def esc(s):
    return s.replace(u'&', u'&amp;').replace(u'<', u'&lt;').replace(u'>', u'&gt;')


def life_html(key, lang):
    u"""Oilada / Maktabda / Munosabatlarda plus the suggested directions.

    Only Uzbek for now: this is long-form written copy, and a machine-shaped
    Russian rendering of it would read worse than not offering it at all. The
    section simply does not appear on the ru/ and en/ pages until it is written.
    Returns '' for any archetype not yet written, so the ten pages keep
    building while the content lands one at a time.
    """
    if lang != 'uz' or key not in lc.LIFE:
        return u''
    d = lc.LIFE[key]
    out = u''
    for area in ('family', 'school', 'friends'):
        if area not in d:
            continue
        title, sub = lc.AREA_TITLES[area]
        cols = u''
        for kind, label, cls in (('strong', lc.STRONG_LABEL, 'good'),
                                 ('weak', lc.WEAK_LABEL, 'watch')):
            items = u''.join(
                u'<li><b>%s</b> %s</li>' % (esc(t), esc(p)) for t, p in d[area][kind])
            cols += u'<div class="lifecol %s"><h4>%s</h4><ul>%s</ul></div>' % (cls, label, items)
        out += (u'<h3 class="lifehead">%s <span>%s</span></h3>'
                u'<div class="lifegrid">%s</div>') % (esc(title), esc(sub), cols)

    if d.get('careers'):
        rows = sorted(((lc.pct(key, w), n, why) for n, w, why in d['careers']), reverse=True)
        items = u''.join(
            u'<li class="career"><div class="carhead"><span class="carname">%s</span>'
            u'<span class="carpct">%d%%</span></div>'
            u'<div class="carbar"><i style="width:%d%%"></i></div>'
            u'<p class="carwhy">%s</p></li>' % (esc(n), p, p, esc(why))
            for p, n, why in rows)
        out += (u'<h3 class="lifehead">%s</h3><ul class="careers">%s</ul>'
                u'<p class="cardisc">%s</p>') % (
            esc(lc.CAREER_TITLE), items, esc(lc.DISCLAIMER))
    return out


count = 0
for lang in LANGS:
    t = S[lang]
    for key, a in ARCH.items():
        v = a['byLang'][lang]
        fam = FAMS[a['fam']]
        siblings = [(b['slug'], b['byLang'][lang])
                    for k, b in ARCH.items() if b['fam'] == a['fam'] and k != key]
        sib_html = u''.join(
            u'<a class="sib" href="obraz-%s.html"><span class="sibart">%s</span>'
            u'<span class="sibname">%s</span></a>' % (slug, bv['svg'], bv['name'])
            for slug, bv in siblings)

        # The guide PDFs exist only in Uzbek; say so on the pages where that is
        # news, rather than after the download.
        guidelang = (u' ' + t['arch.guide.lang']) if t['arch.guide.lang'] else u''

        body = BODY % {
            'famc': fam['c'], 'famsoft': fam['soft'],
            'famdark': fam['dark'], 'famlit': fam['lit'],
            'famname': fam['name'][lang], 'famnote': fam['note'][lang],
            'svg': v['svg'], 'name': v['name'], 'slug': a['slug'],
            'line0': v['lines'][0], 'line1': v['lines'][1],
            'l_strength': t['arch.strength'], 'l_watch': t['arch.watch'],
            'strengthcap': v['strength'][0].upper() + v['strength'][1:],
            'watch': v['watch'],
            'l_how': t['arch.how.h2'],
            'how': t['arch.how.p'] % {'t0': v['traits'][0], 't1': v['traits'][1]},
            'hownote': t['arch.how.note'],
            'l_fig': t['arch.fig.h2'], 'figwho': v['figure']['who'],
            'figyears': v['figure']['years'], 'figwhy': v['figure']['why'],
            'l_guide': t['arch.guide.h2'],
            'guideb': t['arch.guide.b'] % {'name': v['name']},
            'guidep': t['arch.guide.p'], 'guidelang': guidelang,
            'guidebtn': t['arch.guide.btn'],
            'l_sibs': t['arch.sibs.h2'] % {'fam': fam['name'][lang]},
            'sibs': sib_html, 'life': life_html(key, lang),
        }

        fname = 'obraz-%s.html' % a['slug']
        title = t['arch.title'] % {'name': v['name']}
        desc = u'%s %s' % (v['lines'][0], v['strength'])
        html = bp.head(lang, title, desc, fname) + bp.nav(lang, fname, 'obrazlar.html') \
             + body + bp.close(lang) + bp.footer(lang) + bp.SCRIPTS
        bp.write(OUT + DIR[lang] + fname, bp.localize(html, lang))
        count += 1
    print('wrote %2d archetype pages to %s' % (len(ARCH), DIR[lang] or './'))

print('%d pages total' % count)

# life.js carries the same content to the result screen in test.html, which is a
# standalone client-side app and cannot read life_content.py. Regenerated here so
# the two can never disagree.
build_life_js.build()

# The sitemap lists every page both generators produce, so it is written last,
# once, from the slugs we just used.
bp.write_sitemap([a['slug'] for a in ARCH.values()])
