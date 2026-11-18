// Copies the book's art and printed pages from ../curriculum into public/ (gitignored),
// so the repo keeps one copy of every image. Runs before dev and build.
import { cpSync, mkdirSync, existsSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const site = join(dirname(fileURLToPath(import.meta.url)), "..");
const repo = join(site, "..");
const jobs = [
  [join(repo, "curriculum/book/imgc"), join(site, "public/images/book")],
  [join(repo, "curriculum/flip/pages"), join(site, "public/pages")],
];
for (const [from, to] of jobs) {
  if (!existsSync(from)) throw new Error(`Missing ${from}`);
  mkdirSync(to, { recursive: true });
  for (const f of readdirSync(from)) cpSync(join(from, f), join(to, f));
}
// Only the free Lesson 1 sample is published. The paid packs stay out of public/.
mkdirSync(join(site, "public/downloads"), { recursive: true });
cpSync(
  join(repo, "output/Printable-Lesson-1-Student-Pages.pdf"),
  join(site, "public/downloads/Birth-of-the-King-Lesson-1-Free-Sample.pdf"),
);
console.log("assets synced");
