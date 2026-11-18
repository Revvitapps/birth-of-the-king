import Link from "next/link";
import Image from "next/image";
import type { Lesson } from "@/lib/book";
import { img } from "@/lib/book";
import { LessonMeter } from "@/components/progress";

export function LessonCard({ l, priority = false }: { l: Lesson; priority?: boolean }) {
  const ids = l.steps.map((s) => `${l.num}/${s.slug}`);
  return (
    <Link href={`/lessons/${l.num}`} className="group relative block overflow-hidden rounded-2xl bg-navy text-white">
      <div className="relative aspect-[3/4]">
        <Image src={img(l.cover)} alt="" fill priority={priority} sizes="(min-width: 1024px) 20vw, (min-width: 640px) 45vw, 85vw" className="object-cover transition-transform duration-700 group-hover:scale-105" />
        <div className="absolute inset-0 bg-gradient-to-t from-night via-night/40 to-transparent" />
      </div>
      <div className="absolute inset-x-0 bottom-0 p-4">
        <p className="kicker text-gold">Lesson {l.num}</p>
        <h3 className="display mt-1 text-2xl">{l.title}</h3>
        <p className="mt-1 font-serif text-sm italic text-gold-soft">{l.ref}</p>
        <div className="mt-3"><LessonMeter num={l.num} ids={ids} /></div>
      </div>
    </Link>
  );
}
