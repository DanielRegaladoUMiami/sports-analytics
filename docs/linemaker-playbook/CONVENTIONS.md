# Convenciones del vault

Vault de Markdown estilo Obsidian. Los enlaces usan `[[nombre-de-archivo-sin-.md]]`.

## Carpetas
- `raw/transcripts/<id>.md`: transcript limpio con bloques `[mm:ss]`. **Solo uso local/personal, no se publica.**
- `videos/<id>.md`: una nota por video (plantilla abajo). Se escribe en español y se parafrasea; las citas textuales van en una sola frase corta.
- `topics/<topic>.md`: síntesis por tema, enlaza a los videos.
- `hypotheses/H-###-<slug>.md`: reglas accionables consolidadas, con estado de validación.
- `index.md`: mapa general.

## Vocabulario controlado (usar SOLO estos slugs en `topics:` y en los enlaces `[[topic-...]]`)
Temas: `bankroll`, `unit-sizing`, `mindset-discipline`, `heavy-favorites`, `parlays-sgp`, `player-props`,
`sides-totals`, `implied-probability-ev`, `line-shopping`, `research-process`, `live-betting`,
`bet-timing`, `prediction-markets` (Kalshi/Polymarket), `sportsbook-limits`, `cappers-scams`,
`proof-tracking` (trackers, reportes mensuales), `betting-vs-investing`, `bet-types-explained`,
`personal-story` (anécdotas, pérdidas grandes), `sales-funnel` (promos de su membresía).

Deportes: `mlb`, `nfl`, `nba`, `nhl`, `ncaaf`, `ncaab`, `wnba`, `soccer`, `tennis`, `golf`, `ufc`, `horse-racing`, `multi`.

Tipo de video (`type`): `strategy`, `bankroll`, `mindset`, `sport-specific-system`, `proof-report`,
`daily-picks`, `story`, `explainer`, `tools-research`.

## Plantilla `videos/<id>.md`

```markdown
---
id: <id>
title: "<título>"
url: https://www.youtube.com/watch?v=<id>
upload_date: YYYY-MM-DD
views: <n>
type: <type>
sports: [mlb, nfl]
topics: [heavy-favorites, player-props]
---

# <título>

**TL;DR:** 2-3 líneas en español.

## Ideas clave
- Idea parafraseada [mm:ss]

## Reglas accionables
<!-- Una por regla concreta que se pueda testear. Si no hay, escribir "Ninguna". -->
- **rule-slug-descriptivo** (ej. `mlb-under-player-runs-scored`)
  - Deporte / mercado: mlb / player runs scored
  - Condición → apuesta: siempre → under 0.5
  - Claim: win rate / odds / ROI que él da (o "ninguno")
  - Evidencia que muestra: tracker, anécdota, ninguna
  - Cómo probarlo: datos y métrica (hit rate vs prob. implícita sin vig, CLV)
  - Fuente: [mm:ss]

## Números y claims
- Bankroll, unidades, win rates, ROI, montos ganados/perdidos [mm:ss]

## Señales de alerta
- Claims sin evidencia, contradicciones, venta de membresía, sesgo de selección.

## Relaciones
- Temas: [topic-bankroll](topics/topic-bankroll.md), [topic-player-props](topics/topic-player-props.md)
- Videos que menciona o con los que se relaciona: [[<id>]] — por qué
```
