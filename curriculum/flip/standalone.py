"""Build the downloadable flip book page from index.html: a complete HTML document
with no web fonts, so it opens straight from a folder with no internet.
usage: python3 standalone.py OUT_DIR   (writes OUT_DIR/index.html)"""
import os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(here, 'index.html'), encoding='utf-8').read()
s = re.sub(r'<link rel="preconnect"[^>]*>\n', '', s)
s = re.sub(r'<link rel="stylesheet" href="https://fonts[^>]*>\n', '', s)
s = re.sub(r'<meta name="claude:[^>]*>\n', '', s)
assert 'http' not in s.replace('http-equiv', ''), 'external reference left in page'
title, rest = s.split('\n', 1)
head, body = rest.split('</style>\n', 1)
out = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
       + title + '\n' + head + '</style>\n</head>\n<body>\n' + body + '\n</body>\n</html>\n')
os.makedirs(sys.argv[1], exist_ok=True)
open(os.path.join(sys.argv[1], 'index.html'), 'w', encoding='utf-8').write(out)
