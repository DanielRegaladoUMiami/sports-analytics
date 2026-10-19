---
id: H-006
title: "SGP “correlacionados” (QB+WR, favorito+team total)"
kind: market
sport: multi
status: untested
n_videos: 13
n_variants: 11
first_mention: 2024-12-03
last_mention: 2026-10-14
---

# H-006 · SGP “correlacionados” (QB+WR, favorito+team total)

**Estado:** ⬜ sin probar · 📊 se puede probar con datos de mercado

## Qué dice
SGPs “correlacionados”: yardas del QB + yardas del WR1, ML del favorito + team total over 1.5, varias líneas del mismo jugador.

## Lectura previa (antes de los datos)
Se contradice: dice que las casas no cobran la correlación y también que sí la cobran. Calcula la probabilidad como si las patas fueran independientes. Las casas sí aplican ajustes de correlación en los SGP, así que en general el edge es negativo.

## Plan de prueba
Con play-by-play (nflfastR) estimar la probabilidad conjunta empírica de cada par de patas y compararla con el precio del SGP (requiere snapshots de precios de SGP).

## Variantes (11) y videos (13)

### `nfl-sgp-qb-alt-pass-yds-plus-wr1-alt-rec-yds`
- [dwuHJlEWJpQ](https://www.youtube.com/watch?v=dwuHJlEWJpQ) (2025-09-02) The NFL Parlay Trick Bookies Don’t Want You Using (Step-By-Step Guide)
  - Condición → apuesta: QB con buen matchup; ambas patas con prob. ≥~88-92% → SGP de 2 patas si prob. conjunta > implícita
  - Claim: +18% de edge en el ejemplo; "backtesteado"
- [tFCnjIYwejw](https://www.youtube.com/watch?v=tFCnjIYwejw) (2025-09-15) The NFL Parlay Betting Hack Nobody Talks About
  - Condición → apuesta: QB vs bottom-5 defensa vs QB y WR1 vs bottom-5 vs WR (DvP fantasy); alternos bajos con prob. real > implícita → parlay de 2 patas
  - Claim: +8% de edge en el ejemplo (81% vs 73%)
- [cimeXxqoy1k](https://www.youtube.com/watch?v=cimeXxqoy1k) (2026-10-14) The NFL SGP That Almost Never Loses (86% Win Rate)
  - Condición → apuesta: defensa rival permite ≥10.5 yds/completion → escalón de cada pata con hit rate de temporada > implícita, SGP solo si prob. conjunta > implícita del SGP
  - Claim: ~86% de probabilidad estimada; +8% de gap

### `nba-sgp-star-alt-ladder-high-hit-rate`
- [2dEGauXhljY](https://www.youtube.com/watch?v=2dEGauXhljY) (2025-12-10) The NBA Parlay Strategy Nobody Is Using (90% NBA Bet)
  - Condición → apuesta: jugador de mayor usage + rival top-5 en FP concedidos a su posición + cada pata con hit rate ≥94% → SGP si producto de hit rates > implícita del SGP (típicamente -500/-650)
  - Claim: "90%" de acierto en estos SGP; edges de +5 a +8 pts

### `nfl-sgp-qb-wr-alt-yards-vs-weak-secondary`
- [CZBuhdA3ax4](https://www.youtube.com/watch?v=CZBuhdA3ax4) (2026-01-12) The NFL SGP Winning 90% of the Time
  - Condición → apuesta: rival en el bottom-5 en yardas por completo y en fantasy points concedidos a WR + cada pata ≥90% de prob. estimada + prob. conjunta > implícita del SGP → SGP
  - Claim: 90% de acierto

### `nba-sgp-single-player-under-average-legs`
- [ZtQAgLD49-I](https://www.youtube.com/watch?v=ZtQAgLD49-I) (2024-12-03) Win 70% Of Your NBA Parlays With This Sports Betting Strategy
  - Condición → apuesta: jugador con buen matchup y alta prob. de superar su PRA → SGP con cada categoría ~20–40% bajo su promedio, a precio ~-180/-210
  - Claim: 70% de acierto, rentable a -170/-210

### `nfl-sgp-qb-pass-yds-plus-td-vs-weak-pass-d`
- [awDLJlH-Uy0](https://www.youtube.com/watch?v=awDLJlH-Uy0) (2025-11-27) The NFL Parlay That Wins 90% of the Time
  - Condición → apuesta: QB titular no novato vs defensa bottom-10 en yds/completion permitidas Y bottom-5 en pass TD permitidos → SGP over yardas (línea con hit rate ≥90%) + 1+ TD
  - Claim: "gana 90% del tiempo" (el propio ejemplo da 74%)

### `wc-group-sgp-fav-ml-plus-team-over-1-5`
- [b0oKNLDi4YA](https://www.youtube.com/watch?v=b0oKNLDi4YA) (2026-06-08) The World Cup Parlay That Wins 85% of the Time
  - Condición → apuesta: fase de grupos jornada 1-2, favorito top-15 FIFA vs rival ranking ≥40/debutante, ML del favorito entre -300 y -700 → SGP ML + TT o1.5
  - Claim: ~85% de acierto; +9% edge en el ejemplo

### `nba-sgp-same-player-high-prob-alt-lines`
- [cPyOXGv8mJk](https://www.youtube.com/watch?v=cPyOXGv8mJk) (2025-11-11) The Legal Sports Betting Hack Sportsbooks Fear
  - Condición → apuesta: dos líneas alternativas bajas del mismo jugador con ~95% de hit rate cada una → SGP de 2 patas cuando el precio sea ~-250
  - Claim: "edge tremendo"

### `soccer-wc-sgp-favorite-ml-team-total-over-1p5`
- [gC-s8abUmrQ](https://www.youtube.com/watch?v=gC-s8abUmrQ) (2026-06-13) The Ultimate World Cup Sports Betting Strategy
  - Condición → apuesta: favorito top 15 FIFA vs. rival ≥40, partido 1 o 2 de grupos, ML entre -300 y -700 → SGP ML favorito + favorito over 1.5 goles
  - Claim: hit ~85% (de 80 a 88%); precio del libro de +150 a -220; edge de +9%

### `nfl-sgp-qb-alt-pass-yds-plus-1-pass-td`
- [oS8392pF5do](https://www.youtube.com/watch?v=oS8392pF5do) (2026-10-02) If I Only Had $500 To Bet On NFL With, I’d Do This
  - Condición → apuesta: QB con hit rate alto en el umbral, red zone pass % ≥55%, rival malo en yds/completación y TD de pase permitidos, game script de volumen → SGP solo si prob. estimada > implícita del SGP
  - Claim: ejemplos ilustrativos de 78-82% estimado vs 71-74% implícito

### `soccer-sgp-over-1-5-goals-plus-attacker-over-1-5-shots`
- [okW0zYVFsSI](https://www.youtube.com/watch?v=okW0zYVFsSI) (2026-05-18) The Soccer Parlay That Wins 85% of the Time
  - Condición → apuesta: pasan los 4 filtros, SGP ≥ -250 y edge estimado ≥ +10% → apostar
  - Claim: gana 85% del tiempo; edge ~9% por apuesta [00:00] [03:04]

### `nba-sgp-star-pts-reb-ast-low-thresholds-vs-bottom5-dvp`
- [qaJecoSXUBU](https://www.youtube.com/watch?v=qaJecoSXUBU) (2025-10-21) The NBA Parlay That Wins 80% of the Time
  - Condición → apuesta: líder de usage vs defensa bottom-5 en fantasy permitidos a su posición; umbrales con ≥90% de acierto vs defensas similares; SGP mejor que -260 → apostar
  - Claim: gana 80% del tiempo [00:00]

## Relaciones
- Índice: [index](../index.md) · Contradicciones: [contradictions](../contradictions.md) · Evolución: [timeline](../timeline.md)
