# OSF Pre-registration — Ze-AL v4 Simulation Stage-0

**Date locked:** 2026-05-09 (before any experiment run)
**Author:** J. Tkemaladze (Georgia Longevity Alliance)
**Conflict of Interest:** Author is developer of the Ze-AL formalism — disclosed.

## 1. Background and prior work

This simulation is the v4 follow-up to `Ze-Allostasis-v3.md`, which reported a
pre-registered negative finding: the σ_E(t)-normalised Ze-AL formula
(`Ze(t) = |R(t)−E(t)|/σ_E(t)`) underperformed a 24-hour moving-average residual
baseline (r=0.39 vs r=0.59) and exhibited sign reversal under a 50%-shortened
GP length-scale (r=−0.41).

We hypothesised in the v3 Discussion that σ_E(t) cancels the very signal
allostatic load is supposed to capture, because GP predictive uncertainty
inflates during stressor events. v4 tests three corrections.

## 2. Hypotheses (locked)

**H1** (σ_calib correction). v4 univariate `|R(t)−E(t)|/σ_calib`, where
σ_calib is the frozen residual SD on the calibration window, will
yield Pearson r ≥ 0.55 with ground-truth burden under the primary
correctly-specified condition.

**H2** (multivariate Mahalanobis). v4 Mahalanobis
`(R(t)−E(t))^T Σ_calib^{-1} (R(t)−E(t))` using the cross-channel
calibration covariance will achieve **r ≥ 0.65** under primary.

**H3** (KL surprise add-on). Adding a Bayesian KL surprise term will
yield **r ≥ 0.65** under primary AND additional positive value under
≥1 sensitivity condition.

**H4** (sign-reversal elimination). Under length-scale −50%, v4 Mahalanobis
and v4 VFE will retain r > 0 (in contrast to v3's r=−0.41).

## 3. Design

- Multivariate 5-channel accelerometric simulator
- 4 scenarios × 50 subjects (n=200)
- 90 days × 24 hourly samples
- Stressors are coherent (couple to all 5 channels with channel-specific signs)
- Baseline: 24h + 7d periodic per channel
- Pre-registered seed: **20260509**

## 4. Estimators

1. Traditional AL proxy (univariate quartile exceedance)
2. MA-residual baseline (24h MA, frozen σ_baseline)
3. v3 σ_E (univariate `|R−E|/σ_E(t)`)
4. v4 σ_calib (univariate `|R−E|/σ_calib`)
5. **v4 Mahalanobis (multivariate)** — primary
6. **v4 VFE (Mahalanobis + KL surprise)** — primary

## 5. Sensitivity conditions (locked)

1. Primary (correctly specified GP)
2. Length-scale −50% (RBF length-scale forced to half optimum)
3. Length-scale +50% (forced to 1.5× optimum)
4. No-circadian kernel (RBF only, omits 24h periodic)
5. Noise σ × 3 (observation noise inflated 3× baseline)

## 6. Statistical analysis

- Pearson r between estimator output and ground-truth burden
- 95% bootstrap CI (2000 iterations, percentile)
- No p-value adjustment (descriptive simulation)
- All numbers reported to 3 decimal places

## 7. Pre-committed decision rules

| Outcome | Action |
|---|---|
| H2 satisfied (r ≥ 0.65 primary) AND H4 (no sign reversal) | Submit manuscript to NPJ Digital Medicine |
| H2 satisfied but H4 fails | Submit with explicit "robustness limitation" section |
| H2 fails (r < 0.65 primary) but r > MA-baseline | Submit to PLOS ONE as methodology paper with honest framing |
| H2 fails AND r < MA-baseline | KILL — repeat v3 conclusion; concept C path aborted |

## 8. Deviations clause

Any deviation from this protocol (e.g., post-hoc estimator additions,
alternative scenarios) will be documented as exploratory and reported
separately from the pre-registered analysis.

## 9. Code and data availability

Public GitHub repository upon submission. Deterministic with seed=20260509.
All scripts in `src/`, full result JSON in `results/`.

## 10. Conflict of Interest

J. Tkemaladze (Georgia Longevity Alliance) is the developer of the Ze-AL
formalism. This is disclosed in the manuscript. Code and data are public;
any third party can reproduce identically.
