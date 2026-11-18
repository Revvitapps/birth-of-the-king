import { Clapperboard } from "lucide-react";
import { lessonVideos } from "@/data/media";

export function VideoSlot({ num, title }: { num: number; title: string }) {
  const v = lessonVideos[num];
  if (v) {
    const isFile = /\.(mp4|webm)$/i.test(v.src);
    return (
      <div className="overflow-hidden rounded-2xl bg-black">
        {isFile ? (
          <video src={v.src} poster={v.poster} controls playsInline preload="none" className="aspect-video w-full" />
        ) : (
          <iframe src={v.src} title={v.title} allow="encrypted-media; picture-in-picture; fullscreen" loading="lazy" className="aspect-video w-full" />
        )}
      </div>
    );
  }
  return (
    <div className="flex aspect-video w-full flex-col items-center justify-center gap-2 rounded-2xl border-2 border-dashed border-gold/50 bg-navy/5 p-6 text-center">
      <Clapperboard className="text-gold-deep" size={34} aria-hidden />
      <p className="font-sans text-sm font-extrabold uppercase tracking-[0.18em] text-navy">Lesson {num} video</p>
      <p className="max-w-xs font-serif text-muted">[PLACEHOLDER] A short video for “{title}” goes here.</p>
    </div>
  );
}
