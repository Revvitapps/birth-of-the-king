import Link from "next/link";
import { Crown } from "lucide-react";
import { site } from "@/lib/site";

export function BuyButton({ label = "Get the Book", className = "" }: { label?: string; className?: string }) {
  const cls = `inline-flex min-h-12 items-center justify-center gap-2 rounded-full bg-gold px-6 font-sans text-base font-extrabold text-navy transition-transform active:scale-[0.98] ${className}`;
  if (site.buyUrl)
    return (
      <a href={site.buyUrl} className={cls} rel="noopener">
        <Crown size={18} aria-hidden /> {label}
      </a>
    );
  return (
    <Link href="/book" className={cls}>
      <Crown size={18} aria-hidden /> {label}
    </Link>
  );
}
