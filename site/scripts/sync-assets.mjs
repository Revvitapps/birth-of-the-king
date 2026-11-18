// Copies the book's art and printed pages from ../curriculum into public/ (gitignored),
// so the repo keeps one copy of every image. Runs before dev and build.
import { cpSync, mkdirSync, existsSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const site = join(dirname(fileURLToPath(import.meta.url)), "..");
const repo = join(site, "..");
// In the git repo the book lives in ../curriculum and the PDFs in ../output.
// In the Mac "Birth of the King" folder it lives in ../Source and the PDFs sit in the folder itself.
const book = [join(repo, "curriculum"), join(repo, "Source")].find((d) => existsSync(join(d, "book/imgc")));
if (!book) throw new Error("Book source not found next to the site (expected ../curriculum or ../Source)");
const pdfs = [join(repo, "output"), repo].find((d) => existsSync(join(d, "Printable-Lesson-1-Student-Pages.pdf")));
if (!pdfs) throw new Error("Printable-Lesson-1-Student-Pages.pdf not found in ../output or ..");
const jobs = [
  [join(book, "book/imgc"), join(site, "public/images/book")],
  [join(book, "flip/pages"), join(site, "public/pages")],
];
for (const [from, to] of jobs) {
  if (!existsSync(from)) throw new Error(`Missing ${from}`);
  mkdirSync(to, { recursive: true });
  for (const f of readdirSync(from)) cpSync(join(from, f), join(to, f));
}
// Only the free Lesson 1 sample is published. The paid packs stay out of public/.
mkdirSync(join(site, "public/downloads"), { recursive: true });
cpSync(
  join(pdfs, "Printable-Lesson-1-Student-Pages.pdf"),
  join(site, "public/downloads/Beyond-the-Manger-Lesson-1-Free-Sample.pdf"),
);
console.log("assets synced");
