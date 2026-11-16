import json
from pypdf import PdfReader, PdfWriter, Transformation, PageObject
from pypdf.generic import NameObject
B='/tmp/claude-0/-home-user/3a5c4b7d-4602-5541-b0fe-22f390b862a8/scratchpad/book/'
OUT='/mnt/project-files/birth-of-the-king/'
pages=json.load(open(B+'pages.json'))
r=PdfReader(B+'book_raw.pdf')
# page 1 is the letter-size (8.5 x 11 in) full-bleed cover from cover_letter.pdf; the rest stay 7 x 10 in
w=PdfWriter(); w.append(PdfReader(B+'cover_letter.pdf')); w.append(r, pages=(1, len(r.pages)))
w._root_object[NameObject('/PageLayout')]=NameObject('/TwoPageRight')
w.add_metadata({'/Title':'Birth of the King - Teacher Edition','/Author':'Birth of the King Curriculum'})
names={'l1':'Lesson 1 · The Promised King','l2':'Lesson 2 · A King Is Born','l3':'Lesson 3 · Star in the Sky','l4':'Lesson 4 · The Wise Men Worship the King','l5':'Lesson 5 · Escape to Egypt','key':'Teacher Answer Key'}
w.add_outline_item('Cover',0); w.add_outline_item('How to Use This Book',2); w.add_outline_item('Contents',3)
for p in pages:
    if p.get('id') in names: w.add_outline_item(names[p['id']],p['n']-1)
w.write(OUT+'Birth-of-the-King-Flip-Book.pdf')
import shutil; shutil.copy(B+'cover_letter.pdf', OUT+'Front-Cover-8.5x11.pdf')
# printable packs (letter size)
LW,LH=612,792; sc=LH/720.0  # 10in -> 11in
allw=PdfWriter()
for L in range(1,6):
    pw=PdfWriter(); idx=[p['n']-1 for p in pages if p['t'] in('color','work') and p.get('lesson')==L]
    for i in idx:
        src=r.pages[i]
        for target in (pw,allw):
            np_=PageObject.create_blank_page(width=LW,height=LH)
            np_.merge_transformed_page(src, Transformation().scale(sc).translate((LW-504*sc)/2,0))
            target.add_page(np_)
    pw.add_metadata({'/Title':f'Birth of the King - Lesson {L} Student Pages (Printable)'})
    pw.write(OUT+f'Printable-Lesson-{L}-Student-Pages.pdf'); print(L,len(idx))
allw.add_metadata({'/Title':'Birth of the King - All Student Pages (Printable)'})
allw.write(OUT+'Printable-All-Student-Pages.pdf')
