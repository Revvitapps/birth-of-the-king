import type { MetadataRoute } from "next";
import { lessons } from "@/lib/book";
import { site } from "@/lib/site";

export default function sitemap(): MetadataRoute.Sitemap {
  const base = ["", "/lessons", "/activities", "/book", "/more"].map((p) => ({ url: `${site.url}${p}` }));
  const ls = lessons.flatMap((l) => [
    { url: `${site.url}/lessons/${l.num}` },
    ...l.steps.map((s) => ({ url: `${site.url}/lessons/${l.num}/${s.slug}` })),
  ]);
  return [...base, ...ls];
}
