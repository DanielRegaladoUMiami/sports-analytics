"""Extrae reglas accionables (slugs) y metadata de videos/*.md -> raw/rules.tsv y raw/videos.tsv."""
import re, sys, pathlib
root = pathlib.Path(sys.argv[1]); rows, vids = [], []
for p in sorted((root / "videos").glob("*.md")):
    s = p.read_text(errors="ignore")
    fm = dict(re.findall(r"^(\w+):\s*(.*)$", s.split("---")[1], re.M)) if s.startswith("---") else {}
    vids.append((p.stem, fm.get("upload_date", ""), fm.get("type", ""), fm.get("sports", ""), fm.get("topics", ""), fm.get("title", "").strip('"')))
    sec = re.search(r"## Reglas accionables(.*?)(\n## |\Z)", s, re.S)
    if not sec: continue
    for slug in re.findall(r"^\s*-\s*\*\*`?([a-z0-9][a-z0-9.\-]+)`?\*\*", sec.group(1), re.M):
        rows.append((slug, p.stem))
(root / "raw/rules.tsv").write_text("\n".join("\t".join(r) for r in rows) + "\n")
(root / "raw/videos.tsv").write_text("\n".join("\t".join(v) for v in vids) + "\n")
print(len(vids), "videos;", len(rows), "rule mentions;", len({r[0] for r in rows}), "unique slugs")
