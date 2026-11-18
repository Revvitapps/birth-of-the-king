import type { Metadata } from "next";
import Link from "next/link";
import Image from "next/image";
import { notFound } from "next/navigation";
import { Printer } from "lucide-react";
import type { Activity, Coloring as C, Reading, Lesson } from "@/lib/book";
import { getStep, img, keysFor, lessons, stepHref, stepLabel } from "@/lib/book";
import { hasAccess } from "@/lib/access";
import { Md, Paras, plain } from "@/components/md";
import { ReadAloud } from "@/components/read-aloud";
import { MarkDone } from "@/components/progress";
import { ModeToggle } from "@/components/mode-toggle";
import { NotesBox } from "@/components/notes-box";
import { StepNav } from "@/components/step-nav";
import { Coloring } from "@/components/coloring";
import { ActivityView } from "@/components/activity";
import { Locked } from "@/components/locked";

export function generateStaticParams() {
  return lessons.flatMap((l) => l.steps.map((s) => ({ num: String(l.num), slug: s.slug })));
}

export async function generateMetadata({ params }: PageProps<"/lessons/[num]/[slug]">): Promise<Metadata> {
  const { num, slug } = await params;
  const r = getStep(Number(num), slug);
  if (!r) return {};
  const desc = r.step.kind === "reading" ? plain(r.step.paras[0]).slice(0, 160) : `${stepLabel(r.step)} from Lesson ${num}: ${r.lesson.title}`;
  return { title: r.step.title, description: desc };
}

const norm = (s: string) => s.toLowerCase().replace(/[^a-z]/g, "");

function Head({ l, kicker, title, children }: { l: Lesson; kicker: string; title: string; children?: React.ReactNode }) {
  return (
    <header className="bg-navy text-white">
      <div className="px-site mx-auto max-w-6xl pb-8 pt-12">
        <Link href={`/lessons/${l.num}`} className="inline-flex min-h-11 items-center font-sans text-sm font-bold text-gold-soft hover:text-white">
          ← Lesson {l.num}: {l.title}
        </Link>
        <p className="kicker mt-4 text-gold">{kicker}</p>
        <h1 className="display mt-2 text-[clamp(2rem,6vw,3.6rem)]"><Md text={title} /></h1>
        <div className="mt-3 h-1 w-20 bg-gold" />
        {children}
      </div>
    </header>
  );
}

function ReadingView({ l, s, id }: { l: Lesson; s: Reading; id: string }) {
  const speak = [s.title, ...(s.verse ? [`${s.verse}. ${s.vref}.`] : []), ...s.paras.map(plain)];
  return (
    <article className="lg:grid lg:grid-cols-[minmax(0,0.9fr)_minmax(0,1.1fr)]">
      {s.art && (
        <div className="relative h-[68svh] overflow-hidden bg-night lg:sticky lg:top-0 lg:h-svh">
          <Image
            src={img(s.art.img)}
            alt={s.art.cap ? plain(s.art.cap) : ""}
            fill
            priority
            sizes="(min-width: 1024px) 45vw, 100vw"
            className={`${s.art.contain ? "object-contain p-4" : "drift object-cover"}`}
          />
          <div className="absolute inset-x-0 bottom-0 h-40 bg-gradient-to-t from-night/90 to-transparent lg:hidden" />
          {s.art.cap && (
            <p className="absolute bottom-4 left-4 right-4 font-serif text-base italic text-white lg:bottom-6 lg:left-6 lg:right-auto lg:max-w-[80%] lg:rounded-full lg:bg-white lg:px-4 lg:py-1.5 lg:font-sans lg:text-sm lg:font-bold lg:not-italic lg:text-navy">
              <Md text={s.art.cap} />
            </p>
          )}
          <Link href={`/lessons/${l.num}`} className="absolute left-3 top-3 inline-flex min-h-11 items-center rounded-full bg-night/60 px-4 font-sans text-sm font-bold text-white backdrop-blur lg:hidden">
            ← Lesson {l.num}
          </Link>
        </div>
      )}
      <div className="min-w-0">
        <div className="bg-navy text-white">
          <div className="px-site max-w-3xl pb-8 pt-10">
            <Link href={`/lessons/${l.num}`} className="hidden min-h-11 items-center font-sans text-sm font-bold text-gold-soft hover:text-white lg:inline-flex">
              ← Lesson {l.num}: {l.title}
            </Link>
            <p className="kicker mt-2 text-gold">{s.kicker}</p>
            <h1 className="display mt-2 text-[clamp(2rem,5.5vw,3.4rem)]"><Md text={s.title} /></h1>
            <div className="mt-3 h-1 w-20 bg-gold" />
            {s.verse && (
              <blockquote className="mt-5 font-serif text-lg italic text-gold-soft">
                “<Md text={s.verse} />” <span className="not-italic font-bold text-white">({s.vref})</span>
              </blockquote>
            )}
            {s.read && <p className="mt-3 font-sans text-sm font-semibold text-white/80">Read together: <Md text={s.read} /></p>}
            <div className="mt-5 flex flex-wrap gap-2">
              <ReadAloud text={speak} />
              <ModeToggle />
            </div>
          </div>
        </div>
        <div className="px-site max-w-3xl py-8">
          <Paras paras={s.paras} />
          {s.figs && s.figs.length > 0 && (
            <div className="my-8 grid gap-3 sm:grid-cols-2">
              {s.figs.map((f) => (
                <figure key={f.img} className="overflow-hidden rounded-xl border border-line bg-white">
                  <Image src={img(f.img)} alt={plain(f.cap)} width={1200} height={900} sizes="(min-width: 640px) 40vw, 100vw" className="h-auto w-full" />
                  {f.cap && <figcaption className="px-3 py-2 font-sans text-xs font-semibold text-muted"><Md text={f.cap} /></figcaption>}
                </figure>
              ))}
            </div>
          )}
          {s.callout && (
            <div className="my-8 rounded-2xl border-l-4 border-gold bg-gold-soft/50 p-5">
              <p className="font-sans text-sm font-extrabold uppercase tracking-[0.18em] text-navy"><Md text={s.callout.title} /></p>
              {s.callout.body.map((b, i) => <p key={i} className="mt-2 font-serif text-lg"><Md text={b} /></p>)}
            </div>
          )}
          {s.notes && (
            <aside className="teacher-only my-10 rounded-2xl border-l-[6px] border-gold bg-paper p-5 shadow-sm" aria-label="Teaching Nuggets">
              <p className="kicker text-gold-deep">Teaching Nuggets</p>
              <div className="mt-2 space-y-4">
                {s.notes.map((n, i) => (
                  <div key={i}>
                    {n.h && <h3 className="font-sans text-base font-extrabold text-navy"><Md text={n.h} /></h3>}
                    {n.t.split("\n").map((t, j) => <p key={j} className="mt-1 font-serif text-base leading-relaxed"><Md text={t} /></p>)}
                  </div>
                ))}
              </div>
              <div className="mt-6"><NotesBox id={id} /></div>
            </aside>
          )}
          <div className="mt-6"><MarkDone id={id} /></div>
        </div>
      </div>
    </article>
  );
}

function ColoringStep({ l, s, id }: { l: Lesson; s: C; id: string }) {
  return (
    <>
      <Head l={l} kicker={`${s.kick} · Lesson ${l.num}`} title={s.title}>
        <p className="mt-4 max-w-2xl font-serif text-lg text-white/85">Pick a color, then tap any space in the picture to fill it. Your picture saves on this device.</p>
      </Head>
      <div className="px-site mx-auto max-w-6xl py-8">
        <Coloring src={img(s.img)} id={id} title={s.title} />
        {s.caption && <p className="mt-4 font-serif text-lg"><Md text={s.caption} /></p>}
        <div className="mt-6"><MarkDone id={id} /></div>
      </div>
    </>
  );
}

function ActivityStep({ l, s, id }: { l: Lesson; s: Activity; id: string }) {
  const key = keysFor(l.num).find((k) => norm(k.title) === norm(s.title));
  return (
    <>
      <Head l={l} kicker={`${s.kick} · Lesson ${l.num}`} title={s.title}>
        <div className="mt-5 flex items-start gap-4">
          {s.ins && <p className="max-w-2xl flex-1 font-serif text-lg text-white/90"><Md text={s.ins} /></p>}
          {s.sketch && (
            <div className="hidden h-28 w-28 shrink-0 rounded-xl bg-cream p-2 sm:block">
              <Image src={img(s.sketch)} alt="" width={200} height={200} className="h-full w-full object-contain" />
            </div>
          )}
        </div>
        <div className="mt-5 flex flex-wrap gap-2">
          <ModeToggle />
          <a href={`/pages/p${String(s.page).padStart(3, "0")}.jpg`} target="_blank" rel="noopener" className="inline-flex min-h-11 items-center gap-2 rounded-full border border-white/25 px-4 font-sans text-sm font-bold">
            <Printer size={16} aria-hidden /> Printable page
          </a>
        </div>
      </Head>
      <div className="px-site mx-auto max-w-3xl py-8">
        <ActivityView a={s} id={id} />
        {key && (
          <details className="teacher-only mt-10 rounded-2xl border border-gold/50 bg-gold-soft/30 p-5">
            <summary className="min-h-11 cursor-pointer font-sans text-sm font-extrabold uppercase tracking-[0.18em] text-navy">Answer key</summary>
            <ol className="mt-2 list-decimal pl-5 font-serif text-lg">{key.answers.map((a, i) => <li key={i}><Md text={a} /></li>)}</ol>
          </details>
        )}
        <div className="mt-6"><MarkDone id={id} /></div>
      </div>
    </>
  );
}

export default async function StepPage({ params }: PageProps<"/lessons/[num]/[slug]">) {
  const { num: n, slug } = await params;
  const num = Number(n);
  const r = getStep(num, slug);
  if (!r) notFound();
  const { lesson: l, step: s, index, prev, next } = r;
  const id = `${num}/${s.slug}`;
  const open = await hasAccess(num);

  if (!open)
    return (
      <main>
        <Head l={l} kicker={`${stepLabel(s)} · Lesson ${num}`} title={s.title} />
        <div className="px-site mx-auto max-w-3xl py-8">
          {s.kind === "reading" && <p className="mb-6 font-serif text-xl leading-relaxed"><Md text={s.paras[0]} /></p>}
          <Locked num={num} next={stepHref(num, s.slug)} />
        </div>
      </main>
    );

  return (
    <main>
      {s.kind === "reading" && <ReadingView l={l} s={s} id={id} />}
      {s.kind === "color" && <ColoringStep l={l} s={s} id={id} />}
      {s.kind === "activity" && <ActivityStep l={l} s={s} id={id} />}
      <StepNav
        id={id}
        index={index}
        total={l.steps.length}
        lessonHref={`/lessons/${num}`}
        prev={prev ? { href: stepHref(num, prev.slug), title: prev.title } : null}
        next={next ? { href: stepHref(num, next.slug), title: next.title } : null}
      />
    </main>
  );
}
