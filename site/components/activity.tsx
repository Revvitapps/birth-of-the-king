"use client";
import Image from "next/image";
import { useEffect, useRef, useState } from "react";
import { Check, X } from "lucide-react";
import type { Activity as A, Block } from "@/lib/book";
import { img, pageImg } from "@/lib/book";
import { Md } from "@/components/md";
import { DrawPad } from "@/components/draw-pad";
import { MatchGame, OrderGame, FillGame, TreeGame, WordSearch, Maze, Trace, Letters } from "@/components/games";
import { chimeWrong, smallWin, celebrate } from "@/lib/fun";

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

function Choice({ id, q, options, answer, onRight }: { id: string; q: string; options: string[]; answer?: number; onRight?: () => void }) {
  const [v, set] = useAnswer(`botk:ans:${id}`);
  const [shake, setShake] = useState<number | null>(null);
  const [miss, setMiss] = useState<number[]>([]);
  const checks = answer !== undefined;
  const solved = checks && v === String(answer);
  return (
    <div role="radiogroup" aria-label={q} className="mt-2 flex flex-wrap gap-2">
      {options.map((o, i) => {
        const on = v === String(i);
        const right = checks && on && i === answer;
        const wrong = checks && miss.includes(i) && !solved;
        return (
          <button
            key={i}
            role="radio"
            aria-checked={on}
            disabled={solved && !on}
            onClick={(e) => {
              if (!checks) return set(on ? "" : String(i));
              if (solved) return;
              if (i === answer) {
                set(String(i));
                smallWin(e.currentTarget);
                onRight?.();
              } else {
                chimeWrong();
                setMiss((m) => [...m, i]);
                setShake(i);
                setTimeout(() => setShake(null), 420);
              }
            }}
            className={`flex min-h-12 items-center gap-2 rounded-2xl border-2 px-3 py-2 text-left font-serif text-base transition-colors ${
              right
                ? "pop border-emerald-600 bg-emerald-600 text-white"
                : wrong
                  ? "border-red-300 bg-red-50 text-ink/60"
                  : on
                    ? "border-navy bg-navy text-white"
                    : "border-navy/15 bg-paper text-ink hover:border-navy/50"
            } ${shake === i ? "shake" : ""} disabled:opacity-50`}
          >
            <span className={`grid h-7 w-7 shrink-0 place-items-center rounded-full font-sans text-xs font-extrabold ${right ? "bg-white text-emerald-700" : wrong ? "bg-red-200 text-red-800" : on ? "bg-gold text-navy" : "bg-navy/10 text-navy"}`}>
              {right ? <Check size={16} aria-hidden /> : wrong ? <X size={16} aria-hidden /> : String.fromCharCode(65 + i)}
            </span>
            <Md text={o} />
            {wrong && <span className="sr-only">(not this one)</span>}
          </button>
        );
      })}
      {checks && <span aria-live="polite" className="sr-only">{solved ? "Correct!" : miss.length ? "Try again" : ""}</span>}
    </div>
  );
}

function Quiz({ id, b }: { id: string; b: Extract<Block, { k: "mc" }> }) {
  const box = useRef<HTMLOListElement>(null);
  const checkable = b.items.filter((it) => it.options && it.answer !== undefined).length;
  const count = () => {
    let n = 0;
    b.items.forEach((it, i) => {
      try {
        if (it.options && it.answer !== undefined && localStorage.getItem(`botk:ans:${id}.${i}`) === String(it.answer)) n++;
      } catch {}
    });
    return n;
  };
  const [got, setGot] = useState(0);
  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect -- hydrate from device storage
    setGot(count());
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [id]);
  const onRight = () => {
    const n = count();
    setGot(n);
    if (n === checkable) setTimeout(() => celebrate(box.current), 250);
  };
  return (
    <>
      <ol ref={box} className="mt-4 space-y-6">
        {b.items.map((it, i) => (
          <li key={i} className="grid grid-cols-[2rem_1fr] gap-x-2">
            <span className="font-sans text-lg font-extrabold text-gold-deep">{b.start + i}.</span>
            <div>
              <p className="font-serif text-lg text-ink"><Md text={it.text} /></p>
              {it.options ? (
                <Choice id={`${id}.${i}`} q={it.text} options={it.options} answer={it.answer} onRight={onRight} />
              ) : (
                <Answer id={`${id}.${i}`} lines={it.lines || 1} label={it.text} />
              )}
            </div>
          </li>
        ))}
      </ol>
      {checkable > 0 && (
        <div className="mt-5 flex items-center gap-3 rounded-2xl bg-navy px-4 py-3 text-white" aria-live="polite">
          <span className="flex gap-0.5 text-xl" aria-hidden>
            {Array.from({ length: checkable }).map((_, i) => (
              <span key={i} className={i < got ? "text-gold" : "text-white/25"}>★</span>
            ))}
          </span>
          <span className="font-sans text-sm font-bold">
            {got === checkable ? "All right! Well done!" : `${got} of ${checkable} stars`}
          </span>
        </div>
      )}
    </>
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
          {b.lines > 0 && <Answer id={id} lines={b.lines} label={b.text} />}
          {b.draw && <div className="mt-3"><DrawPad id={`${id}.d`} label={b.draw} /></div>}
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
      return <Quiz id={id} b={b} />;
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
    case "wordsearch":
      return <WordSearch id={id} grid={b.grid} words={b.words} />;
    case "maze":
      return <Maze id={id} svg={b.svg} />;
    case "match":
      if (b.answer && b.answer.length === b.left.length && b.answer.every((x) => x >= 0))
        return <MatchGame id={id} left={b.left} right={b.right} answer={b.answer} />;
      return (
        <div className="mt-4 grid gap-2 sm:grid-cols-2">
          <ol className="space-y-2">{b.left.map((l, i) => <li key={i} className="rounded-xl bg-white p-3 ring-1 ring-line"><Md text={l} /></li>)}</ol>
          <ol className="space-y-2">{b.right.map((r, i) => <li key={i} className="rounded-xl bg-paper p-3 ring-1 ring-line"><Md text={r} /></li>)}</ol>
        </div>
      );
    case "order":
      return b.answer ? (
        <>
          {b.lead && <p className="mt-5 font-serif text-lg font-bold text-ink"><Md text={b.lead} /></p>}
          <OrderGame id={id} items={b.items} answer={b.answer} />
        </>
      ) : (
        <ul className="mt-4 space-y-2">{b.items.map((it) => <li key={it.letter} className="rounded-xl bg-white p-3 ring-1 ring-line"><b>{it.letter}.</b> <Md text={it.text} /></li>)}</ul>
      );
    case "fill":
      return b.answer && b.bank ? (
        <FillGame id={id} rows={b.rows} answer={b.answer} bank={b.bank} />
      ) : (
        <div>{b.rows.map((r, i) => <div key={i} className="mt-4"><p className="font-serif text-lg"><Md text={r} /></p><Answer id={`${id}.${i}`} lines={1} label={r} /></div>)}</div>
      );
    case "tree":
      return b.slots && b.bank ? <TreeGame id={id} slots={b.slots} bank={b.bank} /> : null;
    case "trace":
      return <Trace id={id} text={b.text} rtl={b.rtl} rows={b.rows} lead={b.lead} />;
    case "letters":
      return <Letters items={b.items} />;
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
