---
id: H-030
title: "NFL/CFB: yardas y TDs del QB"
kind: market
sport: nfl
status: untested
n_videos: 9
n_variants: 9
first_mention: 2023-10-03
last_mention: 2026-09-11
---

# H-030 · NFL/CFB: yardas y TDs del QB

**Estado:** ⬜ sin probar · 📊 se puede probar con datos de mercado

## Qué dice
NFL/CFB: yardas alternas del QB por debajo de su promedio contra secundarias débiles, 1+ TD de pase contra defensas que permiten muchos y QB senior en CFB.

## Lectura previa (antes de los datos)
Poner la línea por debajo del promedio no te da edge si el precio ya lo refleja. La varianza de las yardas de pase es alta.

## Plan de prueba
Con nflfastR, construir la distribución de yardas de pase por QB × defensa (EPA/dropback permitido) y comparar P(yardas ≥ escalón) con los precios de la escalera alterna.

## Variantes (9) y videos (9)

### `nfl-qb-passing-yards-under-favorite`
- [7bpBUYJLqRQ](https://www.youtube.com/watch?v=7bpBUYJLqRQ) (2025-02-13) You'll Never Bet On Sports The Same After Watching This
  - Condición → apuesta: prob. real (temporada + temporada previa + defensas similares) > implícita → under (ej. Mahomes u280 a -220)
  - Claim: +4% de edge en el ejemplo; 6-2 en el Super Bowl

### `nfl-qb-passing-yards-alt-ladder-edge`
- [8YEBZ_RkIFk](https://www.youtube.com/watch?v=8YEBZ_RkIFk) (2025-12-03) How I Win Almost 80% of My NFL Picks With This Method
  - Condición → apuesta: proyección = completos/partido × yardas por completo que concede la defensa rival; elegir la línea alterna con mayor prob. estimada − implícita (puede ser -440 o -150)
  - Claim: +10% (Goff 200+) y +15% (Prescott 250+)

### `nfl-qb-over-0-5-pass-td-vs-leaky-defense`
- [9R5P42vMejw](https://www.youtube.com/watch?v=9R5P42vMejw) (2025-09-25) The NFL Bet That Wins 90% of the Time
  - Condición → apuesta: rival permite ≥1.7 TD de pase por partido + QB titular veterano (no rookie ni suplente) + ≥90% de partidos con TD contra defensas de ese grupo → over 0.5 a ~-350
  - Claim: "90% a casi 100%", "trackeado"

### `nfl-qb-alt-passing-yards-over-weak-secondary`
- [CZBqNY5cayw](https://www.youtube.com/watch?v=CZBqNY5cayw) (2024-09-05) Top 3 Best Bets To Place In Football
  - Condición → apuesta: rival con secundaria débil (yardas por pase permitidas altas) + alterna fijada por debajo del promedio de temporada del QB → over a ~-160/-200
  - Claim: prob. del 70-90%, "80-85% a veces"

### `nfl-qb-alt-passing-yards-over-below-avg`
- [JYoFuBDaqFA](https://www.youtube.com/watch?v=JYoFuBDaqFA) (2023-10-03) These Are The BEST Player Props To Bet On In Sports Betting!
  - Condición → apuesta: línea principal inflada sobre el promedio de temporada → over alterno por debajo del promedio
  - Claim: "aumenta mucho la probabilidad"; ningún número

### `nfl-qb-1plus-pass-td-prior-season-90pct`
- [KpiwGiESfMU](https://www.youtube.com/watch?v=KpiwGiESfMU) (2026-09-11) The NFL Bet That Almost Never Loses (90% Win Rate)
  - Condición → apuesta: QB (mismo equipo) con ≥90% de juegos con 1+ TD la temporada previa + rival que permite ≥1.5 TD de pase/juego + prob. real > implícita → over 0.5 TD
  - Claim: 90%+ de acierto

### `nfl-qb-passing-yards-alt-below-average`
- [QbKmM7Qb6pc](https://www.youtube.com/watch?v=QbKmM7Qb6pc) (2023-10-14) How To Make PROFITABLE Bets In The NFL
  - Condición → apuesta: línea principal por encima del promedio del QB → comprar over alternativo por debajo de su promedio
  - Claim: mayor probabilidad

### `ncaaf-senior-qb-alt-pass-yds-over`
- [U6qd0TcKwLQ](https://www.youtube.com/watch?v=U6qd0TcKwLQ) (2025-08-21) The College Football Bet Nobody Is Using (90% Win Rate)
  - Condición → apuesta: QB senior + rival bottom-20 vs pase + ofensiva ≥55% pase + alt line a -270/-330 + prob. real ≥90% → over de la línea alterna
  - Claim: gana 90% del tiempo; "unos cuantos QBs cada semana" cumplen

### `nfl-qb-alt-pass-yds-200-plus-vs-weak-pass-d`
- [uJq_OcbUEzg](https://www.youtube.com/watch?v=uJq_OcbUEzg) (2025-08-11) The NFL Bet Nobody Is Using (85% NFL Bet)
  - Condición → apuesta: QB de volumen (35+ intentos/juego) con hit rate alto de 200+ en la temporada, rival bottom-5 vs el pase → over 200 alterno aunque cueste -300
  - Claim: 80-90% para ciertos QBs [00:00]; Burrow 88% [01:01]

## Relaciones
- Índice: [index](../index.md) · Contradicciones: [contradictions](../contradictions.md) · Evolución: [timeline](../timeline.md)
