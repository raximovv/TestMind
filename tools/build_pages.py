# -*- coding: utf-8 -*-
u"""Generates the static TestMind pages, in every language, so the nav and footer
can never drift — between pages or between languages.

Uzbek is written to the repo root, Russian to ru/ and English to en/, so every
link already shared in the wild keeps working. Page filenames are identical in
all three languages; only the prose differs (see i18n.py).

test.html, site.css, site.js and characters.js are shared, single-copy files at
the root. Pages in ru/ and en/ reach them with ../ — see localize().
"""
import io, json, os, re

import i18n
from i18n import S, LANGS, DIR, UP, HTML_LANG, OG_LOCALE, LANG_SHORT, LANG_FULL

OUT = 'C:/Users/Asus/TestMind-site/'

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
           "%3Crect width='64' height='64' rx='14' fill='%230F6E8C'/%3E"
           "%3Cpath d='M15 34 Q15 11 32 11 Q49 11 49 34 Z' fill='%23fff'/%3E"
           "%3Crect x='13' y='38' width='38' height='11' rx='3.5' fill='%23fff'/%3E"
           "%3Cpath d='M32 16 q4 6 0 11 q-4 -5 0 -11z' fill='%230F6E8C'/%3E%3C/svg%3E")

SITE = 'https://raximovv.github.io/TestMind'   # one line to change on the .uz domain

EMAIL = 'raximovrahim1@gmail.com'

# Files that exist once, at the root, and are NOT translated. A page in ru/ or
# en/ has to climb out of its folder to reach them; everything else stays a
# plain relative link, because the translated pages sit beside each other.
# Kept as an explicit list rather than a clever rule so that adding a shared
# asset is a deliberate act.
ROOT_ONLY = ['test.html', 'site.css', 'site.js', 'characters.js', 'strings.js',
             'fonts/', 'guides/']
_ROOT_RE = re.compile(r'(href|src)="(%s)' % '|'.join(
    re.escape(f) for f in ROOT_ONLY))


def localize(html, lang):
    u"""Point the shared root files at ../ for the non-root languages."""
    up = UP[lang]
    if not up:
        return html
    return _ROOT_RE.sub(lambda m: '%s="%s%s' % (m.group(1), up, m.group(2)), html)


def url_for(lang, fname):
    u"""Absolute URL of one page in one language."""
    return u'%s/%s%s' % (SITE, DIR[lang], '' if fname == 'index.html' else fname)


def head(lang, title, desc, fname, extra=u''):
    u"""`fname` produces the canonical URL and the hreflang set, which is what
    stops the three languages from competing with each other in search results:
    each says "I am the <lang> version of this page, here are my siblings"."""
    alts = u''.join(
        u'\n<link rel="alternate" hreflang="%s" href="%s">' % (HTML_LANG[l], url_for(l, fname))
        for l in LANGS)
    alts += u'\n<link rel="alternate" hreflang="x-default" href="%s">' % url_for('uz', fname)
    return u"""<!doctype html>
<html lang="%s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:type" content="website">
<meta property="og:site_name" content="TestMind">
<meta property="og:locale" content="%s">
<meta property="og:image" content="%s/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="%s">
<link rel="canonical" href="%s">%s
<link rel="preload" href="fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="site.css">%s
</head>
<body>
""" % (HTML_LANG[lang], title, desc, title, desc, OG_LOCALE[lang], SITE, FAVICON,
       url_for(lang, fname), alts, extra)


def langsw(lang, fname):
    u"""UZ · RU · EN, each pointing at the same page in the other language.

    Deliberately plain links, and deliberately no automatic redirect based on
    the browser's Accept-Language: auto-switching breaks shared links and traps
    people in a language they did not choose."""
    out = u''
    for l in LANGS:
        if l == lang:
            out += u'<span aria-current="true">%s</span>' % LANG_SHORT[l]
        else:
            out += u'<a href="%s%s%s" hreflang="%s" lang="%s" title="%s">%s</a>' % (
                UP[lang], DIR[l], fname, HTML_LANG[l], HTML_LANG[l],
                LANG_FULL[l], LANG_SHORT[l])
    return u'<div class="langsw" role="group" aria-label="%s">%s</div>' % (
        S[lang]['nav.langlabel'], out)


def nav(lang, fname, active=None):
    t = S[lang]
    items = [('index.html', t['nav.home']), ('obrazlar.html', t['nav.types']),
             ('test.html', t['nav.test']),
             ('qanday-ishlaydi.html', t['nav.how']), ('savollar.html', t['nav.faq'])]
    active = active or fname
    links = ''
    for href, label in items:
        cur = ' aria-current="page"' if href == active else ''
        links += u'\n    <a href="%s"%s>%s</a>' % (href, cur, label)
    return u"""<nav class="nav"><div class="wrap navin">
  <a class="brand" href="index.html">TestMind</a>
  <div class="navlinks">%s
  </div>
  %s
  <a class="btn sm" href="test.html" data-cta>%s</a>
</div></nav>
""" % (links, langsw(lang, fname), t['nav.cta'])


SOCIAL = u'<div class="socrow" aria-hidden="true"><span class="soc" title="Telegram"><svg viewBox="0 0 24 24"><path fill="#fff" d="M9.78 18.65l.28-4.23 7.68-6.92c.34-.31-.07-.46-.52-.19L7.74 13.3 3.64 12c-.88-.25-.89-.86.2-1.3l15.97-6.16c.73-.33 1.43.18 1.15 1.3l-2.72 12.81c-.19.91-.74 1.13-1.5.71L12.6 16.3l-1.99 1.93c-.23.23-.42.42-.83.42z"/></svg></span><span class="soc" title="Instagram"><svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="4.6" fill="none" stroke="#fff" stroke-width="1.9"/><circle cx="12" cy="12" r="3.6" fill="none" stroke="#fff" stroke-width="1.9"/><circle cx="16.6" cy="7.4" r="1.15" fill="#fff"/></svg></span><span class="soc" title="Facebook"><svg viewBox="0 0 24 24"><path fill="#fff" d="M13.4 21v-7.1h2.38l.36-2.77H13.4V9.35c0-.8.22-1.35 1.38-1.35h1.47V5.52c-.25-.03-1.13-.11-2.15-.11-2.13 0-3.58 1.3-3.58 3.68v2.05H8.13v2.77h2.39V21z"/></svg></span><span class="soc" title="YouTube"><svg viewBox="0 0 24 24"><path fill="#fff" d="M21.58 8.2a2.47 2.47 0 0 0-1.74-1.75C18.3 6.03 12 6.03 12 6.03s-6.3 0-7.84.42A2.47 2.47 0 0 0 2.42 8.2 25.9 25.9 0 0 0 2 12a25.9 25.9 0 0 0 .42 3.8 2.47 2.47 0 0 0 1.74 1.75c1.54.42 7.84.42 7.84.42s6.3 0 7.84-.42a2.47 2.47 0 0 0 1.74-1.75A25.9 25.9 0 0 0 22 12a25.9 25.9 0 0 0-.42-3.8z"/><path fill="var(--lazur)" d="M10.05 14.85l5.2-2.85-5.2-2.85z"/></svg></span><span class="soc" title="TikTok"><svg viewBox="0 0 24 24"><path fill="#fff" d="M16.6 3c.28 1.9 1.35 3.16 3.4 3.32v2.4c-1.18.11-2.2-.27-3.4-.98v5.55c0 4.05-4.41 5.31-6.18 2.41-1.14-1.87-.44-5.15 3.23-5.28v2.53c-.28.05-.58.12-.85.22-.82.32-1.28 1.14-1.05 1.99.24.88 1.36 1.53 2.26.9.55-.38.7-1 .7-1.66V3z"/></svg></span></div>'


def footer(lang):
    t = S[lang]
    # In ru/en the test link leads somewhere Uzbek-only; say so next to the link
    # rather than letting the reader discover it after the click.
    note = (u' <span class="fnote">(%s)</span>' % t['foot.testnote']) if UP[lang] else u''
    return u"""<footer class="foot"><div class="wrap">
  <div class="footgrid">
    <div class="footcol"><h2>TestMind</h2><ul>
      <li><a href="index.html">%(home)s</a></li>
      <li><a href="obrazlar.html">%(types10)s</a></li>
      <li><a href="qanday-ishlaydi.html">%(how)s</a></li>
    </ul></div>
    <div class="footcol"><h2>%(test)s</h2><ul>
      <li><a href="test.html" data-cta>%(cta)s</a>%(note)s</li>
      <li><a href="savollar.html">%(faqlong)s</a></li>
    </ul></div>
    <div class="footcol"><h2>%(about)s</h2><ul>
      <li><a href="privacy.html">%(privacy)s</a></li>
      <li><a href="qanday-ishlaydi.html#model">%(model)s</a></li>
      <li><a href="maktablar.html">%(schools)s</a></li>
    </ul></div>
    <div class="footcol"><h2>%(contact)s</h2><ul>
      <li><a href="mailto:%(email)s">%(email)s</a></li>
    </ul>
      %(social)s</div>
  </div>
  <div class="footbar">
    <span>© 2026 TestMind</span>
    <span>%(disclaimer)s</span>
  </div>
</div></footer>
""" % {'home': t['nav.home'], 'types10': t['foot.types10'], 'how': t['nav.how'],
       'test': t['foot.test'], 'cta': t['nav.cta'], 'note': note,
       'faqlong': t['foot.faqlong'], 'about': t['foot.about'],
       'privacy': t['foot.privacy'], 'model': t['foot.model'],
       'schools': t['foot.schools'], 'contact': t['foot.contact'],
       'email': EMAIL, 'social': SOCIAL, 'disclaimer': t['foot.disclaimer']}


SCRIPTS = u"""<script src="characters.js"></script>
<script src="strings.js"></script>
<script src="site.js"></script>
</body>
</html>
"""


def close(lang):
    t = S[lang]
    note = (u'\n  <p class="testlang">%s</p>' % t['testlang.note']) if t['testlang.note'] else u''
    return u"""<section class="close">
  <h2>%s</h2>
  <p>%s</p>
  <a class="btn big" href="test.html" data-cta>%s</a>%s
</section>
""" % (t['close.h2'], t['close.p'], t['nav.cta'], note)


# ---------------------------------------------------------------- home
HOME = u"""<header class="hero" id="top">
  <div style="text-align:center;padding:52px 20px 28px;max-width:760px;margin:0 auto">
    <h1>%(home.h1)s</h1>
    <p class="lead" style="font-size:clamp(16px,2.4vw,19px);margin-bottom:26px">
      %(home.lead)s</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
      <a class="btn big" href="test.html" data-cta>%(nav.cta)s</a>
      <a class="btn big ghost" href="obrazlar.html">%(home.cta2)s</a>
    </div>
  </div>
  <div class="scene" id="scene" aria-hidden="true"></div>
  <p class="scenecap">%(home.scenecap)s</p>
</header>

<section class="alt">
  <div class="wrap">
    <div class="center"><h2>%(home.num.h2)s</h2>
      <p class="lead">%(home.num.lead)s</p></div>
    <div class="facts">
      <div class="fact"><div class="factn">0</div><div class="factl">%(home.fact1)s</div></div>
      <div class="fact"><div class="factn">0</div><div class="factl">%(home.fact2)s</div></div>
      <div class="fact"><div class="factn">0</div><div class="factl">%(home.fact3)s</div></div>
      <div class="fact"><div class="factn">0</div><div class="factl">%(home.fact4)s</div></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="panel">
      <div class="ptext">
        <span class="ptag">%(home.p1.tag)s</span>
        <h2>%(home.p1.h2)s</h2>
        <p>%(home.p1.p)s</p>
        <a class="btn" href="test.html" data-cta>%(nav.cta)s</a>
      </div>
      <div class="part" id="vg-result"></div>
    </div>

    <div class="panel flip">
      <div class="ptext">
        <span class="ptag">%(home.p2.tag)s</span>
        <h2>%(home.p2.h2)s</h2>
        <p>%(home.p2.p)s</p>
        <a class="btn ghost" href="obrazlar.html">%(home.p2.btn)s</a>
      </div>
      <div class="part" id="vg-others"></div>
    </div>

    <div class="panel">
      <div class="ptext">
        <span class="ptag">%(home.p3.tag)s</span>
        <h2>%(home.p3.h2)s</h2>
        <p>%(home.p3.p)s</p>
        <a class="btn ghost" href="qanday-ishlaydi.html">%(home.p3.btn)s</a>
      </div>
      <div class="part" id="vg-future"></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="center"><h2>%(home.why.h2)s</h2>
      <p class="lead">%(home.why.lead)s</p></div>
    <div class="why">
      <div class="wcard"><h3>%(home.w1.h3)s</h3><p>%(home.w1.p)s</p></div>
      <div class="wcard"><h3>%(home.w2.h3)s</h3><p>%(home.w2.p)s</p></div>
      <div class="wcard"><h3>%(home.w3.h3)s</h3><p>%(home.w3.p)s</p></div>
      <div class="wcard"><h3>%(home.w4.h3)s</h3><p>%(home.w4.p)s</p></div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- obrazlar
OBRAZLAR = u"""<header class="phead"><div class="wrap">
  <h1>%(types.h1)s</h1>
  <p class="lead">%(types.lead)s</p>
</div></header>

<div id="bands"></div>
"""

# ---------------------------------------------------------------- how it works
QANDAY = u"""<header class="phead"><div class="wrap">
  <h1>%(how.h1)s</h1>
  <p class="lead">%(how.lead)s</p>
</div></header>

<section><div class="wrap">
  <h2>%(how.steps.h2)s</h2>
  <p class="lead">%(how.steps.lead)s</p>
  <div class="steps">
    <div class="step"><div class="stepn">1</div>
      <h3>%(how.s1.h3)s</h3>
      <p>%(how.s1.p)s</p></div>
    <div class="step"><div class="stepn">2</div>
      <h3>%(how.s2.h3)s</h3>
      <p>%(how.s2.p)s</p></div>
    <div class="step"><div class="stepn">3</div>
      <h3>%(how.s3.h3)s</h3>
      <p>%(how.s3.p)s</p></div>
  </div>
</div></section>

<section class="alt" id="model"><div class="wrap">
  <h2>%(how.model.h2)s</h2>
  <p class="lead">%(how.model.lead)s</p>
  <div class="why">
    <div class="wcard"><h3>%(how.m1.h3)s</h3><p>%(how.m1.p)s</p></div>
    <div class="wcard"><h3>%(how.m2.h3)s</h3><p>%(how.m2.p)s</p></div>
    <div class="wcard"><h3>%(how.m3.h3)s</h3><p>%(how.m3.p)s</p></div>
    <div class="wcard"><h3>%(how.m4.h3)s</h3><p>%(how.m4.p)s</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <h2>%(how.data.h2)s</h2>
  <p class="lead">%(how.data.lead)s</p>
  <div class="why">
    <div class="wcard"><h3>%(how.d1.h3)s</h3><p>%(how.d1.p)s</p></div>
    <div class="wcard"><h3>%(how.d2.h3)s</h3><p>%(how.d2.p)s</p></div>
    <div class="wcard"><h3>%(how.d3.h3)s</h3><p>%(how.d3.p)s</p></div>
    <div class="wcard"><h3>%(how.d4.h3)s</h3>
      <p><a href="privacy.html">%(how.d4.link)s</a>%(how.d4.after)s</p></div>
  </div>
</div></section>
"""

# ---------------------------------------------------------------- faq
SAVOLLAR = u"""<header class="phead"><div class="wrap">
  <h1>%(faq.h1)s</h1>
  <p class="lead">%(faq.lead)s</p>
</div></header>

<section><div class="wrap"><div class="faq">
  <details><summary>%(faq.q1)s</summary><p>%(faq.a1)s</p></details>
  <details><summary>%(faq.q2)s</summary><p>%(faq.a2)s</p></details>
  <details><summary>%(faq.q3)s</summary><p>%(faq.a3)s</p></details>
  <details><summary>%(faq.q4)s</summary><p>%(faq.a4)s</p></details>
  <details><summary>%(faq.q5)s</summary><p>%(faq.a5)s</p></details>
  <details><summary>%(faq.q6)s</summary><p>%(faq.a6)s</p></details>
  <details><summary>%(faq.q7)s</summary><p>%(faq.a7)s</p></details>
  <details><summary>%(faq.q8)s</summary><p>%(faq.a8)s</p></details>
  <details><summary>%(faq.q9)s</summary><p>%(faq.a9)s</p></details>
</div></div></section>
"""

# ---------------------------------------------------------------- privacy
PRIVACY = u"""<header class="phead"><div class="wrap">
  <h1>%(priv.h1)s</h1>
  <p class="lead">%(priv.lead)s</p>
</div></header>

<section><div class="wrap" style="max-width:780px">
  <h2>%(priv.h.stored)s</h2>
  <p>%(priv.p.stored)s</p>

  <h2>%(priv.h.never)s</h2>
  <p>%(priv.p.never)s</p>

  <h2>%(priv.h.answers)s</h2>
  <p>%(priv.p.answers1)s</p>
  <p>%(priv.p.answers2)s</p>
  <p>%(priv.p.answers3)s</p>

  <h2>%(priv.h.email)s</h2>
  <p>%(priv.p.email1)s</p>
  <p>%(priv.p.email2)s</p>
  <p>%(priv.p.email3)s</p>

  <h2>%(priv.h.device)s</h2>
  <p>%(priv.p.device)s</p>

  <h2>%(priv.h.third)s</h2>
  <p>%(priv.p.third)s</p>

  <h2>%(priv.h.result)s</h2>
  <p>%(priv.p.result)s</p>

  <h2>%(priv.h.age)s</h2>
  <p>%(priv.p.age)s</p>

  <h2>%(priv.h.contact)s</h2>
  <p>%(priv.p.contact)s
     <a href="mailto:%(email)s">%(email)s</a>.</p>
</div></section>
"""

# ---------------------------------------------------------------- schools / parents
MAKTABLAR = u"""<header class="phead"><div class="wrap">
  <h1>%(sch.h1)s</h1>
  <p class="lead">%(sch.lead)s</p>
</div></header>

<section><div class="wrap" style="max-width:820px">
  <h2>%(sch.h.what)s</h2>
  <p>%(sch.p.what)s</p>

  <h2>%(sch.h.notwhat)s</h2>
  <p>%(sch.p.notwhat)s</p>

  <h2>%(sch.h.limits)s</h2>
  <div class="why" style="margin-top:14px">
    <div class="wcard"><h3>%(sch.l1.h3)s</h3><p>%(sch.l1.p)s</p></div>
    <div class="wcard"><h3>%(sch.l2.h3)s</h3><p>%(sch.l2.p)s</p></div>
    <div class="wcard"><h3>%(sch.l3.h3)s</h3><p>%(sch.l3.p)s</p></div>
    <div class="wcard"><h3>%(sch.l4.h3)s</h3><p>%(sch.l4.p)s</p></div>
  </div>

  <h2>%(sch.h.howto)s</h2>
  <div class="steps" style="margin-top:14px">
    <div class="step"><div class="stepn">1</div>
      <h3>%(sch.t1.h3)s</h3><p>%(sch.t1.p)s</p></div>
    <div class="step"><div class="stepn">2</div>
      <h3>%(sch.t2.h3)s</h3><p>%(sch.t2.p)s</p></div>
    <div class="step"><div class="stepn">3</div>
      <h3>%(sch.t3.h3)s</h3><p>%(sch.t3.p)s</p></div>
  </div>

  <h2>%(sch.h.dont)s</h2>
  <div class="why" style="margin-top:14px">
    <div class="wcard"><h3>%(sch.d1.h3)s</h3><p>%(sch.d1.p)s</p></div>
    <div class="wcard"><h3>%(sch.d2.h3)s</h3><p>%(sch.d2.p)s</p></div>
    <div class="wcard"><h3>%(sch.d3.h3)s</h3><p>%(sch.d3.p)s</p></div>
    <div class="wcard"><h3>%(sch.d4.h3)s</h3><p>%(sch.d4.p)s</p></div>
  </div>

  <h2>%(sch.h.data)s</h2>
  <p>%(sch.p.data1)s</p>
  <p>%(sch.p.data2)s</p>
  <p>%(sch.p.data3)s</p>
  <p>%(sch.p.data4)s</p>

  <h2>%(sch.h.contact)s</h2>
  <p>%(sch.p.contact)s
     <a href="mailto:%(email)s">%(email)s</a>.
     %(sch.p.contact2)s</p>
</div></section>
"""

# fname -> (template, title key, desc key, appends the closing CTA)
PAGES = [
    ('index.html',           HOME,      'home.title',  'home.desc',  True),
    ('obrazlar.html',        OBRAZLAR,  'types.title', 'types.desc', True),
    ('qanday-ishlaydi.html', QANDAY,    'how.title',   'how.desc',   True),
    ('savollar.html',        SAVOLLAR,  'faq.title',   'faq.desc',   True),
    ('privacy.html',         PRIVACY,   'priv.title',  'priv.desc',  False),
    ('maktablar.html',       MAKTABLAR, 'sch.title',   'sch.desc',   False),
]


def jsonld(obj):
    return u'\n<script type="application/ld+json">%s</script>' % json.dumps(
        obj, ensure_ascii=False, separators=(',', ':'))


# Only two pages carry structured data, and only where it is honestly true: the
# site itself, and the FAQ page (which is genuinely a list of questions and
# answers). Marking anything else up would be decoration, not description.
def site_ld(lang):
    return jsonld({
        '@context': 'https://schema.org', '@type': 'WebSite',
        'name': 'TestMind', 'url': url_for(lang, 'index.html'),
        'inLanguage': HTML_LANG[lang], 'description': S[lang]['home.desc'],
    })


def faq_ld(html):
    u"""Read the FAQ entries back out of the page we just built, so the structured
    data can never describe questions the page does not actually contain."""
    pairs = re.findall(r'<summary>(.*?)</summary>(.*?)</details>', html, re.S)
    strip = lambda s: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s)).strip()
    return jsonld({
        '@context': 'https://schema.org', '@type': 'FAQPage',
        'mainEntity': [{
            '@type': 'Question', 'name': strip(q),
            'acceptedAnswer': {'@type': 'Answer', 'text': strip(a)},
        } for q, a in pairs],
    })


def fill(tpl, lang):
    u"""%(key)s substitution straight from the language's string table.

    A key that is missing raises KeyError and stops the build — which is the
    point: a half-translated page should never reach the repo.
    """
    d = dict(S[lang])
    d['email'] = EMAIL
    return tpl % d


def build_page(lang, fname, tpl, tkey, dkey, with_close):
    t = S[lang]
    body = fill(tpl, lang)
    if with_close:
        body += close(lang)
    extra = u''
    if fname == 'index.html':
        extra = site_ld(lang)
    elif fname == 'savollar.html':
        extra = faq_ld(body)
    html = head(lang, t[tkey], t[dkey], fname, extra) \
         + nav(lang, fname) + body + footer(lang) + SCRIPTS
    return localize(html, lang)


def write(path, text):
    d = os.path.dirname(path)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    io.open(path, 'w', encoding='utf-8', newline='').write(text)


def build_all():
    i18n.check()
    for lang in LANGS:
        for fname, tpl, tkey, dkey, with_close in PAGES:
            html = build_page(lang, fname, tpl, tkey, dkey, with_close)
            path = OUT + DIR[lang] + fname
            write(path, html)
            print('wrote %-34s %6d bytes' % (DIR[lang] + fname, len(html.encode('utf-8'))))


# ---------------------------------------------------------------- sitemap
# Written here rather than by hand so a new page or a new language can never be
# forgotten: the list is what this script and build_archetypes.py actually
# produce. test.html appears once, at the root, because there is only one test.
def write_sitemap(slugs):
    entries = [(SITE + '/test.html', '0.9')]
    for lang in LANGS:
        for fname in i18n.PAGE_FILES:
            pri = '1.0' if (fname == 'index.html' and lang == 'uz') else (
                  '0.8' if fname == 'index.html' else '0.7')
            entries.append((url_for(lang, fname), pri))
        for s in slugs:
            entries.append((url_for(lang, 'obraz-%s.html' % s), '0.6'))
    body = u''.join(u'  <url><loc>%s</loc><priority>%s</priority></url>\n' % e
                    for e in entries)
    xml = (u'<?xml version="1.0" encoding="UTF-8"?>\n'
           u'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + body + u'</urlset>\n')
    write(OUT + 'sitemap.xml', xml)
    write(OUT + 'robots.txt',
          u'User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % SITE)
    print('wrote %-34s %6d bytes (%d urls)'
          % ('sitemap.xml', len(xml.encode('utf-8')), len(entries)))
    print('wrote %-34s' % 'robots.txt')


if __name__ == '__main__':
    build_all()
    # Standalone run: pull the archetype slugs from the shipped characters.js so
    # the sitemap lists the same ten pages build_archetypes.py writes.
    import subprocess
    slugs = json.loads(subprocess.check_output(['node', '-e', '''
const fs=require('fs'),vm=require('vm');const s={};vm.createContext(s);
vm.runInContext(fs.readFileSync(%r,'utf8'),s);
process.stdout.write(JSON.stringify(Object.values(s.ARCHETYPES).map(a=>a.slug)));
''' % (OUT + 'characters.js')]).decode('utf-8'))
    write_sitemap(slugs)
