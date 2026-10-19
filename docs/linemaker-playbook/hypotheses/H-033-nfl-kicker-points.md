---
id: H-033
title: "NFL: puntos del kicker over"
kind: market
sport: nfl
status: untested
n_videos: 3
n_variants: 3
first_mention: 2025-10-13
last_mention: 2025-12-22
---

# H-033 · NFL: puntos del kicker over

**Estado:** ⬜ sin probar · 📊 se puede probar con datos de mercado

## Qué dice
NFL: puntos del kicker over 5.5 (o alterno) con un kicker de FG% ≥90% contra una defensa que permite muchos FG.

## Lectura previa (antes de los datos)
Es un mercado de nicho con poco límite, donde podría haber ineficiencia real.

## Plan de prueba
Con nflfastR, puntos por juego del kicker en función de los drives que se frenan en la zona de FG; P(≥6) comparada con el precio.

## Variantes (3) y videos (3)

### `nfl-kicker-points-alt-over-special-teams-filter`
- [KJKFuo4XPXY](https://www.youtube.com/watch?v=KJKFuo4XPXY) (2025-10-13) The NFL Bet That Wins 87% of the Time
  - Condición → apuesta: rival bottom-5 en puntos permitidos a kickers + rival bottom-10 en puntos/intento de FG permitidos + ofensiva top-10 en intentos de FG/juego + kicker top-10 en FG% + hit rate > implícita → over alterno de puntos del kicker
  - Claim: 87% de acierto

### `nfl-kicker-points-over-5-5`
- [tCH6dKye_8E](https://www.youtube.com/watch?v=tCH6dKye_8E) (2025-12-22) The NFL Bet That Almost Never Loses
  - Condición → apuesta: pateador con ≥90% de FG, rival que permite muchos FG/kicker points, buena red zone propia → over 5.5 si hit rate > implícita
  - Claim: "casi nunca pierde"; 82% vs 75% implícito (+7) [07:38]

### `nfl-kicker-points-over-5.5`
- [wjyw8gvfz3E](https://www.youtube.com/watch?v=wjyw8gvfz3E) (2025-12-08) The NFL Bet Nobody Is Using (80% NFL Bet)
  - Condición → apuesta: defensa rival entre las que más FG hechos permite por juego y kicker con FG% ≥90% → over 5.5 kicker points
  - Claim: título "80%"; ejemplo 83% real vs 68% implícito (+15%)

## Relaciones
- Índice: [index](../index.md) · Contradicciones: [contradictions](../contradictions.md) · Evolución: [timeline](../timeline.md)
