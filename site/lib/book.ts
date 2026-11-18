// Typed access to the book. data/book.json is generated from curriculum/book/c_*.py
// by scripts/export_book.py, so the printed book and the site never drift apart.
import raw from "@/data/book.json";

export type Art = { img: string; cap: string; contain: boolean; page: number };
export type Fig = { img: string; cap: string };
export type Nugget = { h: string; t: string };

export type Block =
  | { k: "q"; text: string; lines: number }
  | { k: "qs"; items: { text: string; lines: number }[] }
  | { k: "mc"; start: number; items: { text: string; options?: string[]; lines?: number; answer?: number }[] }
  | { k: "read"; paras: string[] }
  | { k: "box"; label: string }
  | { k: "grid4"; cells: string[] }
  | { k: "lines"; lines: number }
  | { k: "bank"; words: string[] }
  | { k: "part"; text: string }
  | { k: "img"; img: string }
  | { k: "printed" }
  | { k: "wordsearch"; grid: string[][]; words: string[] }
  | { k: "maze"; svg: string }
  | { k: "match"; left: string[]; right: string[]; answer?: number[] }
  | { k: "order"; items: { letter: string; text: string }[]; answer?: number[] }
  | { k: "fill"; rows: string[]; answer?: string[]; bank?: string[] }
  | { k: "tree"; slots?: { label: string; answer: string }[]; bank?: string[] }
  | { k: "trace"; text: string; rtl: boolean; rows: number; lead: string }
  | { k: "letters"; items: { char: string; name: string }[] };

export type Reading = {
  kind: "reading";
  slug: string;
  title: string;
  kicker: string;
  page: number;
  paras: string[];
  verse?: string;
  vref?: string;
  read?: string;
  notes?: Nugget[];
  callout?: { title: string; body: string[] };
  figs?: Fig[];
  art?: Art;
};
export type Coloring = { kind: "color"; slug: string; title: string; kick: string; img: string; caption: string; page: number };
export type Activity = {
  kind: "activity";
  slug: string;
  title: string;
  kick: string;
  ins: string;
  page: number;
  blocks: Block[];
  printed: boolean;
  sketch?: string;
};
export type Step = Reading | Coloring | Activity;

export type Plan = {
  passages: string;
  objectives: string[];
  prayer: string;
  materials: string;
  overview: string;
  dyk: string;
  flow: [string, string][];
  page: number;
};
export type Lesson = { num: number; title: string; ref: string; cover: string; page: number; plan: Plan; steps: Step[] };
export type FrontPage = { title: string; kicker: string; paras: string[]; slug: string };
export type Key = { lesson: number; title: string; answers: string[] };

type Book = { front: FrontPage[]; lessons: Lesson[]; keys: Key[]; pageCount: number };
const book = raw as unknown as Book;

export const lessons = book.lessons;
export const front = book.front;
export const keys = book.keys;

export const getLesson = (num: number) => lessons.find((l) => l.num === num);
export const getStep = (num: number, slug: string) => {
  const lesson = getLesson(num);
  if (!lesson) return undefined;
  const i = lesson.steps.findIndex((s) => s.slug === slug);
  if (i < 0) return undefined;
  return { lesson, step: lesson.steps[i], index: i, prev: lesson.steps[i - 1], next: lesson.steps[i + 1] };
};
export const keysFor = (num: number) => keys.filter((k) => k.lesson === num);

export const img = (name: string) => `/images/book/${name}`;
export const pageImg = (n: number) => `/pages/p${String(n).padStart(3, "0")}.jpg`;
export const stepHref = (num: number, slug: string) => `/lessons/${num}/${slug}`;

export const lessonWeeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"];

export const stepLabel = (s: Step) => (s.kind === "reading" ? "Reading" : s.kind === "color" ? "Coloring" : s.kick || "Activity");

export const allActivities = () =>
  lessons.flatMap((l) => l.steps.filter((s) => s.kind !== "reading").map((s) => ({ lesson: l, step: s as Coloring | Activity })));
