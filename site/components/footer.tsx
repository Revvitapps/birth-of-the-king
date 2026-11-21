import Link from "next/link";
import Image from "next/image";
import { site } from "@/lib/site";

export function Footer() {
  return (
    <footer className="no-print mt-16 bg-night px-site py-10 text-white/80">
      <div className="mx-auto flex max-w-6xl flex-col gap-6 sm:flex-row sm:items-center sm:justify-between">
        <div className="flex items-center gap-3">
          <Image src="/images/book/fhk_logo.png" alt="For His Kingdom" width={56} height={53} className="rounded-full bg-cream p-1" />
          <div>
            <p className="font-sans text-sm font-extrabold uppercase tracking-[0.2em] text-gold">{site.name}</p>
            <p className="font-serif text-sm">© {site.publisher}</p>
          </div>
        </div>
        <nav aria-label="Footer" className="flex flex-wrap gap-x-5 gap-y-2 font-sans text-sm">
          <Link href="/lessons" className="hover:text-white">Lessons</Link>
          <Link href="/activities" className="hover:text-white">Activities</Link>
          <Link href="/book" className="hover:text-white">Get the Book</Link>
          <Link href="/more" className="hover:text-white">About</Link>
        </nav>
      </div>
      <p className="mx-auto mt-8 max-w-6xl font-sans text-xs text-white/75">
        Concept prototype by <span style={{ color: "#C6F94D" }}>Revvit</span>
      </p>
    </footer>
  );
}
