"""VTT de YouTube -> markdown con bloques de ~30s y timestamp [mm:ss], sin líneas repetidas."""
import re, sys, pathlib

def parse(path):
    cues, start = [], None
    for line in path.read_text(errors="ignore").splitlines():
        m = re.match(r"(\d+):(\d+):(\d+)\.\d+ -->", line)
        if m:
            h, mi, s = map(int, m.groups()); start = h * 3600 + mi * 60 + s; continue
        txt = re.sub(r"<[^>]+>", "", line).strip()
        if start is None or not txt or txt.startswith(("WEBVTT", "Kind:", "Language:")): continue
        if cues and cues[-1][1] == txt: continue
        cues.append((start, txt))
    seen, out = set(), []
    for t, txt in cues:
        if txt in seen: continue
        seen.add(txt); out.append((t, txt))
    return out

def blocks(cues, size=30):
    cur, t0 = [], None
    for t, txt in cues:
        if t0 is None: t0 = t
        if t - t0 >= size and cur:
            yield t0, " ".join(cur); cur, t0 = [], t
        cur.append(txt)
    if cur: yield t0, " ".join(cur)

src, dst = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
meta = {l.split("|")[0]: l.rstrip("\n").split("|") for l in (src / "meta.txt").read_text().splitlines() if l}
for vid in sorted({p.name.split(".")[0] for p in (src / "vtt").glob("*.vtt")}):
    cands = [src / "vtt" / f"{vid}.en.vtt", src / "vtt" / f"{vid}.en-orig.vtt"]
    f = next((c for c in cands if c.exists()), None)
    if not f: continue
    m = meta.get(vid, [vid, "", "", "", ""])
    lines = [f"# {m[4]}", "", f"- id: {vid}", f"- url: https://www.youtube.com/watch?v={vid}",
             f"- upload_date: {m[1]}", f"- duration_s: {m[2]}", f"- views: {m[3]}", ""]
    lines += [f"[{t//60:02d}:{t%60:02d}] {b}" for t, b in blocks(parse(f))]
    (dst / f"{vid}.md").write_text("\n".join(lines) + "\n")
print(len(list(dst.glob("*.md"))), "transcripts")
