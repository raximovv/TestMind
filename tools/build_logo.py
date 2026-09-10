# -*- coding: utf-8 -*-
u"""Cuts every logo asset the site uses out of one source render.

`logo-source.png` is the artwork as it was delivered: the navy bird sitting on
a photographic sky. Nothing on the site can use it in that state, so this
script lifts the mark off its background and emits the four things the pages
actually reference. Run it again if the artwork is ever replaced.

    python build_logo.py

    assets/ui/logo.png              the mark, transparent, for the nav
    assets/ui/icon.png              32px tab icon
    assets/ui/apple-touch-icon.png  180px home-screen icon
    favicon.ico                     16/32/48, for the automatic /favicon.ico hit

How the cut-out works. The mark is one flat ink colour and the sky behind it is
a smooth gradient, so the honest way to separate them is a matte rather than a
threshold: estimate what the sky WOULD have been under every pixel, then read
each pixel's darkness as coverage. A threshold throws the anti-aliased edge
away and leaves the bird with a staircase outline at every size.

Two passes, because the ink colour has to be measured from the mark's interior
rather than from its darkest pixel. Guessing too dark leaves the whole body at
about 0.87 alpha, and the logo then prints grey instead of navy.

The two icons are NOT the bare mark. A thin navy bird on transparency is a
smudge at 16px, which is the size that actually matters in a browser tab, so
the icons invert it: paper mark on a solid navy tile, which holds its shape all
the way down.
"""
import io
import os
import statistics
import sys

from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(HERE, 'logo-source.png')
UI = os.path.join(ROOT, 'assets', 'ui')

# Where the mark sits in the delivered render, plus enough sky around it for the
# background model to read from. Measured once; if the artwork is replaced this
# is the line to change.
BOX = (756, 325, 915, 577)
PAD = 30

FLOOR = 0.035          # below this a pixel is sky, not a soft edge
SOLID = 0.92           # above this a pixel is body, not a soft edge
PAPER = (250, 246, 238)

lum = lambda c: 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def cut_out():
    u"""Return (mark as RGBA, ink colour)."""
    im = Image.open(SRC).convert('RGB')
    crop = im.crop((BOX[0] - PAD, BOX[1] - PAD, BOX[2] + PAD + 1, BOX[3] + PAD + 1))
    cw, ch = crop.size
    px = crop.load()

    def corner(cx, cy):
        s = [px[cx + dx, cy + dy] for dx in range(8) for dy in range(8)]
        return tuple(statistics.fmean(c[i] for c in s) for i in range(3))

    tl, tr = corner(0, 0), corner(cw - 8, 0)
    bl, br = corner(0, ch - 8), corner(cw - 8, ch - 8)

    def sky(x, y):
        fx, fy = x / (cw - 1), y / (ch - 1)
        return [(tl[i] * (1 - fx) + tr[i] * fx) * (1 - fy)
                + (bl[i] * (1 - fx) + br[i] * fx) * fy for i in range(3)]

    def matte(ink):
        ink_l = lum(ink)
        a = [[0.0] * cw for _ in range(ch)]
        for y in range(ch):
            for x in range(cw):
                bg_l = lum(sky(x, y))
                v = (bg_l - lum(px[x, y])) / (bg_l - ink_l)
                a[y][x] = 0.0 if v < FLOOR else (1.0 if v > SOLID else v)
        return a

    rough = matte((0, 0, 0))          # only to find which pixels are interior
    inside = [px[x, y] for y in range(ch) for x in range(cw) if rough[y][x] > 0.90]
    ink = tuple(int(round(statistics.median(c[i] for c in inside))) for i in range(3))

    alpha = matte(ink)
    out = Image.new('RGBA', (cw, ch))
    op = out.load()
    for y in range(ch):
        for x in range(cw):
            op[x, y] = (ink[0], ink[1], ink[2], int(round(alpha[y][x] * 255)))
    return out.crop(out.getbbox()), ink


def recolour(mark, rgb):
    u"""Same shape, different ink. Alpha is what carries the drawing."""
    out = Image.new('RGBA', mark.size)
    op, mp = out.load(), mark.load()
    for y in range(mark.size[1]):
        for x in range(mark.size[0]):
            op[x, y] = (rgb[0], rgb[1], rgb[2], mp[x, y][3])
    return out


def tile(mark, ink, size, radius, fill):
    u"""The mark in paper on a navy tile, centred, at `size` square."""
    scale = size * 0.68 / mark.size[1]
    w, h = max(1, round(mark.size[0] * scale)), max(1, round(mark.size[1] * scale))
    small = recolour(mark, PAPER).resize((w, h), Image.LANCZOS)
    out = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    if radius:
        ImageDraw.Draw(out).rounded_rectangle(
            (0, 0, size - 1, size - 1), radius=radius, fill=fill + (255,))
    else:
        ImageDraw.Draw(out).rectangle((0, 0, size - 1, size - 1), fill=fill + (255,))
    out.paste(small, ((size - w) // 2, (size - h) // 2), small)
    return out


def main():
    if not os.path.isfile(SRC):
        sys.exit('missing %s' % SRC)
    if not os.path.isdir(UI):
        os.makedirs(UI)
    mark, ink = cut_out()

    mark.save(os.path.join(UI, 'logo.png'))
    tile(mark, ink, 32, 7, ink).save(os.path.join(UI, 'icon.png'))
    # iOS masks the corners itself and paints black behind any transparency, so
    # this one is a full square.
    tile(mark, ink, 180, 0, ink).save(os.path.join(UI, 'apple-touch-icon.png'))
    tile(mark, ink, 48, 10, ink).save(
        os.path.join(ROOT, 'favicon.ico'), sizes=[(16, 16), (32, 32), (48, 48)])

    print('ink            #%02X%02X%02X' % ink)
    for p in ('assets/ui/logo.png', 'assets/ui/icon.png',
              'assets/ui/apple-touch-icon.png', 'favicon.ico'):
        full = os.path.join(ROOT, p.replace('/', os.sep))
        print('%-30s %5d bytes' % (p, os.path.getsize(full)))


if __name__ == '__main__':
    main()
