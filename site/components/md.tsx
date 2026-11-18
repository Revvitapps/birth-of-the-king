import { Fragment, type ReactNode } from "react";

// The book's tiny inline markup: **bold** and *italic*.
export function Md({ text }: { text: string }) {
  const out: ReactNode[] = [];
  const re = /\*\*(.+?)\*\*|\*(.+?)\*/g;
  let last = 0;
  let m: RegExpExecArray | null;
  let i = 0;
  while ((m = re.exec(text))) {
    if (m.index > last) out.push(<Fragment key={i++}>{text.slice(last, m.index)}</Fragment>);
    out.push(m[1] ? <b key={i++}>{m[1]}</b> : <i key={i++}>{m[2]}</i>);
    last = m.index + m[0].length;
  }
  if (last < text.length) out.push(<Fragment key={i++}>{text.slice(last)}</Fragment>);
  return <>{out}</>;
}

export const plain = (s: string) => s.replace(/\*\*(.+?)\*\*/g, "$1").replace(/\*(.+?)\*/g, "$1").replace(/^(## |> |- )/, "");

// Renders the book's paragraph list: "## heading", "> quote", "- bullet", "@fig ...", plain.
export function Paras({ paras }: { paras: string[] }) {
  const firstPlain = paras.findIndex((x) => !/^(## |> |- |@fig )/.test(x));
  return (
    <div className="prose-book">
      {paras.map((x, i) => {
        if (x.startsWith("## ")) return <h2 key={i}><Md text={x.slice(3)} /></h2>;
        if (x.startsWith("> ")) return <blockquote key={i}><Md text={x.slice(2)} /></blockquote>;
        if (x.startsWith("- ")) return <p key={i} className="li"><Md text={x.slice(2)} /></p>;
        if (x.startsWith("@fig ")) return null;
        const cls = i === firstPlain ? "first" : undefined;
        return <p key={i} className={cls}><Md text={x} /></p>;
      })}
    </div>
  );
}
