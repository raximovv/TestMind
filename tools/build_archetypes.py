# -*- coding: utf-8 -*-
"""Generates one page per archetype, driven by characters.js so nothing can drift."""
import io, json, subprocess, sys

OUT = 'C:/Users/Asus/TestMind-site/'

# pull the data straight out of the shipped characters.js
dump = subprocess.check_output(['node', '-e', '''
const fs=require('fs'),vm=require('vm');const s={};vm.createContext(s);
vm.runInContext(fs.readFileSync('C:/Users/Asus/TestMind-site/characters.js','utf8'),s);
const out={};
for (const k in s.ARCHETYPES){
  const a=s.ARCHETYPES[k];
  out[k]={name:a.name,slug:a.slug,fam:a.fam,lines:a.lines,strength:a.strength,
          watch:a.watch,figure:a.figure,svg:s.charSvg(k,a.name),
          traits:k.split('|').map(x=>s.TRAIT_NAMES[x])};
}
process.stdout.write(JSON.stringify({arch:out,fams:s.FAMILIES}));
'''])
data = json.loads(dump.decode('utf-8'))
ARCH, FAMS = data['arch'], data['fams']

sys.path.insert(0, 'C:/Users/Asus/AppData/Local/Temp/claude/C--Users-Asus/'
                   'faec2f98-6d9f-4a7e-bfde-43b1971bf1bb/scratchpad/render')
import os, importlib.util
spec = importlib.util.spec_from_file_location('bp',
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build_pages.py'))
bp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bp)   # reuses head(), nav(), FOOTER, SCRIPTS and rewrites the other pages

FAM_NOTES = {
    'lead': u'Odamlarni ortidan ergashtiradiganlar',
    'crea': u'Yangi gʻoya va yechim topadiganlar',
    'care': u'Atrofdagilarni koʻradigan va qoʻllab-quvvatlaydiganlar',
    'base': u'Vaʼdasida turadigan, ishonchli odamlar',
}

for key, a in ARCH.items():
    fam = FAMS[a['fam']]
    siblings = [b for k, b in ARCH.items() if b['fam'] == a['fam'] and k != key]
    sib_html = u''.join(
        u'<a class="sib" href="obraz-%s.html"><span class="sibart">%s</span>'
        u'<span class="sibname">%s</span></a>' % (b['slug'], b['svg'], b['name'])
        for b in siblings)

    body = u"""<article class="apage" style="--fam:%(famc)s;--famsoft:%(famsoft)s">
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
    <div class="abox strong"><h2>Kuchli tomoningiz</h2><p>%(strengthcap)s</p></div>
    <div class="abox warn"><h2>Eʼtibor bering</h2><p>%(watch)s</p></div>

    <h2 class="asec">Bu obraz qanday chiqadi</h2>
    <p>Bu obraz ikkita eng kuchli xususiyatingizdan tugʻiladi: <b>%(t0)s</b> va <b>%(t1)s</b>.
       Boshqa uchtasi ham sizda bor — shunchaki bu ikkisi ulardan koʻra kuchliroq chiqqan.</p>
    <p class="amuted">Agar bu ikki xususiyat bir-biriga juda yaqin boʻlsa, test yakunida sizga
       ikkinchi obraz ham koʻrsatiladi. Natija — bugungi suratingiz, oʻzgarmas yorliq emas.</p>

    <h2 class="asec">Shu xususiyat kimda kuchli boʻlgan</h2>
    <div class="afig"><div class="afigwho">%(figwho)s <span>%(figyears)s</span></div>
      <p>%(figwhy)s</p></div>

    <h2 class="asec">%(famname)s oilasidagi boshqa obrazlar</h2>
    <p class="amuted">%(famnote)s</p>
    <div class="sibs">%(sibs)s</div>
  </div></section>
</article>
""" % {
        'famc': fam['c'], 'famsoft': fam['soft'], 'famname': fam['name'],
        'famnote': FAM_NOTES[a['fam']], 'svg': a['svg'], 'name': a['name'],
        'line0': a['lines'][0], 'line1': a['lines'][1],
        'strengthcap': a['strength'][0].upper() + a['strength'][1:],
        'watch': a['watch'], 't0': a['traits'][0], 't1': a['traits'][1],
        'figwho': a['figure']['who'], 'figyears': a['figure']['years'],
        'figwhy': a['figure']['why'], 'sibs': sib_html,
    }

    title = u'%s — TestMind obrazlari' % a['name']
    desc = u'%s %s' % (a['lines'][0], a['strength'])
    html = bp.head(title, desc) + bp.nav('obrazlar.html') + body + bp.CLOSE + bp.FOOTER + bp.SCRIPTS
    fname = 'obraz-%s.html' % a['slug']
    io.open(OUT + fname, 'w', encoding='utf-8', newline='').write(html)
    print('wrote %-38s %6d bytes' % (fname, len(html.encode('utf-8'))))
