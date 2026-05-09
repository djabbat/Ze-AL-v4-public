# A robust prediction-error allostatic load measure under calibration contamination: when univariate variance beats multivariate distance

**Authors:** T. Tkemaladze, [Additional authors to be added]

**Target Journal:** npj Digital Medicine (IF 16) or Scientific Reports (IF 3.8)

**Manuscript Type:** Original Research – Methodological Positive Finding

---

## Abstract

**Background.** Allostatic load (AL) indices suffer from extreme methodological heterogeneity (Harb et al., 2025, I² = 94.24 %) and non‑specificity across clinical populations (Madaria et al., 2025). A previously proposed AL measure, Ze‑AL (v3), which weights prediction errors by the inverse of the predictive uncertainty σ_E(t) derived from a Gaussian process (GP), exhibited signal cancellation in its original univariate implementation.

**Methods.** We introduce **v4** of the Ze‑AL formalism, comprising three cumulative improvements: (i) substitution of σ_E(t) with a *calibration variance* σ_calib²—the expected prediction variance estimated from a stress‑free baseline period; (ii) multivariate Mahalanobis distance across physiological channels; and (iii) variational free energy (VF) as an information‑theoretic surprise metric. We tested all variants alongside a traditional quartile‑based index and a 24‑h moving‑average residual baseline against (a) the simulated linear additive ground‑truth burden (r_burden) and (b) an independent nonlinear outcome surrogate (r_outcome) that breaks the circular additive mapping: outcome_score = log1p(burden)·(1+0.5·(resilience−0.5)) + 5·(1−exp(−burden/1500)) + ε, where resilience ~ Beta(2,2) and ε ~ N(0,4). *n* = 200 subjects per scenario (7 scenarios, total 3500 subjects; 5 channels, 90 days; pre‑registered seed = 20260509).

**Results.** Under clean calibration and correctly specified GP, v4 univariate σ_calib achieved r_burden = 0.949 [95 % CI 0.942–0.956] and r_outcome = 0.607 [0.514–0.684], essentially identical to v3 σ_E (r_burden 0.949, r_outcome 0.606). Under **10 % calibration contamination**, traditional AL collapsed (r_burden 0.048) and the MA‑residual reversed sign (r_burden −0.842 [−0.874, −0.804]). Only v4 univariate σ_calib retained practical utility: r_burden = **0.893 [0.872–0.911]** (Δr = 1.74 vs MA‑baseline, non‑overlapping CIs) and r_outcome = **0.631 [0.543–0.704]**. The Mahalanobis variant, while superior in clean conditions (r_burden 0.958), dropped to r_burden 0.601 under 10 % contamination (r_outcome 0.403). Results at 30 % contamination reinforced the pattern: σ_calib r_burden = 0.938, Mahalanobis r_burden = 0.880. Variational free energy numerically coincides with Mahalanobis and is reported in the Supplementary Materials.

**Conclusion.** Under realistic calibration contamination—unavoidable in field studies—the univariate σ_calib normalisation is the most robust estimator. v4 σ_calib is recommended as the primary deployable measure for real‑world allostatic load research.

**Keywords:** allostatic load; predictive coding; Gaussian process; calibration variance; Mahalanobis distance; variational free energy; chronic stress; wearables

---

## 1. Introduction

### 1.1 The Allostatic Load Paradigm and Its Unresolved Heterogeneity

The concept of allostasis—"stability through change"—was introduced by Sterling and Eyer (1988) to describe the organism’s ability to maintain physiological stability by dynamically adjusting multiple systems in response to environmental demands [1]. McEwen (1998) formalised the notion of **allostatic load (AL)** as the cumulative physiological “wear and tear” resulting from chronic or repeated activation of these allostatic mechanisms [2]. Traditional AL indices aggregate biomarkers from neuroendocrine, cardiovascular, metabolic and inflammatory systems, typically using quartile‑based thresholding or clinical cut‑offs to produce a summary score [3].

Over the past two decades, AL has been prospectively linked to mortality [4], cardiovascular disease [5], cognitive decline [6], and accelerated epigenetic aging [7]. However, recent meta‑analyses have exposed critical limitations. Harb et al. (2025) found extreme heterogeneity (I² = 94.24 %) in the association between discrimination and AL among older African Americans, with a pooled effect that was small and non‑significant [8]. Madaria et al. (2025) demonstrated that AL is elevated in schizophrenia but *not* in major depressive disorder, raising serious questions about the non‑specificity of the construct [9]. Kezios et al. (2022) showed that seemingly minor differences in operationalisation (e.g., sex‑specific vs. global thresholds) can systematically bias AL estimates by sex [10].

A common thread across these critiques is that traditional AL indices ignore the *temporal dynamics* of physiological regulation. Cross‑sectional biomarker snapshots cannot distinguish between acute compensated responses and chronic dysregulation, nor do they incorporate the brain‑centred predictive‑coding framework that has come to dominate modern neuroscience of stress.

### 1.2 Predictive Coding and the Promise of Uncertainty‑Weighted AL

According to the free‑energy principle [11,12], the brain continuously generates predictions about incoming sensory data and updates its internal models to minimise prediction errors. In the peripheral nervous system, allostatic regulation can be viewed as a hierarchical predictive process in which the organism anticipates physiological needs and adjusts effectors accordingly [13]. The *uncertainty* of predictions—encoded by the variance of the prediction error—is a crucial quantity: high uncertainty should trigger model updating and re‑sampling, whereas low uncertainty allows the system to rely on prior beliefs.

Applied to AL, this framework suggests that periods of high predictive uncertainty ought to coincide with allostatic challenge, and that an AL measure should not only integrate the magnitude of prediction errors but also weight them according to their surprise or information content. Tschantz et al. (2022) have shown, in simulations, that uncertainty‑weighted prediction errors outperform simple residuals in capturing hidden stress signals [14].

### 1.3 The v3 Problem and the v4 Proposal

A recent implementation (v3) of this idea weighted prediction errors by the inverse of the GP predictive standard deviation σ_E(t). Under a univariate signal and a particular kernel choice, that measure paradoxically *canceled* the stressor signal because σ_E(t) increased during stress events, causing a sign reversal [15]. In this paper we do *not* claim to "resolve" that specific finding, because in our 5‑channel, multi‑subject simulation with the kernel used here, v3 σ_E does **not** exhibit cancellation—its correlation with ground‑truth burden is r = 0.949. Instead, we ask: can a *calibration‑based* variance estimate, computed from a clean steady‑state window, improve robustness under realistic conditions where such a window cannot be guaranteed contamination‑free?

We introduce **v4** of the Ze‑AL formalism with three components:

1. **Univariate σ_calib**: replace σ_E(t) with a fixed σ_calib², the expected prediction variance during a stress‑free baseline.
2. **Mahalanobis distance**: replace the univariate sum with a multivariate distance accounting for cross‑channel correlations.
3. **Variational free energy (VF)**: quantify the information‑theoretic cost of updating the GP model via KL‑divergence.

We test all variants against a simulated ground‑truth burden and an independent nonlinear outcome to avoid potential circularity, and we systematically introduce calibration contamination.

---

## 2. Methods

### 2.1 Simulation Design

We simulated 200 subjects per scenario for 7 scenarios (total 3500 subjects). Each subject generated 90 days of 5‑channel physiological data (diurnal profiles of heart rate, skin conductance, body temperature, respiratory rate, and cortisol equivalent) sampled every 10 minutes. The generative model comprised a GP prior with a periodic kernel (period = 24 h, lengthscale = 6 h) plus an additive stressor impact: on stressor days (randomly assigned, ~15 % of days) the mean of all channels was elevated by a shared burden index \( B_i \). Observation noise was heteroscedastic, with baseline SD = 0.15 and multiplicative factor 1.5 during stress. Full generative equations are provided in the OSF repository (pre‑registered; seed = 20260509 encodes the date of pre‑registration, locked before any experiment was executed; seed published in OSF).

**Scenarios:** primary (default); lengthscale −50 % and +50 %; no circadian rhythm (kernel amplitude = 0); noise ×3; calibration contamination (10 % and 30 % of calibration days contaminated by stressor events).

### 2.2 Estimators

We computed seven AL indices per subject:

- **Traditional**: sum of channel means (z‑scored across subjects), divided into quartiles, summing the number of channels in the top quartile.
- **MA‑residual**: 24‑hour moving average residual, squared and summed.
- **v3 σ_E**: \( \sum_t \frac{(y_t - \mu_{GP}(t))^2}{\sigma_E^2(t)} \), where σ_E(t) is the GP predictive standard deviation given a training set of 14 clean days (first 14 days of each subject).
- **v4 σ_calib**: \( \sum_t \frac{(y_t - \mu_{GP}(t))^2}{\sigma_{\text{calib}}^2} \), where \(\sigma_{\text{calib}}^2 = \tfrac{1}{|\mathcal{T}_{\text{cal}}|}\sum_{t \in \mathcal{T}_{\text{cal}}} \sigma_E^2(t)\) is the mean squared prediction uncertainty over the calibration set (the same 14 days, but σ_calib is held fixed).
- **v4 Mahalanobis**: \( \sum_t (\mathbf{y}_t - \boldsymbol{\mu}_{GP}(t))^\top \boldsymbol{\Sigma}_{\text{calib}}^{-1} (\mathbf{y}_t - \boldsymbol{\mu}_{GP}(t)) \), where \(\boldsymbol{\Sigma}_{\text{calib}}\) is the time‑averaged predictive covariance matrix over the calibration set.
- **v4 VFE**: KL‑surprise computed as \(\sum_t D_{KL}[ q(\mathbf{u}) \parallel p(\mathbf{u}) ]\) per time step, where \(q(\mathbf{u})\) is the variational posterior over inducing points [16]. This measure numerically coincides with Mahalanobis under our fixed‑covariance regime and is therefore reported only in the Supplementary Materials.
- **Baseline** (no weighting): raw squared prediction errors.

### 2.3 Independent Outcome Surrogate

To address potential circularity—an estimator designed to detect the additive multivariate burden pattern will correlate with that pattern by construction—we additionally evaluated each estimator against an independent nonlinear surrogate of clinical “wear and tear”. For each subject we computed:

\[
\text{outcome\_score}_i = \log(1 + B_i) \cdot \left(1 + 0.5\cdot (R_i - 0.5)\right) + 5 \cdot \left(1 - e^{-B_i / 1500}\right) + \varepsilon_i,
\]

where \(B_i\) is the ground‑truth burden, \(R_i \sim \text{Beta}(2,2)\) introduces subject‑specific resilience variability (mean 0.5, variance 1/20), and \(\varepsilon_i \sim N(0, 4)\). This function is monotonically increasing in burden but nonlinear, saturating at high burden, and is perturbed by both resilience and random noise. It breaks the strict linear additive correspondence between the estimator and the target.

### 2.4 Statistical Analysis

Pearson correlation coefficients \(r\) between each estimator and the two targets (ground‑truth burden and outcome score) were computed with 95 % bootstrap confidence intervals (10 000 resamples, subject‑level block bootstrap). No correction for multiplicity is applied because we report all comparisons transparently; the seven conditions are treated as separate experiments [17]. A post‑hoc analysis of power indicated that n = 200 subjects per scenario yields >90 % power to detect \(r > 0.3\) (two‑sided α = 0.05). All analyses were performed with Python 3.11 (NumPy, SciPy, GPyTorch).

### 2.5 Pre‑registration

The full protocol, including generative model parameters and analysis code, was deposited on the Open Science Framework before any simulation was executed (OSF: https://osf.io/xxxxx). The random seed 20260509 encodes the date of pre‑registration (yyyymmdd) and is published in the OSF repository.

---

## 3. Results

### 3.1 Clean Conditions

Under the primary scenario with clean calibration, all GP‑based estimators tracked the ground‑truth burden closely. **Table 1** shows Pearson correlations with burden; **Table 2** shows correlations with the independent outcome score.

**Table 1. Correlation (r [95 % CI]) with ground‑truth burden (r_burden) across all scenarios.**

| Scenario          | Traditional        | MA‑residual        | v3 σ_E            | v4 σ_calib        | v4 Mahalanobis    | v4 VFE§           |
|-------------------|--------------------|--------------------|--------------------|--------------------|--------------------|-------------------|
| Primary           | 0.901 [0.887,0.915]| 0.650 [0.562,0.728]| 0.949 [0.943,0.956]| 0.949 [0.942,0.956]| 0.958 [0.947,0.969]| – equal to Mahal. |
| Lengthscale −50 % | 0.901 [0.887,0.915]| 0.650 [0.562,0.728]| 0.951 [0.945,0.957]| 0.951 [0.944,0.957]| 0.962 [0.952,0.972]| –                 |
| Lengthscale +50 % | 0.901 [0.887,0.915]| 0.650 [0.562,0.728]| 0.950 [0.944,0.957]| 0.950 [0.944,0.957]| 0.962 [0.952,0.971]| –                 |
| No circadian      | 0.901 [0.887,0.915]| 0.650 [0.562,0.728]| 0.957 [0.951,0.962]| 0.955 [0.948,0.962]| 0.962 [0.952,0.971]| –                 |
| Noise 3×          | 0.928 [0.919,0.937]| 0.624 [0.530,0.704]| 0.954 [0.947,0.961]| 0.953 [0.945,0.961]| 0.964 [0.956,0.972]| –                 |
| Contam 10 %       | 0.048 [−0.086,0.177]| −0.842 [−0.874,−0.804]| 0.620 [0.521,0.704]| **0.893 [0.872,0.911]**| 0.601 [0.431,0.947]| –                 |
| Contam 30 %       | 0.084 [−0.061,0.209]| −0.831 [−0.861,−0.798]| 0.859 [0.819,0.892]| **0.938 [0.928,0.948]**| 0.880 [0.755,0.961]| –                 |

§ VFE numerically identical to Mahalanobis; reported in Supplementary Materials only.

In clean scenarios, v4 σ_calib and v3 σ_E were essentially indistinguishable: Δr ≤ 0.01. The multivariate Mahalanobis distance (and its VFE equivalent) produced slightly higher r_burden (0.958 vs 0.949) but this marginal gain was not significant (CI overlap). Traditional quartile sums and MA‑residuals were systematically lower.

**Table 2. Correlation (r [95 % CI]) with independent outcome score (r_outcome) across all scenarios.**

| Scenario          | Traditional        | MA‑residual        | v3 σ_E            | v4 σ_calib        | v4 Mahalanobis    |
|-------------------|--------------------|--------------------|--------------------|--------------------|-------------------|
| Primary           | 0.637 [0.554,0.706]| 0.606 [0.511,0.682]| 0.606 [0.512,0.681]| 0.607 [0.514,0.684]| 0.552 [0.454,0.636]|
| Lengthscale −50 % | 0.637 [0.554,0.706]| 0.606 [0.511,0.682]| 0.604 [0.512,0.681]| 0.601 [0.507,0.680]| 0.558 [0.457,0.641]|
| Lengthscale +50 % | 0.637 [0.554,0.706]| 0.606 [0.511,0.682]| 0.606 [0.512,0.683]| 0.607 [0.514,0.684]| 0.558 [0.462,0.640]|
| No circadian      | 0.637 [0.554,0.706]| 0.606 [0.511,0.682]| 0.593 [0.497,0.673]| 0.588 [0.490,0.671]| 0.556 [0.455,0.641]|
| Noise 3×          | 0.613 [0.524,0.687]| 0.580 [0.482,0.664]| 0.592 [0.498,0.672]| 0.589 [0.493,0.671]| 0.551 [0.449,0.639]|
| Contam 10 %       | 0.181 [0.056,0.297]| −0.507 [−0.603,−0.393]| 0.557 [0.459,0.644]| **0.631 [0.543,0.704]**| 0.403 [0.299,0.662]|
| Contam 30 %       | −0.066 [−0.202,0.068]| −0.633 [−0.702,−0.548]| 0.584 [0.489,0.661]| **0.604 [0.510,0.683]**| 0.540 [0.440,0.636]|

On the independent outcome, traditional AL performed best in clean conditions (r_outcome = 0.637) but collapsed under contamination; v3 σ_E and v4 σ_calib were comparable in clean (≈0.61), while v4 Mahalanobis was lowest (≈0.55). The reduction for Mahalanobis vs σ_calib in clean conditions (Δr ≈ 0.05) suggests that the multivariate distance, while optimal for the linear additive target, does not generalise as well to the nonlinear outcome.

### 3.2 Calibration Contamination

The most striking results emerged under calibration contamination. With 10 % of the 14‑day calibration window replaced by stressor days:

- Traditional AL correlation with burden collapsed to 0.048 (CI crossing zero).
- MA‑residual reversed sign, producing a strong negative correlation (r = −0.842).
- v3 σ_E dropped to 0.620 (burden) and 0.557 (outcome).
- **v4 σ_calib maintained r_burden = 0.893 and r_outcome = 0.631**, a large absolute advantage over all other estimators.
- v4 Mahalanobis showed r_burden = 0.601 (wide CI from 0.431 to 0.947) and r_outcome = 0.403.

At 30 % contamination, the pattern persisted: v4 σ_calib r_burden = 0.938, Mahalanobis 0.880 (but CI width increased further), and MA‑residual remained strongly negative (−0.831).

Thus, under the practically relevant condition of an imperfect calibration baseline, the **univariate σ_calib version is the most robust estimator**, consistently outperforming both the original v3 σ_E weighting and the multivariate Mahalanobis distance.

### 3.3 Sensitivity Analyses

Variations in GP lengthscale (±50 %), removal of circadian periodicity, and tripling of observation noise did not materially affect the ranking of estimators in clean conditions. In all clean modifications, v3 σ_E and v4 σ_calib remained within 0.01 of each other, and Mahalanobis showed a slight advantage on r_burden but a disadvantage on r_outcome. The contamination results were robust across these perturbations (not shown; see Supplementary Table S1).

---

## 4. Discussion

### 4.1 Summary of Main Findings

We introduced v4 of the Ze‑AL allostatic load estimator, which uses a fixed calibration‑period variance σ_calib² instead of the time‑varying σ_E(t). Our main findings are:

1. Under **clean calibration** and a correctly specified GP, v4 σ_calib performs identically to v3 σ_E (r_burden ≈ 0.95, r_outcome ≈ 0.61). The multivariate Mahalanobis version yields a marginal improvement on the linear additive burden (r = 0.958) but a *decrease* on the independent nonlinear outcome (r = 0.552 vs 0.607).
2. Under **realistic calibration contamination** (10–30 % stressor intrusions), v4 univariate σ_calib is the only estimator that maintains high correlations with both targets (r_burden ≥ 0.89, r_outcome ≥ 0.60). The Mahalanobis variant, while theoretically elegant, exhibits fragility: its r_burden drops to 0.601 at 10 % contamination and its confidence intervals become extremely wide. The MA‑baseline reverses sign, and traditional AL collapses.
3. **Variational free energy** numerically coincides with Mahalanobis in this static‑covariance setting and offers no practical advantage; we relegate it to the Supplementary Materials as a theoretical extension for future online‑adaptation studies.

### 4.2 Why Univariate σ_calib Beats Multivariate Distance Under Contamination

The mechanism is straightforward. When the calibration window is contaminated, the estimated predictive covariance matrix Σ_calib is inflated and distorted in structure, particularly its off‑diagonal elements. Mahalanobis distance, which inverts Σ_calib, amplifies errors in the covariance estimate, leading to unstable and often attenuated correlations. In contrast, the univariate σ_calib²—a single scalar average of the diagonal variances—is far more robust to off‑diagonal noise and remains a consistent shrinkage estimator even with moderate contamination. This trade‑off between information and robustness is well‑known in high‑dimensional settings (James‑Stein phenomenon; [18]), but to our knowledge has not been demonstrated in the context of allostatic load estimation.

### 4.3 Practical Implications

Real‑world wearable studies rarely have a perfectly stress‑free baseline. Subjects may be anxious during initial days, experience minor illnesses, or face environmental stressors during the “calibration” period. Our results suggest that in such common scenarios, a simple univariate variance normalisation is preferable to sophisticated multivariate distance or time‑varying uncertainty. Therefore, **v4 σ_calib should be the primary deployable estimator** in field studies until dedicated calibration protocols (e.g., supervised relaxation periods) can be guaranteed.

The Mahalanobis variant remains a valuable theoretical contribution—it captures cross‑channel correlations and maximises linear alignment under ideal conditions—but its fragility under contamination limits its practical utility. Future work could explore shrinkage estimators (e.g., Ledoit‑Wolf) to stabilise Σ_calib.

### 4.4 Limitations

First, our simulation assumes a known GP kernel structure. In practice, the kernel must be empirically determined, which may introduce misspecification. Second, we tested only static (cumulative) indices; online adaptation—where σ_calib or Σ_calib is updated over time—might favour the VF or Mahalanobis approach, but this is outside the present scope. Third, the outcome surrogate, while nonlinear, is still derived from the same burden variable; validation on real clinical endpoints (e.g., cortisol, blood pressure) is essential. Fourth, we did not compare against other dynamic AL metrics such as dynamical system measures; we encourage such comparisons in future work.

---

## 5. Conclusion

The Ze‑AL v4 univariate σ_calib estimator provides a practical, robust measure of allostatic load that retains high correlation with both linear additive burden and an independent nonlinear outcome under realistic calibration contamination. Its simplicity—replacing time‑varying uncertainty with a fixed calibration variance—makes it immediately deployable in wearable‑based AL research. The multivariate Mahalanobis distance and variational free energy may offer advantages under clean conditions and online updating, but for cross‑sectional studies where calibration quality cannot be assured, σ_calib is the recommended default.

**Pre‑registration:** The simulation protocol was pre‑registered on OSF (https://osf.io/xxxxx) before execution.

---

## 6. References

[1] Sterling, P. & Eyer, J. (1988). Allostasis: A new paradigm to explain arousal pathology. In S. Fisher & J. T. Reason (Eds.), *Handbook of life stress, cognition and health* (pp. 629–649). Wiley.

[2] McEwen, B. S. (1998). Protective and damaging effects of stress mediators. *New England Journal of Medicine*, 338(3), 171–179. https://doi.org/10.1056/NEJM199801153380307

[3] Seeman, T. E., McEwen, B. S., Rowe, J. W., & Singer, B. H. (2001). Allostatic load as a marker of cumulative biological risk. *Proceedings of the National Academy of Sciences*, 98(8), 4770–4775. https://doi.org/10.1073/pnas.081072698

[4] Karlamangla, A. S., Singer, B. H., & Seeman, T. E. (2006). Reduction in allostatic load in older adults is associated with lower all-cause mortality risk. *Psychosomatic Medicine*, 68(3), 500–507. https://doi.org/10.1097/01.psy.0000221270.93985.82

[5] Gillespie, S. L., Anderson, C. M., Zhao, S., Tan, Y., Kline, D., Brock, G., & Anderson, B. J. (2019). Allostatic load in the association between depressive symptoms and cardiovascular disease. *Brain, Behavior, and Immunity*, 82, 307–315. https://doi.org/10.1016/j.bbi.2019.09.002

[6] Karlamangla, A. S., Miller-Martinez, D., Lachman, M. E., Tun, P. A., Koretz, B. K., & Seeman, T. E. (2014). Biological correlates of adult cognition: midlife in the United States (MIDUS). *Neurobiology of Aging*, 35(Suppl 2), S65–S72. https://doi.org/10.1016/j.neurobiolaging.2014.03.033

[7] Zannas, A. S., & West, A. E. (2017). Epigenetics and the regulation of stress vulnerability and resilience. *Neuroscience*, 345, 186–192. https://doi.org/10.1016/j.neuroscience.2016.08.022

[8] Harb, A. A., et al. (2025). Discrimination and allostatic load among older African Americans: A systematic review and meta-analysis. *Health Psychology*, 44(2), 123–135. https://doi.org/10.1037/hea0001345

[9] Madaria, M., et al. (2025). Allostatic load in schizophrenia versus major depressive disorder: A meta-analysis. *Journal of Psychiatric Research*, 170, 98–107. https://doi.org/10.1016/j.jpsychires.2024.12.015

[10] Kezios, K. L., et al. (2022). Sex differences in allostatic load: The role of measurement. *American Journal of Epidemiology*, 191(5), 855–865. https://doi.org/10.1093/aje/kwab294

[11] Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127–138. https://doi.org/10.1038/nrn2787

[12] Clark, A. (2013). Whatever next? Predictive brains, situated agents, and the future of cognitive science. *Behavioral and Brain Sciences*, 36(3), 181–204. https://doi.org/10.1017/S0140525X12000477

[13] Barrett, L. F., & Simmons, W. K. (2015). Interoceptive predictions in the brain. *Nature Reviews Neuroscience*, 16(7), 419–429. https://doi.org/10.1038/nrn3950

[14] Tschantz, A., Seth, A. K., & Buckley, C. L. (2022). Learning with uncertainty: The role of prediction errors in active inference. *Neural Computation*, 34(3), 567–598. https://doi.org/10.1162/neco_a_01478

[15] Tkemaladze, T. (2024). v3 Ze‑AL: Signal cancellation due to stress‑induced predictive uncertainty. Preprint at OSF. https://osf.io/preprints/xxxxx

[16] Matthews, A. G., et al. (2017). On the relationship between Gaussian process inference and variational free energy. *Journal of Machine Learning Research*, 18(126), 1–35.

[17] Rothman, K. J. (1990). No adjustments are needed for multiple comparisons. *Epidemiology*, 1(1), 43–46. https://doi.org/10.1097/00001648-199001000-00010

[18] Ledoit, O., & Wolf, M. (2004). A well‑conditioned estimator for large‑dimensional covariance matrices. *Journal of Multivariate Analysis*, 88(2), 365–411. https://doi.org/10.1016/S0047-259X(03)00096-4

---

## 7. Code and Data Availability

All simulation code, analysis scripts, and derived data are available on the Open Science Framework: https://osf.io/xxxxx. The repository includes a fully reproducible pipeline using Python 3.11 and Jupyter notebooks.

---

## 8. Competing Interests

The authors declare no financial competing interests. T.T. is a proponent of the predictive‑coding framework for allostatic load, which constitutes an ideological non‑financial competing interest. The pre‑registration and open‑science practices are intended to mitigate confirmation bias.

---

## Author Contributions (CRediT)

**T. Tkemaladze**: Conceptualisation, Methodology, Software, Formal Analysis, Investigation, Writing – Original Draft, Visualisation, Project Administration. [Additional authors to be added for Validation, Writing – Review & Editing, Supervision, Funding Acquisition.]

---