"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { BookOpen, Crown, Home, Menu, Palette } from "lucide-react";

const tabs = [
  { href: "/", label: "Home", icon: Home },
  { href: "/lessons", label: "Lessons", icon: BookOpen },
  { href: "/book", label: "Get the Book", icon: Crown, orb: true },
  { href: "/activities", label: "Activities", icon: Palette },
  { href: "/more", label: "More", icon: Menu },
];

export function TabBar() {
  const path = usePathname();
  const active = (href: string) => (href === "/" ? path === "/" : path.startsWith(href));
  return (
    <nav
      aria-label="Main"
      className="no-print fixed inset-x-0 bottom-0 z-40 border-t border-white/10 bg-night/95 backdrop-blur"
      style={{ paddingBottom: "env(safe-area-inset-bottom)" }}
    >
      <ul className="mx-auto grid h-[var(--tab-h)] max-w-xl grid-cols-5 items-end">
        {tabs.map(({ href, label, icon: Icon, orb }) => {
          const on = active(href);
          if (orb)
            return (
              <li key={href} className="flex justify-center">
                <Link
                  href={href}
                  aria-current={on ? "page" : undefined}
                  className="group -mt-7 flex flex-col items-center gap-1 pb-2 font-sans text-[11px] font-bold text-gold-soft"
                >
                  <span
                    className={`grid h-[58px] w-[58px] place-items-center rounded-full border-4 border-night bg-gold text-navy shadow-[0_6px_0_0_rgba(0,0,0,0.25)] transition-transform group-active:scale-95 ${on ? "ring-2 ring-gold-soft" : ""}`}
                  >
                    <Icon aria-hidden size={26} strokeWidth={2.4} />
                  </span>
                  <span className="leading-none">{label}</span>
                </Link>
              </li>
            );
          return (
            <li key={href}>
              <Link
                href={href}
                aria-current={on ? "page" : undefined}
                className={`flex h-[var(--tab-h)] min-h-11 flex-col items-center justify-center gap-1 font-sans text-[11px] font-semibold ${on ? "text-gold" : "text-white/70 hover:text-white"}`}
              >
                <Icon aria-hidden size={22} strokeWidth={on ? 2.4 : 1.9} />
                <span className="leading-none">{label}</span>
              </Link>
            </li>
          );
        })}
      </ul>
    </nav>
  );
}
