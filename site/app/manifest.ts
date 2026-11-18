import type { MetadataRoute } from "next";

export default function manifest(): MetadataRoute.Manifest {
  return {
    id: "/",
    name: "Birth of the King",
    short_name: "Birth of the King",
    description: "Five lessons on the birth of Yeshua: readings, Teaching Nuggets, coloring and activities.",
    start_url: "/?source=pwa",
    scope: "/",
    display: "standalone",
    orientation: "portrait",
    theme_color: "#1f2f5c",
    background_color: "#141b30",
    categories: ["education", "books", "kids"],
    icons: [
      { src: "/pwa/icon-192.png", sizes: "192x192", type: "image/png", purpose: "any" },
      { src: "/pwa/icon-512.png", sizes: "512x512", type: "image/png", purpose: "any" },
      { src: "/pwa/maskable-192.png", sizes: "192x192", type: "image/png", purpose: "maskable" },
      { src: "/pwa/maskable-512.png", sizes: "512x512", type: "image/png", purpose: "maskable" },
    ],
    shortcuts: [
      { name: "Continue the lessons", url: "/lessons", icons: [{ src: "/pwa/icon-192.png", sizes: "192x192" }] },
      { name: "Coloring and activities", url: "/activities", icons: [{ src: "/pwa/icon-192.png", sizes: "192x192" }] },
      { name: "Lesson 1: The Promised King", url: "/lessons/1", icons: [{ src: "/pwa/icon-192.png", sizes: "192x192" }] },
      { name: "Get the Book", url: "/book", icons: [{ src: "/pwa/icon-192.png", sizes: "192x192" }] },
    ],
  };
}
