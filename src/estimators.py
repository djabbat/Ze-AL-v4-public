"""
Five estimators of allostatic burden, applied to the simulated R(t).

1. Traditional AL proxy   — quartile threshold exceedance count (univariate)
2. MA-residual            — 24h moving-average residual integral (univariate)
3. Ze-AL v3 (sigma_E)     — |R-E|/sigma_E(t), GP-based, univariate (the v3 formula
                            that proved fragile under model misspecification)
4. Ze-AL v4 sigma_calib   — |R-E|/sigma_calib (univariate, frozen scale)
5. Ze-AL v4 Mahalanobis   — multivariate (R-E)' Sigma_calib^-1 (R-E)
6. Ze-AL v4 VFE           — Mahalanobis + Bayesian KL surprise term (full
                            variational-free-energy form)

All estimators take a Subject and return a scalar.
"""
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ExpSineSquared, WhiteKernel
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=Warning)

CALIB_DAYS = 14   # first 14 days for calibration / GP fit
DT_H = 1.0


def _make_kernel(length_scale: float = 12.0, period: float = 24.0,
                 noise_level: float = 0.5):
    return (RBF(length_scale=length_scale, length_scale_bounds=(1.0, 200.0))
            + ExpSineSquared(length_scale=1.0, periodicity=period,
                             periodicity_bounds="fixed",
                             length_scale_bounds="fixed")
            + WhiteKernel(noise_level=noise_level,
                          noise_level_bounds=(1e-2, 5.0)))


def _fit_gp_channel(t: np.ndarray, R_k: np.ndarray, kernel=None):
    if kernel is None:
        kernel = _make_kernel()
    gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=0,
                                  alpha=1e-6, normalize_y=True)
    gp.fit(t.reshape(-1, 1), R_k)
    return gp


# Per-process GP cache: (subject_id, kernel_factory_id, channel) -> fitted GP
_GP_CACHE: dict = {}


def _fit_gps(subject, n_train: int, kernel_fn=_make_kernel, cache_tag: str = "default"):
    """Fit one GP per channel on the first n_train hours.

    Uses per-process cache keyed by (subject.sid, cache_tag, channel) so that
    estimator_v4_vfe does not re-fit the GPs already fit by
    estimator_v4_mahalanobis. The cache is flushed per subject after both
    estimators have run (handled in run_experiment._eval_one_subject).
    """
    t = subject.t
    R = subject.R
    K, _ = R.shape
    gps = []
    for k in range(K):
        key = (subject.sid, cache_tag, k, n_train)
        gp = _GP_CACHE.get(key)
        if gp is None:
            gp = _fit_gp_channel(t[:n_train], R[k, :n_train], kernel_fn())
            _GP_CACHE[key] = gp
        gps.append(gp)
    return gps


def _flush_cache(subject_id: int):
    keys = [k for k in _GP_CACHE if k[0] == subject_id]
    for k in keys:
        del _GP_CACHE[k]


def estimator_traditional(subject, n_train: int = None, **_):
    """Number of test-window observations exceeding training quartile thresholds.

    Univariate (channel 0). Same idea as v3 traditional AL proxy.
    """
    if n_train is None:
        n_train = int(CALIB_DAYS * 24 / DT_H)
    R0_train = subject.R[0, :n_train]
    R0_test = subject.R[0, n_train:]
    q1, q3 = np.quantile(R0_train, [0.25, 0.75])
    iqr = q3 - q1
    high = q3 + 0.5 * iqr  # "high-risk" upper threshold
    low = q1 - 0.5 * iqr
    exceed = ((R0_test > high) | (R0_test < low)).sum()
    return float(exceed)


def estimator_ma_residual(subject, n_train: int = None, window_h: int = 24, **_):
    """24h moving-average residual integral.

    The adversarial baseline that beat v3.
    """
    if n_train is None:
        n_train = int(CALIB_DAYS * 24 / DT_H)
    R0 = subject.R[0]
    w = int(window_h / DT_H)
    pad = np.concatenate([R0[:w][::-1], R0])
    ma = np.convolve(pad, np.ones(w) / w, mode="valid")[:len(R0)]
    res = R0 - ma
    sigma = np.std(res[:n_train])
    return float(np.abs(res[n_train:]).sum() / max(sigma, 1e-3))


def estimator_v3(subject, n_train: int = None, kernel_fn=_make_kernel, **_):
    """Ze-AL v3: integral of |R(t)-E(t)|/sigma_E(t), univariate channel 0."""
    if n_train is None:
        n_train = int(CALIB_DAYS * 24 / DT_H)
    t = subject.t
    R0 = subject.R[0]
    gp = _fit_gp_channel(t[:n_train], R0[:n_train], kernel_fn())
    test_t = t[n_train:].reshape(-1, 1)
    E, sigma_E = gp.predict(test_t, return_std=True)
    sigma_E = np.maximum(sigma_E, 1e-3)
    Ze = np.abs(R0[n_train:] - E) / sigma_E
    return float(Ze.sum())


def estimator_v4_sigma_calib(subject, n_train: int = None,
                              kernel_fn=_make_kernel, **_):
    """v4 univariate: divide by sigma_calib (residual SD over training window)."""
    if n_train is None:
        n_train = int(CALIB_DAYS * 24 / DT_H)
    t = subject.t
    R0 = subject.R[0]
    gp = _fit_gp_channel(t[:n_train], R0[:n_train], kernel_fn())
    E_train = gp.predict(t[:n_train].reshape(-1, 1))
    sigma_calib = np.std(R0[:n_train] - E_train)
    sigma_calib = max(sigma_calib, 1e-3)

    test_t = t[n_train:].reshape(-1, 1)
    E_test = gp.predict(test_t)
    Ze = np.abs(R0[n_train:] - E_test) / sigma_calib
    return float(Ze.sum())


def estimator_v4_mahalanobis(subject, n_train: int = None,
                              kernel_fn=_make_kernel,
                              cache_tag: str = "default", **_):
    """v4 multivariate Mahalanobis with sigma_calib."""
    if n_train is None:
        n_train = int(CALIB_DAYS * 24 / DT_H)
    t = subject.t
    R = subject.R
    K, n = R.shape

    gps = _fit_gps(subject, n_train, kernel_fn, cache_tag=cache_tag)
    E_train = np.zeros((K, n_train))
    E_test = np.zeros((K, n - n_train))
    for k in range(K):
        E_train[k] = gps[k].predict(t[:n_train].reshape(-1, 1))
        E_test[k] = gps[k].predict(t[n_train:].reshape(-1, 1))

    res_train = R[:, :n_train] - E_train  # K x n_train
    Sigma = np.cov(res_train) + 1e-3 * np.eye(K)
    Sigma_inv = np.linalg.inv(Sigma)

    res_test = R[:, n_train:] - E_test    # K x (n-n_train)
    # Mahalanobis squared at each timestep: sum_{kj} res[k] * Sinv[k,j] * res[j]
    Ze_t = np.einsum("kn,kj,jn->n", res_test, Sigma_inv, res_test)
    return float(Ze_t.sum())


def estimator_v4_vfe(subject, n_train: int = None,
                     kernel_fn=_make_kernel,
                     beta: float = 0.5, kl_window_h: int = 24,
                     cache_tag: str = "default", **_):
    """Full VFE: Mahalanobis + Bayesian KL surprise term.

    KL approximation:
      Per channel k, in each rolling window w of `kl_window_h` hours,
      compare residual variance vs preceding window. Sum KL between
      the two implied Gaussian residual distributions.

      KL[N(0,sig_curr) || N(0,sig_prev)] = 0.5 (log(sig_prev/sig_curr)
                                                 + sig_curr/sig_prev - 1)
    This penalises forced belief updates — operationalising McEwen
    "wear and tear" as the cost of repeated re-calibration.
    """
    if n_train is None:
        n_train = int(CALIB_DAYS * 24 / DT_H)
    mahal = estimator_v4_mahalanobis(subject, n_train, kernel_fn,
                                     cache_tag=cache_tag)

    R = subject.R
    K, n = R.shape
    # Reuse cached GPs from estimator_v4_mahalanobis (same cache_tag)
    t = subject.t
    gps = _fit_gps(subject, n_train, kernel_fn, cache_tag=cache_tag)
    E_test = np.zeros((K, n - n_train))
    for k in range(K):
        E_test[k] = gps[k].predict(t[n_train:].reshape(-1, 1))
    res_test = R[:, n_train:] - E_test  # K x (n-n_train)

    w = int(kl_window_h / DT_H)
    n_test = res_test.shape[1]
    n_windows = n_test // w
    if n_windows < 2:
        return mahal

    kl_total = 0.0
    for k in range(K):
        for wi in range(1, n_windows):
            i0_curr = wi * w
            r_curr = res_test[k, i0_curr:i0_curr + w]
            r_prev = res_test[k, (wi - 1) * w:wi * w]
            sig_curr = float(np.var(r_curr) + 1e-6)
            sig_prev = float(np.var(r_prev) + 1e-6)
            kl_total += 0.5 * (np.log(sig_prev / sig_curr)
                               + sig_curr / sig_prev - 1.0)
    return float(mahal + beta * kl_total)


ESTIMATORS = {
    "traditional":  estimator_traditional,
    "ma_residual":  estimator_ma_residual,
    "v3_sigma_E":   estimator_v3,
    "v4_sigma_calib": estimator_v4_sigma_calib,
    "v4_mahalanobis": estimator_v4_mahalanobis,
    "v4_vfe":       estimator_v4_vfe,
}


if __name__ == "__main__":
    from generator import generate_subject
    s = generate_subject(seed=20260509, scenario="medium", T_days=30)
    print(f"subject: burden={s.burden:.1f}  R={s.R.shape}")
    for name, fn in ESTIMATORS.items():
        v = fn(s)
        print(f"  {name:18s} = {v:.2f}")
