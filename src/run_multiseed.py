"""
Multi-seed sensitivity analysis (Red Team v8 specific demand).
Runs the full pipeline 10 times with different master seeds,
reports distribution of correlations per estimator/condition.
"""
import os, sys, json, time
from pathlib import Path
import numpy as np

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

sys.path.insert(0, str(Path(__file__).parent))
from generator import generate_cohort
from estimators import ESTIMATORS, _make_kernel, _flush_cache
from run_experiment import run_condition, summarize, _eval_one_subject

ROOT = Path(__file__).parent.parent
SEEDS = [20260509 + i * 100000 for i in range(10)]
# Seeds: 20260509, 20360509, 20460509, 20560509, ..., 21160509

# We'll run only the primary condition + contam_calib_10pct + contam_calib_30pct
# across all 10 seeds — these are the most informative comparisons. Other
# conditions are stable across seeds based on iter-7 evidence (within 0.005 r).
CONDITIONS = ["primary", "contam_calib_10pct", "contam_calib_30pct"]
ESTIMATORS_SUBSET = ["traditional", "ma_residual", "v3_sigma_E",
                     "v4_sigma_calib", "v4_mahalanobis"]

def run_one_seed(master_seed: int):
    """Generate cohort with this seed, run conditions, return summary."""
    # Monkey-patch the base_seed for this run
    import generator as _gen
    cohort = _gen.generate_cohort(n_per_scenario=50, T_days=90,
                                   base_seed=master_seed)
    out = {}
    for cond in CONDITIONS:
        rows = run_condition(cond, cohort)
        s = summarize(rows)
        out[cond] = {est: {"r_burden": s[est]["r_burden"],
                            "r_outcome": s[est]["r_outcome"],
                            "r_behavioral": s[est]["r_behavioral"]}
                     for est in ESTIMATORS_SUBSET}
    return out


def main():
    print(f"Multi-seed sensitivity: {len(SEEDS)} seeds × {len(CONDITIONS)} conditions",
          flush=True)
    print(f"Seeds: {SEEDS}", flush=True)
    all_results = {}
    t_start = time.time()
    for i, seed in enumerate(SEEDS):
        t0 = time.time()
        print(f"\n[{i+1}/{len(SEEDS)}] seed={seed}", flush=True)
        all_results[str(seed)] = run_one_seed(seed)
        dt = time.time() - t0
        print(f"  done in {dt/60:.1f}min", flush=True)
    print(f"\nTotal: {(time.time()-t_start)/60:.1f}min", flush=True)

    # Aggregate per-condition / per-estimator distributions
    aggregated = {}
    for cond in CONDITIONS:
        aggregated[cond] = {}
        for est in ESTIMATORS_SUBSET:
            for target in ["r_burden", "r_outcome", "r_behavioral"]:
                vals = [all_results[str(s)][cond][est][target] for s in SEEDS]
                aggregated[cond].setdefault(est, {})
                aggregated[cond][est][target] = {
                    "mean": float(np.mean(vals)),
                    "sd":   float(np.std(vals, ddof=1)),
                    "min":  float(np.min(vals)),
                    "max":  float(np.max(vals)),
                    "vals": vals,
                }
    out_path = ROOT / "results/multiseed_summary.json"
    out_path.write_text(json.dumps({"seeds": SEEDS,
                                    "raw": all_results,
                                    "aggregated": aggregated}, indent=2))
    print(f"\nSaved → {out_path}")

    # Print key numbers
    print("\n=== KEY NUMBERS ===")
    for cond in CONDITIONS:
        print(f"\n[{cond}]")
        for est in ESTIMATORS_SUBSET:
            a = aggregated[cond][est]["r_burden"]
            print(f"  {est:18s} r_burden mean={a['mean']:+.3f}  sd={a['sd']:.3f}"
                  f"  range=[{a['min']:+.3f}, {a['max']:+.3f}]")


if __name__ == "__main__":
    main()
