---
id: H-012
title: "Kalshi/Polymarket: comprar “No”, precios viejos, modelo vs precio"
kind: market
sport: multi
status: untested
n_videos: 7
n_variants: 5
first_mention: 2025-12-01
last_mention: 2026-09-25
---

# H-012 · Kalshi/Polymarket: comprar “No”, precios viejos, modelo vs precio

**Estado:** ⬜ sin probar · 📊 se puede probar con datos de mercado

## Qué dice
En Kalshi/Polymarket: comprar “No” en longshots y en props de goleador o asistente, comprar cuando su probabilidad > precio, y aprovechar precios viejos en mercados de menciones.

## Lectura previa (antes de los datos)
El sesgo favorito-longshot en mercados de predicción está documentado. El de precios viejos es más bien una curiosidad, con poca liquidez.

## Plan de prueba
Con la API histórica de Kalshi medir el retorno de comprar “No” por bucket de precio (1-10¢) en outrights y props. Esto conecta directo con tus repos de Kalshi.

## Variantes (5) y videos (7)

### `pm-buy-when-model-prob-exceeds-price`
- [WFHg_pvRxhQ](https://www.youtube.com/watch?v=WFHg_pvRxhQ) (2025-12-01) +$2,000,000 From One Simple Sports Betting Strategy
  - Condición → apuesta: mover el volumen ganador a Kalshi/Novig para evitar límites
  - Claim: se pueden colocar montos enormes (hasta "$1M")
- [W6Ac37hxyII](https://www.youtube.com/watch?v=W6Ac37hxyII) (2026-03-18) How To Legally Bet on Sports in California, Texas and Georgia (2026)
  - Condición → apuesta: prob. estimada > precio del contrato (+ comisiones) → comprar "Sí"
  - Claim: mercados más blandos que las casas en 2026
- [WO-BY_28oM4](https://www.youtube.com/watch?v=WO-BY_28oM4) (2026-09-25) If I Had To Make $300 On NFL This Weekend, I’d Do This
  - Condición → apuesta: prob. estimada > precio del contrato → comprar Sí; verificar volumen
  - Claim: sin límites de apuesta

### `pm-mention-markets-post-event-stale-prices`
- [kTSD2sxtqJc](https://www.youtube.com/watch?v=kTSD2sxtqJc) (2026-02-05) How To Bet On Polymarket And Actually Win (Guaranteed Profit)
  - Condición → apuesta: el evento ya terminó (emisión en vivo en la costa este) y el mercado sigue abierto con precios que no reflejan el resultado → comprar el lado ya conocido
  - Claim: "dinero garantizado", entre 5 y 20% por operación

### `pm-buy-no-longshot-outrights`
- [lWB1VmwMbl4](https://www.youtube.com/watch?v=lWB1VmwMbl4) (2026-07-29) The Kalshi Bet That's Basically Free Money
  - Condición → apuesta: contrato de longshot (Sí ≤ ~6-10¢) → comprar "No"
  - Claim: "dinero gratis", 100% de prob. real

### `prediction-markets-fade-early-leader`
- [rAiVEC8QLS0](https://www.youtube.com/watch?v=rAiVEC8QLS0) (2026-07-15) This Sports Betting Mistake Is Keeping You Broke
  - Condición → apuesta: líder tras la ronda 1 (golf) o tras 100 vueltas (NASCAR) → "No" a que gane
  - Claim: "no puedo decir cuántas veces gané" [05:09]

### `kalshi-buy-no-player-props`
- [w0rQSgDN2CA](https://www.youtube.com/watch?v=w0rQSgDN2CA) (2026-06-28) How To Bet World Cup Knockout Stages On Kalshi
  - Condición → apuesta: comprar "No" en jugador anota/asiste cuando el precio del "Sí" está inflado
  - Claim: "edges enormes" en el No

## Relaciones
- Índice: [index](../index.md) · Contradicciones: [contradictions](../contradictions.md) · Evolución: [timeline](../timeline.md)
