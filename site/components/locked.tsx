import { Lock } from "lucide-react";
import { BuyButton } from "@/components/buy-button";
import { UnlockForm } from "@/components/unlock-form";

export function Locked({ num, next }: { num: number; next: string }) {
  return (
    <div className="rounded-2xl border border-gold/50 bg-gold-soft/40 p-6">
      <p className="flex items-center gap-2 font-sans text-sm font-extrabold uppercase tracking-[0.18em] text-navy">
        <Lock size={16} aria-hidden /> Lesson {num} comes with the book
      </p>
      <p className="mt-2 font-serif text-lg">Lesson 1 is free to try. The full curriculum unlocks Lessons 2 to 7 on this site, plus the PDF and every printable page.</p>
      <div className="mt-4"><BuyButton /></div>
      <p className="mt-6 font-sans text-sm font-bold text-navy">Already have the book?</p>
      <div className="mt-2"><UnlockForm next={next} /></div>
    </div>
  );
}
