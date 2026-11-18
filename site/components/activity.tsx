"use client";
import Image from "next/image";
import { useEffect, useState } from "react";
import type { Activity as A, Block } from "@/lib/book";
import { img, pageImg } from "@/lib/book";
import { Md } from "@/components/md";
import { DrawPad } from "@/components/draw-pad";

function useAnswer(key: string) {
  const [v, setV] = useState("");
  useEffect(() => {
    try {
      // eslint-disable-next-line react-hooks/set-state-in-effect -- hydrate from device storage
      setV(localStorage.getItem(key) || "");
    } catch {}
  }, [key]);
  const set = (x: string) => {
    setV(x);
    try { localStorage.setItem(key, x); } catch {}
  };
  return [v, set] as const;
}

function Answer({ id, lines, label }: { id: string; lines: number; label: string }) {
  const [v, set] = useAnswer(`botk:ans:${id}`);
  return (
    <textarea
      aria-label={label}
      value={v}
      onChange={(e) => set(e.target.value)}
      rows={Math.max(1, lines)}
      className="ruled mt-1 block w-full resize-y rounded-md border-0 bg-transparent px-1 font-serif text-lg text-navy"
      style={{ minHeight: `${Math.max(1, lines) * 2.2 + 0.2}rem` }}
    />
  );
}

function Choice({ id, q, options }: { id: string; q: string; options: string[] }) {
  const [v, set] = useAnswer(`botk:ans:${id}`);
  return (
    <div role="radiogroup" aria-label={q} className="mt-2 flex flex-wrap gap-2">
      {options.map((o, i) => {
        const on = v === String(i);
        return (
          <button
            key={i}
            role="radio"
            aria-checked={on}
            onClick={() => set(on ? "" : String(i))}
            className={`flex min-h-11 items-center gap-2 rounded-full border px-3 py-1.5 text-left font-serif text-base transition-colors ${on ? "border-navy bg-navy text-white" : "border-navy/20 bg-paper text-ink hover:border-navy/50"}`}
          >
            <span className={`grid h-6 w-6 shrink-0 place-items-center rounded-full font-sans text-xs font-extrabold ${on ? "bg-gold text-navy" : "bg-navy/10 text-navy"}`}>
              {String.fromCharCode(65 + i)}
            </span>
            <Md text={o} />
          </button>
        );
      })}
    </div>
  );
}

function BlockView({ b, id, page, title }: { b: Block; id: string; page: number; title: string }) {
  switch (b.k) {
    case "part":
      return <h3 className="mt-6 border-b-2 border-gold pb-1 font-sans text-base font-extrabold text-navy"><Md text={b.text} /></h3>;
    case "q":
      return (
        <div className="mt-5">
          <p className="font-serif text-lg font-bold text-ink"><Md text={b.text} /></p>
          <Answer id={id} lines={b.lines} label={b.text} />
        </div>
      );
    case "lines":
      return <Answer id={id} lines={b.lines} label="Your answer" />;
    case "qs":
      return (
        <ol className="mt-4 space-y-5">
          {b.items.map((it, i) => (
            <li key={i} className="grid grid-cols-[2rem_1fr] gap-x-2">
              <span className="font-sans text-lg font-extrabold text-gold-deep">{i + 1}.</span>
              <div>
                <p className="font-serif text-lg text-ink"><Md text={it.text} /></p>
                <Answer id={`${id}.${i}`} lines={it.lines} label={it.text} />
              </div>
            </li>
          ))}
        </ol>
      );
    case "mc":
      return (
        <ol className="mt-4 space-y-6">
          {b.items.map((it, i) => (
            <li key={i} className="grid grid-cols-[2rem_1fr] gap-x-2">
              <span className="font-sans text-lg font-extrabold text-gold-deep">{b.start + i}.</span>
              <div>
                <p className="font-serif text-lg text-ink"><Md text={it.text} /></p>
                {it.options ? <Choice id={`${id}.${i}`} q={it.text} options={it.options} /> : <Answer id={`${id}.${i}`} lines={it.lines || 1} label={it.text} />}
              </div>
            </li>
          ))}
        </ol>
      );
    case "read":
      return (
        <div className="mt-4 rounded-xl border-l-4 border-gold bg-gold-soft/50 p-4 font-serif text-lg leading-relaxed">
          {b.paras.map((p, i) => <p key={i} className="mb-2 last:mb-0"><Md text={p} /></p>)}
        </div>
      );
    case "box":
      return <div className="mt-5"><DrawPad id={id} label={b.label} /></div>;
    case "grid4":
      return (
        <div className="mt-4 grid gap-4 sm:grid-cols-2">
          {b.cells.map((c, i) => <DrawPad key={i} id={`${id}.${i}`} label={c} />)}
        </div>
      );
    case "bank":
      return (
        <div className="mt-4 flex flex-wrap items-center gap-2 rounded-xl bg-navy/5 p-3">
          <span className="kicker text-navy">Word bank</span>
          {b.words.map((w) => <span key={w} className="rounded-full bg-white px-3 py-1 font-sans text-sm font-semibold text-navy ring-1 ring-navy/15"><Md text={w} /></span>)}
        </div>
      );
    case "img":
      return (
        <div className="mt-5 overflow-hidden rounded-xl border border-line bg-white">
          <Image src={img(b.img)} alt="" width={1200} height={900} sizes="(min-width: 1024px) 760px, 100vw" className="h-auto w-full" />
        </div>
      );
    case "printed":
      return (
        <figure className="mt-5 overflow-hidden rounded-xl border border-line bg-white shadow-sm">
          <Image src={pageImg(page)} alt={`Printed page: ${title}`} width={1224} height={1584} sizes="(min-width: 1024px) 760px, 100vw" className="h-auto w-full" />
          <figcaption className="border-t border-line bg-paper px-4 py-2 font-sans text-xs text-muted">
            This part is made for paper. Print the page, or work on it together on screen.
          </figcaption>
        </figure>
      );
  }
}

export function ActivityView({ a, id }: { a: A; id: string }) {
  // a page with print-only parts shows the printed page once, after the interactive parts
  const blocks = a.blocks.filter((b) => b.k !== "printed");
  return (
    <div>
      {blocks.map((b, i) => <BlockView key={i} b={b} id={`${id}.${i}`} page={a.page} title={a.title} />)}
      {a.printed && <BlockView b={{ k: "printed" }} id={`${id}.p`} page={a.page} title={a.title} />}
    </div>
  );
}
