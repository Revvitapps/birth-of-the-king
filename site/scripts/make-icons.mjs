// Builds the PWA icons and the OG image from the book's own art (sharp).
// Regular icons: navy tile, gold star crown mark. Maskable: same mark inside the 80% safe zone.
import sharp from "sharp";
import { mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const site = join(dirname(fileURLToPath(import.meta.url)), "..");
const out = join(site, "public/pwa");
const art = join(site, "../curriculum/book/imgc");
mkdirSync(out, { recursive: true });

const NAVY = "#1f2f5c", GOLD = "#c9a24a", SOFT = "#efe2bf";

// A crown under a star: the book's ✦ motif and the King.
const mark = (size, scale) => {
  const s = size * scale;
  const o = (size - s) / 2;
  const u = s / 100;
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 ${size} ${size}">
  <rect width="${size}" height="${size}" fill="${NAVY}"/>
  <g transform="translate(${o},${o}) scale(${u})">
    <path d="M50 6 L55 22 L71 27 L55 32 L50 48 L45 32 L29 27 L45 22 Z" fill="${SOFT}"/>
    <path d="M14 52 L30 66 L50 46 L70 66 L86 52 L80 84 L20 84 Z" fill="${GOLD}"/>
    <rect x="20" y="87" width="60" height="7" rx="2" fill="${GOLD}"/>
  </g></svg>`;
};

const png = (svg, file) => sharp(Buffer.from(svg)).png().toFile(join(out, file));

await png(mark(192, 0.86), "icon-192.png");
await png(mark(512, 0.86), "icon-512.png");
await png(mark(192, 0.62), "maskable-192.png");
await png(mark(512, 0.62), "maskable-512.png");
await png(mark(180, 0.8), "apple-touch-icon.png");

// OG: cover art on the right, title on navy at left.
const cover = await sharp(join(art, "cover.jpg")).resize(560, 630, { fit: "cover", position: "top" }).toBuffer();
const text = `<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630">
  <rect width="1200" height="630" fill="${NAVY}"/>
  <text x="64" y="150" font-family="Inter, Arial, sans-serif" font-size="22" font-weight="800" letter-spacing="6" fill="${GOLD}">AN IN-DEPTH BIBLE CURRICULUM</text>
  <text x="60" y="280" font-family="Inter, Arial, sans-serif" font-size="92" font-weight="900" fill="#fff">BEYOND</text>
  <text x="60" y="390" font-family="Inter, Arial, sans-serif" font-size="92" font-weight="900" fill="#fff">THE MANGER</text>
  <rect x="64" y="420" width="120" height="6" fill="${GOLD}"/>
  <text x="64" y="480" font-family="Georgia, serif" font-style="italic" font-size="28" fill="${SOFT}">7 lessons · readings, coloring and activities</text>
</svg>`;
await sharp(Buffer.from(text)).composite([{ input: cover, left: 640, top: 0 }]).png().toFile(join(out, "og.png"));
console.log("icons written to public/pwa");
