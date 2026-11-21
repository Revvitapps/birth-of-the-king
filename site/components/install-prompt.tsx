"use client";
import { useEffect, useState } from "react";
import { Share, X } from "lucide-react";

type BIP = Event & { prompt: () => Promise<void>; userChoice: Promise<{ outcome: string }> };
const SEEN = "botk:visits";
const NOPE = "botk:install-dismissed";

// Shows from the second visit, or right after finishing a lesson step (event "botk:keyaction").
// Native prompt on Chromium, Share steps on iOS, hidden when already installed.
export function InstallPrompt() {
  const [evt, setEvt] = useState<BIP | null>(null);
  const [show, setShow] = useState(false);
  const [ios, setIos] = useState(false);

  useEffect(() => {
    const standalone =
      window.matchMedia("(display-mode: standalone)").matches || (navigator as Navigator & { standalone?: boolean }).standalone;
    if (standalone) return;
    let dismissed = false;
    let visits = 0;
    try {
      dismissed = localStorage.getItem(NOPE) === "1";
      if (!sessionStorage.getItem(SEEN)) {
        visits = Number(localStorage.getItem(SEEN) || "0") + 1;
        localStorage.setItem(SEEN, String(visits));
        sessionStorage.setItem(SEEN, "1");
      } else visits = Number(localStorage.getItem(SEEN) || "0");
    } catch {}
    if (dismissed) return;
    const isIos = /iphone|ipad|ipod/i.test(navigator.userAgent) && !/crios|fxios/i.test(navigator.userAgent);
    const onBip = (e: Event) => {
      e.preventDefault();
      setEvt(e as BIP);
      if (visits >= 2) setShow(true);
    };
    const onKey = () => setShow(true);
    window.addEventListener("beforeinstallprompt", onBip);
    window.addEventListener("botk:keyaction", onKey);
    const t = isIos && visits >= 2 ? window.setTimeout(() => { setIos(true); setShow(true); }, 1200) : 0;
    if (isIos) window.addEventListener("botk:keyaction", () => setIos(true));
    return () => {
      window.removeEventListener("beforeinstallprompt", onBip);
      window.removeEventListener("botk:keyaction", onKey);
      clearTimeout(t);
    };
  }, []);

  if (!show || (!evt && !ios)) return null;
  const close = () => {
    setShow(false);
    try { localStorage.setItem(NOPE, "1"); } catch {}
  };
  return (
    <div role="dialog" aria-label="Install the app" className="no-print fixed inset-x-3 z-50 mx-auto max-w-md rounded-2xl border border-gold/40 bg-navy p-4 text-white shadow-2xl"
      style={{ bottom: "calc(var(--tab-h) + env(safe-area-inset-bottom) + 12px)" }}>
      <button onClick={close} aria-label="Not now" className="absolute right-2 top-2 grid h-11 w-11 place-items-center text-white/70 hover:text-white">
        <X size={18} />
      </button>
      <p className="font-sans text-sm font-extrabold uppercase tracking-[0.18em] text-gold">Keep it on your phone</p>
      <p className="mt-1 pr-8 font-serif text-base">Add Beyond the Manger to your home screen. Lessons open fast, even with no signal at church.</p>
      {evt ? (
        <button
          onClick={async () => { await evt.prompt(); close(); }}
          className="mt-3 min-h-11 rounded-full bg-gold px-5 font-sans text-sm font-extrabold text-navy"
        >
          Install
        </button>
      ) : (
        <p className="mt-3 flex items-center gap-2 font-sans text-sm text-gold-soft">
          Tap <Share size={16} aria-label="Share" /> then <b>Add to Home Screen</b>.
        </p>
      )}
    </div>
  );
}
