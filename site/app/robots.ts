import type { MetadataRoute } from "next";
import { site } from "@/lib/site";

// Off (noindex) until SITE_INDEXING=on at launch.
export default function robots(): MetadataRoute.Robots {
  if (process.env.SITE_INDEXING !== "on") return { rules: [{ userAgent: "*", disallow: "/" }] };
  return { rules: [{ userAgent: "*", allow: "/", disallow: ["/api/"] }], sitemap: `${site.url}/sitemap.xml` };
}
