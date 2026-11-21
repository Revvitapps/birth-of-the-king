/* Beyond the Manger service worker.
   Navigations: network first, then the last good copy, then /offline.html.
   Static assets (/_next/static, /images, /pages, /pwa, fonts): cache first, capped.
   Never touches /api or non-GET requests. Bump VERSION to roll caches. */
const VERSION = "botk-v3";
const SHELL = `${VERSION}-shell`;
const PAGES = `${VERSION}-pages`;
const ASSETS = `${VERSION}-assets`;
const PRECACHE = ["/", "/lessons", "/activities", "/book", "/more", "/lessons/1", "/offline.html", "/manifest.webmanifest", "/pwa/icon-192.png"];
const MAX_PAGES = 80;
const MAX_ASSETS = 300;

self.addEventListener("install", (e) => {
  e.waitUntil(
    caches.open(SHELL).then((c) => Promise.all(PRECACHE.map((u) => c.add(new Request(u, { cache: "reload" })).catch(() => {})))).then(() => self.skipWaiting()),
  );
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches
      .keys()
      .then((keys) => Promise.all(keys.filter((k) => !k.startsWith(VERSION)).map((k) => caches.delete(k))))
      .then(() => self.clients.claim()),
  );
});

async function trim(name, max) {
  const c = await caches.open(name);
  const keys = await c.keys();
  for (let i = 0; i < keys.length - max; i++) await c.delete(keys[i]);
}

self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin || url.pathname.startsWith("/api/")) return;

  if (req.mode === "navigate") {
    e.respondWith(
      fetch(req)
        .then((res) => {
          if (res.ok) {
            const copy = res.clone();
            caches.open(PAGES).then((c) => c.put(req, copy)).then(() => trim(PAGES, MAX_PAGES));
          }
          return res;
        })
        .catch(async () => (await caches.match(req)) || (await caches.match("/offline.html"))),
    );
    return;
  }

  const p = url.pathname;
  const isAsset =
    p.startsWith("/_next/static/") || p.startsWith("/_next/image") || p.startsWith("/images/") || p.startsWith("/pages/") || p.startsWith("/pwa/") || /\.(woff2?|png|jpg|jpeg|webp|avif|svg)$/.test(p);
  if (!isAsset) return;
  e.respondWith(
    caches.match(req).then(
      (hit) =>
        hit ||
        fetch(req).then((res) => {
          if (res.ok) {
            const copy = res.clone();
            caches.open(ASSETS).then((c) => c.put(req, copy)).then(() => trim(ASSETS, MAX_ASSETS));
          }
          return res;
        }),
    ),
  );
});
