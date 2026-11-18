"use client";
import { useCallback, useEffect, useRef, useState } from "react";
import { Download, Eraser, Printer, RotateCcw, Undo2 } from "lucide-react";

// Tap-to-fill coloring on the book's own line art. Work is saved on this device (IndexedDB).
const PALETTE = [
  ["Gold", "#e7b93e"],
  ["Sun", "#f7dd5c"],
  ["Orange", "#f08a3c"],
  ["Red", "#d9483b"],
  ["Rose", "#f2a3b3"],
  ["Purple", "#7d4fb0"],
  ["Royal", "#2f4fa8"],
  ["Sky", "#7cc3ea"],
  ["Olive", "#7b9a3c"],
  ["Leaf", "#3f9b5a"],
  ["Sand", "#e2c79a"],
  ["Brown", "#8a5a3a"],
  ["Stone", "#a9adb6"],
  ["White", "#ffffff"],
] as const;

const DB = "botk-coloring";
function idb(): Promise<IDBDatabase> {
  return new Promise((res, rej) => {
    const r = indexedDB.open(DB, 1);
    r.onupgradeneeded = () => r.result.createObjectStore("pics");
    r.onsuccess = () => res(r.result);
    r.onerror = () => rej(r.error);
  });
}
async function save(key: string, blob: Blob | null) {
  const db = await idb();
  const tx = db.transaction("pics", "readwrite");
  if (blob) tx.objectStore("pics").put(blob, key);
  else tx.objectStore("pics").delete(key);
}
async function load(key: string): Promise<Blob | undefined> {
  const db = await idb();
  return new Promise((res) => {
    const r = db.transaction("pics").objectStore("pics").get(key);
    r.onsuccess = () => res(r.result as Blob | undefined);
    r.onerror = () => res(undefined);
  });
}

const hex = (h: string) => {
  const n = parseInt(h.slice(1), 16);
  return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
};

export function Coloring({ src, id, title }: { src: string; id: string; title: string }) {
  const canvas = useRef<HTMLCanvasElement>(null);
  const lines = useRef<Uint8Array | null>(null); // 1 = ink line
  const history = useRef<ImageData[]>([]);
  const [color, setColor] = useState<string>(PALETTE[0][1]);
  const [ready, setReady] = useState(false);
  const [canUndo, setCanUndo] = useState(false);

  const persist = useCallback(() => {
    const c = canvas.current;
    if (!c) return;
    c.toBlob((b) => b && save(id, b).catch(() => {}), "image/png");
  }, [id]);

  useEffect(() => {
    let alive = true;
    const base = new Image();
    base.src = src;
    base.onload = async () => {
      const c = canvas.current;
      if (!c || !alive) return;
      c.width = base.naturalWidth;
      c.height = base.naturalHeight;
      const ctx = c.getContext("2d", { willReadFrequently: true })!;
      ctx.fillStyle = "#fff";
      ctx.fillRect(0, 0, c.width, c.height);
      ctx.drawImage(base, 0, 0);
      const d = ctx.getImageData(0, 0, c.width, c.height).data;
      const mask = new Uint8Array(c.width * c.height);
      for (let i = 0, p = 0; i < d.length; i += 4, p++) {
        const luma = 0.299 * d[i] + 0.587 * d[i + 1] + 0.114 * d[i + 2];
        mask[p] = luma < 150 ? 1 : 0;
      }
      lines.current = mask;
      try {
        const saved = await load(id);
        if (saved && alive) {
          const bmp = await createImageBitmap(saved);
          ctx.drawImage(bmp, 0, 0);
        }
      } catch {}
      if (alive) setReady(true);
    };
    return () => {
      alive = false;
    };
  }, [src, id]);

  const fill = (x: number, y: number) => {
    const c = canvas.current;
    const mask = lines.current;
    if (!c || !mask) return;
    const ctx = c.getContext("2d", { willReadFrequently: true })!;
    const W = c.width,
      H = c.height;
    const img = ctx.getImageData(0, 0, W, H);
    const d = img.data;
    const start = y * W + x;
    if (mask[start]) return;
    history.current.push(new ImageData(new Uint8ClampedArray(d), W, H));
    if (history.current.length > 8) history.current.shift();
    setCanUndo(true);
    const [r, g, b] = hex(color);
    const sr = d[start * 4],
      sg = d[start * 4 + 1],
      sb = d[start * 4 + 2];
    if (sr === r && sg === g && sb === b) return;
    const tol = 60;
    const same = (p: number) =>
      !mask[p] && Math.abs(d[p * 4] - sr) + Math.abs(d[p * 4 + 1] - sg) + Math.abs(d[p * 4 + 2] - sb) <= tol;
    const seen = new Uint8Array(W * H);
    const stack = [start];
    const painted: number[] = [];
    while (stack.length) {
      let p = stack.pop()!;
      const row = Math.floor(p / W);
      while (p % W > 0 && !seen[p - 1] && same(p - 1)) p--;
      let up = false,
        down = false;
      for (; p < (row + 1) * W && !seen[p] && same(p); p++) {
        seen[p] = 1;
        painted.push(p);
        d[p * 4] = r;
        d[p * 4 + 1] = g;
        d[p * 4 + 2] = b;
        d[p * 4 + 3] = 255;
        if (row > 0) {
          const q = p - W;
          if (!seen[q] && same(q)) {
            if (!up) { stack.push(q); up = true; }
          } else up = false;
        }
        if (row < H - 1) {
          const q = p + W;
          if (!seen[q] && same(q)) {
            if (!down) { stack.push(q); down = true; }
          } else down = false;
        }
      }
    }
    // soften the seam: also tint anti-aliased pixels that touch the fill
    for (const p of painted) {
      for (const q of [p - 1, p + 1, p - W, p + W]) {
        if (q < 0 || q >= W * H || seen[q] || mask[q]) continue;
        const l = 0.299 * d[q * 4] + 0.587 * d[q * 4 + 1] + 0.114 * d[q * 4 + 2];
        if (l > 150 && l < 245) {
          d[q * 4] = (d[q * 4] + r) >> 1;
          d[q * 4 + 1] = (d[q * 4 + 1] + g) >> 1;
          d[q * 4 + 2] = (d[q * 4 + 2] + b) >> 1;
        }
      }
    }
    ctx.putImageData(img, 0, 0);
    persist();
  };

  const onPointer = (e: React.PointerEvent<HTMLCanvasElement>) => {
    const c = canvas.current;
    if (!c || !ready) return;
    const rect = c.getBoundingClientRect();
    const x = Math.floor(((e.clientX - rect.left) / rect.width) * c.width);
    const y = Math.floor(((e.clientY - rect.top) / rect.height) * c.height);
    // a tap that lands on a line nudges to the nearest open pixel
    const mask = lines.current!;
    for (let rr = 0; rr < 6; rr++) {
      for (const [dx, dy] of [[0, 0], [rr, 0], [-rr, 0], [0, rr], [0, -rr]]) {
        const px = x + dx,
          py = y + dy;
        if (px >= 0 && py >= 0 && px < c.width && py < c.height && !mask[py * c.width + px]) {
          fill(px, py);
          return;
        }
      }
    }
  };

  const undo = () => {
    const c = canvas.current;
    const prev = history.current.pop();
    if (!c || !prev) return;
    c.getContext("2d")!.putImageData(prev, 0, 0);
    setCanUndo(history.current.length > 0);
    persist();
  };

  const reset = () => {
    const c = canvas.current;
    if (!c) return;
    const base = new Image();
    base.src = src;
    base.onload = () => {
      const ctx = c.getContext("2d")!;
      ctx.fillStyle = "#fff";
      ctx.fillRect(0, 0, c.width, c.height);
      ctx.drawImage(base, 0, 0);
      history.current = [];
      setCanUndo(false);
      save(id, null).catch(() => {});
    };
  };

  const download = () => {
    const a = document.createElement("a");
    a.download = `${title.replace(/[^a-z0-9]+/gi, "-")}.png`;
    a.href = canvas.current!.toDataURL("image/png");
    a.click();
  };

  const btn = "inline-flex min-h-11 items-center gap-2 rounded-full border border-navy/20 bg-paper px-4 font-sans text-sm font-bold text-navy disabled:opacity-40";

  return (
    <div className="grid gap-4 lg:grid-cols-[1fr_260px] lg:items-start">
      <div className="relative overflow-hidden rounded-2xl border border-line bg-white">
        <canvas
          ref={canvas}
          onPointerDown={onPointer}
          aria-label={`Coloring page: ${title}. Pick a color, then tap a space to fill it.`}
          className="mx-auto block h-auto max-h-[56svh] w-auto max-w-full cursor-crosshair touch-manipulation lg:max-h-[78vh]"
        />
        {!ready && <div className="absolute inset-0 grid place-items-center font-sans text-sm text-muted">Getting the page ready…</div>}
      </div>
      <div className="no-print order-first lg:sticky lg:top-4 lg:order-none">
        <p className="kicker text-gold-deep">Pick a color, tap a space</p>
        <div role="radiogroup" aria-label="Colors" className="mt-2 grid grid-cols-7 gap-1.5 lg:grid-cols-4 lg:gap-2">
          {PALETTE.map(([name, c]) => (
            <button
              key={c}
              role="radio"
              aria-checked={color === c}
              aria-label={name}
              onClick={() => setColor(c)}
              className={`aspect-square min-h-11 rounded-full border-2 transition-transform ${color === c ? "scale-110 border-navy ring-2 ring-gold" : "border-black/15"}`}
              style={{ background: c }}
            />
          ))}
        </div>
        <div className="mt-3 flex flex-wrap gap-2 max-lg:[&>button]:px-3 max-lg:[&>button]:text-xs">
          <button className={btn} onClick={undo} disabled={!canUndo}><Undo2 size={16} aria-hidden /> Undo</button>
          <button className={btn} onClick={() => setColor("#ffffff")}><Eraser size={16} aria-hidden /> Eraser</button>
          <button className={btn} onClick={reset}><RotateCcw size={16} aria-hidden /> Start over</button>
          <button className={btn} onClick={download}><Download size={16} aria-hidden /> Save picture</button>
          <button className={btn} onClick={() => window.print()}><Printer size={16} aria-hidden /> Print</button>
        </div>
      </div>
    </div>
  );
}
