import type { Metadata } from "next";
import { lessons } from "@/lib/book";
import { LessonCard } from "@/components/lesson-card";
import { ModeToggle } from "@/components/mode-toggle";
import { Footer } from "@/components/footer";

export const metadata: Metadata = { title: "Lessons" };

export default function Lessons() {
  return (
    <main>
      <header className="bg-navy pb-10 pt-14 text-white">
        <div className="px-site mx-auto flex max-w-6xl flex-wrap items-end justify-between gap-4">
          <div>
            <p className="kicker text-gold">Birth of the King</p>
            <h1 className="display mt-2 text-4xl sm:text-5xl">The Lessons</h1>
            <p className="mt-3 max-w-xl font-serif text-lg text-white/85">Teach them in order. Each one opens with a plan, then the readings and activities in the order the book places them.</p>
          </div>
          <ModeToggle className="text-white" />
        </div>
      </header>
      <section className="px-site mx-auto grid max-w-6xl gap-5 py-10 sm:grid-cols-2 lg:grid-cols-3">
        {lessons.map((l, i) => <LessonCard key={l.num} l={l} priority={i < 3} />)}
      </section>
      <Footer />
    </main>
  );
}
