import type { Metadata, Viewport } from "next";
import { Caladea, Inter } from "next/font/google";
import { Analytics } from "@vercel/analytics/next";
import "./globals.css";
import { site } from "@/lib/site";
import { TabBar } from "@/components/tab-bar";
import { Pwa } from "@/components/pwa";
import { InstallPrompt } from "@/components/install-prompt";
import { modeScript } from "@/components/mode-toggle";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter", weight: ["500", "600", "700", "800", "900"] });
const caladea = Caladea({ subsets: ["latin"], variable: "--font-caladea", weight: ["400", "700"], style: ["normal", "italic"] });

const indexing = process.env.SITE_INDEXING === "on";

export const viewport: Viewport = {
  themeColor: "#1f2f5c",
  viewportFit: "cover",
  width: "device-width",
  initialScale: 1,
};

export const metadata: Metadata = {
  metadataBase: new URL(site.url),
  title: { default: `${site.name} · ${site.tagline}`, template: `%s · ${site.name}` },
  description: site.description,
  applicationName: site.name,
  manifest: "/manifest.webmanifest",
  robots: indexing ? { index: true, follow: true } : { index: false, follow: false },
  appleWebApp: { capable: true, title: site.short, statusBarStyle: "black-translucent" },
  other: { "apple-mobile-web-app-capable": "yes" },
  icons: {
    icon: [
      { url: "/pwa/icon-192.png", sizes: "192x192", type: "image/png" },
      { url: "/pwa/icon-512.png", sizes: "512x512", type: "image/png" },
    ],
    apple: [{ url: "/pwa/apple-touch-icon.png", sizes: "180x180" }],
  },
  openGraph: {
    type: "website",
    siteName: site.name,
    title: site.name,
    description: site.description,
    images: [{ url: "/pwa/og.png", width: 1200, height: 630, alt: site.name }],
  },
  twitter: { card: "summary_large_image", title: site.name, description: site.description, images: ["/pwa/og.png"] },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" data-mode="teacher" className={`${inter.variable} ${caladea.variable}`} suppressHydrationWarning>
      <head>
        <script dangerouslySetInnerHTML={{ __html: modeScript }} />
      </head>
      <body>
        <a href="#main" className="sr-only z-50 rounded bg-gold px-4 py-2 font-sans font-bold text-navy focus:not-sr-only focus:fixed focus:left-3 focus:top-3">
          Skip to content
        </a>
        <div id="main">{children}</div>
        <TabBar />
        <InstallPrompt />
        <Pwa />
        <Analytics />
      </body>
    </html>
  );
}
