"use client";
// On-screen versions of the book's puzzles: matching, story order, labels, family tree,
// word search, maze and letter tracing. Answers come from the book's own answer key.
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { Check, RotateCcw, Sparkles, Star, Volume2 } from "lucide-react";
import { celebrate, chimeRight, chimeWrong, smallWin } from "@/lib/fun";
import { Md } from "@/components/md";
import { DrawPad } from "@/components/draw-pad";

/* ---------- shared bits ---------- */

function useSaved<T>(key: string, initial: T) {
  const [v, setV] = useState<T>(initial);
  useEffect(() => {
    try {
      const raw = localStorage.getItem(key);
      // eslint-disable-next-line react-hooks/set-state-in-effect -- hydrate from device storage
      if (raw) setV(JSON.parse(raw));
    } catch {}
  }, [key]);
  const set = useCallback(
    (x: T) => {
      setV(x);
      try {
        localStorage.setItem(key, JSON.stringify(x));
      } catch {}
    },
    [key],
  );
  return [v, set] as const;
}

function useShake() {
  const [k, setK] = useState<string | null>(null);
  const shake = (id: string) => {
    setK(null);
    requestAnimationFrame(() => setK(id));
    chimeWrong();
    setTimeout(() => setK((c) => (c === id ? null : c)), 450);
  };
  return [k, shake] as const;
}

function Banner({ done, total, label, onReset }: { done: number; total: number; label: string; onReset?: () => void }) {
  const finished = done >= total;
  return (
    <div
      className={`mt-4 flex flex-wrap items-center justify-between gap-3 rounded-2xl px-4 py-3 font-sans ${finished ? "bg-gold text-navy" : "bg-navy/5 text-navy"}`}
      role="status"
    >
      <span className="flex items-center gap-2 text-sm font-extrabold">
        {finished ? <Sparkles size={18} aria-hidden /> : <Star size={18} aria-hidden className="text-gold-deep" />}
        {finished ? `You did it! ${label}` : `${done} of ${total} done`}
      </span>
      <span className="flex items-center gap-1" aria-hidden>
        {Array.from({ length: total }).map((_, i) => (
          <Star key={i} size={16} className={i < done ? "fill-current text-gold-deep" : "text-navy/20"} />
        ))}
      </span>
      {finished && onReset && (
        <button onClick={onReset} className="inline-flex min-h-11 items-center gap-1 rounded-full px-3 text-sm font-bold underline-offset-4 hover:underline">
          <RotateCcw size={14} aria-hidden /> Play again
        </button>
      )}
    </div>
  );
}

const PAIR = ["#f2a3b3", "#7cc3ea", "#f7dd5c", "#9ad19a", "#c9b2ea", "#f5b97a"];

/* ---------- matching ---------- */

export function MatchGame({ id, left, right, answer }: { id: string; left: string[]; right: string[]; answer: number[] }) {
  const [pairs, setPairs] = useSaved<(number | null)[]>(`botk:game:${id}`, left.map(() => null));
  const [sel, setSel] = useState<number | null>(null);
  const [shaking, shake] = useShake();
  const box = useRef<HTMLDivElement>(null);
  const done = pairs.filter((p) => p !== null).length;

  const pick = (r: number, el: HTMLElement) => {
    if (sel === null) return;
    if (answer[sel] === r) {
      const next = [...pairs];
      next[sel] = r;
      setPairs(next);
      setSel(null);
      if (next.every((p) => p !== null)) celebrate(box.current);
      else smallWin(el);
    } else {
      shake(`r${r}`);
    }
  };
  const owner = (r: number) => pairs.findIndex((p) => p === r);

  return (
    <div ref={box} className="mt-5">
      <p className="font-sans text-sm font-bold text-navy">Tap a word on the left, then tap what it matches on the right.</p>
      <div className="mt-3 grid grid-cols-[minmax(0,0.8fr)_minmax(0,1.2fr)] gap-3">
        <ul className="space-y-2">
          {left.map((l, i) => {
            const paired = pairs[i] !== null;
            return (
              <li key={i}>
                <button
                  disabled={paired}
                  onClick={() => setSel(sel === i ? null : i)}
                  aria-pressed={sel === i}
                  className={`flex min-h-14 w-full items-center gap-2 rounded-xl border-2 px-3 py-2 text-left font-sans text-base font-extrabold transition-transform ${
                    sel === i ? "scale-[1.03] border-navy bg-navy text-white" : "border-navy/15 bg-white text-navy"
                  }`}
                  style={paired ? { background: PAIR[i % PAIR.length], borderColor: "transparent" } : undefined}
                >
                  {paired && <Check size={18} aria-hidden />}
                  <Md text={l} />
                </button>
              </li>
            );
          })}
        </ul>
        <ul className="space-y-2">
          {right.map((r, i) => {
            const o = owner(i);
            return (
              <li key={i}>
                <button
                  disabled={o >= 0}
                  onClick={(e) => pick(i, e.currentTarget)}
                  className={`min-h-14 w-full rounded-xl border-2 px-3 py-2 text-left font-serif text-base leading-snug ${shaking === `r${i}` ? "shake border-red-400" : "border-navy/15"} ${
                    o >= 0 ? "border-transparent" : sel !== null ? "bg-white hover:border-gold" : "bg-white"
                  }`}
                  style={o >= 0 ? { background: PAIR[o % PAIR.length] } : undefined}
                >
                  <Md text={r} />
                </button>
              </li>
            );
          })}
        </ul>
      </div>
      <Banner done={done} total={left.length} label="Every match is right." onReset={() => setPairs(left.map(() => null))} />
    </div>
  );
}

/* ---------- story order ---------- */

export function OrderGame({ id, items, answer }: { id: string; items: { letter: string; text: string }[]; answer: number[] }) {
  const [placed, setPlaced] = useSaved<number[]>(`botk:game:${id}`, []);
  const [shaking, shake] = useShake();
  const [hint, setHint] = useState("");
  const box = useRef<HTMLDivElement>(null);
  const next = placed.length + 1;
  const finished = placed.length === items.length;

  const tap = (i: number, el: HTMLElement) => {
    if (placed.includes(i)) return;
    if (answer[i] === next) {
      const p = [...placed, i];
      setPlaced(p);
      setHint("");
      if (p.length === items.length) celebrate(box.current);
      else smallWin(el);
    } else {
      shake(`o${i}`);
      setHint(answer[i] > next ? "Not yet! Something else happened before that." : "That one already happened.");
    }
  };

  return (
    <div ref={box} className="mt-5">
      {!finished && (
        <p className="font-sans text-sm font-bold text-navy">
          What happened <span className="rounded bg-gold px-1.5 text-navy">{next === 1 ? "first" : `next (#${next})`}</span>? Tap it.
        </p>
      )}
      {hint && <p className="mt-1 font-serif text-base text-red-700" role="status">{hint}</p>}
      {finished ? (
        <ol className="mt-3 space-y-2">
          {placed.map((i, n) => (
            <li key={i} className="flex items-start gap-3 rounded-xl bg-gold-soft/60 px-3 py-2">
              <span className="grid h-8 w-8 shrink-0 place-items-center rounded-full bg-navy font-sans font-extrabold text-gold">{n + 1}</span>
              <span className="pt-1 font-serif text-lg"><Md text={items[i].text} /></span>
            </li>
          ))}
        </ol>
      ) : (
        <ul className="mt-3 grid gap-2 sm:grid-cols-2">
          {items.map((it, i) => {
            const pos = placed.indexOf(i);
            return (
              <li key={i}>
                <button
                  disabled={pos >= 0}
                  onClick={(e) => tap(i, e.currentTarget)}
                  className={`flex min-h-14 w-full items-start gap-3 rounded-xl border-2 px-3 py-2 text-left ${shaking === `o${i}` ? "shake border-red-400" : pos >= 0 ? "border-transparent bg-gold-soft/70" : "border-navy/15 bg-white hover:border-gold"}`}
                >
                  <span className={`grid h-8 w-8 shrink-0 place-items-center rounded-full font-sans font-extrabold ${pos >= 0 ? "bg-navy text-gold" : "bg-navy/10 text-navy/40"}`}>
                    {pos >= 0 ? pos + 1 : "?"}
                  </span>
                  <span className="pt-1 font-serif text-base leading-snug"><Md text={it.text} /></span>
                </button>
              </li>
            );
          })}
        </ul>
      )}
      <Banner done={placed.length} total={items.length} label="The whole story is in order." onReset={() => setPlaced([])} />
    </div>
  );
}

/* ---------- label / fill-in with a word bank (used by the house and the family tree) ---------- */

function useSlots(id: string, answers: string[], bank: string[]) {
  const [filled, setFilled] = useSaved<(string | null)[]>(`botk:game:${id}`, answers.map(() => null));
  const [chip, setChip] = useState<string | null>(null);
  const [shaking, shake] = useShake();
  const left = bank.filter((w) => !filled.some((f) => f && f.toLowerCase() === w.toLowerCase()));
  const drop = (slot: number, el: HTMLElement, root: HTMLElement | null) => {
    if (!chip || filled[slot]) return;
    if (answers[slot].toLowerCase() === chip.toLowerCase()) {
      const n = [...filled];
      n[slot] = chip;
      setFilled(n);
      setChip(null);
      if (n.every(Boolean)) celebrate(root);
      else smallWin(el);
    } else shake(`s${slot}`);
  };
  return { filled, chip, setChip, left, drop, shaking, reset: () => setFilled(answers.map(() => null)), done: filled.filter(Boolean).length };
}

function Bank({ words, chip, setChip }: { words: string[]; chip: string | null; setChip: (c: string | null) => void }) {
  if (!words.length) return null;
  return (
    <div className="sticky top-2 z-10 rounded-2xl bg-navy p-3 shadow-lg">
      <p className="kicker text-gold">Word bank · tap a word, then tap its spot</p>
      <div className="mt-2 flex flex-wrap gap-2">
        {words.map((w) => (
          <button
            key={w}
            onClick={() => setChip(chip === w ? null : w)}
            aria-pressed={chip === w}
            className={`min-h-11 rounded-full px-4 font-sans text-base font-bold transition-transform ${chip === w ? "scale-110 bg-gold text-navy" : "bg-white text-navy"}`}
          >
            {w}
          </button>
        ))}
      </div>
    </div>
  );
}

function Slot({ label, value, active, shaking, onTap, tone = "light" }: { label?: string; value: string | null; active: boolean; shaking: boolean; onTap: (el: HTMLElement) => void; tone?: "light" | "fixed" }) {
  if (tone === "fixed")
    return <div className="rounded-xl bg-navy px-3 py-2 text-center font-sans text-base font-extrabold text-gold">{label}</div>;
  return (
    <button
      onClick={(e) => onTap(e.currentTarget)}
      disabled={!!value}
      className={`flex min-h-12 w-full flex-col items-center justify-center rounded-xl border-2 px-2 py-1 text-center ${
        value ? "border-transparent bg-gold-soft" : shaking ? "shake border-red-400 bg-white" : active ? "border-dashed border-gold bg-white" : "border-dashed border-navy/25 bg-white"
      }`}
    >
      {label && <span className="font-sans text-[11px] font-bold uppercase tracking-wide text-muted">{label}</span>}
      <span className="font-sans text-base font-extrabold text-navy">{value || (active ? "Tap here" : "?")}</span>
    </button>
  );
}

export function FillGame({ id, rows, answer, bank }: { id: string; rows: string[]; answer: string[]; bank: string[] }) {
  const s = useSlots(id, answer, bank);
  const box = useRef<HTMLDivElement>(null);
  return (
    <div ref={box} className="mt-5 space-y-3">
      <Bank words={s.left} chip={s.chip} setChip={s.setChip} />
      <ul className="space-y-2">
        {rows.map((r, i) => (
          <li key={i} className="grid items-center gap-2 rounded-xl border border-line bg-paper p-3 sm:grid-cols-[1.2fr_1fr]">
            <span className="font-serif text-lg"><Md text={r} /></span>
            <Slot value={s.filled[i]} active={!!s.chip} shaking={s.shaking === `s${i}`} onTap={(el) => s.drop(i, el, box.current)} />
          </li>
        ))}
      </ul>
      <Banner done={s.done} total={rows.length} label="Every part is labeled." onReset={s.reset} />
    </div>
  );
}

export function TreeGame({ id, slots, bank }: { id: string; slots: { label: string; answer: string }[]; bank: string[] }) {
  const s = useSlots(id, slots.map((x) => x.answer), bank);
  const box = useRef<HTMLDivElement>(null);
  const slot = (i: number) => (
    <Slot label={slots[i].label} value={s.filled[i]} active={!!s.chip} shaking={s.shaking === `s${i}`} onTap={(el) => s.drop(i, el, box.current)} />
  );
  const line = <div className="mx-auto h-4 w-0.5 bg-navy/40" aria-hidden />;
  return (
    <div ref={box} className="mt-5 space-y-3">
      <Bank words={s.left} chip={s.chip} setChip={s.setChip} />
      <div className="mx-auto max-w-md rounded-2xl border border-line bg-paper p-4">
        <div className="mx-auto max-w-56">
          <Slot label="Abraham" value={null} active={false} shaking={false} onTap={() => {}} tone="fixed" />
          {line}
          {slot(0)}
          {line}
          {slot(1)}
          {line}
          {slot(2)}
          {line}
          <Slot label="King David" value={null} active={false} shaking={false} onTap={() => {}} tone="fixed" />
        </div>
        <div className="mx-auto mt-0 h-4 w-0.5 bg-navy/40" aria-hidden />
        <div className="mx-auto h-0.5 w-1/2 bg-navy/40" aria-hidden />
        <div className="grid grid-cols-2 gap-3">
          <div>
            <p className="mt-2 text-center font-sans text-[10px] font-extrabold uppercase tracking-[0.14em] text-gold-deep">Legal right · Matthew 1</p>
            {line}
            {slot(3)}
            {line}
            {slot(5)}
          </div>
          <div>
            <p className="mt-2 text-center font-sans text-[10px] font-extrabold uppercase tracking-[0.14em] text-gold-deep">Blood right · Luke 3</p>
            {line}
            {slot(4)}
            {line}
            {slot(6)}
          </div>
        </div>
        <div className="mx-auto h-0.5 w-1/2 bg-navy/40" aria-hidden />
        <div className="mx-auto h-4 w-0.5 bg-navy/40" aria-hidden />
        <div className="mx-auto max-w-56">
          <Slot label="Yeshua" value={null} active={false} shaking={false} onTap={() => {}} tone="fixed" />
        </div>
      </div>
      <Banner done={s.done} total={slots.length} label="Yeshua’s family tree is complete." onReset={s.reset} />
    </div>
  );
}

/* ---------- word search ---------- */

const FOUND = ["#f7dd5c", "#9ad19a", "#7cc3ea", "#f2a3b3", "#c9b2ea", "#f5b97a"];

export function WordSearch({ id, grid, words }: { id: string; grid: string[][]; words: string[] }) {
  const [found, setFound] = useSaved<{ word: string; cells: number[] }[]>(`botk:game:${id}`, []);
  const [start, setStart] = useState<number | null>(null);
  const [hover, setHover] = useState<number | null>(null);
  const [shaking, shake] = useShake();
  const box = useRef<HTMLDivElement>(null);
  const W = grid[0].length;
  const H = grid.length;

  const line = useCallback(
    (a: number, b: number) => {
      const [r1, c1, r2, c2] = [Math.floor(a / W), a % W, Math.floor(b / W), b % W];
      const dr = Math.sign(r2 - r1);
      const dc = Math.sign(c2 - c1);
      const n = Math.max(Math.abs(r2 - r1), Math.abs(c2 - c1));
      if (!(r1 === r2 || c1 === c2 || Math.abs(r2 - r1) === Math.abs(c2 - c1))) return null;
      return Array.from({ length: n + 1 }, (_, i) => (r1 + dr * i) * W + (c1 + dc * i));
    },
    [W],
  );

  const preview = useMemo(() => (start !== null && hover !== null ? line(start, hover) || [] : start !== null ? [start] : []), [start, hover, line]);

  const finish = (end: number) => {
    if (start === null) return;
    if (end === start) return; // first tap: wait for the second
    const cells = line(start, end);
    setStart(null);
    setHover(null);
    if (!cells) return shake("grid");
    const word = cells.map((i) => grid[Math.floor(i / W)][i % W]).join("");
    const hit = words.find((w) => (w === word || w === [...word].reverse().join("")) && !found.some((f) => f.word === w));
    if (!hit) return shake("grid");
    const next = [...found, { word: hit, cells }];
    setFound(next);
    if (next.length === words.length) celebrate(box.current);
    else {
      chimeRight();
    }
  };

  const cellAt = (x: number, y: number) => {
    const el = document.elementFromPoint(x, y) as HTMLElement | null;
    const v = el?.dataset?.cell;
    return v === undefined ? null : Number(v);
  };

  const color = (i: number) => {
    const f = found.findIndex((x) => x.cells.includes(i));
    return f >= 0 ? FOUND[f % FOUND.length] : undefined;
  };

  return (
    <div ref={box} className="mt-5">
      <p className="font-sans text-sm font-bold text-navy">Drag across a word, or tap its first letter and then its last letter.</p>
      <div className="mt-3 grid gap-4 lg:grid-cols-[1fr_220px]">
        <div
          className={`mx-auto grid w-full max-w-[560px] touch-none select-none gap-0.5 rounded-2xl bg-navy p-2 ${shaking === "grid" ? "shake" : ""}`}
          style={{ gridTemplateColumns: `repeat(${W}, minmax(0, 1fr))` }}
          onPointerMove={(e) => {
            if (start === null) return;
            const c = cellAt(e.clientX, e.clientY);
            if (c !== null) setHover(c);
          }}
          onPointerUp={(e) => {
            const c = cellAt(e.clientX, e.clientY);
            if (c !== null) finish(c);
          }}
          role="grid"
          aria-label="Word search"
        >
          {grid.flat().map((ch, i) => {
            const bg = color(i);
            const on = preview.includes(i);
            return (
              <div
                key={i}
                data-cell={i}
                role="gridcell"
                onPointerDown={(e) => {
                  (e.target as HTMLElement).releasePointerCapture?.(e.pointerId);
                  if (start === null) setStart(i);
                }}
                className={`grid aspect-square place-items-center rounded-md font-sans text-[clamp(12px,3.6vw,20px)] font-extrabold ${on ? "bg-gold text-navy" : "text-navy"}`}
                style={!on ? { background: bg || "#fffdf7" } : undefined}
              >
                {ch}
              </div>
            );
          })}
        </div>
        <ul className="flex flex-wrap content-start gap-2 lg:flex-col">
          {words.map((w) => {
            const f = found.findIndex((x) => x.word === w);
            return (
              <li
                key={w}
                className={`rounded-full px-3 py-1 font-sans text-sm font-bold ${f >= 0 ? "text-navy line-through" : "bg-white text-navy ring-1 ring-navy/15"}`}
                style={f >= 0 ? { background: FOUND[f % FOUND.length] } : undefined}
              >
                {w}
              </li>
            );
          })}
        </ul>
      </div>
      <p className="sr-only">Grid has {H} rows.</p>
      <Banner done={found.length} total={words.length} label="Every word found." onReset={() => setFound([])} />
    </div>
  );
}

/* ---------- maze ---------- */

export function Maze({ id, svg }: { id: string; svg: string }) {
  const box = useRef<HTMLDivElement>(null);
  const [won, setWon] = useSaved<boolean>(`botk:game:${id}`, false);
  return (
    <div ref={box} className="mt-5">
      <p className="font-sans text-sm font-bold text-navy">Draw a path with your finger from the fields to Bethlehem.</p>
      <div className="mt-3">
        <DrawPad id={`${id}.path`} label="The way to Bethlehem" background={<div className="h-full w-full [&>svg]:h-full [&>svg]:w-full" dangerouslySetInnerHTML={{ __html: svg }} />} aspect="690 / 552" />
      </div>
      <button
        onClick={() => {
          setWon(true);
          celebrate(box.current);
        }}
        className="mt-3 inline-flex min-h-12 items-center gap-2 rounded-full bg-gold px-5 font-sans font-extrabold text-navy"
      >
        <Sparkles size={18} aria-hidden /> {won ? "Made it to Bethlehem!" : "I made it!"}
      </button>
    </div>
  );
}

/* ---------- tracing and letters ---------- */

export function Trace({ id, text, rtl, rows, lead }: { id: string; text: string; rtl: boolean; rows: number; lead: string }) {
  const guide = (
    <svg viewBox="0 0 566 92" preserveAspectRatio="none" className="h-full w-full" aria-hidden>
      <line x1="0" y1={rtl ? 16 : 26} x2="566" y2={rtl ? 16 : 26} stroke="#9aa0ae" strokeWidth="1.3" />
      <line x1="0" y1={rtl ? 46 : 39} x2="566" y2={rtl ? 46 : 39} stroke="#b9bdc8" strokeWidth="1.1" strokeDasharray="6 5" />
      <line x1="0" y1={rtl ? 76 : 74} x2="566" y2={rtl ? 76 : 74} stroke="#5d6372" strokeWidth="1.6" />
      <text x="283" y={rtl ? 76 : 74} textAnchor="middle" fontSize={rtl ? 84 : 64} fill="#cdd2dc" fontFamily={rtl ? "serif" : "Inter, sans-serif"} fontWeight="700">
        {text}
      </text>
    </svg>
  );
  return (
    <div className="mt-5">
      <p className="font-sans text-sm font-bold text-navy">{lead || `Trace ${rtl ? "His name in Hebrew" : "the name"} with your finger.`}</p>
      <div className="mt-2 grid gap-3">
        {Array.from({ length: Math.min(rows, 2) }).map((_, i) => (
          <DrawPad key={i} id={`${id}.${i}`} label={i === 0 ? `Trace: ${text}` : "Once more!"} background={guide} aspect="566 / 92" thick />
        ))}
      </div>
    </div>
  );
}

export function Letters({ items }: { items: { char: string; name: string }[] }) {
  const say = (t: string) => {
    if (!("speechSynthesis" in window)) return;
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(t.split("·")[0].trim());
    u.rate = 0.85;
    window.speechSynthesis.speak(u);
  };
  return (
    <div className="mt-5">
      <p className="font-sans text-sm font-bold text-navy">Hebrew reads from right to left. Tap a letter to hear its name.</p>
      <ul className="mt-3 grid grid-cols-4 gap-2" dir="rtl">
        {items.map((l) => (
          <li key={l.char}>
            <button onClick={() => say(l.name)} className="flex w-full flex-col items-center gap-1 rounded-2xl border-2 border-navy/10 bg-white py-3 transition-transform active:scale-95">
              <span className="font-serif text-5xl text-navy" lang="he">{l.char}</span>
              <span className="flex items-center gap-1 font-sans text-xs font-bold text-muted" dir="ltr">
                <Volume2 size={12} aria-hidden /> {l.name}
              </span>
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
