// The colour measurements, shared by tools/darkmode.js and tools/darkstates.js.
//
// WHY PARITY AND NOT A THRESHOLD
// ------------------------------
// Asking "is this 4.5:1" answers a different question from "is dark mode as good
// as light mode". The light theme has shipped for months and its choices are
// deliberate: a hairline divider at 1.4:1 is a hairline on purpose. Judging dark
// against an absolute floor therefore floods the report with things that are the
// same in both themes and were never a complaint.
//
// So this measures the SAME element twice, once per theme, and reports where the
// dark one is materially worse. That is the actual defect: a border that was
// faint-but-there at 1.4:1 and is now 1.02:1, or ink that was 7:1 and is now 3:1.
// Absolute failures are still reported, because 2:1 is unreadable whatever the
// light theme does.
'use strict';

// ---------------------------------------------------------------- colour --
function channel(v) {
  v /= 255;
  return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
}
function luminance(c) {
  return 0.2126 * channel(c[0]) + 0.7152 * channel(c[1]) + 0.0722 * channel(c[2]);
}
function parse(s) {
  const m = String(s || '').match(/[\d.]+/g);
  if (!m || m.length < 3) return null;
  return { r: +m[0], g: +m[1], b: +m[2], a: m.length > 3 ? +m[3] : 1 };
}
// A translucent layer over an opaque one. --line and the overlays are written
// as rgba, so almost nothing in the dark theme is its literal value.
function flatten(top, bottom) {
  if (!top) return bottom;
  if (top.a >= 1) return [top.r, top.g, top.b];
  if (!bottom) return null;
  return [
    Math.round(top.r * top.a + bottom[0] * (1 - top.a)),
    Math.round(top.g * top.a + bottom[1] * (1 - top.a)),
    Math.round(top.b * top.a + bottom[2] * (1 - top.a)),
  ];
}
// WCAG's ratio is luminance only, which is the right measure for ink on a ground
// and the WRONG one for two surfaces that differ mostly in hue -- a dark green
// family band on a navy page reads instantly and scores 1.05:1. So surfaces are
// judged by perceptual distance instead. OKLab, scaled x100: about 3 is a
// subtle-but-real tonal step, which is what these bands are.
function oklab(c) {
  const [r, g, b] = c.map(channel);
  const l = Math.cbrt(0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b);
  const m = Math.cbrt(0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b);
  const s = Math.cbrt(0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b);
  return [
    0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s,
    1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s,
    0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s,
  ];
}
function deltaE(a, b) {
  if (!a || !b) return null;
  const p = oklab(a), q = oklab(b);
  return Math.hypot(p[0] - q[0], p[1] - q[1], p[2] - q[2]) * 100;
}

function ratio(a, b) {
  if (!a || !b) return null;
  const [x, y] = [luminance(a), luminance(b)].sort((p, q) => q - p);
  return (x + 0.05) / (y + 0.05);
}

// ------------------------------------------------- the in-page collector --
// Returns raw colours only. Every sum is done in node, where it can be read.
const COLLECT = function () {
  // A key that survives a theme change: the DOM is identical, only the paint
  // differs, so position in the tree identifies the same element in both runs.
  function keyOf(el) {
    const parts = [];
    let node = el;
    while (node && node !== document.body && parts.length < 9) {
      const parent = node.parentElement;
      let n = 1;
      if (parent) {
        const kin = [...parent.children].filter((k) => k.tagName === node.tagName);
        n = kin.indexOf(node) + 1;
      }
      const cls = (node.className && typeof node.className === 'string')
        ? '.' + node.className.trim().split(/\s+/)[0] : '';
      parts.unshift(node.tagName.toLowerCase() + cls + (n > 1 ? ':' + n : ''));
      node = parent;
    }
    return parts.join('>');
  }

  // What is painted behind this element, ignoring its own background. Walks up
  // compositing anything translucent until something opaque stops it.
  function groundBehind(el) {
    const stack = [];
    let node = el.parentElement;
    while (node) {
      const cs = getComputedStyle(node);
      if (cs.backgroundImage !== 'none') return { image: true, rgb: null };
      const m = String(cs.backgroundColor).match(/[\d.]+/g);
      if (m && m.length >= 3) {
        const a = m.length > 3 ? +m[3] : 1;
        if (a > 0) { stack.push(cs.backgroundColor); if (a >= 1) break; }
      }
      if (node === document.documentElement) break;
      node = node.parentElement;
    }
    return { image: false, stack: stack.reverse() };
  }

  // The section this element belongs to, so the report reads by section rather
  // than as one long list. Nearest landmark, else the nearest heading above it.
  function sectionOf(el) {
    const box = el.closest('header,footer,nav,section,article,aside,dialog,[role="dialog"],.rsum,.rpanel,.chlist,.authdialog,.fcwrap,#app');
    if (!box) return 'page';
    const h = box.querySelector('h1,h2,h3,.famname,.rsumhead h2');
    const label = (h && h.textContent.trim().slice(0, 32))
      || box.getAttribute('aria-label')
      || (box.className && String(box.className).split(/\s+/)[0])
      || box.tagName.toLowerCase();
    return label;
  }

  const out = [];
  document.querySelectorAll('body *').forEach((el) => {
    const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.display === 'none') return;
    if (+cs.opacity === 0) return;
    const r = el.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) return;
    // Visually-hidden text is not looked at.
    if (r.width <= 2 && r.height <= 2) return;
    if (el.closest('.vh')) return;

    const ownText = [...el.childNodes].some((k) => k.nodeType === 3 && k.textContent.trim());
    const bw = Math.max(
      parseFloat(cs.borderTopWidth) || 0, parseFloat(cs.borderBottomWidth) || 0,
      parseFloat(cs.borderLeftWidth) || 0, parseFloat(cs.borderRightWidth) || 0);
    const g = groundBehind(el);

    out.push({
      key: keyOf(el),
      section: sectionOf(el),
      tag: el.tagName.toLowerCase(),
      cls: (typeof el.className === 'string' ? el.className : '').trim().split(/\s+/)[0] || '',
      text: ownText ? el.textContent.trim().replace(/\s+/g, ' ').slice(0, 30) : '',
      color: ownText ? cs.color : null,
      bg: cs.backgroundColor,
      bgImage: cs.backgroundImage !== 'none',
      border: bw > 0 ? cs.borderTopColor : null,
      borderW: bw,
      ground: g.image ? null : g.stack,
      overImage: g.image,
      fs: parseFloat(cs.fontSize),
      bold: +cs.fontWeight >= 700,
      // Is this something a reader operates? Those have their own rule.
      control: !!el.closest('button,a,input,select,textarea,[role="menuitem"],[tabindex]')
               || ['button', 'input', 'select', 'textarea', 'a'].indexOf(el.tagName.toLowerCase()) >= 0,
    });
  });
  return out;
};

// ------------------------------------------------------------- node side --
// Resolve one element's measurements into numbers.
function resolve(row) {
  if (row.overImage || !row.ground) return null;   // painted over a picture
  let ground = [255, 255, 255];
  for (const layer of row.ground) {
    const c = parse(layer);
    if (!c) continue;
    ground = flatten(c, ground) || ground;
  }
  const own = parse(row.bg);
  const surface = (own && own.a > 0) ? flatten(own, ground) : ground;
  const out = { ground, surface };
  if (row.color) {
    const ink = parse(row.color);
    if (ink && ink.a >= 0.95) out.text = ratio([ink.r, ink.g, ink.b], surface);
  }
  if (row.border && row.borderW > 0) {
    const b = parse(row.border);
    if (b && b.a > 0) out.border = ratio(flatten(b, surface), surface);
  }
  // A filled shape on its ground: how findable the element is at all. Measured
  // as perceptual distance, not luminance ratio -- see deltaE above.
  if (own && own.a > 0) {
    out.fill = deltaE(surface, ground);
    // A control still has to clear WCAG 1.4.11 on luminance alone, because that
    // is what the standard asks of something you operate.
    out.fillRatio = ratio(surface, ground);
  }
  return out;
}

function needed(row) {
  // WCAG's large-text relaxation, as the text walk already used.
  return (row.fs >= 24 || (row.fs >= 18.66 && row.bold)) ? 3 : 4.5;
}

module.exports = { COLLECT, resolve, needed, ratio, deltaE, parse, flatten, luminance };
