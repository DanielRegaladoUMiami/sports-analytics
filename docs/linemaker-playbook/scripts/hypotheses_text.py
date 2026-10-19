"""Texto de síntesis por hipótesis: (qué dice, lectura previa, plan de prueba).
Escrito a mano después de leer los reportes de los 12 lotes. Lo demás (variantes, videos, fechas) se genera desde videos/."""

T = {
"H-001": (
 "Es el núcleo de su método desde ~2022 y domina 2025-2026. Apostar favoritos pesados (casi siempre props o líneas alternas) entre −200 y −700, "
 "solo cuando su “probabilidad real” supera la implícita. La “probabilidad real” casi siempre es el hit rate de la temporada, o el promedio entre el hit rate de la temporada y el hit rate contra defensas similares.",
 "Para que tenga sentido, la probabilidad tiene que estar bien calibrada **sin vig** y medirse contra el precio de cierre. Su estimador (hit rate muestral de 10-40 juegos) es ruidoso y está sesgado hacia arriba por selección. "
 "Su propio tracker 2025 (75% a −241 promedio, break-even 70.7%) apunta a un edge chico (~+6% por apuesta), muy lejos del 85% que vende. Los props tienen hold alto, así que la implícita sin vig es menor que la que él usa.",
 "Reunir líneas históricas de props alternas (OddsJam/The Odds API/Unabated, o snapshots propios) junto con los resultados. Para cada apuesta que cumpla la regla: hit rate frente a la implícita sin vig, ROI por bucket de odds (−200/−300/−500/−700), CLV, e intervalo de confianza con Wilson o bootstrap. "
 "Hacer walk-forward: estimar el hit rate solo con datos anteriores a la fecha."),
"H-002": (
 "Dentro de una escalera de líneas alternas, elegir el escalón donde (hit rate − probabilidad implícita) es mayor, en vez de la línea principal. Lo aplica en todos los deportes.",
 "Maximizar la diferencia de probabilidad no es lo mismo que maximizar el EV: el EV depende del pago, y un video lo muestra (el escalón −116 era mejor que el que eligió). "
 "Además, las escaleras alternas tienen más hold en los extremos.",
 "Usar la misma base de H-001. Para cada escalera, comparar tres criterios: (a) el escalón con mayor gap, (b) el de mayor EV = p·pago − (1−p), y (c) la línea principal. Comparar ROI y CLV fuera de muestra."),
"H-003": (
 "Evitar las líneas −110 porque, según él, son ≤50% y no tienen edge. Prefiere favoritos juiceados.",
 "Hay un error lógico: en un mercado −110/−110 al menos un lado es ≥50%. Que el −110 tenga poco edge en promedio no implica que el −300 tenga más. "
 "El sesgo favorito-longshot existe en algunos mercados, pero hay que medirlo.",
 "Calcular el ROI histórico por bucket de odds (−110, −150, −200, −300, −500) en props y sides, usando precios de cierre. Es un test descriptivo directo del sesgo favorito-longshot."),
"H-004": (
 "Ir contra el público: favoritos populares (Lakers, Cowboys), overs, equipos grandes del Mundial y lados con ≥80% de tickets.",
 "Choca de frente con H-001, porque su producto principal son favoritos. La evidencia académica de que ir contra el público rinde es débil y depende de la época.",
 "Usar datos históricos de % de tickets y % de dinero (Action Network/VSiN, si se consiguen) y medir el ATS/ROI del lado contrario cuando los tickets son ≥80%, por deporte y temporada."),
"H-005": (
 "Parlays de 2-3 patas, donde cada pata es un prop con ≥85-90% de “probabilidad real”. Los presenta como “la única excepción” a su regla de no hacer parlays.",
 "Multiplica probabilidades como si las patas fueran independientes y usa probabilidades infladas. En un video, con sus propios números el parlay tiene EV negativo (81.4% real contra 83.4% implícito). "
 "El hold de las patas se compone.",
 "Simular con las patas de H-001/H-002: P(parlay) = producto de las probabilidades calibradas, frente al precio ofrecido. Comparar el ROI de los parlays con el de las mismas patas apostadas por separado."),
"H-006": (
 "SGPs “correlacionados”: yardas del QB + yardas del WR1, ML del favorito + team total over 1.5, varias líneas del mismo jugador.",
 "Se contradice: dice que las casas no cobran la correlación y también que sí la cobran. Calcula la probabilidad como si las patas fueran independientes. "
 "Las casas sí aplican ajustes de correlación en los SGP, así que en general el edge es negativo.",
 "Con play-by-play (nflfastR) estimar la probabilidad conjunta empírica de cada par de patas y compararla con el precio del SGP (requiere snapshots de precios de SGP)."),
"H-007": (
 "Solo apuestas directas: nada de parlays, boosts ni pick'em de PrizePicks o Underdog.",
 "Es un buen consejo general (los parlays componen el hold), pero se contradice con H-005 y H-006 en decenas de videos.",
 "No hace falta probarlo con datos; es aritmética del hold. Sirve como referencia para ver en qué videos se contradice."),
"H-008": (
 "Seguir el steam: apostar en la dirección de un movimiento grande desde la apertura y no apostar juegos cuya línea no se movió.",
 "Si te subes tarde a un movimiento, pagas el precio malo. El edge, si existe, está en llegar antes del movimiento, no después.",
 "Con series de apertura → cierre (con timestamp) medir el ROI de apostar al precio actual en la dirección del movimiento, en distintos momentos (T−24h, T−1h). Lo esperable es ROI cercano a −vig."),
"H-009": (
 "Si el % de dinero supera al % de tickets, se sigue al dinero (sharp money). Lo combina con el movimiento de línea y un historial H2H ATS de 10 juegos.",
 "En otro video dice que el sharp money y el RLM son “basura”. El H2H de 10 juegos de hace varios años es ruido. Los datos de splits públicos son de calidad dudosa.",
 "Usar splits históricos de dinero y tickets y medir el ROI cuando dinero − tickets ≥ 20 pts, con y sin el filtro H2H, para NFL, NCAAF, NCAAB y WNBA."),
"H-010": (
 "Comprar medio punto o más para cruzar números clave (NFL 3/7/10/14; CFB 17/21/24...), comprar de vuelta hasta la línea de apertura y teasers de 2 equipos (Wong).",
 "Comprar medio punto alrededor del 3 y del 7 en la NFL puede valer la pena según el precio. Comprar 2-4 puntos casi nunca lo vale. En CFB los números clave son mucho más débiles. "
 "Los teasers Wong funcionaron históricamente, pero hoy las casas los cobran caro.",
 "Con la distribución empírica de márgenes NFL/CFB (nflfastR/cfbfastR), calcular P(push) por número y el precio justo de cada medio punto. Compararlo con el costo típico (−120/−130 por medio punto)."),
"H-011": (
 "Hacer line shopping, apostar el precio que se sale del consenso sin vig (OddsJam), y aprovechar escaleras desalineadas entre casas (ER 2.5 contra 1.5).",
 "Es el único principio en el que coincide con el consenso sharp, pero en otro video desprecia el +EV por diferencia de precio. Lo promueve como afiliado de OddsJam.",
 "Medir el CLV de las apuestas al mejor precio frente al precio promedio. Detectar outliers frente a Pinnacle/consenso sin vig y medir su ROI."),
"H-012": (
 "En Kalshi/Polymarket: comprar “No” en longshots y en props de goleador o asistente, comprar cuando su probabilidad > precio, y aprovechar precios viejos en mercados de menciones.",
 "El sesgo favorito-longshot en mercados de predicción está documentado. El de precios viejos es más bien una curiosidad, con poca liquidez.",
 "Con la API histórica de Kalshi medir el retorno de comprar “No” por bucket de precio (1-10¢) en outrights y props. Esto conecta directo con tus repos de Kalshi."),
"H-020": (
 "MLB: siempre under 0.5 carreras anotadas del bateador, a −200/−300, sobre todo para bateadores del fondo del lineup contra buenos abridores.",
 "Es la regla MLB que más repite en 5 videos. Es plausible que el mercado esté bien calibrado, pero hay que medirlo. Es una buena primera prueba para `mlb-canes-analytics`.",
 "Con Retrosheet/Statcast calcular P(R=0) por posición en el lineup × calidad del abridor (xFIP) × parque. Compararla con precios de props históricos (o con −250 como referencia si no hay líneas). Hacer walk-forward por temporada."),
"H-021": (
 "MLB: bateador under 1.5 hits, sobre todo con mal historial contra el abridor o frente al pitcher más usado en DFS.",
 "El BvP (bateador contra pitcher) tiene muy poco poder predictivo con <30 PA. P(≥2 H) se puede modelar bien con una binomial de PA × AVG esperado.",
 "Usar un modelo binomial o de Poisson de hits por juego (PA esperados por posición en el lineup, xBA contra la mano del pitcher) y comparar el under 1.5 con precios históricos. Medir el lift incremental del BvP."),
"H-022": (
 "MLB: bateador over 0.5 hits cuando el hit rate de la temporada > implícita, con buen BvP o con alta propiedad en DFS. Incluye la versión live después de empezar 0-2.",
 "La versión live es una falacia: después de 0-3 quedan menos PA, así que la probabilidad baja. El resto es la mecánica de H-001 aplicada a MLB.",
 "Usar el mismo modelo binomial de H-021 para P(≥1 H) y compararlo con precios. Para la versión live, P(≥1 H | 0-for-k) con los PA restantes."),
"H-023": (
 "MLB: “no HR” del bateador, en parlays de 2-4 patas, contra ases y en parques que suprimen HR.",
 "La probabilidad base de no batear HR es ~85-90% por juego y las casas la ponen a −700/−1000. El edge es mínimo y el parlay compone el hold.",
 "P(HR=0) con barrel%, HR/FB del pitcher y factor de parque, frente a precios históricos de props de HR."),
"H-024": (
 "MLB: under 2.5/3.5 ER del abridor cuando es el ace o el más usado en DFS frente a una ofensiva débil; over 1.5 frente a ofensivas top. También aprovechar casas que ponen 2.5 cuando el mercado está en 1.5.",
 "Es plausible que haya valor puntual en discrepancias entre casas. El resto depende de lo mismo que H-001. Que la regla de ER dependa de cuántas entradas lanza el abridor es un problema que él ignora.",
 "Modelar ER por apertura en función de IP esperado × (xFIP, wOBA del rival, parque) y compararlo con líneas. Por separado, medir con qué frecuencia una casa pone 2.5 cuando el consenso es 1.5 y qué ROI deja."),
"H-025": (
 "MLB: over de hits permitidos para abridores que lanzan muchas entradas o para el underdog contra un favorito fuerte; under alterno 6.5/7.5 para ases.",
 "Dice que tiene un video dedicado a esto. Los hits permitidos dependen mucho de las IP, la BABIP y la defensa.",
 "Modelo de hits permitidos = BF esperados × (1 − K% − BB%) × BABIP esperada, comparado con líneas."),
"H-026": (
 "MLB: over de strikeouts del abridor cuando el hit rate de la temporada > implícita, ajustado por el K% del rival; over de outs para los que lanzan muchas entradas; K en el primer turno al bate del peor bateador.",
 "Los props de K son de los mercados más estudiados (hay modelos públicos), así que hay poco margen. Los de outs dependen del manejo del bullpen.",
 "Usar un modelo de K (K% del pitcher × K% del rival × BF esperados) y comparar contra líneas de cierre."),
"H-027": (
 "MLB, mercados variados: modelo de totales con 5 factores (edge ≥0.75 carreras), ajuste por viento de ±0.5, totales alternos 6.5/11.5 filtrados, team total over 1.5, “sin carrera en el 2º/3º inning” en vez de NRFI, ignorar la última apertura del pitcher.",
 "Lo del viento y el parque es real, pero el mercado ya lo descuenta. Los totales alternos extremos tienen mucho hold.",
 "Usar Retrosheet con clima (viento) y totales de cierre para medir el residuo del total en función del viento. En los innings, P(0 carreras) por inning comparada con precios."),
"H-030": (
 "NFL/CFB: yardas alternas del QB por debajo de su promedio contra secundarias débiles, 1+ TD de pase contra defensas que permiten muchos y QB senior en CFB.",
 "Poner la línea por debajo del promedio no te da edge si el precio ya lo refleja. La varianza de las yardas de pase es alta.",
 "Con nflfastR, construir la distribución de yardas de pase por QB × defensa (EPA/dropback permitido) y comparar P(yardas ≥ escalón) con los precios de la escalera alterna."),
"H-031": (
 "NFL: yardas por tierra alternas del RB (escalones bajos) contra defensas débiles contra la carrera, el RB recién nombrado titular y unders contra defensas top 5.",
 "Depende muchísimo del guion del partido y del reparto de acarreos.",
 "Distribución de acarreos × YPC por RB, y defensa (yardas por acarreo permitidas). Comparar con escaleras alternas."),
"H-032": (
 "NFL/CFB: yardas alternas del WR1 contra secundarias blandas, unders contra defensas duras, overs para los más usados en DFS y middles over/under del mismo jugador en distintas casas.",
 "Los middles entre casas son la única variante con lógica de precio. Lo demás repite H-001.",
 "Target share × aDOT × catch rate frente a la defensa, y medir con qué frecuencia aparecen middles reales entre casas."),
"H-033": (
 "NFL: puntos del kicker over 5.5 (o alterno) con un kicker de FG% ≥90% contra una defensa que permite muchos FG.",
 "Es un mercado de nicho con poco límite, donde podría haber ineficiencia real.",
 "Con nflfastR, puntos por juego del kicker en función de los drives que se frenan en la zona de FG; P(≥6) comparada con el precio."),
"H-034": (
 "NFL/CFB, totales: under de 1H 28.5 con ofensivas débiles, filtro de YPP, proyección por ritmo × puntos por jugada, under con viento o lluvia, over en CFB con calor y viento moderado, under en pretemporada.",
 "El clima (viento fuerte) es de las pocas señales con soporte empírico, aunque el mercado ya lo ajusta. Las reglas de calor parecen sobreajustadas.",
 "Usar los totales de cierre con resultados y clima (nflfastR trae temperatura y viento) y hacer una regresión del residuo del total sobre viento, temperatura, ritmo y YPP."),
"H-035": (
 "NFL/CFB, live y sides: favorito pregame más barato en live después de un mal inicio, ML en vez de spread cuando es −1 a −4, ir contra los picks de TV y apuestas novedad (primera jugada carrera, punt en el primer drive).",
 "Las novedades son ruido. Lo de comprar en live al favorito pregame merece revisarse con datos de probabilidad de victoria.",
 "Con un modelo de win probability de nflfastR, ver si la línea live sobrerreacciona al marcador temprano (necesita datos de odds live)."),
"H-040": (
 "NBA: props de PRA, puntos y rebotes contra la defensa por posición (DvP). Over si el jugador tiene mucho uso y la defensa es mala, under si tiene poco uso y la defensa es top. Líneas alternas por debajo del promedio.",
 "Se contradice sobre quién va al under de PRA (poco uso contra top 5, o estrellas contra defensas 6-10). El DvP es una métrica ruidosa y con confusores.",
 "Con box scores de la NBA y DvP calculado sin fuga de información, hacer una regresión del residuo (real − línea) sobre DvP, uso y minutos proyectados, ajustando por compañeros ausentes."),
"H-041": (
 "NBA/NCAAB live: tomar ambos ML a precio positivo en partidos con spread ≤3 (un “middle” que no está garantizado), comprar el favorito pregame cuando pasa a underdog, over live cuando el total cae ≥15 y props live después de un primer cuarto frío.",
 "La versión “garantizada” ignora que puede entrar solo una pata. Asumir que la probabilidad pregame no cambia después del primer cuarto es incorrecto.",
 "Necesita odds live históricas. Si no hay, simular con play-by-play la probabilidad de que ambos lados lleguen a precio positivo y el retorno resultante."),
"H-042": (
 "NBA: over de totales alternos del primer cuarto (sobre todo en series de playoffs), total de 2ª mitad por regresión del FG% del 1er tiempo y proyección por eficiencia × ritmo.",
 "La regresión del FG% es real, pero el mercado de 2ª mitad ya la descuenta en parte.",
 "Con play-by-play, ver si el FG% del primer tiempo frente al de la temporada predice el residuo del total de 2ª mitad respecto a la línea."),
"H-043": (
 "NBA, situacionales: evitar overs de estrellas si hay riesgo de paliza (titulares fuera con +16 en el 4º), ir contra equipos en back-to-back, favorito local en Game 5 con la serie 2-2, y desconfiar de favoritos chicos de visita.",
 "Lo de las palizas y los minutos es real y medible. Los back-to-back ya están en el precio.",
 "Minutos del 4º cuarto en función del margen; ATS por situación de descanso."),
"H-050": (
 "NHL: under del 1er periodo 2.5 entre buenas defensas, totales alternos por tendencia H2H, línea de 60 minutos en vez de ML −300, +1.5/+2.5 en el puck line, puntos del PP1 y unders de jugadores del PP2. Además, dice que la NHL es el deporte “más rentable”.",
 "Lo de la línea de 60 minutos frente al ML tiene lógica de precio. Lo demás se basa en H2H con muestras chicas.",
 "Con datos NHL (MoneyPuck), distribución de goles por periodo y P(gana en tiempo regular) frente al precio de la línea de 60 minutos."),
"H-055": (
 "NCAAB: filtro de totales por ritmo y eficiencia (KenPom), seeds 1-3 con defensa élite en spread alterno durante el torneo, under de 1er tiempo con totales altos, conferencias chicas.",
 "Las conferencias chicas son mercados menos eficientes, una idea razonable pero con límites bajos.",
 "Con KenPom y totales de cierre, medir el residuo en función del ritmo y la eficiencia, y el ATS en el torneo por seed y ranking defensivo."),
"H-060": (
 "Soccer: over 1.5 goles en mismatches del Mundial (top 15 contra 40+) y en ligas goleadoras (Bundesliga, Eredivisie), over 0.5 en el 2º tiempo, y apostar solo totales en ligas chicas.",
 "Over 1.5 a −300/−500 en mismatches suele estar bien calibrado. Hay un error grave en un video: dice que hay empates el 3.5% de las veces, cuando son ~25-28%.",
 "Con football-data.co.uk (resultados y cuotas de cierre de muchas ligas), calcular el hit rate del over 1.5 por liga y bucket de cuota frente a la implícita sin vig."),
"H-061": (
 "Soccer: under 3.5/4.5 en el Mundial (grupos por nivel de ranking, knockouts defensivos), under 1.5 del 1er tiempo entre top 15 y la idea de que el público infla los overs.",
 "Los knockouts tienden a tener menos goles; hay que ver si el precio ya lo descuenta.",
 "Mismo dataset que H-060 más histórico de Mundiales y Euros: under 3.5 por fase y por diferencia de ranking."),
"H-062": (
 "Soccer, otros mercados: “to advance” en vez del 1X2 en knockouts, evitar el 1X2, over 1.5 tiros del atacante.",
 "En un video calcula P(≥2 tiros) ≈ 90% con una media de 2.5. Con Poisson da ~71%.",
 "Tiros por partido del jugador (FBref) con Poisson o binomial negativa frente al precio."),
"H-065": (
 "UFC: “la pelea no llega a la decisión” cuando ambos peleadores terminan ≥80-85% de sus peleas, pelea en el Apex con total de 1.5, en peleas femeninas “llega a la decisión” y ML del favorito con edge ≥5%.",
 "El finish rate de cada peleador es informativo, pero las muestras son chicas (10-20 peleas).",
 "Con UFCStats, P(finish) en función del finish rate de ambos, la división y el Apex, comparada con el precio de “doesn't go the distance”."),
"H-066": (
 "Tenis en hierba: over de games entre dos grandes sacadores, under con desajuste de saque y devolución, favorito en sets corridos con filtros de ranking y superficie.",
 "Es lógica de saque y devolución estándar, que el mercado modela bien.",
 "Con datos de Jeff Sackmann y tennis-data.co.uk, modelo de games por % de hold y break, comparado con las líneas."),
"H-067": (
 "Golf: pasar el corte si el jugador tiene ≥5 participaciones y ≥80% de cortes pasados en el campo, más buena forma.",
 "El historial en un campo tiene poco poder predictivo frente al strokes gained general (DataGolf).",
 "Con DataGolf, comparar el modelo de SG con y sin historial del campo para predecir el corte, frente al precio."),
"H-068": (
 "Carreras de caballos: exactas en carreras de claiming baratas, steam tardío y top trainer + top jockey.",
 "El takeout es alto (15-25%) y él mismo calcula mal el de las exactas. Es su peor terreno.",
 "No priorizar."),
"H-069": (
 "Cricket T20: over 250.5 con filtros de promedio de equipo y de sede.",
 "Hay un solo video. No priorizar.",
 "No priorizar."),
"H-070": (
 "DFS: solo 50/50 de entrada única.",
 "Calcula mal el pago (es ~1.8x, no 2x), así que sus ganancias mensuales están infladas.",
 "No aplica."),
"P-001": (
 "Unidad fija como % del bankroll. Sus cifras van de 1% a 5% según el video, 5% para bankrolls chicos, “arriesgar 1u, no apostar para ganar 1u” en favoritos y escalonar la unidad según la probabilidad.",
 "La idea de fondo (unidad fija y chica) es correcta, pero se contradice en casi todos los videos. Si su edge fuera el que dice (85% a −300), Kelly recomendaría ~40%, así que su propio sizing muestra que no cree en esos números.",
 "Simular el riesgo de ruina y el drawdown con Kelly fraccional usando el edge **medido** en H-001."),
"P-002": (
 "Interés compuesto: recalcular la unidad cada mes (algunas veces cada 2-4 semanas), y la tabla de $10k → $1M. No retirar hasta haberlo probado, o retirar lo que exceda el bankroll base.",
 "Sus tablas son crecimiento geométrico hipotético (×1.10-1.15 al mes) y no resultados. Subir la unidad al ganar y no bajarla al perder aumenta el riesgo de ruina.",
 "Simulación Monte Carlo con el edge y la varianza medidos."),
"P-003": (
 "Reglas de stop y de metas: parar después de 1 o 3 derrotas, stop-loss mensual de −5%, meta de +1u al día o +1u por bloque de 3 días, 1-5 o 5-7 apuestas al día, media unidad en playoffs, julio-agosto y principio de temporada, y nada de partidos en TV nacional.",
 "Matemáticamente, los stops no cambian el EV; solo controlan el tilt. Se contradice entre “apostar todos los días” y “ser selectivo”.",
 "No requiere datos; son reglas de disciplina."),
"P-004": (
 "Evitar Martingala, Fibonacci y Paroli, aunque en un video propone una escalera Martingala ($100/$300/$900/$2,700) en jugadas de −200.",
 "Evitarlas es correcto. Su video de Martingala se contradice con su propia regla de no perseguir pérdidas.",
 "No aplica."),
"P-005": (
 "Evitar límites: repartir las apuestas en varias casas en montos redondos, como máximo $500 por casa, hacer parlays basura para parecer recreativo, pasarse a mercados de predicción y (admitido) usar cuentas de familiares o varias cuentas.",
 "Varias de estas tácticas violan los términos de servicio de las casas (multicuenta). Que lo limiten es, en todo caso, señal de que gana algo.",
 "No aplica."),
"P-006": (
 "Proceso: solo apostar con gap ≥3-5 pts, una checklist de 7 puntos, 200 apuestas en papel antes de usar dinero real, recalibrar cada 300 apuestas por bucket y apostar cerca del inicio después de las noticias.",
 "La parte de recalibrar por bucket después de 300 apuestas es la mejor práctica que menciona y es justo la que menos aplica.",
 "Es la plantilla de evaluación para tus propios trackers (calibración por bucket y CLV)."),
"P-007": (
 "Apostar a equipos con ~10 derrotas seguidas y seguir a un capper después de una mala racha.",
 "Es la falacia del jugador.",
 "No aplica."),
}
