---
id: H-027
title: "MLB: totales, innings y otros mercados"
kind: market
sport: mlb
status: untested
n_videos: 8
n_variants: 11
first_mention: 2022-04-12
last_mention: 2026-06-23
---

# H-027 · MLB: totales, innings y otros mercados

**Estado:** ⬜ sin probar · 📊 se puede probar con datos de mercado

## Qué dice
MLB, mercados variados: modelo de totales con 5 factores (edge ≥0.75 carreras), ajuste por viento de ±0.5, totales alternos 6.5/11.5 filtrados, team total over 1.5, “sin carrera en el 2º/3º inning” en vez de NRFI, ignorar la última apertura del pitcher.

## Lectura previa (antes de los datos)
Lo del viento y el parque es real, pero el mercado ya lo descuenta. Los totales alternos extremos tienen mucho hold.

## Plan de prueba
Usar Retrosheet con clima (viento) y totales de cierre para medir el residuo del total en función del viento. En los innings, P(0 carreras) por inning comparada con precios.

## Variantes (11) y videos (8)

### `mlb-h2h-recent-home-away-trend`
- [2YB2DZID6_I](https://www.youtube.com/watch?v=2YB2DZID6_I) (2024-08-06) How To Make $1,000s Using This Sports Betting Strategy
  - Condición → apuesta: H2H reciente (≤3 años) con récord sesgado en la misma localía → apoyar ese lado/over-under
  - Claim: ninguno cuantificado

### `mlb-2nd-inning-tie-after-1-0-first`
- [Kf5xPZrDW_A](https://www.youtube.com/watch?v=Kf5xPZrDW_A) (2023-05-21) Win More In Sports Betting With 2023 MLB Rule Changes!
  - Condición → apuesta: la 1ª entrada termina 1-0 → apostar "empate" en la 2ª entrada (~-130)
  - Claim: "produce decentemente" (sin número)

### `mlb-alt-team-total-over-1-5-filters`
- [emeoXTN9wt4](https://www.youtube.com/watch?v=emeoXTN9wt4) (2026-06-15) MLB SPORTS BETTING STRATEGY THAT ACTUALLY MAKES A PROFIT EVERYDAY
  - Condición → apuesta: equipo top-10 en R/G y HR/G vs abridor ERA ≥4.00 y HR/9 ≥1.4, bullpen rival bottom-10 en ERA, parque con factor ≥100 → over 1.5 carreras del equipo
  - Claim: ~90% (título del video y ejemplo Dodgers con 100% filtrado); edge +3% a +14%

### `mlb-avoid-nrfi`
- [fOVpOUHINAA](https://www.youtube.com/watch?v=fOVpOUHINAA) (2022-04-12) Stop Using This MLB Sports Betting Strategy And Start Doing This Instead To Be More Profitable!
  - Condición → apuesta: siempre, incluso con dos ases → no apostar NRFI
  - Claim: "te garantizo que serás más rentable"

### `mlb-no-run-2nd-3rd-inning`
- [fOVpOUHINAA](https://www.youtube.com/watch?v=fOVpOUHINAA) (2022-04-12) Stop Using This MLB Sports Betting Strategy And Start Doing This Instead To Be More Profitable!
  - Condición → apuesta: tras ver la 1ª entrada (pitcher sólido), apostar "no carrera" en la 2ª o 3ª
  - Claim: "la mayor probabilidad de acierto"

### `mlb-alt-total-over-6p5-7p5-filtered`
- [l78HMb0zrz4](https://www.youtube.com/watch?v=l78HMb0zrz4) (2026-06-23) The 80% MLB Totals System Nobody Talks About
  - Condición → apuesta: H2H ≥8/10 overs + ERA de ambos abridores ≥4 + ambos bullpens en el bottom 10 + parque de bateadores + HR/9 alto de ambos → over 6.5 o 7.5
  - Claim: ~80%

### `mlb-alt-total-under-10p5-11p5-filtered`
- [l78HMb0zrz4](https://www.youtube.com/watch?v=l78HMb0zrz4) (2026-06-23) The 80% MLB Totals System Nobody Talks About
  - Condición → apuesta: H2H ≥8/10 unders + ERA de ambos ≤3 + ambos bullpens top 10 + parque de pitchers + HR/9 bajo → under 10.5 o 11.5
  - Claim: ~80%

### `mlb-live-at-bat-out-vs-top-dfs-owned-pitcher`
- [oftzUFbC6XI](https://www.youtube.com/watch?v=oftzUFbC6XI) (2024-08-12) Make $100 A Day On MLB Bets With This Easy To Follow Sports Betting Strategy
  - Condición → apuesta: pitcher más usado en DFS; bateadores rivales sin historial bueno vs él y fuera del top-25 de K% → apostar "out (fly/pop) o error" en sus 2 primeros turnos
  - Claim: $50-100 diarios con apuestas de $50; casi nunca un día perdedor

### `mlb-ignore-pitcher-last-start-recency`
- [r_KuAMjKunw](https://www.youtube.com/watch?v=r_KuAMjKunw) (2024-10-21) These 7 Secret Rules Made Me A Successful Sports Bettor
  - Condición → apuesta: no ajustar la apuesta por una mala/buena última salida del abridor; usar promedios de más largo plazo
  - Claim: "le pasa todo el tiempo" que el que fue castigado lanza una joya [12:16]

### `mlb-total-model-0.75-run-edge`
- [vdoxBu_Xb1E](https://www.youtube.com/watch?v=vdoxBu_Xb1E) (2026-05-25) How To Calculate Any MLB Total In 10 Min (Step-By-Step)
  - Condición → apuesta: proyección del modelo de 5 factores difiere del total de la casa ≥0.75 carreras → apostar en esa dirección
  - Claim: "las edges son reales", lo ha hecho "en miles de juegos" (sin cifras)

### `mlb-total-wind-adjustment`
- [vdoxBu_Xb1E](https://www.youtube.com/watch?v=vdoxBu_Xb1E) (2026-05-25) How To Calculate Any MLB Total In 10 Min (Step-By-Step)
  - Condición → apuesta: viento soplando hacia fuera ≥10 mph → +0.5 carreras (inclinarse al over); hacia dentro ≥10 mph → −0.5 (under)
  - Claim: efecto de ±0.5 carreras

## Relaciones
- Índice: [index](../index.md) · Contradicciones: [contradictions](../contradictions.md) · Evolución: [timeline](../timeline.md)
