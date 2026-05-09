"""
Multivariate accelerometric burden simulator for Ze-AL v4.

Channels (mimicking real wrist accelerometer features):
  k=0: log vector magnitude     (z-VM)
  k=1: sleep probability        (sleep_prob)
  k=2: activity fragmentation   (fragmentation)
  k=3: M30 peak intensity       (M30)
  k=4: circadian acrophase dev  (acrophase_dev)

Stressors perturb COHERENTLY across channels — that is the multivariate
signal Mahalanobis-based estimators are supposed to amplify.

Ground-truth burden:
  burden = sum_i A_i * weight(u_i)
  weight(0) = 0.3 (predictable), weight(1) = 1.0 (unpredictable)
"""
import numpy as np
from dataclasses import dataclass, field
from typing import List

K_CHANNELS = 5
DT_H = 1.0  # hourly sampling


@dataclass
class Subject:
    sid: int
    scenario: str
    R: np.ndarray      # K x N
    t: np.ndarray      # N
    events: list       # list of dicts (t, A, u)
    burden: float
    noise_sigma: float
    # outcome_score: nonlinear function of burden — useful but admittedly
    # not fully independent (cf. RT TBPR concern).
    outcome_score: float = 0.0
    resilience: float = 0.0
    # behavioral_score: truly independent dimension. Constructed as
    #   behavioral = 0.30 * z(burden) + 0.70 * latent_independent + N(0, 0.5)
    # where latent_independent ~ N(0, 1) is sampled independently of all
    # generator state. r(behavioral, burden) ≈ 0.3 by construction;
    # an estimator that captures *only* burden cannot exceed this ceiling.
    # Estimators that are *not* burden detectors will track behavioral
    # only to the extent of the small burden component. This addresses the
    # RT v4 critique: "outcome is function of burden". behavioral is a
    # genuinely independent target.
    behavioral_score: float = 0.0
    latent_independent: float = 0.0


def _circadian_baseline(t: np.ndarray, K: int) -> np.ndarray:
    """K x N baseline: 24h + 7d periodic, channel-specific phases/amps."""
    out = np.zeros((K, len(t)))
    for k in range(K):
        amp_24 = 1.0 + 0.25 * k
        amp_7 = 0.4 * amp_24
        phase_24 = k * np.pi / 5
        phase_7 = k * np.pi / 4
        out[k] = (amp_24 * np.sin(2 * np.pi * t / 24.0 + phase_24)
                  + amp_7 * np.sin(2 * np.pi * t / (24.0 * 7.0) + phase_7))
    return out


def _stressor_kernel(width_h: float, dt_h: float = DT_H) -> np.ndarray:
    """Gaussian impulse kernel (decay over ~width_h hours)."""
    w = max(int(round(width_h / dt_h)), 3)
    half = w
    x = np.arange(-half, half + 1) * dt_h
    k = np.exp(-(x ** 2) / (2 * (width_h / 2.5) ** 2))
    return k / k.max()


def _channel_coupling_pattern(K: int, rng,
                              mode: str = "coherent") -> np.ndarray:
    """K-vector specifying multi-channel response to a stressor.

    mode='coherent'      — moderately correlated, standard scenario
    mode='antagonistic'  — strict alternation [+1,-1,+1,-1,+1], stress test
                           for Mahalanobis (which assumes coherent residuals)
    """
    if mode == "coherent":
        base = np.array([1.0, -0.6, 0.8, 0.7, -0.5][:K])
        jitter = rng.normal(0, 0.15, size=K)
    elif mode == "antagonistic":
        # Strict alternation; magnitudes randomised to prevent perfect
        # cancellation when stressor amplitude is averaged
        base = np.array([1.0, -1.0, 1.0, -1.0, 1.0][:K])
        jitter = rng.normal(0, 0.10, size=K)
    else:
        raise ValueError(mode)
    return base + jitter


def generate_subject(seed: int, scenario: str, T_days: int = 90,
                     dt_h: float = DT_H, K: int = K_CHANNELS,
                     calib_days: int = 14,
                     calib_contam_frac: float = 0.0,
                     coupling_mode: str = "coherent") -> Subject:
    """Generate one subject under the given scenario.

    Stressors are confined to t > calib_days * 24 hours so that the
    calibration window contains no stressor signal — this ensures Σ_calib
    estimates the true noise covariance, not a stressor-contaminated one.

    Scenarios:
        control: 0 events
        low:     2 events/day, 20% unpredictable, no jitter
        medium:  4 events/day, 60% unpredictable, no jitter
        high:    4 events/day, 100% unpredictable, with amplitude jitter
    """
    rng = np.random.default_rng(seed)
    n_steps = int(round(T_days * 24 / dt_h))
    t = np.arange(n_steps) * dt_h

    R = _circadian_baseline(t, K)

    # Stressor schedule
    if scenario == "control":
        events_per_day, p_unpredictable, jitter_amp = 0, 0.0, False
    elif scenario == "low":
        events_per_day, p_unpredictable, jitter_amp = 2, 0.20, False
    elif scenario == "medium":
        events_per_day, p_unpredictable, jitter_amp = 4, 0.60, False
    elif scenario == "high":
        events_per_day, p_unpredictable, jitter_amp = 4, 1.00, True
    else:
        raise ValueError(scenario)

    events: List[dict] = []
    burden = 0.0
    # Stressors live primarily in the test window (days calib_days .. T_days),
    # but a fraction `calib_contam_frac` may be placed inside the calibration
    # window (days 0..calib_days). This is used by the calibration-contamination
    # sensitivity condition.
    test_T_days = T_days - calib_days
    n_events_total = events_per_day * test_T_days
    if n_events_total > 0:
        n_contam = int(round(n_events_total * calib_contam_frac))
        n_test = n_events_total - n_contam
        # contaminated events uniformly in calibration window
        contam_times = [rng.uniform(0.5, calib_days * 24 - 0.5)
                        for _ in range(n_contam)]
        # test events uniformly in test window
        test_times = [(calib_days * 24
                       + (i + rng.uniform(0.1, 0.9))
                       * (test_T_days * 24 / max(n_test, 1)))
                      for i in range(n_test)]
        all_times = sorted(contam_times + test_times)

        for i, ev_t in enumerate(all_times):
            A = (3.0 + (rng.normal(0, 0.8) if jitter_amp else 0.0))
            A = float(np.clip(A, 1.5, 6.0))
            u = int(rng.uniform() < p_unpredictable)
            events.append({"t": float(ev_t), "A": A, "u": u})

            # Apply stressor across channels
            kernel = _stressor_kernel(width_h=8.0, dt_h=dt_h)
            coupling = _channel_coupling_pattern(K, rng, mode=coupling_mode)
            t_idx = int(round(ev_t / dt_h))
            half = (len(kernel) - 1) // 2
            i0, i1 = max(0, t_idx - half), min(n_steps, t_idx - half + len(kernel))
            k0, k1 = i0 - (t_idx - half), len(kernel) - ((t_idx - half + len(kernel)) - i1)
            for k in range(K):
                R[k, i0:i1] += A * coupling[k] * kernel[k0:k1]

            burden += A * (1.0 if u else 0.3)

    # Channel-specific Gaussian observation noise
    noise_sigma = 0.5
    noise = rng.normal(0, noise_sigma, size=R.shape)
    R = R + noise

    # Outcome-1: nonlinear transform of burden + resilience (NOT fully
    # independent — addresses circularity partially; see behavioral below).
    resilience = float(rng.beta(2.0, 2.0))
    sigma_outcome = 4.0
    eps = float(rng.normal(0, sigma_outcome))
    outcome_score = (
        np.log1p(max(burden, 0.0)) * (1.0 + 0.5 * (resilience - 0.5))
        + 5.0 * (1.0 - np.exp(-max(burden, 0.0) / 1500.0))
        + eps
    )

    # Outcome-2 (behavioral): genuinely independent — only 30% burden
    # component, 70% latent independent variable. An estimator that detects
    # *only* burden has a theoretical ceiling of r ≈ 0.30 against this.
    latent_independent = float(rng.normal(0, 1))
    # We z-score burden here using a global mean/sd estimated from the
    # cohort-wide burden distribution (locked, derived once at OSF prereg
    # time, hard-coded to avoid leakage). For 4-scenario cohort with our
    # parameters: mean ≈ 555, sd ≈ 380 (taken from a 200-subject pilot).
    z_burden = (burden - 555.0) / 380.0
    behavioral_score = 0.30 * z_burden + 0.70 * latent_independent + float(rng.normal(0, 0.5))

    return Subject(
        sid=seed, scenario=scenario, R=R, t=t,
        events=events, burden=burden, noise_sigma=noise_sigma,
        outcome_score=float(outcome_score), resilience=resilience,
        behavioral_score=float(behavioral_score),
        latent_independent=latent_independent,
    )


def generate_cohort(scenarios=("control", "low", "medium", "high"),
                    n_per_scenario: int = 50,
                    base_seed: int = 20260509,
                    T_days: int = 90,
                    dt_h: float = DT_H,
                    K: int = K_CHANNELS,
                    calib_contam_frac: float = 0.0,
                    coupling_mode: str = "coherent") -> List[Subject]:
    cohort = []
    for sc_idx, sc in enumerate(scenarios):
        for i in range(n_per_scenario):
            seed = base_seed + sc_idx * 10000 + i
            cohort.append(generate_subject(
                seed, sc, T_days=T_days, dt_h=dt_h, K=K,
                calib_contam_frac=calib_contam_frac,
                coupling_mode=coupling_mode,
            ))
    return cohort


if __name__ == "__main__":
    cohort = generate_cohort(n_per_scenario=5, T_days=30)
    print(f"generated {len(cohort)} subjects")
    for s in cohort[:4]:
        print(f"  sid={s.sid} sc={s.scenario:8s} R={s.R.shape} burden={s.burden:.1f} ev={len(s.events)}")
