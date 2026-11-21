"""Helpers shared by the lesson files."""
def _n(x,y,t,g=False):
    return f'<div class="nd{' given' if g else ''}" style="left:{x}in;top:{y}in">{t}</div>'
def _v(x,y1,y2): return f'<div style="position:absolute;left:{x-0.01}in;top:{y1}in;width:0.02in;height:{y2-y1}in;background:#1f2f5c"></div>'
def _h(y,x1,x2): return f'<div style="position:absolute;top:{y-0.01}in;left:{x1}in;width:{x2-x1}in;height:0.02in;background:#1f2f5c"></div>'
_C, _L, _R = 2.95, 1.225, 4.675
_parts = [_n(2.325,0,'Abraham',True), _v(_C,0.42,0.6), _n(2.325,0.6,"Abraham's son"), _v(_C,1.02,1.2), _n(2.325,1.2,"Ruth's husband"),
          _v(_C,1.62,1.8), _n(2.325,1.8,"David's father"), _v(_C,2.22,2.4), _n(2.325,2.4,'King David',True),
          _v(_C,2.82,3.0), _h(3.0,_L,_R), _v(_L,3.0,3.2), _v(_R,3.0,3.2),
          _n(0.6,3.2,"David's son (Matthew)"), _n(4.05,3.2,"David's son (Luke)"), _v(_L,3.62,3.85), _v(_R,3.62,3.85),
          _n(0.6,3.85,'Legal father'), _n(4.05,3.85,'Mother'), _v(_L,4.27,4.45), _v(_R,4.27,4.45), _h(4.45,_L,_R), _v(_C,4.45,4.6),
          _n(2.325,4.6,'Yeshua',True),
          '<div style="position:absolute;left:0.35in;top:2.62in;width:1.75in;font-family:Inter;font-size:7.5pt;color:#c9a24a;font-weight:800;text-align:center">LEGAL RIGHT · MATTHEW 1</div>',
          '<div style="position:absolute;left:3.8in;top:2.62in;width:1.75in;font-family:Inter;font-size:7.5pt;color:#c9a24a;font-weight:800;text-align:center">BLOOD RIGHT · LUKE 3</div>']
TREE = '<div class="tree" style="height:5.1in"><img class="treesk" src="imgc/sk_tree.png">' + ''.join(_parts) + '</div>'

def _hw(kind, words):
    """handwriting guide row as SVG: words = list of (text, style) where style in solid|trace|''"""
    W, H = 566, 92
    if kind == 'heb':
        top, mid, base, fs, fam = 16, 46, 76, 84, 'DejaVu Sans'
    else:
        top, mid, base, fs, fam = 26, 39, 74, 64, 'Inter'
    g = f'<line x1="0" y1="{top}" x2="{W}" y2="{top}" stroke="#9aa0ae" stroke-width="1.3"/>'
    g += f'<line x1="0" y1="{mid}" x2="{W}" y2="{mid}" stroke="#b9bdc8" stroke-width="1.1" stroke-dasharray="6 5"/>'
    g += f'<line x1="0" y1="{base}" x2="{W}" y2="{base}" stroke="#5d6372" stroke-width="1.6"/>'
    xs = [W / 4, 3 * W / 4] if len(words) == 2 else [W / 2]
    for (t, st), x in zip(words, xs):
        if not t: continue
        col = '#1f2f5c' if st == 'solid' else '#c3c8d3'
        extra = ' direction="rtl" unicode-bidi="bidi-override"' if False else ''
        g += f'<text x="{x}" y="{base}" text-anchor="middle" font-family="{fam}" font-size="{fs}" fill="{col}">{t}</text>'
    return f'<svg class="hw" viewBox="0 0 {W} {H}" style="height:{H/96:.2f}in">{g}</svg>'


import random

# ---------- maze: shepherds to Bethlehem ----------
def _maze(cols=11, rows=14, cell=38, seed=11):
    rnd = random.Random(seed)
    walls = {(c, r): {'N', 'S', 'E', 'W'} for c in range(cols) for r in range(rows)}
    seen = {(0, 0)}; stack = [(0, 0)]
    D = {'N': (0, -1, 'S'), 'S': (0, 1, 'N'), 'E': (1, 0, 'W'), 'W': (-1, 0, 'E')}
    while stack:
        c, r = stack[-1]
        nb = [(d, c + dx, r + dy, o) for d, (dx, dy, o) in D.items() if (c + dx, r + dy) in walls and (c + dx, r + dy) not in seen]
        if not nb: stack.pop(); continue
        d, nc, nr, o = rnd.choice(nb)
        walls[(c, r)].discard(d); walls[(nc, nr)].discard(o); seen.add((nc, nr)); stack.append((nc, nr))
    walls[(0, 0)].discard('W'); walls[(cols - 1, rows - 1)].discard('E')
    ox, oy = 150, 10
    seg = []
    for (c, r), w in walls.items():
        x, y = ox + c * cell, oy + r * cell
        if 'N' in w: seg.append(f'M{x} {y}h{cell}')
        if 'W' in w: seg.append(f'M{x} {y}v{cell}')
        if r == rows - 1 and 'S' in w: seg.append(f'M{x} {y+cell}h{cell}')
        if c == cols - 1 and 'E' in w: seg.append(f'M{x+cell} {y}v{cell}')
    W = ox + cols * cell + 122; H = oy * 2 + rows * cell
    g = f'<path d="{" ".join(seg)}" stroke="#1f2f5c" stroke-width="3.2" stroke-linecap="round" fill="none"/>'
    # start: the shepherds
    g += f'<image href="imgc/sk_shepherds.png" x="2" y="{oy-4}" width="142" height="142"/><text x="72" y="{oy+150}" text-anchor="middle" font-family="Inter" font-weight="800" font-size="10" fill="#1f2f5c">START</text>'
    g += ''
    # finish: a wooden sign that says Bethlehem
    ex, ey = ox + cols * cell, oy + (rows - 1) * cell
    sx, sy = ex + 10, ey - 22
    g += f'<path d="M{ex+2} {ey+cell*0.5} h6" stroke="#c9a24a" stroke-width="3" fill="none"/>'
    g += f'<rect x="{sx+47}" y="{sy+30}" width="8" height="62" fill="#d9c08a" stroke="#1f2f5c" stroke-width="2"/>'
    g += f'<path d="M{sx+4} {sy} h88 l12 16 l-12 16 h-88 z" fill="#f4e3b5" stroke="#1f2f5c" stroke-width="2.4" stroke-linejoin="round"/>'
    g += f'<text x="{sx+50}" y="{sy+20.5}" text-anchor="middle" font-family="Inter" font-weight="900" font-size="11.5" fill="#1f2f5c">BETHLEHEM</text>'
    g += f'<text x="{sx+52}" y="{sy-10}" text-anchor="middle" font-size="24" fill="#c9a24a">★</text>'
    g += f'<path d="M{sx+30} {sy+92} q21 -8 42 0" stroke="#1f2f5c" stroke-width="1.6" fill="none"/>'
    return f'<svg viewBox="0 0 {W} {H}" style="width:100%;display:block">{g}</svg>'

CUTS = '<div class="scissors"><b>✂</b> Color, cut on the dashed lines, and glue into the picture</div><div class="cuts">' + ''.join(
    f'<div><img src="imgc/{n}.jpg"></div>' for n in ['cut_mary', 'cut_joseph', 'cut_baby', 'cut_sheep', 'cut_lamb']) + '</div>'

WS = '''<div class="paper"><div class="ear"><div class="box">Price<br>One Lepton</div><div class="box">Today’s Weather<br>Clear skies · Bright star in the east!</div></div>
<div class="mast">The Judea Times</div>
<div class="dateline"><span>Vol. I · No. 1</span><span>Jerusalem, Judea</span><span>Matthew 2:1–8</span></div>
<div class="extra">★ EXTRA! EXTRA! ★</div><div class="head">Wise Men Seek a Newborn King!</div>
<div class="grid"><div class="col"><h5>Strange Star Seen in the East</h5><div class="by">By ______________, Staff Reporter</div>''' + ''.join('<div class="ln"></div>' for _ in range(6)) + '''
<div class="pic"></div><div class="cap">Caption:<div class="ln"></div></div></div>
<div class="col"><h5>King Herod Calls a Secret Meeting</h5><div class="by">By ______________, Palace Reporter</div>''' + ''.join('<div class="ln"></div>' for _ in range(9)) + '''
<div class="side"><b>Interview Corner</b>''' + ''.join('<div class="ln"></div>' for _ in range(2)) + '''</div>
<div class="ad"><b>WANTED</b>Directions to Bethlehem! Ask the chief priests.<br><i>(Micah 5:2)</i></div></div></div></div>'''
import random as _r
def _wordsearch(words, n=13, seed=3):
    rnd = _r.Random(seed); g = [[None]*n for _ in range(n)]; dirs = [(1,0),(0,1),(1,1)]
    for w in sorted(words, key=len, reverse=True):
        for _ in range(500):
            dx, dy = rnd.choice(dirs); x = rnd.randrange(n - (len(w)-1)*dx); y = rnd.randrange(n - (len(w)-1)*dy)
            if all(g[y+i*dy][x+i*dx] in (None, c) for i, c in enumerate(w)):
                for i, c in enumerate(w): g[y+i*dy][x+i*dx] = c
                break
        else: raise ValueError(w)
    A = 'ABCDEFGHIJKLMNOPRSTUWY'
    rows = ''.join('<tr>' + ''.join(f'<td>{c or rnd.choice(A)}</td>' for c in r) + '</tr>' for r in g)
    bank = ' · '.join(words)
    return f'<table class="wsearch">{rows}</table><div class="bank" style="text-align:center"><b>Find these words:</b> {bank}</div>'
WS = _wordsearch(['MAGI', 'STAR', 'HEROD', 'BETHLEHEM', 'PARTHIA', 'CAMEL', 'CARAVAN', 'SCRIBES', 'PROPHET', 'JERUSALEM', 'DANIEL', 'MICAH', 'KING', 'EAST'])


MATCH = '''<div class="match"><div class="mc">
<div class="mi"><b>1</b> Gold</div><div class="mi"><b>2</b> Frankincense</div><div class="mi"><b>3</b> Myrrh</div></div>
<div class="mc"><div class="mi">A sweet-smelling resin burned in worship. It shows Yeshua is the High Priest.</div>
<div class="mi">An ointment used in burial. It points to Yeshua’s death for sin.</div>
<div class="mi">A treasure fit for royalty. It shows Yeshua is the King.</div></div></div>'''
def _code(msg):
    out = []
    for word in msg.split():
        cells = ''.join(f'<div class="cc"><div class="cl"></div><div class="cn">{ord(ch)-64}</div></div>' for ch in word)
        out.append(f'<div class="cw">{cells}</div>')
    return '<div class="code">' + ''.join(out) + '</div>'
KEY = '<table class="ckeytbl"><tr>' + ''.join(f'<td><b>{chr(65+i)}</b><br>{i+1}</td>' for i in range(13)) + '</tr><tr>' + ''.join(f'<td><b>{chr(65+i)}</b><br>{i+1}</td>' for i in range(13, 26)) + '</tr></table>'

SEQ = [('An angel appears to Mary.', ''), ('The Roman emperor orders everyone to register for a census.', ''),
       ('Mary and Joseph travel to Bethlehem.', ''), ('Yeshua is born in Bethlehem.', ''), ('An angel appears to shepherds in the fields.', ''),
       ('Yeshua is presented at the temple (Leviticus 12; Exodus 13).', ''), ('The Wise Men see a star and travel to Jerusalem to meet King Herod.', ''),
       ('The Wise Men bow down and worship Yeshua.', ''), ('The Wise Men return to their country by another way.', ''), ('Joseph and his family escape to Egypt.', '')]
ORDER = [5, 9, 2, 10, 4, 1, 3, 8, 6, 7]  # scrambled display order (indexes into SEQ, 1-based)
SEQ_HTML = ''.join(f'<div class="seq"><div class="bx"></div><b style="font-family:Inter;color:#c9a24a">{chr(65+i)}.</b> {SEQ[k-1][0]}</div>' for i, k in enumerate(ORDER))

