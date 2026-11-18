"use client";
// Celebrations for kids: a star burst and a soft chime. Respects reduced motion and a mute switch.

const MUTE = "botk:mute";
let ctx: AudioContext | null = null;

export const isMuted = () => {
  try {
    return localStorage.getItem(MUTE) === "1";
  } catch {
    return false;
  }
};
export const setMuted = (m: boolean) => {
  try {
    localStorage.setItem(MUTE, m ? "1" : "0");
  } catch {}
};

function tone(freqs: number[], dur = 0.12, type: OscillatorType = "triangle", gap = 0.09) {
  if (isMuted()) return;
  try {
    ctx ??= new AudioContext();
    const t0 = ctx.currentTime;
    freqs.forEach((f, i) => {
      const o = ctx!.createOscillator();
      const g = ctx!.createGain();
      o.type = type;
      o.frequency.value = f;
      const t = t0 + i * gap;
      g.gain.setValueAtTime(0.0001, t);
      g.gain.exponentialRampToValueAtTime(0.18, t + 0.02);
      g.gain.exponentialRampToValueAtTime(0.0001, t + dur + 0.2);
      o.connect(g).connect(ctx!.destination);
      o.start(t);
      o.stop(t + dur + 0.25);
    });
  } catch {}
}

export const chimeRight = () => tone([784, 1047]);
export const chimeWrong = () => tone([220, 196], 0.1, "sine", 0.12);
export const chimeWin = () => tone([523, 659, 784, 1047, 1319], 0.16, "triangle", 0.11);

const reduced = () => typeof window !== "undefined" && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

// Gold and cream stars burst from a point (or the screen centre) and fall away.
export function starBurst(x?: number, y?: number, count = 18) {
  if (reduced()) return;
  const cx = x ?? window.innerWidth / 2;
  const cy = y ?? window.innerHeight / 2.4;
  const layer = document.createElement("div");
  layer.setAttribute("aria-hidden", "true");
  layer.style.cssText = "position:fixed;inset:0;pointer-events:none;z-index:60;overflow:hidden";
  const colors = ["#c9a24a", "#efe2bf", "#e7b93e", "#ffffff", "#7cc3ea"];
  for (let i = 0; i < count; i++) {
    const s = document.createElement("span");
    const a = (Math.PI * 2 * i) / count + Math.random() * 0.4;
    const d = 70 + Math.random() * 140;
    const size = 12 + Math.random() * 16;
    s.textContent = "★";
    s.style.cssText = `position:absolute;left:${cx}px;top:${cy}px;font-size:${size}px;color:${colors[i % colors.length]};text-shadow:0 1px 0 rgba(0,0,0,.25);transform:translate(-50%,-50%)`;
    layer.appendChild(s);
    s.animate(
      [
        { transform: "translate(-50%,-50%) scale(.3) rotate(0deg)", opacity: 1 },
        { transform: `translate(calc(-50% + ${Math.cos(a) * d}px), calc(-50% + ${Math.sin(a) * d}px)) scale(1) rotate(180deg)`, opacity: 1, offset: 0.6 },
        { transform: `translate(calc(-50% + ${Math.cos(a) * d * 1.2}px), calc(-50% + ${Math.sin(a) * d + 120}px)) scale(.8) rotate(260deg)`, opacity: 0 },
      ],
      { duration: 1100 + Math.random() * 400, easing: "cubic-bezier(.2,.7,.3,1)", fill: "forwards" },
    );
  }
  document.body.appendChild(layer);
  setTimeout(() => layer.remove(), 1700);
}

export function celebrate(el?: Element | null) {
  const r = el?.getBoundingClientRect();
  starBurst(r ? r.left + r.width / 2 : undefined, r ? r.top + r.height / 2 : undefined, 26);
  chimeWin();
}

export function smallWin(el?: Element | null) {
  const r = el?.getBoundingClientRect();
  starBurst(r ? r.left + r.width / 2 : undefined, r ? r.top + r.height / 2 : undefined, 8);
  chimeRight();
}
