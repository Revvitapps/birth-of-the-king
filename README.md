# Birth of the King

An in-depth Bible curriculum on the birth of the King: a 102-page teaching flip book (7 x 10 in), printable student pages for each of the five lessons, and a page-turning web version.

## Layout

- `curriculum/book/` : the book itself. `c_front.py`, `c_l1.py` to `c_l5.py` and `c_back.py` hold the text of each section, `build.py` turns them into `book.html`, `style.css` is the design, `imgc/` holds the print-ready images and maps.
- `curriculum/render_book.js` : renders `book.html` to PDF with Playwright. `finish.py` adds bookmarks and writes the printable student packs.
- `curriculum/maps2.py`, `compose.py` : draw the maps (Natural Earth data, downloaded separately, see `NOTE-maps.txt`).
- `curriculum/gen/` : the prompts used for the illustrations.
- `curriculum/flip/` : the page-turning web flip book (`index.html` plus `pages/`).
- `curriculum/history/` : earlier versions of the build script and stylesheet.
- `output/` : the finished PDFs.
- `notes/` : revision checklists.

## Rebuild

```
cd curriculum/book && python3 build.py
cd .. && node render_book.js book book.html book/book_raw.pdf shots
node render_cover.js "$PWD/book"   # letter-size cover
python3 finish.py
```

Do not recompress the PDF by swapping images with pypdf. It blanks the maps and logos. Keep the file small by re-encoding the JPGs in `book/imgc` instead.
