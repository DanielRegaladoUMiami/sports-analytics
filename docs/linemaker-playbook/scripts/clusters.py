"""Mapa slug de regla -> hipótesis consolidada (primer regex que matchea gana).
kind: market = testeable con datos de mercado; practice = bankroll/proceso; fallacy = regla que él da pero es una falacia."""
CLUSTERS = [
 # --- prácticas (van primero para no caer en reglas de mercado) ---
 ("P-004","martingale-and-progressions","Martingala y progresiones de stake","practice","multi",r"martingale|progression"),
 ("P-007","gamblers-fallacy-rules","Reglas basadas en la falacia del jugador","fallacy","multi",r"losing-streaks|tout-join-after-cold"),
 ("P-005","beating-account-limits","Evitar límites de las casas (repartir stakes, cuentas)","practice","multi",r"split-unit-across|split-stakes|max-500|prime-accounts|use-prediction-markets"),
 ("P-002","compounding-monthly-rebase","Interés compuesto: recalcular la unidad cada mes","practice","multi",r"monthly-rebase|monthly-unit-recalc|compound|unit-resize|monthly-compound|withdraw"),
 ("P-003","stop-rules-and-goals","Reglas de stop, metas y volumen","practice","multi",r"stop|monthly-unit-goal|daily-plus|three-day|^target-|set-and-forget|limit-daily|nov-jan|reduce-stakes|half-units|playoffs-half|minimal-stake|avoid-big-stakes|avoid-primetime|avoid-betting-favorite"),
 ("P-001","unit-sizing","Tamaño de unidad (% del bankroll)","practice","multi",r"unit|stake-cap|max-bet|max-stake|risk-one|flat-risk|golf-stake|confidence-no-stake|cap-open|max-open-exposure"),
 ("P-006","edge-threshold-and-process","Umbral de edge y proceso antes de apostar","practice","multi",r"min-gap|min-edge|positive-probability|bet-only-positive|paper-trade|recalibrate|sides-totals-wait|bet-close-to-start|bet-near-close"),
 ("H-007","no-parlays","Solo apuestas directas, sin parlays ni boosts","practice","multi",r"straight-bets|^avoid-parlays|avoid-multileg|avoid-parlays-5plus|avoid-sgp-profit|avoid-sportsbook-odds-boosts"),
 # --- mercado: transversales ---
 ("H-004","fade-public-favorites","Fade al público: favoritos y overs sobrevalorados","market","multi",r"avoid-public-favorites|fade-overs-and-favorites|avoid-ml-favorites|wc-fade-public|fade-small-road|public-overs-shaded|fade-public-80|avoid-point-spreads"),
 ("H-010","key-numbers-buy-points","Números clave y compra de puntos","market","multi",r"key-number|buy-points|buy-off|teaser|buy-through|buy-total-back|buy-back-to-opening"),
 ("H-009","money-vs-tickets","Dinero vs tickets (sharp money / RLM)","market","multi",r"money-vs|sharp-money|rlm-fade|follow-money-vs-public|steam-h2h|line-move-h2h|wnba-alt-total-line-move|bet-split|total-over-steam"),
 ("H-008","follow-line-movement","Seguir el movimiento de línea (steam)","market","multi",r"line-move|follow-sharp-line|follow-steam|follow-late-line|follow-opening|small-market-follow"),
 ("H-011","line-shopping-price-discrepancy","Line shopping y discrepancias de precio entre casas","market","multi",r"line-shop|line-shopping|outlier-price|middle-arb|line-discrepancy|alt-line-mismatch|kalshi-vs-sportsbook|pm-kalshi-vs"),
 ("H-012","prediction-markets","Kalshi/Polymarket: comprar “No”, precios viejos, modelo vs precio","market","multi",r"^pm-|prediction-markets-fade|kalshi-buy-no"),
 ("H-006","sgp-correlated","SGP “correlacionados” (QB+WR, favorito+team total)","market","multi",r"sgp"),
 ("H-005","high-prob-leg-parlays","Parlays de 2-3 patas de alta probabilidad","market","multi",r"parlay"),
 ("H-003","avoid-minus110","Evitar líneas −110 / main lines","market","multi",r"minus-?110"),
 # --- MLB ---
 ("H-020","mlb-under-player-runs-scored","MLB: under 0.5 carreras anotadas del bateador","market","mlb",r"mlb-under-player-runs"),
 ("H-023","mlb-no-home-run","MLB: “no HR” del bateador","market","mlb",r"mlb.*(no-home-run|no-hr|under-hr|under-0-5-hr)"),
 ("H-021","mlb-batter-hits-under-1-5","MLB: bateador under 1.5 hits","market","mlb",r"mlb.*(hits-under|under-1-5-hits|under-batter-hits|batter-under-1|avoid-plus-money-batter|under-1\.5-hits)"),
 ("H-022","mlb-batter-1plus-hit","MLB: bateador over 0.5 hits (1+ hit)","market","mlb",r"mlb.*(record-a-hit|1plus-hit|over-0\.5-hits|over-0-5-hits)"),
 ("H-025","mlb-pitcher-hits-allowed","MLB: hits permitidos del abridor","market","mlb",r"mlb.*hits-allowed"),
 ("H-024","mlb-pitcher-earned-runs","MLB: carreras limpias (ER) del abridor","market","mlb",r"mlb.*(earned-runs|-er-|under-3-5|under-2-5)"),
 ("H-026","mlb-pitcher-k-and-outs","MLB: strikeouts y outs del abridor","market","mlb",r"mlb.*(pitcher-k|strikeout|pitcher-outs)"),
 ("H-027","mlb-totals-innings-other","MLB: totales, innings y otros mercados","market","mlb",r"^mlb-"),
 # --- Football ---
 ("H-033","nfl-kicker-points","NFL: puntos del kicker over","market","nfl",r"kicker"),
 ("H-030","football-qb-passing","NFL/CFB: yardas y TDs del QB","market","nfl",r"(nfl|ncaaf)-.*qb"),
 ("H-031","football-rb-rushing","NFL: yardas por tierra del RB","market","nfl",r"nfl-.*rb-|rush"),
 ("H-032","football-wr-and-yardage","NFL/CFB: yardas de WR y props de yardas","market","nfl",r"wr|nfl-top-dfs|star-alt-yards|middle-player-yards|ncaaf-yards"),
 ("H-034","football-totals-halves","NFL/CFB: totales, mitades, clima y ritmo","market","nfl",r"nfl-1h|nfl-total|bad-weather|ncaaf-over|ncaaf-under|preseason"),
 ("H-035","football-live-sides-novelty","NFL/CFB: live, sides y apuestas novedad","market","nfl",r"^(nfl|ncaaf)-|fade-tv"),
 # --- NBA ---
 ("H-041","nba-live","NBA/NCAAB live: medios, favoritos que pasan a underdog, totales","market","nba",r"nba-live"),
 ("H-042","nba-quarter-half-totals","NBA: totales de cuarto/mitad y regresión de FG%","market","nba",r"nba.*(1q|q1|2h|total-eff)"),
 ("H-040","nba-props-vs-dvp","NBA: props (PRA, puntos, rebotes) vs defensa por posición","market","nba",r"nba-.*(pra|points|rebounds|props|dfs)|props-matchup-dvp"),
 ("H-043","nba-situational","NBA: situacionales (blowouts, back-to-back, Game 5)","market","nba",r"^nba-"),
 ("H-050","nhl","NHL: totales, puck line, puntos y goleadores","market","nhl",r"^nhl-"),
 ("H-055","ncaab","NCAAB: totales por ritmo, spreads del torneo, conferencias chicas","market","ncaab",r"^ncaab?-"),
 # --- Soccer y otros ---
 ("H-061","soccer-unders","Soccer: unders (Mundial, knockouts, ligas defensivas)","market","soccer",r"(soccer|wc).*under"),
 ("H-060","soccer-overs","Soccer: over 1.5 / 2º tiempo / ligas goleadoras","market","soccer",r"(soccer|wc).*(over|totals-only|obscure)"),
 ("H-062","soccer-other","Soccer: “to advance”, tiros del jugador, evitar 1X2","market","soccer",r"^soccer-"),
 ("H-065","ufc","UFC: “no llega a la decisión” y favoritos","market","ufc",r"^ufc-"),
 ("H-066","tennis","Tenis: games en hierba y sets corridos","market","tennis",r"^tennis-"),
 ("H-067","golf","Golf: pasar el corte por historial en el campo","market","golf",r"^golf-"),
 ("H-068","horse-racing","Carreras de caballos: exactas, steam tardío","market","horse-racing",r"^horse"),
 ("H-069","cricket","Cricket T20: overs filtrados","market","multi",r"^cricket"),
 ("H-070","dfs","DFS: solo 50/50 de entrada única","market","multi",r"^dfs"),
 # --- favoritos / alt lines al final (son los más genéricos) ---
 ("H-001","heavy-favorites-true-prob","Favoritos pesados (−200 a −700) cuando prob. “real” > implícita","market","multi",r"heavy|chalk|true-edge|true-prob|any-positive-edge|props-over-minus|implied-under80|short-fav"),
 ("H-002","alt-ladder-hit-rate-vs-implied","Escalera de líneas alternas: hit rate > implícita","market","multi",r"alt-line|alt-lines|hit-rate|hitrate|props-full-season|missing-teammates|favor-unders"),
]

# Overrides manuales cuando el regex se equivoca.
OVERRIDES = {
    "multi-h2h-trend-streaks": "H-009",
    "multi-halftime-lines-pre-analysis": "P-006",
    "multi-live-avoid-worse-than-close": "H-008",
    "wnba-alt-total-high-probability": "H-002",
    "soccer-attacker-over-1-5-shots": "H-062",
    "soccer-player-shots-over-1-5-volume-vs-leaky-defense": "H-062",
    "soccer-knockout-to-advance-over-moneyline": "H-062",
    "nfl-alt-prop-season-hit-rate-vs-implied": "H-002",
    "nfl-props-implied-under80-true-over83": "H-001",
    "heavy-favorites-less-mispriced-than-minus110": "H-003",
    "soccer-obscure-leagues-higher-units": "H-060",
}

def cluster_of(slug):
    import re
    if slug in OVERRIDES: return OVERRIDES[slug]
    for cid, *_, rx in CLUSTERS:
        if re.search(rx, slug): return cid
    return None
