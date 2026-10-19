---
id: H-065
title: "UFC: “no llega a la decisión” y favoritos"
kind: market
sport: ufc
status: untested
n_videos: 6
n_variants: 7
first_mention: 2022-06-14
last_mention: 2026-07-10
---

# H-065 · UFC: “no llega a la decisión” y favoritos

**Estado:** ⬜ sin probar · 📊 se puede probar con datos de mercado

## Qué dice
UFC: “la pelea no llega a la decisión” cuando ambos peleadores terminan ≥80-85% de sus peleas, pelea en el Apex con total de 1.5, en peleas femeninas “llega a la decisión” y ML del favorito con edge ≥5%.

## Lectura previa (antes de los datos)
El finish rate de cada peleador es informativo, pero las muestras son chicas (10-20 peleas).

## Plan de prueba
Con UFCStats, P(finish) en función del finish rate de ambos, la división y el Apex, comparada con el precio de “doesn't go the distance”.

## Variantes (7) y videos (6)

### `ufc-apex-total-1-5-fight-doesnt-go-distance`
- [0e__XxLXcu8](https://www.youtube.com/watch?v=0e__XxLXcu8) (2022-06-14) 3-Step Sports Betting Strategy For UFC That Hits At A High %
  - Condición → apuesta: pelea en el UFC Apex + total de rounds en 1.5 → "No llega a la distancia"
  - Claim: "pega a un porcentaje muy alto" (sin cifra); precio -180 a -250

### `ufc-fight-not-go-distance-finishers-filter`
- [0tB326SZyPY](https://www.youtube.com/watch?v=0tB326SZyPY) (2026-06-11) The UFC Bet That Wins 85% of the Time
  - Condición → apuesta: línea de rounds 1.5 + ambos ≥80% finish rate (≥8 peleas) + precio -250 a -500 + sin exclusiones → apostar "no llega a decisión"
  - Claim: 85% de acierto, ROI ~18%

### `ufc-avoid-method-of-victory-props`
- [0tB326SZyPY](https://www.youtube.com/watch?v=0tB326SZyPY) (2026-06-11) The UFC Bet That Wins 85% of the Time
  - Condición → apuesta: siempre → evitar; preferir el mercado agregado de finalización
  - Claim: la probabilidad standalone de "X por KO" es menor de lo que la gente cree (sin cifra)

### `ufc-womens-fights-goes-distance-over-late-rounds`
- [2ncgokeGPHI](https://www.youtube.com/watch?v=2ncgokeGPHI) (2026-06-21) I Gave AI $55,000 To Bet UFC On Kalshi
  - Condición → apuesta: pelea femenina donde gusta el over 2.5 rounds → tomar "goes the distance" (finalizaciones tardías poco frecuentes)
  - Claim: "es básicamente lo mismo" (sin cifra)

### `ufc-fight-not-go-distance-both-high-finishers`
- [Sf-uWz9YhrE](https://www.youtube.com/watch?v=Sf-uWz9YhrE) (2026-06-12) UFC Freedom 250 Bet That Wins 91% of the Time
  - Condición → apuesta: ambos peleadores con tasa de finalización > 85% → "no llega a la distancia" si el precio implica menos que la estimación (min tasa + bono)
  - Claim: probabilidad real 91.5% vs 79% implícito, edge ~12.5 pts

### `ufc-ml-favorite-when-model-edge-5pct`
- [n6r_drytEYA](https://www.youtube.com/watch?v=n6r_drytEYA) (2026-07-10) WHO WINS MCGREGOR VS  HOLLOWAY 2? (UFC 329 Breakdown & Predictions)
  - Condición → apuesta: probabilidad proyectada por el modelo ≥ implícita + ~5 pts y precio igual o mejor al objetivo → favorito ML
  - Claim: ~5% de edge en cada pick (5.0, 4.96, 4.97, 4.47%) [06:09]

### `ufc-fight-doesnt-go-distance`
- [pr7uicYs23Q](https://www.youtube.com/watch?v=pr7uicYs23Q) (2026-07-02) I Hit 100% Of My Bets Using AI
  - Condición → apuesta: pelea seleccionada por la IA → "no va a la distancia"
  - Claim: parte del 26-0

## Relaciones
- Índice: [index](../index.md) · Contradicciones: [contradictions](../contradictions.md) · Evolución: [timeline](../timeline.md)
