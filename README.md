# Ze-AL v4 — Stage 0 Simulation

Pre-registered v4 simulation, derived from the v3 negative-finding paper
(`~/Desktop/Ze-Allostasis-v3.md`).

## Hypothesis (locked before run)

**H1.** Replacing σ_E(t) (online predictive uncertainty) with σ_calib (frozen
calibration-period residual scale) eliminates the self-cancellation that drove
v3 sign reversal.

**H2.** Multivariate Mahalanobis using a calibration covariance Σ_calib
amplifies coherent cross-channel stressor responses.

**H3.** Adding a Bayesian KL surprise term (cost of belief update across
6-hour windows) adds independent predictive signal beyond Mahalanobis alone.

**Pre-registered success threshold (from prior v3 paper):**
- v4 Mahalanobis Pearson r ≥ 0.65 with ground-truth burden under primary condition
- Robust under all 4 sensitivity conditions (no sign reversal)
- Beat MA-residual baseline (v3's adversarial baseline)

## Layout

```
src/
  generator.py       — multivariate (5-channel) accelerometric burden simulator
  estimators.py      — 6 estimators
  run_experiment.py  — primary + 4 sensitivity conditions
  make_figures.py    — fig1-3 PNG generation
  write_manuscript.py — DeepSeek manuscript drafting after results
results/
  summary.json       — per-condition × per-estimator r + bootstrap CI
  raw_rows.json      — per-subject estimator outputs
  experiment.log     — run log
figures/
  fig1_subject.png   — single-subject 5-channel trace
  fig2_correlations.png — bar chart, all conditions × estimators
  fig3_scatter.png   — v4-VFE vs ground-truth scatter, colored by scenario
```

## Reproducibility

- Seed: **20260509**
- Cohort: 4 scenarios × 50 = 200 subjects
- Time window: 90 days × 24 h
- Channels: 5

## Pre-registration

OSF protocol locked before any run. See `OSF_PREREG.md`.

## Conflict of Interest

Author J. Tkemaladze is the developer of the Ze-AL formalism. Code is public
and deterministic; analysis is reproducible by any third party.
