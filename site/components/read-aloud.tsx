"use client";
import { useEffect, useRef, useState } from "react";
import { Pause, Volume2 } from "lucide-react";

// Reads the passage aloud with the device's own voice (Web Speech API).
export function ReadAloud({ text, label = "Read it to me" }: { text: string[]; label?: string }) {
  const [state, setState] = useState<"idle" | "playing" | "unsupported">("idle");
  const queue = useRef<SpeechSynthesisUtterance[]>([]);

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect -- feature detection after mount
    if (!("speechSynthesis" in window)) setState("unsupported");
    return () => {
      if ("speechSynthesis" in window) window.speechSynthesis.cancel();
    };
  }, []);

  if (state === "unsupported") return null;

  const pickVoice = () => {
    const voices = window.speechSynthesis.getVoices().filter((v) => v.lang.startsWith("en"));
    return voices.find((v) => /natural|premium|enhanced|samantha|google us/i.test(v.name)) || voices[0];
  };

  const toggle = () => {
    const synth = window.speechSynthesis;
    if (state === "playing") {
      synth.cancel();
      setState("idle");
      return;
    }
    synth.cancel();
    const voice = pickVoice();
    queue.current = text.filter(Boolean).map((t, i, all) => {
      const u = new SpeechSynthesisUtterance(t);
      if (voice) u.voice = voice;
      u.rate = 0.95;
      if (i === all.length - 1) u.onend = () => setState("idle");
      return u;
    });
    queue.current.forEach((u) => synth.speak(u));
    setState("playing");
  };

  return (
    <button
      onClick={toggle}
      aria-pressed={state === "playing"}
      className="inline-flex min-h-11 items-center gap-2 rounded-full border border-current/25 px-4 font-sans text-sm font-bold"
    >
      {state === "playing" ? <Pause size={18} aria-hidden /> : <Volume2 size={18} aria-hidden />}
      {state === "playing" ? "Stop reading" : label}
    </button>
  );
}
