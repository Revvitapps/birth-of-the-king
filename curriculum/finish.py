"""Builds the finished PDFs from the rendered book. Usage: python3 finish.py <raw book pdf> <student cover pdf> <out dir>"""
import json, sys, os
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject
RAW, SCOVER, OUT = sys.argv[1], sys.argv[2], sys.argv[3].rstrip('/') + '/'
T = 'Beyond the Manger'
pages = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'book', 'pages.json')))
r = PdfReader(RAW); sc = PdfReader(SCOVER)
w = PdfWriter(clone_from=r)
w._root_object[NameObject('/PageLayout')] = NameObject('/TwoPageRight')
w.add_metadata({'/Title': T + ': A Detailed Look into the Story of the Promised King - Teacher Edition', '/Author': 'For His Kingdom'})
w.add_outline_item('Cover', 0); w.add_outline_item('How to Use This Book', 2); w.add_outline_item('Contents', 3)
L = 0
for p in pages:
    if p['t'] == 'opener':
        L += 1; w.add_outline_item(f"Lesson {L} · {p['title']}", p['n'] - 1)
    if p.get('id') == 'key': w.add_outline_item('Teacher Answer Key', p['n'] - 1)
LESSONS = L
w.write(OUT + 'Beyond-the-Manger-Flip-Book.pdf')
cw = PdfWriter(); cw.add_page(r.pages[0]); cw.write(OUT + 'Front-Cover-8.5x11.pdf')
cw = PdfWriter(); cw.add_page(sc.pages[0]); cw.write(OUT + 'Student-Workbook-Cover-8.5x11.pdf')
allw = PdfWriter(); allw.add_page(sc.pages[0])
for L in range(1, LESSONS + 1):
    pw = PdfWriter(); idx = [p['n'] - 1 for p in pages if p['t'] in ('color', 'work') and p.get('lesson') == L]
    for i in idx:
        pw.add_page(r.pages[i]); allw.add_page(r.pages[i])
    pw.add_metadata({'/Title': f'{T} - Lesson {L} Student Pages (Printable)'})
    pw.write(OUT + f'Printable-Lesson-{L}-Student-Pages.pdf'); print(L, len(idx))
allw.add_metadata({'/Title': T + ' - Student Workbook'})
allw.write(OUT + 'Beyond-the-Manger-Student-Workbook.pdf')
