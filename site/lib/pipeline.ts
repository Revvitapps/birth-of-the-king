"use client";
// Every sign-up goes through upsertContact(): kept on the device, then POSTed to
// /api/pipeline, which forwards to PIPELINE_WEBHOOK_URL when it is set.
export type Contact = { email: string; name?: string; role?: string; source: string };

const KEY = "botk:contacts";

export async function upsertContact(c: Contact) {
  const record = { ...c, email: c.email.trim().toLowerCase(), at: new Date().toISOString() };
  try {
    const list = JSON.parse(localStorage.getItem(KEY) || "[]") as Contact[];
    const next = [...list.filter((x) => x.email !== record.email), record];
    localStorage.setItem(KEY, JSON.stringify(next));
  } catch {}
  const res = await fetch("/api/pipeline", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(record),
  });
  return res.ok;
}
