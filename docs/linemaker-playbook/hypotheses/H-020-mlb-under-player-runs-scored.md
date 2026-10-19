---
id: H-020
title: "MLB: under 0.5 carreras anotadas del bateador"
kind: market
sport: mlb
status: untested
n_videos: 5
n_variants: 1
first_mention: 2022-07-19
last_mention: 2026-04-01
---

# H-020 · MLB: under 0.5 carreras anotadas del bateador

**Estado:** ⬜ sin probar · 📊 se puede probar con datos de mercado

## Qué dice
MLB: siempre under 0.5 carreras anotadas del bateador, a −200/−300, sobre todo para bateadores del fondo del lineup contra buenos abridores.

## Lectura previa (antes de los datos)
Es la regla MLB que más repite en 5 videos. Es plausible que el mercado esté bien calibrado, pero hay que medirlo. Es una buena primera prueba para `mlb-canes-analytics`.

## Plan de prueba
Con Retrosheet/Statcast calcular P(R=0) por posición en el lineup × calidad del abridor (xFIP) × parque. Compararla con precios de props históricos (o con −250 como referencia si no hay líneas). Hacer walk-forward por temporada.

## Variantes (1) y videos (5)

### `mlb-under-player-runs-scored`
- [muUH-9zFVBc](https://www.youtube.com/watch?v=muUH-9zFVBc) (2022-07-19) New Sports Betting App That Finds You (Almost) 70% Winners!
  - Condición → apuesta: bateador del fondo del lineup (o recién subido) frente a un abridor del que esperas buena salida → under 0.5 carreras
  - Claim: 80% (8/10) en el ejemplo
- [VsklOUwl57U](https://www.youtube.com/watch?v=VsklOUwl57U) (2024-08-02) This Sports Bettor Doubled His Bankroll After Learning The Linemaker Method
  - Condición → apuesta: bateador en los 3 últimos del orden + pitcher rival bueno → under 0.5 carreras
  - Claim: "la mayoría me han pegado"
- [xlBD5MdvUlU](https://www.youtube.com/watch?v=xlBD5MdvUlU) (2025-03-27) How To Actually Make Money Sports Betting On The MLB
  - Condición → apuesta: bateador con mal historial contra el abridor (o en general) → under 0.5 carreras anotadas
  - Claim: "la apuesta más rentable de MLB"; precios −200 a −300; a veces "95%"
- [bwrzVTRN_OM](https://www.youtube.com/watch?v=bwrzVTRN_OM) (2025-07-22) 30 Day Sports Betting Challenge ($10k Bankroll Into ???)
  - Condición → apuesta: bateador "to not cross the plate" → under 0.5 carreras anotadas
  - Claim: ninguno explícito
- [mbxBU5XjbM8](https://www.youtube.com/watch?v=mbxBU5XjbM8) (2026-04-01) How to Make $50 Per Day Betting on Sports (The Math)
  - Condición → apuesta: siempre → under 0.5 carreras anotadas
  - Claim: ninguno específico (es parte del sistema del 85%)

## Relaciones
- Índice: [index](../index.md) · Contradicciones: [contradictions](../contradictions.md) · Evolución: [timeline](../timeline.md)
