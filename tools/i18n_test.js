// Checks the runtime language resolution in strings.js without a browser:
// characters.js + strings.js are loaded into a bare VM with a stub <html lang>,
// which is the only thing tmLang() reads.
//
//   node i18n_test.js
const fs = require('fs'), vm = require('vm'), path = require('path');
const DIR = path.resolve(__dirname, '..') + path.sep;

let pass = 0, fail = 0;
const ok = (name, cond, detail) => {
  if (cond) { pass++; console.log('  ok   ' + name); }
  else { fail++; console.log('  FAIL ' + name + (detail ? '  -> ' + detail : '')); }
};

function ctx(lang) {
  const s = { document: { documentElement: { getAttribute: () => lang } } };
  vm.createContext(s);
  vm.runInContext(fs.readFileSync(DIR + 'assets/characters.js', 'utf8'), s);
  vm.runInContext(fs.readFileSync(DIR + 'assets/strings.js', 'utf8'), s);
  return s;
}

const uz = ctx('uz'), ru = ctx('ru'), en = ctx('en');
const KEYS = Object.keys(uz.ARCHETYPES);
const FAMS = Object.keys(uz.FAMILIES);

console.log('\napproved character assets');
// The set grows one reviewed character at a time, so the test names the approved
// keys rather than counting them: a character that quietly stopped resolving, or
// one that started resolving before it was approved, both have to fail here.
const APPROVED = {
  'E|C': 'assets/characters/gayratli-tashkilotchi.webp',
  'E|A': 'assets/characters/jamoaning-yuragi.webp',
  'ES|C': 'assets/characters/barqaror-strateg.webp',
  'ES|E': 'assets/characters/xotirjam-yetakchi.webp',
  'ES|O': 'assets/characters/xotirjam-kashfiyotchi.webp',
  'E|O': 'assets/characters/gayratli-ijodkor.webp',
  'O|C': 'assets/characters/ijodkor-strateg.webp',
  'ES|A': 'assets/characters/ishonchli-dost.webp',
  'O|A': 'assets/characters/ijodkor-insonparvar.webp',
  'A|C': 'assets/characters/ishonchli-tayanch.webp'
};
// Driven off APPROVED so that redesigning the remaining characters is a
// one-line edit to the map above rather than a new pair of assertions each time.
for (const k of Object.keys(APPROVED))
  ok(uz.ARCHETYPES[k].name + ' uses the approved raster',
     uz.charRasterSrc(k) === APPROVED[k], uz.charRasterSrc(k));
ok('every approved character is on the raster path',
   Object.keys(APPROVED).every(k => !!uz.charRasterSrc(k)));
ok('ru/en runtime paths climb back to the shared asset',
   Object.keys(APPROVED).every(k =>
     ru.charRasterSrc(k) === '../' + APPROVED[k] &&
     en.charRasterSrc(k) === '../' + APPROVED[k]));
ok('every approved file is actually in the repo',
   Object.values(APPROVED).every(p => fs.existsSync(DIR + p)));
ok('unapproved characters remain on the vector renderer',
   KEYS.filter(k => !(k in APPROVED)).every(k => !uz.charRasterSrc(k)));

console.log('\nhero scene');
{
  // site.js calls mountPage() as it loads, so the stub has to absorb that pass.
  const s = { document: { documentElement: { getAttribute: () => 'uz' },
    getElementById: () => null, querySelector: () => null,
    querySelectorAll: () => [], addEventListener: () => {} } };
  s.window = s; s.addEventListener = () => {};
  s.localStorage = { getItem: () => null, setItem: () => {} };
  vm.createContext(s);
  for (const f of ['assets/characters.js', 'assets/strings.js', 'assets/site.js'])
    vm.runInContext(fs.readFileSync(DIR + f, 'utf8'), s);

  const H = 530;                       // the scene viewBox height
  const plaza = s.SCENE_BG_PLAZA * H;  // the floor line, in viewBox units
  const floating = s.SCENE_CAST.filter(c => c[2] < plaza).map(c => c[0] + '@' + c[2]);
  ok('every hero character stands on the plaza, not on the building',
     floating.length === 0, 'above y=' + plaza.toFixed(1) + ': ' + floating.join(', '));

  const svg = s.buildScene();
  ok('the backdrop is drawn once, before the cast',
     (svg.match(/<image[^>]+backgrounds\//g) || []).length === 1);
  ok('the backdrop file is in the repo', fs.existsSync(DIR + s.SCENE_BG), s.SCENE_BG);
  // Covering by height is what crops the sides instead of letterboxing the sky.
  const m = svg.match(/<image[^>]+width="([\d.]+)"[^>]+height="(\d+)"/);
  ok('the backdrop covers the full scene height', m && +m[2] === H);
  ok('the backdrop is not distorted',
     m && Math.abs((+m[1] / +m[2]) - (s.SCENE_BG_W / s.SCENE_BG_H)) < 0.001,
     m && (+m[1] / +m[2]).toFixed(4));
  ok('the characters are still separate layers, not flattened in',
     (svg.match(/<g transform="translate/g) || []).length >= s.SCENE_CAST.length);
}

console.log('\nlanguage resolution');
ok('uz page resolves to uz', uz.tmLang() === 'uz', uz.tmLang());
ok('ru page resolves to ru', ru.tmLang() === 'ru', ru.tmLang());
ok('en page resolves to en', en.tmLang() === 'en', en.tmLang());
ok('unknown lang falls back to uz', ctx('de').tmLang() === 'uz');
ok('missing lang attribute falls back to uz',
   (() => { const s = { document: { documentElement: { getAttribute: () => null } } };
            vm.createContext(s);
            vm.runInContext(fs.readFileSync(DIR + 'assets/characters.js', 'utf8'), s);
            vm.runInContext(fs.readFileSync(DIR + 'assets/strings.js', 'utf8'), s);
            return s.tmLang() === 'uz'; })());

console.log('\nall ten archetypes translated, in every field');
for (const L of [ru, en]) {
  const code = L.tmLang();
  let missing = [];
  for (const k of KEYS) {
    const a = L.tmArch(k), base = uz.ARCHETYPES[k];
    if (a.name === base.name) missing.push(k + '.name');
    if (a.lines[0] === base.lines[0]) missing.push(k + '.lines');
    if (a.strength === base.strength) missing.push(k + '.strength');
    if (a.watch === base.watch) missing.push(k + '.watch');
    if (a.figure.why === base.figure.why) missing.push(k + '.figure.why');
  }
  ok(code + ': no field left as the Uzbek original', missing.length === 0,
     missing.slice(0, 6).join(', '));
  ok(code + ': all 10 archetypes present', KEYS.every(k => L.tmArch(k).name), '');
  ok(code + ': two description lines each',
     KEYS.every(k => L.tmArch(k).lines.length === 2));
  // Dates are not language-dependent and must survive the overlay untouched.
  ok(code + ': figure years kept from the base',
     KEYS.every(k => L.tmArch(k).figure.years === uz.ARCHETYPES[k].figure.years));
  // slug drives the URL — a translated slug would 404.
  ok(code + ': slugs unchanged',
     KEYS.every(k => L.tmArch(k).slug === uz.ARCHETYPES[k].slug));
  ok(code + ': families and their notes translated',
     FAMS.every(f => L.tmFam(f) !== uz.FAMILIES[f].name &&
                     L.tmFamNote(f) !== uz.FAM_NOTES[f]));
  ok(code + ': ui labels translated',
     ['strength', 'watch', 'fig', 'resume'].every(x => L.tmUi(x) !== uz.tmUi(x)));
}

console.log('\nuzbek is untouched by the overlay');
ok('uz tmArch returns the original object',
   KEYS.every(k => uz.tmArch(k).name === uz.ARCHETYPES[k].name));
ok('uz tmFam returns the original name',
   FAMS.every(f => uz.tmFam(f) === uz.FAMILIES[f].name));
ok('uz ui labels are the Uzbek ones', uz.tmUi('resume') === 'Testni davom ettirish');

console.log('\npartial translations degrade to Uzbek, not to blank');
{
  const s = ctx('ru');
  delete s.STRINGS.ru.arch['ES|A'].watch;         // simulate a forgotten field
  const a = s.tmArch('ES|A');
  ok('missing field falls back to the Uzbek text',
     a.watch === uz.ARCHETYPES['ES|A'].watch && a.name !== uz.ARCHETYPES['ES|A'].name);
  delete s.STRINGS.ru.arch['E|C'];                // simulate a forgotten archetype
  ok('missing archetype returns the complete Uzbek card',
     s.tmArch('E|C').name === uz.ARCHETYPES['E|C'].name && !!s.tmArch('E|C').lines);
}

console.log('\ntranslated names are actually in the right script');
ok('ru names are Cyrillic',
   KEYS.every(k => /[А-Яа-яЁё]/.test(ru.tmArch(k).name)));
ok('en names are plain Latin (no Uzbek turned commas)',
   KEYS.every(k => !/[\u02bb\u02bc]/.test(en.tmArch(k).name + en.tmArch(k).lines.join(''))));
ok('ru strength fragments capitalise cleanly for the page heading',
   KEYS.every(k => { const s = ru.tmArch(k).strength;
                     return s[0].toUpperCase() !== s[0] || /^[А-ЯЁ]/.test(s[0].toUpperCase()); }));

console.log('\n' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
