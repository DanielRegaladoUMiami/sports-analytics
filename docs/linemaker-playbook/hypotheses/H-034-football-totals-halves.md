---
id: H-034
title: "NFL/CFB: totales, mitades, clima y ritmo"
kind: market
sport: nfl
status: untested
n_videos: 9
n_variants: 9
first_mention: 2022-08-17
last_mention: 2026-09-04
---

# H-034 · NFL/CFB: totales, mitades, clima y ritmo

**Estado:** ⬜ sin probar · 📊 se puede probar con datos de mercado

## Qué dice
NFL/CFB, totales: under de 1H 28.5 con ofensivas débiles, filtro de YPP, proyección por ritmo × puntos por jugada, under con viento o lluvia, over en CFB con calor y viento moderado, under en pretemporada.

## Lectura previa (antes de los datos)
El clima (viento fuerte) es de las pocas señales con soporte empírico, aunque el mercado ya lo ajusta. Las reglas de calor parecen sobreajustadas.

## Plan de prueba
Usar los totales de cierre con resultados y clima (nflfastR trae temperatura y viento) y hacer una regresión del residuo del total sobre viento, temperatura, ritmo y YPP.

## Variantes (9) y videos (9)

### `nfl-1h-alt-under-28-5-low-ypp`
- [3YcOcgTLHTQ](https://www.youtube.com/watch?v=3YcOcgTLHTQ) (2025-10-06) The NFL Bet Hitting at 92% of the Time
  - Condición → apuesta: ofensivas en el bottom 5-8 en yardas/jugada y defensas en el top 5-8 en yardas/jugada permitidas → under 28.5 1H
  - Claim: 92% en la temporada en curso

### `ncaaf-over-hot-windy-nonconference`
- [80LAi7-hX8I](https://www.youtube.com/watch?v=80LAi7-hX8I) (2022-08-17) College Football Sports Betting Strategy! (4 Steps To Win More This Season)
  - Condición → apuesta: viento 7-20 mph + temperatura 85-110 °F + no conferencia → over
  - Claim: 59% de acierto

### `nfl-total-pace-ppp-projection`
- [8YEBZ_RkIFk](https://www.youtube.com/watch?v=8YEBZ_RkIFk) (2025-12-03) How I Win Almost 80% of My NFL Picks With This Method
  - Condición → apuesta: proyección = promedio de (jugadas_A × PPP_of_A, jugadas_A × PPP_def_B) + lo mismo para B; si la proyección supera la línea (y la línea no cruza un número clave) → over
  - Claim: proyección de 55 vs línea de 54

### `nfl-1h-under-28-5-low-total-h2h`
- [HgqnOETvyL8](https://www.youtube.com/watch?v=HgqnOETvyL8) (2026-09-04) I Found An NFL Bet That Wins 80% Of The Time
  - Condición → apuesta: total del partido 38.5-44.5 + H2H últimas 5 temporadas ≥80% con 1T ≤28 + precio con gap positivo (≤ -800 si 90%) → under 28.5 1T
  - Claim: 80% mínimo, hasta 95% por temporada; backtest de 5 años

### `ncaaf-over-hot-moderate-wind`
- [J3mEne7vTvw](https://www.youtube.com/watch?v=J3mEne7vTvw) (2023-08-30) SIMPLE College Football Strategy That Wins at OVER 60%
  - Condición → apuesta: viento 5-15 mph + temperatura 90-105 °F → over (comprar puntos si la línea está en número clave)
  - Claim: >60% de acierto

### `ncaaf-under-run-heavy-slow-pace`
- [NI88kYAo6S8](https://www.youtube.com/watch?v=NI88kYAo6S8) (2026-08-28) The NCAAF Bet That Wins 80% of the Time
  - Condición → apuesta: ambos equipos run% ≥55%, ≤67 jugadas/partido, defensas rivales ≤5.3 YPP permitido (bonus: red zone ≤85%) → under; comprar alternativa por encima de los números clave
  - Claim: 80% de acierto "en la situación correcta"; +6% de edge en el ejemplo

### `nfl-under-bad-weather-wind-rain`
- [NJ9KIicNZ48](https://www.youtube.com/watch?v=NJ9KIicNZ48) (2025-12-18) Finding 1st Half Totals With This NFL Betting Strategy
  - Condición → apuesta: lluvia persistente y viento fuerte → inclinarse al under
  - Claim: ninguno cuantitativo

### `nfl-preseason-alt-under-starters-rest`
- [fhjYc9R3Hrg](https://www.youtube.com/watch?v=fhjYc9R3Hrg) (2026-08-14) The NFL Preseason Bet That Wins 80% of the Time
  - Condición → apuesta: semana 2+ de pretemporada, ambos equipos descansan titulares, ningún QB2 con ≥20 starts, total 38-44 (ideal 40-43) → under alternativo ~8 puntos por encima a ~-300
  - Claim: 80-90% de acierto; edge 5-15%

### `nfl-total-ypp-filter`
- [vHND1mhk77o](https://www.youtube.com/watch?v=vHND1mhk77o) (2025-09-22) NFL Totals Hack That Wins At 80% (Step by Step)
  - Condición → apuesta: ambos top 5 YPP ofensivo y bottom 10 YPP defensivo → over; ambos bottom 10 YPP ofensivo y top 5 YPP defensivo → under
  - Claim: ninguno específico

## Relaciones
- Índice: [index](../index.md) · Contradicciones: [contradictions](../contradictions.md) · Evolución: [timeline](../timeline.md)
