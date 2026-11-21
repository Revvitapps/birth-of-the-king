"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { KeyRound } from "lucide-react";

export function UnlockForm({ next }: { next?: string }) {
  const [attempt, setAttempt] = useState("");
  const [err, setErr] = useState(false);
  const router = useRouter();
  return (
    <form
      onSubmit={async (e) => {
        e.preventDefault();
        const r = await fetch("/api/unlock", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ attempt }) });
        if (r.ok) {
          router.push(next || "/lessons");
          router.refresh();
        } else setErr(true);
      }}
      className="flex flex-col gap-3 sm:flex-row"
    >
      <label htmlFor="code" className="sr-only">Access code</label>
      <input id="code" value={attempt} onChange={(e) => { setAttempt(e.target.value); setErr(false); }} placeholder="Access code from your receipt" autoCapitalize="characters"
        className="min-h-12 flex-1 rounded-xl border border-navy/20 bg-white px-4 font-sans text-base uppercase tracking-widest text-ink" />
      <button className="inline-flex min-h-12 items-center justify-center gap-2 rounded-xl bg-navy px-6 font-sans font-extrabold text-white">
        <KeyRound size={18} aria-hidden /> Unlock
      </button>
      {err && <p role="alert" className="font-sans text-sm text-red-700">That code didn’t match. Check your receipt email.</p>}
    </form>
  );
}
