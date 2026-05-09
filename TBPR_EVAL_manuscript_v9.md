# Review A: PARANOID — Ze-AL-v4-manuscript-v9-overnight

## Article-type
research — Original research, methodological simulation study with pre-registration

## Verdict
**REVISE_MINOR**

## Scores (1-5)
- HypothesisClarity: 5
- IMRaDCompliance: 5
- StatisticalRigor: 4
- DataIntegrity: 5
- RefQualityTier: 4
- FactualAccuracy: 3
- SourceIntegrity: 3
- Reproducibility: 5
- AbstractMatch: 5
- DiscussionGrounded: 4
- COI_Honesty: 5

## Fact-check audit
| # | Claim/Quote/Number | Type | Verifiable? | Correct? | Action |
|---|-------------------|------|-------------|----------|--------|
| 1 | Harb et al. (2025) I² = 94.24% | Meta-analysis statistic | Text says 2025, reference says 2026 | Inconsistent year | Flag for correction |
| 2 | PMID: 41370963 for Harb | Reference identifier | Valid PubMed ID? Not checked; plausible range | Unknown | Mark as unverified; suggest author verify |
| 3 | Madaria et al. (2025) g = 1.33 | Effect size | Reference checks out; no year conflict | Yes | Accept |
| 4 | Pre-registration seed = 20260509 | Code/Simulation | Deterministic; OSF DOI provided | Yes | Accept |
| 5 | Rothman 1990: no multiple comparisons adjustment | Citation | Author and year match known paper | Yes | Accept |
| 6 | Sample size n=200, power >0.99 for r≥0.30 | Statistical claim | Fisher z-transform calculation correct | Yes | Accept |
| 7 | 24-hour moving average baseline | Method description | Clear and plausible | Yes | Accept |
| 8 | Antagonistic channels: strict alternation [+1,-1,...] | Parameter | Defined explicitly | Yes | Accept |
| 9 | Behavioral target ceiling r=0.30 | Theoretical bound | Correct by construction | Yes | Accept |
| 10 | Multi-seed sensitivity: SD=0.000 under contamination | Result | Deterministic given seed? Suspect truncation; SD cannot be exactly zero unless identical values | Suspicious | Flag: explain zero variability across seeds under contamination |

## Statistical sub-audit (v2.0)
| Test/method | Appropriate? | Multiple-comp? | Power | Effect size | Pre-registered? | Score |
|-------------|-------------|----------------|-------|-------------|-----------------|-------|
| Pearson correlation across n=200 subjects | Yes | No correction (Rothman 1990) – defensible but suboptimal | Pre-registered power >0.99 for r≥0.30 | CI 95% reported via bootstrap | Yes | 4/5 (deduction for no multiple comparison correction in exploratory 144 tests) |
| Bootstrap CI (10k resamples, bias-corrected percentile) | Appropriate | N/A | N/A | Included | Yes | 5/5 |
| Multi-seed sensitivity | Exploratory, no formal inference | N/A | N/A | Mean±SD range | Post-hoc | 3/5 (exploratory, but done appropriately) |

## Reference tier audit (v2.0)
| # | Citation | Tier (1-5) | Justification |
|---|----------|------------|---------------|
| 1 | Tkemaladze (2026) OSF | 3 | Pre-registration – not peer-reviewed but verifiable |
| 2 | Sterling & Eyer (1988) book chapter | 3 | Classic, but book chapter |
| 3 | McEwen (1998) NEJM | 1 | Top journal |
| 4 | Seeman et al. (2001) PNAS | 1 | Top journal |
| 5 | Karlamangla et al. (2006) Psychosom Med | 2 | Specialty journal |
| 6 | Gillespie et al. (2019) Psychoneuroendocrinology | 2 | Specialty journal |
| 7 | Karlamangla et al. (2014) Neurobiol Aging | 3 | Solid specialty |
| 8 | Zannas et al. (2017) Neuroscience | 3 | Solid specialty |
| 9 | Harb et al. (2026) Psychoneuroendocrinology | 2 | Specialty, but year mismatch in text vs ref |
| 10 | Madaria et al. (2025) Front Psychiatry | 3 | Solid specialty |
| 11 | Kezios et al. (2022) Am J Epidemiol | 1 | Top epidemiology journal |
| 12 | Friston (2010) Nat Rev Neurosci | 1 | Top review journal |
| 13 | Clark (2013) Behav Brain Sci | 1 | High-impact |
| 14 | Barrett & Simmons (2015) Nat Rev Neurosci | 1 | Top review |
| 15 | Tschantz et al. (2022) Neural Comput | 2 | Specialty |
| 16 | Matthews et al. (2017) JMLR | 1 | Top ML journal |
| 17 | Rothman (1990) Epidemiology | 2 | Specialty |
| 18 | Ledoit & Wolf (2004) J Multivariate Anal | 2 | Specialty |

Average tier: ~1.9 → RefQualityTier = 4/5 (since Tier1=5, but average tier 1.9 corresponds to score ~4)

## Plagiarism / attribution audit
| # | Suspicious passage | Possible source | Action |
|---|------------------|-----------------|--------|
| 1 | "stability through change" – Sterling & Eyer (1988) | Direct quote, attributed | Accept |
| 2 | Definition of allostatic load – McEwen (1998) | Standard definition, paraphrased | Accept |
| 3 | Free-energy principle description – Friston 2010 | Standard summary, cited | Accept |
No evidence of plagiarism.

## Conflict-of-Interest audit (v2.0 — expanded)
| Type | Detected? | Severity | Disclosed in paper? |
|---|---|---|---|
| Financial (industry funding, stock, patents) | None declared | None | Yes – "no financial competing interests" |
| Ideological (author = theory inventor) | Yes – T.T. is developer of Ze-AL | Medium – mitigated by pre-registration and public code | Yes – stated in Competing Interests and Methods |
| Career (dependency on outcome / promotion / funding) | Likely – single author, no external team | Low-Medium | Not explicitly stated, but pre-registration mitigates |

## Checklist (12 items ✓/✗)
1. Operationalised falsifiable hypothesis ✓
2. IMRaD structure (or appropriate for article-type) ✓
3. Statistical methods appropriate (full sub-audit pass) ✓ (mild concern about multiple comparisons)
4. Limitations explicit ✓
5. **Conflict of interest declared FULLY (financial + ideological + career)** ✓
6. Reference reality + tier ≥3 average ✓ (average tier ~2, but high proportion Tier1/2; Tier≥3 satisfied)
7. No fabrication markers / data integrity ✓
8. Internal consistency (Abstract = Results = Discussion) ✓
9. Evidence base + meta-analysis context ✓ (cites meta-analyses)
10. Methodology depth (replication-ready) ✓ (code provided, deterministic seed)
11. Data/code availability ✓
12. Author contributions (CRediT) ✓

## Blocking issues (factual integrity / plagiarism — text-revision won't fix)
None.

## Fixable issues (max 3)
1. Correct year discrepancy for Harb et al. (text says 2025, reference says 2026) – verify actual publication year.
2. Clarify why multi-seed contamination results show SD=0.000; either explain deterministic contamination or note rounding/truncation.
3. Add multiple-comparison correction (FDR) for the 144 correlations, or justify more strongly the no-correction choice beyond Rothman citation.

---

# Review B: CYNIC — Ze-AL-v4-manuscript-v9-overnight

## Article-type
research — original research, simulation

## Verdict
**ACCEPT**

## Scores (1-5)
- HypothesisClarity: 5
- IMRaDCompliance: 5
- StatisticalRigor: 5
- DataIntegrity: 5
- RefQualityTier: 5
- FactualAccuracy: 5
- SourceIntegrity: 5
- Reproducibility: 5
- AbstractMatch: 5
- DiscussionGrounded: 5
- COI_Honesty: 5

## Fluff & Padding audit
| Section/Chapter | Real content (Y/N) | Specific to book's thesis (Y/N) | Generic/cliché | Score |
|-----------------|--------------------|--------------------------------|----------------|-------|
| Introduction 1.1 | Y – describes AL heterogeneity problem | Y – directly motivates the work | N – citations support | 5 |
| Introduction 1.2 | Y – predictive coding link | Y – central to method | N | 5 |
| Methods 2.1-2.8 | Y – detailed generative model | Y – all specific | N | 5 |
| Results 3.1-3.2 | Y – tables, clear text | Y | N | 5 |
| Discussion 4.1-4.5 | Y – interpretation, limitations | Y | N – measured tone, no hype | 5 |
| Independent Behavioral Target subsection | Y – novel control condition | Y | N – well-explained | 5 |

## Repetition / circularity audit
| Idea | Mentioned in chapters | Different angles? |
|------|----------------------|-------------------|
| σ_calib robustness | Abstract, Results, Discussion | Yes – each section adds nuance (contamination levels, comparison with Mahalanobis) |
| Antagonistic channel robustness | Methods, Results, Discussion | Yes – explanation of why it works |
| Behavioral target ceiling | Abstract, Methods, Results, Discussion | Yes – consistent but not redundant |
| Need for real-world validation | Discussion, Conclusion | Acceptable – not excessive |

## Checklist (12 items ✓/✗)
1. Operationalised falsifiable hypothesis ✓
2. IMRaD structure (or appropriate for article-type) ✓
3. Statistical methods appropriate (full sub-audit pass) ✓
4. Limitations explicit ✓
5. **Conflict of interest declared FULLY (financial + ideological + career)** ✓
6. Reference reality + tier ≥3 average ✓
7. No fabrication markers / data integrity ✓
8. Internal consistency (Abstract = Results = Discussion) ✓
9. Evidence base + meta-analysis context ✓
10. Methodology depth (replication-ready) ✓
11. Data/code availability ✓
12. Author contributions (CRediT) ✓

## Blocking issues
None.

## Fixable issues (max 3)
None. The manuscript is dense, well-structured, and every paragraph serves a purpose. The author avoids clichés, self-help platitudes, and generic case studies. The behavioral target section is novel and not padded. Accept as is.

---

# Review C: RED TEAM — Ze-AL-v4-manuscript-v9-overnight

## Article-type
research — original research, simulation

## Verdict
**REVISE_MINOR**

## Scores (1-5)
- HypothesisClarity: 5
- IMRaDCompliance: 5
- StatisticalRigor: 4
- DataIntegrity: 4
- RefQualityTier: 4
- FactualAccuracy: 4
- SourceIntegrity: 4
- Reproducibility: 5
- AbstractMatch: 5
- DiscussionGrounded: 3
- COI_Honesty: 4

## Counter-argument audit
| Author's claim | Strongest counter-argument | Engaged in book? | Quality of engagement |
|----------------|---------------------------|------------------|-----------------------|
| σ_calib is most robust under contamination | What about 50%+ contamination? Simulation only tested 10% and 30%. Could break beyond that. | Not addressed – no extrapolation or higher contamination tested | Weak – should discuss boundary |
| GP-based methods equivalent under clean calibration | That equivalence might mask different sensitivity to model misspecification (e.g., kernel choice, non-stationarity). | Partially – tested lengthscale misspecification, but not other kernel parameters | Moderate – could add discussion |
| Antagonistic channels do not degrade Mahalanobis | Real physiology may have non-stationary coupling (time-varying). Alternating is one extreme; what about correlated noise with opposite stress responses? | Not addressed – assumes coupling fixed during baseline | Weak – add caveat |
| Behavioral target is "truly independent" | It is not independent of the stressor; it is independent of the channel features but shares variance with burden. The term "independent" could mislead readers. | Notes "partly determined" but title says "truly independent" | Moderate – rephrase for accuracy |
| Moving-average baseline should be avoided | In some real datasets, a moving average might be the only feasible baseline (e.g., no clean calibration period). The simulation assumes a clean baseline exists for GP methods. | Not discussed – assumes baseline availability | Weak – add practical advice for cases without calibration |

## Bias audit
| Type (selection / confirmation / survivor / financial / ideological) | Severity | Disclosed? |
|----------------------------------------------------------------------|----------|------------|
| Confirmation bias – simulation designed to favour GP methods | Medium – the generative model uses smooth Gaussian processes which match GP assumptions. Alternative models (e.g., abrupt stressor onsets, non-stationary noise) not tested. | Partial – acknowledged that synthetic data may not capture full complexity |
| Financial / ideological – author is developer | Low-Medium – mitigated by pre-registration and public code, but single-author paper may still be perceived as promotional | Yes – stated |
| Outcome reporting bias – only 144 of possibly many correlations reported | Low – pre-registered all comparisons; no hidden outcomes | Yes – pre-registered |

## Checklist (12 items ✓/✗)
1. Operationalised falsifiable hypothesis ✓
2. IMRaD structure (or appropriate for article-type) ✓
3. Statistical methods appropriate (full sub-audit pass) ✓
4. Limitations explicit ✓
5. **Conflict of interest declared FULLY (financial + ideological + career)** ✓
6. Reference reality + tier ≥3 average ✓
7. No fabrication markers / data integrity ✓
8. Internal consistency (Abstract = Results = Discussion) ✓
9. Evidence base + meta-analysis context ✓
10. Methodology depth (replication-ready) ✓
11. Data/code availability ✓
12. Author contributions (CRediT) ✓

## Blocking issues
None.

## Fixable issues (max 3)
1. Address the boundary of σ_calib robustness: add discussion of what contamination levels might break the method (e.g., >50%) or test an additional condition.
2. Rephrase "truly independent behavioral target" to avoid overclaim – e.g., "behavioral target with known theoretical upper bound independent of the physiological measures".
3. Add a paragraph acknowledging that real-world settings may lack a clean calibration period, and discuss whether moving-window GP or other adaptive baselines could be alternatives.

---

## TBPR-article Combined Verdict — Ze-AL-v4-manuscript-v9-overnight

## Per-reviewer breakdown
- A (PARANOID): **REVISE_MINOR** (score sum 48/55) — top concern: citation year inconsistency and unverified SD=0.000 flag
- B (CYNIC): **ACCEPT** (score sum 55/55) — top concern: none; manuscript is dense and fluff-free
- C (RED TEAM): **REVISE_MINOR** (score sum 47/55) — top concern: missing boundary testing for contamination, overclaim on "truly independent" label, insufficient engagement with counter-arguments

## Combined verdict (worst of 3)
**REVISE_MINOR**

## Combined score
score = MIN(48, 55, 47) = 47/55

## Editorial recommendation
- Suggested publisher tier: tier-1 academic (e.g., eLife, PLOS Computational Biology, npj Digital Medicine) – manuscript is methodologically rigorous and well-documented.
- Estimated time-to-publication: 3–6 months with one minor revision round.

## Top 3 actions for author
1. **Fix citation year** for Harb et al. (text vs reference) and clarify whether the SD=0.000 in multi-seed analysis is real or a rounding artefact.
2. **Add discussion** on the limits of σ_calib robustness (e.g., higher contamination levels, non-stationary baselines) and rephrase "truly independent behavioral target" to reduce hype.
3. **Address counter-arguments** regarding real-world baseline availability and the generalizability of the GP assumptions to abrupt or non-stationary stress profiles.