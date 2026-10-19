---
id: H-040
title: "NBA: props (PRA, puntos, rebotes) vs defensa por posición"
kind: market
sport: nba
status: untested
n_videos: 16
n_variants: 14
first_mention: 2021-04-18
last_mention: 2026-04-17
---

# H-040 · NBA: props (PRA, puntos, rebotes) vs defensa por posición

**Estado:** ⬜ sin probar · 📊 se puede probar con datos de mercado

## Qué dice
NBA: props de PRA, puntos y rebotes contra la defensa por posición (DvP). Over si el jugador tiene mucho uso y la defensa es mala, under si tiene poco uso y la defensa es top. Líneas alternas por debajo del promedio.

## Lectura previa (antes de los datos)
Se contradice sobre quién va al under de PRA (poco uso contra top 5, o estrellas contra defensas 6-10). El DvP es una métrica ruidosa y con confusores.

## Plan de prueba
Con box scores de la NBA y DvP calculado sin fuga de información, hacer una regresión del residuo (real − línea) sobre DvP, uso y minutos proyectados, ajustando por compañeros ausentes.

## Variantes (14) y videos (16)

### `nba-props-defense-vs-position-over-recent-form`
- [2dEGauXhljY](https://www.youtube.com/watch?v=2dEGauXhljY) (2025-12-10) The NBA Parlay Strategy Nobody Is Using (90% NBA Bet)
  - Condición → apuesta: rival en el top-5 de FP concedidos a la posición del jugador → favorecer overs del jugador
  - Claim: matchup favorable aumenta la probabilidad (sin cifra)
- [1Jr8Y5OYrCE](https://www.youtube.com/watch?v=1Jr8Y5OYrCE) (2026-03-23) I Used Ai for Sports Betting and the Results Will Shock You
  - Condición → apuesta: elegir overs por matchup débil (defensa vs posición del rival) e ignorar rachas de pocos partidos
  - Claim: la forma reciente "no importa"; el matchup sí (sin cifra)

### `nba-alt-pra-over-vs-weak-dvp`
- [JYoFuBDaqFA](https://www.youtube.com/watch?v=JYoFuBDaqFA) (2023-10-03) These Are The BEST Player Props To Bet On In Sports Betting!
  - Condición → apuesta: opción 1-2 del equipo + buen matchup → over del PRA alterno por debajo de su promedio
  - Claim: ninguno numérico
- [HGOSZ1i-mmg](https://www.youtube.com/watch?v=HGOSZ1i-mmg) (2024-01-11) How This One Strategy Could Change Your Sports Betting Forever
  - Condición → apuesta: rival débil defendiendo la posición del jugador → over del PRA alterno fijado en (o ~1 punto bajo) su promedio de temporada, a precio -150/-210
  - Claim: "alta probabilidad"; ningún número

### `props-matchup-dvp-over-under`
- [KDbjCr-oNA0](https://www.youtube.com/watch?v=KDbjCr-oNA0) (2021-04-18) These Are The Best Type Of Games To Bet On & Make Money! (And What Games You Should Avoid Betting…)
  - Condición → apuesta: jugador contra la peor defensa de su posición → over
  - Claim: el book usa el promedio sin ajustar por matchup
- [K5ZKKKm1Cgg](https://www.youtube.com/watch?v=K5ZKKKm1Cgg) (2021-05-28) What Is The Best Bet In Sports Betting To Put Your Money On!? (Highest % Chance To Win)
  - Condición → apuesta: jugador contra la peor defensa de su posición → over; contra la mejor → under
  - Claim: los books ignoran el matchup; los props "siempre" dan valor

### `nba-star-pra-over-hedge-alt-spread`
- [-1yJ97DQus8](https://www.youtube.com/watch?v=-1yJ97DQus8) (2024-01-18) NBA 4th Quarter Betting Secrets! (How to Dodge Blowout Losses...)
  - Condición → apuesta: favorito con spread pregame ~-10 o más y estrella con matchup favorable → over PRA (1u) + spread alternativo ~-13.5/-14.5 a +money (1u)
  - Claim: casi nunca pierdes ambas; puedes "ganar doble" o salir a la par (sin cifras)

### `nba-points-alt-ladder-season-plus-similar-defense`
- [APSRbsyjlRI](https://www.youtube.com/watch?v=APSRbsyjlRI) (2026-04-17) The Betting Strategy That Got Me to 83% Win Rate (Here's Exactly Why)
  - Condición → apuesta: prob. = promedio(tasa de acierto en la temporada, tasa contra defensas similares); apostar la línea donde prob. − implícita > 0 (suele ser la línea baja a -400/-500)
  - Claim: le llevó a un 83% de acierto (título)

### `nba-alt-pra-over-high-usage-vs-bottom5-dvp`
- [FLRjvBqb81Y](https://www.youtube.com/watch?v=FLRjvBqb81Y) (2025-01-20) How I Made $5k in 30 Days Using This NBA Sports Betting Strategy
  - Condición → apuesta: jugador top-2 en usage% de su equipo + rival bottom-5 en DvP contra su posición → over del PRA alterno con precio -250 a -270
  - Claim: 70-80% de acierto; "$5,000 el mes pasado" [00:00], [05:05], [08:39]

### `nba-props-adjust-for-missing-teammates`
- [L2YT8wBPl7Y](https://www.youtube.com/watch?v=L2YT8wBPl7Y) (2024-01-04) 2024 Sports Betting Guide To Success! (Top 5 Steps to Beat the Books & Profit)
  - Condición → apuesta: cuando faltan compañeros clave, usar solo la muestra de partidos con esas mismas ausencias para estimar el hit rate
  - Claim: ninguno

### `nba-under-points-low-usage-starter-tough-dvp`
- [TDsm0vE2wXk](https://www.youtube.com/watch?v=TDsm0vE2wXk) (2026-01-30) Why Betting NBA Teams is a Trap
  - Condición → apuesta: titular con 4.º–5.º usage del quinteto + rival top en defensa vs su posición → under alterno donde hit rate de temporada − prob. implícita ≥ 3 pts
  - Claim: ninguno de win rate; edge de 3% en el ejemplo

### `nba-star-pra-over-alt-below-season-avg`
- [VFaNZeIIPn4](https://www.youtube.com/watch?v=VFaNZeIIPn4) (2022-02-23) Secret Sports Betting Strategy That Wins At A High % In The NBA (4 Things To Look For!)
  - Condición → apuesta: estrella con alto uso + rival en el bottom de defensa vs. su posición → over de PRA en una línea alternativa por debajo de su promedio de temporada
  - Claim: "alto %" de acierto (sin cifra)

### `nba-pra-alt-under-low-usage-tough-defense`
- [h0jDxVor7FU](https://www.youtube.com/watch?v=h0jDxVor7FU) (2025-02-20) Give Me 21 Minutes And I'll Show You How I Made $12,000 Betting On NBA (Step-By-Step Guide)
  - Condición → apuesta: usage ≤18% + rival top 5 defendiendo la posición + línea alterna 3-4 pts por encima a -250/-270 + hit histórico del under ≥75% → under PRA alterno
  - Claim: ~77% de acierto combinado (overs y unders), +12.31u

### `nba-pra-alt-over-high-usage-weak-defense`
- [h0jDxVor7FU](https://www.youtube.com/watch?v=h0jDxVor7FU) (2025-02-20) Give Me 21 Minutes And I'll Show You How I Made $12,000 Betting On NBA (Step-By-Step Guide)
  - Condición → apuesta: usage ≥25% + rival entre los peores defendiendo la posición + línea alterna 3-4 pts por debajo a -250/-270 + hit histórico ≥75% → over PRA alterno
  - Claim: ~77% (combinado)

### `nba-dfs-pra-under-star-vs-top6-10-defense`
- [lhxcieV3WLY](https://www.youtube.com/watch?v=lhxcieV3WLY) (2024-01-26) This PrizePicks Hack Is The Best Sports Betting Strategy To Consistently Win More Bets!
  - Condición → apuesta: estrella con usage alto contra una defensa 6ª-10ª en DvP de su posición, con alto % histórico de under contra defensas similares → "less" en PRA, combinando las 2 mejores
  - Claim: "puedes ganar dinero" (sin cifra); dice haber hecho tracking

### `nba-pra-alt-line-at-season-avg-vs-worst-dvp`
- [o0fLpbF9SdI](https://www.youtube.com/watch?v=o0fLpbF9SdI) (2023-11-17) How To Get NBA Player Props At Even Money
  - Condición → apuesta: estrella vs top-5 peor defensa por posición (DvP fantasy) → over PRA alterno en su promedio de temporada
  - Claim: "higher probability" (sin número)

### `nba-alt-rebounds-leading-rebounder-vs-poor-rebounding-opp`
- [oRtjseFNwn0](https://www.youtube.com/watch?v=oRtjseFNwn0) (2025-11-04) This NBA Bet Almost Never Loses (85% Win Rate)
  - Condición → apuesta: rebotador líder titular; rival bottom-10 en OREB y DREB permitidos, top-15 en FGA, bottom-15 en FG% → over del escalón con mayor diferencia vs implícita
  - Claim: "85% win rate" en el título; "casi nunca pierde"

## Relaciones
- Índice: [index](../index.md) · Contradicciones: [contradictions](../contradictions.md) · Evolución: [timeline](../timeline.md)
