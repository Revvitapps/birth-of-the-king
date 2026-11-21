import { BookOpen, Palette, PencilLine } from "lucide-react";
import type { Step } from "@/lib/book";

export function StepIcon({ s, size = 18 }: { s: Step; size?: number }) {
  if (s.kind === "reading") return <BookOpen size={size} aria-hidden />;
  if (s.kind === "color") return <Palette size={size} aria-hidden />;
  return <PencilLine size={size} aria-hidden />;
}
