import type { Metadata } from "next";
import Link from "next/link";
import Image from "next/image";
import { notFound } from "next/navigation";
import { ArrowRight, Lightbulb } from "lucide-react";
import { getLesson, img, keysFor, lessons, stepHref, stepLabel } from "@/lib/book";
import { hasAccess } from "@/lib/access";
import { Md } from "@/components/md";
import { StepIcon } from "@/components/step-icon";
import { DoneTick, LessonMeter } from "@/components/progress";
import { ModeToggle } from "@/components/mode-toggle";
import { VideoSlot } from "@/components/video-slot";
import { Locked } from "@/components/locked";
import { ReadAloud } from "@/components/read-aloud";
import { Footer } from "@/components/footer";

export function generateStaticParams() {
  return lessons.map((l) => ({ num: String(l.num) }));
}

export async function generateMetadata({ params }: PageProps<"/lessons/[num]">): Promise<Metadata> {
  const l = getLesson(Number((await params).num));
  return l ? { title: `Lesson ${l.num}: ${l.title}`, description: l.plan.overview } : {};
}

export default async function LessonPage({ params }: PageProps<"/lessons/[num]">) {
  const num = Number((await params).num);
  const l = getLesson(num);
  if (!l) notFound();
  const open = await hasAccess(num);
  const p = l.plan;
  const keys = keysFor(num);
  const ids = l.steps.map((s) => `${num}/${s.slug}`);

  return (
    <main>
      <section className="relative isolate overflow-hidden bg-night text-white">
        <Image src={img(l.cover)} alt="" fill priority sizes="100vw" className="drift -z-10 object-cover object-[50%_35%]" />
        <div className="absolute inset-0 -z-10 bg-gradient-to-t from-night via-night/50 to-night/20" />
        <div className="px-site mx-auto flex min-h-[62svh] max-w-6xl flex-col justify-end pb-10 pt-20">
          <Link href="/lessons" className="mb-auto inline-flex min-h-11 items-center font-sans text-sm font-bold text-gold-soft hover:text-white">← All lessons</Link>
          <p className="kicker text-gold">Lesson {num}</p>
          <h1 className="display mt-2 text-[clamp(2.6rem,9vw,5.5rem)]">{l.title}</h1>
          <p className="mt-3 font-serif text-lg italic text-gold-soft">{l.ref}</p>
          <div className="mt-6 flex flex-wrap items-center gap-3">
            {open && (
              <Link href={stepHref(num, l.steps[0].slug)} className="inline-flex min-h-12 items-center gap-2 rounded-full bg-gold px-6 font-sans font-extrabold text-navy">
                Start the lesson <ArrowRight size={18} aria-hidden />
              </Link>
            )}
            <ModeToggle className="text-white" />
          </div>
          <div className="mt-6 max-w-xs"><LessonMeter num={num} ids={ids} /></div>
        </div>
      </section>

      <div className="px-site mx-auto grid max-w-6xl gap-10 py-10 lg:grid-cols-[1.25fr_1fr]">
        <div>
          <p className="kicker text-gold-deep">Bible Lesson Overview</p>
          <p className="mt-3 font-serif text-xl leading-relaxed"><Md text={p.overview} /></p>
          <div className="mt-4"><ReadAloud text={[p.overview]} label="Listen" /></div>

          <div className="mt-8 rounded-2xl border-l-4 border-gold bg-gold-soft/50 p-5">
            <p className="flex items-center gap-2 font-sans text-sm font-extrabold uppercase tracking-[0.18em] text-navy"><Lightbulb size={16} aria-hidden /> Did you know?</p>
            <p className="mt-2 font-serif text-lg"><Md text={p.dyk} /></p>
          </div>

          <div className="mt-8"><VideoSlot num={num} title={l.title} /></div>

          <h2 className="display mt-10 text-2xl text-navy">In this lesson</h2>
          {open ? (
            <ol className="mt-4 divide-y divide-line rounded-2xl border border-line bg-paper">
              {l.steps.map((s, i) => (
                <li key={s.slug}>
                  <Link href={stepHref(num, s.slug)} className="flex min-h-16 items-center gap-3 px-4 py-3 hover:bg-gold-soft/30">
                    <span className="w-6 text-right font-sans text-sm font-bold text-muted">{i + 1}</span>
                    <span className={`grid h-10 w-10 shrink-0 place-items-center rounded-lg ${s.kind === "reading" ? "bg-navy text-gold" : "bg-gold text-navy"}`}>
                      <StepIcon s={s} />
                    </span>
                    <span className="flex-1">
                      <span className="block font-sans text-[11px] font-bold uppercase tracking-[0.16em] text-gold-deep">{stepLabel(s)}</span>
                      <span className="block font-sans text-base font-bold text-navy">{s.title}</span>
                    </span>
                    <DoneTick id={`${num}/${s.slug}`} />
                  </Link>
                </li>
              ))}
            </ol>
          ) : (
            <div className="mt-4"><Locked num={num} next={`/lessons/${num}`} /></div>
          )}
        </div>

        <aside className="space-y-4">
          <div className="rounded-2xl bg-navy p-5 text-white">
            <p className="kicker text-gold">Bible Passages</p>
            <p className="mt-2 font-serif text-lg"><Md text={p.passages} /></p>
          </div>
          <div className="rounded-2xl border border-line bg-paper p-5">
            <p className="kicker text-gold-deep">In this lesson, children will learn</p>
            <ol className="mt-3 list-decimal space-y-1.5 pl-5 font-serif text-lg marker:font-sans marker:font-bold marker:text-gold-deep">
              {p.objectives.map((o) => <li key={o}><Md text={o} /></li>)}
            </ol>
          </div>
          <div className="teacher-only rounded-2xl border border-line bg-paper p-5">
            <p className="kicker text-gold-deep">Opening Prayer</p>
            <p className="mt-2 font-serif text-lg italic"><Md text={p.prayer} /></p>
          </div>
          <div className="teacher-only rounded-2xl border border-line bg-paper p-5">
            <p className="kicker text-gold-deep">Materials</p>
            <p className="mt-2 font-serif text-lg"><Md text={p.materials} /></p>
          </div>
          {open && keys.length > 0 && (
            <details className="teacher-only rounded-2xl border border-gold/50 bg-gold-soft/30 p-5">
              <summary className="min-h-11 cursor-pointer font-sans text-sm font-extrabold uppercase tracking-[0.18em] text-navy">Answer key, Lesson {num}</summary>
              <div className="mt-3 space-y-4">
                {keys.map((k) => (
                  <div key={k.title}>
                    <p className="font-sans text-sm font-extrabold text-navy">{k.title}</p>
                    <ol className="mt-1 list-decimal pl-5 font-serif">{k.answers.map((a, i) => <li key={i}><Md text={a} /></li>)}</ol>
                  </div>
                ))}
              </div>
            </details>
          )}
        </aside>
      </div>
      <Footer />
    </main>
  );
}
