---
id: H-050
title: "NHL: totales, puck line, puntos y goleadores"
kind: market
sport: nhl
status: untested
n_videos: 8
n_variants: 8
first_mention: 2020-10-21
last_mention: 2026-06-06
---

# H-050 · NHL: totales, puck line, puntos y goleadores

**Estado:** ⬜ sin probar · 📊 se puede probar con datos de mercado

## Qué dice
NHL: under del 1er periodo 2.5 entre buenas defensas, totales alternos por tendencia H2H, línea de 60 minutos en vez de ML −300, +1.5/+2.5 en el puck line, puntos del PP1 y unders de jugadores del PP2. Además, dice que la NHL es el deporte “más rentable”.

## Lectura previa (antes de los datos)
Lo de la línea de 60 minutos frente al ML tiene lógica de precio. Lo demás se basa en H2H con muestras chicas.

## Plan de prueba
Con datos NHL (MoneyPuck), distribución de goles por periodo y P(gana en tiempo regular) frente al precio de la línea de 60 minutos.

## Variantes (8) y videos (8)

### `nhl-pp1-top-scorer-over-0-5-points-vs-high-pim`
- [CLuLX0M834I](https://www.youtube.com/watch?v=CLuLX0M834I) (2025-10-11) The NHL Bet Winning 85% of the Time
  - Condición → apuesta: rival top-5 en PIM + equipo top-10 en PP% + jugador entre los 2 primeros en puntos de la PP1 + prob. contra rivales similares > implícita → over 0.5 puntos (típicamente -300/-400)
  - Claim: 85% de acierto

### `nhl-heavy-fav-60min-regulation-line`
- [FldXYiT4jtw](https://www.youtube.com/watch?v=FldXYiT4jtw) (2022-06-08) Try This NHL Sports Betting Strategy & Cut Big Favorites Odds In Half!
  - Condición → apuesta: favorito ML -300 a -500 → apostar su victoria en regulación (~-150/-180)
  - Claim: "corta las odds a la mitad"; el favorito rara vez va a OT

### `nhl-alt-total-h2h-trend-open-5-5-6-5`
- [GtUr_qGv4cU](https://www.youtube.com/watch?v=GtUr_qGv4cU) (2025-10-16) The NHL Bet Nobody Is Using (90% NHL Bet)
  - Condición → apuesta: apertura 5.5 + H2H últimos 10 ≥8-2 al under + sin movimiento en contra → under alterno 7; apertura 6.5 + H2H ≥8-2 al over + sin movimiento en contra → over alterno 5
  - Claim: 90% de acierto

### `nhl-plus-puckline-last10-hitrate-vs-implied`
- [HjBJaTvt0_8](https://www.youtube.com/watch?v=HjBJaTvt0_8) (2026-06-06) Don’t Bet The Stanley Cup Final Until You See This
  - Condición → apuesta: tasa de cobertura en últimos 10 juegos > prob. implícita del precio → apostar la línea con "edge"
  - Claim: CAR +1.5 90% vs 73%; VGK +2.5 100% vs 85%; over 3.5 100% vs 88%

### `nhl-totals-static-5-5-5-value`
- [O5sEcFeOArQ](https://www.youtube.com/watch?v=O5sEcFeOArQ) (2020-12-16) These Are The Sports Leagues You Should Bet The Most Money On? (I Bet It's Not What You Think!)
  - Condición → apuesta: buscar valor en totales NHL porque el book casi siempre los deja en 5.5 (ajustando con el juice)
  - Claim: los totales "no se mueven" y se pueden explotar

### `nhl-alt-1p-under-2-5-goals`
- [TkKc1FxqkqU](https://www.youtube.com/watch?v=TkKc1FxqkqU) (2026-06-02) This Stanley Cup Bet Looks Too Easy
  - Condición → apuesta: frecuencia histórica (H2H/temporada) de ≤2 goles en el 1P > prob. implícita → under 2.5 1P
  - Claim: 83% de probabilidad, edge 3–7%

### `nhl-under-1-5-points-pp2-vs-elite-goalie-pk`
- [WpOHTGsDo6c](https://www.youtube.com/watch?v=WpOHTGsDo6c) (2025-11-14) The NHL Parlay That Hits 90% Of The Time
  - Condición → apuesta: jugadores de PP2 contra rival top-5 en GAA y top-5 en PK, portero titular confirmado → parlay de los 2 unders de mayor hit rate
  - Claim: "acierta 90% del tiempo"

### `nhl-prioritize-moneyline-and-totals`
- [kfYK33T13YA](https://www.youtube.com/watch?v=kfYK33T13YA) (2020-10-21) THIS is The MOST PROFITABLE Sport to Bet on! (How & Why it's The Best...)
  - Condición → apuesta: preferir la NHL (ML en rango ~-200 a +200 y totales 5.5-6) sobre otros deportes
  - Claim: es "el deporte más rentable" (sin cifras)

## Relaciones
- Índice: [index](../index.md) · Contradicciones: [contradictions](../contradictions.md) · Evolución: [timeline](../timeline.md)
