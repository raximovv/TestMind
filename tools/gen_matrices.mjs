// Generates assets/matrix.js: the figural-matrix items for challenge 6.
//
//   node tools/gen_matrices.mjs
//
// This generator lives in TestMind because TestMind owns the item banks: the
// personality, interest and values banks are all authored here and read out of
// here by Naseeb Edu, and the reasoning bank is no different. Naseeb Edu still
// carries its own copy of the OUTPUT from before the challenges moved; when it
// is next regenerated it should be regenerated from this file.
//
// WHY GENERATED RATHER THAN BORROWED. Every off-the-shelf reasoning test this
// product could have used is closed to it. Raven's is Pearson's. ICAR, which
// exists precisely to be the public-domain alternative, is deposited under a
// Scientific Use License: academic use only, no commercial use, which is what a
// school paying for a platform is. CAAS and the VIA Youth Survey failed the
// same way and were dropped from the roster for it.
//
// What IS open is the method. Matzen et al. (2010) published the Sandia
// Generated Matrix Tool under BSD-3-Clause -- a generator, not a fixed pool --
// on the argument that rule-based generation removes the need to keep a small
// item set secret. The rule taxonomy underneath it (constant in a row,
// progression, distribute-three) is Carpenter, Just & Shell (1990), which is
// published science and not anyone's property. So this file implements that
// taxonomy and draws its own items. Nothing is copied; the licence is clear;
// the pool is unlimited, which also means a student who retakes this next year
// does not meet the same twelve puzzles.
//
//   Matzen, L. E., Benz, Z. O., Dixon, K. R., Posey, J., Kroger, J. K., &
//   Speed, A. E. (2010). Recreating Raven's: Software for systematically
//   generating large numbers of Raven-like matrix problems with normed
//   properties. Behavior Research Methods, 42(2), 525-541.
//   Carpenter, P. A., Just, M. A., & Shell, P. (1990). What one intelligence
//   test measures. Psychological Review, 97(3), 404-431.
//
// WHAT THE SCORE MEANS. A number of items correct, and nothing more. It is a
// rank inside the group that has taken it, not an IQ and not an ability
// estimate, because there is no Uzbek sample behind it and inventing norms
// would be worse than having none. The UI must never print a quotient.
//
// Figural on purpose: no words, so nothing has to be translated and no student
// is measured on their Russian.

import fs from 'node:fs'
import path from 'node:path'

const OUT = path.join(process.cwd(), 'assets', 'matrix.js')
const SEED = 20260910          // fixed, so regenerating gives the same test

// A small deterministic PRNG. Math.random would make every regeneration a
// different test, and an item bank that changes under you is not a test.
function mulberry32(seed) {
  return function random() {
    seed |= 0; seed = (seed + 0x6D2B79F5) | 0
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed)
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}

// Three shapes, not four, and no rotation attribute. Both were tried and both
// broke the items: a square rotated 45 degrees IS a diamond to the eye, so a
// row reading circle, square, triangle appeared as circle, diamond, triangle
// and the rule became invisible. An attribute a solver cannot see is not
// difficulty, it is a broken item.
const SHAPES = ['circle', 'square', 'triangle']
const FILLS = ['none', 'half', 'solid']
const COUNTS = [1, 2, 3]

const pick = (rnd, list) => list[Math.floor(rnd() * list.length)]

function shuffled(rnd, list) {
  const out = list.slice()
  for (let i = out.length - 1; i > 0; i--) {
    const j = Math.floor(rnd() * (i + 1))
    ;[out[i], out[j]] = [out[j], out[i]]
  }
  return out
}

// ---------------------------------------------------------------- the rules
//
// Each returns a 3x3 grid of values for one attribute.
//
// constant      the value is fixed along a row and changes between rows
// progression   the value steps by a fixed amount along the row
// distribute3   all three values appear once in every row and every column,
//               which is the rule that makes a matrix feel like a puzzle
//               rather than a pattern

function constantRule(rnd, values) {
  const byRow = shuffled(rnd, values).slice(0, 3)
  return [0, 1, 2].map((row) => [0, 1, 2].map(() => byRow[row % byRow.length]))
}

function progressionRule(rnd, values) {
  const step = rnd() < 0.5 ? 1 : -1
  const starts = shuffled(rnd, [0, 1, 2])
  return [0, 1, 2].map((row) => [0, 1, 2].map((col) => {
    const index = (((starts[row] + step * col) % values.length) + values.length) % values.length
    return values[index]
  }))
}

function distribute3Rule(rnd, values) {
  const order = shuffled(rnd, values)
  // A Latin square: row r, column c takes order[(r + c) mod 3].
  const flip = rnd() < 0.5 ? 1 : 2
  return [0, 1, 2].map((row) => [0, 1, 2].map((col) => order[(row + flip * col) % 3]))
}

const RULES = {
  constant: constantRule,
  progression: progressionRule,
  distribute3: distribute3Rule,
}

// -------------------------------------------------------------- the drawing
//
// One cell, 60x60, drawn as a string. Shapes sit on a row so `count` reads at a
// glance; three small ones are still legible at the size an option chip gets.

function cellSvg(attrs) {
  const { shape, count, fill } = attrs
  const size = count === 1 ? 28 : count === 2 ? 20 : 16
  const gap = count === 1 ? 0 : count === 2 ? 26 : 20
  const start = 30 - (gap * (count - 1)) / 2
  // Half fill is a lighter tone, not hatching. Hatching was tried first and
  // disappeared at three shapes to a cell: the stripes were wider than the
  // shape. A tone reads at every size, which is what an item needs when the
  // count attribute is free to move underneath it.
  const paint = fill === 'none' ? 'none' : 'currentColor'
  const alpha = fill === 'half' ? ' fill-opacity=".38"' : ''
  let out = ''
  for (let i = 0; i < count; i++) {
    const cx = start + gap * i
    const r = size / 2
    if (shape === 'circle') {
      out += `<circle cx="${cx}" cy="30" r="${r}" fill="${paint}"${alpha} stroke="currentColor" stroke-width="2"/>`
    } else if (shape === 'square') {
      out += `<rect x="${cx - r}" y="${30 - r}" width="${size}" height="${size}" fill="${paint}"${alpha} stroke="currentColor" stroke-width="2"/>`
    } else {
      out += `<path d="M${cx} ${30 - r} L${cx + r} ${30 + r} L${cx - r} ${30 + r} Z" fill="${paint}"${alpha} stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>`
    }
  }
  return out
}

const DEFS = ''

function tileSvg(attrs) {
  return `<svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">${cellSvg(attrs)}</svg>`
}

function gridSvg(grid) {
  // 3x3 of 60px cells with 10px gutters, bottom-right left blank.
  let body = DEFS
  for (let row = 0; row < 3; row++) {
    for (let col = 0; col < 3; col++) {
      const x = col * 70, y = row * 70
      if (row === 2 && col === 2) {
        body += `<rect x="${x + 1}" y="${y + 1}" width="58" height="58" rx="6" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="6 5" opacity=".55"/>`
        body += `<text x="${x + 30}" y="${y + 39}" text-anchor="middle" font-size="26" font-weight="700" fill="currentColor" opacity=".55">?</text>`
        continue
      }
      body += `<g transform="translate(${x} ${y})">${cellSvg(grid[row][col])}</g>`
    }
  }
  return `<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" role="img">${body}</svg>`
}

// Two attribute grids are collinear when one is a straight relabelling of the
// other: a consistent value-for-value swap turns A into B in all nine cells.
// The student then only has to read one of them.
function collinear(a, b) {
  const forward = new Map(), backward = new Map()
  for (let row = 0; row < 3; row++) {
    for (let col = 0; col < 3; col++) {
      const from = String(a[row][col]), to = String(b[row][col])
      if (forward.has(from) && forward.get(from) !== to) return false
      if (backward.has(to) && backward.get(to) !== from) return false
      forward.set(from, to)
      backward.set(to, from)
    }
  }
  return true
}

const collinearWithAny = (grid, placed) =>
  Object.values(placed).some((other) => collinear(grid, other))

// --------------------------------------------------------------- the items

const ATTRS = [
  { name: 'shape', values: SHAPES },
  { name: 'count', values: COUNTS },
  { name: 'fill', values: FILLS },
]

function buildItem(rnd, ruleCount, id) {
  // `ruleCount` attributes get a real rule; the rest stay constant. That count
  // is the difficulty knob Carpenter et al. found mattered most.
  const chosen = shuffled(rnd, ATTRS)
  const plan = chosen.map((attr, index) => {
    if (index < ruleCount) {
      const kind = pick(rnd, ['progression', 'distribute3'])
      return { attr, kind }
    }
    return { attr, kind: 'constant' }
  })

  const grids = {}
  const kinds = {}
  for (const { attr, kind } of plan) {
    // Re-roll while this attribute moves in lockstep with one already placed.
    // Two distribute-three rules can land on the same Latin square, and then an
    // item labelled "three rules" is one rule wearing three hats: every cell is
    // predictable from any single attribute, so it solves like the easiest item
    // on the page while sitting at the hard end of the ladder.
    let grid = RULES[kind](rnd, attr.values)
    for (let tries = 0; tries < 40 && collinearWithAny(grid, grids); tries++) {
      grid = RULES[kind](rnd, attr.values)
    }
    grids[attr.name] = grid
    kinds[attr.name] = kind
  }

  const at = (row, col) => ({
    shape: grids.shape[row][col],
    count: grids.count[row][col],
    fill: grids.fill[row][col],
  })

  const grid = [0, 1, 2].map((row) => [0, 1, 2].map((col) => at(row, col)))
  const answer = at(2, 2)

  // Distractors, one per classic family: change exactly one attribute of the
  // right answer, plus one that repeats a neighbouring cell. A distractor that
  // differs in two things at once is one nobody picks.
  const seen = new Set([JSON.stringify(answer)])
  const options = [answer]
  const candidates = []
  for (const attr of ATTRS) {
    for (const value of attr.values) {
      if (answer[attr.name] === value) continue
      candidates.push({ ...answer, [attr.name]: value })
    }
  }
  candidates.push({ ...grid[2][1] }, { ...grid[1][2] }, { ...grid[0][0] })
  for (const candidate of shuffled(rnd, candidates)) {
    if (options.length >= 8) break
    const key = JSON.stringify(candidate)
    if (seen.has(key)) continue
    seen.add(key)
    options.push(candidate)
  }
  while (options.length < 8) {
    const filler = { shape: pick(rnd, SHAPES), count: pick(rnd, COUNTS), fill: pick(rnd, FILLS) }
    const key = JSON.stringify(filler)
    if (seen.has(key)) continue
    seen.add(key)
    options.push(filler)
  }

  const order = shuffled(rnd, options)
  return {
    id,
    rules: Object.fromEntries(Object.entries(kinds).filter(([, kind]) => kind !== 'constant')),
    difficulty: ruleCount,
    grid: gridSvg(grid),
    options: order.map(tileSvg),
    answer: order.findIndex((o) => JSON.stringify(o) === JSON.stringify(answer)),
  }
}

// Twelve items, easiest first: the ramp Raven-like tests use so a student who
// is going to struggle still answers something before it gets hard.
const LADDER = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3]
const rnd = mulberry32(SEED)
const items = LADDER.map((ruleCount, index) =>
  buildItem(rnd, ruleCount, `mx${String(index + 1).padStart(2, '0')}`))

const bad = items.filter((item) => item.answer < 0 || item.options.length !== 8)
if (bad.length) {
  console.error('malformed items: ' + bad.map((i) => i.id).join(', '))
  process.exit(1)
}

const body = `// GENERATED by tools/gen_matrices.mjs -- do not edit by hand.
//
// Figural matrix items for challenge 6. Find the rule that runs along the rows,
// then pick the tile that belongs in the empty corner.
//
// Drawn here rather than borrowed because every ready-made reasoning test is
// closed to a commercial school product -- Raven's is Pearson's, and ICAR, the
// public-domain alternative, is deposited under an academic-use-only licence.
// The generator follows the rule taxonomy in Carpenter, Just & Shell (1990) and
// the generate-don't-hoard argument of Matzen et al. (2010), whose own tool is
// BSD-3-Clause. See scripts/gen_matrices.mjs for the full reasoning.
//
// The score is a count of correct answers. It is a rank inside whoever has
// taken it -- NOT an IQ, and not an ability estimate. There is no Uzbek sample
// behind it, and there will not be one for years.

var MATRIX_ITEMS = ${JSON.stringify(items, null, 2)}

var MATRIX_MAX = MATRIX_ITEMS.length

// Bands, not a number out of twelve, and never a quotient. Three wide buckets
// are all twelve items can honestly support.
function matrixBand(correct) {
  const share = correct / MATRIX_MAX
  if (share >= 0.75) return 'strong'
  if (share >= 0.4) return 'mixed'
  return 'developing'
}
`

fs.writeFileSync(OUT, body, 'utf8')
const spread = items.reduce((acc, i) => { acc[i.difficulty] = (acc[i.difficulty] || 0) + 1; return acc }, {})
console.log(`wrote ${path.relative(process.cwd(), OUT)}  ${items.length} items, rules per item: ${JSON.stringify(spread)}`)
