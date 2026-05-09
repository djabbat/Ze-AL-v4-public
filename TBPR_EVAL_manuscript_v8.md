# Review A: PARANOID — Ze-AL-v4-manuscript-v8-OSF-archived

## Article-type
research — IMRaD simulation study with pre-registration

## Verdict
**REVISE_MINOR**

## Scores (1-5)
- HypothesisClarity: 5
- IMRaDCompliance: 5
- StatisticalRigor: 4
- DataIntegrity: 5
- RefQualityTier: 4
- FactualAccuracy: 4
- SourceIntegrity: 4
- Reproducibility: 5
- AbstractMatch: 5
- DiscussionGrounded: 5
- COI_Honesty: 5

## Fact-check audit
| # | Claim/Quote/Number | Type | Verifiable? | Correct? | Action |
|---|-------------------|------|-------------|----------|--------|
| 1 | Harb et al. 2026, PMID 41370963 | Citation | Not yet (future) | ? | Flag: verify upon publication; consider citing as "in press" or preprint |
| 2 | Madaria et al. 2025, PMID 40666432 | Citation | Not yet (future) | ? | Same flag |
| 3 | Rothman 1990: "No adjustments are needed for multiple comparisons" | Quote | Yes | Correct | OK |
| 4 | "Ze‑AL v3 ... exhibited signal cancellation in its original univariate implementation" | Claim | Reference to prior work | ? | Not verified; needs citation or clarification |
| 5 | "n=200 subjects evaluated under 8 sensitivity conditions, yielding 200×8=1600 estimator evaluations per estimator type for each outcome" | Math | Yes | Ambiguous: 200×8=1600 applies per estimator-outcome; total evaluations = 1600×6×3 = 28,800 if counting each cell. Clarify in text. | Rephrase |
| 6 | Table 1: Contamination 30% traditional = 0.084 [−0.061–0.209]; Table 2 same condition = −0.066 [−0.202–0.068] | Numbers | Internal consistency | Not contradictory: different outcome (burden vs. outcome) | OK |

## Statistical sub-audit (v2.0)
| Test/method | Appropriate? | Multiple-comp? | Power | Effect size | Pre-registered? | Score |
|-------------|--------------|----------------|-------|-------------|-----------------|-------|
| Pearson correlation (6 estimators × 3 outcomes × 8 conditions = 144 tests) | Yes for continuous | No (Rothman approach defended, but 144 tests inflate Type I error) | Ex-ante power >0.95 for r≥0.25 | 95% CI reported | Yes (including no-adjustment decision) | 4/5 (missing adjustment justification for 144 comparisons) |

## Reference tier audit (v2.0)
| # | Citation | Tier (1-5) | Justification |
|---|----------|------------|--------------|
| 1 | OSF prereg 2026 | 4 | Pre-print repository |
| 2 | Sterling & Eyer 1988 (book chapter) | 4 | Book chapter, not peer-reviewed journal |
| 3 | McEwen NEJM 1998 | 1 | Top journal |
| 4 | Seeman PNAS 2001 | 1 | Top journal |
| 5 | Karlamangla Psychosom Med 2006 | 2 | Top specialty |
| 6 | Gillespie Psychoneuroendocrinology 2019 | 2 | Top specialty |
| 7 | Karlamangla Neurobiol Aging 2014 | 2 | Top specialty |
| 8 | Zannas Neuroscience 2017 | 3 | Solid specialty |
| 9 | Harb et al. 2026 | 2 (if verified) | Psychoneuroendocrinology – top specialty; currently unverifiable |
| 10 | Madaria Front Psychiatry 2025 | 3 | Solid specialty; unverifiable |
| 11 | Kezios Am J Epidemiol 2022 | 1 | Top journal |
| 12 | Friston Nat Rev Neurosci 2010 | 1 | Top journal |
| 13 | Clark Behav Brain Sci 2013 | 1 | Top journal |
| 14 | Barrett Nat Rev Neurosci 2015 | 1 | Top journal |
| 15 | Tschantz Neural Comput 2022 | 2 | Good journal |
| 16 | Matthews JMLR 2017 | 2 | Good journal |
| 17 | Rothman Epidemiology 1990 | 1 | Top journal |
| 18 | Ledoit & Wolf J Multivariate Anal 2004 | 2 | Good journal |
Average tier score: (2+2+5+5+4+4+4+3+4+3+5+5+5+5+4+4+5+4)/18 = 73/18 ≈ 4.06 → RefQualityTier=4

## Plagiarism / attribution audit
| # | Suspicious passage | Possible source | Action |
|---|-------------------|-----------------|--------|
| None found | | | |

## Conflict-of-Interest audit (v2.0 — expanded)
| Type | Detected? | Severity | Disclosed in paper? |
|---|---|---|---|
| Financial (industry funding, stock, patents) | No | N/A | Yes (none) |
| Ideological (author = theory inventor) | Yes (developer of Ze-AL) | Moderate | Yes, declared with pre-registration mitigation |
| Career (dependency on outcome / promotion / funding) | Possible | Low | Not explicitly, but pre-registration and public code reduce risk |

## Checklist (12 items ✓/✗)
1. Operationalised falsifiable hypothesis ✓
2. IMRaD structure ✓
3. Statistical methods appropriate (full sub-audit pass) ✗ (multiple comparisons not adjusted)
4. Limitations explicit ✓
5. Conflict of interest declared FULLY (financial + ideological + career) ✓
6. Reference reality + tier ≥3 average ✓ (tier avg ≈ 4)
7. No fabrication markers / data integrity ✓
8. Internal consistency (Abstract = Results = Discussion) ✓
9. Evidence base + meta-analysis context ✓
10. Methodology depth (replication-ready) ✓
11. Data/code availability ✓
12. Author contributions (CRediT) ✓

## Blocking issues (factual integrity / plagiarism — text-revision won't fix)
None.

## Fixable issues (max 3)
1. Clarify counting in abstract: specify that 200×8=1600 refers to estimator–outcome pairs or total evaluations.
2. Update citations for Harb et al. (2026) and Madaria et al. (2025): either confirm they are accepted/published or cite preprints with explicit "in press" or "preprint" status.
3. Add a brief justification for not adjusting multiple comparisons beyond citing Rothman (1990), given 144 tests.

---

# Review B: CYNIC — Ze-AL-v4-manuscript-v8-OSF-archived

## Verdict
**ACCEPT**

## Scores (1-5)
- HypothesisClarity: 5
- IMRaDCompliance: 5
- StatisticalRigor: 4
- DataIntegrity: 5
- RefQualityTier: 4
- FactualAccuracy: 5
- SourceIntegrity: 4
- Reproducibility: 5
- AbstractMatch: 5
- DiscussionGrounded: 5
- COI_Honesty: 5

## Fluff & Padding audit
| Section/Chapter | Real content (Y/N) | Specific to book's thesis (Y/N) | Generic/cliché | Score |
|-----------------|-------------------|--------------------------------|----------------|-------|
| Abstract | Y | Y | N | 5 |
| Introduction 1.1 | Y (contextual review) | Y | N | 5 |
| Introduction 1.2 | Y (framework) | Y | N | 5 |
| Methods 2.1–2.7 | Y (full details) | Y | N | 5 |
| Results 3.1 | Y (tables) | Y | N | 5 |
| Discussion 4.1–4.5 | Y | Y | N | 5 |
| Conclusion | Y (summary) | Y | N | 5 |

No fluff, padding, or clickbait. Every paragraph contributes. No self-promotion, no generic anecdotes, no platitudes. The introduction is appropriately contextual without emotional openings. The methods are dense and necessary. The discussion focuses on interpretation, not repetition.

## Repetition / circularity audit
| Idea | Mentioned in chapters | Different angles? |
|------|----------------------|-------------------|
| Need for temporal dynamics in AL | 1.1, 4.1 | Yes: lit review → results interpretation |
| σ_calib robustness | Abstract, 3.1, 4.3 | Consistent, no redundancy |
| Antagonistic-channel result | 2.4, 3.1, 4.2 | Each section adds new information (prediction, finding, explanation) |
| Behavioral target utility | 2.5, 3.1, 4.3 | Yes: design → result → implication |

No problematic repetition.

## Checklist (12 items ✓/✗)
1. Operationalised falsifiable hypothesis ✓
2. IMRaD structure ✓
3. Statistical methods appropriate (full sub-audit pass) ✗ (multiple comparisons not adjusted; pre-registered decision but still a weakness)
4. Limitations explicit ✓
5. Conflict of interest declared FULLY ✓
6. Reference reality + tier ≥3 average ✓
7. No fabrication markers / data integrity ✓
8. Internal consistency ✓
9. Evidence base + meta-analysis context ✓
10. Methodology depth (replication-ready) ✓
11. Data/code availability ✓
12. Author contributions (CRediT) ✓

## Blocking issues
None.

## Fixable issues (max 3)
1. Minor: Add a sentence in Methods justifying the decision to not adjust for multiple comparisons (e.g., exploratory nature, Rothman rationale).
2. Ensure the future citations (Harb, Madaria) are verifiable; if not yet published, consider a note.

---

# Review C: RED TEAM — Ze-AL-v4-manuscript-v8-OSF-archived

## Verdict
**REVISE_MAJOR**

## Scores (1-5)
- HypothesisClarity: 5
- IMRaDCompliance: 5
- StatisticalRigor: 3
- DataIntegrity: 4
- RefQualityTier: 4
- FactualAccuracy: 4
- SourceIntegrity: 4
- Reproducibility: 5
- AbstractMatch: 5
- DiscussionGrounded: 4
- COI_Honesty: 5

## Counter-argument audit
| Author's claim | Strongest counter-argument | Engaged in book? | Quality of engagement |
|----------------|----------------------------|------------------|-----------------------|
| σ_calib is most robust under calibration contamination | Real-world contamination may differ (e.g., slow drift, non-random transients) | Partially: limitations mention impulsive Gaussian stressors only | Moderate – acknowledge but don't test alternatives |
| Mahalanobis distance robust to antagonistic coupling | Real physiology may have time-delayed or frequency-specific antagonism | Not addressed | Weak – assumes static coupling pattern |
| GP-based methods outperform traditional AL indices | Traditional AL uses multi-domain biomarkers (neuroendocrine, metabolic, inflammatory) – not comparable to 5-channel accelerometry | Not addressed | Weak – no head-to-head comparison |
| Behavioral target with ceiling 0.30 validates signal extraction | The 0.30 ceiling is arbitrary; real outcomes may have higher or lower ceiling | Not discussed | Weak – no justification for chosen ceiling |
| Pre-registration ensures integrity | Single seed with deterministic code; results may not generalize to other random seeds | Not addressed | Weak – no multi-seed sensitivity analysis |

## Bias audit
| Type | Severity | Disclosed? |
|------|----------|------------|
| Selection (simulation parameters) | Moderate – parameters may favor GP methods (e.g., kernel, contamination pattern) | Partially – pre-registered but not justified from literature |
| Confirmation (author = theory inventor) | Moderate – developer of Ze-AL | Yes, with mitigation |
| Survivor (only successful tests reported) | Low – contamination tests show failure of others | N/A |

## Checklist (12 items ✓/✗)
1. Operationalised falsifiable hypothesis ✓
2. IMRaD structure ✓
3. Statistical methods appropriate (full sub-audit pass) ✗ (no multiple comparison correction; single seed)
4. Limitations explicit ✓
5. Conflict of interest declared FULLY ✓
6. Reference reality + tier ≥3 average ✓
7. No fabrication markers / data integrity ✓
8. Internal consistency ✓
9. Evidence base + meta-analysis context ✓ (but could strengthen with comparison to established AL indices)
10. Methodology depth (replication-ready) ✓
11. Data/code availability ✓
12. Author contributions (CRediT) ✓

## Blocking issues
- Lack of comparison with any established multi-domain allostatic load index (e.g., quartile sum, clinical cut-offs) in a realistic simulation or empirical dataset.
- Single-seed simulation may not be generalizable; results could vary with different seeds.

## Fixable issues (max 3)
1. Add a simulation with alternative contamination patterns (sustained shifts, slow drifts) and multi-seed (≥10 seeds) sensitivity analysis.
2. Include a comparison with a standard AL index from biomarker literature (e.g., using the same five channels but with quartile-based sum) on the same simulated data.
3. Strengthen discussion by engaging with alternative theoretical frameworks (e.g., reactivity vs. recovery models) and justifying the chosen ceiling for the behavioral target.

---

## AGGREGATION

# TBPR-article Combined Verdict — Ze-AL-v4-manuscript-v8-OSF-archived

## Per-reviewer breakdown
- A (PARANOID): **REVISE_MINOR** (score sum 51/55) — top concern: verification of future citations (Harb, Madaria)
- B (CYNIC): **ACCEPT** (score sum 51/55) — top concern: multiple comparison adjustment justification
- C (RED TEAM): **REVISE_MAJOR** (score sum 48/55) — top concern: lack of engagement with counter-arguments and comparison with established AL indices

## Combined verdict (worst of 3)
**REVISE_MAJOR**

## Combined score
score = MIN(51, 51, 48) = 48/55

## Editorial recommendation
- Suggested publisher tier: tier-2 academic (Routledge/Springer) or top specialty journal (e.g., npj Digital Medicine, Psychoneuroendocrinology) after major revisions
- Estimated time-to-publication: 6–9 months with 1–2 major revision cycles

## Top 3 actions for author
1. **Address counter-arguments and broaden evidence base**: Compare GP-based methods against a traditional multi-domain AL index (e.g., quartile sum over equivalent channels) and test alternative contamination scenarios (slow drift, non-random transients); add multi-seed sensitivity analysis (≥10 seeds).
2. **Improve statistical rigor**: Either apply a multiple-comparison correction (e.g., FDR) or provide a strong justification for no adjustment in the context of 144 tests; consider reporting effect-size confidence intervals with adjusted significance thresholds.
3. **Verify and clarify references**: Confirm that Harb et al. (2026) and Madaria et al. (2025) are accepted/published, or cite as preprints/in press; if not yet available, replace with verifiable sources or note the status explicitly.