import type { Metadata } from "next";
import Link from "next/link";
import Image from "next/image";
import { allActivities, img, pageImg, stepHref, lessons } from "@/lib/book";
import { Footer } from "@/components/footer";
import { DoneTick } from "@/components/progress";

export const metadata: Metadata = { title: "Coloring and Activities" };

export default function Activities() {
  const all = allActivities();
  const coloring = all.filter((a) => a.step.kind === "color");
  return (
    <main>
      <header className="bg-navy pb-10 pt-14 text-white">
        <div className="px-site mx-auto max-w-6xl">
          <p className="kicker text-gold">For the kids</p>
          <h1 className="display mt-2 text-4xl sm:text-5xl">Coloring and Activities</h1>
          <p className="mt-3 max-w-xl font-serif text-lg text-white/85">
            {coloring.length} coloring pages and {all.length - coloring.length} activities from the book. Do them on screen, or print the page.
          </p>
        </div>
      </header>

      <section id="coloring" className="px-site mx-auto max-w-6xl scroll-mt-4 py-10" aria-labelledby="ch">
        <h2 id="ch" className="display text-2xl text-navy">Coloring pages</h2>
        <ul className="mt-5 grid grid-cols-2 gap-4 sm:grid-cols-3 lg:grid-cols-6">
          {coloring.map(({ lesson, step }) => (
            <li key={step.slug}>
              <Link href={stepHref(lesson.num, step.slug)} className="group block">
                <div className="relative aspect-[2/3] overflow-hidden rounded-xl border border-line bg-white">
                  <Image src={img(step.kind === "color" ? step.img : "")} alt="" fill sizes="(min-width: 1024px) 16vw, 45vw" className="object-contain p-2 transition-transform group-hover:scale-105" />
                  <span className="absolute right-2 top-2"><DoneTick id={`${lesson.num}/${step.slug}`} /></span>
                </div>
                <p className="mt-2 font-sans text-sm font-bold text-navy">{step.title}</p>
                <p className="font-sans text-xs text-muted">Lesson {lesson.num}</p>
              </Link>
            </li>
          ))}
        </ul>
      </section>

      {lessons.map((l) => {
        const acts = all.filter((a) => a.lesson.num === l.num && a.step.kind === "activity");
        return (
          <section key={l.num} className="px-site mx-auto max-w-6xl py-6" aria-labelledby={`l${l.num}`}>
            <h2 id={`l${l.num}`} className="font-sans text-lg font-extrabold text-navy">
              <span className="kicker mr-2 text-gold-deep">Lesson {l.num}</span> {l.title}
            </h2>
            <ul className="mt-4 grid grid-cols-2 gap-4 sm:grid-cols-3 lg:grid-cols-6">
              {acts.map(({ step }) => (
                <li key={step.slug}>
                  <Link href={stepHref(l.num, step.slug)} className="group block">
                    <div className="relative aspect-[17/22] overflow-hidden rounded-xl border border-line bg-white shadow-sm">
                      <Image src={pageImg(step.page)} alt="" fill sizes="(min-width: 1024px) 16vw, 45vw" className="object-cover object-top transition-transform group-hover:scale-105" />
                      <span className="absolute right-2 top-2"><DoneTick id={`${l.num}/${step.slug}`} /></span>
                    </div>
                    <p className="mt-2 font-sans text-sm font-bold text-navy">{step.title}</p>
                    <p className="font-sans text-xs text-muted">{step.kind === "activity" ? step.kick : ""}</p>
                  </Link>
                </li>
              ))}
            </ul>
          </section>
        );
      })}
      <Footer />
    </main>
  );
}
