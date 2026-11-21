import "server-only";
import { createHash } from "node:crypto";
import { cookies } from "next/headers";

// Lesson 1 is always free. When ACCESS_CODE is set, Lessons 2 to 7 need the code buyers
// receive with the book. When it is not set (prototype), everything is open.
export const FREE_LESSONS = [1];
export const ACCESS_COOKIE = "botk_access";

export const accessToken = (code: string) =>
  createHash("sha256").update(`birth-of-the-king:${code.trim().toUpperCase()}`).digest("hex").slice(0, 32);

export const gateOn = () => Boolean(process.env.ACCESS_CODE);

export async function hasAccess(lesson: number) {
  if (FREE_LESSONS.includes(lesson)) return true;
  const code = process.env.ACCESS_CODE;
  if (!code) return true;
  const jar = await cookies();
  return jar.get(ACCESS_COOKIE)?.value === accessToken(code);
}
