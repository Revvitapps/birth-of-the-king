import Link from "next/link";

export default function NotFound() {
  return (
    <main className="px-site mx-auto flex min-h-[70svh] max-w-xl flex-col justify-center py-16">
      <p className="kicker text-gold-deep">Page not found</p>
      <h1 className="display mt-2 text-4xl text-navy">This page wandered off</h1>
      <p className="mt-3 font-serif text-lg">Like the Wise Men, follow the star back home.</p>
      <Link href="/" className="mt-6 inline-flex min-h-12 w-fit items-center rounded-full bg-navy px-6 font-sans font-extrabold text-white">Go home</Link>
    </main>
  );
}
