# Review A: PARANOID — Ze-AL-v4-manuscript-v3

## Article-type
research — original simulation-based methodological study with IMRaD structure.

## Verdict
**REJECT_AND_RESUBMIT**

## Scores (1-5)
- HypothesisClarity: 4
- IMRaDCompliance: 5
- StatisticalRigor: 4
- DataIntegrity: 1
- RefQualityTier: 4
- FactualAccuracy: 2
- SourceIntegrity: 3
- Reproducibility: 1
- AbstractMatch: 5
- DiscussionGrounded: 4
- COI_Honesty: 5

## Fact-check audit
| # | Claim/Quote/Number | Type | Verifiable? | Correct? | Action |
|---|-------------------|------|-------------|----------|--------|
| 1 | Pre-registration on OSF (osf.io/xxxxx) | Data integrity | No – link is placeholder | Cannot verify | Must provide real URL; seed date 20260509 appears to be in the future (May 2026) – anachronism or typo |
| 2 | Harb et al. (2025) Health Psychology 44(2) | Reference | Questionable – 2025 may still be in press | Likely real but unverifiable | Check publication status; if not yet published, cite as preprint |
| 3 | Madaria et al. (2025) J Psychiatr Res 170:98–107 | Reference | Questionable – same issue | Likely real but unverifiable | Same as above |
| 4 | Tkemaladze (2024) v3 preprint on OSF | Self-citation | Partially – URL not given | Assumed real | Provide URL; verify it exists |
| 5 | “Pearson correlation coefficients … with 95% bootstrap CI (10 000 resamples)” | Statistical method | Verifiable in principle | Correct | No action |
| 6 | “No correction for multiplicity … treated as separate experiments [17]” | Methodology | Verifiable | Acceptable per Rothman (1990) but some editors require correction | Minor issue |
| 7 | “seed = 20260509 encodes the date of pre-registration” | Factual | No – date is future | Incorrect or typo | Must correct seed or explain |

**Blocking issues:**
- Placeholder OSF link (osf.io/xxxxx) instead of valid URL → pre-registration and code not accessible.
- Pre-registration seed date appears to be in the future (2026-05-09) relative to any plausible review date; suggests either anachronism or deliberate misrepresentation.
- Two key references (Harb 2025, Madaria 2025) cannot be verified as published; if they are still in press or preprints, this must be stated.

## Statistical sub-audit (v2.0)
| Test/method | Appropriate? | Multiple-comp? | Power | Effect size | Pre-registered? | Score |
|---|---|---|---|---|---|---|
| Pearson correlation with bootstrap CI | Yes – for continuous association | No correction (stated, reference Rothman) | Post-hoc power >90% for r>0.3 | r with 95% CI reported | Claimed but not verifiable | 4/5 |
| | Missing: outlier handling rule, normality assumption check (though n=200 robust) | | | | | |

## Reference tier audit (v2.0)
| # | Citation | Tier (1-5) | Justification |
|---|----------|------------|--------------|
| 1 | Sterling & Eyer 1988 | 3 – book chapter | No DOI, but seminal; tier 3 |
| 2 | McEwen 1998 NEJM | 1 – original research | Top tier |
| 3 | Seeman 2001 PNAS | 1 – top tier | |
| 4 | Karlamangla 2006 Psychosom Med | 2 – top specialty | |
| 5 | Gillespie 2019 Brain Behav Immun | 2 – specialty top | |
| 6 | Karlamangla 2014 Neurobiol Aging | 2 – good specialty | |
| 7 | Zannas 2017 Neuroscience | 2 – good | |
| 8 | Harb 2025 Health Psychol | 3 – solid but unverifiable | Tier uncertain; assign 3 |
| 9 | Madaria 2025 J Psychiatr Res | 3 – solid but unverifiable | |
| 10 | Kezios 2022 Am J Epidemiol | 2 – top epidemiology | |
| 11 | Friston 2010 Nat Rev Neurosci | 1 – top review | |
| 12 | Clark 2013 Behav Brain Sci | 1 – high impact | |
| 13 | Barrett 2015 Nat Rev Neurosci | 1 – top | |
| 14 | Tschantz 2022 Neural Comput | 2 – good | |
| 15 | Tkemaladze 2024 preprint OSF | 4 – preprint | |
| 16 | Matthews 2017 JMLR | 2 – top ML | |
| 17 | Rothman 1990 Epidemiology | 2 – good methods | |
| 18 | Ledoit & Wolf 2004 J Multivariate Anal | 2 – good | |

Average tier ≈ (3+1+1+2+2+2+2+3+3+2+1+1+1+2+4+2+2+2)/18 ≈ 1.94 → score 4 (since 1.94 is near 2, corresponding to tier 2 average → score = 5 - (average tier - 1)? Actually the scoring: Tier 1=5, Tier 2=4, Tier 3=3, etc. Average tier 1.94 ≈ tier 2 → score 4. Acceptable.

## Plagiarism / attribution audit
No clear instances of copy-paste or misattribution; all quotes and ideas are properly attributed.

## Conflict-of-Interest audit (v2.0 — expanded)
| Type | Detected? | Severity | Disclosed in paper? |
|---|---|---|---|
| Financial (industry funding, stock, patents) | No | None | Yes – “no financial competing interests” |
| Ideological (author = theory inventor) | Yes – T.T. is a proponent of predictive-coding framework | Low – mitigated by pre-registration | Yes – stated in Competing Interests |
| Career (dependency on outcome / promotion / funding) | No explicit, but first author may have career interest | Minor | Not explicitly, but pre-registration is partial mitigation |

## Checklist (12 items ✓/✗)
1. Operationalised falsifiable hypothesis ✓
2. IMRaD structure ✓
3. Statistical methods appropriate (full sub-audit pass) ✓
4. Limitations explicit ✓
5. Conflict of interest declared FULLY (financial + ideological + career) ✓
6. Reference reality + tier ≥3 average ✗ (two 2025 refs unverifiable)
7. No fabrication markers / data integrity ✗ (placeholder OSF, anachronistic seed)
8. Internal consistency (Abstract = Results = Discussion) ✓
9. Evidence base + meta-analysis context ✓
10. Methodology depth (replication-ready) ✗ (code unavailable)
11. Data/code availability ✗ (placeholder)
12. Author contributions (CRediT) ✓ (partial but acceptable)

**Count: 8 ✓, 4 ✗**

## Blocking issues (factual integrity / plagiarism — text-revision won't fix)
1. **Data integrity fundamentally compromised**: The OSF repository link is a placeholder (`osf.io/xxxxx`); there is no way to verify pre-registration, simulation code, or seed. The seed date `20260509` is anachronistic (May 2026) relative to the review period. Without verifiable code and pre-registration, the study is not reproducible and the claims of pre-registration are unverifiable.

## Fixable issues (max 3)
1. Replace all placeholder URLs with actual OSF links; correct the seed date to a plausible past date (e.g., 20250509) and ensure pre-registration timestamp precedes simulation execution.
2. Provide full simulation code, analysis scripts, and derived data in a public repository.
3. Verify the publication status of Harb et al. (2025) and Madaria et al. (2025); if not yet published, cite as preprints and note the status.

---

# Review B: CYNIC — Ze-AL-v4-manuscript-v3

## Article-type
research

## Verdict
**ACCEPT**

## Scores (1-5)
- HypothesisClarity: 5
- IMRaDCompliance: 5
- StatisticalRigor: 4
- DataIntegrity: 4
- RefQualityTier: 4
- FactualAccuracy: 4
- SourceIntegrity: 4
- Reproducibility: 3
- AbstractMatch: 5
- DiscussionGrounded: 5
- COI_Honesty: 5

## Fluff & Padding audit
| Section/Chapter | Real content (Y/N) | Specific to book's thesis (Y/N) | Generic/cliché | Score |
|---|---|---|---|---|
| Abstract | Y | Y | N – concise, no hype | 5 |
| Introduction 1.1 | Y | Y – literature review focused on AL heterogeneity | N | 5 |
| 1.2 | Y | Y – predictive coding motivation | N | 5 |
| 1.3 | Y | Y – v3 problem and v4 proposal | N | 5 |
| Methods 2.1 | Y | Y – full simulation details | N | 5 |
| 2.2 | Y | Y – estimator definitions | N | 5 |
| 2.3 | Y | Y – independent outcome | N – clever design | 5 |
| 2.4 | Y | Y – statistical plan | N | 5 |
| Results 3.1-3.3 | Y | Y – tables and sensitivity | N – necessary | 5 |
| Discussion 4.1-4.4 | Y | Y – honest appraisal, no overclaim | N | 5 |
| Conclusion | Y | Y – practical recommendation | N | 5 |

No fluff, no padding, no clickbait. The paper earns every paragraph.

## Repetition / circularity audit
| Idea | Mentioned in chapters | Different angles? |
|---|---|---|
| σ_calib is robust under contamination | 3.2, 4.2, 5 | Yes – results, mechanism, practical implication |
| Mahalanobis is better clean but fragile | 3.1, 3.2, 4.2, 4.3 | Yes – repeated in different contexts, but that's reinforcement, not repetition |
| Limitations | 4.4 | Only once – appropriate |

No problematic repetition.

## Checklist (12 items ✓/✗)
1. ✓
2. ✓
3. ✓
4. ✓
5. ✓
6. ✓ (refs solid, mostly verifiable; two 2025 refs are minor concern but acceptable for now)
7. ✓
8. ✓
9. ✓
10. ✓ (methodology depth sufficient for simulation study)
11. ✗ (code not publicly available – the only flaw)
12. ✓

**Count: 11 ✓, 1 ✗**

## Blocking issues
None.

## Fixable issues (max 3)
1. Provide the OSF repository with code and data to fully enable replication.
2. Add a brief note on how the kernel was chosen (cross-validation or prior knowledge) to enhance replicability.
3. (Minor) Consider including a comparison with one existing dynamic AL algorithm (e.g., cumulative deficit index with time-varying thresholds) to strengthen practical relevance.

---

# Review C: RED TEAM — Ze-AL-v4-manuscript-v3

## Article-type
research

## Verdict
**REVISE_MINOR**

## Scores (1-5)
- HypothesisClarity: 4
- IMRaDCompliance: 5
- StatisticalRigor: 3
- DataIntegrity: 3
- RefQualityTier: 4
- FactualAccuracy: 4
- SourceIntegrity: 4
- Reproducibility: 2
- AbstractMatch: 5
- DiscussionGrounded: 4
- COI_Honesty: 5

## Counter-argument audit
| Author's claim | Strongest counter-argument | Engaged in book? | Quality of engagement |
|---|---|---|---|
| v4 σ_calib is the most robust under calibration contamination | There are many other dynamic AL measures (e.g., dynamical system load, multi-scale entropy, cumulative deficit index) that may be equally or more robust; the paper only compares traditional quartile and MA-residual | Partially – limitations mention "did not compare against other dynamic AL metrics" but does not test them | Weak – omission of state-of-the-art comparators weakens the claim of superiority |
| Mahalanobis is fragile because Σ_calib is inflated under contamination | The James-Stein shrinkage (Ledoit-Wolf) could stabilise Σ_calib; the authors mention this as future work but do not test it | Superficially – one sentence in Discussion | Acceptable given scope, but a simulation including shrinkage would strengthen |
| The outcome surrogate breaks circularity | The surrogate is still derived from the same burden variable; it is not truly independent (e.g., clinical data) | Acknowledged in limitations | Adequate |
| Known GP kernel is assumed | In practice, kernel misspecification could severely bias predictions; the paper tests lengthscale and noise variations but not kernel function misspecification | Tested some perturbations but not kernel function (e.g., using Matérn vs periodic) | Partial – could add a scenario with wrong kernel form |

## Bias audit
| Type (selection / confirmation / survivor / financial / ideological) | Severity | Disclosed? |
|---|---|---|
| Selection bias: Only tested their own v3 and v4, not competitor AL methods | Moderate – claim of "most robust" requires broader comparison | Not explicitly; limitations note missing comparisons |
| Confirmation bias: All scenarios favour v4 σ_calib under contamination; no scenario where another method outperforms it significantly | Low – contamination scenarios are central, but no negative-case analysis | Partially mitigated by pre-registration |
| Ideological: Author is proponent of predictive-coding framework | Low – disclosed | Yes |
| Financial: None | None | Yes |

## Checklist (12 items ✓/✗)
1. ✓
2. ✓
3. ✓ (statistical methods appropriate, but see counter-argument)
4. ✓ (limitations section present)
5. ✓
6. ✓
7. ✗ (data not available; replication impossible)
8. ✓
9. ✓
10. ✓ (depth adequate for a simulation)
11. ✗ (code not public)
12. ✓

**Count: 10 ✓, 2 ✗**

## Blocking issues
None – the paper is conceptually sound and sufficiently original.

## Fixable issues (max 3)
1. **Add comparisons with at least one other dynamic AL estimator** (e.g., dynamic system load from time-series complexity, or a moving-window cumulative deficit index) to show that the claimed robustness is not an artefact of the chosen comparators.
2. **Test at least one misspecified kernel functional form** (e.g., Matérn instead of periodic) to assess sensitivity of v4 σ_calib.
3. Provide code and data to enable full reproducibility (shared with other reviewers).

---

# TBPR-article Combined Verdict — Ze-AL-v4-manuscript-v3

## Per-reviewer breakdown
- **A (PARANOID)**: REJECT_AND_RESUBMIT (score sum 39/55) — top concern: data integrity (placeholder OSF, anachronistic seed) and unverifiable pre-registration  
- **B (CYNIC)**: ACCEPT (score sum 48/55) — top concern: lack of code availability (minor)  
- **C (RED TEAM)**: REVISE_MINOR (score sum 43/55) — top concern: missing comparisons with other dynamic AL methods and generalizability tests

## Combined verdict (worst of 3)
**REJECT_AND_RESUBMIT**

## Combined score
score = MIN(39, 48, 43) = **39/55**

## Editorial recommendation
- **Suggested publisher tier**: tier-2 academic (Springer / Routledge) – suitable for specialist methodological audience  
- **Estimated time-to-publication**: 6 months with M=2 revision rounds (addressing data availability, comparisons, and generalizability)

## Top 3 actions for author
1. **Fix data integrity immediately**: Replace all OSF placeholders with actual, locked, versioned repository links containing the simulation code, analysis scripts, and pre-registration document. Correct the seed date to a past date (e.g., 20250509) and ensure pre-registration timestamp precedes simulation execution. Without this, the paper cannot be considered reproducible.
2. **Broaden the comparator set**: Include at least one existing dynamic AL estimator (e.g., dynamical system load, multi-scale entropy, or time-varying cumulative deficit) to demonstrate that v4 σ_calib is not just best among the chosen few.
3. **Test kernel misspecification**: Run at least one scenario where the GP kernel is intentionally misspecified (e.g., use Matérn kernel for data generated with periodic kernel) to assess robustness of all estimators, especially v4 σ_calib. This will directly address a key limitation acknowledged but not tested.