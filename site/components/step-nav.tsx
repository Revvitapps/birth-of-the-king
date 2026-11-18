"use client";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Flag } from "lucide-react";
import { markDone } from "@/components/progress";
import { celebrate } from "@/lib/fun";

type L = { href: string; title: string } | null;

// Sticky prev/next above the tab bar. Moving on marks this step done.
export function StepNav({ id, prev, next, lessonHref, index, total }: { id: string; prev: L; next: L; lessonHref: string; index: number; total: number }) {
  return (
    <nav
      aria-label="Lesson steps"
      className="no-print sticky z-30 border-t border-line bg-cream/95 backdrop-blur"
      style={{ bottom: "calc(var(--tab-h) + env(safe-area-inset-bottom))" }}
    >
      <div className="px-site mx-auto flex max-w-6xl items-center gap-2 py-2">
        {prev ? (
          <Link href={prev.href} className="flex min-h-11 min-w-11 items-center gap-2 rounded-full px-2 font-sans text-sm font-bold text-navy hover:bg-navy/5" aria-label={`Back: ${prev.title}`}>
            <ArrowLeft size={18} aria-hidden /> <span className="hidden max-w-48 truncate sm:inline">{prev.title}</span>
          </Link>
        ) : (
          <Link href={lessonHref} aria-label="Back to the lesson plan" className="flex min-h-11 items-center gap-2 rounded-full px-2 font-sans text-sm font-bold text-navy hover:bg-navy/5">
            <ArrowLeft size={18} aria-hidden /> <span className="hidden sm:inline">Lesson plan</span>
          </Link>
        )}
        <div className="flex-1 text-center font-sans text-xs font-bold text-muted">
          {index + 1} / {total}
        </div>
        <Link
          href={next ? next.href : lessonHref}
          onClick={(e) => {
            markDone(id);
            if (!next) celebrate(e.currentTarget);
          }}
          className="flex min-h-11 items-center gap-2 rounded-full bg-navy px-4 font-sans text-sm font-extrabold text-white"
        >
          {next ? (
            <>
              <span className="max-w-[40vw] truncate sm:max-w-56">Next: {next.title}</span> <ArrowRight size={18} aria-hidden />
            </>
          ) : (
            <>
              <Flag size={16} aria-hidden /> Finish lesson
            </>
          )}
        </Link>
      </div>
    </nav>
  );
}
