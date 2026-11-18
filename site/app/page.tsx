import Link from "next/link";
import Image from "next/image";
import { ArrowRight, BookOpen, Crown, Palette, Printer, ScrollText, Sparkles } from "lucide-react";
import { lessons, img, stepHref } from "@/lib/book";
import { site } from "@/lib/site";
import { LessonCard } from "@/components/lesson-card";
import { SignupForm } from "@/components/signup-form";
import { Footer } from "@/components/footer";

const first = lessons[0];

const answers = [
  { href: `/lessons/1`, icon: ScrollText, title: "Teach Lesson 1 tonight", note: "Plan, prayer, readings and activities in order" },
  { href: stepHref(1, first.steps[0].slug), icon: BookOpen, title: "Read the story with my kids", note: "Painted art, read aloud on any phone" },
  { href: "/activities#coloring", icon: Palette, title: "Something to color", note: "Tap-to-fill coloring pages from the book" },
  { href: "/activities", icon: Sparkles, title: "Activities and quizzes", note: "Answer on screen or print them out" },
  { href: "/book#sample", icon: Printer, title: "Printable student pages", note: "Lesson 1 pack free, all seven with the book" },
  { href: "/book", icon: Crown, title: "Get the whole book", note: "110 pages, teacher edition" },
];

export default function Home() {
  return (
    <main>
      <section className="relative isolate min-h-[88svh] overflow-hidden bg-night text-white">
        <Image src={img("cover.jpg")} alt="" fill priority sizes="100vw" className="drift -z-10 object-cover object-[50%_30%] opacity-90 lg:opacity-35 lg:blur-xl" />
        <div className="absolute inset-0 -z-10 bg-gradient-to-b from-night/70 via-night/20 to-night" />
        <div className="px-site mx-auto grid min-h-[88svh] max-w-6xl items-end gap-12 pb-12 pt-24 lg:grid-cols-[1.2fr_0.8fr] lg:items-center lg:py-20">
          <div>
          <p className="kicker text-gold-soft">An In-Depth Bible Curriculum</p>
          <h1 className="display mt-3 text-[clamp(3rem,11vw,7rem)]">
            Beyond
            <br />
            the Manger
          </h1>
          <div className="mt-4 h-1 w-24 bg-gold" />
          <p className="mt-4 max-w-xl font-sans text-xl font-bold text-gold-soft">{site.tagline}</p>
          <p className="mt-2 max-w-xl font-serif text-lg italic text-white/90">{site.sub}</p>
          <div className="mt-8 flex flex-wrap gap-3">
            <Link href="/lessons/1" className="inline-flex min-h-12 items-center gap-2 rounded-full bg-gold px-6 font-sans font-extrabold text-navy">
              Start Lesson 1 <ArrowRight size={18} aria-hidden />
            </Link>
            <Link href="/book" className="inline-flex min-h-12 items-center gap-2 rounded-full border border-white/40 px-6 font-sans font-bold text-white">
              Get the Book
            </Link>
          </div>
          </div>
          <div className="relative hidden aspect-[2/3] w-full max-w-md justify-self-end overflow-hidden rounded-2xl shadow-2xl ring-4 ring-gold/70 lg:block">
            <Image src={img("cover.jpg")} alt="" fill priority sizes="420px" className="object-cover" />
          </div>
        </div>
      </section>

      <section className="px-site mx-auto max-w-6xl py-14" aria-labelledby="need">
        <h2 id="need" className="display text-3xl text-navy sm:text-4xl">What do you need?</h2>
        <ul className="mt-6 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {answers.map(({ href, icon: Icon, title, note }) => (
            <li key={title}>
              <Link href={href} className="group flex min-h-20 items-center gap-4 rounded-2xl border border-line bg-paper p-4 transition-colors hover:border-gold">
                <span className="grid h-12 w-12 shrink-0 place-items-center rounded-xl bg-navy text-gold">
                  <Icon size={22} aria-hidden />
                </span>
                <span className="flex-1">
                  <span className="block font-sans text-base font-extrabold text-navy">{title}</span>
                  <span className="block font-serif text-sm text-muted">{note}</span>
                </span>
                <ArrowRight size={18} aria-hidden className="text-gold-deep transition-transform group-hover:translate-x-1" />
              </Link>
            </li>
          ))}
        </ul>
      </section>

      <section className="bg-navy py-14 text-white" aria-labelledby="seven">
        <div className="px-site mx-auto max-w-6xl">
          <p className="kicker text-gold">Seven lessons</p>
          <h2 id="seven" className="display mt-2 text-3xl sm:text-4xl">From the promise to the road home to Nazareth</h2>
          <p className="mt-3 max-w-2xl font-serif text-lg text-white/85">
            Each lesson has a one-page plan, painted reading spreads, Teaching Nuggets for the grown-ups, and the coloring pages and worksheets that belong with each reading.
          </p>
        </div>
        <div className="px-site mt-8 flex snap-x snap-mandatory gap-4 overflow-x-auto pb-4 lg:mx-auto lg:grid lg:max-w-6xl lg:grid-cols-4 lg:overflow-visible">
          {lessons.map((l, i) => (
            <div key={l.num} className="w-[72vw] max-w-72 shrink-0 snap-start sm:w-[42vw] lg:w-auto lg:max-w-none">
              <LessonCard l={l} priority={i < 2} />
            </div>
          ))}
        </div>
      </section>

      <section id="sample" className="px-site mx-auto max-w-6xl py-14" aria-labelledby="free">
        <div className="grid items-center gap-8 lg:grid-cols-[1fr_1.2fr]">
          <div className="relative mx-auto aspect-[17/22] w-full max-w-sm overflow-hidden rounded-xl border border-line bg-white shadow-xl">
            <Image src="/pages/p015.jpg" alt="A student page from Lesson 1" fill sizes="(min-width: 1024px) 380px, 80vw" className="object-cover" />
          </div>
          <div>
            <p className="kicker text-gold-deep">Free sample</p>
            <h2 id="free" className="display mt-2 text-3xl text-navy sm:text-4xl">Try Lesson 1 free</h2>
            <p className="mt-3 font-serif text-lg text-ink/85">
              Get the Lesson 1 student pages to print at home: coloring pages, the family tree, handwriting practice and more.
            </p>
            <div className="mt-6"><SignupForm /></div>
          </div>
        </div>
      </section>
      <Footer />
    </main>
  );
}
