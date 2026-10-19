---
id: H-003
title: "Evitar líneas −110 / main lines"
kind: market
sport: multi
status: untested
n_videos: 8
n_variants: 5
first_mention: 2022-09-20
last_mention: 2026-10-14
---

# H-003 · Evitar líneas −110 / main lines

**Estado:** ⬜ sin probar · 📊 se puede probar con datos de mercado

## Qué dice
Evitar las líneas −110 porque, según él, son ≤50% y no tienen edge. Prefiere favoritos juiceados.

## Lectura previa (antes de los datos)
Hay un error lógico: en un mercado −110/−110 al menos un lado es ≥50%. Que el −110 tenga poco edge en promedio no implica que el −300 tenga más. El sesgo favorito-longshot existe en algunos mercados, pero hay que medirlo.

## Plan de prueba
Calcular el ROI histórico por bucket de odds (−110, −150, −200, −300, −500) en props y sides, usando precios de cierre. Es un test descriptivo directo del sesgo favorito-longshot.

## Variantes (5) y videos (8)

### `multi-avoid-minus110-props`
- [ZDyYkXUtTJY](https://www.youtube.com/watch?v=ZDyYkXUtTJY) (2025-01-13) Most Profitable Sports Betting Strategy? (+EV Sports Betting Explained)
  - Condición → apuesta: evitar líneas -110
  - Claim: casi todas tienen ≤50% (a veces 40%)
- [Sw2kRfHVRPA](https://www.youtube.com/watch?v=Sw2kRfHVRPA) (2025-05-12) Sports Betting Is A Video Game. Here's How To Win Consistently.
  - Condición → apuesta: jugadas -110 → evitarlas (claim: prob. real < 55%)
  - Claim: casi ninguna jugada -110 supera el umbral de 52.4–55%
- [_AAUS3Wrtho](https://www.youtube.com/watch?v=_AAUS3Wrtho) (2025-09-04) 5 Sports Betting Habits That Made Me Rich
  - Condición → apuesta: evitar líneas principales -110
  - Claim: nadie gana 54–55% a -110 de forma sostenida

### `avoid-minus-110-main-lines-props`
- [eCrEWE5lLqU](https://www.youtube.com/watch?v=eCrEWE5lLqU) (2025-02-11) What Everyone Gets Wrong About Gambling on Sports
  - Condición → apuesta: no apostar líneas -110 (dice que su prob. real suele ser <50%); buscar favoritos -200 con 70-80%
  - Claim: nadie sostiene 55-58% a -110
- [cimeXxqoy1k](https://www.youtube.com/watch?v=cimeXxqoy1k) (2026-10-14) The NFL SGP That Almost Never Loses (86% Win Rate)
  - Condición → apuesta: preferir alt lines bajas con gap positivo sobre la línea -110 (que suele tener hit rate < 52.4% en su ejemplo)
  - Claim: las líneas -110 son -EV de forma sistemática

### `heavy-favorites-less-mispriced-than-minus110`
- [EraFwb5giTE](https://www.youtube.com/watch?v=EraFwb5giTE) (2026-07-13) Most Bettors Are Wrong About Favorites
  - Condición → apuesta: preferir cuotas de -250 a -400 frente a -110, porque las casas ponen menos margen o se equivocan más a favor del apostador en favoritas fuertes
  - Claim: a -110 nadie gana a largo plazo; a -300 aparecen prob. reales del 80-100%

### `multi-accept-juiced-odds-not-only-minus110`
- [PR6zkoH-HoY](https://www.youtube.com/watch?v=PR6zkoH-HoY) (2022-09-20) This Sports Betting Myth Is Causing You To Make Bad Bets And Lose...
  - Condición → apuesta: no descartar apuestas a -150/-200 por el juice; evaluarlas igual que una de -110
  - Claim: limitarse a -110 es "receta para perder"

### `favor-heavy-favorite-props-over-minus-110`
- [baNtraY2EgA](https://www.youtube.com/watch?v=baNtraY2EgA) (2023-09-25) The True Value System: Linemaker Sports' SECRET to a 70% Win Rate!
  - Condición → apuesta: preferir líneas cortas (alt) donde la frecuencia histórica supera la implícita, en vez de líneas -110
  - Claim: el valor se esconde en cuotas altas porque el público las evita

## Relaciones
- Índice: [index](../index.md) · Contradicciones: [contradictions](../contradictions.md) · Evolución: [timeline](../timeline.md)
