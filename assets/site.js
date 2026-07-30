// TestMind — shared page scripts. Requires characters.js to be loaded first.
// ES5 string concat on purpose: plenty of school phones here still run an old
// Android browser.

var TILE='#2E8FA8', TILE_D='#1F6B80';
var STONE='#E8DCC0', STONE_D='#D5C6A2', STONE_L='#F2E9D5';
var GOLD='#C08A2E', DEEP='#16505F';
var FOOT = 238;   // y of the feet inside a character's own 200x250 viewBox

function inner(k){ return charSvg(k).replace(/^<svg[^>]*>/, '').replace(/<\/svg>$/, ''); }

/* ================= Registan hero scene ================= */

function finial(x, y){
  return '<path d="M'+x+' '+y+' v-14" stroke="'+GOLD+'" stroke-width="3.5" stroke-linecap="round"/>'
       + '<circle cx="'+x+'" cy="'+(y-18)+'" r="4.5" fill="'+GOLD+'"/>';
}

// Ribbed melon dome on a drum; y is the bottom of the drum.
function ribbedDome(x, y, r){
  var dh = r*1.68, drum = r*0.78, i, f;
  var s = '<g transform="translate('+x+','+y+')">'
    + '<rect x="'+(-r*0.66)+'" y="'+(-drum)+'" width="'+(r*1.32)+'" height="'+drum+'" fill="'+STONE+'"/>'
    + '<rect x="'+(-r*0.66)+'" y="'+(-drum)+'" width="'+(r*1.32)+'" height="9" fill="'+STONE_D+'"/>'
    + '<path d="M'+(-r)+' '+(-drum)+' C'+(-r)+' '+(-drum-r*0.85)+' '+(-r*0.44)+' '+(-drum-dh*0.72)
    + ' 0 '+(-drum-dh)+' C'+(r*0.44)+' '+(-drum-dh*0.72)+' '+r+' '+(-drum-r*0.85)+' '+r+' '+(-drum)
    + ' Z" fill="'+TILE+'"/><g stroke="'+TILE_D+'" stroke-width="1.8" fill="none" opacity=".45">';
  for (i = -2; i <= 2; i++){
    if (!i){ s += '<path d="M0 '+(-drum-dh)+' V'+(-drum)+'"/>'; continue; }
    f = i/2.6;
    s += '<path d="M'+(f*r*0.5)+' '+(-drum-dh*0.86)+' C'+(f*r*0.8)+' '+(-drum-dh*0.5)
       + ' '+(f*r)+' '+(-drum-dh*0.24)+' '+(f*r)+' '+(-drum)+'"/>';
  }
  return s + '</g>' + finial(0, -drum-dh) + '</g>';
}

function minaret(x, g, h){
  return '<g transform="translate('+x+','+g+')">'
    + '<path d="M-14 0 L-9.5 '+(-h)+' h19 L14 0 Z" fill="'+STONE+'"/>'
    + '<g fill="'+TILE+'" opacity=".7">'
    + '<rect x="-12.6" y="'+(-h*0.34)+'" width="25" height="10"/>'
    + '<rect x="-11.4" y="'+(-h*0.60)+'" width="23" height="10"/>'
    + '<rect x="-10.4" y="'+(-h*0.84)+'" width="21" height="10"/></g>'
    + '<rect x="-17" y="'+(-h-14)+'" width="34" height="14" rx="3" fill="'+TILE_D+'"/>'
    + '<path d="M-11 '+(-h-14)+' C-11 '+(-h-32)+' 0 '+(-h-39)+' 0 '+(-h-52)
    + ' C0 '+(-h-39)+' 11 '+(-h-32)+' 11 '+(-h-14)+' Z" fill="'+TILE+'"/>'
    + finial(0, -h-52) + '</g>';
}

// Sherdor's sun. The real mosaic is a lion with a human-faced sun rising behind it;
// the lion does not survive being drawn this small, the sun does.
function sherMotif(x, y, sc, flip){
  return '<g transform="translate('+x+','+y+') scale('+(flip?-sc:sc)+','+sc+')">'
    + '<g stroke="'+GOLD+'" stroke-width="2.4" stroke-linecap="round">'
    + '<path d="M0 -17 v-6"/><path d="M12 -12 l4.5 -4.5"/><path d="M17 0 h6"/>'
    + '<path d="M12 12 l4.5 4.5"/><path d="M0 17 v6"/><path d="M-12 12 l-4.5 4.5"/>'
    + '<path d="M-17 0 h-6"/><path d="M-12 -12 l-4.5 -4.5"/></g>'
    + '<circle r="12" fill="'+GOLD+'"/>'
    + '<g fill="#6B4A12"><circle cx="-4" cy="-2" r="1.5"/><circle cx="4" cy="-2" r="1.5"/></g>'
    + '<path d="M-4.5 3.5 q4.5 4 9 0" stroke="#6B4A12" stroke-width="1.6" fill="none" '
    + 'stroke-linecap="round"/></g>';
}

// A madrasa: arcaded wings, a tall central pishtoq, optional domes and minarets.
function madrasa(cx, g, w, h, o){
  o = o || {};
  var pw = w*0.40, wingH = h*0.60, s = '', i, side, nx, nw = 26, gap = 14;
  if (o.domes) for (i = 0; i < o.domes.length; i++)
    s += ribbedDome(cx + o.domes[i][0], g - wingH + 6, o.domes[i][1]);
  s += '<g transform="translate('+cx+','+g+')">'
     + '<rect x="'+(-w/2)+'" y="'+(-wingH)+'" width="'+w+'" height="'+wingH+'" fill="'+STONE+'"/>'
     + '<rect x="'+(-w/2)+'" y="'+(-wingH)+'" width="'+w+'" height="12" fill="'+STONE_D+'"/>';
  for (side = -1; side <= 1; side += 2){
    for (i = 0; i < 3; i++){
      nx = side*(pw/2 + 16 + i*(nw+gap)) - (side < 0 ? nw : 0);
      s += '<path d="M'+nx+' -8 v'+(-wingH*0.44)+' q0 -20 '+(nw/2)+' -20 q'+(nw/2)+' 0 '+(nw/2)
         + ' 20 v'+(wingH*0.44)+' Z" fill="'+DEEP+'" opacity=".82"/>';
    }
  }
  s += '<rect x="'+(-pw/2)+'" y="'+(-h)+'" width="'+pw+'" height="'+h+'" fill="'+STONE_L+'"/>'
     + '<rect x="'+(-pw/2)+'" y="'+(-h)+'" width="'+pw+'" height="14" fill="'+STONE_D+'"/>'
     + '<path d="M'+(-pw*0.32)+' 0 V'+(-h*0.52)+' Q'+(-pw*0.32)+' '+(-h*0.86)+' 0 '+(-h*0.90)
     + ' Q'+(pw*0.32)+' '+(-h*0.86)+' '+(pw*0.32)+' '+(-h*0.52)+' V0 Z" fill="'+TILE_D+'"/>'
     + '<path d="M'+(-pw*0.24)+' 0 V'+(-h*0.52)+' Q'+(-pw*0.24)+' '+(-h*0.80)+' 0 '+(-h*0.84)
     + ' Q'+(pw*0.24)+' '+(-h*0.80)+' '+(pw*0.24)+' '+(-h*0.52)+' V0 Z" fill="'+DEEP+'"/>'
     + '<g fill="'+TILE+'" opacity=".8">';
  for (i = 0; i < 4; i++){
    s += '<rect x="'+(-pw/2+5)+'" y="'+(-h+22+i*20)+'" width="9" height="9"/>'
       + '<rect x="'+(pw/2-14)+'" y="'+(-h+22+i*20)+'" width="9" height="9"/>';
  }
  s += '</g>';
  if (o.sher) s += sherMotif(-pw*0.34, -h*0.76, 1.15, false) + sherMotif(pw*0.34, -h*0.76, 1.15, true);
  s += '</g>';
  if (o.minarets) s += minaret(cx - w/2 - 4, g, o.minarets) + minaret(cx + w/2 + 4, g, o.minarets);
  return s;
}

// The photographed backdrop. One layer, drawn first; the characters stay
// separate <g> elements on top of it so they can still be repositioned, rescaled
// or swapped one at a time.
var SCENE_BG = 'assets/backgrounds/islom-sivilizatsiyasi-markazi.webp';
var SCENE_BG_W = 2172, SCENE_BG_H = 724;

// Where the open plaza starts in the source image, as a fraction of its height.
// Measured off the artwork, not guessed: the drawing this replaces gave the cast
// a quarter of the scene to stand in, the photograph gives about an eighth.
//
// Two ways to buy back the depth were tried and both cost more than they gave --
// zooming in crops the wings and minarets away, and lifting the image to paint
// extra floor underneath leaves a flat band no single colour can blend into,
// because the real plaza has perspective and this one would not. So the cast
// moves instead. It sits deeper in frame than it did, which is simply what this
// photograph's own perspective asks for.
//
// Every character's feet must land below this line or they stand on the steps.
// i18n_test.js checks that against SCENE_CAST so a future reposition cannot
// quietly float someone again.
var SCENE_BG_PLAZA = 0.87;

// Hoisted out of buildScene so the tests can read the positions without having
// to parse the emitted SVG. [key, x, footY, scale] in viewBox units.
// Further away reads as higher and smaller, which is the order of these rows.
// Nobody stands closer than ~515: a figure needs floor BELOW its feet as well as
// under them, or its shadow and reflection fall off the bottom of the frame and
// it goes back to looking pasted on. Learned the hard way at 522.
var SCENE_CAST = [['ES|O',300,468,0.56], ['A|C',906,470,0.58],
                  ['E|A',420,490,0.76],  ['O|C',786,492,0.76],
                  ['ES|E',548,512,0.96], ['E|O',664,515,0.94]];

function buildScene(){
  var W = 1200, H = 530, s = '', i;
  // Cover, not fit: scale by height so the image fills the box top to bottom and
  // the sides overhang. That is what crops the outer minarets on a narrow screen
  // while keeping the dome and the entrance centred, which is the same trade the
  // outer preserveAspectRatio="xMidYMax slice" already makes for the characters.
  var bsc = H / SCENE_BG_H, bw = SCENE_BG_W * bsc, bx = (W - bw) / 2;
  s += '<image href="' + tmAssetPath(SCENE_BG) + '" x="' + bx.toFixed(1) + '" y="0"'
     + ' width="' + bw.toFixed(1) + '" height="' + H + '"'
     + ' preserveAspectRatio="xMidYMid slice"/>';

  // Contact shadow and reflection. Every character used to be vector art with a
  // shadow ellipse drawn into it; the redesigned ones are photographs with no
  // shadow at all, so against a real floor they read as stickers laid on top of
  // the picture rather than people standing on it. Both are drawn here, per
  // figure and scaled with it, so the approved artwork is never touched.
  s += '<defs>'
     // Two ellipses, not one. The wide soft pool is ambient occlusion -- it says
     // "something is standing here". The tight dark one right under the soles is
     // the contact patch, and it is the part that actually makes a figure touch
     // the floor instead of hover a few centimetres above it.
     + '<radialGradient id="tmsh"><stop offset="0" stop-color="#4A3A28" stop-opacity=".30"/>'
     + '<stop offset=".5" stop-color="#4A3A28" stop-opacity=".14"/>'
     + '<stop offset="1" stop-color="#4A3A28" stop-opacity="0"/></radialGradient>'
     + '<radialGradient id="tmsh2"><stop offset="0" stop-color="#3A2C1E" stop-opacity=".50"/>'
     + '<stop offset=".6" stop-color="#3A2C1E" stop-opacity=".22"/>'
     + '<stop offset="1" stop-color="#3A2C1E" stop-opacity="0"/></radialGradient>'
     // Local figure coords: y=238 is the sole, y=150 is roughly the waist. The
     // reflection is strongest at the sole and gone by the waist, which is what
     // a polished floor does -- a full-length mirror image would look like ice.
     + '<linearGradient id="tmrg" gradientUnits="userSpaceOnUse" x1="0" y1="150" x2="0" y2="238">'
     + '<stop offset="0" stop-color="#000"/><stop offset="1" stop-color="#fff"/></linearGradient>'
     + '<mask id="tmrefl"><rect x="0" y="0" width="200" height="250" fill="url(#tmrg)"/></mask>'
     + '</defs>';

  var cast = SCENE_CAST;
  for (i = 0; i < cast.length; i++){
    var c = cast[i], sc = c[3], fig = inner(c[0]);
    // Mirrored about the sole: local (100, FOOT) still lands on (x, footY), but
    // everything above the feet is thrown downward instead of up.
    s += '<g transform="translate('+(c[1]-100*sc)+','+(c[2]+FOOT*sc)+') scale('+sc+','+(-sc)+')">'
       + '<g mask="url(#tmrefl)" opacity=".26">' + fig + '</g></g>';
    s += '<ellipse cx="'+c[1]+'" cy="'+c[2]+'" rx="'+(58*sc).toFixed(1)+'" ry="'+(13*sc).toFixed(1)
       + '" fill="url(#tmsh)"/>'
       + '<ellipse cx="'+c[1]+'" cy="'+(c[2]-1).toFixed(1)+'" rx="'+(27*sc).toFixed(1)+'" ry="'+(6*sc).toFixed(1)
       + '" fill="url(#tmsh2)"/>';
    s += '<g transform="translate('+(c[1]-100*sc)+','+(c[2]-FOOT*sc)+') scale('+sc+')">'+fig+'</g>';
  }
  // slice keeps the characters large on a phone by cropping the sides instead of shrinking
  return '<svg viewBox="0 0 '+W+' '+H+'" preserveAspectRatio="xMidYMax slice" '
       + 'xmlns="http://www.w3.org/2000/svg">'+s+'</svg>';
}

/* ================= small vignettes for the explainer panels ================= */

function vgFrame(body, w, h){
  return '<svg viewBox="0 0 '+w+' '+h+'" xmlns="http://www.w3.org/2000/svg">'
       + '<rect width="'+w+'" height="'+h+'" rx="16" fill="#FFFFFF"/>' + body + '</svg>';
}
function figAt(k, cx, footY, sc){
  return '<g transform="translate('+(cx-100*sc)+','+(footY-FOOT*sc)+') scale('+sc+')">'+inner(k)+'</g>';
}

// 1. A student in front of a result card that carries their own face.
function vgResult(){
  var b = '<ellipse cx="200" cy="252" rx="170" ry="12" fill="#0B2027" opacity=".05"/>'
    + figAt('O|C', 108, 250, 0.82)
    + '<g transform="translate(196,44)">'
    + '<rect width="176" height="196" rx="14" fill="#F1F6F7" stroke="#D7E2E4"/>'
    + '<rect width="176" height="46" rx="14" fill="#6B4FA8"/>'
    + '<rect y="32" width="176" height="14" fill="#6B4FA8"/>'
    + '<text x="88" y="30" text-anchor="middle" font-family="Bitter,Georgia,serif" '
    + 'font-size="17" font-weight="700" fill="#FFFFFF">Ijodkor Strateg</text>'
    + '<g transform="translate(88,60) scale(0.42)">' + inner('O|C') + '</g>'
    + '<g fill="#C6D3D8"><rect x="24" y="164" width="128" height="7" rx="3.5"/>'
    + '<rect x="44" y="180" width="88" height="7" rx="3.5"/></g></g>';
  return vgFrame(b, 400, 272);
}

// 2. Two students, different results, understanding each other.
function vgOthers(){
  var b = '<ellipse cx="200" cy="252" rx="170" ry="12" fill="#0B2027" opacity=".05"/>'
    + figAt('E|A', 112, 250, 0.86) + figAt('ES|A', 292, 250, 0.86)
    + '<g fill="#237A5E" opacity=".55">'
    + '<circle cx="176" cy="70" r="6"/><circle cx="200" cy="60" r="8"/><circle cx="228" cy="70" r="6"/></g>'
    + '<path d="M150 96 q50 -30 104 0" stroke="#237A5E" stroke-width="3" fill="none"'
    + ' stroke-linecap="round" stroke-dasharray="2 9" opacity=".6"/>';
  return vgFrame(b, 400, 272);
}

// 3. A signpost: the same person, several possible directions.
function vgFuture(){
  var b = '<ellipse cx="200" cy="252" rx="170" ry="12" fill="#0B2027" opacity=".05"/>'
    + '<g transform="translate(286,0)">'
    + '<rect x="-5" y="72" width="10" height="178" fill="#A5866040"/>'
    + '<rect x="-5" y="72" width="10" height="178" fill="#9C7C52"/>'
    + '<g font-family="Inter,Segoe UI,sans-serif" font-size="13" font-weight="600" fill="#FFFFFF">'
    + '<path d="M-78 84 h140 l16 15 -16 15 h-140 z" fill="#0F6E8C"/>'
    + '<text x="-68" y="104">Kasb</text>'
    + '<path d="M-92 126 h154 l16 15 -16 15 h-154 z" fill="#C08A2E"/>'
    + '<text x="-82" y="146">Yoʻnalish</text>'
    + '<path d="M-70 168 h132 l16 15 -16 15 h-132 z" fill="#237A5E"/>'
    + '<text x="-60" y="188">Fan</text></g></g>'
    + figAt('ES|E', 120, 250, 0.86);
  return vgFrame(b, 400, 272);
}

/* ================= character gallery ================= */

var FAM_ORDER = ['lead','crea','care','base'];
// FAM_NOTES moved to characters.js: the page generators read it from there, and
// two copies of the same four lines had no way of staying in step.

// full=true adds the first description line (used on the Obrazlar page).
function buildGallery(full){
  var byFam = {}, html = '', i, j, k, f, fam, keys, a;
  for (k in ARCHETYPES){ a = ARCHETYPES[k]; (byFam[a.fam] = byFam[a.fam] || []).push(k); }
  for (i = 0; i < FAM_ORDER.length; i++){
    f = FAM_ORDER[i]; fam = FAMILIES[f]; keys = byFam[f] || [];
    // heading levels stay in order: page h1 -> family h2 -> card h3
    html += '<div class="fam" style="--famc:'+fam.c+';--famsoft:'+fam.soft+';--famdark:'+fam.dark+';--famlit:'+fam.lit+'">'
          + '<div class="famhead"><h2 class="famname">'+tmFam(f)+'</h2>'
          + '<span class="famnote">'+tmFamNote(f)+'</span></div><div class="cards">';
    for (j = 0; j < keys.length; j++){
      a = tmArch(keys[j]);
      html += '<a class="ccard" href="obraz-'+a.slug+'.html">'
            + '<div class="cart">'+charSvg(keys[j], a.name)+'</div>'
            + '<div class="cbody"><h3 class="cname">'+a.name+'</h3>'
            + (full ? '<p class="cline">'+a.lines[0]+'</p>' : '')
            + '<p class="cstr">'+tmUi('strength')+a.strength+'</p>'
            + (full ? '<p class="cwatch">'+tmUi('watch')+a.watch+'</p>' : '')
            + '<p class="cfig">'+tmUi('fig')+'<b>'+a.figure.who+'</b> · '+a.figure.years+'</p>'
            + '</div></a>';
    }
    html += '</div></div>';
  }
  return html;
}

// Full-bleed colour band per family, characters in a row - the layout used by
// 16personalities.com/personality-types. Each character links to its own page.
function buildBands(){
  var byFam = {}, html = '', i, j, k, f, fam, keys, a;
  for (k in ARCHETYPES){ a = ARCHETYPES[k]; (byFam[a.fam] = byFam[a.fam] || []).push(k); }
  for (i = 0; i < FAM_ORDER.length; i++){
    f = FAM_ORDER[i]; fam = FAMILIES[f]; keys = byFam[f] || [];
    html += '<section class="famband" style="--famc:'+fam.c+';--famsoft:'+fam.soft+';--famdark:'+fam.dark+';--famlit:'+fam.lit+'">'
          + '<div class="wrap"><h2 class="famtitle">'+tmFam(f)+'</h2>'
          + '<p class="famsub">'+tmFamNote(f)+'</p><div class="famrow">';
    for (j = 0; j < keys.length; j++){
      a = tmArch(keys[j]);
      html += '<a class="ftype" href="obraz-'+a.slug+'.html">'
            + '<span class="ftart">'+charSvg(keys[j], a.name)+'</span>'
            + '<span class="ftname">'+a.name+'</span>'
            + '<span class="ftdesc">'+a.lines[0]+'</span>'
            + '<span class="ftfig">'+a.figure.who+'</span></a>';
    }
    html += '</div></div></section>';
  }
  return html;
}

/* ================= shared behaviour ================= */

// If an unfinished test is saved on this device, say so on every start button.
function markResumeCtas(){
  try {
    var d = JSON.parse(localStorage.getItem('testmind_draft_v1'));
    if (!d || !d.answers) return;
    var done = 0, i;
    for (i = 0; i < d.answers.length; i++) if (d.answers[i] > 0) done++;
    if (!done) return;
    var els = document.querySelectorAll('[data-cta]');
    for (i = 0; i < els.length; i++) els[i].textContent = tmUi('resume');
  } catch (e) {}
}


function mountPage(){
  var scene = document.getElementById('scene');
  if (scene) scene.innerHTML = buildScene();
  var bandBox = document.getElementById('bands');
  if (bandBox) bandBox.innerHTML = buildBands();
  var gal = document.getElementById('gallery');
  if (gal) gal.innerHTML = buildGallery(gal.getAttribute('data-full') === '1');
  var v;
  if ((v = document.getElementById('vg-result'))) v.innerHTML = vgResult();
  if ((v = document.getElementById('vg-others'))) v.innerHTML = vgOthers();
  if ((v = document.getElementById('vg-future'))) v.innerHTML = vgFuture();
  markResumeCtas();
}
// This file is loaded at the bottom of <body>, so the DOM is already parsed — but
// guard anyway, so nothing silently fails to render if the tag is ever moved to
// <head> or given defer/async.
if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mountPage);
else mountPage();

// Parent-letter page: the button prints only the letter (print CSS hides the rest).
var _pl = document.getElementById('printLetter');
if (_pl) _pl.onclick = function(){ window.print(); };
