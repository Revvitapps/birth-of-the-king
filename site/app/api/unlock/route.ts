import { NextResponse } from "next/server";
import { ACCESS_COOKIE, accessToken } from "@/lib/access";

export async function POST(req: Request) {
  const code = process.env.ACCESS_CODE;
  if (!code) return NextResponse.json({ ok: true, open: true });
  const { attempt } = (await req.json().catch(() => ({}))) as { attempt?: string };
  if (!attempt || accessToken(attempt) !== accessToken(code)) {
    return NextResponse.json({ ok: false }, { status: 401 });
  }
  const res = NextResponse.json({ ok: true });
  res.cookies.set(ACCESS_COOKIE, accessToken(code), {
    httpOnly: true,
    sameSite: "lax",
    secure: process.env.NODE_ENV === "production",
    path: "/",
    maxAge: 60 * 60 * 24 * 365,
  });
  return res;
}
