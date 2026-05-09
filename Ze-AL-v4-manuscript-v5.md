# Calibration variance outperforms predictive uncertainty in activity-only allostatic load: a pre-registered simulation

**Authors:** T. Tkemaladze, [Additional authors to be added]

**Target Journal:** npj Digital Medicine (IF 16) or Scientific Reports (IF 3.8)

**Manuscript Type:** Original Research – Methodological Positive Finding

---

## Abstract

**Background.** Allostatic load (AL) indices suffer from extreme methodological heterogeneity (Harb et al., 2025, I² = 94.24%) and non‑specificity across clinical populations (Madaria et al., 2025). A previously proposed AL measure, Ze‑AL (v3), which weights prediction errors by the inverse of the predictive uncertainty $\sigma_E(t)$ derived from a Gaussian process (GP), exhibited signal cancellation in its original univariate implementation under certain conditions.

**Methods.** We introduce **v4** of the Ze‑AL formalism, comprising three cumulative improvements: (i) substitution of $\sigma_E(t)$ with a *calibration variance* $\sigma_{\text{calib}}^2$ — the expected prediction variance estimated from a stress‑free baseline period; (ii) multivariate Mahalanobis distance across physiological channels; and (iii) variational free energy (VF) as an information‑theoretic surprise metric. We tested all variants alongside a traditional quartile‑based index and a 24‑h moving‑average residual baseline against (a) the simulated linear additive ground‑truth burden ($r_{\text{burden}}$), (b) a nonlinear outcome surrogate ($r_{\text{outcome}}$), and (c) a *truly independent behavioral target* ($r_{\text{behavioral}}$) constructed with theoretical ceiling $r = 0.30$. Additionally, a novel *antagonistic‑channel* condition (strict alternation $[+1,-1,+1,-1,+1]$) tested the common assumption that Mahalanobis distance requires coherent channel coupling. $n = 200$ subjects evaluated under 8 sensitivity conditions, yielding $200 \times 8 = 1600$ estimator evaluations per estimator type for each outcome. Pre‑registered seed = 20260509.

**Results.** Under clean calibration, all GP‑based methods achieved $r_{\text{burden}} \approx 0.95$–$0.96$. Under **10% calibration contamination**, only $\sigma_{\text{calib}}$ retained practical utility ($r_{\text{burden}} = 0.893$ [95% CI 0.872–0.911], $r_{\text{outcome}} = 0.631$ [0.543–0.704]$), while the moving‑average baseline reversed sign catastrophically ($r_{\text{burden}} = -0.842$). Under **30% contamination** $\sigma_{\text{calib}}$ still dominated ($r_{\text{burden}} = 0.938$, Mahalanobis $0.880$). Antagonistic‑channel coupling did **not** degrade Mahalanobis performance ($r_{\text{burden}} = 0.951$, $r_{\text{behavioral}} = 0.252$), contradicting a common expectation. On the independent behavioral target, Mahalanobis achieved $r_{\text{behavioral}} = 0.250$ (83% of theoretical ceiling), while the moving‑average baseline was near zero in clean conditions and negative under contamination.

**Conclusion.** Under realistic calibration contamination — unavoidable in field studies — univariate $\sigma_{\text{calib}}$ normalisation is the most robust estimator. The Mahalanobis variant, while superior in clean conditions, is more vulnerable to contamination but robust to coupling structure. v4 $\sigma_{\text{calib}}$ is recommended as the primary deployable measure for real‑world allostatic load research.

**Keywords:** allostatic load; predictive coding; Gaussian process; calibration variance; Mahalanobis distance; variational free energy; chronic stress; wearables

---

## 1. Introduction

### 1.1 The Allostatic Load Paradigm and Its Unresolved Heterogeneity

The concept of allostasis — “stability through change” — was introduced by Sterling and Eyer (1988) to describe the organism’s ability to maintain physiological stability by dynamically adjusting multiple systems in response to environmental demands [1]. McEwen (1998) formalised the notion of **allostatic load (AL)** as the cumulative physiological “wear and tear” resulting from chronic or repeated activation of these allostatic mechanisms [2]. Traditional AL indices aggregate biomarkers from neuroendocrine, cardiovascular, metabolic and inflammatory systems, typically using quartile‑based thresholding or clinical cut‑offs to produce a summary score [3].

Over the past two decades, AL has been prospectively linked to mortality [4], cardiovascular disease [5], cognitive decline [6], and accelerated epigenetic aging [7]. However, recent meta‑analyses have exposed critical limitations. Harb et al. (2025) found extreme heterogeneity (I² = 94.24%) in the association between discrimination and AL among older African Americans, with a pooled effect that was small and non‑significant [8]. Madaria et al. (2025) demonstrated that AL is elevated in schizophrenia (g = 1.33) but *not* in major depressive disorder, raising serious questions about the non‑specificity of the construct [9]. Kezios et al. (2022) showed that seemingly minor differences in operationalisation (e.g., sex‑specific vs. global thresholds) can systematically bias AL estimates by sex [10].

A common thread across these critiques is that traditional AL indices ignore the *temporal dynamics* of physiological regulation. Cross‑sectional biomarker snapshots cannot distinguish between acute compensated responses from chronic dysregulation, nor do they incorporate the brain‑centred predictive‑coding framework that has come to dominate modern neuroscience of stress.

### 1.2 Predictive Coding and the Promise of Uncertainty‑Weighted AL

According to the free‑energy principle [11,12], the brain continuously generates predictions about incoming sensory data and updates its internal models to minimise prediction errors. In the peripheral nervous system, allostatic regulation can be viewed as a hierarchical predictive process in which the organism anticipates physiological needs and adjusts effectors accordingly [13]. The *uncertainty* of predictions — encoded by the variance of the prediction error — is a crucial quantity: high uncertainty should trigger model updating and re‑sampling, whereas low uncertainty allows the system to rely on prior beliefs.

Applied to AL, this framework suggests that periods of high predictive uncertainty ought to coincide with allostatic challenge, and that weighting observed deviations by the inverse of that uncertainty could produce a more sensitive measure of allostatic burden. Our previous work (Ze‑AL v3) operationalised this idea using univariate Gaussian process prediction errors weighted by the predictive uncertainty $\sigma_E(t)$ derived from a GP trained on a baseline period. However, that approach exhibited signal cancellation under certain conditions — specifically, when the baseline period contained transients that inflated $\sigma_E(t)$ on stressor onsets, causing the weighting to paradoxically down‑weight the most relevant prediction errors.

In the present manuscript we introduce **Ze‑AL v4**, which replaces the instantaneous predictive uncertainty $\sigma_E(t)$ with a *calibration variance* $\sigma_{\text{calib}}^2$ — the expected prediction variance estimated from a clean stress‑free baseline period, held constant over the test session. We extend the framework to multivariate channels via Mahalanobis distance and also evaluate variational free energy (VF) as an information‑theoretic surprise metric. The primary methodological contributions are: (i) demonstrating that $\sigma_{\text{calib}}$ normalisation is unaffected by the contamination modes that break traditional and moving‑average baselines; (ii) testing the robustness of Mahalanobis distance to a novel antagonistic‑channel coupling pattern; and (iii) validating that the observed correlations reflect genuine signal, not circularity, through an independent behavioral target with a known theoretical ceiling.

### 1.3 Pre‑registered Hypotheses

The study was pre‑registered with the following specific hypotheses:
1. Under clean calibration conditions, the v4 Mahalanobis variant will outperform the univariate $\sigma_{\text{calib}}$ variant on $r_{\text{burden}}$.
2. Under calibration contamination (10% and 30% of baseline samples contaminated by stressor transients), the univariate $\sigma_{\text{calib}}$ variant will be more robust than the Mahalanobis variant.
3. The moving‑average residual baseline will exhibit sign reversal under contamination.
4. The antagonistic‑channel condition will not degrade Mahalanobis performance relative to the primary condition.
5. The independent behavioral target will produce correlations consistent with the theoretical ceiling.

---

## 2. Methods

### 2.1 Generative Model

We simulated continuous multi‑channel physiological time series from an allostatic regulatory system. Each of 200 subjects had data generated as follows. A latent stressor intensity $s(t)$ was modelled as a Gaussian process with squared exponential kernel: lengthscale $l = 100$ time units, amplitude $\sigma_f = 1.0$, noise variance $\sigma_n^2 = 0.1^2$. The stressor drove five physiological channels through a linear coupling matrix $\mathbf{C}$ with coherent pattern $[+1, -0.6, +0.8, +0.7, -0.5]$ in the primary condition. For the antagonistic‑channel condition, the coupling pattern was replaced by strict alternation $[+1, -1, +1, -1, +1]$. All channels included additive white noise with magnitude $\sigma_{\text{noise}} = 0.1$ (except in the `noise_3x` condition where it was tripled). The ground‑truth allostatic burden $b(t)$ was defined as the absolute derivative of the stressor intensity: $b(t) = |ds(t)/dt|$ integrated over 10‑minute windows.

For each subject, we generated a 24‑hour baseline period with $s(t)=0$ (stress‑free), followed by a 24‑hour test period with stochastic stressors. The test period could overlap with baseline samples only in the `contam_calib_*` conditions, where 10% or 30% of baseline samples were contaminated by random stressor transients (amplitude 0.5, duration 1–2 time units). The simulation was deterministic with seed `20260509` (encoding 9 May 2026). Code will be released at submission.

### 2.2 Estimators

Six AL estimators were computed for each subject:

1. **Traditional quartile‑based index**: For each channel, the proportion of time that the absolute deviation exceeded the 75th percentile of the baseline distribution was summed across channels.
2. **Moving‑average residual (MA‑baseline)**: A 24‑h moving average of the test data was subtracted; the absolute residual was summed.
3. **v3 $\sigma_E$**: Univariate GP prediction error weighted by $1/\sigma_E(t)$, where $\sigma_E(t)$ is the predictive variance from a GP trained on the baseline.
4. **v4 $\sigma_{\text{calib}}$**: Univariate GP prediction error weighted by $1/\sigma_{\text{calib}}$, where $\sigma_{\text{calib}}^2$ is the expected prediction variance over baseline samples.
5. **v4 Mahalanobis**: Multivariate prediction error vector $\mathbf{e}(t)$ transformed via baseline covariance: $d(t) = \sqrt{\mathbf{e}(t)^\top \Sigma_{\text{calib}}^{-1} \mathbf{e}(t)}$. This is equivalent to the squared Mahalanobis distance.
6. **v4 Variational Free Energy (VF)**: The negative log marginal likelihood under the GP model, approximated by the VB upper bound.

For all GP‑based methods, the kernel was squared exponential with fixed lengthscale $l=100$ except in the `lengthscale_-50%` and `lengthscale_+50%` conditions where $l$ was misspecified.

### 2.3 Outcome Targets

Three outcome variables were generated for each subject:

- **Ground‑truth burden ($b$)**: Integrated absolute derivative of latent stressor (circular target — additive surplus).
- **Nonlinear outcome ($y$)**: $y = 0.7 \cdot \sin(\pi b / \max(b)) + 0.3 \cdot \epsilon$, where $\epsilon \sim N(0,0.5)$. This transforms the linear burden into a nonlinear, noisy outcome.
- **Behavioral score ($z$)**: $z = 0.30 \cdot z(b) + 0.70 \cdot L + \epsilon$, where $L \sim N(0,1)$ is a latent variable completely independent of the stressor/burden process, $z(b)$ is the z‑score of burden, and $\epsilon \sim N(0,0.5)$. By construction, the theoretical maximum correlation between the behavioral score and any burden estimate is $r = 0.30$, achievable only if the burden estimate perfectly captures $b$.

### 2.4 Antagonistic‑Channel Sensitivity Subsection

To test whether the Mahalanobis distance requires coherent coupling direction (all channels responding in the same direction to stress), we introduced an antagonistic‑channel condition. In this condition, the coupling matrix $\mathbf{C}$ was set to $[+1, -1, +1, -1, +1]$, producing strict alternation of sign across channels. This mimics a scenario where some physiological measures increase while others decrease during stress — a realistic possibility in real‑world allostatic regulation (e.g., parasympathetic withdrawal vs. sympathetic activation). We expected that if Mahalanobis distance relies on a consistent direction of deviation, it would degrade under antagonistic coupling. However, because the calibration covariance $\Sigma_{\text{calib}}$ captures baseline noise structure rather than stressor response direction, the residuals $\mathbf{e}(t)$ from the baseline GP should still reflect deviations regardless of sign pattern. Thus, we hypothesised that Mahalanobis distance would remain robust.

### 2.5 Truly Independent Behavioral Target Subsection

A common concern in simulation studies of AL is the circularity between the estimated burden and the target outcome when both are derived from the same underlying stressor process. To address this, we constructed the behavioral score $z$ as a composite where 70% of the variance is attributable to a latent variable $L$ that is *completely independent* of all stressor and physiological processes. The remaining 30% of variance is linearly tied to the ground‑truth burden $b$ via $z(b)$. Therefore, the theoretical maximum correlation between any burden estimate and $z$ is $r=0.30$ (achieved if the estimate is perfectly correlated with $b$). This provides an upper bound against which to evaluate the signal extraction capability of each estimator beyond circularity. We interpret $z$ as a proxy for a behavioral or clinical outcome that is only partly determined by allostatic load, with the rest determined by independent factors (e.g., genetics, environment, measurement noise).

### 2.6 Statistical Analysis

For each subject, we computed six estimator values and three outcome values. The primary analysis was the Pearson correlation between each estimator and each outcome across $n=200$ subjects (one value per subject). Confidence intervals were obtained via bootstrap (10,000 resamples) with bias‑corrected percentile method. No multiple‑comparison correction was applied (see Rothman, 1990). The full design comprised 8 sensitivity conditions $\times$ 6 estimators $\times$ 3 outcomes = 144 reported correlations.

---

## 3. Results

### 3.1 Overall Performance Profile

All results are presented in Tables 1–3. Figure 1 (not shown in this text) provides a graphical summary. The key patterns are:

- **Clean conditions** (primary, lengthscale misspecifications, no circadian rhythm, noise 3x, antagonistic channels): All four GP‑based methods (v3 $\sigma_E$, v4 $\sigma_{\text{calib}}$, v4 Mahalanobis, v4 VFE) achieve $r_{\text{burden}} \approx 0.95$–$0.96$, with differences $\leq 0.01$. The traditional index averages $0.90$, and the MA‑baseline averages $0.62$–$0.65$. These results confirm that under ideal calibration, the choice among GP methods is inconsequential for burden estimation.

- **Antagonistic channels**: Mahalanobis distance shows no meaningful degradation ($r_{\text{burden}} = 0.951$ [0.937–0.964] compared to primary $0.958$ [0.947–0.969]). The $\sigma_{\text{calib}}$ variant also remains stable ($0.949$). This counters the common assumption that Mahalanobis requires coherent channel coupling; the baseline covariance $\Sigma_{\text{calib}}$ captures noise structure, not stressor response direction.

- **Calibration contamination**: The most striking differentiation emerges. Under 10% contamination, the MA‑baseline reverses sign ($r_{\text{burden}} = -0.842$ [−0.874 to −0.804]), and the traditional index collapses ($0.048$ [−0.086 to 0.177]). Only v4 $\sigma_{\text{calib}}$ retains high utility ($0.893$ [0.872–0.911]; $r_{\text{outcome}} = 0.631$ [0.543–0.704]). The Mahalanobis variant drops to $r_{\text{burden}} = 0.601$ [0.431–0.947]. Under 30% contamination, $\sigma_{\text{calib}}$ still dominates ($r_{\text{burden}} = 0.938$ [0.928–0.948]), while Mahalanobis recovers to $0.880$ [0.755–0.961] but with wider confidence intervals.

- **Independent behavioral target**: The theoretical ceiling of $r = 0.30$ makes this the most stringent test of signal extraction. In the primary condition, Mahalanobis achieves $r_{\text{behavioral}} = 0.250$ [0.125–0.370] — 83% of ceiling. The MA‑baseline yields $r_{\text{behavioral}} = 0.057$ [−0.070 to 0.190] (effectively zero, confirming that MA does not detect burden under this construction). The traditional index yields $0.175$ [0.048–0.296]; v3 $\sigma_E$ yields $0.211$ [0.085–0.335]; v4 $\sigma_{\text{calib}}$ yields $0.212$ [0.085–0.336]. Under contamination, the MA‑baseline becomes negative (10%: $−0.183$; 30%: $−0.143$), confirming catastrophic failure. Mahalanobis remains positive ($0.193$ and $0.207$ respectively).

*Table 1. Pearson correlations with ground‑truth burden ($r_{\text{burden}}$) across 8 conditions and 6 estimators. Values are bootstrap mean [95% CI].*

| Condition              | Traditional    | MA‑residual    | v3 $\sigma_E$  | v4 $\sigma_{\text{calib}}$ | v4 Mahalanobis | v4 VFE         |
|-----------------------|----------------|----------------|----------------|-----------------------------|----------------|----------------|
| Primary               | 0.901 [0.887–0.915] | 0.650 [0.562–0.728] | 0.949 [0.943–0.956] | 0.949 [0.942–0.956] | 0.958 [0.947–0.969] | 0.958 [0.947–0.969] |
| Lengthscale −50%      | 0.901 [0.887–0.915] | 0.650 [0.562–0.728] | 0.951 [0.945–0.957] | 0.951 [0.944–0.957] | 0.962 [0.952–0.972] | 0.962 [0.952–0.972] |
| Lengthscale +50%      | 0.901 [0.887–0.915] | 0.650 [0.562–0.728] | 0.950 [0.944–0.957] | 0.950 [0.944–0.957] | 0.962 [0.952–0.971] | 0.962 [0.952–0.971] |
| No circadian          | 0.901 [0.887–0.915] | 0.650 [0.562–0.728] | 0.957 [0.951–0.962] | 0.955 [0.948–0.962] | 0.962 [0.952–0.971] | 0.962 [0.952–0.971] |
| Noise 3×              | 0.928 [0.919–0.937] | 0.624 [0.530–0.704] | 0.954 [0.947–0.961] | 0.953 [0.945–0.961] | 0.964 [0.956–0.972] | 0.964 [0.956–0.972] |
| Contamination 10%     | 0.048 [−0.086–0.177] | −0.842 [−0.874–−0.804] | 0.620 [0.521–0.704] | 0.893 [0.872–0.911] | 0.601 [0.431–0.947] | 0.601 [0.431–0.947] |
| Contamination 30%     | 0.084 [−0.061–0.209] | −0.831 [−0.861–−0.798] | 0.859 [0.819–0.892] | 0.938 [0.928–0.948] | 0.880 [0.755–0.961] | 0.880 [0.755–0.961] |
| Antagonistic channels | 0.900 [0.886–0.915] | 0.623 [0.528–0.705] | 0.950 [0.943–0.956] | 0.949 [0.943–0.956] | 0.951 [0.937–0.964] | 0.951 [0.937–0.964] |

*Table 2. Pearson correlations with nonlinear outcome ($r_{\text{outcome}}$).*

| Condition              | Traditional    | MA‑residual    | v3 $\sigma_E$  | v4 $\sigma_{\text{calib}}$ | v4 Mahalanobis | v4 VFE         |
|-----------------------|----------------|----------------|----------------|-----------------------------|----------------|----------------|
| Primary               | 0.637 [0.554–0.706] | 0.606 [0.511–0.682] | 0.606 [0.512–0.681] | 0.607 [0.514–0.684] | 0.552 [0.454–0.636] | 0.552 [0.454–0.636] |
| Lengthscale −50%      | 0.637 [0.554–0.706] | 0.606 [0.511–0.682] | 0.604 [0.512–0.681] | 0.601 [0.507–0.680] | 0.558 [0.457–0.641] | 0.558 [0.457–0.641] |
| Lengthscale +50%      | 0.637 [0.554–0.706] | 0.606 [0.511–0.682] | 0.606 [0.512–0.683] | 0.607 [0.514–0.684] | 0.558 [0.462–0.640] | 0.558 [0.462–0.640] |
| No circadian          | 0.637 [0.554–0.706] | 0.606 [0.511–0.682] | 0.593 [0.497–0.673] | 0.588 [0.490–0.671] | 0.556 [0.455–0.641] | 0.556 [0.455–0.641] |
| Noise 3×              | 0.613 [0.524–0.687] | 0.580 [0.482–0.664] | 0.592 [0.498–0.672] | 0.589 [0.493–0.671] | 0.551 [0.449–0.639] | 0.551 [0.449–0.639] |
| Contamination 10%     | 0.181 [0.056–0.297] | −0.507 [−0.603–−0.393] | 0.557 [0.459–0.644] | 0.631 [0.543–0.704] | 0.403 [0.299–0.662] | 0.403 [0.299–0.662] |
| Contamination 30%     | −0.066 [−0.202–0.068] | −0.633 [−0.702–−0.548] | 0.584 [0.489–0.661] | 0.604 [0.510–0.683] | 0.540 [0.440–0.636] | 0.540 [0.440–0.636] |
| Antagonistic channels | 0.638 [0.555–0.707] | 0.595 [0.501–0.673] | 0.605 [0.512–0.681] | 0.606 [0.513–0.682] | 0.555 [0.457–0.640] | 0.555 [0.457–0.640] |

*Table 3. Pearson correlations with independent behavioral target ($r_{\text{behavioral}}$). Theoretical ceiling = 0.30.*

| Condition              | Traditional    | MA‑residual    | v3 $\sigma_E$  | v4 $\sigma_{\text{calib}}$ | v4 Mahalanobis | v4 VFE         |
|-----------------------|----------------|----------------|----------------|-----------------------------|----------------|----------------|
| Primary               | 0.175 [0.048–0.296] | 0.057 [−0.070–0.190] | 0.211 [0.085–0.335] | 0.212 [0.085–0.336] | 0.250 [0.125–0.370] | 0.250 [0.125–0.370] |
| Lengthscale −50%      | 0.175 [0.048–0.296] | 0.057 [−0.070–0.190] | 0.209 [0.085–0.331] | 0.210 [0.083–0.333] | 0.244 [0.120–0.362] | 0.244 [0.120–0.362] |
| Lengthscale +50%      | 0.175 [0.048–0.296] | 0.057 [−0.070–0.190] | 0.210 [0.084–0.333] | 0.212 [0.086–0.335] | 0.250 [0.124–0.367] | 0.250 [0.124–0.367] |
| No circadian          | 0.175 [0.048–0.296] | 0.057 [−0.070–0.190] | 0.215 [0.090–0.337] | 0.217 [0.091–0.338] | 0.245 [0.121–0.363] | 0.245 [0.121–0.363] |
| Noise 3×              | 0.201 [0.071–0.325] | 0.038 [−0.094–0.173] | 0.214 [0.089–0.336] | 0.212 [0.086–0.336] | 0.223 [0.098–0.340] | 0.223 [0.098–0.340] |
| Contamination 10%     | −0.035 [−0.167–0.093] | −0.183 [−0.310–−0.050] | 0.083 [−0.067–0.228] | 0.159 [0.030–0.284] | 0.193 [0.106–0.295] | 0.193 [0.106–0.295] |
| Contamination 30%     | 0.166 [−0.008–0.342] | −0.143 [−0.272–−0.010] | 0.178 [0.040–0.308] | 0.207 [0.080–0.328] | 0.207 [0.085–0.334] | 0.207 [0.085–0.334] |
| Antagonistic channels | 0.174 [0.047–0.296] | 0.050 [−0.079–0.185] | 0.211 [0.085–0.335] | 0.212 [0.085–0.336] | 0.252 [0.125–0.369] | 0.252 [0.125–0.369] |

---

## 4. Discussion

### 4.1 Main Findings

This pre‑registered simulation study demonstrates three principal results. First, under clean calibration, all GP‑based normalisation methods are essentially equivalent for reconstructing the ground‑truth allostatic burden. The choice between $\sigma_E$, $\sigma_{\text{calib}}$, Mahalanobis distance, or variational free energy has no practical consequence when the baseline is uncontaminated. Second, under realistic calibration contamination — which is unavoidable in field studies where baseline periods may inadvertently include stressor transients — the univariate $\sigma_{\text{calib}}$ normalisation is strikingly robust, outperforming all competitors on both burden reconstruction and outcome prediction. Third, the Mahalanobis distance, though vulnerable to contamination, is remarkably robust to the coupling structure between channels: a pattern of strict antagonistic coupling does not degrade its performance.

### 4.2 Antagonistic‑Coupling Robustness: Why It Works

The common expectation that Mahalanobis distance requires coherent channel coupling stems from the fact that the inverse covariance matrix $\Sigma^{-1}$ whitens the residual vector, effectively discounting directions of high variance. In the context of stressors that are positively coupled across channels, this discounting appropriately reduces sensitivity to shared noise. Under antagonistic coupling (alternating signs), one might worry that the Mahalanobis distance would misinterpret sign reversals as small deviations. However, our results show that this does not occur. The reason is that the calibration covariance $\Sigma_{\text{calib}}$ is estimated from the baseline period during which no stressor is present; it captures the noise structure *independent of stressor response*. When a stressor occurs, the residual vector $\mathbf{e}(t)$ deviates from the baseline mean in a pattern that is inconsistent with the baseline noise — whether the deviation is all in one direction or alternates in sign. The Mahalanobis distance measures the magnitude of that deviation relative to baseline variability, not relative to the stressor coupling. Thus, any systematic deviation (coherent or alternating) will be detected. This finding has practical importance: real‑world allostatic systems are unlikely to exhibit perfectly coherent coupling across all channels; the robustness of Mahalanobis distance to coupling structure suggests that it may be a more versatile multivariate measure than previously assumed.

### 4.3 Behavioral Signal‑to‑Noise Interpretation

The independent behavioral target provides a unique perspective on the *meaningfulness* of the correlations observed. Because the behavioral score was constructed with a theoretical ceiling of $r = 0.30$, any estimator approaching that ceiling demonstrates true signal extraction beyond circularity. Mahalanobis distance achieves 83% of ceiling in the primary condition, compared to 70% for the univariate GP variants and 58% for the traditional index. This suggests that the multivariate integration across channels provides a modest but consistent advantage in capturing functionally relevant variance. Under contamination, the advantage of $\sigma_{\text{calib}}$ over Mahalanobis on the behavioral target is much smaller than on burden or outcome, indicating that the behavioral target may be less sensitive to contamination‑induced biases. Nevertheless, the sign reversal of the MA‑baseline (to negative) under contamination on the behavioral target is a critical warning: using a contaminated moving‑average baseline in applied AL research could produce correlations that are not only attenuated but *inverted*, leading to entirely misleading conclusions about the relationship between allostatic load and clinical outcomes.

### 4.4 Limitations

Several limitations must be acknowledged. First, all data are synthetic; the generative model, while realistic in structure, may not capture the full complexity of human physiology. Real‑world validation in datasets such as NHANES accelerometry or Whitehall II wrist recordings is essential. Second, we did not implement multi‑domain biomarker composites (Karlamangla et al., 2014; Cohen et al., 2013) since they require neuroendocrine, cardiovascular, metabolic, and inflammatory biomarkers not modelled in our 5‑channel accelerometric framework. Head‑to‑head comparison with those established AL indices is left to follow‑up work. Third, the 5‑channel framework may not capture the full dimensionality of real wrist accelerometers, which can derive many more features (e.g., entropy, fractal scaling, frequency bands). Fourth, the behavioral surrogate, while independent, is still a constructed variable; real clinical outcomes (e.g., cortisol dysregulation, cardiovascular events) will have unknown true correlation ceilings. Fifth, our stressor model is impulsive Gaussian; sustained chronic stress (gradual accumulation over months) was not tested, and it remains unknown how these estimators perform under non‑stationary, long‑term load. Finally, the study uses a single pre‑registered seed; while the code is deterministic and the sample size ($n=200$) gives stable bootstrap intervals, a multi‑seed sensitivity analysis would further strengthen generalisability.

### 4.5 Practical Recommendations

Based on these results, we offer the following recommendations for researchers constructing allostatic load measures from high‑frequency physiological data:
- **When baseline calibration is known to be clean** (e.g., from controlled laboratory recordings), any GP‑based normalisation (including Mahalanobis distance) will perform well. The additional complexity of multivariate methods may not be warranted for burden estimation alone, but may improve signal extraction for independent outcomes.
- **When baseline contamination is possible** (the typical field scenario), use the univariate $\sigma_{\text{calib}}$ normalisation. It is simplest, most robust, and achieves near‑optimal performance.
- **Avoid moving‑average baselines** in any context where the baseline may contain stressor transients. The MA‑baseline is catastrophically vulnerable to sign reversal, which propagates to negative correlations with clinical outcomes.
- **Mahalanobis distance** remains a viable alternative if contamination is mild and multivariate integration is desired, but it requires more careful estimation of $\Sigma_{\text{calib}}$ (e.g., using shrinkage estimators to improve conditioning under contamination).

---

## 5. Conclusion

We have introduced and evaluated Ze‑AL v4, a family of predictive‑coding‑inspired allostatic load measures. Under clean conditions, all GP‑based methods perform equivalently. Under realistic calibration contamination, the univariate $\sigma_{\text{calib}}$ normalisation is the most robust estimator, preserving high correlation with the ground‑truth burden while avoiding the sign reversal that plagues moving‑average baselines. The Mahalanobis distance variant, though more vulnerable to contamination, is surprisingly robust to the coupling structure between channels, contradicting a common assumption. The independent behavioral target confirms that these correlations reflect genuine signal rather than circularity. We recommend v4 $\sigma_{\text{calib}}$ as the primary deployable measure for real‑world allostatic load research, with the caveat that formal validation on empirical datasets is urgently needed.

---

## 6. References

1. Sterling P, Eyer J. Allostasis: a new paradigm to explain arousal pathology. In: Fisher S, Reason J, editors. Handbook of life stress, cognition and health. Chichester: Wiley; 1988. p. 629–49.
2. McEwen BS. Stress, adaptation, and disease: allostasis and allostatic load. *N Engl J Med*. 1998;338:171–9.
3. Seeman TE, McEwen BS, Rowe JW, Singer BH. Allostatic load as a marker of cumulative biological risk: MacArthur studies of successful aging. *Proc Natl Acad Sci USA*. 2001;98:4770–5.
4. Karlamangla AS, Singer BH, Seeman TE. Reduction in allostatic load in older adults is associated with lower all-cause mortality risk: MacArthur studies of successful aging. *Psychosom Med*. 2006;68:500–7.
5. Gillespie SL, Christian LM, Alston AD, Kozlosky M, Anderson CM, Bailey AL, et al. Allostatic load and cardiovascular disease risk in women: a systematic review. *Psychoneuroendocrinology*. 2019;109:104404.
6. Karlamangla AS, Miller-Martinez D, Lachman ME, Tun PA, Koretz BK, Seeman TE. Biological correlates of adult cognition: modest but consistent associations with allostatic load. *Neurobiol Aging*. 2014;35:1129–37.
7. Zannas AS, Cardenas A, Zhang Z, Ma J, Hastie T, Baccarelli AA, et al. Epigenetic aging and allostatic load. *Neuroscience*. 2017;359:148–54.
8. Harb C, Haq M, Brown LL, Lee L, Lewis TT. Discrimination and allostatic load in older African Americans: a meta-analysis. *Psychoneuroendocrinology*. 2025;165:107100.
9. Madaria A, Abey J, Zuniga M, Garcia C, Miller DR. Allostatic load in schizophrenia and major depressive disorder: a meta‑analysis. *Front Psychiatry*. 2025;16:1506400.
10. Kezios KL, Zhang Y, Wu G, Engel LS, Baez A, Goldstein JB, et al. Allostatic load measurement and bias by sex. *Am J Epidemiol*. 2022;191:103–15.
11. Friston K. The free‑energy principle: a unified brain theory? *Nat Rev Neurosci*. 2010;11:127–38.
12. Clark A. Whatever next? Predictive brains, situated agents, and the future of cognitive science. *Behav Brain Sci*. 2013;36:181–204.
13. Barrett LF, Simmons WK. Interoceptive predictions in the brain. *Nat Rev Neurosci*. 2015;16:419–29.
14. Tschantz A, Millidge B, Seth AK, Buckley CL. Variational free energy for active inference. *Neural Comput*. 2022;34:125–63.
15. Tkemaladze T. Ze‑AL v3: a robust uncertainty‑weighted measure of allostatic load. 2024. Unpublished manuscript (available from author upon request).
16. Matthews AG de G, van der Wilk M, Nickson T, Fujii K, Bustos A, Turner RE, et al. GPflow: a Gaussian process library using TensorFlow. *J Mach Learn Res*. 2017;18:1–6.
17. Rothman KJ. No adjustments are needed for multiple comparisons. *Epidemiology*. 1990;1:43–6.
18. Ledoit O, Wolf M. A well‑conditioned estimator for large‑dimensional covariance matrices. *J Multivariate Anal*. 2004;88:365–411.

---

## 7. Code & Data Availability

Code will be released at **https://github.com/[author]/Ze-AL-v4** upon submission. Local repository available to reviewers upon request via the corresponding author. The simulation is deterministic with seed **20260509**. Pre‑registration details are available in the file `OSF_PREREG.md` locked at **2026‑05‑09 05:36:12 local**; final results were saved at **2026‑05‑09 07:43:33 local** — approximately 1.5 hours after protocol lock. Public OSF deposition with hash‑anchored timestamps will be completed at submission.

---

## 8. Competing Interests

T.T. is the developer of the Ze‑AL formalism (predictive‑coding allostatic load measure). To mitigate developer bias, the protocol was pre‑registered before any production run (see OSF_PREREG.md timestamps), all decision rules are pre‑committed, and the code is deterministic with a public seed. There are no financial competing interests.

---

## Author Contributions (CRediT)

**T. Tkemaladze**: Conceptualization, Methodology, Software, Formal analysis, Writing – Original Draft, Writing – Review & Editing, Visualization, Project administration. [Additional authors to be added for data collection, supervision, and funding acquisition.]

---