# Birth of the King

An in-depth Bible curriculum on the birth of the King: a 102-page teaching flip book (8.5 x 11 in), printable student pages for each of the five lessons, and a page-turning web version.

## Layout

- `curriculum/book/` : the book itself. `c_front.py`, `c_l1.py` to `c_l5.py` and `c_back.py` hold the text of each section, `build.py` turns them into `book.html`, `style.css` is the design, `imgc/` holds the print-ready images and maps.
- `curriculum/render_book.js` : renders `book.html` to PDF with Playwright. `finish.py` adds bookmarks and writes the printable student packs.
- `curriculum/maps2.py`, `compose.py` : draw the maps (Natural Earth data, downloaded separately, see `NOTE-maps.txt`).
- `curriculum/gen/` : the prompts used for the illustrations.
- `curriculum/flip/` : the page-turning web flip book (`index.html` plus `pages/`).
- `curriculum/history/` : earlier versions of the build script and stylesheet.
- `output/` : the finished PDFs.
- `notes/` : revision checklists.
- `site/` : the interactive teaching site (Next.js PWA) built from the book source. See `site/README.md`.

## Rebuild

```
cd curriculum/book && python3 build.py
cd .. && node render_book.js "$PWD/book" book.html "$PWD/book/book_raw.pdf" "$PWD/shots"
python3 finish.py
```

Every page is US Letter (8.5 x 11 in). Pages are laid out at 7.727 x 10 in and zoomed 1.1 in `style.css`. Do not use CSS text-shadow or blurred box-shadow: PDF viewers show them as dark boxes.

Do not recompress the PDF by swapping images with pypdf. It blanks the maps and logos. Keep the file small by re-encoding the JPGs in `book/imgc` instead.
