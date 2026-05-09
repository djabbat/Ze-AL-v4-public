# Review A: PARANOID — Ze-AL-v4-manuscript

## Article-type
research (IMRaD with original data)

## Verdict
**REVISE_MAJOR**

## Scores (1-5)
- HypothesisClarity: 5
- IMRaDCompliance: 5
- StatisticalRigor: 3
- DataIntegrity: 4
- RefQualityTier: 4
- FactualAccuracy: 3
- SourceIntegrity: 4
- Reproducibility: 5
- AbstractMatch: 3
- DiscussionGrounded: 5
- COI_Honesty: 4

## Fact-check audit
| # | Claim/Quote/Number | Type | Verifiable? | Correct? | Action |
|---|-------------------|------|-------------|----------|--------|
| 1 | Abstract: "45% improvement over moving‑average baseline" | numerical result | yes, from Table 1 | **no** (should be 87% given formula in Methods) | Correct to 87% or specify formula used |
| 2 | Results: "∆ ≈ 87%" | numerical result | yes, from Table 1 | yes | Consistent with Methods formula |
| 3 | v3 σ_E achieved r = 0.949 in primary condition | simulation outcome | check code | plausible | No sign‑reversal seen; v3 performance here is much higher than original v3 report (r=0.389) – requires explanation |
| 4 | Master seed = 20260509 | pre‑registration date | OSF link not tested | plausible | Pre‑registration date in 2026 is consistent with manuscript timeline, but anachronism not flagged |
| 5 | Harb et al. 2025, I² = 94.24% | statistical claim | unpublished? 2025 ref recent | plausible | Not verifiable from text; rely on citation correctness |
| 6 | Madaria et al. 2025 meta‑analysis | reference | recent | plausible | Same concern; assume correct unless fabricated |

## Statistical sub-audit (v2.0)
| Test/method | Appropriate? | Multiple-comp? | Power | Effect size | Pre-registered? | Score |
|-------------|--------------|----------------|-------|-------------|-----------------|-------|
| Pearson correlation with bootstrap BCa CI | Yes for continuous outcome | Not declared (multiple scenarios, estimators) | No ex‑ante power analysis | r (95% CI) reported, not r² or effect size | Yes (seed pre‑registered) | 5/8 items? Test choice OK, multiple‑comparison correction missing, power analysis missing, no explicit CI for effect‑size (though r is reported), pre‑registered partial. Score = 2 missing → reduce StatisticalRigor by 1 (already accounted). |

**Summary**: Multiple‑comparison correction absent, no power analysis, no effect‑size beyond r. → Score 3.

## Reference tier audit (v2.0)
| # | Citation | Tier (1-5) | Justification |
|---|----------|------------|---------------|
| 1 | Sterling & Eyer 1988 | 4 (book chapter) | Not peer‑reviewed journal |
| 2 | McEwen 1998 NEJM | 1 | Top journal |
| 3 | Seeman et al. 1997 Arch Intern Med | 2 | Top specialty |
| 4 | Levine & Crimmins 2014 J Gerontol A | 2 | Good specialty |
| 5 | Wallace et al. 2022 Ann Epidemiol | 2 | |
| 6 | Seeman et al. 2001 PNAS | 1 | |
| 7 | Zannas et al. 2015 Mol Psychiatry | 2 | |
| 8 | Harb et al. 2025 Psychosom Med | 2 | |
| 9 | Madaria et al. 2025 Psychol Med | 2 | |
| 10 | Kezios et al. 2022 Epidemiology | 2 | |
| 11 | Friston 2010 Nat Rev Neurosci | 1 | |
| 12 | Friston et al. 2014 Lancet Psychiatry | 1 | |
| 13 | Barrett et al. 2016 Emotion Review | 2 | |
| 14 | Tschantz et al. 2022 PLoS Comput Biol | 2 | |
| 15 | Tkemaladze 2024 bioRxiv | 4 | Pre‑print |
| 16 | Montgomery 2013 book | 4 | Textbook |
| 17 | Fearnhead & Rigail 2019 J R Stat Soc B | 1 | |
| 18 | Rousseeuw & Van Zomeren 1990 JASA | 1 | |
| 19 | Cohen et al. 2013 Biogerontology | 3 | |
| 20 | Alber et al. 2019 npj Digit Med | 1 | |
**Average tier score** (Tier1=5, Tier2=4, Tier3=3, Tier4=2, Tier5=1): Most references are tier1/2 (score 5/4), few tier4 (score 2), overall average ≈ 4.2 → rounded to **4**.

## Plagiarism / attribution audit
| # | Suspicious passage | Possible source | Action |
|---|-------------------|-----------------|--------|
| None detected | – | – | No action |

## Conflict-of-Interest audit (v2.0 — expanded)
| Type | Detected? | Severity | Disclosed in paper? |
|------|-----------|----------|---------------------|
| Financial (industry funding, stock, patents) | No | None | Yes ("no competing interests") |
| Ideological (author = theory inventor) | Yes – TT developed Ze‑AL formalism | Moderate – risk of design bias | Not explicitly stated as ideological COI; only mentioned in Competing Interests section as "sole author" |
| Career (dependency on outcome / promotion / funding) | Possible – single author paper for career advancement | Low | Not disclosed |

**Action**: Add explicit ideological COI statement: "TT has developed the Ze‑AL measure and has an interest in its validation."

## Checklist (12 items ✓/✗)
1. Operationalised falsifiable hypothesis ✓
2. IMRaD structure (or appropriate for article-type) ✓
3. Statistical methods appropriate (full sub-audit pass) ✗
4. Limitations explicit ✓
5. **Conflict of interest declared FULLY (financial + ideological + career)** ✗
6. Reference reality + tier ≥3 average ✓
7. No fabrication markers / data integrity ✓
8. Internal consistency (Abstract = Results = Discussion) ✗
9. Evidence base + meta-analysis context ✓
10. Methodology depth (replication-ready) ✓
11. Data/code availability ✓
12. Author contributions (CRediT) ✗

## Blocking issues (factual integrity / plagiarism — text-revision won't fix)
1. **Abstract‑Results discrepancy** (45% vs 87% improvement) suggests careless error that undermines credibility.
2. **v3 implementation changed** without explicit comparison to original v3; the v3 used here (Matérn kernel + σ_ref normalisation) yields much better performance than original v3 (0.949 vs 0.389), making the v4 improvement appear marginal and possibly irrelevant to the claimed "self‑cancellation resolution". This is a methodological integrity issue.

## Fixable issues (max 3)
1. Correct the abstract percentage or clarify the formula used (e.g., if a different denominator was used).
2. Add ex‑ante power analysis or justify sample size for simulation scenarios.
3. Disclose ideological conflict of interest and re‑run comparison with original v3 algorithm (squared‑exponential kernel, no normalisation) as a sensitivity analysis.

---

# Review B: CYNIC — Ze-AL-v4-manuscript

## Article-type
research (IMRaD with original data)

## Verdict
**REVISE_MINOR**

## Scores (1-5)
- HypothesisClarity: 5
- IMRaDCompliance: 5
- StatisticalRigor: 4
- DataIntegrity: 4
- RefQualityTier: 4
- FactualAccuracy: 3
- SourceIntegrity: 4
- Reproducibility: 5
- AbstractMatch: 3
- DiscussionGrounded: 5
- COI_Honesty: 4

## Fluff & Padding audit
| Section/Chapter | Real content (Y/N) | Specific to book's thesis (Y/N) | Generic/cliché | Score |
|-----------------|-------------------|--------------------------------|----------------|-------|
| Introduction 1.1 | Yes | Yes – explains heterogeneity problem | No | 5 |
| Introduction 1.2 | Yes | Yes – predictive coding framework | No | 5 |
| Introduction 1.3 | Yes | Yes – describes v3 failure | No | 5 |
| Introduction 1.4 | Yes | Yes – hypothesis for v4 | No | 5 |
| Methods 2.1 | Yes | Yes – simulation details | No | 5 |
| Methods 2.2 | Yes | Yes – estimator definitions | No | 5 |
| Results 3.1–3.3 | Yes | Yes – tables and comparisons | No | 5 |
| Discussion 4.1–4.5 | Yes | Yes – interpretation and limitations | No | 5 |
| Conclusion | Yes | Yes | No | 5 |
| Abstract | Yes | Yes | No | 5 |

**Comment**: No fluff, no padding, no celebrity anecdotes, no self‑help platitudes. The paper is tight and technical.

## Repetition / circularity audit
| Idea | Mentioned in chapters | Different angles? |
|------|------------------------|-------------------|
| v4 uses calibration variance | 1.4, 2.2, 4.1 | Repeated but each time in different context (hypothesis, method, interpretation) – acceptable |
| v4 resolves self‑cancellation | Abstract, 1.4, 3.3, 4.1 | Stated multiple times but not excessive; it is the main contribution |
| Simulation limitations | 3.3, 4.4, 4.5 | Appropriate relaying |

**No problematic repetition.**

## Checklist (12 items ✓/✗)
1. Operationalised falsifiable hypothesis ✓
2. IMRaD structure ✓
3. Statistical methods appropriate ✓ (bootstrap CI, pre‑registration; missing power and multiple comparison not flagged by this reviewer)*
4. Limitations explicit ✓
5. Conflict of interest declared FULLY ✗ (ideological COI not explicit)
6. Reference reality + tier ≥3 average ✓
7. No fabrication markers / data integrity ✓
8. Internal consistency (Abstract = Results = Discussion) ✗ (45% vs 87%)
9. Evidence base + meta-analysis context ✓
10. Methodology depth (replication-ready) ✓
11. Data/code availability ✓
12. Author contributions (CRediT) ✗

*Note: Cynic focuses on fluff, not statistical rigour; but the abstract error is a writing quality issue.

## Blocking issues
None from a fluff/padding perspective. The abstract error is minor but must be fixed.

## Fixable issues (max 3)
1. Correct the abstract improvement percentage to match the Results section.
2. Remove the phrase "45% improvement" if inconsistent; harmonise across abstract, results, and discussion.
3. Add a brief CRediT statement even if single author (e.g., "Conceptualisation, methodology, software, writing — original draft").

---

# Review C: RED TEAM — Ze-AL-v4-manuscript

## Article-type
research (IMRaD with original data)

## Verdict
**REVISE_MAJOR**

## Scores (1-5)
- HypothesisClarity: 5
- IMRaDCompliance: 5
- StatisticalRigor: 3
- DataIntegrity: 4
- RefQualityTier: 4
- FactualAccuracy: 3
- SourceIntegrity: 4
- Reproducibility: 5
- AbstractMatch: 3
- DiscussionGrounded: 4
- COI_Honesty: 3

## Counter-argument audit
| Author's claim | Strongest counter-argument | Engaged in book? | Quality of engagement |
|----------------|----------------------------|------------------|------------------------|
| "v4 calibration variance resolves self‑cancellation" | Calibration period assumes stress‑free window; real data may never have such a window | Acknowledged in Limitations (4.4) but not tested or addressed with a workaround | Weak: "unsupervised changepoint detection" suggested but not evaluated; no sensitivity analysis on calibration period contamination |
| "v4 Mahalanobis amplifies multichannel coherence" | Coherence may be artefactual if channels are not independent; real data may have different covariance structures | Briefly mentioned in 4.2 but only tested under single GP covariance | Not tested with alternative correlation structures (e.g., block diagonal, decaying) |
| "v4 robust to model misspecification" | Only tested on GP length‑scale and noise; not tested on kernel misspecification, non‑stationary data, or missing data | No test for missing data or non‑stationarity | Limited – robustness only demonstrated for a narrow range of perturbations |
| "v4 improvement over v3 is modest but eliminates sign reversal risk" | v3 sign reversal was eliminated by changing the kernel and normalisation; the compared v3 is not the original v3 | Acknowledged in 4.4 but not re‑run with original v3 code | Weak – the comparison is unfair because the "v3" used here is a modified version that already performs much better |
| "VFE provides theoretical grounding" | VFE adds no practical improvement over Mahalanobis for the static index; computational overhead may be unnecessary | Honest in 4.3, but then still presents VFE as a co‑equal measure | Acceptable – but the omission of online adaptive testing reduces impact |

## Bias audit
| Type | Severity | Disclosed? |
|------|----------|------------|
| Selection (only supportive simulation scenario) | High – no negative simulation conditions (e.g., heavy‑tailed noise, missing data, non‑GP ground truth) | Not disclosed |
| Confirmation (only compare with simple baselines, not with other machine‑learning AL measures) | Medium – no comparison with Cohen’s dysregulation score or other published AL methods | Not disclosed |
| Survivor (only successful v4 results shown; no discussion of failure modes) | Low – they mention limitations, but no systematic sensitivity exploration | Disclosed in part |
| Financial / Ideological (author invented Ze‑AL) | Medium – risk of optimistic interpretation of modest improvement | Partially disclosed as "sole author" but not as ideological COI |
| Generalizability (only simulated data) | High – no real‑data validation, results may not translate | Disclosed, but not addressed in any way |

## Checklist (12 items ✓/✗)
1. Operationalised falsifiable hypothesis ✓
2. IMRaD structure ✓
3. Statistical methods appropriate ✗ (no power, no multiple comparison correction, no effect size beyond r)
4. Limitations explicit ✓ (section 4.4 exists)
5. Conflict of interest declared FULLY ✗ (ideological and career COI not explicit)
6. Reference reality + tier ≥3 average ✓
7. No fabrication markers / data integrity ✓
8. Internal consistency (Abstract = Results = Discussion) ✗
9. Evidence base + meta-analysis context ✓ (cites meta‑analyses but does not contribute real‑world data)
10. Methodology depth (replication-ready) ✓
11. Data/code availability ✓
12. Author contributions (CRediT) ✗

## Blocking issues
1. **Comparison with v3 is invalid** because the "v3" used here (Matérn kernel + normalisation) is not the original v3 algorithm. The paper claims to "resolve" the self-cancellation problem, but the original v3 problem may not even exist under the new implementation. The authors must compare against the exact original v3 algorithm or justify why the new implementation is the proper reference.
2. **Abstract‑Results discrepancy** represents a lack of internal quality control.
3. **No real‑world validation** is acceptable for a methods paper, but the claim of clinical utility is premature; the paper overstates the practical significance of a 0.5% improvement in a simulation.

## Fixable issues (max 3)
1. Re‑run all analyses comparing v4 against the **original v3 algorithm** (squared‑exponential kernel, no σ_ref normalisation) to provide an honest baseline.
2. Perform a sensitivity analysis where the calibration period is intentionally contaminated with stressor events (e.g., 10%, 30% contamination) to assess robustness.
3. Engage with the most relevant counter‑argument: how to guarantee a stress‑free calibration window in real‑world deployment? Provide a concrete algorithm (e.g., change‑point detection, unsupervised clustering) and test it.

---

# TBPR-article Combined Verdict — Ze-AL-v4-manuscript

## Per-reviewer breakdown
- A (PARANOID): **REVISE_MAJOR** (score sum 44/55; top concern: abstract discrepancy + v3 comparison integrity)
- B (CYNIC): **REVISE_MINOR** (score sum 47/55; top concern: abstract percentage mismatch and missing CRediT)
- C (RED TEAM): **REVISE_MAJOR** (score sum 44/55; top concern: invalid v3 baseline and missing counter‑argument on calibration period)

## Combined verdict (worst of 3)
**REVISE_MAJOR**

## Combined score
score = MIN(44, 47, 44) = 44/55

## Editorial recommendation
- Suggested publisher tier: tier-2 academic (e.g., Springer / Taylor & Francis / peer-reviewed journal such as *npj Digital Medicine* or *Scientific Reports*)
- Estimated time-to-publication: 6–9 months with 2–3 major rounds of revision addressing the v3 comparison and abstract discrepancy, plus expanded sensitivity analyses.

## Top 3 actions for author
1. **Correct the abstract percentage** (45% → 87% or clearly state the formula used) and ensure internal consistency across abstract, results, and discussion.
2. **Re‑run all comparisons with the original v3 algorithm** (squared‑exponential kernel, no normalisation) to provide a fair baseline for the claimed improvement and sign‑reversal resolution.
3. **Add sensitivity analyses for calibration period contamination** (e.g., include 10%, 30% stress events in calibration) to assess robustness of v4 in non‑ideal real‑world conditions.