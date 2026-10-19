---
id: H-001
title: "Favoritos pesados (−200 a −700) cuando prob. “real” > implícita"
kind: market
sport: multi
status: untested
n_videos: 29
n_variants: 14
first_mention: 2023-08-18
last_mention: 2026-09-16
---

# H-001 · Favoritos pesados (−200 a −700) cuando prob. “real” > implícita

**Estado:** ⬜ sin probar · 📊 se puede probar con datos de mercado

## Qué dice
Es el núcleo de su método desde ~2022 y domina 2025-2026. Apostar favoritos pesados (casi siempre props o líneas alternas) entre −200 y −700, solo cuando su “probabilidad real” supera la implícita. La “probabilidad real” casi siempre es el hit rate de la temporada, o el promedio entre el hit rate de la temporada y el hit rate contra defensas similares.

## Lectura previa (antes de los datos)
Para que tenga sentido, la probabilidad tiene que estar bien calibrada **sin vig** y medirse contra el precio de cierre. Su estimador (hit rate muestral de 10-40 juegos) es ruidoso y está sesgado hacia arriba por selección. Su propio tracker 2025 (75% a −241 promedio, break-even 70.7%) apunta a un edge chico (~+6% por apuesta), muy lejos del 85% que vende. Los props tienen hold alto, así que la implícita sin vig es menor que la que él usa.

## Plan de prueba
Reunir líneas históricas de props alternas (OddsJam/The Odds API/Unabated, o snapshots propios) junto con los resultados. Para cada apuesta que cumpla la regla: hit rate frente a la implícita sin vig, ROI por bucket de odds (−200/−300/−500/−700), CLV, e intervalo de confianza con Wilson o bootstrap. Hacer walk-forward: estimar el hit rate solo con datos anteriores a la fecha.

## Variantes (14) y videos (29)

### `true-edge-heavy-favorite-props`
- [7bpBUYJLqRQ](https://www.youtube.com/watch?v=7bpBUYJLqRQ) (2025-02-13) You'll Never Bet On Sports The Same After Watching This
  - Condición → apuesta: prob. real estimada > implícita → apostar; nunca jugar favoritas "a ciegas"
  - Claim: 83% de acierto en el año, +11.33u en ~6 semanas
- [7FdbUxX286M](https://www.youtube.com/watch?v=7FdbUxX286M) (2025-05-15) This Sports Betting Strategy Consistently Makes 30%+ ROI Every Year
  - Condición → apuesta: prob. modelo − prob. no-vig > 0 → apostar
  - Claim: ≥30% ROI anual; 46u y 60u
- [E2fLhLeZp2o](https://www.youtube.com/watch?v=E2fLhLeZp2o) (2025-12-12) The 3 Sports Betting Principles That Will Make Anyone Rich
  - Condición → apuesta: prob. real ≥ implícita + ~13 pp → apostar en simples de tamaño fijo
  - Claim: "la estrategia más rentable de la historia de las apuestas"
- [BoFRfXNvHHk](https://www.youtube.com/watch?v=BoFRfXNvHHk) (2026-03-27) The Sports Betting Strategy That's Printing Money in 2026 (Full Breakdown)
  - Condición → apuesta: prob. real > implícita → apostar; evitar moneylines
  - Claim: 79.5% de acierto a -331, ROI ~10%, ~$35K en ~3 meses
- [EU5iIchgoJc](https://www.youtube.com/watch?v=EU5iIchgoJc) (2026-04-13) The $100,000 Mistake That Taught Me How to Win at Sports Betting
  - Condición → apuesta: prob. real (temporada + rivales similares) > implícita → apostar; evitar moneylines
  - Claim: su sistema "de alta probabilidad" de 10+ años
- [APSRbsyjlRI](https://www.youtube.com/watch?v=APSRbsyjlRI) (2026-04-17) The Betting Strategy That Got Me to 83% Win Rate (Here's Exactly Why)
  - Condición → apuesta: prob. real > implícita → apostar aunque sea -500
  - Claim: 83% de acierto
- [EraFwb5giTE](https://www.youtube.com/watch?v=EraFwb5giTE) (2026-07-13) Most Bettors Are Wrong About Favorites
  - Condición → apuesta: prob. real > implícita a ~-300 → apostar
  - Claim: "la única forma de ganar a largo plazo"

### `heavy-favorites-minus200-400-with-edge`
- [OLJCL1JpsI0](https://www.youtube.com/watch?v=OLJCL1JpsI0) (2023-08-18) Sports Betting Became WAY Easier After I Stopped Doing This One Thing...
  - Condición → apuesta: favoritos -200/-300 con factores adicionales que eleven la prob. estimada a 70-75%
  - Claim: su tracker mostró que los favoritos caros ganaban y los -110/plus money perdían
- [Q6Ww7S1llAI](https://www.youtube.com/watch?v=Q6Ww7S1llAI) (2025-02-06) I Got Rich Sports Betting When I Applied These 2 Habits
  - Condición → apuesta: prob. real > break-even de la cuota → apostar; si es menor, pasar
  - Claim: ninguno cuantitativo (título: "me hice rico")
- [Pz-zqTA2dpM](https://www.youtube.com/watch?v=Pz-zqTA2dpM) (2025-05-09) Sports Betting Is Now On 'EASY Mode' (Anyone Can Grow Their Bankroll Doing This)
  - Condición → apuesta: prob. real ≥ implícita + ~5 pts → apostar
  - Claim: ninguno cuantitativo
- [SSRm0cZRuxs](https://www.youtube.com/watch?v=SSRm0cZRuxs) (2025-08-06) This Is EXACTLY How I'd Grow A $10k Bankroll In 6 Months
  - Condición → apuesta: props con ~70%+ de prob. real y edge conocido → apostar con unidad 3-5%
  - Claim: 60-70% / 70% de acierto; 10-15 u/mes
- [LEWp-GanOeA](https://www.youtube.com/watch?v=LEWp-GanOeA) (2026-01-14) How to Make Sports Betting Your 2nd Income
  - Condición → apuesta: prob. estimada > prob. implícita por "margen significativo" → apostar; si no, pasar
  - Claim: 75% de acierto a cuota media -241 en 2025

### `multi-heavy-fav-props-true-prob-edge`
- [_HxbkKE2yS0](https://www.youtube.com/watch?v=_HxbkKE2yS0) (2023-10-27) My Secret To Having A 70% Sports Betting Win-rate
  - Condición → apuesta: la jugada de mayor prob. real del día → 1 u
  - Claim: 71.8% de acierto, +3.56 u en dos meses
- [ZDyYkXUtTJY](https://www.youtube.com/watch?v=ZDyYkXUtTJY) (2025-01-13) Most Profitable Sports Betting Strategy? (+EV Sports Betting Explained)
  - Condición → apuesta: hit rate de temporada (y vs rival) > prob. implícita → over
  - Claim: "cientos de miles de dólares" con este enfoque
- [XsZmejg215k](https://www.youtube.com/watch?v=XsZmejg215k) (2025-02-04) How I Won 83% Of My Sports Betting Picks Using This Strategy Last Month
  - Condición → apuesta: alt line con prob. real ≥70% y mayor que la implícita (edge 3–5%) → apostar 1 u de riesgo
  - Claim: 83% de acierto, +8.8 u en enero
- [Sw2kRfHVRPA](https://www.youtube.com/watch?v=Sw2kRfHVRPA) (2025-05-12) Sports Betting Is A Video Game. Here's How To Win Consistently.
  - Condición → apuesta: prob. real estimada > prob. implícita del precio → apostar el lado favorito (no apostar favoritos sin edge)
  - Claim: 77% de acierto, +19 u en el año; nunca un año negativo desde 2021
- [Z6h3HdNAUD8](https://www.youtube.com/watch?v=Z6h3HdNAUD8) (2026-09-16) The Only Strategy I’d Use To Get Rich Sports Betting
  - Condición → apuesta: prob. estimada alta (≈70–85%+) y mayor que la implícita → apostar; si no hay brecha, pasar
  - Claim: crecimiento a largo plazo + control emocional

### `heavy-favorites-minus160-400-with-edge`
- [OYT7FXMPLus](https://www.youtube.com/watch?v=OYT7FXMPLus) (2024-06-12) How To Outsmart The Sportsbooks And Turn Your Bets Into Consistent Wins!
  - Condición → apuesta: priorizar alta probabilidad de acierto (-160 a -300) sobre cuotas -110
  - Claim: ~70% de acierto a largo plazo; beneficio de $67k (o $670k) en un año
- [NlFN5fRCPXo](https://www.youtube.com/watch?v=NlFN5fRCPXo) (2025-06-05) How I Made $8.7k in 30 Days Using This 3-Step Sports Betting Strategy (just copy me)
  - Condición → apuesta: cuota entre -160 y -400 y prob. real > implícita → apostar; evitar -110/+100
  - Claim: 75% mensual, 83% en otro mes

### `multi-player-props-heavy-juice-75pct`
- [04ZIVory948](https://www.youtube.com/watch?v=04ZIVory948) (2025-02-26) I Quit My Job To Do Sports Betting Full Time. Here's How...
  - Condición → apuesta: prop con "probabilidad real" estimada ≥75% a odds ~-250 → apostar (unidad fija 3%)
  - Claim: largo plazo ≥75% de acierto → "imprimir dinero"

### `multi-heavy-favorites-minus300-to-minus700`
- [062l1DLExcM](https://www.youtube.com/watch?v=062l1DLExcM) (2026-08-10) How I’d Double My Bankroll In 12 Months
  - Condición → apuesta: odds entre -300 y -700 y prob. estimada > implícita → apostar 3% del bankroll
  - Claim: aciertos de 85-90% en las jugadas filtradas; ~+5.5% mensual

### `nfl-props-implied-under80-true-over83`
- [3QxDuwXRaSk](https://www.youtube.com/watch?v=3QxDuwXRaSk) (2025-08-18) The Sports Betting Strategy I Use To Win Every NFL Season
  - Condición → apuesta: prob. implícita ≤80% y "real" ≥83% con margen ≥5 pts → apostar (10 por semana)
  - Claim: 8/10 semanales, +2u/semana

### `multi-props-heavy-juice-blended-hit-rate`
- [4jeXX4ym25o](https://www.youtube.com/watch?v=4jeXX4ym25o) (2026-03-20) How I Won 86% Of My Sports Betting Picks for 2 Months Straight (2-Step Strategy)
  - Condición → apuesta: prob. "real" = media(hit rate temporada, hit rate vs defensas similares) supera la implícita en 5-15 pts → apostar
  - Claim: 86% de acierto en dos meses; ROI 11-16% mensual

### `heavy-favorites-minus300-mispriced`
- [MwALGLuMROU](https://www.youtube.com/watch?v=MwALGLuMROU) (2026-02-23) Sports Betting Is Easy When You Understand This
  - Condición → apuesta: prob. real estimada significativamente > prob. implícita (ej. 85% vs 75%) → apostar el favorito
  - Claim: 80-85% de acierto a ~-300 durante 5 años

### `heavy-favorites-minus170-270-singles-only`
- [RR7Bp-Jfki8](https://www.youtube.com/watch?v=RR7Bp-Jfki8) (2025-01-28) Turning A $50 Bet Into $20,000 In One Year (Step-By-Step Sports Betting Guide)
  - Condición → apuesta: prob. real > implícita dentro de ese rango → single de 1 unidad (2% del bankroll), nunca parlay
  - Claim: 70-80% de acierto sostenido 5+ años; 10 u/mes

### `props-over-minus-220-270-min-5pct-edge`
- [g1eby-Dy48M](https://www.youtube.com/watch?v=g1eby-Dy48M) (2025-03-03) I Tried Sports Betting For 17 Months (and Here's What Happened)
  - Condición → apuesta: prop over entre -220 y -270 con prob. estimada ≥5pp sobre la implícita → apostar; si no, pasar
  - Claim: base de su +$976k en 17 meses

### `multi-heavy-favorites-250-750-band`
- [iVbBr6-XOUM](https://www.youtube.com/watch?v=iVbBr6-XOUM) (2026-05-04) How To Turn $1,000 Into $10,000 Sports Betting
  - Condición → apuesta: cuota en [-750, -250] + prob. estimada > implícita (≥75%) + sin riesgo de lesión, clima o rotación → apostar 3% del bankroll actual
  - Claim: 83% de acierto "según mi tracker", ~8% de edge

### `multi-bet-any-positive-edge-regardless-of-odds`
- [njTt4UX_IxM](https://www.youtube.com/watch?v=njTt4UX_IxM) (2026-05-23) How To Find Winning Bets In 60 Seconds
  - Condición → apuesta: edge del modelo > 0 (aun a -800) → apostar; edge ≈ 0 → omitir
  - Claim: casi todos los picks mostrados ganaron (7-8 de 9 aprox.)

### `multi-short-fav-alt-lines-model-edge`
- [potl3UqywWw](https://www.youtube.com/watch?v=potl3UqywWw) (2025-07-04) How I Won 77% Of My Sports Betting Picks Last Month (Step-By-Step)
  - Condición → apuesta: probabilidad estimada > implícita (edge 1-5%) → apostar 1 unidad fija
  - Claim: 77% de acierto y +15.5u en un mes; +12.12u al 78% el mes previo

## Relaciones
- Índice: [index](../index.md) · Contradicciones: [contradictions](../contradictions.md) · Evolución: [timeline](../timeline.md)
