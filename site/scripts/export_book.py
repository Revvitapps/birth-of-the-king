#!/usr/bin/env python3
"""Export the Birth of the King book source (curriculum/book/c_*.py) into
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

MODULES = ['c_front', 'c_l1', 'c_l2', 'c_l3', 'c_l4', 'c_l5', 'c_back']


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
        # Hand-laid print layouts (mazes, trees, word searches, handwriting rows).
        # The site shows the printed page for these.
        return {'k': 'printed'}
    raise ValueError(k)


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
                if figs: step['art'] = {'img': figs[0]['img'], 'cap': figs[0]['cap'], 'contain': False, 'page': p['n']}
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

    # the escape-route map sits in the back matter; it is the answer map for Lesson 5
    data = {'front': front, 'lessons': lessons, 'keys': keys, 'pageCount': len(pages)}
    os.makedirs(os.path.join(SITE, 'data'), exist_ok=True)
    with open(os.path.join(SITE, 'data', 'book.json'), 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)

    n_steps = sum(len(l['steps']) for l in lessons)
    print(f'{len(pages)} book pages -> {len(lessons)} lessons, {n_steps} steps, {len(keys)} answer keys')


if __name__ == '__main__':
    sys.exit(main())
