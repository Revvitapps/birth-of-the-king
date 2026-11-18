// axe-core scan of the main routes (WCAG 2 A/AA). Usage: BASE=http://localhost:3000 node scripts/check-a11y.mjs
import { createRequire } from "node:module";
const require = createRequire(import.meta.url);
const { chromium } = require("playwright");
const { AxeBuilder } = require("@axe-core/playwright");

const BASE = process.env.BASE || "http://localhost:3000";
const routes = ["/", "/lessons", "/lessons/1", "/lessons/1/the-promised-king-son-of-david", "/lessons/1/king-david-coloring", "/lessons/2/lets-see-what-you-remember-activity", "/activities", "/book", "/more"];
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 390, height: 844 } });
const page = await ctx.newPage();
let total = 0;
for (const r of routes) {
  await page.goto(BASE + r, { waitUntil: "networkidle" });
  const res = await new AxeBuilder({ page }).withTags(["wcag2a", "wcag2aa"]).analyze();
  for (const v of res.violations) {
    total++;
    console.log(r, v.id, v.impact, v.nodes.length, v.nodes.slice(0, 2).map((n) => n.target.join(" ")).join(" | "));
  }
}
await browser.close();
console.log(`${routes.length} routes, ${total} violations`);
process.exit(total ? 1 : 0);
