# Mathematical and statistical foundations of predictive models for sports betting (soccer, NFL, CFB)

> Research notes compiled 2026-10-18. Scope: how match outcome, spread, total and derivative probabilities are modelled; exact formulas, assumptions, weaknesses and empirical performance.
> **Method note:** Within this session's tool budget, I verified some sources directly: the FiveThirtyEight NFL Elo source code, Sides et al. (2022, CFB), the Covers totals table, Walsh & Joshi (2024), the abstracts of Hubáček et al. and Berrar et al., the pi-rating parameters, and the Dixon-Coles ξ value through secondary sources. I did not re-download the full texts of several classic papers (Maher 1982, Dixon & Coles 1997, Karlis & Ntzoufras 2003, Baio & Blangiardo 2010, Glickman & Stern 1998, Glickman 1999, Herbrich et al. 2006). Their formulas below are the standard published specifications, cited by full reference. Anything not confirmed by a fetched source is marked **[unverified]** or listed under Gaps.

---

## 1. Soccer goal models: Poisson → Dixon-Coles → bivariate Poisson → NB/ZIP → Bayesian hierarchical; deriving 1X2 / AH / O/U / BTTS; xG vs goals

### Takeaway
Most structural soccer models use the double-Poisson framework. Each team gets attack and defence strength parameters plus a home effect, giving goal rates λ (home) and μ (away). Dixon-Coles adds a low-score dependence correction τ and exponential time decay ξ. Every market (1X2, Asian handicap, totals, BTTS, correct score) is then a sum over cells of a single score-probability matrix. xG-based inputs are less noisy than goals and are generally found more predictive of future performance. I found no clean head-to-head benchmark of xG-fed versus goals-fed Dixon-Coles.

### Cited Findings

**Maher (1982), independent Poisson.** Home goals $X\sim\text{Pois}(\lambda)$ and away goals $Y\sim\text{Pois}(\mu)$ are independent, with
$$\lambda=\alpha_i\beta_j\gamma,\qquad \mu=\alpha_j\beta_i,$$
where $\alpha$ = attack, $\beta$ = defence weakness and $\gamma$ = home advantage. In log-linear (GLM) form: $\log\lambda=\text{home}+\text{att}_i-\text{def}_j$, with the identifiability constraint $\sum\text{att}=0$ (or mean 1 in multiplicative form). Fitted by maximum likelihood / Poisson GLM. Maher noted a small positive correlation between home and away scores and under-prediction of draws. — Maher, M.J. (1982) "Modelling association football scores", *Statistica Neerlandica* 36(3):109–118. https://doi.org/10.1111/j.1467-9574.1982.tb00782.x

**Dixon & Coles (1997).** Joint probability:
$$P(X=x,Y=y)=\tau_{\lambda,\mu}(x,y)\,\frac{e^{-\lambda}\lambda^x}{x!}\frac{e^{-\mu}\mu^y}{y!}$$
$$\tau(x,y)=\begin{cases}1-\lambda\mu\rho & x=y=0\\ 1+\lambda\rho & x=0,y=1\\ 1+\mu\rho & x=1,y=0\\ 1-\rho & x=y=1\\ 1&\text{otherwise}\end{cases}$$
with $\max(-1/\lambda,-1/\mu)\le\rho\le\min(1/(\lambda\mu),1)$. Here $\lambda=\alpha_i\beta_j\gamma$ and $\mu=\alpha_j\beta_i$. The correction touches only the 0-0, 1-0, 0-1 and 1-1 cells, and ρ sets the direction of the shift. Under the usual parameterisation (penaltyblog, metricgate), a negative ρ raises the 0-0 and 1-1 probabilities. — Dixon, M.J. & Coles, S.G. (1997) "Modelling association football scores and inefficiencies in the football betting market", *JRSS C (Applied Statistics)* 46(2):265–280. https://research-information.bris.ac.uk/en/publications/modelling-association-football-scores-and-inefficiencies-in-the-f/ ; tau description in https://penaltyblog.readthedocs.io/en/latest/models/overview.html

**Time weighting (pseudo-likelihood).** The likelihood is maximised over matches $k$ played before time $t$:
$$L_t=\prod_{k:t_k<t}\big[\tau(x_k,y_k)\,\text{Pois}(x_k;\lambda_k)\,\text{Pois}(y_k;\mu_k)\big]^{\phi(t-t_k)},\qquad \phi(t)=e^{-\xi t}.$$
Dixon & Coles chose ξ by maximising out-of-sample predictive log-likelihood of match outcomes. A 2026 arXiv paper cites ξ = 0.0065 per half-week (days/3.5), "following Dixon and Coles", and notes the half-life is roughly one year. ξ is not a universal default: penaltyblog's docs use example values such as 0.001 per day. — https://arxiv.org/pdf/2605.16066 ; https://penaltyblog.readthedocs.io/en/latest/models/overview.html
- **Arithmetic check [inference]:** $\ln 2/0.0065 \approx 107$ half-weeks $\approx 1.03$ years, which is consistent with the "one-year half-life".
- **Estimation in practice:** ML via numerical optimisation (L-BFGS / Nelder-Mead) on the weighted log-likelihood, with constraint $\sum\log\alpha_i=0$. The original paper also used a two-stage approach that fits ρ along with the team parameters. — Dixon & Coles (1997), ibid.

**Bivariate Poisson (Karlis & Ntzoufras 2003).** Let $X=W_1+W_3$ and $Y=W_2+W_3$ with $W_k\sim\text{Pois}(\lambda_k)$ independent. Then $\text{Cov}(X,Y)=\lambda_3$ and
$$P(x,y)=e^{-(\lambda_1+\lambda_2+\lambda_3)}\frac{\lambda_1^x}{x!}\frac{\lambda_2^y}{y!}\sum_{k=0}^{\min(x,y)}\binom{x}{k}\binom{y}{k}k!\left(\frac{\lambda_3}{\lambda_1\lambda_2}\right)^k.$$
Here $\log\lambda_1=\mu+\text{home}+\text{att}_i+\text{def}_j$ and $\log\lambda_2=\mu+\text{att}_j+\text{def}_i$. The authors also propose a diagonal-inflated version that inflates draw probabilities, $P_D(x,y)=(1-p)\,BP(x,y)+p\,D(x;\theta)\mathbb{1}[x=y]$, fitted by EM. Weakness: the model only allows non-negative correlation. — Karlis, D. & Ntzoufras, I. (2003) "Analysis of sports data by using bivariate Poisson models", *JRSS D (The Statistician)* 52(3):381–393. https://doi.org/10.1111/1467-9884.00366

**Negative binomial / zero-inflated variants.** These handle overdispersion ($\text{Var}>\text{mean}$) through NB with $\text{Var}=\mu+\mu^2/r$, or extra zeros through ZIP: $P(0)=\pi+(1-\pi)e^{-\lambda}$. Packages such as penaltyblog implement Poisson, Dixon-Coles, bivariate Poisson, NB, ZIP and Weibull-count models side by side. — https://penaltyblog.readthedocs.io/en/latest/models/overview.html
- **[Inference / widely reported, not verified this session]:** League goal counts are close to equidispersed, so NB/ZIP rarely beat DC by much on outcome RPS. Their main use is in derivative tails (high totals, 0-0).

**Bayesian hierarchical (Baio & Blangiardo 2010).**
$$y_{g1}\mid\theta_{g1}\sim\text{Pois}(\theta_{g1}),\quad \log\theta_{g1}=\text{home}+\text{att}_{h(g)}+\text{def}_{a(g)},\quad \log\theta_{g2}=\text{att}_{a(g)}+\text{def}_{h(g)}.$$
$\text{att}_t\sim N(\mu_{att},\tau_{att}^{-1})$ and $\text{def}_t\sim N(\mu_{def},\tau_{def}^{-1})$, with sum-to-zero constraints. The hierarchy induces correlation between $y_{g1}$ and $y_{g2}$ ("conditional independence given θ yields marginal dependence"). Because the pooled hierarchy over-shrinks extreme teams, the authors propose a **mixture prior** with three latent groups (top / mid / bottom), each with its own mean and precision, which reduces over-shrinkage. Fitted by MCMC (WinBUGS) on Serie A 2007/08. — Baio, G. & Blangiardo, M. (2010) "Bayesian hierarchical model for the prediction of football results", *Journal of Applied Statistics* 37(2):253–264. https://doi.org/10.1080/02664760802684177
- **Dynamic extensions:** Rue & Salvesen (2000) *JRSS D* 49(3):399–418 (time-varying Brownian strengths); Koopman & Lit (2015) *JRSS A* 178(1):167–186 (bivariate Poisson state-space). [references, not fetched]
- **2025–26 work:** Bayesian weighted discrete-time dynamic models — https://arxiv.org/pdf/2508.05891 ; a market-calibrated AFT model for in-play forecasting — https://arxiv.org/pdf/2605.16066

**Deriving markets from the score matrix.** Let $p_{xy}=P(X=x,Y=y)$, truncated at about 10 goals each and renormalised.
- 1X2: $P(H)=\sum_{x>y}p_{xy}$, $P(D)=\sum_{x=y}p_{xy}$, $P(A)=\sum_{x<y}p_{xy}$.
- Over/under $L$ (half-line): $P(\text{Over})=\sum_{x+y>L}p_{xy}$. On an integer line, the push probability is $P(x+y=L)$, and the bet is priced with $P(\text{win})/(1-P(\text{push}))$.
- BTTS: $P=\sum_{x\ge1,y\ge1}p_{xy}=1-P(X=0)-P(Y=0)+p_{00}$.
- Asian handicap $h$ on home: let $D=X-Y$.
  - Half-ball $h=-0.5$: win iff $D\ge1$.
  - Whole ball $h=-1$: win $D\ge2$, push $D=1$, so $EV=P(W)\cdot(o-1)-P(L)$.
  - Quarter ball $h=-0.75$: half the stake on −0.5 and half on −1, so $EV=\tfrac12EV_{-0.5}+\tfrac12EV_{-1}$.
- Under independent Poisson, $D$ follows the **Skellam** distribution:
$$P(D=k)=e^{-(\lambda+\mu)}\left(\frac{\lambda}{\mu}\right)^{k/2}I_{|k|}\!\left(2\sqrt{\lambda\mu}\right)$$
where $I$ is the modified Bessel function of the first kind. — Skellam, J.G. (1946) *JRSS* 109(3):296; applied to soccer in Karlis & Ntzoufras (2009) "Bayesian modelling of football outcomes: using the Skellam's distribution for the goal difference", *IMA J. Management Mathematics* 20(2):133–145. https://doi.org/10.1093/imaman/dpn026 [not fetched]
- Inverse use: market 1X2 plus O/U prices can be inverted to implied $(\lambda,\mu)$, and the AH/BTTS price then follows. This is the standard way to "back out" team goal expectancies (penaltyblog "goal expectancy" module). — https://penaltyblog.readthedocs.io/en/latest/_sources/models/goal_expectancy.rst.txt

**xG vs goals.** Ijtsma (2015) is reported to have found xG ratio the most predictive of rest-of-season goal ratio and points per game. McKinley (2022, American Soccer Analytics) extended this and found some event-based metrics more predictive than xG in MLS. Shots are far more frequent than goals, so xG is a lower-variance signal. — as summarised in https://tonyelhabr.rbind.io/posts/xg-predictor-future-results/
- Restricting xG to neutral game states did not improve prediction of future performance over overall xG (blog analysis, not peer-reviewed). — https://tonyelhabr.rbind.io/posts/xg-predictor-future-results/
- The xG–goals association varies by competition: r = 0.488 overall, lowest in the UCL at r = 0.403. — https://www.revistas.uma.es/index.php/riccafd/article/view/21310
- Critical view: xG's focus on shot quality limits its use for team evaluation and outcome prediction. — 2026 Politecnico di Milano thesis https://www.politesi.polimi.it/retrieve/79a2e807-ec50-4951-be79-6bc203a1bc0b/2026_03_Romano_Thesis.pdf
- Comparison of xG vs expected possession value as outcome predictors (Bundesliga, 2025). — Forcher et al., *Frontiers in Sports & Active Living* https://public-pages-files-2025.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2025.1713852/pdf (results not extracted)

### Inferences
- In practice the strongest structural set-up is a DC- or bivariate-Poisson-type model with time decay, fed a blend of goals and xG. A common practitioner recipe is to fit on xG, or on a weighted mix such as 0.3·goals + 0.7·xG [inference, not a cited result]. Then shrink the result toward market-implied λ, μ.
- Because every derivative market comes from one matrix, internal consistency is guaranteed. Edge on derivatives (BTTS, AH quarter lines) comes from better dependence/dispersion modelling (ρ, λ₃, NB) rather than from better strength estimates.
- For a monotone ordinal 3-way outcome, the RPS is the standard score: $\text{RPS}=\frac{1}{r-1}\sum_{i=1}^{r-1}\big(\sum_{j\le i}(p_j-e_j)\big)^2$ (Constantinou & Fenton 2012, *JQAS* 8(1)) [reference not fetched].

### Gaps
- No peer-reviewed head-to-head found in this session of "DC fit on xG" vs "DC fit on goals" by RPS on the same leagues and seasons.
- Exact ρ estimates reported in the 1997 paper were not retrieved. Typical values are small and negative (~−0.1 to −0.2) [unverified].

---

## 2. Rating systems: Elo (incl. FiveThirtyEight NFL), Glicko/Glicko-2, TrueSkill, Massey, state-space (Glickman & Stern 1998), pi-ratings

### Takeaway
All of these share one structure: a latent strength θ, an expected-result link (logistic for Elo, normal for Glickman-Stern/TrueSkill), and an update proportional to the surprise. They differ in how uncertainty is represented (none in Elo, RD in Glicko, σ² in TrueSkill and Kalman) and in whether score margin enters the update. FiveThirtyEight's NFL Elo uses K = 20, HFA = 65 Elo, a log margin-of-victory multiplier with autocorrelation damping, and 1/3 regression to 1505 between seasons.

### Cited Findings

**Elo (logistic):** $E_A=\dfrac{1}{1+10^{-(R_A-R_B+\text{HFA})/400}}$ and $R_A' = R_A+K\cdot M\cdot(S_A-E_A)$.

**FiveThirtyEight NFL Elo (official code `forecast.py`):** `HFA = 65.0`, `K = 20.0`, `REVERT = 1/3` toward 1505 between seasons. The MOV multiplier is
$$M=\ln(\max(|PD|,1)+1)\cdot\frac{2.2}{\Delta_{elo,winner}\cdot 0.001+2.2},$$
with M = 1 for ties. $\Delta_{elo,winner}$ includes HFA. The denominator damps updates when a favourite wins big, which corrects Elo autocorrelation. Win probability is $1/(10^{-\Delta/400}+1)$. — https://github.com/fivethirtyeight/nfl-elo-game (forecast.py: https://raw.githubusercontent.com/fivethirtyeight/nfl-elo-game/master/forecast.py)
- The README benchmark scores the game's points system: the Elo baseline scores 648.24 points per season, and changing HFA from 65 to 100 lowered the score to 603.42 (vs Elo's 645.9 in that comparison). — https://github.com/fivethirtyeight/nfl-elo-game
- Later FiveThirtyEight versions added QB adjustments, travel and rest adjustments, and an Elo→spread conversion of about Elo/25 points **[unverified this session]**. The methodology page now redirects to ABC News and could not be fetched.

**Elo in soccer:** Hvattum & Arntzen (2010) "Using ELO ratings for match result prediction in association football", *IJF* 26(3):460–470. They use a goal-difference-dependent K, $K=k_0(1+\delta)^{\lambda}$, and feed the Elo difference into an ordered logit. Elo-based ordered logit was competitive with other statistical models but worse than bookmaker odds. https://doi.org/10.1016/j.ijforecast.2009.10.002 [not fetched]

**Glicko (Glickman 1999, *JRSS C* 48(3):377–394):** Each player has $(r, RD)$, with $q=\ln10/400$ and $g(RD)=1/\sqrt{1+3q^2RD^2/\pi^2}$.
- $E=1/(1+10^{-g(RD_j)(r-r_j)/400})$
- $d^2=\big[q^2\sum g^2E(1-E)\big]^{-1}$
- $r'=r+\frac{q}{1/RD^2+1/d^2}\sum g(RD_j)(s_j-E)$ and $RD'=(1/RD^2+1/d^2)^{-1/2}$
- Between periods, RD grows: $RD\leftarrow\min(\sqrt{RD^2+c^2t},350)$.
- Glicko-2 adds a volatility σ updated by a one-dimensional root-find (system constant τ).
- Source: http://www.glicko.net/glicko/glicko.pdf ; http://www.glicko.net/glicko/glicko2.pdf [not fetched; standard spec]

**TrueSkill (Herbrich, Minka & Graepel 2006, NeurIPS):** Skill $s\sim N(\mu,\sigma^2)$ and performance $p\sim N(s,\beta^2)$. With $c^2=2\beta^2+\sigma_A^2+\sigma_B^2$ and $t=(\mu_A-\mu_B)/c$, the update for winner A is
$$\mu_A\leftarrow\mu_A+\frac{\sigma_A^2}{c}v(t,\varepsilon/c),\qquad \sigma_A^2\leftarrow\sigma_A^2\big[1-\frac{\sigma_A^2}{c^2}w(t,\varepsilon/c)\big],$$
where $v=\phi/\Phi$ and $w=v(v+t)$, and ε is the draw margin. Inference uses message passing / EP on a factor graph. — https://www.microsoft.com/en-us/research/publication/trueskilltm-a-bayesian-skill-rating-system/ [not fetched]

**Massey / least squares (Massey 1997 thesis):** Solve $y_g=r_{h}-r_{a}+\text{HFA}+\varepsilon$ by least squares. The normal equations $M r = p$ have $M$ = Laplacian-like (games-played diagonal, −games between off-diagonal) and $p$ = cumulative point differential. One row is replaced with $\sum r=0$ for identifiability. MOV capping is common in CFB. Equivalent to ridge-free OLS on a team-indicator design matrix. — Massey, K. (1997) "Statistical models applied to the rating of sports teams", Bluefield College honors thesis; https://masseyratings.com/theory/massey97.pdf [not fetched]

**Glickman & Stern (1998) NFL state-space model:**
$$y_{g}=\theta_{h,w}-\theta_{a,w}+\alpha_{h}+\varepsilon_g,\quad\varepsilon\sim N(0,\sigma^2)$$
- Within a season: $\theta_{w+1}=\beta_w\theta_w+\omega$, $\omega\sim N(0,\sigma^2_w)$.
- Between seasons: $\theta_{s+1}=\beta_s\theta_s+\eta$ (regression to the mean, with $\beta_s<1$).
- Team-specific home advantages $\alpha$; fitted by MCMC.
- They report predictive accuracy comparable to the Las Vegas line, without beating it.
- Reference: Glickman, M.E. & Stern, H.S. (1998) "A state-space model for National Football League scores", *JASA* 93(441):25–35. https://doi.org/10.1080/01621459.1998.10474084 [not fetched; summary from standard knowledge, **comparison-to-line claim unverified**]
- A Kalman filter gives the Gaussian closed-form equivalent.

**Pi-ratings (Constantinou & Fenton 2013):**
- Each team has separate home and away ratings. Expected goal difference uses $\hat g = b^{|R|/c}-1$ (sign of R), with $b=10$ and $c=3$.
- Error $e=|g_{obs}-\hat g_D|$, weighted as $\psi(e)=c\log_{10}(1+e)$.
- Update at the venue played: $R'_{venue}=R+\psi\lambda$.
- Cross-update of the other venue's rating: $\Delta\cdot\gamma$.
- Defaults: λ = 0.035 and γ = 0.7, chosen by minimising goal-difference error over five EPL seasons.
- Later fit: λ = 0.054 and γ = 0.79 by minimising RPS across leagues (2018 study).
- Reference: Constantinou, A.C. & Fenton, N.E. (2013) "Determining the level of ability of football teams by dynamic ratings based on the relative discrepancies in scores between adversaries", *JQAS* 9(1):37–50. DOI 10.1515/jqas-2012-0036.
- Sources: https://cran.r-project.org/web/packages/piratings/refman/piratings.html ; https://arxiv.org/pdf/2003.09384

**Bradley-Terry-Elo unification:** Elo can be viewed as online SGD on a Bradley-Terry likelihood. — Király & Qian (2017) https://arxiv.org/pdf/1701.08055

### Inferences
- Elo's K corresponds to a fixed Kalman gain. Glicko, TrueSkill and Glickman-Stern adapt the gain to uncertainty, which matters early in a season and after roster shocks such as QB changes.
- MOV multipliers need the autocorrelation correction (538's 2.2/(0.001Δ+2.2)). Without it, favourites' ratings inflate.
- Pi-ratings are the strongest pure-goals rating feature for ML in soccer (see §4).

### Gaps
- Could not fetch FiveThirtyEight's current NFL/CFB methodology page (domain redirected to ABC News). The QB adjustment value and the Elo/25 spread conversion need confirmation from an archived copy (web.archive.org).

---

## 3. American football: margin distributions, key numbers, spread↔probability, alt spreads, totals, halves/quarters, spread–total correlation, CFB differences

### Takeaway
Stern's normal model, margin ~ N(spread, ~13.9), still anchors pregame win probability. Recent SD estimates are about 13.5. Because NFL margins cluster heavily on 3 and 7 (and on 6, 10, 4 and 14), a pure normal mis-prices alternate spreads and half-points near key numbers. Practitioners use empirical, spread-conditional discrete tables or smoothed versions of them. In CFB the unconditional margin SD is about 21 points, and the spread-conditional SD is about 15.

### Cited Findings

**Stern (1991):** The NFL margin relative to the line is approximately $N(0,13.86^2)$, estimated from the 1981, 1983 and 1984 seasons. So
$$P(\text{fav wins})=\Phi(s/\sigma),\qquad P(\text{cover } L)=1-\Phi\big((L+0.5-s)/\sigma\big)\ \text{(discrete adj.)}.$$
- Reference: Stern, H. (1991) "On the probability of winning a football game", *The American Statistician* 45(3):179–183. https://doi.org/10.1080/00031305.1991.10475798
- Later data: the 1978–2012 SD is 13.45 — https://www.footballperspective.com/the-2013-playoffs-were-not-very-random/ (via search snippet).
- "More recent values of the standard deviation are 13.5 points." — Sides et al. 2022 https://arxiv.org/pdf/2212.08116
- **Citation conflict:** some web sources attribute the result to a 1986 Stern paper or a 1992 JSM talk. The peer-reviewed reference is the 1991 *American Statistician* article. — https://arxiv.org/pdf/2212.08116 cites Stern (1991).
- **Weakness:** Stern's model treats a 5-point favourite winning by exactly 5 as being as likely as a 7-point favourite winning by exactly 7. Margins of 5 are actually much rarer than 7. The continuous normal also ignores discreteness. Winston's fix uses $P(a-0.5\le M\le b+0.5)$. — https://arxiv.org/pdf/2212.08116
- Example: PFR's pregame win-probability model uses Vegas line + normal SD (~13.45). — https://www.pro-football-reference.com/about/win_prob.htm (search snippet)

**Key numbers (NFL margins):**
- 3 is the most common margin, at about 14.8% of games. One source gives this for 2003 onward; ESPN gives it for the post-2015 period, so the sources disagree on the sample window.
- 7 is next, at about 9% (ESPN) or 8.7% (older decade sample).
- Sources: https://www.espn.com/chalk/story/_/id/34706289/nfl-betting-cheat-sheet-why-three-magic-number-week-4 ; https://www.actionnetwork.com/nfl/nfl-key-betting-numbers-spread-margins-of-victory-line-value
- 2003–2020 order: 3 > 7 > 6 > 10. After the 2015 PAT move (kick from the 15), 6-point margins rose from 5.53% to 8.09%. — https://www.actionnetwork.com/nfl/nfl-betting-tips-odds-rule-changes-margin-victory-spread
- Six- and eight-point games rose about 2.4% in 2015–2023 vs 2006–2014, and five-point games rose about 1.4%. — https://www.covers.com/nfl/key-numbers
- Since 1922, margins of 3, 7, 10, 4, 6 and 14 together account for 42.5% of results. — https://www.eldo.co/despite-its-weird-scores-2015-had-the-most-normal-margins-of-victory-in-nfl-history.html
- Raw margin tables: https://walterfootball.com/nflmargins.php

**Totals distribution (NFL) and key totals.** Covers table of share of games by total points, 2004–2013 → 2014–2023:

| Total | Share 2004–2013 → 2014–2023 |
|---|---|
| 37 | 3.8% → 3.6% |
| 40 | 3.5% → 3.7% |
| 41 | 3.9% → 3.5% |
| 43 | 3.7% → 3.2% |
| 44 | 4.1% → 3.7% |
| 47 | 3.2% → 3.1% |
| 51 | 3.6% → 3.9% |
| 60+ | 12.9% → 15.8% |
| <35 | 26.8% → 22.1% |

- Key ranges are 36–37, 39–41, 43–51 and 54–55. The most frequent single totals occur in only about 4% of games, much flatter than margins. — https://www.covers.com/nfl/key-numbers

**Spread → probability: normal vs empirical.** Sides, Harvill & Sides (2022) build a CFB method that combines the normal with the empirical frequency of each exact margin, to answer questions like "model says 7.9, should I take −7?" They provide a public online tool. — https://arxiv.org/pdf/2212.08116
- Standard practitioner method **[inference / practice]**: $P(M=k\mid s)$ comes from a smoothed empirical table (kernel-smoothing over nearby spreads, or a normal × key-number reweighting).
- An alternate-spread or half-point price is then $P(M>L)$ summed over discrete k.
- The value of a half-point equals $P(M=k)$ at the integer crossed. It is largest at 3 and 7 for typical spreads.
- Buying off 3 is worth roughly ~8–10% probability mass for spreads near 3 **[unverified, rule-of-thumb]**.

**CFB differences.**
- 2021 season: unconditional SD of score differential = 21.01. For games with similar spreads, the conditional SD = 15.35. Common practice uses N(spread, 15).
- Example: for 82 games with spread 6–7 in 2021, only 3 (3.7%) fell outside ±2σ.
- CFB home-field advantage is about 2–2.5 points (SP+ context).
- Source: https://arxiv.org/pdf/2212.08116
- Key numbers are weaker in CFB because spreads are larger and more varied, and OT and 2-pt rules differ [inference].

**Halves and quarters.**
- First-half spreads are "almost always more than 50%" of the full-game spread. Example: a full-game favourite of 5.5 can share a 1H number with a 3.5 favourite. — https://www.pff.com/news/bet-optimizing-spread-bets-with-first-half-lines
- A betting blog claims 1H lines are about 55–60% of the full-game spread and total. Its example maps −7 to about −4, and a total of 47 to about 25.5–26 (≈ 54–55%). It says second halves "produce slightly more points", which contradicts a >50% 1H total share. — https://www.deucescracked.com/blog/nfl-first-half-halftime-betting-strategy (low-quality source; treat with caution)
- **[Inference]:** The 1H share of the spread exceeds 50% because favourites build leads and then play conservatively (game-script compression of the 2H margin). The 1H/2H total split is close to 50/50 but varies with 2-minute-drill and end-of-half scoring.

**Spread–total correlation (SGP).**
- CFB 2005–2015: when favourites cover, games are more likely to go over. This justified books restricting fav+over parlays. — "Correlated parlay betting", UWF https://ircommons.uwf.edu/esploro/outputs/journalArticle/Correlated-parlay-betting/99380090298406600
- SGP pricing example: a two-leg correlated SGP paid +137 vs +264 at independent prices, and the negatively correlated version paid +472. — https://juicereel.beehiiv.com/p/the-dangers-of-same-game-parlays
- **[Inference]:** The correlation is strongest when the spread is large relative to the total (a big favourite's points are a large share of the total). Sum and difference of two team scores are only uncorrelated if the team-score variances are equal.

### Inferences
- Team totals: let $T$ = total and $s$ = spread (home favoured by $s$). The implied means are $\mu_{fav}=(T+s)/2$ and $\mu_{dog}=(T-s)/2$. In practice team-total distributions are also lumpy (multiples of 3 and 7: 10, 13, 14, 17, 20, 21, 24, 27, 28, 31).
- A coherent derivative-pricing engine for NFL simulates the joint (home, away) score distribution, either by drive/possession simulation or by a bivariate discrete model calibrated to the market spread and total. All derivatives (alt lines, team totals, halves, SGPs) are then priced from that one joint distribution. This mirrors the soccer score-matrix approach.

### Gaps
- No exact, up-to-date (2015–2025) NFL margin frequency table was fetched. Frequencies for 3 and 7 conflict on the sample window (2003+ vs post-2015).
- No published NFL quarter-by-quarter share of spread/total was found (Q1/Q2/Q3/Q4 ratios) in this session's sources.
- No published NFL spread–total correlation coefficient was found.

---

## 4. Machine learning vs structural models

### Takeaway
In the 2017 Soccer Prediction Challenge (goals-only data, 200k+ matches, RPS scoring), the winner was gradient-boosted trees on hand-built rating features (pi-ratings, PageRank) by Hubáček et al. The organisers' post-challenge XGBoost on rating features scored about RPS 0.2054. ML wins when it consumes well-engineered structural features such as ratings. It does not win on raw data. Against the betting market, models are only profitable when decorrelated from the bookmaker and selected on calibration rather than accuracy.

### Cited Findings
- Hubáček, Šourek & Železný won the 2017 Soccer Prediction Challenge (run with the *Machine Learning* journal special issue). Their best model was **gradient-boosted trees on manually constructed features**, including pi-ratings and a PageRank-based rating as latent variables. They also discuss whether monotone probabilities across ordinal outcomes are a valid assumption for RPS. — Hubáček, O., Šourek, G. & Železný, F. (2019) "Learning to predict soccer results from relational data with gradient boosted trees", *Machine Learning* 108(1):29–47. https://ida.fel.cvut.cz/papers/hubacek2019learning.html ; https://cs.fel.cvut.cz/en/news/detail/1302
- Challenge set-up: predict future matches across many world leagues from a training set of >200,000 past results (goals only). — https://ida.fel.cvut.cz/papers/hubacek2019learning.html
- Berrar, Lopes & Dubitzky (organisers, so their entry was not eligible to win):
  - "Recency feature" and "rating feature" learning sets.
  - The top-ranking model was **k-NN on the rating feature set**.
  - An XGBoost ensemble slightly improved on it after the challenge, reportedly accuracy 0.5194 and RPS 0.2054. That figure comes via a secondary source and was not confirmed in the original paper.
  - Reference: *Machine Learning* 108:97–126 (2019), DOI 10.1007/s10994-018-5747-8. https://mlanthology.org/mlj/2019/berrar2019mlj-incorporating ; https://arxiv.org/pdf/2403.07669
- Review (Bunker, Yeung & Fujii 2024): gradient-boosted trees such as CatBoost on soccer-specific ratings like pi-ratings perform best when goals are the only features. Deep learning and RF need more thorough comparison. — https://arxiv.org/abs/2403.07669
- Walsh & Joshi (2024): on NBA data, selecting models by **calibration** rather than accuracy gave average ROI +34.69% vs −35.17%, and best case +36.93% vs +5.56%. This is one betting season, so the sample is small. — *Machine Learning with Applications* 16:100539. https://researchportal.bath.ac.uk/en/publications/machine-learning-for-sports-betting-should-model-selection-be-bas/
- Systematic review of ML in sports betting (2024). — https://arxiv.org/pdf/2410.21484
- Related, not fetched: Hubáček, Šourek & Železný (2019) "Exploiting sports-betting market using machine learning", *IJF* 35(2):783–796. It proposes training with a penalty on correlation with bookmaker probabilities, so the model finds bets where it disagrees with the market. https://doi.org/10.1016/j.ijforecast.2019.01.001

### Inferences
- ML loses when:
  - the feature set is just raw recent results, where ratings/DC already compress the signal;
  - samples are small (NFL: ~272 games/season);
  - the models are tuned on accuracy or log-loss in-sample without temporal CV.
- ML wins when:
  - it can add heterogeneous information (injuries, lineups, weather, tracking/xG) on top of structural features;
  - the target is a derivative market where structural independence assumptions break.
- Recommended architecture: structural model (DC/Elo/state-space) → features (rating diffs, λ/μ, market-implied probs) → GBM → calibration layer.

### Gaps
- I could not confirm the exact RPS scores of the 2017 challenge winner or the full leaderboard from primary sources. A winning RPS of about 0.2063 is commonly cited **[unverified]**.
- No equivalent public NFL/CFB ML-vs-structural benchmark competition was found.

---

## 5. Calibration and combining with the market

### Takeaway
Post-hoc calibration includes Platt/logistic, isotonic and beta calibration. Shrinkage toward devigged market probabilities, ideally fitted as a logistic blend on held-out data, is usually worth more than model complexity, because closing lines are hard to beat. Model selection should target calibration and proper scores (log-loss, Brier, RPS), not accuracy.

### Cited Findings
- Calibration-based model selection is associated with large ROI differences in NBA betting (see §4). — https://researchportal.bath.ac.uk/en/publications/machine-learning-for-sports-betting-should-model-selection-be-bas/
- **Platt scaling:** $p=\sigma(a f+b)$, fitted on a held-out set. — Platt, J. (1999) "Probabilistic outputs for SVMs…", in *Advances in Large Margin Classifiers*. [reference, not fetched]
- **Isotonic regression:** non-parametric monotone mapping via PAV. It needs more data and overfits on small sets. — Zadrozny, B. & Elkan, C. (2002) KDD. [reference, not fetched]
- **Beta calibration:** $p=1/\big(1+1/(e^{c}\,s^{a}/(1-s)^{b})\big)$, i.e. logit $p = a\ln s - b\ln(1-s)+c$. It nests the identity and suits tree/NB outputs better than Platt. — Kull, M., Silva Filho, T. & Flach, P. (2017) "Beta calibration", AISTATS, PMLR 54:623–631. http://proceedings.mlr.press/v54/kull17a.html [not fetched]
- **Market shrinkage / stacking [standard practice; inference]:** $\text{logit}\,p^*=w_0+w_1\,\text{logit}\,p_{model}+w_2\,\text{logit}\,p_{market}$, fitted by logistic regression on out-of-sample predictions. Here $p_{market}$ is devigged (multiplicative, Shin, or power method). $w_1/(w_1+w_2)$ estimates how much independent information the model adds; edge exists only where the blend departs from the market.
- Decorrelation from bookmakers as a training objective. — Hubáček et al. (2019) *IJF* 35(2):783–796 (see §4).

### Inferences
- Use a time-ordered calibration set, not random CV, because team strengths drift.
- For multi-class soccer (1X2), calibrate ordinally (e.g. on the cumulative logits) or with a Dirichlet calibration. Calibrating each class independently breaks the probabilities' sum-to-one and RPS monotonicity.
- For spreads and totals, calibrate the σ of the margin or total distribution (e.g. 13.5 NFL, 15 CFB conditional) as a parameter, rather than calibrating each alt line separately. This keeps all derivatives consistent.

### Gaps
- Not fetched: empirical comparisons of Platt vs isotonic vs beta specifically on sports-betting data, and devig method comparisons (Buchdahl, Pinnacle articles, Clarke et al. 2017 on the Shin and power methods). These belong to an adjacent research track.
