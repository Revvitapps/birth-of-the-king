# Birth of the King: interactive site

The teaching site for *Birth of the King*, the five-lesson Bible curriculum on the birth of Yeshua. Every reading from the book, paired with its painting, read aloud on any phone, with Teaching Nuggets for the teacher and the coloring pages and activities right after the reading they belong to. Kids color by tapping, answer quizzes and draw on screen, or print the page. It installs as an app (PWA) and keeps working offline once a lesson has been opened. It also sells the book: a centre "Get the Book" tab and a free Lesson 1 sample that collects emails.

## Run

```
cd site
npm install
npm run dev        # http://localhost:3000 (also on your LAN for phones)
```

`npm run dev` and `npm run build` first copy the book's art from `../curriculum` into `public/`. After editing the book text (`curriculum/book/c_*.py`), run `npm run export:book` to refresh `data/book.json`.

## Environment (all optional)

| Variable | What it does |
| --- | --- |
| `NEXT_PUBLIC_SITE_URL` | Base URL for metadata and the sitemap |
| `SITE_INDEXING` | `on` lets search engines index the site. Unset = noindex (prototype) |
| `ACCESS_CODE` | When set, Lessons 2 to 5 ask for this code once per device. Lesson 1 stays free |
| `NEXT_PUBLIC_BUY_URL` | Store link for every "Get the Book" button |
| `PIPELINE_WEBHOOK_URL` | Sign-ups (free sample) are forwarded here as JSON |

## Brand

| Token | Value | Source |
| --- | --- | --- |
| Navy | `#1f2f5c` | book `style.css` `--navy` |
| Navy 2 | `#2b3f78` | book `--navy2` |
| Gold | `#c9a24a` | book `--gold` (fills, rules, text on navy) |
| Gold deep | `#82621c` | added for gold text on cream (5.3:1) |
| Gold soft | `#efe2bf` | book `--goldsoft` |
| Cream | `#fbf8f1` | book `--cream` |
| Ink | `#22242a` | book `--ink` |
| Headings | Inter 800/900, uppercase | book headings |
| Body | Caladea | book body |
| Art | `curriculum/book/imgc/*` | the book's own paintings, line art, maps and sketches |
| Logo | `fhk_logo.png` | For His Kingdom |
| Icons | `public/pwa/*` | `scripts/make-icons.mjs` (star over a crown, book colours) |

## Screens

| Route | What it is |
| --- | --- |
| `/` | Cover art, "What do you need?" with six answers, the five lessons, free Lesson 1 sample |
| `/lessons` | The five lessons with progress |
| `/lessons/[n]` | Lesson plan: overview (read aloud), Did You Know, video slot, steps in book order, passages, objectives, prayer, materials, answer key |
| `/lessons/[n]/[step]` | A reading (painting + text + Teaching Nuggets + notes), a tap-to-fill coloring page, or an activity (answers, multiple choice, drawing pads, printed page) with prev/next |
| `/activities` | Every coloring page and activity, by lesson |
| `/book` | Get the Book: formats, what's inside, free sample |
| `/more` | How to Use This Book, A Note on Names and Sources, settings |

Teacher / Kids switch: Teacher mode shows Teaching Nuggets, notes, prayers and answer keys. Kids mode hides them.

## Real vs stubbed

- Real: all lesson text, art, Teaching Nuggets, activities and answer keys (exported from the book source), read aloud (device voice), coloring, drawing, answers and progress saved on the device, offline support, install prompt, sign-up API and webhook forwarding, access-code unlock.
- Stubbed: prices, store link, contact email and lesson videos show `[PLACEHOLDER]`. Mazes, word searches, the family tree, handwriting rows and cut-and-paste pages show the printed page instead of an on-screen version.

## Verified

2026-11-18 at 390 × 844 and 1440 × 900 (headless Chromium): typecheck, lint and build clean; 77 routes return 200; axe WCAG A/AA 0 violations on 9 main routes; no horizontal overflow; offline fallback works; Lighthouse mobile (local `next start`, warm) Performance 90, Accessibility 100.

## Launch

1. Vercel: import `Revvitapps/birth-of-the-king`, Root Directory `site`, keep "Include files outside the root directory" on (the build copies art from `../curriculum`).
2. Set the env vars above. Leave `SITE_INDEXING` unset until launch.
3. Prototype domain `birth-of-the-king.revvit.io`: add it in Vercel, then a Cloudflare `CNAME birth-of-the-king -> cname.vercel-dns.com`, DNS only (grey cloud). Ask Matthew first.
4. At launch: real domain, `SITE_INDEXING=on`, redeploy, submit `/sitemap.xml` in Search Console.
