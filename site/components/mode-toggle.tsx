"use client";
import { useEffect, useState } from "react";
import { GraduationCap, Sparkles } from "lucide-react";

export type Mode = "teacher" | "student";
const KEY = "botk:mode";

export const modeScript = `try{document.documentElement.dataset.mode=localStorage.getItem('${KEY}')||'teacher'}catch(e){document.documentElement.dataset.mode='teacher'}`;

// Teacher mode shows Teaching Nuggets, notes and answer keys. Kid mode hides them.
export function ModeToggle({ className = "" }: { className?: string }) {
  const [mode, setMode] = useState<Mode>("teacher");
  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect -- read the mode the head script already applied
    setMode((document.documentElement.dataset.mode as Mode) || "teacher");
  }, []);
  const set = (m: Mode) => {
    setMode(m);
    document.documentElement.setAttribute("data-mode", m);
    try { localStorage.setItem(KEY, m); } catch {}
  };
  return (
    <div role="group" aria-label="Who is reading" className={`inline-flex rounded-full border border-current/20 p-1 font-sans text-xs font-bold ${className}`}>
      {(["teacher", "student"] as const).map((m) => (
        <button
          key={m}
          aria-pressed={mode === m}
          onClick={() => set(m)}
          className={`flex min-h-9 items-center gap-1.5 rounded-full px-3 ${mode === m ? "bg-gold text-navy" : "opacity-80 hover:opacity-100"}`}
        >
          {m === "teacher" ? <GraduationCap size={15} aria-hidden /> : <Sparkles size={15} aria-hidden />}
          {m === "teacher" ? "Teacher" : "Kids"}
        </button>
      ))}
    </div>
  );
}
