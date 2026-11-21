// Screenshots the main routes at phone and desktop size and fails on horizontal overflow.
// Usage: BASE=http://localhost:3000 node scripts/check-shots.mjs
import { createRequire } from "node:module";
const { chromium } = createRequire(import.meta.url)("playwright"); // preinstalled globally or as a devDependency
import { mkdirSync } from "node:fs";

const BASE = process.env.BASE || "http://localhost:3000";
const routes = [
  "/",
  "/lessons",
  "/lessons/1",
  "/lessons/1/the-promised-king-son-of-david",
  "/lessons/1/king-david-coloring",
  "/lessons/4/lets-see-what-you-remember-activity",
  "/lessons/5/the-long-road-west-activity",
  "/lessons/5/a-magis-travel-journal-activity",
  "/lessons/1/yeshuas-family-tree-activity",
  "/activities",
  "/book",
  "/more",
];
const sizes = [
  { name: "phone", width: 390, height: 844 },
  { name: "desktop", width: 1440, height: 900 },
];
mkdirSync("shots", { recursive: true });
const browser = await chromium.launch();
let bad = 0;
for (const s of sizes) {
  const ctx = await browser.newContext({ viewport: { width: s.width, height: s.height }, deviceScaleFactor: 1 });
  const page = await ctx.newPage();
  const errors = [];
  page.on("pageerror", (e) => errors.push(e.message));
  for (const r of routes) {
    await page.goto(BASE + r, { waitUntil: "networkidle" });
    await page.waitForTimeout(400);
    const over = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    if (over > 0) { bad++; console.log(`OVERFLOW ${over}px ${s.name} ${r}`); }
    const tab = await page.locator('nav[aria-label="Main"]').isVisible();
    if (!tab) { bad++; console.log(`NO TAB BAR ${s.name} ${r}`); }
    const file = `shots/${s.name}${r === "/" ? "-home" : r.replaceAll("/", "-")}.png`;
    await page.screenshot({ path: file, fullPage: process.env.FULL === "1" });
  }
  if (errors.length) { bad++; console.log(s.name, "page errors:", errors); }
  await ctx.close();
}
await browser.close();
console.log(`${routes.length * sizes.length} screenshots, ${bad} problems`);
process.exit(bad ? 1 : 0);
