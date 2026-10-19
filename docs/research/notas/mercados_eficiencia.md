# Efficiency of Sports Betting and Prediction Markets, and Extracting Fair Probabilities from Prices

Notes compiled 2026-10-18. Status flags used here:
- **[V]** means I read the claim in the primary source (full text or abstract) during this session.
- **[S]** means it comes from a search snippet or secondary summary only.
- **[K]** means it is standard reference knowledge that I did not re-verify this session. A stable URL or DOI is given, but the number should be checked before it is quoted.

---

## 1. Market efficiency theory and evidence (weak and semi-strong form)

### Takeaway
Major-market odds are very accurate forecasts. Closing consensus odds track realized frequencies almost exactly (R² ≈ 0.999 in Kaunitz et al.), and odds-implied probabilities match or beat statistical models and tipsters. Even so, they are not perfectly efficient. Documented, persistent deviations include the favourite-longshot bias in the 1X2 market, slow or outlier soft-book prices and bookmaker "shading" toward bettor biases. Exploiting these deviations is constrained in practice by margins and by account limiting.

### Cited Findings
**Levitt (2004)**
- Full reference: Steven D. Levitt, "Why are Gambling Markets Organised So Differently from Financial Markets?", *Economic Journal* 114(495), April 2004, pp. 223–246. [IDEAS/RePEc](https://ideas.repec.org/a/ecj/econjl/v114y2004i495p223-246.html); full text [PDF (Berkeley mirror)](https://www.stat.berkeley.edu/users/aldous/157/Papers/Levitt_Gambling_2004.pdf). [S]
- How prices work: bookmakers post a price and adjust it only rarely and by small amounts. They do not act as balancing market makers. Instead they take large positions and deliberately deviate from the market-clearing price to exploit bettor biases, which raises their profits. Bookmakers forecast better than bettors. [IDEAS abstract](https://ideas.repec.org/a/ecj/econjl/v114y2004i495p223-246.html) [S]
- Data: an online-bookmaker NFL contest in the 2001–02 season, with 285 entrants making 19,770 bets on 242 games. Because it is a contest, these bettors may not represent ordinary bettors. [AcaWiki summary](https://acawiki.org/Why_are_Gambling_Markets_Organised_So_Differently_from_Financial_Markets%3F) [S]
- The NBER working-paper version finds "little evidence that bettors can systematically beat the bookmaker, even given the distorted prices." [NBER w9422, "How Do Markets Function? An Empirical Analysis of Gambling on the NFL"](https://www.nber.org/papers/w9422) [S]
- [K] The commonly cited mechanism is that bettors over-back favourites and home teams, so books shade those lines and home underdogs cover slightly more than 50%. I did not extract the paper's exact figure this session, so check it in the PDF.

**Classic NFL point-spread efficiency** [K]
- Stern, H. (1991). "On the Probability of Winning a Football Game." *The American Statistician* 45(3), 179–183. [doi:10.1080/00031305.1991.10475798](https://doi.org/10.1080/00031305.1991.10475798)
  - Final NFL margins relative to the point spread are approximately Normal(0, σ≈13.86) for 1981–84 games.
  - This gives a formula for converting a spread into a win probability: P(favourite wins) = Φ(spread/σ).
  - The spread is an approximately unbiased estimate of the margin.
- Gandar, J., Zuber, R., O'Brien, T., Russo, B. (1988). "Testing Rationality in the Point Spread Betting Market." *Journal of Finance* 43(4), 995–1008. [doi:10.1111/j.1540-6261.1988.tb02617.x](https://doi.org/10.1111/j.1540-6261.1988.tb02617.x)
  - Finds that NFL closing spreads pass standard statistical tests of rationality.
  - Some behavioural (economic) betting-rule tests suggest residual inefficiency.
  - Line movements from open to close improve accuracy.

**Kaunitz, Zhong & Kreiner (2017), soccer** [V]
- Full reference: "Beating the bookies with their own numbers – and how the online sports betting market is rigged." [arXiv:1710.02824](https://arxiv.org/abs/1710.02824); code at [github.com/Lisandro79/BeatTheBookie](https://github.com/Lisandro79/BeatTheBookie).
- Data: closing odds from 32 bookmakers (including Pinnacle, bet365 and William Hill) for football matches, January 2005 to June 2015. [arXiv PDF](https://arxiv.org/pdf/1710.02824) [V]
- Consensus probability: p_cons = 1/mean(Ω), where Ω is the set of odds across bookmakers.
- Regressing outcomes on p_cons gives R² = 0.999 for home wins, and a near-perfect fit for draws and away wins. True probability ≈ p_cons − α, with α = 0.034 (home), 0.057 (draw) and 0.037 (away). [V]
- Bet rule: bet when the odds ω satisfy ω > 1/(p_cons − α), using α = 0.05. Expected return E(Π) ≈ (p_cons − α)·ω − 1. [V]
- Results [V]:

  | Test | Bets | Accuracy | Return | Profit at $50 per bet |
  |---|---|---|---|---|
  | 10-year closing-odds backtest | 56,435 | 44.4% | +3.5% | $98,865 (10.8 SD above a random-bet bootstrap) |
  | Minute-level backtest (6 months) | 6,994 | 47.6% | +9.9% | — |
  | Paper trading (3 months) | 407 | 44.4% | +5.5% | $1,128.50 |
  | Real money (5 months) | 265 | about 47% | +8.5% | $957.50 |
  | Paper + real combined | 672 | — | +6.2% | $2,086 |

- Account limiting: "A few months after we began placing bets with real money bookmakers limited our accounts, which forced us to stop." Stakes were capped below $50 and bookmakers required manual approval of bets. [arXiv PDF](https://arxiv.org/pdf/1710.02824) [V]
- Press coverage: [MIT Technology Review, 2017-10-19](https://www.technologyreview.com/2017/10/19/67760/the-secret-betting-strategy-that-beats-online-bookmakers/) [S]
- Reading of the result: the consensus is near-efficient, but individual soft books post stale or outlier odds. An edge exists against those books, not against the consensus or sharp price.

**Štrumbelj (2014)**
- Full reference: E. Štrumbelj, "On determining probability forecasts from betting odds," *International Journal of Forecasting* 30(4), 934–943. [doi:10.1016/j.ijforecast.2014.02.008](https://doi.org/10.1016/j.ijforecast.2014.02.008)
- Odds-implied probabilities are strong forecasts and match or beat models and tipsters. [Secondary description, arXiv:1802.08848](https://arxiv.org/pdf/1802.08848) [S]
- Shin-method probabilities improve on basic normalisation, as measured by the Ranked Probability Score (RPS). [Springer 2022 paper citing Štrumbelj](https://link.springer.com/article/10.1007/s10479-022-04722-3) [S]
- Štrumbelj's Shin variant is solved numerically. [arXiv:2604.17194](https://arxiv.org/pdf/2604.17194) [S]

**European football efficiency: Angelini & De Angelis; Winkelmann et al.**
- Angelini, G. & De Angelis, L. (2019). "Efficiency of online football betting markets." *International Journal of Forecasting* 35(2), 712–721. [doi:10.1016/j.ijforecast.2018.07.008](https://doi.org/10.1016/j.ijforecast.2018.07.008)
- The study covers 41 bookmakers and 11 European leagues. Taking the best available odds across bookmakers, 8 of the 11 markets are efficient and 3 show exploitable inefficiencies. [Univ. Venice record](https://iris.unive.it/handle/10278/3708322) [S]
- Hegarty & Whelan (below) cite this paper as confirming 1X2 inefficiencies. [S]
- Winkelmann, D., Deutscher, C., Ötting, M. (2021). "Bookmakers' mispricing of the disappeared home advantage in the German Bundesliga after the COVID-19 break." *Applied Economics* 53(26). [doi:10.1080/00036846.2021.1873234](https://doi.org/10.1080/00036846.2021.1873234) [K]
  - Odds were slow to adjust to the loss of home advantage in empty stadiums.
  - The gap created a temporary profitable inefficiency that disappeared as bookmakers learned.
- Other studies:
  - A 2009 *Journal of Forecasting* study finds predictable patterns and profits that are not fully consistent with weak-form efficiency. [Southampton eprint](https://eprints.soton.ac.uk/373110/1/football_20efficiency_20full_20060115.pdf) [S]
  - [UEA: "How efficient is the European football betting market?"](https://research-portal.uea.ac.uk/en/publications/how-efficient-is-the-european-football-betting-market-evidence-fr/) [S]

**Wunderlich & Memmert** [K]
- Wunderlich, F. & Memmert, D. (2018). "The Betting Odds Rating System: Using soccer forecasts to forecast soccer." *PLOS ONE* 13(6): e0198668. [doi:10.1371/journal.pone.0198668](https://doi.org/10.1371/journal.pone.0198668)
  - Ratings derived from odds outperform Elo-type ratings.
- Wunderlich, F. & Memmert, D. (2020). "Are betting returns a useful measure of accuracy in (sports) forecasting?" *International Journal of Forecasting* 36(2), 713–722. [doi:10.1016/j.ijforecast.2019.08.009](https://doi.org/10.1016/j.ijforecast.2019.08.009)
  - Betting returns are a noisy and potentially misleading accuracy metric.
  - Use proper scoring rules (RPS, log-loss, Brier) instead.
- Wunderlich, F. & Memmert, D. (2021). "Forecasting the outcomes of sports events: A review." *European Journal of Sport Science* 21(7), 944–957. [doi:10.1080/17461391.2020.1793002](https://doi.org/10.1080/17461391.2020.1793002)
  - Betting odds are a robust, hard-to-beat benchmark.
- Wunderlich, Caparrós & Memmert, "Does the consideration of market prices in model selection increase model profitability?" Listed as forthcoming in *IJF* (2026); presented at a seminar on 2026-10-06. Seminar text: "the high accuracy of betting odds is a robust empirical result in the literature." [UniBS seminar listing](https://www.unibs.it/en/node/14503) [S]

### Inferences
- Weak-form efficiency approximately holds for consensus or sharp closing prices in major soccer and NFL markets.
- Rejections come from three sources: (a) the favourite-longshot bias in 1X2, (b) individual soft-book prices that deviate from the consensus, and (c) structural breaks the market prices slowly, such as COVID-era home advantage.
- In practice, a model's edge should be measured against the de-vigged sharp or consensus closing price using a proper scoring rule, not by backtested ROI.

### Gaps
- I did not extract Levitt's exact home-underdog cover rates or Gandar's exact test statistics this session. Check them in the PDFs.
- I found no CFB-specific efficiency paper in this pass. CFB is generally believed to be less efficient than the NFL in lower-tier games, but I have no citation for that.

---

## 2. Favourite-longshot bias (FLB): evidence and explanations

### Takeaway
FLB is large in horse racing and present in soccer 1X2 fixed-odds markets. It is absent in competitive or low-margin markets such as Asian handicaps and, roughly, NFL spreads. It also appears in Kalshi prediction markets. Competing explanations:
- Risk-loving bettors.
- Probability misperception: overweighting small probabilities.
- Shin's insider-trading model: bookmakers widen longshot prices to protect against informed bettors.
- Bookmaker market power or risk aversion (Hegarty & Whelan).

### Cited Findings
**Soccer: Hegarty & Whelan, "Forecasting Soccer Matches with Betting Odds: A Tale of Two Markets"** [S]
- Versions: CEPR DP17949 (2023); UCD WP2023/05; *International Journal of Forecasting*, 2025 per the author's site.
- Finding: the 1X2 market shows FLB, but the Asian handicap market for the same matches does not and gives efficient forecasts. [CEPR DP17949](https://cepr.org/publications/dp17949); [author page](https://www.karlwhelan.com/?p=2367); [MPRA 116925](https://mpra.ub.uni-muenchen.de/116925/)
- Their explanation: pricing depends on market competitiveness. Asian handicap markets carry lower margins. [karlwhelan.com](https://karlwhelan.com/sports-betting-asian-handicap-vs-1x2/) [S]
- Related papers:
  - Whelan's monopoly model: monopolistic bookmakers produce FLB and competitive markets do not. Tested on more than 80,000 European games in two markets. [MPRA 117243](https://mpra.ub.uni-muenchen.de/117243/1/Monopoly.pdf) [S]
  - Whelan's risk-aversion paper: FLB arises from bookmaker risk aversion even in competitive markets. Uses 84,230 European matches from 2011/12 to 2021/22 with average closing odds from Buchdahl's football-data. [MPRA 116923](https://mpra.ub.uni-muenchen.de/116923/1/MPRA_paper_116923.pdf); [UCD WP23/16](https://www.ucd.ie/economics/t4media/WP23_16.pdf) [S]

**Horse racing and explanations** [K]
- Snowberg, E. & Wolfers, J. (2010). "Explaining the Favorite–Long Shot Bias: Is it Risk-Love or Misperceptions?" *Journal of Political Economy* 118(4), 723–746. [doi:10.1086/655844](https://doi.org/10.1086/655844)
  - Uses US horse racing data, including exotic bets, to separate the two explanations.
  - The data favour misperceptions (probability weighting à la prospect theory) over risk-love.
- Shin, H. S. (1991). "Optimal Betting Odds Against Insider Traders." *Economic Journal* 101(408), 1179–1185. [doi:10.2307/2234434](https://doi.org/10.2307/2234434)
- Shin, H. S. (1992). "Prices of State Contingent Claims with Insider Traders, and the Favourite-Longshot Bias." *Economic Journal* 102(411), 426–435. [doi:10.2307/2234526](https://doi.org/10.2307/2234526)
- Shin, H. S. (1993). "Measuring the Incidence of Insider Trading in a Market for State-Contingent Claims." *Economic Journal* 103(420), 1141–1153. [doi:10.2307/2234240](https://doi.org/10.2307/2234240)
  - Model: a fraction z of bettors know the outcome. The bookmaker protects itself by setting longshot odds proportionally shorter, which produces FLB endogenously.
  - Shin's UK racing estimate: z ≈ 2%.

**Prediction markets**
- FLB on Kalshi: see section 5. [Bürgi, Deng & Whelan](https://www.karlwhelan.com/Papers/Kalshi.pdf) [V]
- InTrade: Page & Clemen (2013) found longshots too expensive, but only for contracts far from expiry, attributed to time discounting. Near close they found no significant deviation. Cited in [Bürgi et al.](https://www.karlwhelan.com/Papers/Kalshi.pdf) [V, as cited]
- "Yogi Berra bias": in sports contracts, the price of the losing team in the last 15 minutes was too high (Page 2012). Cited in [Bürgi et al.](https://www.karlwhelan.com/Papers/Kalshi.pdf) [V, as cited]
- The Iowa Electronic Markets showed no FLB (Berg & Rietz 2019). Cited in [Bürgi et al.](https://www.karlwhelan.com/Papers/Kalshi.pdf) [V, as cited]

**Other**
- Data Golf argues that FLB in golf odds is "not a bias" in the usual sense: it reflects how margin is distributed. [Data Golf](https://datagolf.com/fav-longshot-not-a-bias) [S]
- [K] In NFL spreads, FLB is generally weak or absent because spread betting equalises the two sides near 50/50. The moneyline market can show mild FLB. I did not verify a specific citation for NFL moneyline FLB this session.

### Inferences
- For soccer, use Asian handicap or sharp-book prices to derive "true" probabilities. Prefer them to soft 1X2 prices.
- If you must use 1X2 prices, use a de-vig method that allocates more margin to longshots, such as Shin, power or odds-ratio, not multiplicative.

### Gaps
- I found no recent NFL-specific or CFB-specific FLB estimate with verified numbers.

---

## 3. Removing the vig/overround: methods, formulas, accuracy

### Takeaway
Multiplicative normalisation is the simplest method but spreads margin proportionally, so it ignores FLB. Methods that put more margin on longshots (Shin, power/"logarithmic", odds-ratio) are more accurate in 1X2 and many-outcome markets:
- Clarke, Kovalchik & Ingram (2017) found the power method beats multiplicative everywhere and matches or beats Shin.
- Štrumbelj (2014) found Shin beats basic normalisation.
- In 2-way markets the methods differ little. Shin is identical to additive with 2 outcomes.

### Cited Findings
**Notation:** decimal odds o_i, raw implied π_i = 1/o_i, booksum B = Σπ_i, margin M = B − 1, n = number of outcomes, fair probability p_i.

1. **Multiplicative (basic normalisation):** p_i = π_i / B. This is the most common method. It does not allow for FLB, and run in reverse it can give bookmaker probabilities above 1. [implied vignette](https://rdrr.io/cran/implied/f/vignettes/introduction.Rmd) [S]; [Clarke et al. 2017](https://www.sciencepublishinggroup.com/article/10.11648/j.ajss.20170506.12) [V-abstract]
2. **Additive:** p_i = π_i − (B − 1)/n. Equal margin per outcome. It can produce negative probabilities for big longshots. [implied vignette](https://rdrr.io/cran/implied/f/vignettes/introduction.Rmd) [S]
3. **Margin weights proportional to odds (Buchdahl "wpo"):** M_i = M·π_i^−1/n… (the printed formula is garbled). Buchdahl's original definition is p_i = (n − M·o_i)/(n·o_i). Source: Buchdahl, "Wisdom of the Crowd," football-data.co.uk. [implied vignette](https://rdrr.io/cran/implied/f/vignettes/introduction.Rmd) [S]
4. **Shin (1992/1993):** solve for the insider share z ∈ [0,1) such that Σp_i = 1, where

   p_i(z) = [ √( z² + 4(1−z)·π_i²/B ) − z ] / [ 2(1−z) ]

   - [K] This is the Jullien–Salanié (1994) / Štrumbelj (2014) closed form for given z. It is solved by root-finding or fixed-point iteration, with z₀ = 0, alternating z = (Σ√(z²+4(1−z)π_i²/B) − 2) / (n − 2) for n > 2.
   - Implementations: Python [`shin` (mberk)](https://www.github.com/mberk/shin) and [PyPI](https://pypi.org/project/shin); R [`implied`](https://rdrr.io/cran/implied/f/vignettes/introduction.Rmd) [S]
   - **2-way case:** the Shin and additive methods are equivalent for two-competitor events. [Clarke et al. 2017](https://www.sciencepublishinggroup.com/article/10.11648/j.ajss.20170506.12) [V-abstract]
   - So for a moneyline or totals pair: p_1 = π_1 − (B−1)/2.
5. **Power (Vovk & Zhdanov 2009; Clarke 2016):** p_i = π_i^k, with k solved so that Σπ_i^k = 1 (k > 1 when B > 1).
   - The `implied` package writes it as p_i = π_i^(1/k).
   - Buchdahl calls this the "logarithmic" method.
   - It never produces probabilities outside [0,1] and builds in FLB. [Clarke et al. 2017](https://www.sciencepublishinggroup.com/article/10.11648/j.ajss.20170506.12) [V-abstract]; [implied vignette](https://rdrr.io/cran/implied/f/vignettes/introduction.Rmd) [S]
6. **Odds-ratio (Cheung 2015):** assume a constant odds ratio c between bookmaker and fair odds: c = [π_i(1−p_i)] / [p_i(1−π_i)]. Then p_i = π_i / (c + π_i − c·π_i), with c solved so that Σp_i = 1. References: Cheung, K. (2015), "Fixed-odds betting and traditional odds"; Buchdahl, "Wisdom of the Crowd." [implied vignette](https://rdrr.io/cran/implied/f/vignettes/introduction.Rmd) [S]
7. **Balanced book and Jensen–Shannon distance (jsd):** further variants in `implied`. JSD (C. D. Long) solves for a constant JS distance between p and π. [implied vignette](https://rdrr.io/cran/implied/f/vignettes/introduction.Rmd) [S]

**Accuracy comparisons**
- Clarke, S., Kovalchik, S., Ingram, M. (2017). "Adjusting bookmaker's odds to allow for overround." *American Journal of Sports Science* 5(6), 45–49. [doi:10.11648/j.ajss.20170506.12](https://www.sciencepublishinggroup.com/article/10.11648/j.ajss.20170506.12)
  - Uses three large bookmaker datasets from different sports.
  - The power method "universally outperforms the multiplicative method" and outperforms or is comparable to Shin. [V-abstract]
- Štrumbelj (2014): Shin beats basic normalisation on RPS. [S, via secondary sources above]
- Buchdahl (football-data "Wisdom of the Crowd" and Pinnacle articles): [K] finds that the odds-ratio and logarithmic/power methods best fit the observed FLB in soccer 1X2, with multiplicative worst. I did not retrieve his text this session.
- 2026 critique: [arXiv:2604.17194](https://arxiv.org/pdf/2604.17194) [S]
  - Argues the power method wrongly assumes a power law with no intercept.
  - In its data, the estimated intercept was below 1 for all bookmakers.

**Implementation recipes** [K, derived from formulas above]
- **2-way** (moneyline, spread, totals):
  - Multiplicative: p₁ = π₁/(π₁+π₂).
  - Additive/Shin: p₁ = π₁ − (B−1)/2.
  - Power: solve π₁^k + π₂^k = 1 by bisection on k ∈ [1, 10].
  - Odds-ratio: solve for c by bisection.
  - At Pinnacle-level margins (about 2–3%) the methods differ by under about 0.5–1 pp, except at heavy favourites.
- **3-way** (1X2): use Shin, power or odds-ratio via one-dimensional root-finding. The draw gets an intermediate share of margin.
- American odds: o = 1 + A/100 if A > 0, and o = 1 + 100/|A| if A < 0. For Kalshi or Polymarket, the price in $ is π directly. Fees should be added to the effective cost.

### Inferences
- Default choice for 1X2 and futures: power or Shin. For 2-way NFL or CFB markets at sharp books, multiplicative is close enough, but power or Shin is still preferable for heavy favourites.
- Evaluate the choice with the log-loss of de-vigged closing probabilities on your own historical data.

### Gaps
- I could not retrieve Buchdahl's original ranking text. The claim that odds-ratio or log is best "per Buchdahl" is [K] and needs verification.
- I did not get Clarke et al.'s numeric loss metrics. The abstract gives only qualitative results.

---

## 4. Sharp vs soft books; closing line as the "true probability" benchmark

### Takeaway
Sharp market makers take large limits, run low margins and move lines on informed money:
- Pinnacle and Circa, plus Asian books such as SBOBET and Singbet, and betting exchanges.
- Their closing prices are the standard estimate of "true" probability.

Soft or retail books copy sharp lines, run higher margins, and manage risk by limiting winning customers rather than by moving prices (Levitt 2004; Kaunitz et al. 2017). Efficiency falls with liquidity, so lower leagues, props and derivatives are less efficient.

### Cited Findings
- Bookmakers post and hold prices and take positions. They are not balancing market makers. [Levitt 2004](https://ideas.repec.org/a/ecj/econjl/v114y2004i495p223-246.html) [S]
- Soft books limit winners instead of correcting prices. Kaunitz et al. had stakes capped and accounts restricted within months. [arXiv:1710.02824](https://arxiv.org/pdf/1710.02824) [V]
- Margin falls as kickoff nears. One worked example shows Pinnacle's overround moving from about 6.8% at open to about 2.6% at kickoff. [oddspapi blog](https://oddspapi.io/blog/?p=3056) [S, vendor]
- Accuracy rises toward close:
  - Kalshi prices "become more accurate as markets approach closing." [Bürgi et al.](https://www.karlwhelan.com/Papers/Kalshi.pdf) [V]
  - Gandar et al. (1988) find that open-to-close NFL line moves improve accuracy. [doi](https://doi.org/10.1111/j.1540-6261.1988.tb02617.x) [K]
- The consensus of closing odds across 32 books is calibrated to R² ≈ 0.999. [Kaunitz et al.](https://arxiv.org/pdf/1710.02824) [V]
- Data Golf replicated Buchdahl's method of using one book's odds to bet into others. Blind returns at each book are near zero, and the sharpness ranking differs by book. [Data Golf "How sharp are bookmakers"](https://datagolf.com/how-sharp-are-bookmakers) [S]
- Several practitioner sites call Pinnacle's de-vigged closing line the "best estimate of true probability." One claims "Journal of Sports Sciences research" supports this without citing it, so treat that as unverified. [thespread.com](https://www.thespread.com/?p=550721) [S, low quality]
- Liquidity and efficiency on Kalshi: the authors regress FLB by trading-volume quintile, and the lowest-volume quintile shows the bias most clearly. [Bürgi et al., Table 6](https://www.karlwhelan.com/Papers/Kalshi.pdf) [V]
- [K] Buchdahl's Pinnacle articles (pinnacle.com/betting-resources) report that beating the closing price ("closing line value", CLV) predicts long-run profitability. They also find Pinnacle closing odds well calibrated in major soccer leagues, with somewhat larger noise in lower leagues. I did not fetch these this session.

### Inferences
- Benchmark hierarchy for "fair" probability:
  1. Pinnacle, Circa or exchange de-vigged closing price.
  2. The consensus of many books.
  3. The opening price.
  4. A single soft book.
- CLV against Pinnacle close is the most statistically efficient performance signal. It needs far fewer bets than ROI to reach significance.
- Expect larger exploitable errors in CFB lower-tier games, soccer lower divisions, player props and derivative markets (halves, quarters, team totals). The basis is the Kalshi volume finding and the general liquidity logic, not a dedicated study.

### Gaps
- I found no peer-reviewed study this session that quantifies closing-line efficiency by league tier or for props versus mains with verified numbers. Buchdahl's *Squares & Sharps* (2016) and his Pinnacle articles are the likely sources but were not retrieved.

---

## 5. Prediction markets: theory and Kalshi/Polymarket sports evidence (as of Oct 2026)

### Takeaway
Under log utility, a prediction-market price approximates the mean belief (Wolfers & Zitzewitz). Manski shows that in general the price only bounds the mean belief.

Empirically, Kalshi prices are informative and sharpen toward close but show a clear FLB:
- Contracts under 10¢ lose more than 60%.
- Contracts above 50–70¢ earn small positive returns.
- Makers do far better than takers.

The first sports-specific Kalshi study (2026) finds good mid-game calibration in NBA, MLB and NHL. Calibration distorts in the final 10 minutes and before tip-off, and parlays are overpriced by about 3% per leg. Head-to-head accuracy against sportsbooks looks roughly at parity, but the evidence is mostly non-peer-reviewed.

### Cited Findings
**Theory**
- Wolfers, J. & Zitzewitz, E. (2004). "Prediction Markets." *Journal of Economic Perspectives* 18(2), 107–126. [doi:10.1257/0895330041371321](https://doi.org/10.1257/0895330041371321) [K]
- Wolfers, J. & Zitzewitz, E. (2006). "Interpreting Prediction Market Prices as Probabilities." NBER WP 12200. [nber.org/papers/w12200](https://www.nber.org/papers/w12200) [K]
  - If traders have log utility, the equilibrium price equals the mean belief.
  - Under other risk preferences the deviation is usually small.
- Manski, C. F. (2006). "Interpreting the predictions of prediction markets." *Economics Letters* 91(3), 425–429. [doi:10.1016/j.econlet.2006.01.004](https://doi.org/10.1016/j.econlet.2006.01.004)
  - Assumes risk-neutral traders who invest all their wealth.
  - A price p implies the mean belief lies in [p², 2p − p²]. As summarised in [Bürgi et al.](https://www.karlwhelan.com/Papers/Kalshi.pdf) [V]
  - Gjerstad (2004) and Wolfers–Zitzewitz (2006) show that with log utility, price ≈ mean belief. [same source, V]

**Kalshi: Bürgi, Deng & Whelan, "Makers and Takers: The Economics of the Kalshi Prediction Market"** [V]
- Versions: UCD WP2025/19; dated January 2026 in the PDF; also CESifo 2026 and GWU 2026-001. [PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf); [UCD WP](https://www.ucd.ie/economics/t4media/WP2025_19.pdf); [VoxEU column](https://cepr.org/voxeu/columns/economics-kalshi-prediction-market); [CESifo](https://www.ifo.de/en/cesifo/publications/2026/working-paper/makers-and-takers-economics-kalshi-prediction-market)
- Data:
  - 46,282 contracts from 12,403 events, covering 2021 to April 2025.
  - Contracts were open at least 24 hours and had at least $1,000 volume.
  - 313,972 Yes/No prices, taken at close and at daily intervals up to 10 days before close.
  - Sports trading only began in January 2025, and results are robust to excluding sports.
- Kalshi taker fee during the sample: $0.07·P·(1−P) per contract, rounded up to the cent.
  - About 1.77% of cost at 50¢ when buying 100 contracts.
  - Kalshi began charging makers after April 2025.
- Results:
  - Contracts at 10¢ and under lose more than 60% on average.
  - Above 50¢ returns are small and positive; above 70¢ they are statistically significant.
  - The average pre-fee return is −20% (mostly from losses on cheap contracts).
  - Maker average return is −9.64% versus −31.46% for takers. Makers buying at 50¢ or more earn +2.6%.
  - FLB holds across categories but weakens in 2025 data, where the coefficient is smaller and less significant.
  - FLB is strongest in the lowest-volume quintile.
- Model: modest disagreement among traders plus small overweighting of low probabilities reproduces the patterns.

**Kalshi sports: Moshrefi, "Prices, Probabilities, and Parlays: Systematic Bias in Sports Prediction Markets"** [V]
- Princeton; [arXiv:2607.14430](https://arxiv.org/html/2607.14430v1), submitted 2026-07-15.
- Data: about 23 million executed Kalshi moneyline trades (NBA 13.0M, MLB 7.1M, NHL 2.8M), early March to mid-May 2026.
- Calibration by time to expiry:
  - Miscalibration is U-shaped: largest just after listing and in the final minutes.
  - Trades roughly 30–240 minutes before close are near-perfectly calibrated.
  - In the final 0–10 minutes the power-law exponent γ̂ is 1.27–1.31, and the Platt slope is 1.62 (NBA), 2.05 (MLB) and about 4.56 (NHL). The curve becomes step-like with Prelec α > 1, the opposite of lottery-style probability weighting.
- Parlays:
  - Median ratio of executed parlay price to the product of leg prices is 0.991 for 2 legs, rising to 1.305 for 11 legs. About +3% markup per added leg (R² ≈ 0.94).
  - Parlays priced near 30¢ win about 24% of the time; near 40¢, about 30%.
- No direct comparison with sportsbooks.

**Kalshi's own research** [S, company-sponsored]
- Reports that 10¢ and cheaper contracts win less often than their price implies. [Crypto Briefing](https://cryptobriefing.com/kalshi-prediction-markets-reliability-study/)

**Polymarket vs sportsbooks** (non-peer-reviewed analytics)
- NBA 2024–25: 1,000 games comparing OddsPortal and Polymarket. Both picked about 66% of winners correctly, with no significant accuracy difference. [Polymarket Analytics](https://polymarketanalytics.com/research/nba-sportsbooks-vs-prediction-markets) [S]
- Cross-category, January 2024 to May 2026, 28,407 resolved markets:
  - Calibration error is about 2.1 pts for Polymarket versus about 6.4% for sportsbook lines.
  - Sports are slightly overconfident on favourites.
  - Vig over 1,840 NBA and soccer markets: about 4.4% at sportsbooks versus about 1.5% in Polymarket taker fees.
  - Source: [Poly Syncer](https://www.polysyncer.com/blog/polymarket-prediction-accuracy) [S, vendor, methods unclear]
- About 1,100 Polymarket sports trades (2026) suggest DraftKings and FanDuel are better calibrated, with much deeper handle per game. [ZenHodl](https://zenhodl.net/blog/state-of-prediction-markets-2026) [S, vendor, rough estimates]

### Inferences
- Treat Kalshi and Polymarket mid-prices (not last trades) as roughly calibrated probabilities in liquid pre-game and in-play windows.
- Apply an FLB correction to cheap contracts (under about 15¢), especially in thin markets. A Shin- or power-style shrink toward 0 works.
- Avoid relying on the final-minutes prices, which are distorted.
- Edges are most plausible for longshot "No" (makers) and in low-volume derivatives.
- The fee formula 0.07·P(1−P) must be in any EV calculation.

### Gaps
- I found no peer-reviewed, sports-specific study of Kalshi or Polymarket NFL, CFB or soccer calibration as of October 2026. Moshrefi covers NBA, MLB and NHL only. Bürgi et al. ends before most sports volume.
- The Polymarket-vs-sportsbook accuracy comparisons are vendor analyses with unclear methods and conflicting conclusions.
- Post-2025 Kalshi maker-fee details and current sports fee schedules were not verified from official Kalshi docs this session.
- I saw but did not read an arXiv paper, "The profit-bias identity in sports betting" ([arXiv:2609.06739](https://arxiv.org/pdf/2609.06739)), that may be relevant.
