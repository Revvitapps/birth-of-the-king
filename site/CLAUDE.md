@AGENTS.md

# Birth of the King: interactive teaching site

## 0. Status and decisions (living, update first)

- 2026-11-18: First working version built on branch `claude/project-thread-3xe8zs` (draft PR). Next.js 16 PWA in `site/`, following the Revvit PWA plan.
- The printed book is the single source of truth. `scripts/export_book.py` turns `curriculum/book/c_*.py` into `data/book.json`; `scripts/sync-assets.mjs` copies the art and printed page images into `public/` before dev and build (they are gitignored here).
- Brand comes from the book's own stylesheet (navy #1f2f5c, gold #c9a24a, cream #fbf8f1, Inter + Caladea). Gold text on light grounds uses `--gold-deep` #82621c for contrast.
- 2026-11-18, decided by Matthew: Lesson 1 free, Lessons 2 to 5 for buyers only. Set `ACCESS_CODE` in Vercel (never in git) on every deployment people can reach; buyers get the code with their purchase receipt.
- Access: Lesson 1 is always free. Lessons 2 to 5 lock only when `ACCESS_CODE` is set (buyers get the code on their receipt). Unset means everything is open (prototype).
- Only the Lesson 1 student pack is published as a download. The other paid PDFs are never copied into `public/`.
- Prototype stays noindexed until `SITE_INDEXING=on`.
- Author's standing book rules also apply to any new site copy: no first person (I/me/we/us/our) in lessons or worksheets.

### Open questions for Matthew
1. Prices for each format and the store link (`NEXT_PUBLIC_BUY_URL`).
2. Contact email for the site.
3. Videos: who records them, and where they are hosted (YouTube/Vimeo embed or mp4 on Vercel Blob/R2). Add them in `data/media.ts`.
4. Domain: `birth-of-the-king.revvit.io` for the prototype, then a real domain at launch?

## 1. Brief

A fully immersive teaching version of the Birth of the King curriculum: the lessons in book order, each reading paired with its painting, Teaching Nuggets for the teacher, and the student activities flowing right after the reading they belong to, done on screen or printed. It also supports selling the book and PDF for Christmas 2026.

## 2. Commands

```
npm run dev            # syncs assets, then next dev on 0.0.0.0
npm run export:book    # rebuild data/book.json after editing the book source
npm run icons          # rebuild public/pwa icons and OG image
npm run build && npm start
npm run typecheck && npm run lint
BASE=http://localhost:3000 npm run check:routes   # every sitemap route + PWA files
BASE=http://localhost:3000 npm run check:a11y     # axe WCAG A/AA on main routes
BASE=http://localhost:3000 npm run check:shots    # phone + desktop screenshots, overflow check
```
