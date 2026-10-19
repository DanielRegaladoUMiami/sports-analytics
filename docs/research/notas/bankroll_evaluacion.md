# Bankroll Management and Statistical Evaluation of Betting Models/Bettors

Source key used throughout:
- **[fetched]**: the source was retrieved or searched during this session and the claim was checked against it.
- **[ref, not fetched]**: a standard academic reference given from bibliographic knowledge. The full text was NOT retrieved this session, so check the exact equation or page before quoting it in a paper.
- **[derived]**: algebra or simulation done for these notes, with the code below. These are not claims from any source.

Numerical examples were computed with a short Python script: `/private/tmp/claude-502/-Users-danielregalado/8cbba81f-c945-4239-8c5e-dea312ee3b44/scratchpad/calc.py`. It uses a seeded simulation with 2,000 paths × 5,000 bets.

Notation:
- Decimal odds `o`. Net odds `b = o − 1`.
- Model win probability `p`, with `q = 1 − p`.
- Fraction of bankroll staked `f`.
- Prediction-market contract price `c ∈ (0,1)`, which pays $1 if YES.

---

## 1. Kelly criterion: derivation, binary/decimal/prediction-market formulas, growth & drawdown, fractional Kelly, parameter uncertainty, simultaneous/correlated bets, market-relative edge

### Takeaway
Kelly is the stake that maximizes E[log wealth]. For a single binary bet it is `f* = (bp − q)/b = edge/odds`. For a $1-payout contract bought at all-in price `c'` (price plus fee) it is `f* = (p − c')/(1 − c')`.

Full Kelly is very volatile, and anything above 2× Kelly has negative growth. Errors in the estimate of `p` dominate everything else. Practitioners and the literature (MacLean–Thorp–Ziemba; Baker & McHale) therefore shrink stakes: fractional Kelly at ¼–½ is the norm. Simultaneous or mutually exclusive bets need a joint optimization (Kelly 1956 for horse races; Whitrow 2007), not independent single-bet Kellys.

### Cited Findings

**Core derivation and formulas**

- **Original source.** Kelly, J. L. (1956). "A New Interpretation of Information Rate." *Bell System Technical Journal* 35(4): 917–926. https://doi.org/10.1002/j.1538-7305.1956.tb03809.x [ref, not fetched]. Kelly shows that a gambler with a private "information channel" maximizes the exponential growth rate of capital by maximizing the expected log. For a parimutuel race with mutually exclusive outcomes he gives the allocation algorithm described below.

- **Derivation** [derived; standard, see Thorp 2006 below]. Wealth after one bet is `W·(1 + b f)` with probability `p` and `W·(1 − f)` with probability `q`. The growth rate per bet is
  `G(f) = p·ln(1 + b f) + q·ln(1 − f)`.
  Setting `G'(f) = pb/(1+bf) − q/(1−f) = 0` gives
  **`f* = (b p − q)/b = p − q/b`**.
  In decimal odds: `f* = (p·o − 1)/(o − 1)`. The numerator is the expected value per unit staked (the "edge") and the denominator is the net odds. Hence the phrase "Kelly = edge / odds".

- **MacLean, Thorp & Ziemba** state that "in the one asset two valued payoff case, the optimal Kelly wager is the edge (expected return) divided by the odds." — [MacLean, Thorp & Ziemba, "Good and bad properties of the Kelly criterion" (2010)](https://www.stat.berkeley.edu/~aldous/157/Papers/Good_Bad_Kelly.pdf) [fetched]

- **Reference treatment.** Thorp, E. O. (2006). "The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market." In Zenios & Ziemba (eds.), *Handbook of Asset and Liability Management*, Vol. 1, Elsevier, pp. 385–428 [ref, not fetched]. It contains:
  - the even-money case `f* = p − q`;
  - the continuous approximation `f* ≈ μ/σ²` with growth `g* ≈ μ²/(2σ²)`;
  - the fractional-Kelly growth trade-off `g(k·f*) ≈ g*·(2k − k²)`;
  - drawdown results such as P(wealth ever falls to fraction x) = `x^(2/k − 1)` for fractional Kelly `k` in continuous time. That gives x for full Kelly and x³ for half Kelly, so P(ever halving) is 50% at full Kelly and 12.5% at half Kelly.
  - **Verify these closed forms against the chapter before citing them in a paper.**

**NFL −110 worked example** [derived]

| Quantity | Formula | Value |
|---|---|---|
| Net odds | `b = 100/110` | 0.9091 |
| Break-even win rate | `1/(1+b) = 110/210` | 52.381% |
| EV per unit at p = 0.53 | `pb − q` | +1.18% ROI |
| Kelly stake | `f* = 0.01182/0.9091` | 1.30% of bankroll |
| Growth per bet, full Kelly | `G(f*)` | 7.69×10⁻⁵ log-units |
| Growth per bet, half Kelly | `G(f*/2)` | 75.0% of full-Kelly growth |

The half-Kelly row matches the `2k − k²` rule.

**Kalshi / prediction-market contracts** [derived]

- **Without fees.** Buying YES at price `c` gives net odds `b = (1 − c)/c`. Substituting:
  **`f* = (p − c)/(1 − c)`**, as a fraction of bankroll spent on contracts.
  - This form matches practitioner write-ups: [polymarket-bot docs](https://mintlify.com/joicodev/polymarket-bot/risk/kelly-criterion) and [SimpleFunctions](https://simplefunctions.dev/learn/position-sizing) [fetched via search snippets].
  - Academic treatment: [Application of the Kelly Criterion to Prediction Markets, arXiv:2412.14144](https://arxiv.org/abs/2412.14144) [fetched via search snippet]. It explicitly sets fees aside.
  - Buying NO is symmetric: replace `p → 1 − p` and `c → c_NO` (≈ 1 − c_YES_bid).

- **With fees.** Let `φ(c)` be the fee per contract, paid at purchase, with nothing charged at settlement. The all-in cost is `c' = c + φ(c)`. Each winning contract still pays $1, so `b = (1 − c')/c'` and
  **`f* = (p − c')/(1 − c')`**, where `f` = fraction of bankroll spent including fees.
  - Equivalent edge condition: bet only if `p > c + φ(c)`.

- **Kalshi taker fee formula** (secondary sources): `fee = ceil_to_cent(0.07 × C × P × (1 − P))`, where `C` is the number of contracts and `P` is the price in dollars.
  - Example: 100 contracts at $0.55 → $1.74.
  - Makers reportedly pay nothing on most markets, and some products, including sports, reportedly have different rates.
  - Sources: [SailGP Kalshi fees page](https://sailgp.com/prediction-markets/kalshi/fees), [Allium blog](https://allium.so/blog/kalshi-fees-why-the-cost-peaks-near-50-cents/), [chudi.dev](https://chudi.dev/blog/kalshi-fees) [fetched via search snippets; Kalshi's official fee PDF was NOT retrieved].

- **Kalshi example** [derived]. p = 0.60, c = 0.50:
  - per-contract fee `φ = 0.07·0.25 = $0.0175`, so `c' = 0.5175`;
  - `f* = 0.0825/0.4825 = 17.1%`, versus 20.0% ignoring fees.
  - Because `φ ∝ c(1−c)`, fees hurt most near 50¢.
  - Rounding up to the cent is applied per order, which makes small orders relatively more expensive.

**Growth and drawdown properties** (MacLean, Thorp & Ziemba 2010, [PDF](https://www.stat.berkeley.edu/~aldous/157/Papers/Good_Bad_Kelly.pdf) [fetched])

- **Good properties:**
  - maximizing E log X asymptotically maximizes the rate of asset growth (Breiman 1961);
  - it minimizes the expected time to reach large goals;
  - it asymptotically maximizes median log wealth;
  - "the E log X bettor never risks ruin";
  - the policy is myopic, so it only needs current opportunities;
  - competitive optimality: E(X/X*) ≤ 1 for any other strategy X.
- **Bad property:** because log utility's Arrow-Pratt risk aversion is 1/w (≈ 0), "Kelly bets may be exceedingly large and risky for favorable bets" in the short term. A long sequence of bad outcomes can produce large losses "even if there are many independent investment opportunities."
- **Overbetting:** "the growth rate becomes zero plus the risk free rate when one bets exactly twice the Kelly wager … it never pays to bet more than the Kelly strategy because then risk increases … and growth decreases."
- **Blackjack illustration** (p = 0.51, f* = 0.02, Fig. 3 from MacLean & Ziemba 1999): the probability of doubling before halving rises steeply as you bet less than Kelly, while relative growth falls slowly near f*.
- **Fractional Kelly** is "simply a blend of Kelly and cash." For lognormal assets, power utility δw^δ (δ < 0) is equivalent to fraction α = 1/(1 − δ). So half Kelly ↔ δ = −1 and quarter Kelly ↔ δ = −3. This equivalence is NOT exact for discrete bets. For a coin toss the power-utility optimum is `f*_δ = (p^α − q^α)/(p^α + q^α)`, which is not α·f*.
- **Errors in inputs:** errors in means are about 20× as costly as errors in covariances, and about 10× as costly as errors in variances (Chopra & Ziemba 1993, Table 1). This is the main reason the mean estimate (the edge) dominates Kelly risk.

**Simulated drawdowns for NFL −110, p = 0.53, f* = 1.30%, 5,000 bets** [derived; seeded Monte Carlo, 2,000 paths]

| Kelly multiple | Median final bankroll | P(final < start) | Median max drawdown | P(max DD > 50%) |
|---|---|---|---|---|
| 1.0 (full) | 1.47× | 33.7% | 57.7% | 70.5% |
| 0.5 | 1.33× | 25.6% | 33.1% | 9.6% |
| 0.25 | 1.18× | 21.2% | 17.7% | 0.05% |

Even with a *known* true 53% edge, full Kelly has a ~1/3 chance of being behind after 5,000 bets (about 19 NFL seasons at 270 bets/season) and usually suffers a >50% peak-to-trough drawdown.

**Parameter uncertainty and shrinkage**

- **Baker, R. D. & McHale, I. G. (2013).** "Optimal Betting Under Parameter Uncertainty: Improving the Kelly Criterion." *Decision Analysis* 10(3): 189–199. https://doi.org/10.1287/deca.2013.0271 — [INFORMS](https://pubsonline.informs.org/doi/10.1287/deca.2013.0271), [Salford repository](https://salford-repository.worktribe.com/output/1410355/optimal-betting-under-parameter-uncertainty-improving-the-kelly-criterion), [RePEc](https://ideas.repec.org/a/inm/ordeca/v10y2013i3p189-199.html) [fetched via search abstract]
  - When `p` is estimated, the optimal stake is a *shrunken* Kelly stake `k·f̂*` with `k < 1`. Shrinking improves out-of-sample growth.
  - They compare several estimators of the shrinkage factor, give a "back-of-envelope" correction, and test on simulated data and tennis betting data.
  - They also extend the result to bet "shrinkage and swelling" under general risk-averse utilities.
- **Follow-up:** Metel (2017), "Kelly betting on horse races with uncertainty," arXiv:1701.02814 — [ar5iv](https://ar5iv.arxiv.org/html/1701.02814) [fetched via search snippet]. It extends the shrinkage idea to multi-outcome races.
- **Illustrative shrinkage factor** [derived; this is not B&M's exact formula]. Expected growth near f* is ≈ `g* − (σ²_R/2)(f − f*)²`. Minimizing `E[(k f̂ − f*)²]` for an unbiased estimate `f̂` with sampling variance `Var(f̂)` gives
  `k* = f*² / (f*² + Var(f̂))`.
  - In words: shrink by the "signal share" of the estimated stake. If the standard error of your edge equals the edge itself, `k ≈ ½`. This is a Bayesian-flavored justification for half-Kelly.
  - B&M also discuss shrinkage that depends on the distribution of `p̂`. A LessWrong discussion notes that their rule of thumb assumes a beta distribution ([LessWrong, "Never go full Kelly"](https://www.lesswrong.com/posts/TNWnK9g2EeRnQA8Dg/never-go-full-kelly), non-peer-reviewed).
- **Practitioner guidance:** prediction-market practitioners recommend 25–50% Kelly because overestimating the edge leads to overbetting — [NexusFi](https://nexusfi.com/a/prediction-markets/position-sizing-binary-markets) [fetched via snippet].

**Simultaneous, mutually exclusive and correlated bets**

- **Mutually exclusive outcomes** (horse race; soccer 1X2) — Kelly 1956 [ref, not fetched]; explicit algorithm in Smoczyński, P. & Tomkins, D. (2010), "An explicit solution to the problem of optimizing the allocations of a bettor's wealth when wagering on horse races," *Mathematical Scientist* 35(1) [ref, not fetched]. Algorithm:
  1. Sort outcomes by `p_i·o_i` in descending order.
  2. For a candidate set S, compute the reserve rate `R(S) = (1 − Σ_{i∈S} p_i)/(1 − Σ_{i∈S} 1/o_i)`.
  3. Add outcomes to S while `p_i·o_i > R(S)`.
  4. Stake `f_i = p_i − R/o_i` for i ∈ S, and 0 otherwise.

  Two consequences:
  - You may optimally back two of the three 1X2 outcomes, such as draw and away.
  - The stake on an outcome is *not* the single-bet Kelly stake, because the other legs hedge it.
- **Many simultaneous independent events** — Whitrow, C. (2007). "Algorithms for optimal allocation of bets on many simultaneous events." *JRSS Series C (Applied Statistics)* 56(5): 607–623. https://doi.org/10.1111/j.1467-9876.2007.00594.x — [RePEc](https://ideas.repec.org/a/bla/jorssc/v56y2007i5p607-623.html) [fetched via abstract]
  - Maximizes E log over the 2^n joint outcomes using stochastic-gradient algorithms, compared with the simplex method, and tests on real bookmaker odds.
  - Generalizes Kelly to many simultaneous bets.
  - A 2026 arXiv paper (Long, [arXiv:2603.26620](https://arxiv.org/html/2603.26620v1)) calls Whitrow's finding an "empirical near-proportionality phenomenon": the singles-only optimum is close to the isolated per-event Kelly stakes, scaled down [fetched via snippet].
- **Grant, Johnstone & Kwon (2008)**, "Optimal Betting Strategies for Simultaneous Games," *Decision Analysis* 5(1). https://doi.org/10.1287/deca.1080.0106 — [INFORMS](https://pubsonline.informs.org/doi/abs/10.1287/deca.1080.0106) [fetched via search listing only].
- **Same-game and correlated bets** [derived/inference]. With correlated outcomes (for example side + total in the same NFL game, or Kalshi ladders on the same underlying), maximize `E[ln(1 + Σ_i f_i R_i)]` over the *joint* outcome distribution. Monte Carlo from the model's joint simulation works well for this.
  - The continuous approximation gives the vector `f* ≈ Σ⁻¹ μ`, where Σ is the covariance of per-unit returns.
  - Positively correlated legs reduce the stake on each leg, and same-direction bets on one event behave like a single larger bet.
  - No fetched source covers same-game correlation specifically; see Gaps.

**Kelly relative to the market**

- A market-relative edge implies a Kelly fraction [derived]. If the no-vig market probability is `m` and the bet is priced at the market (`o ≈ 1/m` before vig), then `f* = (p − m)/(1 − m)`. This is identical in form to the prediction-market formula, so Kelly stake is linear in the probability gap `p − m`.
- In practice, blend model and market probabilities before sizing: `p_used = w·p_model + (1 − w)·m`, with `w` chosen by out-of-sample log-loss.
  - This is a form of shrinkage toward the market prior.
  - The closing line is a strong prior: football-data finds a ~1:1 relation between price/close ratio and realized yield ([football-data.co.uk, "The Efficiency of the Pinnacle.com Closing Line"](https://football-data.co.uk/blog/pinnacle_efficiency.php) [fetched]).
  - No fetched source gives a canonical formula for `w`.

### Inferences
- For a typical NFL side bettor with a real 53% edge, full Kelly is only 1.3% of bankroll per bet. The realistic edge is smaller, and `p` is estimated with error that is large relative to a 0.6-percentage-point edge. Shrinkage (Baker & McHale) therefore pushes the sensible stake to ~0.3–0.65% (¼–½ Kelly).
- On Kalshi, fees are price-dependent. Run Kelly on the all-in price `c + φ(c)`, never on the quoted mid. Near 50¢ the 7%·c(1−c) taker fee (1.75¢) can erase small edges entirely.
- For 1X2 soccer, use the Kelly/Smoczyński–Tomkins multi-outcome solution. For portfolios of same-day independent matches, Whitrow's result implies scaled-down single Kellys are close to optimal. For correlated same-game legs, use joint simulation.

### Gaps
- Thorp (2006) and the continuous-time drawdown formula `P(min W ≤ x) = x^(2/k−1)` were not fetched this session. They are given from bibliographic knowledge and must be verified.
- The exact closed-form shrinkage factor in Baker & McHale (2013) was not retrieved; only the abstract was. The `k*` formula above is a derivation in the same spirit, not their formula.
- Kalshi's official fee schedule (including the sports-specific rate and current effective date) was not retrieved; only secondary sources were.
- No peer-reviewed source on Kelly for same-game parlays or correlated props was found.

---

## 2. CLV (closing line value) as a measure of skill

### Takeaway
CLV compares the price you got with the efficient (no-vig) closing price. Across large soccer samples, the price/close ratio predicts realized yield almost 1:1 minus the margin.

Because each bet's CLV is a low-variance, continuous signal, it converges far faster than win/loss ROI. Two caveats:
- CLV must exceed the vig to be profitable.
- At least one rigorous NBA study (Whelan) finds that only the top decile of CLV converts into meaningful profit.

### Cited Findings

**Definitions** [derived from cited usage]
- Price CLV: `CLV_price = o_taken / o_close − 1`.
  - Example from Buchdahl's analysis: a bet at 2.50 against a 2.00 close has "25%" expected value.
  - Source: [football-data.co.uk Pinnacle efficiency](https://football-data.co.uk/blog/pinnacle_efficiency.php) [fetched]; same definition in [Whelan, "The Truth about Closing Line Value"](https://www.karlwhelan.com/?p=2595) [fetched].
- No-vig version (recommended): `EV_close = o_taken · π_close − 1`, where `π_close` is the de-vigged closing probability.
  - Multiplicative de-vig: `π_i = (1/o_i)/Σ_j(1/o_j)`.
  - Alternatives include the power/Shin methods (not fetched here).
  - This measures your expected ROI *if the close is the true probability*.
- Kalshi analogue: `CLV = π_close − c'` in probability points. Here `π_close` is the closing mid or last price, and `c'` is your all-in entry price including fee.

**Evidence that CLV predicts ROI**
- **Buchdahl/football-data, 87,960 Pinnacle pre-closing vs closing price pairs** (4 seasons from 2012/13):
  - Expected yield (price/close ratio) and actual level-stake returns are strongly correlated with "an almost perfect 1:1 relationship" (slope ≈ 1.00).
  - Expected yields run a few points above observed yields because the margin was not removed.
  - Source: [football-data.co.uk](https://football-data.co.uk/blog/pinnacle_efficiency.php) [fetched]
- **Buchdahl, 132,645 soccer matches** (search snippet; Pinnacle articles by Buchdahl):
  - Where the opening/closing ratio was 1.05, actual returns were ~105%.
  - The average positive-EV bet had expected value 108.8% (median 106.0%), and only 2.8% of the sample exceeded 125%.
  - Sources: [Pinnacle author page, Joseph Buchdahl](https://www.pinnacle.com/betting-resources/en/author/joseph-buchdahl); [football-data list of Buchdahl's Pinnacle articles](https://football-data.co.uk/blog/pinnaclesports_articles.php) [fetched via snippet only; the exact article was not retrieved].
- **Pinnacle's Marco Blume** argues that beating the closing line is a reliable sign of long-term +EV; others treat it as a sign of skill but not a requirement. The original Pinnacle page was not retrieved — see [Pinnacle "Why Pinnacle doesn't close winning accounts"](https://www.pinnacle.com/betting-resources/en/educational/the-maths-behind-pinnacles-winners-welcome-policy/n6rjx78p6nrd6zyk) [snippet].
- **Kaunitz, Zhong & Kreiner (2017)**, "Beating the bookies with their own numbers — and how the online sports betting market is rigged," [arXiv:1710.02824](https://arxiv.org/abs/1710.02824) [fetched abstract]:
  - Used the consensus implied probabilities across bookmakers to find mispriced odds.
  - Profitable in a 10-year closing-odds simulation, a 6-month minute-to-minute simulation, and 5 months of real-money betting across thousands of games.
  - Bookmakers responded with "discriminatory practices against successful clients" (account limiting).
  - A search snippet reports mean odds 2.32 with 9.9% return over 6,994 bets, and p = 0.089 on a 672-bet subsample. These numbers were not verified in the full text.

**Counter-evidence and caveats**
- **Whelan, ["The Truth about Closing Line Value"](https://www.karlwhelan.com/?p=2595)** [fetched]. NBA moneylines, 3,670 games 2022/23–2024/25, ~10 books per game, close = median of the books' final quotes:
  - Positive-CLV bets do outperform negative-CLV ones.
  - But a ninth-decile example with ~5% average CLV earned only ~0.2% profit, and only the top CLV decile earned meaningful profit (11.4%; 16% at the 24-hour horizon).
  - NBA margin ≈ 4.5%.
  - Conclusion: positive average CLV does not guarantee profit; CLV must beat the vig.
  - Caveat: the full calculations are in Whelan's book *Fine Margins*.
- **TheSpread** and **Track360** state the common practitioner view: CLV is "the strongest single proxy for long-term betting skill" but not a guarantee — [Track360](https://track360.io/glossary/closing-line-value), [TheSpread](https://www.thespread.com/?p=536584) [snippets; low-authority sources].
- **NFL opening vs closing lines:** [arXiv:1211.4000](https://arxiv.org/pdf/1211.4000) found no statistically significant difference in predictive value between them [snippet]. So the "close is always sharper" assumption is market-dependent.

**Why CLV converges faster** [derived]
- The per-bet outcome-based return at decimal odds `o` has SD ≈ `√(o − 1)` per unit staked for a near-fair bet. That is 1.0 at evens and 0.95 at −110 (see section 5).
- Per-bet CLV (for example `ln(o_taken/o_close)`) is a continuous quantity whose SD is typically a few percent. This was not measured from a source here.
- The number of bets needed to estimate the mean to a given precision scales with variance. With CLV SD around 0.03–0.05 versus ROI SD around 0.95, CLV needs roughly (0.95/0.04)² ≈ 500× fewer bets.
- This holds only under the assumption that the closing price is an unbiased estimate of true probability. The assumption is supported by Buchdahl's ~1:1 slope and qualified by Whelan.

### Inferences
- For model evaluation, compute both no-vig `EV_close` and raw `o/o_close − 1`. Test whether mean no-vig CLV > 0 *and* whether mean raw CLV exceeds the market margin.
- For Kalshi, where "closing" is the last trade before event lock, the analogous metric is `π_last − c_entry_all_in`. Thin late liquidity can make the last price noisy; use a time-weighted mid over the final N minutes.
- Treat CLV as a *leading indicator* to be corroborated by ROI over time, not as a substitute. Whelan's result shows that the mapping from CLV to profit depends on margin and market efficiency.

### Gaps
- The original Buchdahl Pinnacle article with the 132,645-match analysis was not retrieved; the figures come from a search summary.
- No source measuring the empirical SD of per-bet CLV was found, so the ~500× speed-up is an illustrative assumption.
- I found no peer-reviewed study that formally regresses bettor-level long-run ROI on bettor-level CLV.

---

## 3. Scoring rules, calibration, and model-vs-market comparison

### Takeaway
Use strictly proper scoring rules to compare probabilistic forecasts:
- log-loss / ignorance;
- Brier score (multi-class quadratic);
- RPS for ordered outcomes.

Decompose Brier (Murphy) into reliability − resolution + uncertainty, plot reliability diagrams, and report ECE. Compare model versus market loss differentials with Diebold–Mariano tests.

For soccer 1X2, Constantinou & Fenton (2012) argued for RPS. Wheatcroft (2019/2021) argues the distance-sensitivity argument adds nothing and that log score (ignorance) performs better.

### Cited Findings

**Proper scoring rules**
- Gneiting, T. & Raftery, A. E. (2007). "Strictly Proper Scoring Rules, Prediction, and Estimation." *JASA* 102(477): 359–378. https://doi.org/10.1198/016214506000001437 [ref, not fetched].
  - A scoring rule is strictly proper if the expected score is uniquely optimized by reporting the true distribution.
  - The log score and the quadratic (Brier) score are both strictly proper.
- Formulas (K outcomes, forecast vector p, one-hot outcome y; standard):
  - **Log-loss / ignorance:** `LL = −(1/N) Σ_n ln p_{n, y_n}`.
  - **Brier (multi-class):** `BS = (1/N) Σ_n Σ_k (p_{nk} − y_{nk})²`. The binary form is `(p − y)²`.
  - **RPS** (Epstein 1969, *J. Applied Meteorology* 8: 985–987 [ref, not fetched]), for ordered outcomes (Home, Draw, Away), with cumulative `P_k = Σ_{j≤k} p_j` and `Y_k = Σ_{j≤k} y_j`:
    `RPS = (1/(K−1)) Σ_{k=1}^{K−1} (P_k − Y_k)²`.
    Penaltyblog reproduces the RPS worked examples: [penaltyblog RPS docs](https://penaltyblog.readthedocs.io/en/latest/metrics/rps.html) [snippet].
- **Murphy decomposition.** Murphy, A. H. (1973). "A New Vector Partition of the Probability Score." *J. Applied Meteorology* 12: 595–600 [ref, not fetched].
  - Bin forecasts into K bins with n_k forecasts, mean forecast f̄_k, observed frequency ō_k, and overall base rate ō:
    `BS = (1/N) Σ_k n_k (f̄_k − ō_k)² − (1/N) Σ_k n_k (ō_k − ō)² + ō(1 − ō)`,
    i.e. **BS = Reliability − Resolution + Uncertainty**.
  - Lower reliability is better (calibration). Higher resolution is better (sharpness / discrimination). Uncertainty depends only on the base rate.
- **Expected Calibration Error** (standard ML definition; Naeini, Cooper & Hauskrecht 2015, AAAI; Guo et al. 2017, ICML "On Calibration of Modern Neural Networks" [ref, not fetched]):
  `ECE = Σ_k (n_k/N) |ō_k − f̄_k|`.
  It is binning-dependent, so report the bin scheme (equal-width or equal-mass) and add bootstrap CIs.

**The RPS debate in soccer**
- **Constantinou, A. C. & Fenton, N. E. (2012).** "Solving the problem of inadequate scoring rules for assessing probabilistic football forecasting models." *Journal of Quantitative Analysis in Sports* 8(1). https://doi.org/10.1515/1559-0410.1418 — [QMUL repository](https://qmro.qmul.ac.uk/xmlui/handle/123456789/10783) [fetched record].
  - Because H/D/A is ordinal, probability mass "close" to the actual outcome should be rewarded.
  - Using five hypothetical matches, RPS was the only candidate rule that ranked their preferred forecast best every time.
  - This paper made RPS the de facto football metric.
- **Wheatcroft, E. (2019/2021).** "Evaluating probabilistic forecasts of football matches: The case against the Ranked Probability Score." *JQAS* — [arXiv:1908.08980](https://arxiv.org/abs/1908.08980); [LSE Research Online](https://researchonline.lse.ac.uk/id/eprint/111494) [fetched via search abstract].
  - Argues the distance-sensitivity rationale "adds nothing in terms of the usual aims of using scoring rules."
  - In simulations, the **Ignorance (log) score** outperforms both RPS and Brier at selecting the better forecaster.

**Comparing model versus market**
- **Diebold, F. X. & Mariano, R. S. (1995).** "Comparing Predictive Accuracy." *JBES* 13(3): 253–263 [ref, not fetched].
  - Define the loss differential `d_t = L(model_t) − L(market_t)`, for example per-game log-loss, with `d̄` its mean.
  - `DM = d̄ / √(LRV̂(d)/T)` is asymptotically N(0,1), where LRV is a HAC/Newey–West long-run variance.
  - Small-sample correction: Harvey, Leybourne & Newbold (1997), *IJF* 13: 281–291 [ref, not fetched].
  - For independent games, the plain paired t-test (or a paired bootstrap of `d_t`) is equivalent.
  - Cluster by date or week when games share information.
- **Market benchmark:** the de-vigged closing probability. Buchdahl argues the Pinnacle close is "the most efficient or most accurate representation of the probabilities of actual results" ([football-data.co.uk](https://football-data.co.uk/blog/pinnacle_efficiency.php) [fetched]). A model that cannot beat the close's log-loss has no informational edge at closing time. It could still have an edge at bet-time prices: compare against the price you could actually bet.

### Inferences
- Primary metric: log-loss, with Brier and RPS as secondary metrics, in line with Wheatcroft's critique. For 1X2, still report RPS for comparability with the literature.
- The model-vs-market test should use the market price available *at decision time* (the bet-able line) for the edge claim, and the closing price for the information-efficiency claim. These answer different questions.
- Calibration (reliability) matters more for Kelly than raw discrimination. A well-ranked but overconfident model inflates `p − m` and overbets.

### Gaps
- Gneiting & Raftery, Murphy, Diebold–Mariano and ECE references were not fetched this session. The formulas are standard but should be cross-checked.
- No source found comparing DM-test power for log-loss versus Brier in sports-specific sample sizes.

---

## 4. Honest backtesting: walk-forward, leakage, overfitting and multiple testing, bet-able prices, survivorship

### Takeaway
Backtests must be walk-forward (rolling or expanding origin), with every feature, rating and hyperparameter computed only from information available at bet time. They must use prices you could actually have bet (with fees, limits and stale-line risk), not closing prices.

Multiple-testing inflation must be corrected for:
- Deflated Sharpe Ratio (Bailey & López de Prado 2014);
- Probability of Backtest Overfitting (PBO);
- White's Reality Check / Hansen's SPA.

### Cited Findings

**Deflated Sharpe Ratio**
- **Bailey, D. H. & López de Prado, M. (2014).** "The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting and Non-Normality." *Journal of Portfolio Management* 40(5): 94–107. https://doi.org/10.3905/jpm.2014.40.5.094 — [SSRN 2460551](https://papers.ssrn.com/abstract=2460551) [fetched abstract]; formulas via [Wikipedia, Deflated Sharpe ratio](https://en.wikipedia.org/wiki/Deflated_Sharpe_ratio) [snippet; verify against the paper].
- **Probabilistic Sharpe Ratio (PSR)**, for T observations with skew γ₃ and kurtosis γ₄:
  `PSR(SR*) = Φ( (SR̂ − SR*)·√(T − 1) / √(1 − γ₃·SR̂ + ((γ₄ − 1)/4)·SR̂²) )`.
- **Expected maximum Sharpe under the null** across N independent trials with variance V[SR̂_n] (γ = Euler–Mascheroni ≈ 0.5772):
  `SR*₀ = √V[SR̂_n] · [ (1 − γ)·Φ⁻¹(1 − 1/N) + γ·Φ⁻¹(1 − 1/(N·e)) ]`.
- **DSR = PSR(SR*₀).** With N = 1 it reduces to PSR. The correction assumes independent trials, so use the *effective* number of independent trials when model variants are correlated.
- **Betting mapping** [derived]: per-bet Sharpe = mean per-unit return / SD of per-unit return. Count N as all model variants, thresholds, leagues and markets ever tried, not just those reported.

**Data snooping**
- **White, H. (2000).** "A Reality Check for Data Snooping." *Econometrica* 68(5): 1097–1126 [ref, not fetched]. Bootstrap test of whether the *best* of many strategies beats a benchmark, accounting for the search.
- **Hansen, P. R. (2005).** "A Test for Superior Predictive Ability." *JBES* 23(4): 365–380 [ref, not fetched]. A studentized, less conservative version.
- **Bailey, Borwein, López de Prado & Zhu (2017).** "The Probability of Backtest Overfitting." *Journal of Computational Finance* 20(4) [ref, not fetched]. Uses combinatorially symmetric cross-validation (CSCV) to estimate the probability that the in-sample-best configuration underperforms the median out of sample.

**Walk-forward / rolling-origin** [standard practice]
- Tashman, L. J. (2000). "Out-of-sample tests of forecasting accuracy: an analysis and review." *International Journal of Forecasting* 16(4): 437–450 [ref, not fetched].
- Procedure:
  1. Fit on seasons ≤ s.
  2. Predict season s+1, or week w+1 within a season.
  3. Roll forward.
- Hyperparameters are tuned only inside each training window, using nested time-series CV.

**Leakage checklist** [derived from cited material and standard practice]
- Closing odds used as features when bets are priced at opening or bet-time odds. Kaunitz et al. used *closing-odds* simulations separately from minute-to-minute and real-money tests to address exactly this ([arXiv:1710.02824](https://arxiv.org/abs/1710.02824) [fetched]).
- Post-game information: final box-score stats, injuries announced after lock, final Elo after the game.
- Ratings computed on the full season, which is look-ahead. Elo/Massey/Dixon–Coles must be updated strictly sequentially.
- Target leakage via market-derived labels.
- Feature scaling or imputation fit on the full dataset.
- Duplicated games across train and test folds.

**Bet-able prices, limits and survivorship**
- The simulated-versus-real gap in Kaunitz et al.: bookmakers limited the winning accounts ("discriminatory practices against successful clients") — [arXiv:1710.02824](https://arxiv.org/abs/1710.02824) [fetched]. Backtest returns at soft-book prices therefore overstate achievable volume.
- Whelan shows outcomes depend on *which* timestamp's price is used (1 day vs 10 minutes before tip) — [karlwhelan.com](https://www.karlwhelan.com/?p=2595) [fetched].
- For Kalshi, use historical order-book prices on the side you would take (ask for buys), plus the taker fee `0.07·C·P(1−P)` rounded up ([Allium](https://allium.so/blog/kalshi-fees-why-the-cost-peaks-near-50-cents/) [snippet]), and respect displayed depth.
- Survivorship [inference]:
  - Tipster or model leaderboards that drop failed entrants inflate apparent skill.
  - Markets that were delisted or voided must remain in the sample.
  - Report every model variant tried (it feeds N in the DSR).

### Inferences
- A defensible protocol:
  1. Freeze a feature-time contract (each feature timestamped ≤ bet time).
  2. Walk-forward by season or week.
  3. Price at bet-able quotes with fees and limits.
  4. Log every variant tried to compute DSR/PBO.
  5. Hold out a final untouched season, or forward paper-trade.
  6. Report CLV and ROI with confidence intervals.
- Because Kalshi retains only a rolling history (per project memory: ~70 days for MLB), forward-only paper trading is often the only clean out-of-sample test.

### Gaps
- The full DSR paper was not retrieved. The PSR denominator and SR*₀ formula come from secondary sources (Wikipedia and implementations) and must be verified.
- White (2000), Hansen (2005), Bailey et al. PBO (2017) and Tashman (2000) are given from bibliographic knowledge only.
- No sports-specific published study applying DSR or Reality Check to betting models was found this session.

---

## 5. Variance and sample size: proving an edge, significance tests, drawdown and risk of ruin

### Takeaway
Win/loss outcomes are extremely noisy. At −110 with a true 53% win rate (ROI +1.18%):
- per-bet return SD ≈ 0.95;
- ~17,600 bets give only a 50% chance of a one-sided 5% significant result;
- ~40,000 bets are needed for 80% power.

The SE of ROI is ≈ `√(o − 1)/√n`, so longshot bettors need even more bets. Use binomial or t-tests on per-unit returns and bootstrap CIs, and evaluate CLV (lower variance) alongside them.

### Cited Findings

**Variance of per-unit return** [derived]

| Bet type | Per-unit return | Variance | SD |
|---|---|---|---|
| Binary bet at net odds b | `+b` w.p. p, `−1` w.p. q | `p·q·(1 + b)²` | `√(pq)·(1+b)` |
| Near-fair bet (p ≈ 1/o) | — | `≈ o − 1` | `≈ √(o − 1)` |
| −110, p = 0.53 | — | — | 0.953 |

- Near-fair SD by decimal odds: 0.71 at 1.5; 1.0 at 2.0; 1.41 at 3.0; 2.0 at 5.0; 3.0 at 10.0.
- **SE(ROI) ≈ √(o−1)/√n.** This is consistent with Thorp's "square-root" rule that cumulative deviation from expectation grows ~√n while deviation as a fraction of turnover shrinks ~1/√n — [urbino.net, Thorp's Mathematics of Gambling, "Standard Deviation (Repeated Trials)"](https://urbino.net/standard-deviation-repeated-trials/) [snippet].

**NFL −110, true p = 0.53** [derived]

| Bets n | SE of ROI | z-score of true 1.18% ROI |
|---|---|---|
| 100 | 9.5% | 0.12 |
| 500 | 4.3% | 0.28 |
| 1,000 | 3.0% | 0.39 |
| 2,500 | 1.9% | 0.62 |
| 10,000 | 0.95% | 1.24 |

The sample size to reject H₀: ROI ≤ 0 (equivalently p ≤ 0.5238) is `n = ((z_α + z_β)·σ/μ)²`:

| Test level and power | Bets needed |
|---|---|
| α = 5% one-sided, 50% power | 17,590 |
| α = 5% one-sided, 80% power | 40,190 |
| α = 2.5% one-sided (two-sided 5%), 80% power | 51,020 |

**Tests**
- **Binomial test** (equal odds): P(X ≥ wins | n, p₀ = break-even). This is recommended over ad hoc rules — [SBR forum thread](https://www.sportsbookreview.com/forum/players-talk/1636126-statistics-question-re-sample-size) [snippet; forum].
- **Z-score:** `z = (wins − n·p₀)/√(n·p₀·q₀)`. A patent document example: 90/100 → 8σ ([USPTO 8352346](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8352346) [snippet]).
- **A secondhand "Pinnacle rule of thumb"** circulates on forums: wins needed ≈ n/2 + √n. For 500 bets that is 272 wins (54.4%). Two problems:
  - It is not verified at a Pinnacle source.
  - It is about 2σ above a 50% baseline at even money: σ_wins = √n/2, so n/2 + √n = +2σ. It ignores vig (the −110 break-even is 52.38%, not 50%).
  - Source: [SBR forum](https://www.sportsbookreview.com/forum/players-talk/1636126-statistics-question-re-sample-size) [snippet].
- **Mixed odds:** use a one-sample t-test on per-unit returns r_i: `t = r̄ / (s/√n)`. Buchdahl's approach is a t-statistic-style test that adjusts for average odds; his full method is not retrieved here (see Gaps).
- **Bootstrap:** resample bets (or weeks or blocks, for dependence) to get CIs on ROI. A permutation/Monte Carlo alternative simulates outcomes under H₀ using de-vigged market probabilities, then reports the p-value of the observed profit.
- **Empirical illustration** (Kaunitz et al. per search snippet): a 672-bet sample with a real edge gave p = 0.089, not significant, while 6,994 bets at average odds 2.32 gave a 9.9% return — [arXiv:1710.02824](https://arxiv.org/pdf/1710.02824) [snippet; numbers not verified in full text].
- **Luck vs skill in forecasting tournaments** (more general): [arXiv:2509.08744](https://arxiv.org/pdf/2509.08744) [listing only]. Testing Sharpe luck vs skill: [arXiv:1905.08042](https://arxiv.org/pdf/1905.08042) [listing only].

**Drawdowns and risk of ruin**
- Simulated drawdowns at the NFL edge: see the table in section 1. At full Kelly the median max drawdown over 5,000 bets is ~58% and P(DD > 50%) ≈ 70%. At quarter Kelly the median DD is ~18% [derived].
- Under Kelly/fractional Kelly with proportional staking, literal ruin is impossible ("the E log X bettor never risks ruin" — [MacLean, Thorp & Ziemba](https://www.stat.berkeley.edu/~aldous/157/Papers/Good_Bad_Kelly.pdf) [fetched]). Practical ruin is defined as hitting a floor (e.g. −50%). Estimate it by Monte Carlo, or with the continuous approximation `P(ever reach x) = x^(2/k − 1)` (Thorp 2006 [ref, not fetched]).
- **Classical gambler's-ruin** for flat staking [standard]. With unit bets, win prob p, even payoff and bankroll of B units:
  `P(ruin) = ((q/p)^B − (q/p)^N)/(1 − (q/p)^N)` for target N.
  - As N → ∞ this becomes `(q/p)^B` when p > q.
  - For uneven odds, use simulation or the Lundberg-type bound `P(ruin) ≤ e^{−R·B}`, where R solves `E[e^{−R·X}] = 1`.

### Inferences
- With realistic NFL edges (≤ 1–2% ROI), ROI-based "proof" needs tens of thousands of bets, which no individual season provides. This is why CLV (section 2) and proper-score comparisons against the market (section 3, DM test on thousands of games) are the practical evidence.
- Longshot-heavy strategies (soccer draws and aways at 3.0–5.0; Kalshi contracts priced < 20¢) have 1.4–2× the per-bet SD of even-money bets, so they need 2–4× more bets for the same precision.
- For Kalshi, a contract at price c has per-contract return SD `√(c(1−c))/c` per dollar risked. At c = 0.20 that is 2.0, the same as decimal odds 5.0.

### Gaps
- Buchdahl's specific p-value / t-test formula (from *Squares & Sharps, Suckers & Sharks* or his Pinnacle article on luck vs skill) was not retrieved. His exact method, which reportedly adjusts the standard deviation for odds, is a gap to fill from the original.
- Pinnacle's own articles on sample size and the "how many bets" rule of thumb were not found; the √n rule above comes from a forum relay.
- The Kaunitz et al. numbers (6,994 bets, 9.9%, p = 0.089) come from a search snippet and should be verified in the PDF.
- The Wizard of Odds and Unabated sources suggested in the brief were not retrieved because of the tool-call budget.
