#!/usr/bin/env bash
# Descarga subtítulos (en, auto si no hay manuales) + metadata de todos los videos largos del canal.
set -u
R="$(cd "$(dirname "$0")/.." && pwd)"
cut -d"|" -f1 "${LIST:-$R/raw/video_list.txt}" | sed 's#^#https://www.youtube.com/watch?v=#' > "$R/raw/urls.txt"
uvx yt-dlp --skip-download --write-subs --write-auto-subs --sub-langs "en" --sub-format vtt \
  --sleep-requests 0.5 --sleep-subtitles 1 --retries 10 --extractor-retries 5 \
  --download-archive "$R/raw/archive.txt" --no-overwrites \
  --print-to-file "%(id)s|%(upload_date)s|%(duration)s|%(view_count)s|%(title)s" "$R/raw/meta.txt" \
  -o "$R/raw/vtt/%(id)s.%(ext)s" -a "$R/raw/urls.txt"
