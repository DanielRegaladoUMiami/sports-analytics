"""QA automático: timestamps dentro de la duración y números de la nota presentes en el transcript."""
import re, sys, pathlib, statistics
root = pathlib.Path(sys.argv[1])
W = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9","ten":"10","twenty":"20","thirty":"30","forty":"40","fifty":"50","sixty":"60","seventy":"70","eighty":"80","ninety":"90","hundred":"100"}
rows = []
for p in sorted((root / "videos").glob("*.md")):
    t = root / "raw/transcripts" / p.name
    if not t.exists(): continue
    note, tr = p.read_text(errors="ignore"), t.read_text(errors="ignore").lower()
    dur = re.search(r"duration_s:\s*(\d+)", tr); dur = int(dur.group(1)) if dur else None
    ts = [int(m) * 60 + int(s) for m, s in re.findall(r"\[(\d{1,3}):(\d{2})", note)]
    over = [x for x in ts if dur and x > dur + 30]
    body = re.search(r"## Ideas clave(.*?)## Reglas", note, re.S)
    body = (body.group(1) if body else "") + (re.search(r"## Números y claims(.*?)## ", note, re.S) or [None, ""])[1]
    body = re.sub(r"\[\d{1,3}:\d{2}\]", "", body)
    nums = set(re.findall(r"(?<![\d.])(\d{2,6})(?![\d])", body.replace(",", "")))
    trn = " ".join(W.get(w, w) for w in re.findall(r"[a-z]+|\d[\d,.]*", tr)).replace(",", "")
    found = sum(1 for n in nums if re.search(rf"(?<!\d){n}(?!\d)", trn))
    rows.append((p.stem, len(ts), len(over), len(nums), found / len(nums) if nums else 1.0))
print("notes:", len(rows))
print("notes with timestamps beyond duration:", sum(1 for r in rows if r[2]), [r[0] for r in rows if r[2]][:10])
print("notes with 0 timestamps:", sum(1 for r in rows if r[1] == 0))
cov = [r[4] for r in rows]
print("number-match rate: median %.0f%%, p10 %.0f%%" % (100 * statistics.median(cov), 100 * sorted(cov)[len(cov) // 10]))
for r in sorted(rows, key=lambda r: r[4])[:8]: print("  low:", r[0], "nums", r[3], "match %.0f%%" % (100 * r[4]))
