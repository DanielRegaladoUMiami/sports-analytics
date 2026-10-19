"""Fallback con youtube-transcript-api para videos que yt-dlp no pudo bajar. Escribe VTT mínimo en raw/vtt/."""
import sys, pathlib
from youtube_transcript_api import YouTubeTranscriptApi
raw = pathlib.Path(sys.argv[1]); api = YouTubeTranscriptApi()
def ts(s): h, r = divmod(s, 3600); m, s = divmod(r, 60); return f"{int(h):02d}:{int(m):02d}:{s:06.3f}"
for vid in (raw / "missing.txt").read_text().split():
    try:
        tr = api.fetch(vid, languages=["en"])
        lines = ["WEBVTT", ""] + [f"{ts(s.start)} --> {ts(s.start + s.duration)}\n{s.text}\n" for s in tr]
        (raw / "vtt" / f"{vid}.en.vtt").write_text("\n".join(lines)); print("OK", vid)
    except Exception as e:
        print("FAIL", vid, type(e).__name__)
