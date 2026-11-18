#!/usr/bin/env python3
"""Export the Beyond the Manger book source (curriculum/book/c_*.py) into
site/data/book.json. Images are copied by scripts/sync-assets.mjs.

The book stays the single source of truth: edit the c_*.py files, rebuild the
book as usual, then run `npm run export:book` here.

Run with `python3 -I` so nothing in the book folder can shadow stdlib modules.
"""
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
REPO = os.path.dirname(SITE)
BOOK = os.path.join(REPO, 'curriculum', 'book')
FLIP = os.path.join(REPO, 'curriculum', 'flip', 'pages')
OUT = os.path.join(REPO, 'output')

MODULES = ['c_front', 'c_l1', 'c_l2', 'c_l3', 'c_l4', 'c_l5', 'c_l6', 'c_l7', 'c_back']


# The lesson files share helpers in c_common.py. Appended, so nothing there can shadow the stdlib.
sys.path.append(BOOK)


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(BOOK, name + '.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.PAGES


def slugify(s):
    s = s.lower().replace('’', '').replace("'", '')
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s


def img_name(n):
    for ext in ('jpg', 'png'):
        if os.path.exists(os.path.join(BOOK, 'imgc', f'{n}.{ext}')):
            return f'{n}.{ext}'
    raise FileNotFoundError(n)


def block(b):
    k = b[0]
    if k == 'q':
        return {'k': 'q', 'text': b[1], 'lines': b[2]}
    if k == 'qs':
        items = []
        for it in b[1]:
            t, n = it if isinstance(it, (list, tuple)) else (it, 1)
            items.append({'text': t, 'lines': n})
        return {'k': 'qs', 'items': items}
    if k == 'mc':
        qs = []
        for q, opts in b[1]:
            if isinstance(opts, int):
                qs.append({'text': q, 'lines': opts})
            else:
                qs.append({'text': q, 'options': list(opts)})
        return {'k': 'mc', 'start': b[2] if len(b) > 2 else 1, 'items': qs}
    if k == 'read':
        return {'k': 'read', 'paras': list(b[1])}
    if k == 'box':
        return {'k': 'box', 'label': b[1]}
    if k == 'grid4':
        return {'k': 'grid4', 'cells': list(b[1])}
    if k == 'lines':
        return {'k': 'lines', 'lines': b[1]}
    if k == 'bank':
        return {'k': 'bank', 'words': list(b[1])}
    if k == 'part':
        return {'k': 'part', 'text': b[1]}
    if k == 'img':
        return {'k': 'img', 'img': img_name(b[1])}
    if k == 'html':
        h = b[1]
        tag = lambda t: [re.sub(r'<[^>]+>', '', x).strip() for x in re.findall(t, h, re.S)]
        if 'class="wsearch"' in h:
            grid = [re.findall(r'<td>(.)</td>', row) for row in re.findall(r'<tr>(.*?)</tr>', h, re.S)]
            words = re.search(r'Find these words:</b>(.*?)</div>', h, re.S).group(1)
            return {'k': 'wordsearch', 'grid': grid, 'words': [w.strip() for w in re.sub(r'<[^>]+>', '', words).split('·') if w.strip()]}
        if h.startswith('<svg viewBox="0 0 690'):
            return {'k': 'maze', 'svg': h}
        if 'class="match"' in h:
            cols = re.findall(r'<div class="mc">(.*?)</div>\s*(?=<div class="mc">|</div>$)', h, re.S)
            mis = re.findall(r'<div class="mi">(.*?)</div>', h, re.S)
            left = [re.sub(r'<[^>]+>', '', re.sub(r'<b>\d+</b>\s*', '', x)).strip() for x in mis if x.startswith('<b>')]
            right = [x.strip() for x in mis if not x.startswith('<b>')]
            return {'k': 'match', 'left': left, 'right': right}
        if 'class="seqrow"' in h:
            items = [{'letter': a, 'text': t.strip()} for a, t in re.findall(r'<b[^>]*>([A-Z])\.</b>(.*?)</div>', h, re.S)]
            return {'k': 'order', 'items': items}
        if 'class="tbl"' in h and 'class="blank"' in h:
            return {'k': 'fill', 'rows': re.findall(r'<tr><td>(.*?)</td><td class="blank">', h)}
        if 'class="tree"' in h:
            return {'k': 'tree'}
        if 'class="hw"' in h:
            texts = re.findall(r'<text[^>]*fill="#1f2f5c">(.*?)</text>', h)
            lead = tag(r'<div class="qt"[^>]*>(.*?)</div>')
            return {'k': 'trace', 'text': texts[0], 'rtl': bool(re.search(r'[\u0590-\u05ff]', texts[0])), 'rows': len(re.findall(r'class="hw"', h)), 'lead': lead[0] if lead else ''}
        if 'class="letters"' in h:
            return {'k': 'letters', 'items': [{'char': c, 'name': n} for c, n in re.findall(r'<div class="hl">(.*?)</div><div class="nm">(.*?)</div>', h)]}
        strip = lambda x: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', x)).strip()
        if h.startswith('<ol class="qs">'):
            return {'k': 'qs', 'items': [{'text': strip(''.join(re.findall(r'<div class="qt"[^>]*>(.*?)</div>', li, re.S))),
                                          'lines': max(1, li.count('class="ln"'))} for li in re.findall(r'<li>(.*?)</li>', h, re.S)]}
        if 'class="seq"' in h:
            lead = tag(r'<div class="qt"[^>]*>(.*?)</div>')
            names = [strip(x) for x in re.findall(r'<div class="bx"></div>(.*?)</div>', h, re.S)]
            return {'k': 'order', 'lead': lead[0] if lead else '', 'items': [{'letter': chr(65 + i), 'text': t} for i, t in enumerate(names)]}
        if 'class="readbox"' in h:
            return {'k': 'read', 'paras': [re.sub(r'</?b>', '**', x).strip() for x in re.findall(r'<p>(.*?)</p>', h, re.S)]}
        if 'class="drawbox"' in h and 'class="qt"' in h:
            return {'k': 'q', 'text': tag(r'<div class="qt"[^>]*>(.*?)</div>')[0], 'lines': h.count('class="ln"'), 'draw': strip(re.search(r'<span>(.*?)</span>', h).group(1))}
        if h.startswith('<div class="q"><div class="qt">'):
            return {'k': 'q', 'text': re.sub(r'_{3,}', '____', tag(r'<div class="qt"[^>]*>(.*?)</div>')[0]), 'lines': max(1, h.count('class="ln"'))}
        if 'Map link:' in h:
            return {'k': 'read', 'paras': [re.sub(r'</?b>', '**', re.sub(r'<div[^>]*>|</div>|☐ ', '', h)).strip()]}
        # Hand-laid print layouts (cut-outs, labelled maps). The site shows the printed page for these.
        return {'k': 'printed'}
    raise ValueError(k)


def _words(t):
    return set(w for w in re.findall(r"[a-z]{3,}|\d+", t.lower()))


def attach_answers(lessons, keys):
    """Turns the printed answer key into machine-checkable answers where the key is unambiguous."""
    norm = lambda t: re.sub(r'[^a-z]', '', t.lower())
    for l in lessons:
        for st in l['steps']:
            if st['kind'] != 'activity':
                continue
            key = next((k for k in keys if k['lesson'] == l['num'] and norm(k['title']) == norm(st['title'])), None)
            if not key:
                continue
            ans = key['answers']
            letters = [a for a in ans if re.match(r'^[A-E]\. ', a)]
            li = 0
            for b in st['blocks']:
                if b['k'] == 'mc':
                    for it in b['items']:
                        if it.get('options') and li < len(letters):
                            it['answer'] = ord(letters[li][0]) - 65
                            li += 1
                if b['k'] == 'match':
                    flat = ' · '.join(ans)
                    parts = re.split(r' · |\n', flat)
                    out = []
                    for i, left in enumerate(b['left']):
                        cand = [x for x in parts if re.match(rf'^(Matching: )?{i+1} ', x)] or [x for x in parts if norm(x).startswith(norm(left))]
                        line = cand[0] if cand else ans[i] if i < len(ans) else ''
                        line = line.split(': ', 1)[-1]
                        scores = [len(_words(line) & _words(r)) for r in b['right']]
                        out.append(max(range(len(scores)), key=lambda j: scores[j]))
                    if len(set(out)) == len(out):
                        b['answer'] = out
                if b['k'] == 'order':
                    m = dict(re.findall(r'\b([A-Z]) (\d+)', ans[0]))
                    if len(m) == len(b['items']):
                        b['answer'] = [int(m[it['letter']]) for it in b['items']]
                    else:
                        # stops named in the key in order: "Damascus 3, Jerusalem 4"
                        named = re.findall(r'([^,]+?) (\d+)(?:,|$)', ans[0])
                        out = []
                        for it in b['items']:
                            best = max(named, key=lambda x: len(_words(x[0]) & _words(it['text'])), default=None)
                            out.append(int(best[1]) if best and _words(best[0]) & _words(it['text']) else 0)
                        if sorted(out) == list(range(1, len(out) + 1)):
                            b['answer'] = out
                if b['k'] == 'fill':
                    bank = next((x['words'] for x in st['blocks'] if x['k'] == 'bank'), [])
                    want = [a.lower() for a in ans[:len(b['rows'])]]
                    if ans and ans[0].startswith('Table: '):
                        want = [a.strip().lower() for a in ans[0][7:].split(',')]
                    if all(w in [x.lower() for x in bank] for w in want):
                        b['answer'] = want
                        b['bank'] = bank
                if b['k'] == 'tree':
                    t = ' '.join(ans)
                    slots = [('Abraham’s son', r'Abraham’s son: (\w+)'), ('Ruth’s husband', r'Ruth’s husband: (\w+)'), ('David’s father', r'David’s father: (\w+)'),
                             ('David’s son (Matthew)', r'Matthew: (\w+)'), ('David’s son (Luke)', r'Luke: (\w+)'),
                             ('Legal father', r'→ (\w+) \(legal father\)'), ('Mother', r'→ (\w+) \(mother\)')]
                    b['slots'] = [{'label': lab, 'answer': re.search(rx, t).group(1)} for lab, rx in slots]
                    b['bank'] = next((x['words'] for x in st['blocks'] if x['k'] == 'bank'), [])
            # a tree or fill page carries its own word bank, so the plain bank chip row is dropped
            if any(b['k'] in ('tree', 'fill') and b.get('bank') for b in st['blocks']):
                st['blocks'] = [b for b in st['blocks'] if b['k'] != 'bank']
            st['printed'] = any(b['k'] == 'printed' for b in st['blocks'])


def main():
    pages = []
    for m in MODULES:
        pages += load(m)
    for i, p in enumerate(pages):
        p['n'] = i + 1

    front, lessons, keys, used_imgs = [], [], [], set()
    cur = None
    pending_art = None
    slugs = set()

    def uniq(s):
        base, i = s, 2
        while s in slugs:
            s = f'{base}-{i}'; i += 1
        slugs.add(s)
        return s

    def use(n):
        name = img_name(n); used_imgs.add(name); return name

    for p in pages:
        t = p['t']
        if t == 'opener':
            slugs.clear()
            cur = {'num': p['num'], 'title': p['title'], 'ref': p['ref'], 'cover': use(p['img']),
                   'page': p['n'], 'steps': []}
            lessons.append(cur)
            continue
        if t == 'plan':
            cur['plan'] = {k: p[k] for k in ('passages', 'objectives', 'prayer', 'materials', 'overview', 'dyk')}
            cur['plan']['flow'] = [list(x) for x in p['flow']]
            cur['plan']['page'] = p['n']
            continue
        if t == 'illus':
            pending_art = {'img': use(p['img']), 'cap': p.get('cap', ''), 'contain': bool(p.get('contain')), 'page': p['n']}
            continue
        if t in ('fm', 'toc'):
            if t == 'fm':
                front.append({'title': p['title'], 'kicker': p['kicker'], 'paras': p['paras'], 'slug': slugify(p['title'])})
            continue
        if t == 'key':
            for h, items in p['sections']:
                mm = re.match(r'L(\d)\s*·\s*(.+)', h)
                keys.append({'lesson': int(mm.group(1)), 'title': mm.group(2), 'answers': list(items)})
            continue
        if t in ('cover', 'back'):
            if t == 'cover':
                use(p['img'])
            continue
        if cur is None:
            continue
        if t == 'text':
            step = {'kind': 'reading', 'slug': uniq(slugify(p['title'])), 'title': p['title'], 'kicker': p['kicker'],
                    'page': p['n'], 'paras': p['paras']}
            for k in ('verse', 'vref', 'read'):
                if p.get(k): step[k] = p[k]
            if p.get('notes'):
                step['notes'] = [{'h': h, 't': tx} for h, tx in p['notes']]
            if p.get('callout'):
                ct, cc = p['callout']
                step['callout'] = {'title': ct, 'body': list(cc) if isinstance(cc, (list, tuple)) else [cc]}
            figs = []
            if p.get('top'):
                figs += [{'img': use(x[0]), 'cap': x[1]} for x in p['top']]
            if p.get('sidefig'):
                figs.append({'img': use(p['sidefig'][0]), 'cap': p['sidefig'][1]})
            if figs: step['figs'] = figs
            if pending_art:
                step['art'] = pending_art
            else:
                # "continued" spreads reuse the previous art in the book; keep the first figure as the hero.
                if figs: step['art'] = {'img': figs[0]['img'], 'cap': figs[0]['cap'], 'contain': figs[0]['img'].startswith('map_'), 'page': p['n']}
            pending_art = None
            cur['steps'].append(step)
            continue
        if t == 'color':
            cur['steps'].append({'kind': 'color', 'slug': uniq(slugify(p['title']) + '-coloring'), 'title': p['title'],
                                 'kick': p.get('kick', 'Color It!'), 'img': use(p['img']), 'caption': p.get('caption', ''),
                                 'page': p['n']})
            continue
        if t == 'work':
            blocks = [block(b) for b in p['blocks']]
            for b in blocks:
                if b['k'] == 'img': used_imgs.add(b['img'])
            st = {'kind': 'activity', 'slug': uniq(slugify(p['title']) + '-activity'), 'title': p['title'],
                  'kick': p.get('kick', 'Activity'), 'ins': p.get('ins', ''), 'page': p['n'], 'blocks': blocks,
                  'printed': any(b['k'] == 'printed' for b in blocks)}
            if p.get('sk'): st['sketch'] = use(p['sk'])
            cur['steps'].append(st)
            continue
        raise ValueError(t)

    # the escape-route map sits in the back matter; it is the answer map for Lesson 7
    attach_answers(lessons, keys)
    data = {'front': front, 'lessons': lessons, 'keys': keys, 'pageCount': len(pages)}
    os.makedirs(os.path.join(SITE, 'data'), exist_ok=True)
    with open(os.path.join(SITE, 'data', 'book.json'), 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)

    n_steps = sum(len(l['steps']) for l in lessons)
    print(f'{len(pages)} book pages -> {len(lessons)} lessons, {n_steps} steps, {len(keys)} answer keys')


if __name__ == '__main__':
    sys.exit(main())
