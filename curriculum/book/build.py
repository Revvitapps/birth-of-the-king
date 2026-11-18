#!/usr/bin/env python3
"""Builds the Beyond the Manger flip book HTML from content modules."""
TITLE = "Beyond the Manger"
SUBTITLE = "A Detailed Look into the Story of the Promised King"
import html, re, sys, json, importlib
sys.path.insert(0, '.')

def md(s):
    """tiny inline markup: *italic*, **bold**"""
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\*(.+?)\*', r'<i>\1</i>', s)
    return s

CSS = open('style.css').read()
import os
def src(n):
    return f'imgc/{n}.jpg' if os.path.exists(f'imgc/{n}.jpg') else f'imgc/{n}.png'


def foot(p, label):
    side = 'l' if p['n'] % 2 == 0 else 'r'
    return f'<div class="foot {side}"><span>{md(label)}</span><span class="pg">{p["n"]}</span></div>'

def pg_cover(p):
    return f'''<section class="page cover"><img src="{src(p["img"])}">
<div class="cv-top"><div class="cv-kick">An In-Depth Bible Curriculum</div><h1>Beyond<br>the Manger</h1>
<div class="cv-sub">{SUBTITLE}</div><div class="cv-ref">Matthew 1–2 · Luke 1–2</div>{'<div class="cv-ed">Student Workbook</div>' if p.get("edition") == "Student Workbook" else ""}</div>
<div class="cv-bot">{p.get("edition", "Teacher Edition with Student Activity Pages")}</div></section>'''

def pg_illus(p):
    cap = f'<div class="pill">{md(p["cap"])}</div>' if p.get('cap') else ''
    fit = 'contain' if p.get('contain') else 'cover'
    extra = ' map' if p.get('contain') else ''
    return f'<section class="page art{extra}"><img src="{src(p["img"])}" style="object-fit:{fit}">{cap}<div class="edge"></div></section>'

def pg_opener(p):
    return f'''<section class="page art opener"><img src="{src(p["img"])}">
<div class="op-band"><div class="op-kick">Lesson {p["num"]}</div><div class="op-title">{md(p["title"])}</div>
<div class="op-ref">{md(p["ref"])}</div></div><div class="edge"></div></section>'''

def notes_html(notes, sidefig=None):
    if not notes: return ''
    out = ['<div class="side">']
    if sidefig:
        out.append(f'<figure class="sfig"><img src="{src(sidefig[0])}"><figcaption>{md(sidefig[1])}</figcaption></figure>')
    out.append('<aside class="notes"><div class="tag">Teaching Nuggets</div>')
    for h, t in notes:
        if h: out.append(f'<h3>{md(h)}</h3>')
        for para in t.split('\n'):
            out.append(f'<p>{md(para)}</p>')
    out.append('</aside><div class="mynotes"><div class="tag">Notes</div></div></div>')
    return ''.join(out)

def paras_html(paras):
    out = []; first = True
    for x in paras:
        if x.startswith('## '):
            out.append(f'<h2>{md(x[3:])}</h2>')
        elif x.startswith('> '):
            out.append(f'<blockquote>{md(x[2:])}</blockquote>')
        elif x.startswith('@fig '):
            parts = x[5:].split('|'); im, cap = parts[0], parts[1] if len(parts) > 1 else ''
            h = parts[2] if len(parts) > 2 else '2.2'
            fit = parts[3] if len(parts) > 3 else 'cover'
            out.append(f'<figure class="fig" style="height:{h}in"><img src="{src(im)}" style="object-fit:{fit}">' + (f'<figcaption>{md(cap)}</figcaption>' if cap else '') + '</figure>')
        elif x.startswith('- '):
            out.append(f'<p class="li">{md(x[2:])}</p>')
        else:
            cls = ' class="first"' if first else ''
            out.append(f'<p{cls}>{md(x)}</p>'); first = False
    return ''.join(out)

def band(p, kicker):
    return f'''<div class="band"><div class="kicker">{md(kicker)}</div><h1>{md(p["title"])}</h1>
<div class="num">{p.get("bignum","")}</div><div class="gold"></div></div>'''

def pg_text(p):
    verse = f'<div class="verse">“{md(p["verse"])}” <b>({md(p["vref"])})</b></div>' if p.get('verse') else ''
    read = f'<div class="passages">Read together: {md(p["read"])}</div>' if p.get('read') else ''
    call = ''
    if p.get('callout'):
        t, c = p['callout']
        if isinstance(c, (list, tuple)): c = '<div class="c2">'.join(md(x) + ('</div>' if i else '') for i, x in enumerate(c))
        else: c = md(c)
        call = f'<div class="callout"><b class="t">{md(t)}</b><br>{c}</div>'
    top = ''
    if p.get('top'):
        figs = ''.join(f'<figure style="flex:{t[3] if len(t) > 3 else 1}"><img src="{src(t[0])}" style="object-fit:{t[2] if len(t) > 2 else "cover"}">' + (f'<figcaption>{md(t[1])}</figcaption>' if t[1] else '') + '</figure>' for t in p['top'])
        top = f'<div class="topfig" style="height:{p.get("toph", 2.4)}in">{figs}</div>'
    return f'''<section class="page text">{band(p, p["kicker"])}<div class="body fit">{verse}{read}{top}
<div class="cols"><div class="main">{paras_html(p["paras"])}</div>{notes_html(p.get("notes"), p.get("sidefig"))}</div>{call}</div>
{foot(p, p["foot"])}</section>'''

def pg_plan(p):
    obj = ''.join(f'<li>{md(o)}</li>' for o in p['objectives'])
    flow = ''.join(f'<li><b>{md(a)}</b> {md(b)}</li>' for a, b in p['flow'])
    return f'''<section class="page text plan">{band(p, "Lesson Plan · Lesson " + str(p["num"]))}
<div class="body fit"><div class="planrow"><div class="pl-l">
<div class="pbox"><b class="t">Bible Passages</b><br>{md(p["passages"])}</div>
<div class="pbox"><b class="t">Lesson Goals</b><br>By the end of this lesson, children will be able to:<ol>{obj}</ol></div>
<div class="pbox"><b class="t">Opening Prayer</b><br><i>{md(p["prayer"])}</i></div>
<div class="pbox"><b class="t">Materials</b><br>{md(p["materials"])}</div>
</div><div class="pl-r"><div class="ovw"><b class="t">The Big Picture</b><p>{md(p["overview"])}</p></div>
<div class="callout"><b class="t">Hidden Gem</b><br>{md(p["dyk"])}</div></div></div>
<div class="flow"><b class="t">Lesson Flow</b><ol>{flow}</ol></div></div>
{foot(p, TITLE + " · Lesson " + str(p["num"]))}</section>'''

def lines(n, cls='ln'):
    return ''.join(f'<div class="{cls}"></div>' for _ in range(n))

def block_html(b):
    k = b[0]
    if k == 'q':  # ('q', text, nlines)
        return f'<div class="q"><div class="qt">{md(b[1])}</div>{lines(b[2])}</div>'
    if k == 'qs':  # numbered questions with lines
        out = ['<ol class="qs">']
        for item in b[1]:
            t, n = item if isinstance(item, tuple) else (item, 1)
            out.append(f'<li><div class="qt">{md(t)}</div>{lines(n)}</li>')
        out.append('</ol>'); return ''.join(out)
    if k == 'read':
        return f'<div class="readbox">{"".join("<p>"+md(x)+"</p>" for x in b[1])}</div>'
    if k == 'box':  # ('box', label, height_in[, 'fill'])
        return f'<div class="drawbox {b[3] if len(b) > 3 else ""}" style="height:{b[2]}in"><span>{md(b[1])}</span></div>'
    if k == 'grid4':
        cells = ''.join(f'<div class="cell"><span>{md(x)}</span></div>' for x in b[1])
        return f'<div class="grid4" style="height:{b[2]}in">{cells}</div>'
    if k == 'lines':
        return f'<div class="q">{lines(b[1])}</div>'
    if k == 'bank':
        return '<div class="bank"><b>Word bank:</b> ' + ' · '.join(md(x) for x in b[1]) + '</div>'
    if k == 'html':
        return b[1]
    if k == 'part':
        return f'<div class="part">{md(b[1])}</div>'
    if k == 'mc':  # ('mc', [(question, [options]), ...], start_number)
        start = b[2] if len(b) > 2 else 1
        out = [f'<ol class="qs mcq" start="{start}">']
        for q, opts in b[1]:
            if isinstance(opts, int):
                out.append(f'<li><div class="qt">{md(q)}</div>{lines(opts)}</li>'); continue
            o = ''.join(f'<span class="opt"><i>{chr(65+i)}</i>{md(x)}</span>' for i, x in enumerate(opts))
            out.append(f'<li><div class="qt">{md(q)}</div><div class="opts">{o}</div></li>')
        out.append('</ol>'); return ''.join(out)
    if k == 'img':
        return f'<div class="wsimg" style="height:{b[2]}in"><img src="{src(b[1])}"></div>'
    raise ValueError(k)

def wband(p, kick):
    L = p["lesson"]
    return f'''<img class="wm" src="imgc/fhk_watermark.png"><div class="wband"><div class="wk">{kick} · Lesson {L}</div>
<div class="wname">Name: ____________________</div><div class="wart"><img class="spot" src="imgc/spot_l{L}.png"><img class="logo" src="imgc/fhk_logo.png"></div><h1>{md(p["title"])}</h1></div>'''

SFOOT = TITLE + " · © For His Kingdom"

def pg_work(p):
    ins = f'<div class="ins">{md(p["ins"])}</div>' if p.get('ins') else ''
    if p.get('sk'):
        ins = f'<div class="insrow">{ins}<img class="sk" src="{src(p["sk"])}" style="height:{p.get("skh", 1.2)}in"></div>'
    body = ''.join(block_html(b) for b in p['blocks'])
    if p.get('skbot'):
        body += f'<div class="skbot"><img src="{src(p["skbot"][0])}" style="height:{p["skbot"][1]}in"></div>'
    return f'''<section class="page work {p.get('cls','')}">{wband(p, p.get("kick", "Activity"))}
<div class="wbody fit">{ins}{body}</div>{foot(p, SFOOT)}</section>'''

def pg_color(p):
    q = ''
    if p.get('caption'):
        q = f'<div class="ccap">{md(p["caption"])}</div>'
    return f'''<section class="page work color">{wband(p, p.get("kick", "Color It!"))}
<div class="cimg"><img src="{src(p["img"])}"></div>{q}{foot(p, SFOOT)}</section>'''

def pg_key(p):
    cols = ''.join(f'<div class="kb"><h3>{md(h)}</h3><ol>{"".join("<li>"+md(a)+"</li>" for a in items)}</ol></div>' for h, items in p['sections'])
    return f'''<section class="page text key">{band(p, "Teacher Answer Key")}<div class="body fit keycols">{cols}</div>
{foot(p, TITLE + " · Answer Key")}</section>'''

def pg_frontmatter(p):
    return f'''<section class="page text fm">{band(p, p["kicker"])}<div class="body fit"><div class="main wide">{paras_html(p["paras"])}</div></div>
{foot(p, TITLE)}</section>'''

def pg_toc(p):
    rows = ''.join(f'<div class="toc-l"><span class="tn">{md(a)}</span><span class="tt">{md(b)}</span><span class="tp">{c}</span></div>' if a else f'<div class="toc-s">{md(b)}<span class="tp">{c}</span></div>' for a, b, c in p['rows'])
    return f'''<section class="page text fm">{band(p, "Contents")}<div class="body fit toc">{rows}</div>{foot(p, TITLE)}</section>'''

def pg_back(p):
    return f'''<section class="page back"><div class="bk-in"><div class="bk-star">✦</div>
<p class="bk-v">“For unto us a child is born, unto us a son is given: and the government shall be upon his shoulder: and his name shall be called Wonderful, Counsellor, The mighty God, The everlasting Father, The Prince of Peace.”</p>
<p class="bk-r">Isaiah 9:6</p><p class="bk-t">Beyond the Manger</p><p class="bk-s">A Detailed Look into the Story of the Promised King</p><div class="bk-logo"><img src="imgc/fhk_logo.png"></div></div></section>'''

R = dict(cover=pg_cover, illus=pg_illus, opener=pg_opener, text=pg_text, plan=pg_plan, work=pg_work,
         color=pg_color, key=pg_key, fm=pg_frontmatter, toc=pg_toc, back=pg_back)

def load_pages():
    pages = []
    for mod in ['c_front', 'c_l1', 'c_l2', 'c_l3', 'c_l4', 'c_l5', 'c_back']:
        m = importlib.import_module(mod)
        pages += m.PAGES
    for i, p in enumerate(pages):
        p['n'] = i + 1
    return pages

def build(pages, path, size=('7in', '10in')):
    body = '\n'.join(R[p['t']](p) for p in pages)
    doc = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'
    open(path, 'w').write(doc)

if __name__ == '__main__':
    pages = load_pages()
    # contents page numbers
    for p in pages:
        if p['t'] == 'toc':
            def find(key):
                for q in pages:
                    if q.get('id') == key: return q['n']
                return ''
            p['rows'] = [(a, b, find(c)) for a, b, c in p['rows_src']]
    build(pages, 'book.html')
    build([dict(t='cover', img='cover', edition='Student Workbook', n=1)], 'student_cover.html')
    json.dump([{k: v for k, v in p.items() if k in ('n', 't', 'lesson', 'title', 'id', 'img')} for p in pages], open('pages.json', 'w'), indent=0)
    print(len(pages), 'pages')
