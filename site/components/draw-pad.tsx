"use client";
import { useEffect, useRef, type ReactNode } from "react";
import { RotateCcw } from "lucide-react";

const INKS = ["#1f2f5c", "#d9483b", "#3f9b5a", "#e7b93e", "#7d4fb0"];

// A small sketch pad for the book's "draw your answer" boxes. Saved on this device.
export function DrawPad({
  id,
  label,
  tall = false,
  background,
  aspect,
  thick = false,
}: {
  id: string;
  label: string;
  tall?: boolean;
  background?: ReactNode;
  aspect?: string;
  thick?: boolean;
}) {
  const ref = useRef<HTMLCanvasElement>(null);
  const ink = useRef(INKS[0]);
  const drawing = useRef(false);
  const key = `botk:draw:${id}`;

  useEffect(() => {
    const c = ref.current!;
    const ratio = Math.min(2, window.devicePixelRatio || 1);
    const w = c.clientWidth;
    const h = c.clientHeight;
    c.width = w * ratio;
    c.height = h * ratio;
    const ctx = c.getContext("2d")!;
    ctx.scale(ratio, ratio);
    ctx.lineCap = "round";
    ctx.lineJoin = "round";
    ctx.lineWidth = thick ? 7 : 4;
    try {
      const saved = localStorage.getItem(key);
      if (saved) {
        const im = new Image();
        im.onload = () => ctx.drawImage(im, 0, 0, w, h);
        im.src = saved;
      }
    } catch {}
  }, [key, thick]);

  const pos = (e: React.PointerEvent) => {
    const r = ref.current!.getBoundingClientRect();
    return [e.clientX - r.left, e.clientY - r.top] as const;
  };
  const down = (e: React.PointerEvent<HTMLCanvasElement>) => {
    e.currentTarget.setPointerCapture(e.pointerId);
    drawing.current = true;
    const ctx = ref.current!.getContext("2d")!;
    ctx.strokeStyle = ink.current;
    const [x, y] = pos(e);
    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(x + 0.1, y + 0.1);
    ctx.stroke();
  };
  const move = (e: React.PointerEvent) => {
    if (!drawing.current) return;
    const ctx = ref.current!.getContext("2d")!;
    const [x, y] = pos(e);
    ctx.lineTo(x, y);
    ctx.stroke();
  };
  const up = () => {
    if (!drawing.current) return;
    drawing.current = false;
    try { localStorage.setItem(key, ref.current!.toDataURL("image/png")); } catch {}
  };
  const clear = () => {
    const c = ref.current!;
    c.getContext("2d")!.clearRect(0, 0, c.width, c.height);
    try { localStorage.removeItem(key); } catch {}
  };

  return (
    <div className="rounded-xl border-2 border-dashed border-navy/25 bg-white p-3">
      <div className="flex flex-wrap items-center justify-between gap-2">
        <p className="font-sans text-sm font-bold text-navy">{label}</p>
        <div className="flex items-center gap-1.5">
          {INKS.map((c) => (
            <button
              key={c}
              aria-label={`Pen color ${c}`}
              onClick={() => (ink.current = c)}
              className="h-7 w-7 rounded-full border-2 border-white ring-1 ring-black/15"
              style={{ background: c }}
            />
          ))}
          <button onClick={clear} aria-label="Clear drawing" className="ml-1 grid h-11 w-11 place-items-center text-muted hover:text-navy">
            <RotateCcw size={16} />
          </button>
        </div>
      </div>
      <div
        className={`relative mt-2 overflow-hidden rounded-lg bg-paper ${aspect ? "" : tall ? "h-72" : "h-52"}`}
        style={aspect ? { aspectRatio: aspect } : undefined}
      >
        {background && <div aria-hidden className="pointer-events-none absolute inset-0">{background}</div>}
        <canvas
          ref={ref}
          onPointerDown={down}
          onPointerMove={move}
          onPointerUp={up}
          onPointerCancel={up}
          aria-label={`Drawing space: ${label}`}
          className="absolute inset-0 block h-full w-full touch-none"
        />
      </div>
    </div>
  );
}
