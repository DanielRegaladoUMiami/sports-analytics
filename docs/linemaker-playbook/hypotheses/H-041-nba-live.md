---
id: H-041
title: "NBA/NCAAB live: medios, favoritos que pasan a underdog, totales"
kind: market
sport: nba
status: untested
n_videos: 8
n_variants: 8
first_mention: 2020-03-24
last_mention: 2026-02-09
---

# H-041 · NBA/NCAAB live: medios, favoritos que pasan a underdog, totales

**Estado:** ⬜ sin probar · 📊 se puede probar con datos de mercado

## Qué dice
NBA/NCAAB live: tomar ambos ML a precio positivo en partidos con spread ≤3 (un “middle” que no está garantizado), comprar el favorito pregame cuando pasa a underdog, over live cuando el total cae ≥15 y props live después de un primer cuarto frío.

## Lectura previa (antes de los datos)
La versión “garantizada” ignora que puede entrar solo una pata. Asumir que la probabilidad pregame no cambia después del primer cuarto es incorrecto.

## Plan de prueba
Necesita odds live históricas. Si no hay, simular con play-by-play la probabilidad de que ambos lados lleguen a precio positivo y el retorno resultante.

## Variantes (8) y videos (8)

### `nba-live-both-sides-plus-money-close-spread`
- [-K_KkoIwYL4](https://www.youtube.com/watch?v=-K_KkoIwYL4) (2020-03-24) Live In-Game Sports Betting Strategies & Tips For 2024 (Guaranteed Winning Bets⁉️)
  - Condición → apuesta: juego con spread pregame ≤3; tomar un lado a plus money y luego el otro cuando también cotice plus money, mismo stake
  - Claim: ganancia "garantizada" y frecuente (casi todo juego ≤-3)
- [2hkIiqn3-vA](https://www.youtube.com/watch?v=2hkIiqn3-vA) (2022-11-22) Win Every Game You Bet On In NCAAB With This Strategy
  - Condición → apuesta: spread pregame -1 a -4; juego a 1-4 puntos con 10 min del 1er tiempo → ML al underdog en plus money; si luego pasa a favorito, ML al otro lado en plus money en otro book
  - Claim: "ganas cada apuesta"
- [VnbxySahWoM](https://www.youtube.com/watch?v=VnbxySahWoM) (2024-02-06) Never Lose an NBA Bet Again with This Genius Sports Betting Strategy!?!
  - Condición → apuesta: spread ≤3, tras 4–5 min de Q1 parejo → 0.5 u al lado (+); al invertirse, 0.5 u al otro lado en (+)
  - Claim: "garantiza ganancia", "nunca pierdas"
- [UOCh3ZGOlRI](https://www.youtube.com/watch?v=UOCh3ZGOlRI) (2024-12-10) NBA Sports Betting Strategy That Guarantees You Daily Profits
  - Condición → apuesta: spread pregame -1 a -3, favorito no lidera por 10+ tras Q1 → ML del lado (+) por 0.75 u; si el otro lado pasa a (+), 0.75 u ahí (en otra casa)
  - Claim: ganancia "garantizada"

### `nba-live-buy-pregame-favorite-turned-underdog`
- [-K_KkoIwYL4](https://www.youtube.com/watch?v=-K_KkoIwYL4) (2020-03-24) Live In-Game Sports Betting Strategies & Tips For 2024 (Guaranteed Winning Bets⁉️)
  - Condición → apuesta: favorito pregame que, por una racha temprana del rival, pasa a cotizar como underdog → apostarlo en vivo
  - Claim: "gran valor", sin cifra

### `nba-live-total-over-after-big-drop`
- [-K_KkoIwYL4](https://www.youtube.com/watch?v=-K_KkoIwYL4) (2020-03-24) Live In-Game Sports Betting Strategies & Tips For 2024 (Guaranteed Winning Bets⁉️)
  - Condición → apuesta: total en vivo ≥~15 puntos por debajo del total de cierre tras un cuarto de baja anotación → over en vivo
  - Claim: los books "nunca" se desvían 16-20 puntos del cierre

### `nba-live-prop-buy-after-slow-1q`
- [L4vLUNTHy6g](https://www.youtube.com/watch?v=L4vLUNTHy6g) (2025-03-04) Get A 20% Edge Over The Sportsbooks Using This NBA Sport Betting Strategy
  - Condición → apuesta: prop over pregame de alta prob. cuyo jugador tiene 1Q flojo (o problemas de faltas) y la misma línea cae a ~-150 → apostar el over en vivo
  - Claim: +17% de edge (77% real vs 60% implícito)

### `nba-live-prop-under-after-hot-1q`
- [L4vLUNTHy6g](https://www.youtube.com/watch?v=L4vLUNTHy6g) (2025-03-04) Get A 20% Edge Over The Sportsbooks Using This NBA Sport Betting Strategy
  - Condición → apuesta: under pregame de alta prob.; el jugador arranca muy fuerte en 1Q y el mismo número under queda a ~-150 (especialmente si su patrón de rotación le da pocos minutos en el 2Q) → apostar el under en vivo
  - Claim: +17% de edge

### `nba-live-both-sides-plus-money-close-games`
- [RUEbuNLFQZQ](https://www.youtube.com/watch?v=RUEbuNLFQZQ) (2025-10-30) The NBA Betting System That Never Fails
  - Condición → apuesta: spread pregame ≤2, ambas defensas bottom-10, diferencia ≤5 al final del 1Q → apostar al que pierde a ~+150 y, tras una racha contraria, al otro lado a ~+150 (books distintos); seguro pregame de 25% del stake al favorito
  - Claim: "beneficio garantizado", "nunca falla"

### `nba-live-total-middle-240plus`
- [c5P3woi1Kyw](https://www.youtube.com/watch?v=c5P3woi1Kyw) (2026-02-09) Double Your Money In The NBA With This Sports Betting Strategy (2 Easy Steps)
  - Condición → apuesta: total ≥240; apostar un lado al tip-off; cuando el total vivo se mueve 10-15+ puntos a favor, apostar el lado opuesto en otro book a ~-110
  - Claim: "duplicas tu dinero" al acertar el middle

### `nba-live-pra-over-after-cold-start`
- [o0fLpbF9SdI](https://www.youtube.com/watch?v=o0fLpbF9SdI) (2023-11-17) How To Get NBA Player Props At Even Money
  - Condición → apuesta: jugador objetivo con producción baja en los primeros 3-4 min → over a la línea pregame con precio mejorado (-150 a +100); si arranca fuerte, no apostar
  - Claim: convertir -250 en ~even money

## Relaciones
- Índice: [index](../index.md) · Contradicciones: [contradictions](../contradictions.md) · Evolución: [timeline](../timeline.md)
