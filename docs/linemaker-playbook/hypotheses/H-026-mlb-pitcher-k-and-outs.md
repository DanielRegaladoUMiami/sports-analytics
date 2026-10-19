---
id: H-026
title: "MLB: strikeouts y outs del abridor"
kind: market
sport: mlb
status: untested
n_videos: 6
n_variants: 6
first_mention: 2022-07-19
last_mention: 2026-09-01
---

# H-026 · MLB: strikeouts y outs del abridor

**Estado:** ⬜ sin probar · 📊 se puede probar con datos de mercado

## Qué dice
MLB: over de strikeouts del abridor cuando el hit rate de la temporada > implícita, ajustado por el K% del rival; over de outs para los que lanzan muchas entradas; K en el primer turno al bate del peor bateador.

## Lectura previa (antes de los datos)
Los props de K son de los mercados más estudiados (hay modelos públicos), así que hay poco margen. Los de outs dependen del manejo del bullpen.

## Plan de prueba
Usar un modelo de K (K% del pitcher × K% del rival × BF esperados) y comparar contra líneas de cierre.

## Variantes (6) y videos (6)

### `mlb-pitcher-k-over-low-line-season-hit-rate`
- [1s5uMlqAmm8](https://www.youtube.com/watch?v=1s5uMlqAmm8) (2026-09-01) 30-4 Run Best MLB Props Tuesday 9/1/26
  - Condición → apuesta: % de aperturas de la temporada sobre la línea actual − prob. implícita ≥ ~5 pts (y rival con tasa de K media/alta) → over
  - Claim: racha de "30-4" (título); edges de +4.6 a +15.4 pts

### `mlb-pitcher-strikeouts-heavy-favorite-edge`
- [762Q8K6W8fc](https://www.youtube.com/watch?v=762Q8K6W8fc) (2025-08-04) Why the Best Sports Bettors Don’t Gamble (They Multiply Their Edge)
  - Condición → apuesta: prob. estimada de over K (p.ej. 85%) > implícita de la cuota (-200/-220 ≈ 67-69%) → over
  - Claim: ejemplo hipotético de 85%

### `mlb-pitcher-k-over-hitrate-adj-opp-k-rate`
- [Ie5VMuCwtNU](https://www.youtube.com/watch?v=Ie5VMuCwtNU) (2025-07-28) How The Wealthy Consistently Win In Sports Betting
  - Condición → apuesta: % de salidas superando la línea > implícita **y** rival en el bottom-5 de evitar ponches (alto K%) → over; si el rival es top en contacto, restar ~10 pp y normalmente pasar
  - Claim: ejemplo de +9 pp; ganó 1 caso (Wheeler 8 K)

### `mlb-first-ab-strikeout-weak-hitter`
- [VsklOUwl57U](https://www.youtube.com/watch?v=VsklOUwl57U) (2024-08-02) This Sports Bettor Doubled His Bankroll After Learning The Linemaker Method
  - Condición → apuesta: peor bateador del lineup (alto K%) en su primer turno → strikeout a +200/+300; máximo 1–2 por partido
  - Claim: el miembro acertó 2 de 2

### `mlb-pitcher-outs-over-hist-rate-vs-implied`
- [baNtraY2EgA](https://www.youtube.com/watch?v=baNtraY2EgA) (2023-09-25) The True Value System: Linemaker Sports' SECRET to a 70% Win Rate!
  - Condición → apuesta: % de salidas de la temporada en que superó la línea > probabilidad implícita → over
  - Claim: ~3% de edge en el ejemplo; "70% win rate" en el título

### `mlb-pitcher-outs-over-workhorse`
- [muUH-9zFVBc](https://www.youtube.com/watch?v=muUH-9zFVBc) (2022-07-19) New Sports Betting App That Finds You (Almost) 70% Winners!
  - Condición → apuesta: abridor "workhorse" con hit rate alto sobre la línea (~20.5 outs) y precio menor que su prob. histórica → over
  - Claim: 72% de aciertos en últimos 25 (13/18)

## Relaciones
- Índice: [index](../index.md) · Contradicciones: [contradictions](../contradictions.md) · Evolución: [timeline](../timeline.md)
