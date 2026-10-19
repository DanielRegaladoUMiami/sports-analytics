# Market Microstructure & Execution for Sports Betting via Prediction Markets and Sportsbooks (as of Oct 2026)

> Research date: 2026-10-18. Official Kalshi fee-schedule PDF (kalshi.com/docs/kalshi-fee-schedule.pdf) returned HTTP 429 during research, so Kalshi fee details rely on Kalshi's help center + API docs and on dated third-party explainers that quote the PDF. Formulas labelled "(derived)" are my own arithmetic built on cited inputs.

## 1. Kalshi: fees, contract structure, order book, API, effective probability

### Takeaway
Kalshi charges a quadratic, price-dependent taker fee `ceil(M × 0.07 × C × P × (1−P))`, rounded up to the next cent per fill, peaking at 1.75¢/contract at 50¢. Maker fees (0.0175 coefficient) apply only to series flagged for them, and some sports series carry a 0.5 multiplier. The order book lists only bids, and asks are implied as 1 − opposite bid. The break-even probability for a taker buy is the ask plus the per-contract fee.

### Cited Findings
- Kalshi charges "a transaction fee on the expected earnings on a contract". Some markets, "often for special events such as elections, awards ceremonies, or major sporting championships", carry different fees. Maker fees apply in "some cases" to resting orders, are charged only on execution, and cancelling costs nothing. Full math is in the Fee Schedule PDF. — [Kalshi Help Center: Fees](https://help.kalshi.com/trading/fees)
- Taker fee = round up(M × 0.07 × C × P × (1−P)). Maker fee = round up(M_maker × 0.0175 × C × P × (1−P)). C = contracts, P = price in $, M = series multiplier (default 1, 0 for fee-free series). M_maker defaults to 0, so makers on standard series pay nothing. Maker fees apply only to series the API flags `quadratic_with_maker_fees`. KXMVE combo (multi-leg / parlay-style) markets have maker multiplier 2. "The public series API reports 0.5 on some sports series", for example a group of KXMLB series. The page documents a schedule effective 2026-07-07 with ten fee-free series. It also warns that Kalshi can change multipliers without republishing the PDF. (Last reviewed 2026-09-12; constants verified 2026-09-03.) — [PolyKal: Kalshi Fees Explained](https://polykal.net/kalshi-fees-explained/)
- Rounding is up to the next whole cent, applied per fill. A fill that walks several price levels is rounded separately at each level, which can exceed whole-order rounding by up to 1¢ per extra level. — [PolyKal](https://polykal.net/kalshi-fees-explained/)
- Per-contract fee by price (taker / maker): 10¢ 0.63¢/0.16¢; 20¢ 1.12¢; 30¢ 1.47¢/0.37¢; 40¢ 1.68¢; 50¢ 1.75¢/0.44¢; symmetric above 50¢. No settlement fee. No ACH or wire deposit fee. The page says the same formula applies to every category, which conflicts with PolyKal's report of 0.5 sports multipliers. Its case study: a 50,000-contract taker order paid $598 in fees with ~0.11¢ slippage, versus $155 when routed as a maker. (Updated 2026-08-09.) — [River Markets: Kalshi fees](https://www.rivermarkets.com/insights/kalshi-fees.html)
- Kalshi's own example quoted by a third party: 100 contracts at $0.55 cost $1.74 in fees. Check: 0.07×100×0.55×0.45 = 1.7325 → ceil = $1.74. — [pm.wiki: arbitrage after fees](https://pm.wiki/vi/learn/prediction-market-arbitrage-after-fees)
- The original 2022 CFTC-filed Kalshi fee schedule exists, but it predates the 2026 maker-fee and multiplier changes. — [CFTC filing: Kalshi Fee Schedule (2022)](https://www.cftc.gov/sites/default/files/filings/orgrules/22/09/rule091222kexdcm003.pdf)
- **Order book (API):** "Kalshi's orderbook only returns bids, not asks." The response has `orderbook_fp.yes_dollars` and `no_dollars` arrays of `[price_dollars, count_fp]` string pairs, e.g. `["0.4200","13.00"]`. Strings are used because the book supports sub-penny prices and fractional contract sizes. Arrays are sorted ascending, so the best bid is the last element. YES ask = 1.00 − best NO bid, and NO ask = 1.00 − best YES bid. In the doc's example, a NO bid at $0.56 implies a YES ask of $0.44, and against a $0.42 YES bid the spread is 2¢. — [Kalshi API docs: Orderbook responses](https://docs.kalshi.com/getting_started/orderbook_responses)
- Contracts pay $1 if YES, $0 otherwise. Kalshi runs a central limit order book, so large orders walk through price levels. — [Blockworks Research](https://app.blockworksresearch.com/research/from-betting-to-trading-how-kalshi-is-reshaping-sports-markets); [SailGP prediction-markets guide: slippage](https://sailgp.com/prediction-markets/guide/what-does-slippage-mean)

### Formulas (derived)
- **Taker buy of YES at ask `a`, size C:** fee per contract `f = ceil(M·0.07·C·a(1−a))/C`. Break-even probability `p* = a + f`. EV per contract = `p_model − a − f`.
- **Maker buy at bid `b`:** `p* = b + ceil(M_maker·0.0175·C·b(1−b))/C`. On most series M_maker = 0, so `p* = b`.
- **Selling / buying NO:** buying NO at `1 − bid_YES` is the mirror image, with the same fee formula on the NO price, and P(1−P) is symmetric.
- **Small-lot rounding penalty:** with 1 contract at 50¢, 0.0175 → ceil = $0.02, which is 2¢ (4% of notional) versus 1.75¢ theoretical. With 100 contracts it is $1.75 exactly. **Trade in lots of 100 or more, or as a maker.**
- **Mid-market "fair" from the Kalshi book:** `mid = (best_YES_bid + (1 − best_NO_bid))/2`. Half-spread + taker fee is the round-trip cost of crossing.
- **Example:** a game at mid 50¢ with a 1¢ spread. Taker YES ask = 51¢ and fee = 1.75¢, so `p* ≈ 52.75%`. That is slightly worse than a −110 sportsbook side (52.38%). A maker bid at 50¢ on a no-maker-fee series gives `p* = 50%`, if filled.

### Inferences
- On a zero-maker-fee series, Kalshi as a maker is the cheapest US execution venue for sports. As a taker near 50¢ it is comparable to or worse than −110 once the spread is included. Fees fall toward the tails (0.63¢ at 10¢/90¢), so favourites and longshots are cheap to trade in fee terms.
- Because M varies by series (1, 0.5, 0) and can change silently, a production pipeline should read the fee type and multiplier from the series endpoint of the API at trade time rather than hard-coding 0.07.

### Gaps
- Could not retrieve the official fee PDF (429), so I could not verify which sports series (KXNFL*, KXNCAAF*, totals ladders, player props) currently carry M = 0.5 or maker fees. Only the KXMLB example is sourced.
- Position limits for sports contracts and the exact list of KXNFL/KXNCAAF series tickers (spread, total ladder, props) were not covered by the sources retrieved.
- No source found for withdrawal fees.

## 2. Polymarket (international + Polymarket US): fees, CLOB, rebates

### Takeaway
Polymarket is no longer zero-fee. Since 2026 takers pay `C × feeRate × p(1−p)` by category, with sports at 0.05 (0.03 for NFL/CFB game markets from Oct 2026). Makers pay 0 and earn a share of taker fees as daily rebates (15% for sports). Polymarket US (CFTC-regulated, via the QCEX acquisition) uses the same quadratic form, with sports at 5% from 2026-07-01.

### Cited Findings
- Fee formula `fee_equivalent = C × feeRate × p × (1−p)`. Category taker rates: Sports 0.05, Crypto 0.07, Finance/Politics/Mentions/Tech 0.04, Econ/Culture/Weather/Other 0.05, Geopolitics 0. Maker fee is 0 in every category. Maker rebate share: Sports 15%, Crypto 20%, others 25%. Rebate = (your fee-equivalent / total fee-equivalent) × pool, computed per market and paid daily in pUSD with a $1 minimum. Fees are rounded to 5 decimals, and rebate % is "at the sole discretion of Polymarket". — [Polymarket Docs: Maker Rebates Program](https://docs.polymarket.com/polymarket-learn/trading/maker-rebates-program)
- Timeline: the sports taker rate rose from 0.03 to 0.05 in July 2026, raising the max from $0.75 to $1.25 per 100 shares at 50¢. In October 2026, NFL and college football *game* markets moved to 0.03; season-long football markets stay at 0.05. Examples: 100 sports shares at $0.50 → $1.25 fee (2.5% of notional); at $0.10 → $0.45. (Updated 2026-10-14.) — [StartPolymarket: Polymarket fees](https://startpolymarket.com/learn/polymarket-fees/)
- Earlier history: on 2026-02-18 Polymarket piloted a market-order (taker) fee in sports, starting with college basketball and Serie A. — [MEXC News](https://www.mexc.com/news/739044); [Pine Analytics: Polymarket Fee Rollout](https://pineanalytics.substack.com/p/polymarket-fee-rollout)
- "Fee Structure V2" took effect on 2026-03-30, with sports at 0.03. — [Sacra: Polymarket](https://www.sacra.com/c/polymarket/); [River Markets](https://www.rivermarkets.com/insights/polymarket-us-fees.html)
- Pine Analytics found no decline in sports volume after fees launched. — [Pine Analytics](https://pineanalytics.substack.com/p/polymarket-fee-rollout)
- **Polymarket US:** Polymarket acquired the CFTC-licensed exchange QCEX in July 2025. It relaunched for US traders in December 2025 and dropped the waitlist in May 2026. It trades in USD with no wallet or stablecoin. Fee schedule effective 2026-07-01: makers 0%; taker by category (Sports 5% → $1.25 per 100 at 50¢; Crypto 7%; Politics/Finance 4%; Geopolitics 0%); weekly rebates for takers above $250k monthly volume. — [River Markets: Polymarket US fees](https://www.rivermarkets.com/insights/polymarket-us-fees.html)

### Formulas (derived)
- Taker buy at ask `a`: `p* = a + r·a(1−a)`, with r = 0.05 (sports) or 0.03 (NFL/CFB game markets since Oct 2026). At a = 0.50: r=0.05 → p* = 51.25%; r=0.03 → 50.75%.
- Maker: `p* = b − rebate`, where rebate ≈ 0.15 × (share of the market's fee pool). Makers break even at their bid price, before any rebate.

### Inferences
- For NFL/CFB game lines, Polymarket's taker cost (≤0.75¢ at 50¢) is now below Kalshi's (1.75¢ at M=1). Category- and date-specific rates move several times a year, so fee logic must be versioned by date.
- Sources disagree on the sports rebate share: StartPolymarket and current docs say 15%, while earlier reports say 25%. This reflects the July 2026 change.

### Gaps
- No primary Polymarket announcement retrieved for the Oct 2026 NFL/CFB 0.03 rate (single secondary source).
- No quantitative depth data for Polymarket sports books found (see §4).

## 3. Sportsbooks & exchanges: vig, hold, limiting, sharp-friendly venues

### Takeaway
Straight bets at −110/−110 carry ~4.5% theoretical hold (break-even 52.38%). Realized US hold rose to ~10% in 2025, driven by parlays and SGPs (parlay hold ~18–23%). Winning bettors get limited; Massachusetts data show only 0.64% of accounts limited, but limits correlate with winning. New York's anti-limiting bill (A9125) is still pending. Low-cost alternatives are peer-to-peer exchanges: ProphetX (1–2% commission on net winnings), Novig (commission-free), and Betfair (2/5/8% packages plus an Expert Fee).

### Cited Findings
- US implied national hold ≈10.2% in 2025, up from 9.2% in 2024, attributed to parlays, SGPs and in-play. — [Legal Sports Report](https://www.legalsportsreport.com/263300/sportsbooks-make-more-money-from-slower-sports-betting-growth-in-2025/)
- In six states that report parlays (May–Aug), parlay hold rose from 18.35% (2024) to 22.59% (2025), and parlays' share of operator winnings went from 51.8% to 59.8%. Colorado parlay hold was 20.4% over four months to Aug 2025. — [Ingame](https://www.ingame.com/?p=40653)
- Record 12.4% hold in June 2025. — [Covers](https://www.covers.com/industry/us-sportsbooks-post-record-hold-in-june-2025)
- SGPs and multi-leg parlays "routinely hold 15–30%", versus a 4–5% theoretical hold on straight bets. — [Deuces Cracked: Q2 2026 handle/hold](https://www.deucescracked.com/blog/us-sports-betting-q2-2026-handle-hold-data)
- **Limiting, Massachusetts:** the MGC hired an analyst to review account-level operator data. 0.64% of accounts were limited as of December 2024. "Bettors who consistently won were more likely to have their betting limits lowered" and less likely to be in VIP programs. Many were limited without notice. — [Covers (Apr 2025)](https://www.covers.com/industry/massachusetts-limiting-vip-programs-sports-betting-data-april-2025)
- The MGC moved to require operators to notify limited bettors (Sept–Oct 2025). — [SBC Americas](https://sbcamericas.com/2025/09/30/mgc-data-limiting-bettors-ma/); [CasinoBeats](https://casinobeats.com/2025/10/01/massachusetts-gaming-commission-sportsbooks-notify-bettors-limited/)
- MA regulators discussed exchanges and prediction markets as an outlet for limited sharps ("the box"). — [Covers (Sept 2025)](https://www.covers.com/industry/massachusetts-limiting-sports-betting-prediction-markets-exchanges-sharps-box-september-2025)
- **New York:** Assemblymember Alex Bores' A9125 "Fair Play Act" would bar operators from limiting wagers or deposits because a bettor wins. It keeps exceptions for suspicious activity and problem gambling, and requires electronic notice within 24h stating the reason and duration. It was referred to the Racing & Wagering Committee in fall 2025 and was still pending as of June 2026. The search found no NY Attorney General action; the activity is legislative. DraftKings (FY2023 10-K): "it is customary for sports betting operators to manage customer betting limits at the individual level". — [Covers (Oct 2025)](https://www.covers.com/industry/new-york-legislation-looks-to-prohibit-sportsbooks-from-limiting-bettors-oct-1-2025); [WSN](https://www.wsn.com/betting/new-york-is-considering-a-bill-to-end-limits-on-sports-bettors/)
- **UK comparison:** a UK Gambling Commission review of ~15M accounts found 48% of limited account holders had been profitable over their account lifetime. — [SBC Americas (Jul 2025)](https://sbcamericas.com/2025/07/25/uk-regulator-sports-betting-limits/)
- **ProphetX** (CFTC-approved prediction exchange in 2025–26): commission of up to 1–2% on net winnings per market. Some sources say 0% on props, and the rate may be volume-tiered. No fee on losing or unmatched trades. — [Lines.com](https://www.lines.com/prediction-market/prophetx-review); [Gambling.com](https://www.gambling.com/us/prediction-markets/reviews/prophetx); [DeFi Rate](https://defirate.com/news/prophetx-wins-cftc-approval-sports-focused-prediction-exchange/)
- **Novig** received CFTC approval and is commission-free peer-to-peer; costs come from payment-method fees. — [Legal Sports Report: ProphetX vs Novig (Jun 2026)](https://www.legalsportsreport.com/dfs-sites/prophetx-vs-novig/); [DeFi Rate](https://defirate.com/?p=13815)
- **Sporttrade** (formerly a state-licensed exchange) reportedly told users it had exited its online sports betting markets. — [Legal Sports Report](https://www.legalsportsreport.com/dfs-sites/prophetx-vs-novig/) (thin sourcing)
- **Betfair Exchange:** customers choose 8%, 5% or 2% commission on net winnings depending on package. In 2025 the Premium Charge was replaced by an "Expert Fee" of 20%/40% on rolling 52-week gross profit above £25k. Smarkets charges 2%. — [Sporting Life](https://www.sportinglife.com/free-bets/guides/betfair-exchange-education/how-does-commission-work); [Racing Post](https://racingpost.com/news/britain/betfair-exchange-to-introduce-new-commission-system-for-2025-as-premium-charge-is-dropped-a7wbg0v4GCAJ); [pm.wiki Betfair vs Smarkets](https://pm.wiki/uk/compare/betfair-exchange-vs-smarkets)

### Formulas (derived; standard conversions)
- American odds → implied probability: `q = 100/(odds+100)` for positive odds, `q = |odds|/(|odds|+100)` for negative. −110 gives 0.5238.
- Overround and hold: `O = Σq_i`, so −110/−110 gives O = 1.0476. Theoretical hold = `1 − 1/O` ≈ 4.55%.
- No-vig (multiplicative) fair probability: `p_i = q_i / Σq`. Other methods (additive, Shin, power) handle favourite-longshot bias better on lopsided moneylines.
- Parlay of k legs each with overround O: the effective margin compounds as ~`1 − 1/O^k` (≈ 13% for 3 legs at −110), consistent with observed 15–30% SGP holds.
- Exchange back bet at decimal odds D with commission c on net winnings: `p* = 1 / (1 + (D−1)(1−c))`. For ProphetX/Kalshi-style comparisons, convert everything to break-even probability.

### Inferences
- A model whose edge comes from straight NFL/CFB sides and totals needs >52.4% at −110 sportsbooks but only ≈50.75–52.75% on Polymarket/Kalshi as a taker, and ≈50% as a maker. Exchanges/prediction markets are the structurally better execution venue for a quant bettor, and they do not limit winners. Their binding constraint is liquidity (§4).
- Avoid parlays/SGPs for edge capture: the compounding margin overwhelms almost any per-leg edge.

### Gaps
- No reliable source found on the *speed* of limiting (bets or days until a winner is limited).
- No verified Pinnacle margin or Circa limit figures retrieved. Pinnacle is not licensed in US states.
- No retrieved data on prop-specific hold.

## 4. Liquidity, depth, slippage, maker vs. taker

### Takeaway
Hard depth data are scarce. Kalshi traded $441M in NFL week 1 of 2025 and relies heavily on market makers, so quoted prices can worsen with size. Analysts found Kalshi ML and totals 10–25% more expensive than DraftKings on one date (Sept 2025). In-game liquidity is thin. Maker execution saves large fees (River Markets case: $598 taker vs $155 maker on 50k contracts) but carries adverse-selection risk.

### Cited Findings
- Kalshi had $441M in volume in NFL week 1 (2025), nearly $200M on Sunday. Critic Matt Kalish argued Kalshi has less liquidity and leans on market makers, showing odds differing by bet size. One analyst found ML and total prices 10–25% more expensive than DraftKings and 16–23% more than FanDuel on Sept 5, 2025. A former Kalshi operations head: "We'd all prefer less slippage, but that's not how markets work." — [Yogonet (Sept 2025)](https://www.yogonet.com/international/news/2025/09/09/115258-kalshi-trading-hits-441m-in-first-nfl-week-but-analysts-flag-pricing-gap-with-sportsbooks); [Sigma](https://sigma.world/news/kalshi-nfl-trading-record-nfl/)
- Blockworks analysis of 3.1K Kalshi games ($8.5B notional): prices converge toward outcomes before games. Thin in-game liquidity leaves few intervals where arbitrage is possible and pushes larger bettors toward sportsbooks. — [Blockworks Research](https://app.blockworksresearch.com/research/from-betting-to-trading-how-kalshi-is-reshaping-sports-markets)
- 50,000-contract Kalshi taker execution: $598 fees, ~0.11¢ slippage. Maker-routed: $155. — [River Markets](https://www.rivermarkets.com/insights/kalshi-fees.html)
- A vendor test reports 1–3% average slippage for mid-sized trades on *DraftKings Predictions* (not Kalshi; unverified methodology). — [ats.io](https://ats.io/prediction-markets/draftkings-predictions/liquidity/)

### Inferences
- Practical execution rule: compute VWAP over book levels for the intended size, add the per-fill rounded fee, and compare `p*_VWAP` with the model probability. Do not use top-of-book.
- Maker strategy: rest limit orders slightly inside the no-vig sportsbook consensus. The risk is being picked off when injury, lineup or weather news hits, because resting orders are filled exactly when the price is stale. Mitigations: cancel on news feeds, avoid resting through inactive and lineup announcements, and widen quotes near kickoff. (General microstructure reasoning, not sourced to a sports-specific study.)

### Gaps
- No systematic public data found on top-of-book size for Kalshi or Polymarket NFL/CFB spreads, totals ladders or props. This would need to be measured directly via the API (snapshotting `orderbook_fp`).

## 5. Timing: opening vs closing lines, information arrival

### Takeaway
Academic evidence says NFL closing lines are not significantly more predictive than openers; only ~10% of games move ≥2 points. Exploitable inefficiencies exist in pockets (moneylines, situational spots, sentiment), but they are inconsistent and largely shrink after vig. Closing-line value remains the standard benchmark of skill. I found no rigorous evidence specifically for "bet early in the week" in NFL/CFB.

### Cited Findings
- NFL opening vs closing lines: no statistically significant difference in predictive value. Lines moved ≥2 points in ~10% of games, with no consistent pattern. — [arXiv 1211.4000](https://arxiv.org/pdf/1211.4000)
- Opening lines offered profitable bets against teams that had clinched playoff spots. Closing lines partly adjusted, shrinking most of the edge below the commission, except against teams that had clinched top seeds. — [Financial Services Review: Anchoring, affect, and efficiency…](https://openjournals.libs.uga.edu/fsr/article/view/3242)
- NFL moneyline inefficiencies (2007–2016) exist in both opening and closing lines, vary by season, and are hard to predict. — [Journal of Economic Insight](https://journalofeconomicinsight.com/index.php/joei/article/view/1335)
- An intra-week study of bookie lines found information content rising through the week (efficient), with some sentiment-related inefficiencies. — [IDEAS/RePEc](https://ideas.repec.org/a/mve/journl/v50y2024i2p87-117.html)
- Blockworks: Kalshi prices converge toward outcomes before games. — [Blockworks Research](https://app.blockworksresearch.com/research/from-betting-to-trading-how-kalshi-is-reshaping-sports-markets)

### Inferences
- Since prediction-market sports prices track sportsbook consensus, the most beatable window is when (a) a model incorporates information before the market, or (b) prediction-market books lag sportsbook steam moves. Backtests should record CLV against the sportsbook no-vig close, not only P&L.

### Gaps
- No peer-reviewed 2024–2026 evidence on early-week vs late betting for NFL/CFB or soccer. A dev.to claim (moves >0.5 pt predicting 58–63%) is unverified and excluded.
- No retrieved data on steam-move propagation latency between sportsbooks and Kalshi/Polymarket.

## 6. Cross-venue arbitrage / relative value & regulatory context

### Takeaway
Apparent arbs between Kalshi, Polymarket and sportsbooks are mostly consumed by quadratic fees, per-fill rounding, spread, thin depth and capital lockup. The robust use of sportsbooks is as a no-vig "fair price" reference for buying mispriced prediction-market contracts. Regulatory status is unsettled: the CFTC backs federal preemption (Jan 2026), while states litigate, with a federal appeals ruling for Kalshi in NJ and a state injunction against it in MA.

### Cited Findings
- Arbitrage must be computed after fees; a combined-cost example uses the per-venue quadratic fees. — [pm.wiki: prediction market arbitrage after fees](https://pm.wiki/vi/learn/prediction-market-arbitrage-after-fees)
- Thin in-game liquidity leaves few arbitrage intervals. — [Blockworks Research](https://app.blockworksresearch.com/research/from-betting-to-trading-how-kalshi-is-reshaping-sports-markets)
- Kalshi priced 10–25% more expensively than DraftKings on ML and totals on one date. That is a relative-value gap, not necessarily an arb. — [Yogonet](https://www.yogonet.com/international/news/2025/09/09/115258-kalshi-trading-hits-441m-in-first-nfl-week-but-analysts-flag-pricing-gap-with-sportsbooks)
- **Regulatory (single secondary source, unverified against court orders):**
  - In Jan 2026 the CFTC withdrew its proposed ban on sports event contracts, signalled new rulemaking, and began suing states that issued cease-and-desist orders, asserting exclusive jurisdiction.
  - Massachusetts (Jan 2026): a state court enjoined Kalshi sports contracts for in-state users.
  - Tennessee (Feb 2026): a federal district court granted Kalshi a preliminary injunction.
  - New Jersey (Apr 2026): a federal appeals court upheld Kalshi's injunction, holding its sports contracts are "swaps" under the CEA.
  - Litigation is active in ≥8 states, with cease-and-desist orders from ≥11. All rulings are preliminary, not final.
  - — [pm.wiki: Is Kalshi legal](https://pm.wiki/es/learn/is-kalshi-legal)

### Formulas (derived)
- Two-venue arb (buy YES on A at `a_A`, buy NO on B at `a_B`, same event): profit per pair = `1 − a_A − a_B − f_A(a_A) − f_B(a_B)`, where `f` = venue fee per contract (Kalshi ceil-rounded, Polymarket `r·p(1−p)`, sportsbook vig implicit in odds). It requires identical settlement rules.
- Annualised return must account for lockup: `R_ann ≈ (profit/capital) × 365/days_to_settlement`.
- Relative value: `edge = p_novig_consensus − (a + f(a))`. Bet when edge > threshold (model error + slippage).

### Inferences
- Arbs persist because of:
  - **Fees:** Kalshi 1.75¢ + Polymarket 1.25¢ at 50¢ ≈ 3¢ of round-trip cost.
  - **Rounding** on small lots.
  - **Settlement-rule mismatches:** OT inclusion, push handling (Kalshi binaries cannot push, while a sportsbook total of 47 can), postponements, and void rules.
  - **Capital lockup** until settlement.
  - **Funding frictions:** USDC vs USD, withdrawal times, and state geofencing (e.g. MA).
  - **Sportsbook limiting** of accounts that arb.

### Gaps
- No primary court documents or 2026 mainstream reporting retrieved to verify the regulatory timeline. It should be checked before publication.
- No quantified study of arb frequency or size across Kalshi, Polymarket and sportsbooks.
