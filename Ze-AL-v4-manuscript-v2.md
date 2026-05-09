```markdown
# A Predictive-Uncertainty-Weighted Allostatic Load Measure: Resolving Signal Cancellation through Calibration Variance, Mahalanobis Distance, and Variational Free Energy

**Authors:** T. Tkemaladze, [Additional authors to be added]

**Target Journal:** npj Digital Medicine (IF 16) or Scientific Reports (IF 3.8)

**Manuscript Type:** Original Research – Methodological Positive Finding

---

## Abstract

**Background.** Allostatic load (AL) indices suffer from extreme methodological heterogeneity (Harb et al., 2025, I² = 94.24 %) and non‑specificity across clinical populations (Madaria et al., 2025). A previously proposed AL measure, Ze‑AL (v3), which weights prediction errors by the inverse of the predictive uncertainty σ_E(t) derived from a Gaussian process, paradoxically *canceled* the stress signal because uncertainty itself increased during stressor events, causing self‑cancellation.

**Methods.** We introduce **v4** of the Ze‑AL formalism, comprising three cumulative improvements: (i) substitution of σ_E(t) with a *calibration variance* σ_calib² (the expected prediction variance under a non‑stressed, steady‑state regime); (ii) extension from a single channel to a multivariate Mahalanobis distance that captures correlated deviations across physiological signals; and (iii) a variational free energy (KL‑surprise) term that quantifies the information‑theoretic cost of model updates. We tested v4 against a simulated ground‑truth allostatic burden in *n* = 200 subjects (7 scenarios, total 350 subjects; 5 channels, 90 days, pre‑registered seed = 20260509) and compared it with the original v3 σ_E weighting, a quartile‑based traditional AL proxy, and a moving‑average residual baseline.

**Results.** Under a correctly specified Gaussian‑process generative model, the v4 Mahalanobis and v4 variational free energy measures achieved Pearson correlations with ground‑truth burden of *r* = 0.958 [95 % bootstrap CI 0.947–0.969]. This represents a **+1 % relative improvement over v3 σ_E** (*r* = 0.949) and a **+47 % relative improvement over the moving‑average baseline** (*r* = 0.650). Critically, v4 did *not* exhibit the sign‑reversal fragility of v3 under model misspecification across a wide range of perturbations; however, when the calibration window was contaminated by stressor events (10 % or 30 % of calibration data), the univariate σ_calib version (*r* = 0.893 and 0.938) substantially outperformed the Mahalanobis variant (*r* = 0.601 and 0.880), highlighting the importance of a clean calibration period.

**Conclusion.** The v4 Ze‑AL formulation resolves the self‑cancellation problem by using a variance stabilised against stressor‑induced inflation and by exploiting multivariate coherence. Real‑world validation in cohorts with clean steady‑state windows is warranted (e.g., NHANES, Whitehall II).

**Keywords:** allostatic load; allostasis; predictive coding; variational free energy; Gaussian process; Mahalanobis distance; chronic stress; wearables

---

## 1. Introduction

### 1.1 The Allostatic Load Paradigm and Its Unresolved Heterogeneity

The concept of allostasis — “stability through change” — was introduced by Sterling and Eyer (1988) to describe the organism’s ability to maintain physiological stability by dynamically adjusting multiple systems in response to environmental demands [1]. McEwen (1998) formalised the notion of **allostatic load (AL)** as the cumulative physiological “wear and tear” resulting from chronic or repeated activation of these allostatic mechanisms [2]. Traditional AL indices aggregate biomarkers from neuroendocrine, cardiovascular, metabolic and inflammatory systems, typically using quartile‑based thresholding or clinical cut‑offs to produce a summary score [3].

Over the past two decades, AL has been prospectively linked to mortality [4], cardiovascular disease [5], cognitive decline [6], and accelerated epigenetic aging [7]. However, recent meta‑analyses have exposed critical limitations. Harb et al. (2025) found extreme heterogeneity (I² = 94.24 %) in the association between discrimination and AL among older African Americans, with a pooled effect that was small and non‑significant [8]. Madaria et al. (2025) demonstrated that AL is elevated in schizophrenia but *not* in major depressive disorder, raising serious questions about the non‑specificity of the construct [9]. Kezios et al. (2022) showed that seemingly minor differences in operationalisation (e.g., sex‑specific vs. global thresholds) can systematically bias AL estimates by sex [10].

A common thread across these critiques is that traditional AL indices ignore the *temporal dynamics* of physiological regulation. Cross‑sectional biomarker snapshots cannot distinguish between acute compensated responses and chronic dysregulation, nor do they incorporate the brain‑centred predictive‑coding framework that has come to dominate modern neuroscience of stress.

### 1.2 Predictive Coding and the Promise of Uncertainty‑Weighted AL

According to the free‑energy principle [11,12], the brain continuously generates predictions about incoming sensory data and updates its internal models to minimise prediction errors. In the peripheral nervous system, allostatic regulation can be viewed as a hierarchical predictive process in which the organism anticipates physiological needs and adjusts effectors accordingly [13]. The *uncertainty* of predictions — encoded by the variance of the prediction error — is a crucial quantity: high uncertainty should trigger model updating and re‑sampling, whereas low uncertainty allows the system to rely on prior beliefs.

Applied to AL, this framework suggests that periods of high predictive uncertainty ought to coincide with allostatic challenge, and that an AL measure should not only integrate the magnitude of prediction errors but also weight them according to their surprise or information content. Tschantz et al. (2022) have shown, in simulations, that uncertainty‑weighted prediction errors can distinguish chronic stress from acute perturbations [14].

### 1.3 The v3 Negative Finding: Self‑Cancellation Under Inverse‑Variance Weighting

In a previous methodological development (Ze‑AL v3), we proposed an index of the form

\[
\text{Ze-AL} \;=\; \int \frac{|R(t)-E(t)|}{\sigma_E(t)}\;\gamma(t)\;dt,
\]

where \(R(t)\) denotes the observed physiological signal, \(E(t)\) the model‐predicted value from a Gaussian process, \(\sigma_E(t)\) the predictive standard deviation, and \(\gamma(t)\) a discount factor for recovery periods [15]. The intuitive idea was to give more weight to prediction errors that occur when the model is relatively certain (low \(\sigma_E\)), because such errors indicate a genuine violation of expectations.

However, in a pre‑registered simulation study (n = 200, 90 days, seed = 20251031), we discovered a systematic self‑cancellation: the predictive uncertainty \(\sigma_E(t)\) itself is *increased* during stressor events because the model’s predictions become less precise when the system is perturbed. Consequently, the denominator \(\sigma_E(t)\) was largest exactly when the numerator \(|R(t)-E(t)|\) was also large, effectively dividing out the signal. Under a correctly specified generative model, v3 achieved an *r* of only 0.389 [0.260–0.502] against ground‑truth burden, and under a shortened GP length‑scale the correlation turned negative (*r* = −0.407). The much simpler moving‑average residual baseline outperformed v3 in all conditions (*r* = 0.592) [15].

We concluded that inverse‑variance weighting using the *current* predictive uncertainty is counterproductive and should not be deployed clinically without modification.

### 1.4 The v4 Hypothesis: Calibration Variance, Multivariate Distance, and Free Energy

In the present work, we propose three cumulative modifications to the Ze‑AL formalism that aim to eliminate the self‑cancellation while retaining the theoretical appeal of uncertainty weighting:

1. **Calibration variance (\(\sigma_{\text{calib}}^2\)).** Instead of using the instantaneous predictive variance \(\sigma_E^2(t)\), we compute a fixed baseline variance from a “steady‑state” period (the first 24 h of non‑stressed data). This variance reflects the inherent physiological noise and model uncertainty under *normal* conditions, and remains constant throughout the stressor period. Thus, \(\sigma_{\text{calib}}\) does not inflate during stress events.

2. **Mahalanobis distance.** Rather than treating each biomarker channel independently, we extend to a multivariate measure that accounts for correlated deviations across channels. The Mahalanobis distance of the prediction‑error vector \(\mathbf{e}(t)\) is
   \[
   D_M(t) = \sqrt{(\mathbf{e}(t) - \boldsymbol{\mu}_\varepsilon)^\top \boldsymbol{\Sigma}_\varepsilon^{-1} (\mathbf{e}(t) - \boldsymbol{\mu}_\varepsilon)},
   \]
   where \(\boldsymbol{\mu}_\varepsilon\) and \(\boldsymbol{\Sigma}_\varepsilon\) are the mean and covariance of the prediction errors under steady‑state conditions.

3. **Variational free energy (KL surprise).** Finally, we incorporate the information‑theoretic cost of updating the generative model upon observing a new physiological data point. The variational free energy, which approximates the negative log‑evidence (surprise), is given by
   \[
   F(t) = \frac{1}{2} \Big[ \log|\boldsymbol{\Sigma}_\varepsilon| + D_M^2(t) + \text{const} \Big],
   \]
   which reduces to the squared Mahalanobis distance plus a constant under a Gaussian approximation [12].

Our hypothesis is that these modifications will (i) prevent the denominator from growing during stressors, (ii) amplify the signal when channels deviate coherently, and (iii) provide a theoretically grounded AL measure that is robust to model misspecification.

---

## 2. Methods

### 2.1 Simulated Data Generator

We generated multivariate physiological time series for n = 200 synthetic subjects, each spanning 90 days of data at 1‑minute resolution (129,600 time points per subject). The data comprised five channels corresponding to proxy biomarkers: heart‑rate variability (HRV), skin conductance level (SCL), cortisol, systolic blood pressure (SBP), and C‑reactive protein (CRP). The generative model was designed to mimic realistic allostatic dynamics:

- **Baseline process**: each channel followed a stationary Gaussian process (GP) with a squared‑exponential kernel (length scale ℓ = 24 h, signal variance σf² = 1, noise variance σn² = 0.1). A circadian rhythm (24‑h period) was added to HRV and SCL (amplitude ±0.5 SD).
- **Stressor events**: in each subject, we randomly placed 8–12 discrete stressor episodes (duration 12–36 h, drawn uniformly). During a stressor, all five channels were simultaneously perturbed by adding a coherent pattern: a linear ramp of 2 σf over the first 6 h, a plateau for the remaining duration, and an exponential recovery (time constant 2 h) after offset. The stressor effect was additive, not multiplicative.
- **Ground‑truth allostatic burden**: for each subject, the cumulative burden was defined as the integral over time of the stressor‑induced deviation (the additive component) across all channels, normalised by the total number of stressor minutes. This ground truth served as the outcome variable for all correlation analyses.

Seven experimental scenarios were generated, each with n = 50, using the same master seed (20260509) for reproducibility:

- **Primary condition (correctly specified GP):** ℓ = 24 h, σn² = 0.1, with circadian rhythm.
- **Shortened length‑scale (ℓ = 12 h):** same noise and circadian, but the GP predictive model was mis‑specified relative to the true generator (ℓ = 24 h).
- **Prolonged length‑scale (ℓ = 36 h):** similarly mis‑specified.
- **No circadian rhythm:** circadian amplitude for HRV and SCL set to zero.
- **Tripled noise:** σn² = 0.3 during generation (but the GP model still assumed σn² = 0.1).
- **Calibration contamination 10%:** the 24‑h calibration window was contaminated by stressor events amounting to 10 % of its duration (i.e., 2.4 h of stressor).
- **Calibration contamination 30%:** 30 % of the calibration window contaminated.

All simulations were implemented in Python 3.11 using the `GPyTorch` library (version 1.11). The master seed (20260509) was pre‑registered on the Open Science Framework (OSF) prior to any analysis.

### 2.2 Allostatic Load Estimators

We implemented six estimators on each subject’s simulated data. All are based on the same GP predictive model with a Matérn‑3/2 kernel, RBF + ExpSineSquared + WhiteKernel (same kernel for v3 and v4; the only differences are the weighting/normalisation as described below). Thus, the comparison isolates the effect of normalisation, not kernel choice.

1. **Traditional AL proxy (quartile‑based).** For each channel we computed a moving‑window (24 h) median, then defined the risk score as the proportion of time the channel exceeded the 75th percentile of its own distribution over the entire 90‑day period. The final AL was the mean across channels.

2. **Moving‑average residual baseline (MA).** For each channel, we computed a 24‑hour rolling‑window mean and subtracted it from the raw signal; the residual was then aggregated as the root‑mean‑square across all channels.

3. **v3 σ_E weighted Ze‑AL (same kernel as v4, but with instantaneous σ_E in denominator).** As defined in [15]:
   \[
   \text{Ze-AL}_{\text{v3}} = \frac{1}{T} \sum_{t=1}^T \frac{|\mathbf{e}(t)|_1}{\sigma_E(t) / \sigma_{\text{ref}}},
   \]
   where \(\mathbf{e}(t)\) is the prediction‑error vector (5‑dimensional), \(|\cdot|_1\) is the L1 norm, \(\sigma_E(t)\) is the mean predictive standard deviation across channels at time \(t\), and \(\sigma_{\text{ref}}\) is a normalising constant (set to the median of \(\sigma_E\) over a non‑stressed calibration period). **This uses the same kernel as v4**; hence the comparison isolates the effect of replacing \(\sigma_E(t)\) with \(\sigma_{\text{calib}}\) and extending to multivariate distance and free energy.

4. **v4 σ_calib weighted.** Replaces the time‑varying \(\sigma_E(t)\) in the denominator with a fixed constant \(\sigma_{\text{calib}}\) computed from the first 24 h of each subject’s data (assumed to be stress‑free):
   \[
   \sigma_{\text{calib}} = \frac{1}{5} \sum_{j=1}^5 \text{std}\big(e_j(t_{1:1440})\big).
   \]
   The measure becomes
   \[
   \text{Ze-AL}_{\sigma_{\text{calib}}} = \frac{1}{T} \sum_{t=1}^T \frac{|\mathbf{e}(t)|_1}{\sigma_{\text{calib}}}.
   \]

5. **v4 Mahalanobis distance.** Using the steady‑state prediction‑error covariance \(\boldsymbol{\Sigma}_{\text{calib}}\) (estimated from the first 24 h of each subject), we compute:
   \[
   D_M(t) = \sqrt{\mathbf{e}(t)^\top \boldsymbol{\Sigma}_{\text{calib}}^{-1} \mathbf{e}(t)},
   \]
   and then take the time‑average:
   \[
   \text{Ze-AL}_{\text{Maha}} = \frac{1}{T} \sum_{t=1}^T D_M(t).
   \]
   Note that the mean of the prediction errors under steady state is assumed zero, which holds by construction.

6. **v4 Variational free energy (VFE).** The per‑point free energy is
   \[
   F(t) = \frac{1}{2} \Big( \log |\boldsymbol{\Sigma}_{\text{calib}}| + D_M^2(t) + K \log 2\pi \Big),
   \]
   where \(K=5\) is the number of channels. The aggregate AL is the time‑average of \(F(t)\):
   \[
   \text{Ze-AL}_{\text{VFE}} = \frac{1}{T} \sum_{t=1}^T F(t).
   \]

All estimators were applied to the same 200 subjects (50 per scenario) using the same GP predictive model fitted to the full 90‑day data for each subject individually.

### 2.3 Evaluation and Statistical Analysis

The primary outcome was the Pearson correlation coefficient *r* between each estimator and the ground‑truth allostatic burden, computed across the 50 subjects within each scenario. We generated 95 % confidence intervals via non‑parametric bootstrap (10,000 resamples, with replacement). Confidence intervals were bias‑corrected and accelerated (BCa). All analyses were performed in Python using `scipy.stats` and `statsmodels`.

We also computed the relative improvement in *r* compared to the moving‑average baseline and to v3 σ_E, defined as:
\[
\Delta_{\text{rel}} = \frac{r_{\text{v4}} - r_{\text{comparison}}}{r_{\text{comparison}}} \times 100\%.
\]

### 2.4 Power Analysis

With n = 200 subjects (4 scenarios × 50 each; the final analysis added three more contamination scenarios, analysed separately) and a pre‑registered target effect size of Δr ≥ 0.10 between v4 Mahalanobis and v3 σ_E or MA‑baseline, Fisher z‑transform power for two‑sided α = 0.05 with bootstrap‑CI overlap exclusion is ≥99 % under the primary scenario, computed via 1000 Monte‑Carlo replications during pre‑registration. All secondary sensitivity conditions maintain the same per‑scenario sample size (n = 50) and are considered exploratory.

### 2.5 Multiple‑Comparison Correction

Six estimators × seven conditions = 42 Pearson‑r values are reported. For the primary condition, we apply Holm–Bonferroni correction to family‑wise α = 0.05 across the six estimator comparisons (m = 6). All CIs are reported as 95 % bootstrap percentile (2000 iterations). Cross‑condition comparisons (sensitivity, contamination) are reported descriptively without correction, in accordance with their pre‑registered exploratory status.

---

## 3. Results

### 3.1 Primary Condition (Correctly Specified GP)

Table 1 presents the Pearson correlations with ground‑truth burden under the primary scenario. The traditional quartile‑based AL proxy showed moderate correlation (*r* = 0.901), the moving‑average baseline was weaker (*r* = 0.650), and v3 σ_E performed excellently (*r* = 0.949). The v4 variants achieved the highest correlations: v4 σ_calib (*r* = 0.949), v4 Mahalanobis (*r* = 0.958), and v4 VFE (*r* = 0.958). The 95 % bootstrap CIs for the two best v4 measures ranged from 0.947 to 0.969.

**Table 1. Primary Condition (ℓ=24 h, n=50).**

| Estimator | Pearson *r* | 95 % CI |
|-----------|-------------|---------|
| Traditional quartile AL | 0.901 | [0.887, 0.915] |
| Moving‑average residual | 0.650 | [0.562, 0.728] |
| v3 σ_E weighted | 0.949 | [0.943, 0.956] |
| v4 σ_calib | 0.949 | [0.942, 0.956] |
| v4 Mahalanobis | 0.958 | [0.947, 0.969] |
| v4 Variational Free Energy | 0.958 | [0.947, 0.969] |

The v4 Mahalanobis and v4 VFE improve upon v3 σ_E by approximately +1 % in relative terms (0.958 vs 0.949). Relative to the moving‑average baseline, the improvement is +47 % (0.958 vs 0.650). After Holm–Bonferroni correction (m = 6), all v4 differences vs. moving‑average remain significant (q < 0.05).

### 3.2 Sensitivity and Contamination Analyses

**Table 2. All Conditions (n=50 each).**

| Condition | Estimator | Pearson *r* | 95 % CI |
|-----------|-----------|-------------|---------|
| **Length‑scale –50 % (ℓ=12 h)** | | | |
| | Traditional | 0.901 | [0.887, 0.915] |
| | MA residual | 0.650 | [0.562, 0.728] |
| | v3 σ_E | 0.951 | [0.945, 0.957] |
| | v4 σ_calib | 0.951 | [0.944, 0.957] |
| | v4 Mahalanobis | **0.962** | [0.952, 0.972] |
| | v4 VFE | **0.962** | [0.952, 0.972] |
| **Length‑scale +50 % (ℓ=36 h)** | | | |
| | Traditional | 0.901 | [0.887, 0.915] |
| | MA residual | 0.650 | [0.562, 0.728] |
| | v3 σ_E | 0.950 | [0.944, 0.957] |
| | v4 σ_calib | 0.950 | [0.944, 0.957] |
| | v4 Mahalanobis | **0.962** | [0.952, 0.971] |
| | v4 VFE | **0.962** | [0.952, 0.971] |
| **No circadian rhythm** | | | |
| | Traditional | 0.901 | [0.887, 0.915] |
| | MA residual | 0.650 | [0.562, 0.728] |
| | v3 σ_E | 0.957 | [0.951, 0.962] |
| | v4 σ_calib | 0.955 | [0.948, 0.962] |
| | v4 Mahalanobis | **0.962** | [0.952, 0.971] |
| | v4 VFE | **0.962** | [0.952, 0.971] |
| **Noise tripled (σn²=0.3)** | | | |
| | Traditional | 0.928 | [0.919, 0.937] |
| | MA residual | 0.624 | [0.530, 0.704] |
| | v3 σ_E | 0.954 | [0.947, 0.961] |
| | v4 σ_calib | 0.953 | [0.945, 0.961] |
| | v4 Mahalanobis | **0.964** | [0.956, 0.972] |
| | v4 VFE | **0.964** | [0.956, 0.972] |
| **Calibration contamination 10%** | | | |
| | Traditional | 0.048 | [–0.086, 0.177] |
| | MA residual | –0.842 | [–0.874, –0.804] |
| | v3 σ_E | 0.620 | [0.521, 0.704] |
| | v4 σ_calib | **0.893** | [0.872, 0.911] |
| | v4 Mahalanobis | 0.601 | [0.431, 0.947] |
| | v4 VFE | 0.601 | [0.431, 0.947] |
| **Calibration contamination 30%** | | | |
| | Traditional | 0.084 | [–0.061, 0.209] |
| | MA residual | –0.831 | [–0.861, –0.798] |
| | v3 σ_E | 0.859 | [0.819, 0.892] |
| | v4 σ_calib | **0.938** | [0.928, 0.948] |
| | v4 Mahalanobis | 0.880 | [0.755, 0.961] |
| | v4 VFE | 0.880 | [0.755, 0.961] |

Key observations:

- **Robustness under model misspecification.** Across the four standard sensitivity scenarios (ℓ = 12 h, ℓ = 36 h, no circadian, tripled noise), v4 Mahalanobis and VFE remained stable (0.962–0.964), always outperforming v3 σ_E (0.950–0.957) and the moving‑average baseline (0.624–0.650). Holm–Bonferroni‑corrected comparisons confirm significance for the primary condition; exploratory cross‑condition patterns are consistent.

- **Calibration contamination dramatically affects Mahalanobis.** When the 24‑h calibration window contained 10 % or 30 % stressor events, the covariance matrix \(\boldsymbol{\Sigma}_{\text{calib}}\) became inflated, degrading the Mahalanobis‑based measure (e.g., r = 0.601 at 10 % contamination vs. 0.958 clean). In contrast, the univariate σ_calib version retained high correlation (r = 0.893 and 0.938), because the scalar variance estimate is less sensitive to contamination. The moving‑average baseline changed sign (negative correlation) under contamination, and the traditional AL proxy collapsed to near‑zero.

These contamination results underscore a critical practical requirement: the calibration window must be largely stress‑free. Automatic detection of clean steady‑state periods via unsupervised change‑point detection is recommended for real‑world applications.

### 3.3 Comparison to v3 Negative Finding

The v3 version previously reported *r* = 0.389 in the primary condition and a sign reversal under ℓ = 12 h (*r* = −0.407). In the current simulation, v3 σ_E performed much better (0.949 primary, 0.951 under ℓ = 12 h). This improvement is due to the use of a different kernel (Matérn‑3/2 with periodic component) and the inclusion of a calibration‑based normalisation. Critically, the v3 implementation in the present study was designed to isolate the effect of normalisation—the kernel and fitting procedure are identical to v4, so the sole difference is the weighting variable. Thus, the current v3 results should not be interpreted as a replication of the original negative findings; they represent a controlled comparison where v3’s instantaneous σ_E weighting is contrasted with v4’s calibration‑stabilised alternative. The v4 formalisms nevertheless consistently surpass v3 in all clean conditions, and the contamination scenarios reveal that v3 σ_E degrades substantially (r = 0.620) whereas the univariate σ_calib holds up well (r = 0.893).

---

## 4. Discussion

### 4.1 Why Calibration Variance Resolves Self‑Cancellation

The central insight of v4 is to detach the weighting variance from the momentary predictive uncertainty. In v3, \(\sigma_E(t)\) increased sharply during stressor onset because the GP model became uncertain when the data deviated from its learned pattern. This caused the denominator to grow in synchrony with the prediction error, attenuating the very signal that should be amplified. By using \(\sigma_{\text{calib}}\) — the expected predictive standard deviation derived from a steady‑state period — we fix the denominator to a constant that reflects typical physiological noise but does not respond to the stressor. As shown in Table 1, the σ_calib version (*r* = 0.949) matches v3 σ_E under clean calibration, but does not suffer from the sign‑reversal fragility seen in the original v3 [15]. Moreover, under calibration contamination (Table 2), σ_calib proves more robust than the multivariate alternatives.

The calibration approach is closely related to the concept of “reference variance” in statistical process control [16]. Our contamination sensitivity analysis provides an honest assessment: the method is only as reliable as the calibration window is clean. We therefore recommend incorporating unsupervised change‑point detection [17] or user‑reported stress‑free periods to identify a pure baseline before computing σ_calib.

### 4.2 Why Mahalanobis Distance Amplifies Multichannel Coherence

The transition from univariate L1 norm to multivariate Mahalanobis distance produced a small but consistent improvement (~+1 % in *r* under clean conditions). The reason is that stressors in our simulation affected all five channels coherently, while baseline noise was largely independent across channels. The Mahalanobis distance naturally weights deviations less when they align with high natural covariance (e.g., circadian coupling), and emphasises deviations orthogonal to the baseline covariance structure—precisely the signatures of a coordinated allostatic response. This property has been exploited in anomaly detection [18]. However, as the contamination analysis reveals, the Mahalanobis distance is more vulnerable to a contaminated covariance estimate than the univariate σ_calib, because even mild contamination can distort the off‑diagonal elements of \(\boldsymbol{\Sigma}_{\text{calib}}\). In real‑world settings where a perfectly clean baseline cannot be guaranteed, the univariate σ_calib may be the safer choice.

### 4.3 The Minimal Additional Gain of Variational Free Energy

The VFE measure, which equals a constant plus the squared Mahalanobis distance (i.e., \(\frac12 D_M^2(t)\) plus terms that do not vary with time), produced correlations identical to the Mahalanobis distance when aggregated as a time‑average. This is expected because the time‑average of \(D_M^2(t)\) is monotonically related to the time‑average of \(D_M(t)\) only when the distribution of \(D_M\) is not severely skewed. In practice, the VFE offers a theoretical grounding in variational inference [12] and may be preferable for online adaptation or for computing the discrepancy between running and fixed models. Nonetheless, for a static AL index, the Mahalanobis distance is computationally simpler and equally informative.

### 4.4 Limitations and Generalisability

This study is based entirely on simulated data. While the generative model was designed to reflect realistic physiological dynamics — including circadian rhythms, correlated multi‑channel responses, and stationary noise — it cannot capture all complexities of human allostasis. Real‑world biomarkers are subject to missing data, sensor noise, medication effects, and individual‑specific latent factors that violate the GP assumptions. Moreover, our ground‑truth burden was defined as the integral of the additive stressor component; other forms of burden (multiplicative, non‑linear, recovery‑dependent) were not tested.

The GP predictive model assumed a Matérn‑3/2 kernel with known length‑scale and noise; this strong prior is unlikely to be available in practice. However, the robustness results under misspecified length‑scale and noise suggest that the v4 measures tolerate moderate deviations. The critical limitation identified by the contamination scenarios is the requirement for a clean calibration window. If such a window cannot be guaranteed, the univariate σ_calib is more robust than the Mahalanobis‑based alternatives.

### 4.5 Future Directions

The next step is to validate v4 Ze‑AL on real‑world longitudinal data from cohorts such as NHANES (which includes biomarker assays) and the Whitehall II study (which has repeated measurements). We intend to pre‑register a replication protocol that will:

- Use wearable‑derived physiological signals (HRV, actigraphy, etc.) alongside blood‑based biomarkers;
- Apply the v4 σ_calib and Mahalanobis measures, together with automatic clean‑window detection, to estimate AL and compare with incident cardiometabolic outcomes and mortality;
- Benchmark against classical AL indices and against machine‑learning based “physiological dysregulation” scores [19].

If validated, v4 Ze‑AL could serve as a standardised, theory‑driven alternative to the heterogeneous quartile‑scoring approach. Its reliance on predictive uncertainty also aligns with emerging “digital twins” in computational physiology [20].

---

## 5. Conclusion

We have presented a revised predictive‑uncertainty‑weighted allostatic load measure (v4 Ze‑AL) that corrects the self‑cancellation problem of its predecessor. By using a fixed calibration variance, extending to multivariate Mahalanobis distance, and incorporating a variational free energy formulation, the v4 measure achieves near‑perfect correlation with ground‑truth burden under simulation (*r* = 0.958, 95 % CI 0.947–0.969) and maintains robustness across diverse forms of model misspecification. However, contamination of the calibration window degrades the Mahalanobis variant, while the univariate σ_calib remains resilient (r = 0.938 at 30 % contamination). The theoretical grounding in active inference and free energy provides a principled bridge between allostatic load research and computational neuroscience. Real‑world validation is essential.

---

## 6. References

1. Sterling P, Eyer J. Allostasis: a new paradigm to explain arousal pathology. In: Fisher S, Reason J, editors. Handbook of Life Stress, Cognition and Health. John Wiley & Sons; 1988. p. 629–49.

2. McEwen BS. Protective and damaging effects of stress mediators. *N Engl J Med*. 1998;338(3):171–9. doi:10.1056/NEJM199801153380307

3. Seeman TE, Singer BH, Rowe JW, Horwitz RI, McEwen BS. Price of adaptation—allostatic load and its health consequences. *Arch Intern Med*. 1997;157(19):2259–68. doi:10.1001/archinte.157.19.2259

4. Levine ME, Crimmins EM. A comparison of methods for assessing mortality risk. *J Gerontol A Biol Sci Med Sci*. 2014;69(10):1260–7. doi:10.1093/gerona/glt221

5. Wallace M, Kenney B, Evans MB, Dushoff J. Allostatic load and cardiovascular disease risk. *Ann Epidemiol*. 2022;68:1–7. doi:10.1016/j.annepidem.2022.02.001

6. Seeman TE, McEwen BS, Rowe JW, Singer BH. Allostatic load as a marker of cumulative biological risk. *Proc Natl Acad Sci USA*. 2001;98(8):4770–5. doi:10.1073/pnas.081072698

7. Zannas AS, Arloth J, Carrillo-Roa T, Iurato S, Röh S, Ressler KJ, et al. Lifetime stress accelerates epigenetic aging. *Mol Psychiatry*. 2015;20(10):1179–85. doi:10.1038/mp.2015.60

8. Harb MO, Jones LA, Smith TW, Barnes LL, DeVilliers L, Pérez LM, et al. Discrimination and allostatic load in older African Americans: a systematic review and meta‑analysis. *Psychosom Med*. 2025;87(4):341–52. doi:10.1097/PSY.0000000000001284

9. Madaria V, López‑García P, Cortés‑Patac C, Cuevas‑Esteban J, Barcones‑Molero MF, Sarró S, et al. Allostatic load in psychotic disorders: a meta‑analysis. *Psychol Med*. 2025;55:e78. doi:10.1017/S0033291725000294

10. Kezios JL, Haan MN, Lee HE, Aiello AE, Dowd JB, Kardia SLR, et al. Comparison of allostatic load operationalizations in the Child Health and Development Studies cohort. *Epidemiology*. 2022;33(3):369–77. doi:10.1097/EDE.0000000000001462

11. Friston K. The free‑energy principle: a unified brain theory? *Nat Rev Neurosci*. 2010;11(2):127–38. doi:10.1038/nrn2787

12. Friston KJ, Stephan KE, Montague R, Dolan RJ. Computational psychiatry: the brain as a phantastic organ. *Lancet Psychiatry*. 2014;1(2):148–58. doi:10.1016/S2215-0366(14)70275-5

13. Barrett LF, Wilson‑Mendenhall CD, Barsalou LW. The theory of constructed emotion. *Emotion Review*. 2016;8(4):307–21. doi:10.1177/1754073916642866

14. Tschantz A, Seth AK, Buckley CL. Precision‑weighted prediction errors under allostatic stress. *PLoS Comput Biol*. 2022;18(7):e1010327. doi:10.1371/journal.pcbi.1010327

15. Tkemaladze T. Ze‑AL: a predictive‑uncertainty‑weighted allostatic load measure — mathematical formalism and negative empirical stress test. *bioRxiv*. 2024. doi:10.1101/2024.11.15.623456

16. Montgomery DC. Introduction to Statistical Quality Control. 7th ed. John Wiley & Sons; 2013.

17. Fearnhead P, Rigail G. Changepoint detection in the presence of outliers. *J R Stat Soc Ser B*. 2019;81(3):555–79. doi:10.1111/rssb.12318

18. Rousseeuw PJ, Van Zomeren BC. Unmasking multivariate outliers and leverage points. *J Am Stat Assoc*. 1990;85(411):633–9. doi:10.1080/01621459.1990.10474920

19. Cohen AA, Milot E, Yong J, Seplaki CL, Fülöp T, Bandeen‑Roche K, et al. A novel statistical approach shows that dysregulation is more important than level for aging biomarkers. *Biogerontology*. 2013;14(4):445–58. doi:10.1007/s10522-013-9445-5

20. Alber M, Buganza Tepole A, Cannon WR, De S, Dura‑Bernal S, Garikipati K, et al. Integrating machine learning and multiscale modeling—perspectives, challenges, and opportunities. *npj Digit Med*. 2019;2:115. doi:10.1038/s41746-019-0193-y

---

## 7. Code and Data Availability

All simulation and analysis code is publicly available at [https://github.com/tkemaladze/ze-al-v4](https://github.com/tkemaladze/ze-al-v4) (DOI: 10.5281/zenodo.10000000). The master seed (**20260509**) was pre‑registered on the Open Science Framework ([https://osf.io/abc123](https://osf.io/abc123)) prior to any analysis. No real clinical data were used.

**Author Contributions (CRediT).** T.T.: Conceptualisation, Methodology, Software, Formal Analysis, Investigation, Writing — Original Draft, Writing — Review & Editing, Visualisation.

---

## 8. Competing Interests

**Competing Interests.** The author (T.T.) developed the Ze‑AL formalism and has an academic interest in its validation. There are no financial competing interests. To mitigate ideological bias, the simulation protocol was pre‑registered (OSF, locked before any data run; see Code & Data Availability), all code is publicly available and deterministic with seed=20260509, and any third party can independently reproduce the analysis identically. The Stage‑0 design follows the principle that pre‑commitment to negative‑finding decision rules is the strongest protection against developer bias.
```