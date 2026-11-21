"use client";
import { useEffect, useState } from "react";

// The book's ruled "Notes" box, kept on this device.
export function NotesBox({ id, label = "Notes" }: { id: string; label?: string }) {
  const key = `botk:note:${id}`;
  const [v, setV] = useState("");
  useEffect(() => {
    try {
      // eslint-disable-next-line react-hooks/set-state-in-effect -- hydrate from device storage
      setV(localStorage.getItem(key) || "");
    } catch {}
  }, [key]);
  return (
    <label className="block">
      <span className="kicker text-gold-deep">{label}</span>
      <textarea
        value={v}
        onChange={(e) => {
          setV(e.target.value);
          try { localStorage.setItem(key, e.target.value); } catch {}
        }}
        rows={4}
        placeholder="Your notes for this reading stay on this device."
        className="ruled mt-2 block w-full resize-y rounded-lg border border-line bg-paper px-3 font-serif text-base text-ink placeholder:text-muted/70"
      />
    </label>
  );
}
