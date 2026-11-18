// Site facts. Anything not confirmed by the author is a visible [PLACEHOLDER].
export const site = {
  name: "Birth of the King",
  short: "Birth of the King",
  tagline: "An In-Depth Bible Curriculum on the Birth of the King",
  sub: "The Story of Yeshua the Messiah · Matthew 1–2 · Luke 1–2",
  publisher: "For His Kingdom",
  url: process.env.NEXT_PUBLIC_SITE_URL || "https://birth-of-the-king.revvit.io",
  buyUrl: process.env.NEXT_PUBLIC_BUY_URL || "",
  email: "[PLACEHOLDER: contact email]",
  description:
    "Five lessons on the birth of Yeshua, from the promises of the prophets to the escape to Egypt. Readings, Teaching Nuggets, coloring pages and activities, all in one place.",
};

// Formats from the book plan. Prices are not confirmed yet, so they show as placeholders.
export const formats = [
  {
    id: "digital",
    name: "Complete Digital Curriculum",
    detail: "The full 102-page teacher book as a PDF, plus printable student packs for all five lessons.",
    price: "[PLACEHOLDER price]",
    primary: true,
  },
  {
    id: "activity",
    name: "Student Activity Pack",
    detail: "Every coloring page and worksheet, sized for 8.5 × 11 paper. Print as many copies as you need.",
    price: "[PLACEHOLDER price]",
  },
  {
    id: "print",
    name: "Printed Teaching Book",
    detail: "The teaching book in print, soft or hard cover.",
    price: "[PLACEHOLDER price]",
  },
  {
    id: "church",
    name: "Church and Co-op License",
    detail: "Teach it to a whole class or Sunday school.",
    price: "[PLACEHOLDER price]",
  },
];
