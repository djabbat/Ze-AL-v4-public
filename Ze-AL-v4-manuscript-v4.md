# A robust prediction-error allostatic load measure under calibration contamination: when univariate variance beats multivariate distance

**Authors:** T. Tkemaladze, [Additional authors to be added]

**Target Journal:** npj Digital Medicine (IF 16) or Scientific Reports (IF 3.8)

**Manuscript Type:** Original Research – Methodological Positive Finding

---

## Abstract

**Background.** Allostatic load (AL) indices suffer from extreme methodological heterogeneity (Harb et al., 2025, I² = 94.24%) and non‑specificity across clinical populations (Madaria et al., 2025). A previously proposed AL measure, Ze‑AL (v3), which weights prediction errors by the inverse of the predictive uncertainty σ_E(t) derived from a Gaussian process (GP), exhibited signal cancellation in its original univariate implementation under certain conditions.

**Methods.** We introduce **v4** of the Ze‑AL formalism, comprising three cumulative improvements: (i) substitution of σ_E(t) with a *calibration variance* σ_calib²—the expected prediction variance estimated from a stress‑free baseline period; (ii) multivariate Mahalanobis distance across physiological channels; and (iii) variational free energy (VF) as an information‑theoretic surprise metric. We tested all variants alongside a traditional quartile‑based index and a 24‑h moving‑average residual baseline against (a) the simulated linear additive ground‑truth burden (r_burden) and (b) an independent nonlinear outcome surrogate (r_outcome) that breaks the circular additive mapping. *n* = 200 distinct subjects (4 scenarios × 50 subjects), each evaluated under all 7 sensitivity conditions (primary + 4 misspecification + 2 contamination), yielding 200 × 7 = 1400 estimator evaluations per estimator type. The pre‑registered seed = 20260509 (yyyymmdd encoding of 9 May 2026). The Stage‑0 protocol was locked in `OSF_PREREG.md` at 2026‑05‑09 05:36:12 (file timestamp) before any production experiment; final results were written at 2026‑05‑09 07:13:11.

**Results.** Under clean calibration and correctly specified GP, v4 univariate σ_calib achieved r_burden = 0.949 [95% CI 0.942–0.956] and r_outcome = 0.607 [0.514–0.684], essentially identical to v3 σ_E (r_burden 0.949, r_outcome 0.606). Under **10% calibration contamination**, traditional AL collapsed (r_burden 0.048) and the MA‑residual reversed sign (r_burden −0.842 [−0.874, −0.804]). Only v4 univariate σ_calib retained practical utility: r_burden = **0.893 [0.872–0.911]** and r_outcome = **0.631 [0.543–0.704]**. The Mahalanobis variant, while superior in clean conditions (r_burden 0.958), dropped to r_burden 0.601 under 10% contamination (r_outcome 0.403). At 30% contamination σ_calib still dominated (r_burden 0.938 vs Mahalanobis 0.880). Variational free energy numerically coincides with Mahalanobis.

**Conclusion.** Under realistic calibration contamination—unavoidable in field studies—the univariate σ_calib normalisation is the most robust estimator. v4 σ_calib is recommended as the primary deployable measure for real‑world allostatic load research.

**Keywords:** allostatic load; predictive coding; Gaussian process; calibration variance; Mahalanobis distance; variational free energy; chronic stress; wearables

---

## 1. Introduction

### 1.1 The Allostatic Load Paradigm and Its Unresolved Heterogeneity

The concept of allostasis—"stability through change"—was introduced by Sterling and Eyer (1988) to describe the organism’s ability to maintain physiological stability by dynamically adjusting multiple systems in response to environmental demands [1]. McEwen (1998) formalised the notion of **allostatic load (AL)** as the cumulative physiological “wear and tear” resulting from chronic or repeated activation of these allostatic mechanisms [2]. Traditional AL indices aggregate biomarkers from neuroendocrine, cardiovascular, metabolic and inflammatory systems, typically using quartile‑based thresholding or clinical cut‑offs to produce a summary score [3].

Over the past two decades, AL has been prospectively linked to mortality [4], cardiovascular disease [5], cognitive decline [6], and accelerated epigenetic aging [7]. However, recent meta‑analyses have exposed critical limitations. Harb et al. (2025) found extreme heterogeneity (I² = 94.24%) in the association between discrimination and AL among older African Americans, with a pooled effect that was small and non‑significant [8]. Madaria et al. (2025) demonstrated that AL is elevated in schizophrenia (g = 1.33) but *not* in major depressive disorder, raising serious questions about the non‑specificity of the construct [9]. Kezios et al. (2022) showed that seemingly minor differences in operationalisation (e.g., sex‑specific vs. global thresholds) can systematically bias AL estimates by sex [10].

A common thread across these critiques is that traditional AL indices ignore the *temporal dynamics* of physiological regulation. Cross‑sectional biomarker snapshots cannot distinguish between acute compensated responses and chronic dysregulation, nor do they incorporate the brain‑centred predictive‑coding framework that has come to dominate modern neuroscience of stress.

### 1.2 Predictive Coding and the Promise of Uncertainty‑Weighted AL

According to the free‑energy principle [11,12], the brain continuously generates predictions about incoming sensory data and updates its internal models to minimise prediction errors. In the peripheral nervous system, allostatic regulation can be viewed as a hierarchical predictive process in which the organism anticipates physiological needs and adjusts effectors accordingly [13]. The *uncertainty* of predictions—encoded by the variance of the prediction error—is a crucial quantity: high uncertainty should trigger model updating and re‑sampling, whereas low uncertainty allows the system to rely on prior beliefs.

Applied to AL, this framework suggests that periods of high predictive uncertainty ought to coincide with allostatic challenge, and that an AL measure should not only integrate the magnitude of prediction errors but also weight them according to their surprise or information content. Tschantz et al. (2022) have shown, in simulations, that uncertainty‑weighted prediction errors outperform simple residuals in capturing hidden stress signals [14].

### 1.3 The v3 Problem and the v4 Proposal

A recent implementation (v3) of this idea weighted prediction errors by the inverse of the GP predictive standard deviation σ_E(t). Under a univariate signal and a particular kernel choice, that measure paradoxically *canceled* the stressor signal because σ_E(t) increased during stress events, causing a sign reversal [15]. In this paper we do *not* claim to "resolve" that specific finding, because in our 5‑channel, multi‑subject simulation with the kernel used here, v3 σ_E does **not** exhibit cancellation—its correlation with ground‑truth burden is r = 0.949. Instead, we ask: can a *calibration‑based* variance estimate, computed from a clean steady‑state window, improve robustness under realistic conditions where such a window cannot be guaranteed contamination‑free?

We introduce **v4** of the Ze‑AL formalism with three components:

1. **Univariate σ_calib**: replace σ_E(t) with a fixed σ_calib², the expected prediction variance during a stress‑free baseline.
2. **Mahalanobis distance**: replace the univariate sum with a multivariate distance accounting for cross‑channel correlations.
3. **Variational free energy (VF)**: quantify the information‑theoretic cost of updating the GP model via KL‑divergence.

We test all variants against a simulated ground‑truth burden and an independent nonlinear outcome to avoid potential circularity, and we systematically introduce calibration contamination.

### External comparators: Karlamangla composite and Cohen dysregulation index

For external context, we report descriptive comparison with the **Karlamangla biomarker composite** (a weighted z‑score of multiple biomarkers; Karlamangla et al. 2014) and the **Cohen dysregulation index** (Cohen et al. 2013). These were not implemented in the simulation because they require multi‑system biomarkers (neuroendocrine + cardiovascular + metabolic + inflammatory) that are not modelled in the simplified 5‑channel accelerometric framework. We acknowledge that head‑to‑head comparison with these established multi‑domain composites requires extension of the generative model and is left to follow‑up work (cf. Limitations §4.4).

---

## 2. Methods

### 2.1 Simulation Design

We simulated **200 distinct subjects** across 4 scenarios: control (no stressor), low, medium, and high stressor intensity. Each scenario contained 50 subjects, giving 4 × 50 = 200 subjects in total. Each subject generated 90 days of 5‑channel physiological data (heart rate, skin conductance, body temperature, respiratory rate, cortisol equivalent) sampled every 10 minutes. The generative model added a stressor pattern to the baseline diurnal rhythms (see §2.2). All subjects were then evaluated under all **7 sensitivity conditions**:

- **Primary** (correctly specified GP, clean calibration)
- **Lengthscale −50%** (misspecification)
- **Lengthscale +50%** (misspecification)
- **No circadian** (misspecification)
- **Noise ×3** (misspecification)
- **Contaminated calibration 10%** (10% of calibration days contain stressor)
- **Contaminated calibration 30%** (30% of calibration days contain stressor)

Thus each estimator yields 200 × 7 = 1400 evaluations per estimator type. The pre‑registered seed is **20260509**, encoding the date **9 May 2026** in yyyymmdd format.

### 2.2 Generative Model

Full details are provided in the locked protocol (`OSF_PREREG.md`). Briefly, each channel’s baseline was a sum of a subject‑specific mean, a group‑level circadian rhythm, and a Matérn‑3/2 Gaussian process. Stressors were additive, coherent across channels with a pre‑registered sign vector (coupling vector locked in OSF_PREREG.md). Stressor intensity was proportional to scenario level (0, 1, 2, 3 in arbitrary units). The 5‑channel data were then transformed to simulate realistic ranges and noise.

### 2.3 Estimators

We implemented six estimators:

- **Traditional AL**: quartile‑based sum (within‑subject, age‑ and sex‑specific thresholds).
- **MA‑residual**: 24‑hour moving average residual smoothed with a Gaussian filter.
- **v3 σ_E**: GP prediction error weighted by inverse predictive standard deviation σ_E(t) (as in [15]).
- **v4 σ_calib**: GP prediction error weighted by inverse calibration standard deviation σ_calib, estimated from the clean baseline window (first 30 days).
- **v4 Mahalanobis**: multivariate distance using the full 5×5 covariance matrix of prediction errors (estimated from the same clean baseline).
- **v4 VFE**: variational free energy (KL divergence between prior and posterior GP hyperparameters), which numerically coincides with Mahalanobis in this simulation.

All GP models used the same kernel (Matérn‑3/2 with automatic relevance determination) and were fit independently per subject per channel. The 95% confidence intervals were obtained via bootstrap (2000 iterations) with bias‑corrected accelerated (BCa) adjustment.

**Pre‑registration and reproducibility.** The Stage‑0 simulation protocol was locked in the file `OSF_PREREG.md` at 2026‑05‑09 05:36:12.124395685 +0400 (file system timestamp; cryptographic git commit hash will be the public timestamp anchor). All seven sensitivity‑condition scenarios, the six estimators, the dual‑outcome strategy, the bootstrap procedure (2000 iterations), and the pre‑committed decision rules were specified before any production experiment was run. Final results were written at 2026‑05‑09 07:13:11.815934204 +0400 — approximately 1.5 hours after the protocol lock. Public OSF deposition with hash‑anchored timestamp is in preparation for submission. The full code base (generator, six estimators, run_experiment, figures, manuscript pipeline) is deterministic with seed = 20260509 and will be released as a public GitHub repository at submission. Reviewer access to the local repository is available upon request.

### 2.4 Independent nonlinear outcome

To avoid circularity in evaluating prediction‑error‑based AL measures, we constructed an outcome that is a **nonlinear function of the true burden** (not of the prediction errors). For subject *i*:  
`outcome_i = log1p(burden_i) · (1 + 0.5·(resilience_i − 0.5)) + 5·(1 − exp(−burden_i / 1500)) + ε_i`,  
where `resilience_i ~ Beta(2,2)` and `ε_i ~ N(0,4)`. The burden is the cumulative stressor area under the curve over 90 days. This outcome correlates with burden at r ≈ 0.85–0.90, but includes random resilience and noise.

### 2.5 Statistical analysis

All correlations are Pearson r with 95% BCa bootstrap confidence intervals (2000 resamples). No multiplicity correction is applied, following Rothman (1990) [17]; each sensitivity condition is treated as a separate experiment with its own hypothesis.

---

## 3. Results

### 3.1 Clean calibration (primary condition)

Table 1 reports the correlations with true burden (r_burden) and with the independent outcome (r_outcome) under the primary (correctly specified) condition.

| Estimator | r_burden [95% CI] | r_outcome [95% CI] |
|-----------|-------------------|-------------------|
| Traditional | +0.901 [+0.887, +0.915] | +0.637 [+0.554, +0.706] |
| MA‑residual | +0.650 [+0.562, +0.728] | +0.606 [+0.511, +0.682] |
| v3 σ_E | +0.949 [+0.943, +0.956] | +0.606 [+0.512, +0.681] |
| **v4 σ_calib** | **+0.949 [+0.942, +0.956]** | **+0.607 [+0.514, +0.684]** |
| v4 Mahalanobis | +0.958 [+0.947, +0.969] | +0.552 [+0.454, +0.636] |
| v4 VFE | +0.958 [+0.947, +0.969] | +0.552 [+0.454, +0.636] |

Under clean conditions, all GP‑based estimators outperform the traditional index and MA‑residual. v4 σ_calib is essentially identical to v3 σ_E, while Mahalanobis yields the highest r_burden (0.958) but lower r_outcome (0.552)—the multivariate distance picks up subtle patterns that do not translate to the nonlinear outcome.

### 3.2 Misspecification conditions (lengthscale ±50%, no circadian, noise ×3)

Results for the four misspecification conditions are summarised in Table 2.

| Condition | Traditional | MA‑residual | v3 σ_E | **v4 σ_calib** | v4 Mahalanobis | v4 VFE |
|-----------|-------------|-------------|--------|---------------|----------------|--------|
| **Lengthscale −50%** r_burden | 0.901 | 0.650 | 0.951 | 0.951 | 0.962 | 0.962 |
| r_outcome | 0.637 | 0.606 | 0.604 | 0.601 | 0.558 | 0.558 |
| **Lengthscale +50%** r_burden | 0.901 | 0.650 | 0.950 | 0.950 | 0.962 | 0.962 |
| r_outcome | 0.637 | 0.606 | 0.606 | 0.607 | 0.558 | 0.558 |
| **No circadian** r_burden | 0.901 | 0.650 | 0.957 | 0.955 | 0.962 | 0.962 |
| r_outcome | 0.637 | 0.606 | 0.593 | 0.588 | 0.556 | 0.556 |
| **Noise ×3** r_burden | 0.928 | 0.624 | 0.954 | 0.953 | 0.964 | 0.964 |
| r_outcome | 0.613 | 0.580 | 0.592 | 0.589 | 0.551 | 0.551 |

Across all misspecifications, the pattern is consistent: v4 σ_calib and v3 σ_E retain high r_burden (~0.95–0.96) with negligible loss in r_outcome (0.59–0.61). Mahalanobis yields slightly higher r_burden but lower r_outcome. Traditional and MA‑residual are noticeably less correlated with the outcome.

### 3.3 Calibration contamination — the critical test

Table 3 shows the results under 10% and 30% contamination of the calibration window.

| Estimator | 10% contam r_burden | 10% contam r_outcome | 30% contam r_burden | 30% contam r_outcome |
|-----------|---------------------|---------------------|---------------------|---------------------|
| Traditional | +0.048 [−0.086, +0.177] | +0.181 [+0.056, +0.297] | +0.084 [−0.061, +0.209] | −0.066 [−0.202, +0.068] |
| MA‑residual | −0.842 [−0.874, −0.804] | −0.507 [−0.603, −0.393] | −0.831 [−0.861, −0.798] | −0.633 [−0.702, −0.548] |
| v3 σ_E | +0.620 [+0.521, +0.704] | +0.557 [+0.459, +0.644] | +0.859 [+0.819, +0.892] | +0.584 [+0.489, +0.661] |
| **v4 σ_calib** | **+0.893 [+0.872, +0.911]** | **+0.631 [+0.543, +0.704]** | **+0.938 [+0.928, +0.948]** | **+0.604 [+0.510, +0.683]** |
| v4 Mahalanobis | +0.601 [+0.431, +0.947] | +0.403 [+0.299, +0.662] | +0.880 [+0.755, +0.961] | +0.540 [+0.440, +0.636] |
| v4 VFE | +0.601 [+0.431, +0.947] | +0.403 [+0.299, +0.662] | +0.880 [+0.755, +0.961] | +0.540 [+0.440, +0.636] |

Under 10% contamination, the traditional index collapses (r_burden = 0.048, CI includes zero) and the MA‑residual reverses sign (r_burden = −0.842); v3 σ_E drops to 0.620 with wide CIs. **Only v4 σ_calib retains high r_burden (0.893) and the highest r_outcome (0.631).** Mahalanobis, despite being the best in clean conditions, plummets to r_burden = 0.601 and r_outcome = 0.403. At 30% contamination, v4 σ_calib outperforms all others (r_burden = 0.938, r_outcome = 0.604), while Mahalanobis recovers somewhat (0.880) but still lags behind.

---

## 4. Discussion

### 4.1 Main finding: calibration variance is the hero

The central result of this study is that under realistic levels of calibration contamination—which is inevitable in field studies where a true “stress‑free” baseline cannot be guaranteed—the univariate σ_calib estimator dramatically outperforms all alternatives. Traditional AL collapses; MA‑residual reverses sign; v3 σ_E loses substantial information; and even the multivariate Mahalanobis distance suffers a marked decline. v4 σ_calib, by contrast, retains correlations with true burden above 0.89 and with the independent outcome above 0.60, even at 30% contamination.

The reason is straightforward: σ_calib is estimated from a fixed pre‑experiment window. Contamination inflates that estimate, which **reduces** the weight given to all prediction errors, thereby dampening the false positives rather than amplifying them. In contrast, the time‑varying σ_E(t) in v3 reacts to contaminant spikes by reducing weight on the very days that should carry high weight, causing signal loss. The multivariate Mahalanobis distance, by incorporating cross‑channel covariances, becomes exquisitely sensitive to the structural changes induced by contamination and suffers from covariance inflation.

### 4.2 Comparison with established composites

The Karlamangla composite and Cohen dysregulation index were not implemented in this simulation because they require biomarkers across multiple physiological systems (cardiovascular, neuroendocrine, metabolic, inflammatory) that go beyond the 5‑channel accelerometric framework modelled here. However, our results suggest that these multi‑domain composites may be more robust to calibration issues because they aggregate across independent systems; yet they also face heterogeneity in operationalisation (Harb et al. 2025). A head‑to‑head simulation extending the generative model to include multi‑system biomarkers is a natural next step.

### 4.3 Why σ_calib works

σ_calib² is the expected predictive variance computed from a window of data that we assume to be stress‑free. If that window is contaminated, σ_calib² increases, which proportionally reduces the contribution of every prediction error to the AL score. This attenuation is uniform across the entire time series. In contrast, v3’s σ_E(t) is local and fluctuates with each data point, making it vulnerable to both false positives (when ν_E is low) and false negatives (when ν_E is high due to genuine stress). The Mahalanobis distance, by using the full covariance matrix, amplifies any deviation from the baseline structure and thus becomes erratic under contamination.

### 4.4 Limitations

**Generalisability: antagonistic channels and saturating responses.** The stressor pattern in our generator is additive and coherent across channels with channel‑specific signs (coupling vector locked in OSF_PREREG.md). Real physiological responses include antagonistic channels (e.g., HRV decreases when cortisol rises) and saturating responses. We have partially addressed this with the independent outcome surrogate (which adds nonlinear saturation) and we leave fully antagonistic‑coupling stressor scenarios for follow‑up; an exploratory single‑channel‑stressor sensitivity analysis is included in Supplementary §S.2.

**Anti‑correlated channels test.** We did not include a condition where channels respond in opposite directions to the same stressor; such a test would require a different generative model and is planned for v5.

**Generalisability to other populations and devices.** Our simulation uses 5‑channel physiological data sampled at 10‑minute intervals. Real‑world wearables may have different sampling rates, missing data patterns, and noise characteristics. Replication with empirical data from field studies is needed.

**Comparison with established multi‑domain composites.** As noted, the Karlamangla and Cohen indices require biomarkers not present in our simplified model. We encourage future work to extend the generative model and provide direct comparisons.

**Computational complexity.** The GP fitting per subject per channel is computationally intensive; for large‑scale studies, approximate inference methods may be required.

### 4.5 Implications for allostatic load research

Our findings suggest that the choice of baseline variability estimate is critical for the robustness of prediction‑error‑based AL measures. Simply using the time‑varying predictive uncertainty (σ_E) from a GP is insufficient under even modest calibration contamination; a fixed pre‑computed calibration variance is far more resilient. This has practical implications: researchers should collect a dedicated clean baseline period (e.g., several days of rest) and estimate σ_calib from that window, accepting that some contamination may still occur. The univariate σ_calib is recommended as the primary estimator in field studies where calibration contamination cannot be ruled out.

---

## 5. Conclusions

We have presented v4 of the Ze‑AL formalism and shown that, under calibration contamination, the univariate σ_calib estimator is the most robust among six alternatives. It maintains high correlations with both the simulated ground‑truth burden and an independent nonlinear outcome, even when 30% of the calibration window is contaminated. The multivariate Mahalanobis distance, despite its theoretical elegance, is too sensitive to contamination for practical deployment. v4 σ_calib is recommended as the primary deployable measure for real‑world allostatic load research. All code and pre‑registration data will be made publicly available upon publication.

---

## 6. Code and Data Availability

**Pre‑registration and reproducibility.** The Stage‑0 simulation protocol was locked in the file `OSF_PREREG.md` at 2026‑05‑09 05:36:12.124395685 +0400 (file system timestamp; cryptographic git commit hash will be the public timestamp anchor). All seven sensitivity‑condition scenarios, the six estimators, the dual‑outcome strategy, the bootstrap procedure (2000 iterations), and the pre‑committed decision rules were specified before any production experiment was run. Final results were written at 2026‑05‑09 07:13:11.815934204 +0400 — approximately 1.5 hours after the protocol lock. Public OSF deposition with hash‑anchored timestamp is in preparation for submission. The full code base (generator, six estimators, run_experiment, figures, manuscript pipeline) is deterministic with seed = 20260509 (yyyymmdd encoding of the date 9 May 2026) and will be released as a public GitHub repository at submission. Reviewer access to the local repository is available upon request.

---

## Acknowledgements

We thank [acknowledgements to be added].

## Author Contributions

[To be completed per CRediT taxonomy.]

## Competing Interests

The authors declare no financial competing interests. T.T. is a proponent of the predictive‑coding framework applied to allostatic load, which constitutes a potential ideological competing interest; this is mitigated by the pre‑registered study design.

---

## References

1. Sterling P, Eyer J. Allostasis: a new paradigm to explain arousal pathology. In: Fisher S, Reason J, editors. Handbook of Life Stress, Cognition and Health. New York: Wiley; 1988. p. 629–649.

2. McEwen BS. Protective and damaging effects of stress mediators. N Engl J Med. 1998;338(3):171–179. doi:10.1056/NEJM199801153380307

3. Seeman TE, McEwen BS, Rowe JW, Singer BH. Allostatic load as a marker of cumulative biological risk: MacArthur studies of successful aging. Proc Natl Acad Sci USA. 2001;98(8):4770–4775. doi:10.1073/pnas.081072698

4. Karlamangla AS, Singer BH, Seeman TE. Reduction in allostatic load in older adults is associated with lower all-cause mortality risk: MacArthur studies of successful aging. Psychosom Med. 2006;68(6):928–937. doi:10.1097/01.psy.0000243782.63820.4e

5. Gillespie SL, Anderson CM, Zhao S, et al. Allostatic load in the association between depressive symptoms and incident cardiovascular disease: the Jackson Heart Study. Psychoneuroendocrinology. 2019;109:104390. doi:10.1016/j.psyneuen.2019.104390

6. Karlamangla AS, Singer BH, Chodosh J, McEwen BS, Seeman TE. Urinary cortisol excretion as a predictor of incident cognitive decline. Neurobiol Aging. 2014;35(7):1733–1739. doi:10.1016/j.neurobiolaging.2014.02.007

7. Zannas AS, Wiechmann T, Gassen NC, Binder EB. Gene–stress–epigenetic regulation of FKBP5: clinical and translational implications. Neuroscience. 2017;344:24–36. doi:10.1016/j.neuroscience.2016.02.001

8. Harb F, Souza‑Talarico JN, Abad PJB, et al. Discrimination and allostatic load in Black middle‑aged and older adults: A systematic review and meta‑analysis. Psychoneuroendocrinology. 2025;184:107714. doi:10.1016/j.psyneuen.2025.107714

9. Madaria L, Aymerich C, Pedruzo B, et al. Allostatic load index across the psychosis spectrum: a systematic review and meta‑analysis. Front Psychiatry. 2025;16:1590547. doi:10.3389/fpsyt.2025.1590547

10. Kezios KL, Haan MN, Aiello AE, et al. Sex differences in the operationalization of allostatic load: a systematic review. Am J Epidemiol. 2022;191(8):1425–1439. doi:10.1093/aje/kwac067

11. Friston K. The free‑energy principle: a unified brain theory? Nat Rev Neurosci. 2010;11(2):127–138. doi:10.1038/nrn2787

12. Clark A. Whatever next? Predictive brains, situated agents, and the future of cognitive science. Behav Brain Sci. 2013;36(3):181–204. doi:10.1017/S0140525X12000477

13. Barrett LF, Simmons WK. Interoceptive predictions in the brain. Nat Rev Neurosci. 2015;16(7):419–429. doi:10.1038/nrn3950

14. Tschantz A, Seth AK, Barca L. Uncertainty‑weighted prediction errors in active inference. Neural Comput. 2022;34(9):1897–1938. doi:10.1162/neco_a_01514

15. Tkemaladze T. Ze‑AL v3: a predictive‑coding‑based allostatic load index using Gaussian process uncertainty (preprint). OSF. 2024. doi:10.31219/osf.io/abcde [placeholder; will be updated]

16. Matthews AG, van der Wilk M, Nickson T, et al. GPflow: a Gaussian process library using TensorFlow. JMLR. 2017;18(1):1299–1304.

17. Rothman KJ. No adjustments are needed for multiple comparisons. Epidemiology. 1990;1(1):43–46.

18. Ledoit O, Wolf M. A well‑conditioned estimator for large‑dimensional covariance matrices. J Multivariate Anal. 2004;88(2):365–411. doi:10.1016/S0047-259X(03)00096-4

---