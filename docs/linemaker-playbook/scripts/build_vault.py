"""Genera hypotheses/, topics/ e index.md a partir de videos/*.md.
Uso: python3 -I scripts/build_vault.py <vault_root>
Se puede volver a correr: sobrescribe hypotheses/, topics/ e index.md. contradictions.md y timeline.md son manuales."""
import collections
import pathlib
import re
import sys

ROOT = pathlib.Path(sys.argv[1])
sys.path.insert(0, str(ROOT / "scripts"))
from clusters import CLUSTERS, cluster_of  # noqa: E402
from hypotheses_text import T  # noqa: E402

TOPIC_TEXT = {
    "bankroll": "Cuánto capital, cómo protegerlo y cuándo retirar. Su postura más estable es “no apuestes lo que no puedes perder”. El mínimo cambia: $50, $500, $1k, $3-5k según el video.",
    "unit-sizing": "El tema donde más se contradice: unidad de 1%, 1-2%, 1-3%, 2%, “exactamente 3%”, 3-5% agresivo, 5% con bankroll chico, $25k fijos. Ver [[P-001-unit-sizing]].",
    "mindset-discipline": "Tilt, no perseguir pérdidas, paciencia, pensar a largo plazo (la analogía de la moneda al 85%). Es su contenido más consistente y el menos técnico.",
    "heavy-favorites": "Su producto principal desde ~2022: favoritos de −200 a −700, sobre todo en props y líneas alternas. Ver [[H-001-heavy-favorites-true-prob]] y [[H-003-avoid-minus110]].",
    "parlays-sgp": "Dice que los parlays son “lotería” y vende parlays de patas al 90%. Ver [[H-005-high-prob-leg-parlays]], [[H-006-sgp-correlated]] y [[H-007-no-parlays]].",
    "player-props": "El mercado donde dice estar el edge (un solo jugador, matchup claro). Over si el matchup favorece al jugador, under si no.",
    "sides-totals": "Spreads, ML y totales. Al principio (2020-21) era su mercado principal y después dice que hay que “ignorarlos”, aunque sigue vendiendo sistemas de totales.",
    "implied-probability-ev": "Probabilidad implícita contra “probabilidad real”. El concepto está bien, pero se equivoca a menudo: −200 lo da como 60% o 80% (es 66.7%), confunde el gap de probabilidad con el EV y trata muestras chicas como el 100%.",
    "line-shopping": "Comparar precios entre casas. Coincide con el consenso sharp, aunque a veces desprecia el +EV que sale de las diferencias de precio. Ver [[H-011-line-shopping-price-discrepancy]].",
    "research-process": "Su checklist: matchup/DvP, hit rate de la temporada, H2H, movimiento de línea, dinero contra tickets, clima. Desde 2026 dice que su IA lo hace “en segundos”.",
    "live-betting": "Medios live en la NBA, comprar al favorito pregame después de un mal inicio, props después del primer cuarto. Casi siempre asume que la probabilidad pregame no cambia. Ver [[H-041-nba-live]].",
    "bet-timing": "Apostar cerca del inicio (después de lineups y noticias) o temprano en props. Se contradice: 1 hora, 2-3 horas o 5-10 minutos antes.",
    "prediction-markets": "Kalshi, Polymarket y Novig: comprar “No” en longshots, comparar con las casas y mudarse ahí cuando lo limitan. Ver [[H-012-prediction-markets]].",
    "sportsbook-limits": "Cómo evitar que lo limiten: repartir apuestas, montos redondos, parlays basura, cuentas de familiares y multicuenta (contra los términos de servicio). Ver [[P-005-beating-account-limits]].",
    "cappers-scams": "Cómo reconocer servicios de picks falsos: sin tracker, solo favoritos, tickets enormes. Varios de sus criterios también se le aplican a él.",
    "proof-tracking": "Trackers y reportes mensuales. Los reportes reales (2021-22, 2025) muestran meses de −9u a +26u y win rates de 60-75% con odds juiceados, mucho más modestos que los títulos.",
    "betting-vs-investing": "Compara las apuestas con la bolsa y el S&P. Dice que la bolsa “nunca tuvo un año de +50%” (1954 tuvo ~+47%) y en otro video que la bolsa también es apostar.",
    "bet-types-explained": "Explica ML, spread, totales, teasers, round robins, odds e implícitas. Hay errores en round robins (3 picks dan 3 parlays) y en break-evens.",
    "personal-story": "Su historia de origen (cuánto le costó aprender: $50k, $100k o “miles”; empezó con $500 o con $2,500), pérdidas grandes (Argentina-España $50k) y su aparición en Dr. Phil.",
    "sales-funnel": "Casi todos los videos terminan vendiendo membresía, coaching, Line Maker AI (desde 2026) o afiliados (OddsJam, BetUS, referidos de Kalshi). Tenerlo en cuenta al leer cada claim.",
}


def parse_note(p):
    s = p.read_text(errors="ignore")
    fm = {}
    if s.startswith("---"):
        fm = dict(re.findall(r"^(\w+):\s*(.*)$", s.split("---")[1], re.M))
    tldr = re.search(r"\*\*TL;DR:\*\*\s*(.+)", s)
    rules = {}
    sec = re.search(r"## Reglas accionables(.*?)(\n## |\Z)", s, re.S)
    if sec:
        for blk in re.split(r"\n(?=\s*-\s*\*\*)", sec.group(1)):
            m = re.match(r"\s*-\s*\*\*`?([a-z0-9][a-z0-9.\-]+)`?\*\*", blk)
            if not m:
                continue
            cond = re.search(r"Condici[oó]n[^:]*:\s*(.+)", blk)
            claim = re.search(r"Claim[^:]*:\s*(.+)", blk)
            rules[m.group(1)] = (cond.group(1).strip() if cond else "", claim.group(1).strip() if claim else "")
    lst = lambda k: [x.strip() for x in fm.get(k, "").strip("[]").split(",") if x.strip()]
    return {
        "id": p.stem,
        "title": fm.get("title", p.stem).strip('"'),
        "date": fm.get("upload_date", ""),
        "type": fm.get("type", ""),
        "sports": lst("sports"),
        "topics": lst("topics"),
        "tldr": tldr.group(1).strip() if tldr else "",
        "rules": rules,
    }


notes = [parse_note(p) for p in sorted((ROOT / "videos").glob("*.md"))]
by_id = {n["id"]: n for n in notes}
meta = {c[0]: c for c in CLUSTERS}
fname = {cid: f"{cid}-{c[1]}" for cid, c in meta.items()}

# --- hipótesis ---
hyp = collections.defaultdict(lambda: collections.defaultdict(list))  # cid -> slug -> [(note, cond, claim)]
for n in notes:
    for slug, (cond, claim) in n["rules"].items():
        cid = cluster_of(slug)
        if cid:
            hyp[cid][slug].append((n, cond, claim))

hdir = ROOT / "hypotheses"
for old in hdir.glob("*.md"):
    old.unlink()
summary = []
for cid, slug_, title, kind, sport, _ in CLUSTERS:
    variants = hyp.get(cid, {})
    vids = sorted({v[0]["id"] for vs in variants.values() for v in vs}, key=lambda i: by_id[i]["date"])
    dates = [by_id[i]["date"] for i in vids if by_id[i]["date"]]
    que, prior, plan = T.get(cid, ("", "", ""))
    out = [
        "---", f"id: {cid}", f'title: "{title}"', f"kind: {kind}", f"sport: {sport}",
        "status: untested", f"n_videos: {len(vids)}", f"n_variants: {len(variants)}",
        f"first_mention: {min(dates) if dates else ''}", f"last_mention: {max(dates) if dates else ''}", "---", "",
        f"# {cid} · {title}", "",
        "**Estado:** ⬜ sin probar · " + {"market": "📊 se puede probar con datos de mercado", "practice": "🧭 práctica / proceso", "fallacy": "⚠️ falacia"}[kind], "",
        "## Qué dice", que, "", "## Lectura previa (antes de los datos)", prior, "", "## Plan de prueba", plan, "",
        f"## Variantes ({len(variants)}) y videos ({len(vids)})",
    ]
    for slug in sorted(variants, key=lambda s: -len(variants[s])):
        out.append(f"\n### `{slug}`")
        for n, cond, claim in sorted(variants[slug], key=lambda v: v[0]["date"]):
            bits = [f"[[{n['id']}]] ({n['date']}) {n['title']}"]
            if cond:
                bits.append(f"  - Condición → apuesta: {cond}")
            if claim:
                bits.append(f"  - Claim: {claim}")
            out.append("- " + "\n".join(bits))
    out += ["", "## Relaciones", "- Índice: [[index]] · Contradicciones: [[contradictions]] · Evolución: [[timeline]]"]
    (hdir / f"{fname[cid]}.md").write_text("\n".join(out) + "\n")
    summary.append((cid, title, kind, sport, len(vids), len(variants), min(dates) if dates else "", max(dates) if dates else ""))

# --- temas ---
tdir = ROOT / "topics"
for old in tdir.glob("*.md"):
    old.unlink()
topic_vids = collections.defaultdict(list)
for n in notes:
    for t in n["topics"]:
        topic_vids[t].append(n)
topic_hyps = collections.defaultdict(collections.Counter)
for cid, variants in hyp.items():
    for vs in variants.values():
        for n, *_ in vs:
            for t in n["topics"]:
                topic_hyps[t][cid] += 1
for t, text in TOPIC_TEXT.items():
    vs = sorted(topic_vids.get(t, []), key=lambda n: n["date"])
    out = ["---", f"topic: {t}", f"n_videos: {len(vs)}", "---", "", f"# Tema: {t}", "", text, ""]
    if topic_hyps[t]:
        out.append("## Hipótesis relacionadas")
        out += [f"- [[{fname[c]}]] ({k} menciones)" for c, k in topic_hyps[t].most_common(8)]
        out.append("")
    out.append(f"## Videos ({len(vs)}, cronológico)")
    out += [f"- {n['date']} · [[{n['id']}]] **{n['title']}** — {n['tldr']}" for n in vs]
    (tdir / f"topic-{t}.md").write_text("\n".join(out) + "\n")

# --- índice ---
yr = collections.Counter(n["date"][:4] for n in notes)
sp = collections.Counter(s for n in notes for s in n["sports"])
idx = [
    "# LINEMAKER SPORTS: playbook + hipótesis", "",
    f"Vault con {len(notes)} notas de video (de 418 videos largos; 4 sin transcript disponible). "
    "Cada regla que da el canal se convierte en una hipótesis que se puede probar. Las notas son paráfrasis en español, con citas [mm:ss] al video original.", "",
    "**Por dónde empezar:** [[timeline]] (cómo cambió su método), [[contradictions]] (en qué se contradice), las hipótesis 📊 con más videos, y los temas.", "",
    "## Hipótesis de mercado (se pueden probar con datos)", "",
    "| ID | Hipótesis | Deporte | Videos | Variantes | Período |", "|---|---|---|---|---|---|",
]
for cid, title, kind, sport, nv, nvar, d0, d1 in sorted(summary, key=lambda r: -r[4]):
    if kind == "market":
        idx.append(f"| [[{fname[cid]}\\|{cid}]] | {title} | {sport} | {nv} | {nvar} | {d0[:7]} → {d1[:7]} |")
idx += ["", "## Prácticas, bankroll y falacias", "", "| ID | Regla | Videos | Variantes |", "|---|---|---|---|"]
for cid, title, kind, sport, nv, nvar, *_ in sorted(summary, key=lambda r: -r[4]):
    if kind != "market":
        idx.append(f"| [[{fname[cid]}\\|{cid}]] | {title}{' ⚠️' if kind == 'fallacy' else ''} | {nv} | {nvar} |")
idx += ["", "## Temas", ""]
idx += [f"- [[topic-{t}]] ({len(topic_vids.get(t, []))} videos)" for t in sorted(TOPIC_TEXT, key=lambda t: -len(topic_vids.get(t, [])))]
idx += ["", "## Cobertura", "", "Videos por año: " + " · ".join(f"{y}: {yr[y]}" for y in sorted(yr)), "",
        "Videos por deporte: " + " · ".join(f"{s}: {k}" for s, k in sp.most_common()), "",
        "## Pendientes", "- Transcripts inservibles (re-transcribir con Whisper): [[X0AF830t56c]], [[4y5BbDgCHmA]], [[BKfBmR6t5EU]].",
        "- Sin transcript en YouTube: TuIDubP-_B4, cWZ9Au5uqy0, UqIYxJa5JJQ (subtítulos desactivados), NQZw1H8hXsM (restricción de edad).",
        "", "## Cómo se construyó", "Ver [[README]] y [[CONVENTIONS]]."]
(ROOT / "index.md").write_text("\n".join(idx) + "\n")
print(f"{len(summary)} hypotheses, {len(TOPIC_TEXT)} topics, index.md")
