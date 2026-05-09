# TBPR-article Triple-Blind Review — Ze-AL-v4-manuscript-v4

---

# Review A: PARANOID — Ze-AL-v4-manuscript-v4

## Article-type
research (Original Research – Methodological Positive Finding)

## Verdict
**REVISE_MAJOR**

## Scores (1-5)
- HypothesisClarity: 4
- IMRaDCompliance: 5
- StatisticalRigor: 3
- DataIntegrity: 3
- RefQualityTier: 4
- FactualAccuracy: 3
- SourceIntegrity: 3
- Reproducibility: 4
- AbstractMatch: 5
- DiscussionGrounded: 4
- COI_Honesty: 4

## Fact-check audit
| # | Claim/Quote/Number | Type | Verifiable? | Correct? | Action |
|---|---|---|---|---|---|
| 1 | Pre-registration timestamp 2026-05-09 05:36:12.124395685 +0400 | Data | Partially | ? | Microsecond precision is unusual and could be fabricated. Must justify or remove. |
| 2 | Final results written at 2026-05-09 07:13:11.815934204 +0400 | Data | Partially | ? | Same concern. |
| 3 | Reference 15: Tkemaladze T. Ze-AL v3 … OSF 2024. doi:10.31219/osf.io/abcde [placeholder] | Source | No | ? | Placeholder not verifiable. Must replace with actual DOI. |
| 4 | Harb et al. 2025, I² = 94.24% | Stat | Yes | Likely correct | Check original source for precision. |
| 5 | “v3 σ_E does **not** exhibit cancellation” | Claim | Yes | Consistent with their simulation | Accept. |
| 6 | “The 5‑channel data were then transformed to simulate realistic ranges and noise” | Method | Partially | No detail given | Needs explicit transformation formula. |
| 7 | “r_burden = 0.893 [0.872–0.911]” under 10% contamination | Numeric | Yes | Matches Table 3 | OK. |
| 8 | “MA‑residual reversed sign (r_burden −0.842)” | Numeric | Yes | Matches Table 3 | OK. |
| 9 | “v4 VFE numerically coincides with Mahalanobis” | Claim | Partially | Plausible but not proven | Add theoretical justification or citation. |
| 10 | Karlamangla composite and Cohen dysregulation index not implemented | Claim | Yes | True | Not an error, but the section is incomplete. |

## Statistical sub-audit (v2.0)
| Test/method | Appropriate? | Multiple-comp? | Power | Effect size | Pre-registered? | Score |
|---|---|---|---|---|---|---|
| Pearson correlation + bootstrap | Yes | No correction (Rothman) | Not reported | CI provided | Yes | 3/5 |
| Generative model specification | Adequate | N/A | N/A | N/A | Yes | — |
| Outlier handling | Not specified | N/A | N/A | N/A | No | 0 |

Sub-audit aggregate: 5/8 (missing multiple-comparison correction, power analysis, outlier handling rule). StatisticalRigor reduced accordingly.

## Reference tier audit (v2.0)
| # | Citation | Tier (1-5) | Justification |
|---|---|---|---|---|
| 1 | Sterling & Eyer 1988 (book chapter) | 3 | Non‑journal source |
| 2 | McEwen 1998 *NEJM* | 1 | |
| 3 | Seeman 2001 *PNAS* | 1 | |
| 4 | Karlamangla 2006 *Psychosom Med* | 2 | |
| 5 | Gillespie 2019 *Psychoneuroendocrinology* | 2 | |
| 6 | Karlamangla 2014 *Neurobiol Aging* | 2 | |
| 7 | Zannas 2017 *Neuroscience* | 2 | |
| 8 | Harb 2025 *Psychoneuroendocrinology* | 2 | |
| 9 | Madaria 2025 *Front Psychiatry* | 2 | |
| 10 | Kezios 2022 *Am J Epidemiol* | 1 | |
| 11 | Friston 2010 *Nat Rev Neurosci* | 1 | |
| 12 | Clark 2013 *Behav Brain Sci* | 1 | |
| 13 | Barrett 2015 *Nat Rev Neurosci* | 1 | |
| 14 | Tschantz 2022 *Neural Comput* | 2 | |
| 15 | Tkemaladze 2024 OSF preprint | 4 | Placeholder, unverifiable |
| 16 | Matthews 2017 *JMLR* | 2 | |
| 17 | Rothman 1990 *Epidemiology* | 1 | |
| 18 | Ledoit & Wolf 2004 *J Multivariate Anal* | 2 | |

Average tier ~1.9 → RefQualityTier = 4.

## Plagiarism / attribution audit
No suspicious passages detected.

## Conflict-of-Interest audit (v2.0 — expanded)
| Type | Detected? | Severity | Disclosed in paper? |
|---|---|---|---|
| Financial (industry funding, stock, patents) | No | — | Declared none |
| Ideological (author = theory inventor) | Yes (T.T. is proponent of predictive‑coding AL) | Moderate | Disclosed in Competing Interests |
| Career (dependency on outcome) | Possible positive result benefits author’s reputation | Mild | Not explicitly disclosed |

## Checklist (12 items ✓/✗)
1. Operationalised falsifiable hypothesis ✓  
2. IMRaD structure ✓  
3. Statistical methods appropriate (full sub-audit pass) ✗  
4. Limitations explicit ✓  
5. **Conflict of interest declared FULLY (financial + ideological + career)** ✓ (ideological declared, financial none)  
6. Reference reality + tier ≥3 average ✓ (average tier 1.9 → score 4, acceptable)  
7. No fabrication markers / data integrity ✗ (suspicious timestamps, placeholder ref)  
8. Internal consistency (Abstract = Results = Discussion) ✓  
9. Evidence base + meta-analysis context ✓  
10. Methodology depth (replication-ready) ✓  
11. Data/code availability ✓  
12. Author contributions (CRediT) ✗ (not completed)

## Blocking issues (factual integrity / plagiarism — text-revision won't fix)
- Placeholder reference 15 must be replaced with a real DOI or removed.
- The microsecond‑precision timestamps for pre‑registration and results execution raise suspicion of fabrication; must be justified or corrected to reasonable precision.

## Fixable issues (max 3)
1. Replace reference 15 with actual preprint DOI.  
2. Remove or justify the microsecond timestamps (e.g., state that file system timestamps are recorded exactly).  
3. Add power analysis and outlier handling rule to Methods; consider Bonferroni correction for multiple sensitivity conditions or justify Rothman's approach in Methods.

---

# Review B: CYNIC — Ze-AL-v4-manuscript-v4

## Article-type
research

## Verdict
**REVISE_MINOR**

## Scores (1-5)
- HypothesisClarity: 4
- IMRaDCompliance: 5
- StatisticalRigor: 3 (same deficits as others, but not fluff)
- DataIntegrity: 3
- RefQualityTier: 4
- FactualAccuracy: 4
- SourceIntegrity: 4
- Reproducibility: 4
- AbstractMatch: 5
- DiscussionGrounded: 4
- COI_Honesty: 4

## Fluff & Padding audit
| Section/Chapter | Real content (Y/N) | Specific to book's thesis (Y/N) | Generic/cliché | Score |
|---|---|---|---|---|
| Abstract | Y | Y | N | 5 |
| Introduction | Y | Y | N (background necessary) | 4 |
| Methods | Y | Y | N | 5 |
| Results | Y | Y | N | 5 |
| Discussion | Y | Y | N (slight repetition of main finding) | 4 |
| "External comparators" subsection | Partially | N (admits not implemented) | Slightly generic | 3 |
| Limitations | Y | Y | N | 5 |

Overall density high; minimal fluff. The "External comparators" section is unnecessary and reads as padding. Could be moved to a brief note in Limitations.

## Repetition / circularity audit
| Idea | Mentioned in chapters | Different angles? |
|---|---|---|
| σ_calib robust under contamination | Abstract, Results (Tables 1–3), Discussion, Conclusions | Yes, each with different context (clean, misspecification, contamination) – acceptable. |
| Limitations of traditional AL | Introduction, Discussion | Overlaps; still not excessive. |

No circular reasoning; all claims are supported by data.

## Checklist (12 items ✓/✗)
1. Clear central thesis ✓  
2. Target audience defined ✓ (implicit: allostatic load researchers; could be explicit)  
3. Logical structure ✓  
4. Evidence quality ✓  
5. Originality ✓  
6. Writing quality ✓  
7. Reference reality + accuracy ✓ (except placeholder ref)  
8. No plagiarism / proper attribution ✓  
9. Internal consistency ✓  
10. Depth of treatment ✓  
11. Memorability / pedagogical value ✓  
12. Honesty about limitations ✓  

Total: 12/12 (with minor reservation on #2).

## Blocking issues
None.

## Fixable issues (max 3)
1. Move or condense the "External comparators" paragraph into the Limitations section.  
2. Complete the placeholder reference and author contributions.  
3. Optionally add a sentence explicitly defining the target audience at the end of the Introduction.

---

# Review C: RED TEAM — Ze-AL-v4-manuscript-v4

## Article-type
research

## Verdict
**REVISE_MAJOR**

## Scores (1-5)
- HypothesisClarity: 4
- IMRaDCompliance: 5
- StatisticalRigor: 3
- DataIntegrity: 3
- RefQualityTier: 4
- FactualAccuracy: 3
- SourceIntegrity: 3
- Reproducibility: 4
- AbstractMatch: 5
- DiscussionGrounded: 3
- COI_Honesty: 4

## Counter-argument audit
| Author's claim | Strongest counter-argument | Engaged in book? | Quality of engagement |
|---|---|---|---|
| σ_calib robust under calibration contamination | Real stress responses include antagonistic channels (HRV decrease, cortisol increase) that break the additive, coherent sign assumption. | Only mentioned as limitation; no test. | Poor — claim would be stronger if tested. |
| v4 σ_calib recommended as primary deployable measure | Other dynamic methods (DSEM, time-varying VAR) may be equally robust; not compared. | Not addressed. | Weak. |
| Independent outcome surrogate is independent | Outcome is a function of the same burden that drives prediction errors; not truly independent. | No discussion of this circularity. | Missing. |
| v4 σ_calib outperforms v3 | Under clean calibration, v3 performs equally (r=0.949); in some misspecifications, v3 is similar. The advantage is only under contamination. | Acknowledged but not explored in depth. | Adequate. |
| Pre-registration ensures integrity | The microsecond timestamps are suspicious and could be fabricated; a simple commit hash suffices. | No response. | Not engaged. |

## Bias audit
| Type (selection / confirmation / survivor / financial / ideological) | Severity | Disclosed? |
|---|---|---|
| **Confirmation bias**: Author is proponent of predictive‑coding AL; results mainly support their own previous measure (v4) over v3. | Moderate | Disclosed (ideological COI). |
| **Selection bias**: Only 7 sensitivity conditions chosen; no test of antagonistic channels or different stressor coupling. | Moderate | Not disclosed as bias, but limitations noted. |
| **Survivor bias**: Successful simulation presented; real‑world failure modes (missing data, device dropout) not considered. | Mild | Not addressed. |
| **Stakeholder bias**: Manuscript targets wearable/stress researchers who would benefit from a simple robust metric. | Mild | Not disclosed. |

## Checklist (12 items ✓/✗)
1. Clear central thesis ✓  
2. Target audience defined ✗ (not explicitly stated; assumed but not precise)  
3. Logical structure ✓  
4. Evidence quality ✓  
5. Originality ✓  
6. Writing quality ✓  
7. Reference reality + accuracy ✗ (placeholder ref)  
8. No plagiarism ✓  
9. Internal consistency ✓  
10. Depth of treatment ✓  
11. Memorability / pedagogical value ✓  
12. Honesty about limitations ✓  

Total: 10/12 (items 2 and 7 fail).

## Blocking issues
- Failure to engage seriously with the strongest counter‑argument (antagonistic channels) undermines the generality of the claim.  
- The "independent outcome" is not independent of the burden; this circularity is not addressed.

## Fixable issues (max 3)
1. Add a sensitivity analysis with at least one antagonistic‑coupling stressor scenario (e.g., HR decreases while cortisol increases) to test robustness.  
2. Acknowledge the circularity of the outcome variable and discuss how it may inflate correlations; consider an additional outcome that is truly independent (e.g., a separate behavioral measure).  
3. Replace the suspicious microsecond timestamps with a standard approach (e.g., OSF timestamp + commit hash) to avoid any credibility concerns.

---

# TBPR-article Combined Verdict — Ze-AL-v4-manuscript-v4

## Per-reviewer breakdown
- A (PARANOID): **REVISE_MAJOR** (score sum 42/55) — top concern: fabrication markers in timestamps and placeholder reference  
- B (CYNIC): **REVISE_MINOR** (score sum 44/55) — top concern: minor padding in External comparators section  
- C (RED TEAM): **REVISE_MAJOR** (score sum 41/55) — top concern: insufficient engagement with counter-arguments (antagonistic channels, independent outcome circularity)

## Combined verdict (worst of 3)
**REVISE_MAJOR**

## Combined score
score = MIN(42, 44, 41) = **41/55**

## Editorial recommendation
- **Suggested publisher tier**: tier-2 academic (e.g., *Scientific Reports*, *PLOS ONE*, or *Psychoneuroendocrinology*) after major revisions; if the counter‑argument tests and data integrity issues are resolved, could target *npj Digital Medicine* or *eLife*.  
- **Estimated time-to-publication**: 9–12 months (including 6 months for revisions and re‑review).

## Top 3 actions for author
1. **Address data integrity concerns**: Remove or justify the microsecond timestamps; replace the placeholder reference with a real DOI; complete author contributions and code release.  
2. **Test the strongest counter‑argument**: Add a simulation condition with antagonistic physiological channels (e.g., HR decreasing while cortisol increasing) to demonstrate that σ_calib remains robust, or at least characterise its limitations.  
3. **Strengthen outcome independence**: Either use a truly independent outcome (e.g., a behavioral or self‑report measure not derived from the burden) or explicitly discuss the circularity and its potential impact on the reported correlations.

**Full data and code should be made available to reviewers upon request.**