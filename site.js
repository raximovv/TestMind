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

function buildScene(){
  var W = 1200, H = 530, GY = 390, s = '', i;
  s += '<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
     + '<stop offset="0" stop-color="#CFE7F0"/><stop offset="1" stop-color="#F1F6F7"/></linearGradient>'
     + '<linearGradient id="grnd" x1="0" y1="0" x2="0" y2="1">'
     + '<stop offset="0" stop-color="#EDF2EF"/><stop offset="1" stop-color="#E0EBE6"/></linearGradient></defs>'
     + '<rect width="'+W+'" height="'+H+'" fill="url(#sky)"/>'
     + '<path d="M0 '+GY+' L140 268 L262 336 L360 254 L510 '+GY+' Z" fill="#B4D2DF" opacity=".55"/>'
     + '<path d="M700 '+GY+' L840 262 L960 330 L1070 248 L1200 340 L1200 '+GY+' Z" fill="#B4D2DF" opacity=".55"/>';
  s += madrasa(196, GY, 300, 238, {minarets:250});
  s += madrasa(600, GY, 344, 222, {domes:[[0,68]], minarets:180});
  s += madrasa(1004, GY, 300, 238, {domes:[[-88,32],[88,32]], minarets:250, sher:true});
  s += '<path d="M0 '+GY+' H'+W+' V'+H+' H0 Z" fill="url(#grnd)"/>'
     + '<path d="M0 '+(GY+26)+' H'+W+'" stroke="#CFE2DB" stroke-width="3"/>';
  var cast = [['ES|O',300,418,0.56], ['A|C',906,420,0.58],
              ['E|A',420,462,0.76],  ['O|C',786,464,0.76],
              ['ES|E',548,514,0.96], ['E|O',664,518,0.94]];
  for (i = 0; i < cast.length; i++){
    var c = cast[i], sc = c[3];
    s += '<g transform="translate('+(c[1]-100*sc)+','+(c[2]-FOOT*sc)+') scale('+sc+')">'+inner(c[0])+'</g>';
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
var FAM_NOTES = {
  lead:'Odamlarni ortidan ergashtiradiganlar',
  crea:'Yangi gʻoya va yechim topadiganlar',
  care:'Atrofdagilarni koʻradigan va qoʻllab-quvvatlaydiganlar',
  base:'Vaʼdasida turadigan, ishonchli odamlar'
};

// full=true adds the first description line (used on the Obrazlar page).
function buildGallery(full){
  var byFam = {}, html = '', i, j, k, f, fam, keys, a;
  for (k in ARCHETYPES){ a = ARCHETYPES[k]; (byFam[a.fam] = byFam[a.fam] || []).push(k); }
  for (i = 0; i < FAM_ORDER.length; i++){
    f = FAM_ORDER[i]; fam = FAMILIES[f]; keys = byFam[f] || [];
    // heading levels stay in order: page h1 -> family h2 -> card h3
    html += '<div class="fam" style="--famc:'+fam.c+';--famsoft:'+fam.soft+'">'
          + '<div class="famhead"><h2 class="famname">'+fam.name+'</h2>'
          + '<span class="famnote">'+FAM_NOTES[f]+'</span></div><div class="cards">';
    for (j = 0; j < keys.length; j++){
      a = ARCHETYPES[keys[j]];
      html += '<a class="ccard" href="obraz-'+a.slug+'.html">'
            + '<div class="cart">'+charSvg(keys[j], a.name)+'</div>'
            + '<div class="cbody"><h3 class="cname">'+a.name+'</h3>'
            + (full ? '<p class="cline">'+a.lines[0]+'</p>' : '')
            + '<p class="cstr">Kuchli tomoni: '+a.strength+'</p>'
            + (full ? '<p class="cwatch">Eʼtibor bering: '+a.watch+'</p>' : '')
            + '<p class="cfig">Tarixdan: <b>'+a.figure.who+'</b> · '+a.figure.years+'</p>'
            + '</div></a>';
    }
    html += '</div></div>';
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
    for (i = 0; i < els.length; i++) els[i].textContent = 'Testni davom ettirish';
  } catch (e) {}
}

function mountPage(){
  var scene = document.getElementById('scene');
  if (scene) scene.innerHTML = buildScene();
  var gal = document.getElementById('gallery');
  if (gal) gal.innerHTML = buildGallery(gal.getAttribute('data-full') === '1');
  var v;
  if ((v = document.getElementById('vg-result'))) v.innerHTML = vgResult();
  if ((v = document.getElementById('vg-others'))) v.innerHTML = vgOthers();
  if ((v = document.getElementById('vg-future'))) v.innerHTML = vgFuture();
  markResumeCtas();
}
mountPage();
