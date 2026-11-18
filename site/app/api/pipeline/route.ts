import { NextResponse } from "next/server";

const EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export async function POST(req: Request) {
  let body: Record<string, unknown>;
  try {
    body = await req.json();
  } catch {
    return NextResponse.json({ ok: false, error: "bad json" }, { status: 400 });
  }
  const email = String(body.email || "").trim().toLowerCase();
  if (!EMAIL.test(email)) return NextResponse.json({ ok: false, error: "email" }, { status: 400 });
  const contact = {
    email,
    name: String(body.name || "").slice(0, 120),
    role: String(body.role || "").slice(0, 60),
    source: String(body.source || "site").slice(0, 60),
    at: new Date().toISOString(),
  };
  const hook = process.env.PIPELINE_WEBHOOK_URL;
  if (hook) {
    try {
      await fetch(hook, { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(contact) });
    } catch {
      return NextResponse.json({ ok: false, error: "forward" }, { status: 502 });
    }
  }
  return NextResponse.json({ ok: true, forwarded: Boolean(hook) });
}
