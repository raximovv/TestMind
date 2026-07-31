# -*- coding: utf-8 -*-
u"""Builds the link-preview card (og.png) that Telegram, WhatsApp and Twitter show.

    python build_og.py          # -> build/og.html
    node   make_og.js           # -> ../og.png

og.png used to be a hand-drawn file with no source. It went stale twice over
without anyone noticing, because nothing renders it and nothing checks it: by the
time the founder spotted it in a Telegram preview it was showing character art
that had been replaced ten times over AND the site's old teal palette, months
after the site itself had gone bronze. A preview card is the first thing anyone
sees of the site and the last thing anyone thinks to look at, so it is generated
from the same strings, fonts and artwork as everything else now.

Self-contained on purpose -- fonts and artwork inlined as base64 -- so it renders
identically from file:// with no network.
"""
import base64, io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE) + '/'
OUT = os.path.join(HERE, 'build')

sys.path.insert(0, HERE)
from i18n import S

# Four of the ten, chosen for colour spread rather than importance: at the size a
# chat app shows this, the row reads as a band of colour before it reads as people.
FIGURES = ['xotirjam-yetakchi',     # teal
           'gayratli-ijodkor',      # red and white ikat
           'barqaror-strateg',      # deep red
           'ishonchli-tayanch']     # green


def b64(path, mime):
    with open(ROOT + path, 'rb') as f:
        return 'data:%s;base64,%s' % (mime, base64.b64encode(f.read()).decode('ascii'))


def build(lang='uz'):
    t = S[lang]
    figs = u''.join(
        u'<img src="%s" alt="">' % b64('assets/characters/%s.webp' % s, 'image/webp')
        for s in FIGURES)
    html = u"""<!doctype html><html lang="uz"><head><meta charset="utf-8"><style>
@font-face{font-family:'Bitter';src:url(%(bitter)s) format('woff2');font-weight:700;font-display:block}
@font-face{font-family:'Inter';src:url(%(inter)s) format('woff2');font-weight:400 600;font-display:block}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1200px;height:630px;background:#F4F0E8;font-family:'Inter',sans-serif;
     color:#2B2620;overflow:hidden;position:relative}
.bar{height:12px;background:#8A6A3F}
.wrap{display:flex;height:618px;align-items:center}
.txt{padding:0 0 0 72px;width:596px;flex:none}
.mark{font-family:'Bitter',serif;font-weight:700;font-size:34px;color:#6B5230;
      letter-spacing:-.01em;margin-bottom:34px}
h1{font-family:'Bitter',serif;font-weight:700;font-size:66px;line-height:1.06;
   letter-spacing:-.02em;margin-bottom:26px}
.sub{font-size:25px;color:#6E6558;margin-bottom:14px}
.sub2{font-size:22px;color:#6E6558;margin-bottom:38px}
.btn{display:inline-block;background:#8A6A3F;color:#fff;font-size:24px;font-weight:600;
     padding:17px 34px;border-radius:12px}
/* The figures are photographs with no shadow of their own, exactly as in the
   hero -- without the ellipse under them they float against a flat panel. */
/* Negative gap on purpose: each PNG is a 1024x1536 canvas with the figure
   filling only the middle 60-80%% of it, so laying them edge to edge leaves
   gaps of transparency that read as bad spacing rather than as a group. */
.cast{flex:1;display:flex;align-items:flex-end;justify-content:center;gap:-42px;
      height:100%%;padding-bottom:92px;position:relative}
.cast img{height:250px;width:auto;display:block;position:relative;z-index:1;
          margin-left:-21px;margin-right:-21px}
.cast img:nth-child(3){height:268px}
.cast img:nth-child(4){height:256px}
.ground{position:absolute;left:50%%;transform:translateX(-50%%);bottom:84px;
        width:470px;height:30px;border-radius:50%%;z-index:0;
        background:radial-gradient(closest-side,rgba(74,58,40,.22),rgba(74,58,40,0))}
</style></head><body>
<div class="bar"></div>
<div class="wrap">
  <div class="txt">
    <div class="mark">TestMind</div>
    <h1>%(h1)s</h1>
    <div class="sub">%(sub)s</div>
    <div class="sub2">%(sub2)s</div>
    <span class="btn">%(cta)s</span>
  </div>
  <div class="cast"><div class="ground"></div>%(figs)s</div>
</div>
</body></html>""" % {
        'bitter': b64('assets/fonts/bitter.woff2', 'font/woff2'),
        'inter': b64('assets/fonts/inter.woff2', 'font/woff2'),
        'h1': t['home.h1'],
        'sub': u'50 ta savol · 7 daqiqa · bepul va anonim',
        'sub2': u'Oʻzbek tilidagi shaxsiyat testi',
        'cta': t['nav.cta'],
        'figs': figs,
    }
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    p = os.path.join(OUT, 'og.html')
    io.open(p, 'w', encoding='utf-8', newline='').write(html)
    print('wrote %s  (%d KB)' % (p, os.path.getsize(p) / 1024))


if __name__ == '__main__':
    build()
