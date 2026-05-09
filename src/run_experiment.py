"""
Primary + 4 sensitivity conditions, n=200 (4 scenarios x 50).
Computes Pearson r between each estimator and ground-truth burden.
Also bootstrap 95% CI.

Sensitivity conditions:
  primary           — correctly specified GP kernel
  lengthscale_-50%  — RBF length-scale forced to half
  lengthscale_+50%  — RBF length-scale forced to 1.5x
  no_circadian      — only RBF kernel (no 24h periodic)
  noise_3x          — observation noise sigma 3x baseline
"""
import json
import numpy as np
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
import os, sys

sys.path.insert(0, str(Path(__file__).parent))
from generator import generate_cohort
from estimators import (
    ESTIMATORS, _make_kernel,
)
from sklearn.gaussian_process.kernels import RBF, ExpSineSquared, WhiteKernel


# Sensitivity-condition kernel factories
def _kernel_lengthscale_half():
    return (RBF(length_scale=6.0, length_scale_bounds="fixed")
            + ExpSineSquared(length_scale=1.0, periodicity=24.0,
                             periodicity_bounds="fixed",
                             length_scale_bounds=(0.1, 100.0))
            + WhiteKernel(noise_level=0.5,
                          noise_level_bounds=(1e-3, 10.0)))


def _kernel_lengthscale_oneandhalf():
    return (RBF(length_scale=18.0, length_scale_bounds="fixed")
            + ExpSineSquared(length_scale=1.0, periodicity=24.0,
                             periodicity_bounds="fixed",
                             length_scale_bounds=(0.1, 100.0))
            + WhiteKernel(noise_level=0.5,
                          noise_level_bounds=(1e-3, 10.0)))


def _kernel_no_circadian():
    return (RBF(length_scale=12.0, length_scale_bounds=(1.0, 200.0))
            + WhiteKernel(noise_level=0.5,
                          noise_level_bounds=(1e-3, 10.0)))


def _bootstrap_ci(y_true, y_pred, n_boot=2000, seed=0):
    rng = np.random.default_rng(seed)
    n = len(y_true)
    rs = []
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    if np.std(y_pred) < 1e-9 or np.std(y_true) < 1e-9:
        return float("nan"), (float("nan"), float("nan"))
    r = float(np.corrcoef(y_true, y_pred)[0, 1])
    for _ in range(n_boot):
        idx = rng.integers(0, n, size=n)
        if np.std(y_pred[idx]) < 1e-9 or np.std(y_true[idx]) < 1e-9:
            continue
        rs.append(float(np.corrcoef(y_true[idx], y_pred[idx])[0, 1]))
    lo, hi = np.percentile(rs, [2.5, 97.5])
    return r, (float(lo), float(hi))


def _eval_one_subject(args):
    """Worker: compute all estimators for one subject under one condition."""
    from estimators import _flush_cache
    sid_idx, subject, kernel_factory_name = args
    # Map kernel factory name → callable
    factories = {
        "primary": _make_kernel,
        "lengthscale_-50%": _kernel_lengthscale_half,
        "lengthscale_+50%": _kernel_lengthscale_oneandhalf,
        "no_circadian": _kernel_no_circadian,
        "noise_3x": _make_kernel,  # noise applied to subject; kernel itself unchanged
    }
    kfn = factories[kernel_factory_name]
    out = {"sid": subject.sid, "scenario": subject.scenario,
           "burden": subject.burden,
           "outcome_score": subject.outcome_score,
           "resilience": subject.resilience,
           "behavioral_score": subject.behavioral_score,
           "latent_independent": subject.latent_independent}
    cache_tag = kernel_factory_name
    for name, fn in ESTIMATORS.items():
        if name in ("traditional", "ma_residual"):
            v = fn(subject)
        elif name in ("v4_mahalanobis", "v4_vfe"):
            v = fn(subject, kernel_fn=kfn, cache_tag=cache_tag)
        else:
            v = fn(subject, kernel_fn=kfn)
        out[name] = v
    # Flush this subject's cache to free memory before next subject
    _flush_cache(subject.sid)
    return out


def _apply_noise_3x(subject):
    """Inflate observation noise by 3x (over the already-injected noise sigma)."""
    rng = np.random.default_rng(subject.sid + 999)
    extra_sigma = 2.0 * subject.noise_sigma
    subject.R = subject.R + rng.normal(0, extra_sigma, size=subject.R.shape)
    return subject


def _apply_baseline_drift(subject):
    """Apply slow linear drift across full window; tests Σ_calib robustness
    to non-stationary baselines (RT v6 demand)."""
    K, n = subject.R.shape
    rng = np.random.default_rng(subject.sid + 7777)
    # Per-channel drift amplitude in [-0.5, +0.5] over full 90d window
    slopes = rng.uniform(-0.5, 0.5, size=K) / n
    drift = np.outer(slopes, np.arange(n))
    subject.R = subject.R + drift
    return subject


def run_condition(condition: str, cohort, max_workers: int = None):
    if condition == "noise_3x":
        from copy import deepcopy
        cohort = [_apply_noise_3x(deepcopy(s)) for s in cohort]
    elif condition in ("contam_calib_10pct", "contam_calib_30pct"):
        frac = 0.10 if condition.endswith("10pct") else 0.30
        cohort = generate_cohort(n_per_scenario=50, T_days=90,
                                 calib_contam_frac=frac)
    elif condition == "antagonistic_channels":
        cohort = generate_cohort(n_per_scenario=50, T_days=90,
                                 coupling_mode="antagonistic")
    elif condition == "baseline_drift":
        # Add a slow linear drift component to all channels during calibration
        # period — tests robustness to non-stationary baselines (RT v6 demand).
        from copy import deepcopy
        cohort = [_apply_baseline_drift(deepcopy(s)) for s in cohort]

    # Map condition → kernel factory key for _eval_one_subject
    cond_key = condition
    if condition in ("contam_calib_10pct", "contam_calib_30pct",
                     "antagonistic_channels", "baseline_drift"):
        cond_key = "primary"
    args = [(i, s, cond_key) for i, s in enumerate(cohort)]
    rows = []
    if max_workers is None:
        max_workers = max(os.cpu_count() - 1, 1)
    with ProcessPoolExecutor(max_workers=max_workers) as ex:
        futures = [ex.submit(_eval_one_subject, a) for a in args]
        for fut in as_completed(futures):
            rows.append(fut.result())
    rows.sort(key=lambda r: r["sid"])
    return rows


def summarize(rows, estimators=None):
    """Compute Pearson r against THREE targets:
    (i) ground-truth burden (potentially circular for Mahalanobis)
    (ii) outcome_score (nonlinear transform of burden — addresses circularity)
    (iii) behavioral_score (truly independent — only 30% burden component)
    """
    if estimators is None:
        estimators = list(ESTIMATORS.keys())
    burdens = np.array([r["burden"] for r in rows])
    outcomes = np.array([r["outcome_score"] for r in rows])
    behaviorals = np.array([r["behavioral_score"] for r in rows])
    summary = {}
    for est in estimators:
        vals = np.array([r[est] for r in rows])
        r_b, (b_lo, b_hi) = _bootstrap_ci(burdens, vals)
        r_o, (o_lo, o_hi) = _bootstrap_ci(outcomes, vals, seed=1)
        r_x, (x_lo, x_hi) = _bootstrap_ci(behaviorals, vals, seed=2)
        summary[est] = {
            "r_burden": r_b, "ci_burden": [b_lo, b_hi],
            "r_outcome": r_o, "ci_outcome": [o_lo, o_hi],
            "r_behavioral": r_x, "ci_behavioral": [x_lo, x_hi],
            # legacy
            "r": r_b, "ci_lo": b_lo, "ci_hi": b_hi,
        }
    return summary


def _fdr_bh(p_values, q=0.05):
    """Benjamini-Hochberg FDR correction. Returns adjusted q-values."""
    p = np.asarray(p_values)
    n = len(p)
    order = np.argsort(p)
    ranked = np.empty_like(order)
    ranked[order] = np.arange(n)
    q_vals = p * n / (ranked + 1)
    # monotone correction
    sorted_q = q_vals[order]
    for i in range(n - 2, -1, -1):
        sorted_q[i] = min(sorted_q[i], sorted_q[i + 1])
    out = np.empty_like(q_vals)
    out[order] = np.minimum(sorted_q, 1.0)
    return out.tolist()


def _r_to_p(r, n):
    """Two-sided p-value for Pearson r via Fisher z (n=200, SE=1/sqrt(n-3))."""
    import math
    from scipy.stats import norm
    if abs(r) >= 0.999999:
        return 0.0
    z = math.atanh(r) * math.sqrt(n - 3)
    return float(2 * (1 - norm.cdf(abs(z))))


def main():
    here = Path(__file__).parent.parent
    print("Generating cohort (4 scenarios x 50 = 200 subjects, 90 days)...", flush=True)
    cohort = generate_cohort(n_per_scenario=50, T_days=90)
    print(f"  cohort: {len(cohort)} subjects", flush=True)

    conditions = ["primary",
                  "lengthscale_-50%",
                  "lengthscale_+50%",
                  "no_circadian",
                  "noise_3x",
                  "contam_calib_10pct",
                  "contam_calib_30pct",
                  "antagonistic_channels",
                  "baseline_drift"]

    all_results = {}
    all_rows = {}
    for cond in conditions:
        print(f"\n--- Condition: {cond} ---", flush=True)
        rows = run_condition(cond, cohort)
        all_rows[cond] = rows
        summary = summarize(rows)
        all_results[cond] = summary
        for est, s in summary.items():
            print(f"  {est:18s} r_burd={s['r_burden']:+.3f}"
                  f"   r_out={s['r_outcome']:+.3f}"
                  f"   r_beh={s['r_behavioral']:+.3f}",
                  flush=True)

    # Apply FDR (Benjamini-Hochberg) to the family of burden correlations
    # Family = 6 estimators × 9 conditions = 54 tests
    flat = []
    flat_keys = []
    for cond in conditions:
        for est in all_results[cond]:
            r = all_results[cond][est]["r_burden"]
            p = _r_to_p(r, n=200)
            flat.append(p)
            flat_keys.append((cond, est))
    q_vals = _fdr_bh(flat, q=0.05)
    for (cond, est), q in zip(flat_keys, q_vals):
        all_results[cond][est]["p_burden"] = flat[flat_keys.index((cond, est))]
        all_results[cond][est]["q_burden_fdr"] = q

    out_dir = here / "results"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "summary.json").write_text(json.dumps(all_results, indent=2))
    (out_dir / "raw_rows.json").write_text(json.dumps(all_rows, indent=2))
    print(f"\nSaved → {out_dir / 'summary.json'}")


if __name__ == "__main__":
    main()
