"""
Generate publication figures from results/summary.json + raw_rows.json.
  fig1.png — single-subject trace example
  fig2.png — correlation bars across all conditions × estimators
  fig3.png — scatter plot v4-VFE vs ground-truth burden, color by scenario
"""
import json
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).parent.parent

def main():
    summary = json.loads((ROOT / "results/summary.json").read_text())
    rows = json.loads((ROOT / "results/raw_rows.json").read_text())

    estimators = ["traditional", "ma_residual", "v3_sigma_E",
                  "v4_sigma_calib", "v4_mahalanobis", "v4_vfe"]
    conditions = list(summary.keys())
    colors = {"control": "#888", "low": "#4080d0", "medium": "#e08020", "high": "#c02020"}

    # Figure 2: TWO-PANEL bar chart for r_burden (top) and r_outcome (bottom)
    fig, axes = plt.subplots(2, 1, figsize=(11, 9), sharex=True)
    x = np.arange(len(estimators))
    w = 0.12
    for ax_idx, target in enumerate(["burden", "outcome"]):
        ax = axes[ax_idx]
        for i, cond in enumerate(conditions):
            rs = [summary[cond][e][f"r_{target}"] for e in estimators]
            los = [summary[cond][e][f"ci_{target}"][0] for e in estimators]
            his = [summary[cond][e][f"ci_{target}"][1] for e in estimators]
            offsets = (i - len(conditions)/2 + 0.5) * w
            ax.bar(x + offsets, rs, w, label=cond,
                   yerr=[np.array(rs)-np.array(los), np.array(his)-np.array(rs)],
                   capsize=2)
        ax.set_xticks(x)
        ax.set_xticklabels(estimators, rotation=20, ha="right")
        ax.axhline(0, color="k", lw=0.5)
        if target == "burden":
            ax.set_ylabel("Pearson r vs ground-truth burden\n(potentially circular)")
            ax.set_title("Ze-AL estimators (n=200, 5 channels, 90 days)")
            ax.legend(ncol=4, fontsize=8, loc="lower left")
        else:
            ax.set_ylabel("Pearson r vs independent outcome surrogate\n(nonlinear, subject-varying)")
        ax.set_ylim(-1.0, 1.0)
    plt.tight_layout()
    fig.savefig(ROOT / "figures/fig2_correlations.png", dpi=150)
    plt.close(fig)
    print(f"saved {ROOT/'figures/fig2_correlations.png'}")

    # Figure 3: scatter v4-VFE vs burden, primary condition
    primary_rows = rows["primary"]
    fig, ax = plt.subplots(figsize=(7, 5.5))
    for sc in ["control", "low", "medium", "high"]:
        rs = [r for r in primary_rows if r["scenario"] == sc]
        bx = [r["burden"] for r in rs]
        by = [r["v4_vfe"] for r in rs]
        ax.scatter(bx, by, c=colors[sc], label=sc, s=20, alpha=0.7)
    ax.set_xlabel("Ground-truth burden")
    ax.set_ylabel("Ze-AL v4 VFE")
    ax.set_title(f"v4 VFE vs burden — primary condition (r={summary['primary']['v4_vfe']['r']:.3f})")
    ax.legend()
    plt.tight_layout()
    fig.savefig(ROOT / "figures/fig3_scatter.png", dpi=150)
    plt.close(fig)
    print(f"saved {ROOT/'figures/fig3_scatter.png'}")

    # Figure 1: single subject trace
    from generator import generate_subject
    s = generate_subject(seed=20260509+30000+10, scenario="medium", T_days=30)
    fig, ax = plt.subplots(5, 1, figsize=(10, 8), sharex=True)
    labels = ["z-VM", "sleep_prob", "fragmentation", "M30", "acrophase_dev"]
    for k in range(5):
        ax[k].plot(s.t, s.R[k], lw=0.5)
        for ev in s.events:
            ax[k].axvline(ev["t"], color="r" if ev["u"] else "g", alpha=0.3, lw=0.4)
        ax[k].set_ylabel(labels[k], fontsize=9)
    ax[-1].set_xlabel("Time (h)")
    ax[0].set_title(f"Subject example: scenario={s.scenario}, burden={s.burden:.0f}")
    plt.tight_layout()
    fig.savefig(ROOT / "figures/fig1_subject.png", dpi=150)
    plt.close(fig)
    print(f"saved {ROOT/'figures/fig1_subject.png'}")

if __name__ == "__main__":
    main()
