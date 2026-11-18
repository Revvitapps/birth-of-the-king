// Requests every route from the sitemap (plus the PWA files) against a running server.
// Usage: BASE=http://localhost:3000 node scripts/check-routes.mjs
const BASE = process.env.BASE || "http://localhost:3000";
const xml = await (await fetch(`${BASE}/sitemap.xml`)).text();
const urls = [...xml.matchAll(/<loc>(.*?)<\/loc>/g)].map((m) => new URL(m[1]).pathname);
const extra = ["/manifest.webmanifest", "/sw.js", "/offline.html", "/robots.txt", "/pwa/icon-512.png", "/downloads/Birth-of-the-King-Lesson-1-Free-Sample.pdf"];
let bad = 0;
for (const p of [...urls, ...extra]) {
  const r = await fetch(BASE + p);
  if (!r.ok) { bad++; console.log("FAIL", r.status, p); }
}
const nf = await fetch(`${BASE}/lessons/9`);
if (nf.status !== 404) { bad++; console.log("FAIL expected 404 for /lessons/9, got", nf.status); }
const api = await fetch(`${BASE}/api/pipeline`, { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ email: "test@example.com", source: "check" }) });
if (!api.ok) { bad++; console.log("FAIL /api/pipeline", api.status); }
console.log(`${urls.length + extra.length} routes checked, ${bad} failed`);
process.exit(bad ? 1 : 0);
