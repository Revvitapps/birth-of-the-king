"use client";
import { useEffect, useState, useSyncExternalStore } from "react";
import { Check } from "lucide-react";

const KEY = "botk:done";
const listeners = new Set<() => void>();

function read(): string[] {
  try {
    return JSON.parse(localStorage.getItem(KEY) || "[]");
  } catch {
    return [];
  }
}
let cache: string[] | null = null;
const snapshot = () => (cache ??= read());
const subscribe = (fn: () => void) => {
  listeners.add(fn);
  return () => listeners.delete(fn);
};
const EMPTY: string[] = [];

export function useDone() {
  return useSyncExternalStore(subscribe, snapshot, () => EMPTY);
}

export function markDone(id: string, on = true) {
  const cur = new Set(read());
  if (on) cur.add(id);
  else cur.delete(id);
  cache = [...cur];
  try {
    localStorage.setItem(KEY, JSON.stringify(cache));
  } catch {}
  listeners.forEach((l) => l());
  if (on) window.dispatchEvent(new Event("botk:keyaction"));
}

export function DoneTick({ id }: { id: string }) {
  const done = useDone().includes(id);
  return done ? (
    <span className="grid h-6 w-6 shrink-0 place-items-center rounded-full bg-gold text-navy" aria-label="Done">
      <Check size={14} strokeWidth={3} />
    </span>
  ) : (
    <span className="h-6 w-6 shrink-0 rounded-full border-2 border-line" aria-hidden />
  );
}

export function LessonMeter({ num, ids }: { num: number; ids: string[] }) {
  const done = useDone();
  const n = ids.filter((i) => done.includes(i)).length;
  return (
    <div className="font-sans text-xs font-semibold" aria-label={`Lesson ${num}: ${n} of ${ids.length} stars`}>
      <div className="flex flex-wrap gap-0.5 text-lg leading-none" aria-hidden>
        {ids.map((id) => (
          <span key={id} className={done.includes(id) ? "text-gold drop-shadow" : "opacity-25"}>★</span>
        ))}
      </div>
      <span className="mt-1 block opacity-80">{n === ids.length ? "Every star collected!" : `${n} of ${ids.length} stars`}</span>
    </div>
  );
}

export function MarkDone({ id }: { id: string }) {
  const done = useDone().includes(id);
  const [pulse, setPulse] = useState(false);
  useEffect(() => {
    if (!pulse) return;
    const t = setTimeout(() => setPulse(false), 600);
    return () => clearTimeout(t);
  }, [pulse]);
  return (
    <button
      onClick={() => {
        markDone(id, !done);
        setPulse(!done);
      }}
      aria-pressed={done}
      className={`inline-flex min-h-11 items-center gap-2 rounded-full px-4 font-sans text-sm font-bold transition-transform ${done ? "bg-gold text-navy" : "border border-current/25"} ${pulse ? "scale-105" : ""}`}
    >
      <Check size={18} aria-hidden strokeWidth={3} />
      {done ? "Done" : "Mark as done"}
    </button>
  );
}
