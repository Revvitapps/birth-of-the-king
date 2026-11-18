// Lesson videos. Add a YouTube/Vimeo embed URL or an .mp4 path per lesson and it appears
// on the lesson page. Empty entries show a "video coming" card.
export type LessonVideo = { title: string; src: string; poster?: string };

export const lessonVideos: Record<number, LessonVideo | null> = {
  1: null,
  2: null,
  3: null,
  4: null,
  5: null,
  6: null,
  7: null,
};
