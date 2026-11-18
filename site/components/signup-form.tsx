"use client";
import { useState } from "react";
import { Download, Loader2 } from "lucide-react";
import { upsertContact } from "@/lib/pipeline";

// Free Lesson 1 sample: email in, PDF out. Feeds the lead pipeline.
export function SignupForm({ source = "free-sample", dark = false }: { source?: string; dark?: boolean }) {
  const [email, setEmail] = useState("");
  const [role, setRole] = useState("Parent");
  const [state, setState] = useState<"idle" | "busy" | "done" | "error">("idle");
  const field = `min-h-12 w-full rounded-xl border px-4 font-sans text-base ${dark ? "border-white/25 bg-white/10 text-white placeholder:text-white/60" : "border-navy/20 bg-white text-ink"}`;

  if (state === "done")
    return (
      <div className={`rounded-2xl p-5 ${dark ? "bg-white/10" : "bg-gold-soft/60"}`}>
        <p className="font-sans text-lg font-extrabold">It’s yours.</p>
        <p className="mt-1 font-serif">The Lesson 1 student pack is ready to print.</p>
        <a
          href="/downloads/Birth-of-the-King-Lesson-1-Free-Sample.pdf"
          download
          className="mt-3 inline-flex min-h-11 items-center gap-2 rounded-full bg-gold px-5 font-sans text-sm font-extrabold text-navy"
        >
          <Download size={18} aria-hidden /> Download Lesson 1 pages
        </a>
      </div>
    );

  return (
    <form
      onSubmit={async (e) => {
        e.preventDefault();
        setState("busy");
        try {
          await upsertContact({ email, role, source });
          setState("done");
        } catch {
          setState("error");
        }
      }}
      className="grid gap-3 sm:grid-cols-[1fr_auto_auto]"
    >
      <label className="sr-only" htmlFor={`email-${source}`}>Email</label>
      <input id={`email-${source}`} type="email" required autoComplete="email" placeholder="Your email" value={email} onChange={(e) => setEmail(e.target.value)} className={field} />
      <label className="sr-only" htmlFor={`role-${source}`}>I teach as a</label>
      <select id={`role-${source}`} value={role} onChange={(e) => setRole(e.target.value)} className={`${field} sm:w-auto`}>
        <option>Parent</option>
        <option>Homeschool</option>
        <option>Sunday school</option>
        <option>Co-op</option>
        <option>Grandparent</option>
      </select>
      <button
        disabled={state === "busy"}
        className="inline-flex min-h-12 items-center justify-center gap-2 rounded-xl bg-gold px-6 font-sans text-base font-extrabold text-navy disabled:opacity-60"
      >
        {state === "busy" ? <Loader2 className="animate-spin" size={18} aria-hidden /> : null}
        Send me Lesson 1 free
      </button>
      {state === "error" && <p role="alert" className="font-sans text-sm text-red-700 sm:col-span-3">That didn’t go through. Check the email and try again.</p>}
    </form>
  );
}
