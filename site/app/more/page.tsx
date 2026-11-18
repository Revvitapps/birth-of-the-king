import type { Metadata } from "next";
import Link from "next/link";
import { front } from "@/lib/book";
import { site } from "@/lib/site";
import { Paras } from "@/components/md";
import { ModeToggle } from "@/components/mode-toggle";
import { Footer } from "@/components/footer";

export const metadata: Metadata = { title: "About this curriculum" };

export default function More() {
  return (
    <main>
      <header className="bg-navy pb-10 pt-14 text-white">
        <div className="px-site mx-auto max-w-3xl">
          <p className="kicker text-gold">Welcome, Teacher</p>
          <h1 className="display mt-2 text-4xl sm:text-5xl">About this curriculum</h1>
          <nav aria-label="On this page" className="mt-5 flex flex-wrap gap-2 font-sans text-sm font-bold">
            {front.map((f) => (
              <a key={f.slug} href={`#${f.slug}`} className="inline-flex min-h-11 items-center rounded-full border border-white/25 px-4 hover:border-gold">{f.title}</a>
            ))}
            <a href="#settings" className="inline-flex min-h-11 items-center rounded-full border border-white/25 px-4 hover:border-gold">Settings</a>
          </nav>
        </div>
      </header>
      <div className="px-site mx-auto max-w-3xl py-10">
        {front.map((f) => (
          <section key={f.slug} id={f.slug} className="mb-12 scroll-mt-4">
            <p className="kicker text-gold-deep">{f.kicker}</p>
            <h2 className="display mt-2 text-3xl text-navy">{f.title}</h2>
            <div className="mt-4"><Paras paras={f.paras} /></div>
          </section>
        ))}
        <section id="settings" className="scroll-mt-4 rounded-2xl border border-line bg-paper p-6">
          <h2 className="font-sans text-lg font-extrabold text-navy">Settings</h2>
          <p className="mt-2 font-serif">Teacher mode shows the Teaching Nuggets, your notes, the opening prayers and the answer keys. Kids mode hides them so children can read and play on their own.</p>
          <div className="mt-3 text-navy"><ModeToggle /></div>
          <p className="mt-6 font-serif">Questions: {site.email}</p>
          <p className="mt-2 font-serif">
            Ready for the whole curriculum? <Link href="/book" className="font-bold text-navy underline decoration-gold decoration-2 underline-offset-4">Get the Book</Link>
          </p>
        </section>
      </div>
      <Footer />
    </main>
  );
}
