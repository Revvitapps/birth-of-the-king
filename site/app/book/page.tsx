import type { Metadata } from "next";
import Image from "next/image";
import { BookOpen, Check, Palette, Printer, ScrollText } from "lucide-react";
import { formats, site } from "@/lib/site";
import { lessons } from "@/lib/book";
import { BuyButton } from "@/components/buy-button";
import { SignupForm } from "@/components/signup-form";
import { Footer } from "@/components/footer";

export const metadata: Metadata = { title: "Get the Book", description: site.description };

const inside = [
  { icon: ScrollText, t: "A one-page plan for every lesson", d: "Bible passages, goals, an opening prayer, materials and the order of the readings." },
  { icon: BookOpen, t: "Painted reading spreads", d: "Each topic is a two-page spread: an illustration on the left, the reading on the right." },
  { icon: Check, t: "Teaching Nuggets", d: "Background, word studies and talking points beside every reading, plus a Notes box." },
  { icon: Palette, t: "Coloring pages and activities", d: "Placed right after the reading they belong to, with an answer key at the back." },
  { icon: Printer, t: "Printable student packs", d: "Every student page again, by lesson, sized for 8.5 × 11 paper. Print as many as you need." },
];

export default function BookPage() {
  return (
    <main>
      <section className="bg-night text-white">
        <div className="px-site mx-auto grid max-w-6xl items-center gap-10 py-14 lg:grid-cols-[0.8fr_1.2fr]">
          <div className="relative mx-auto aspect-[17/22] w-full max-w-sm overflow-hidden rounded-r-xl rounded-l-sm shadow-[12px_12px_0_0_rgba(201,162,74,0.35)]">
            <Image src="/pages/p001.jpg" alt="Front cover of Birth of the King" fill priority sizes="(min-width: 1024px) 380px, 80vw" className="object-cover" />
          </div>
          <div>
            <p className="kicker text-gold">Teacher Edition with Student Activity Pages</p>
            <h1 className="display mt-2 text-[clamp(2.6rem,8vw,4.8rem)]">Get the Book</h1>
            <p className="mt-4 max-w-xl font-serif text-xl text-white/90">
              {lessons.length} lessons and 102 pages on the birth of Yeshua the Messiah, from the promises of the prophets to the family’s escape to Egypt.
            </p>
            <div className="mt-6 flex flex-wrap gap-3">
              <BuyButton />
              {!site.buyUrl && <span className="self-center font-sans text-sm text-gold-soft">[PLACEHOLDER: store link]</span>}
            </div>
          </div>
        </div>
      </section>

      <section className="px-site mx-auto max-w-6xl py-12" aria-labelledby="fmt">
        <h2 id="fmt" className="display text-3xl text-navy">Choose a format</h2>
        <ul className="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {formats.map((f) => (
            <li key={f.id} className={`flex flex-col rounded-2xl border p-5 ${f.primary ? "border-gold bg-gold-soft/40" : "border-line bg-paper"}`}>
              {f.primary && <span className="kicker text-gold-deep">Most complete</span>}
              <h3 className="mt-1 font-sans text-lg font-extrabold text-navy">{f.name}</h3>
              <p className="mt-2 flex-1 font-serif text-base text-ink/85">{f.detail}</p>
              <p className="mt-4 font-sans text-sm font-bold text-navy">{f.price}</p>
            </li>
          ))}
        </ul>
      </section>

      <section className="bg-paper py-12" aria-labelledby="inside">
        <div className="px-site mx-auto max-w-6xl">
          <h2 id="inside" className="display text-3xl text-navy">What’s inside</h2>
          <ul className="mt-6 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {inside.map(({ icon: Icon, t, d }) => (
              <li key={t} className="flex gap-4">
                <span className="grid h-12 w-12 shrink-0 place-items-center rounded-xl bg-navy text-gold"><Icon size={22} aria-hidden /></span>
                <span>
                  <span className="block font-sans text-base font-extrabold text-navy">{t}</span>
                  <span className="block font-serif text-base text-ink/85">{d}</span>
                </span>
              </li>
            ))}
          </ul>
          <ol className="mt-10 grid gap-3 sm:grid-cols-5">
            {lessons.map((l) => (
              <li key={l.num} className="rounded-xl bg-navy p-4 text-white">
                <span className="kicker text-gold">Lesson {l.num}</span>
                <span className="mt-1 block font-sans font-extrabold">{l.title}</span>
              </li>
            ))}
          </ol>
        </div>
      </section>

      <section id="sample" className="px-site mx-auto max-w-3xl scroll-mt-4 py-12" aria-labelledby="free">
        <p className="kicker text-gold-deep">Free sample</p>
        <h2 id="free" className="display mt-2 text-3xl text-navy">Try Lesson 1 free</h2>
        <p className="mt-3 font-serif text-lg">Lesson 1 is open on this site. Leave your email to download its printable student pages.</p>
        <div className="mt-5"><SignupForm source="book-page" /></div>
      </section>
      <Footer />
    </main>
  );
}
