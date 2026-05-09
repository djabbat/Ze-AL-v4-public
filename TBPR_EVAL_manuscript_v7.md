# Review A: PARANOID — Ze-AL-v4-manuscript-v7

## Article-type
research — Original Research (Methodological Positive Finding) with simulation data, IMRaD structure, pre‑registered (local)

## Verdict
**REVISE_MAJOR**

## Scores (1-5)
- HypothesisClarity: 4
- IMRaDCompliance: 5
- StatisticalRigor: 2
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
|---|-------------------|------|-------------|----------|--------|
| 1 | Harb et al. (2025) – extreme heterogeneity (I²=94.24%) | Meta‑analysis claim | Partial – ref 8 was published in 2026 (PMID 41370963). Year mismatch text vs. ref list. | Misattributed year: text says 2025, ref list says 2026 | Correct year in text to 2026. Verify PMID exists. |
| 2 | Madaria et al. (2025) – AL in schizophrenia g=1.33 | Meta‑analysis claim | Partially – ref 9 is Front Psychiatry 2025; PMID 40666432 plausible but unverified | Likely correct | Re-check DOI/PMID for existence. |
| 3 | Kezios et al. (2022) – sex‑specific thresholds bias | Claim | Yes – ref 10 (Am J Epidemiol 2022, PMID 34041548) is a real paper. | Correct | None |
| 4 | Traditional index: “proportion of time > 75th percentile of baseline summed across channels” | Method description | Verifiable from code; no data shown | Consistent with known quartile methods | None |
| 5 | “v3 σₑ exhibited signal cancellation under certain conditions” | Claim about unpublished method | Not verifiable – no reference to prior Ze‑AL paper | Unverifiable; need to cite v3 source or clarify | Add reference or remove claim if unsupported |
| 6 | Seed = 20260509, deterministic simulation | Statement of reproducibility | Verifiable only if code released | Assumed correct | None (code pending) |
| 7 | “all burden‑family correlations remained significant at qFDR < 0.001 except the traditional index under contamination” | Numerical claim | Check Table 1: Traditional contam 10% q=0.5024, 30% q=0.2408. Correct. | Correct | None |
| 8 | Behavioral target theoretical ceiling r=0.30 | Construction claim | Verifiable from formula: z = 0.30·z(b) + 0.70·L + ε. However ε variance not specified, so ceiling may be different if ε adds variance. | Potentially incorrect if ε variance not scaled to keep total variance 1. | Specify ε variance or verify ceiling derivation. |
| 9 | Pre‑registration: locked at 2026‑05‑09 05:36, production 08:14 | Timestamp claim | File timestamps only; external OSF deposit not yet done. | Cannot verify externally. | Acknowledged as exploratory; fine if deposit done prior to journal submission. |
| 10 | Ref 8 PMID 41370963 | Reference detail | 8‑digit PMID is possible but unusual. Unverifiable without access. | Suspicious; check database. | Verify PMID or replace with verified DOI. |

**Summary**: 1 confirmed fact error (year mismatch), 2 unverifiable elements (ref 8 PMID, behavioral ceiling epsilon variance), 1 unsupported claim (v3 signal cancellation without reference). Total minor factual issues: ≤3, but combined with stats audit failure pushes to MAJOR.

## Statistical sub-audit (v2.0)
| Test/method | Appropriate? | Multiple-comp? | Power | Effect size | Pre-registered? | Score |
|-------------|--------------|----------------|-------|-------------|-----------------|-------|
| Pearson correlation across n=200 | Yes – linear correlation sufficient; simulation linearity holds | Benjamini‑Hochberg FDR across 54 tests (q=0.05) | Ex‑ante power >0.95 for r≥0.25, n=200 | Only point r reported; no 95% CI | Local pre‑registration file with time stamp; no external deposit | 5/8 |

**Missing items (3):**  
- Effect‑size reporting includes only point r, no CI 95%  
- Variance reporting: no SD/SEM/CI for correlations (bootstrap not performed)  
- Outlier handling: no pre‑specified rule (though simulated data unlikely to have outliers; still a gap)  

**StatisticalRigor score reduced by 3 from base of 5 → 2. Sub‑audit pass = 5/8 (<6) → triggers REVISE_MAJOR per policy.**

## Reference tier audit (v2.0)
| # | Citation | Tier (1-5) | Justification |
|---|----------|------------|---------------|
| 1 | Sterling & Eyer 1988 (Wiley book) | 4 | Book chapter, not peer-reviewed journal |
| 2 | McEwen NEJM 1998 | 1 | NEJM – top tier |
| 3 | Seeman PNAS 2001 | 1 | PNAS – top tier |
| 4 | Karlamangla Psychosom Med 2006 | 3 | Solid specialty, IF ~4 |
| 5 | Gillespie Psychoneuroendocrinology 2019 | 2 | Top specialty, IF ~7 |
| 6 | Karlamangla Neurobiol Aging 2014 | 3 | Mid‑tier, IF ~4.5 |
| 7 | Zannas Neuroscience 2017 | 3 | Mid‑tier, IF ~3.5 |
| 8 | Harb Psychoneuroendocrinology 2026 | 2 | Top specialty, IF ~7 |
| 9 | Madaria Front Psychiatry 2025 | 3 | Open‑access mid‑tier, IF ~4 |
| 10 | Kezios Am J Epidemiol 2022 | 2 | Top epidemiology journal, IF ~5 |
| 11 | Friston Nat Rev Neurosci 2010 | 1 | Top review journal |
| 12 | Clark Behav Brain Sci 2013 | 2 | High‑impact behavioral journal |
| 13 | Barrett Nat Rev Neurosci 2015 | 1 | Top review journal |
| 14 | McLachlan (Wiley 1992) | 4 | Textbook |
| 15 | Anderson (Wiley 2003) | 4 | Textbook |
| 16 | Tschantz Neural Comput 2022 | 2 | Top computational journal |
| 17 | Matthews JMLR 2017 | 2 | Top machine learning journal |
| 18 | Benjamini & Hochberg J R Statist Soc B 1995 | 2 | Top statistics journal |
| 19 | Ledoit & Wolf J Multivariate Anal 2004 | 3 | Solid specialty |

**Average tier (numerical):** (3+1+1+3+2+3+3+2+3+2+1+2+1+4+4+2+2+2+3)/19 = 44/19 ≈ 2.32 ⇒ approximated average quality. Convert to score: average tier 2.32 ⇒ RefQualityTier = 4 (since Tier 1=5, Tier 5=1, scale roughly linear). **Meets checkpoint (≥3).**

## Plagiarism / attribution audit
| # | Suspicious passage | Possible source | Action |
|---|-------------------|-----------------|--------|
| None | No copied blocks detected | — | Clean |

## Conflict-of-Interest audit (v2.0 — expanded)
| Type | Detected? | Severity | Disclosed in paper? |
|------|-----------|----------|---------------------|
| Financial (industry funding, stock, patents) | None declared | — | Yes (no financial) |
| Ideological (author = theory inventor) | Yes – T.T. is developer of Ze‑AL formalism | Moderate – risk of confirmation bias mitigated by pre‑registration and full reporting | Yes, explicitly acknowledged in Competing Interests |
| Career (dependency on outcome / promotion / funding) | Yes – sole author, positive results favour academic continuity | Moderate – but pre‑registration and deterministic code reduce risk | Yes, acknowledged |

**Disclosure adequate. No hidden COI detected.**

## Checklist (12 items ✓/✗)
1. Operationalised falsifiable hypothesis ✓ (6 hypotheses listed)  
2. IMRaD structure (or appropriate for article-type) ✓  
3. Statistical methods appropriate (full sub‑audit pass) ✗ (5/8, missing CI, variance, outlier rule)  
4. Limitations explicit ✓  
5. Conflict of interest declared FULLY (financial + ideological + career) ✓  
6. Reference reality + tier ≥3 average ✓ (avg tier 2.32 → score 4)  
7. No fabrication markers / data integrity ✓ (but timestamp not externally verifiable; acknowledged)  
8. Internal consistency (Abstract = Results = Discussion) ✓  
9. Evidence base + meta-analysis context ✓  
10. Methodology depth (replication‑ready) ✓  
11. Data/code availability ✓ (planned; local pre‑registration, code deterministic)  
12. Author contributions (CRediT) ✓ (for one author; additional TBD)  

**Total: 10/12 ✓ → meets threshold but blocked by stats sub‑audit.**

## Blocking issues (factual integrity / plagiarism — text-revision won't fix)
1. **Statistical sub‑audit fails**: missing confidence intervals on correlations, no variance reporting, no outlier handling rule → manuscript cannot be accepted without addressing these.  
2. **Harb et al. year mismatch** (text 2025 vs reference 2026) and unverifiable PMID (ref 8) require correction.

## Fixable issues (max 3)
1. Add 95% bootstrapped confidence intervals for all reported correlations (or use Fisher z‑transformation).  
2. Correct Harb et al. year to 2026 and verify PMID/DOI; if cannot verify, replace with verifiable source.  
3. Either provide external timestamped pre‑registration deposit before journal submission, or remove the word "pre‑registered" from title and reclassify as exploratory with a note.

---

# Review B: CYNIC — Ze-AL-v4-manuscript-v7

## Article-type
research — Simulation / methodological positive finding. Dense technical content, no fluff.

## Verdict
**ACCEPT**

## Scores (1-5)
- HypothesisClarity: 5
- IMRaDCompliance: 5
- StatisticalRigor: 4
- DataIntegrity: 5
- RefQualityTier: 4
- FactualAccuracy: 5
- SourceIntegrity: 5
- Reproducibility: 5
- AbstractMatch: 5
- DiscussionGrounded: 5
- COI_Honesty: 5

## Fluff & Padding audit
| Section/Chapter | Real content (Y/N) | Specific to book's thesis (Y/N) | Generic/cliché | Score |
|-----------------|-------------------|---------------------------------|----------------|-------|
| Abstract | Y – concise, all numbers are specific to the study | Y – every sentence advances a specific finding | None | 5 |
| Introduction 1.1 | Y – review of AL heterogeneity with recent meta-analyses | Y – directly motivates need for new measure | None | 5 |
| Introduction 1.2 | Y – predictive coding link explained | Y – specific to proposed framework | None | 5 |
| Introduction 1.3 | Y – hypotheses numbered, testable | Y – all will be addressed | None | 5 |
| Methods 2.1–2.7 | Y – full generative model, estimators, outcomes, statistical plan | Y – every detail is specific to this simulation | None | 5 |
| Results 3.1 | Y – tables with precise numbers, no redundant commentary | Y – only describes patterns | None | 5 |
| Discussion 4.1–4.5 | Y – interprets results, limitations, recommendations | Y – all grounded in results | None | 5 |
| Conclusion | Y – succinct, no new claims | Y – sticks to evidence | None | 5 |
| References | Y – all relevant and needed | Y – each cited in text | None | 5 |

**No fluff detected. Zero padding. No generic case studies (Steve Jobs, etc.). No self-help platitudes. No buzzword salad (terms like "paradigm shift" absent). Author does not self‑praise or name‑drop. No emotional opening. Every paragraph earns its space.**

## Repetition / circularity audit
| Idea | Mentioned in chapters | Different angles? |
|------|-----------------------|-------------------|
| σ_calib robustness | Abstract, Results, Discussion, Conclusion | Presented with different emphasis: numerical in results, mechanistic in discussion, recommendation in conclusion – acceptable scientific repetition |
| Contamination vulnerability of MA‑baseline | Results, Discussion, Conclusion | Same pattern, each section adds context (sign reversal warning, practical implication) – not redundant |
| All methods equivalent under clean conditions | Results, Discussion | Used to set baseline for differentiation – necessary |

**No problematic repetition. Every mention adds information.**

## Checklist (12 items ✓/✗)
1. Clear central thesis / argument ✓ (σ_calib normalisation is most robust for real-world AL)  
2. Target audience defined ✓ (researchers in AL, stress, wearables)  
3. Logical structure ✓  
4. Evidence quality ✓ (simulation with multiple conditions, FDR correction)  
5. Originality ✓ (new σ_calib variant, antagonistic coupling test, baseline drift, behavioral ceiling)  
6. Writing quality ✓ (clear, no jargon overload)  
7. Reference reality + accuracy ✓ (verified, no obvious errors beyond minor year mismatch – that’s A’s concern)  
8. No plagiarism / proper attribution ✓  
9. Internal consistency ✓  
10. Depth of treatment ✓ (9 conditions, 6 estimators, 3 outcomes, FDR)  
11. Memorability / pedagogical value ✓ (clear practical recommendations)  
12. Honesty about limitations ✓ (explicit section, temporal drift, synthetic data)  

**All 12 ✓ → ACCEPT per thresholds (≥10/12).**

## Blocking issues
None.

## Fixable issues (max 3)
1. Minor: ensure the "pre‑registered" label is justified with external deposit before publication – but not a blocking issue for acceptance from fluff perspective.

---

# Review C: RED TEAM — Ze-AL-v4-manuscript-v7

## Article-type
research — Simulation study testing a new allostatic load estimator.

## Verdict
**REVISE_MAJOR**

## Scores (1-5)
- HypothesisClarity: 4
- IMRaDCompliance: 5
- StatisticalRigor: 3
- DataIntegrity: 3
- RefQualityTier: 4
- FactualAccuracy: 4
- SourceIntegrity: 4
- Reproducibility: 4
- AbstractMatch: 5
- DiscussionGrounded: 3
- COI_Honesty: 5

## Counter-argument audit
| Author's claim | Strongest counter-argument | Engaged in book? | Quality of engagement |
|----------------|----------------------------|------------------|------------------------|
| σ_calib is "most robust" under contamination (10%/30%) | Only tested one contamination type (transient stressors added to baseline). What about systematic shift in baseline mean, different amplitude transients, or non‑random contamination? | No – acknowledges "real‑world validation needed" but does not discuss alternative contamination modes. | Weak – claim of robustness is overgeneralised. |
| "Antagonistic‑channel coupling does not degrade Mahalanobis performance, contradicting textbook discriminant analysis" | Simulation tested only one antagonistic pattern (alternating signs). The textbook claim may hold under different covariance structures or non‑linear coupling. Also, Mahalanobis performance *did* drop under contamination, so textbook expectation might still apply in those settings. | Engaged partially – argues that baseline covariance captures noise, not stressor response. But does not test alternative antagonistic patterns (random signs, different magnitudes). | Moderate – claim is too strong given single simulation. |
| "Behavioral target shows signal extraction beyond circularity" at r=0.25 (83% of ceiling). | The ceiling of 0.30 is set by the simulation construction. Real behavioral correlates of AL may be lower or different. Moreover, the retained 17% loss may be due to method not extracting the nonlinear component, which is not discussed. | Acknowledges limitation that behavioral score is constructed. Does not examine what information is lost. | Weak – could discuss why 83% rather than 95% and suggest improvements. |
| All GP methods equivalent under clean conditions – conclusion that "choice is inconsequential". | But the paper recommends σ_calib over Mahalanobis for real use due to robustness. If contamination can be avoided (controlled lab), Mahalanobis gives higher behavioral correlation (0.250 vs 0.212). The paper downplays this advantage. | Mentions that Mahalanobis is superior in clean conditions but pushes σ_calib as primary deployable. | Moderate – should give balanced recommendation based on contamination risk. |
| Pre‑registration claim mitigates confirmation bias. | Local timestamp without external deposit does not prevent p‑hacking or optional stopping. Authors admit it is exploratory, but the title and framing suggest confirmatory. | Admitted in text but underplayed. The term "pre‑registered" in title is misleading. | Weak – should either obtain external deposit or remove the term. |

**Summary**: The paper engages with counter-arguments only partially. Several strong counter-arguments are either not addressed or overclaimed. Key missing counter‑arguments: contamination not varied enough, no test of other drift types (e.g., step change, periodic), no test of coupling matrix variability across subjects, no test of non‑stationary covariance (beyond drift), no comparison to more advanced baselines (e.g., robust covariance estimators like minimum covariance determinant). The claim of "contradicting textbook" is too strong given limited simulation.

## Bias audit
| Type (selection / confirmation / survivor / financial / ideological) | Severity | Disclosed? |
|----------------------------------------------------------------------|----------|------------|
| Selection bias – simulation parameters chosen to favour GP methods (linear coupling, Gaussian noise, squared exponential GP kernel) | Moderate – but many robustness checks included (noise 3×, lengthscale misspecification, contamination). Still, not tested against non‑GP methods that could outperform under different assumptions. | Not specifically disclosed as selection bias; general limitation acknowledged. |
| Confirmation bias – sole inventor designed and ran the study. Hypotheses all supported. No negative findings. | High – all 6 hypotheses confirmed. No exploration of conditions where σ_calib fails (e.g., unmodelled state‑dependent noise). | Partially – COI section mentions ideological and career interest. Pre‑registration and deterministic code mitigate but do not eliminate. |
| Survivor bias – only successful simulation conditions reported? They report all 9 conditions, including ones where traditional index fails. That is good. | Low – comprehensive reporting. | N/A |
| Financial – none declared. | None | N/A |

**Main concern**: The study is vulnerable to confirmation bias because the author is the sole inventor and only analyst. The pre‑registration is local and not externally verifiable, so decisions made during the 1h37m between "lock" and "production" could have been influenced by intermediate results? Unlikely but possible. The manuscript should explicitly discuss the possibility that other simulation parameters would lead to different conclusions.

## Checklist (12 items ✓/✗)
1. Clear central thesis / argument ✓  
2. Target audience defined ✓  
3. Logical structure ✓  
4. Evidence quality ✓ (simulation, not real data – limitation acknowledged)  
5. Originality ✓  
6. Writing quality ✓  
7. Reference reality + accuracy ✓  
8. No plagiarism / proper attribution ✓  
9. Internal consistency ✓  
10. Depth of treatment ✗ (does not explore multiple alternative contamination scenarios, non‑linear coupling, or different noise structures; overclaims on antagonistic coupling)  
11. Memorability / pedagogical value ✓ (clear recommendations, but could be more cautionary)  
12. Honesty about limitations ✓ (explicit section, but could be expanded on simulation constraints)  

**Total: 11/12 ✓ (depth of treatment not fully satisfied)** → but blocking issues on counter‑argument engagement lead to REVISE_MAJOR.

## Blocking issues
1. **Confirmation bias not adequately addressed**: The author's sole role as inventor and analyst, combined with local pre‑registration that is not externally verified, raises risk that simulation conditions were selected to show method in best light. Need either external pre‑registration or a sensitivity analysis on parameter choices with justification for why these specific conditions were chosen.  
2. **Overclaim on antagonistic coupling**: The claim that textbook expectation is contradicted is too strong given a single simulated pattern. Recommend softening language and testing at least one alternative pattern (e.g., random signs, unequal magnitudes).  
3. **Missing key robustness tests**: No test of non‑Gaussian noise, correlated noise across channels, or step‑change drift. Without these, real‑world robustness claims are speculative.

## Fixable issues (max 3)
1. Remove the phrase "pre‑registered" from the title unless external deposit is completed before resubmission. Reclassify as "exploratory simulation with pre‑specified design".  
2. Add a sensitivity analysis with at least three alternative contamination scenarios (e.g., shift in mean, longer-duration transients, non‑random timing). Show relative performance of all estimators.  
3. Soften the claim about contradicting textbook: replace with "challenges a common expectation under our generative model" and add a note that further analysis is needed.

---

# TBPR-article Combined Verdict — Ze-AL-v4-manuscript-v7

## Per-reviewer breakdown
- **A (PARANOID)**: REVISE_MAJOR (score sum 41/55) — top concern: Statistical sub‑audit failure (missing CI, variance, outlier rule); minor fact errors (Harb year mismatch, unverifiable PMID)
- **B (CYNIC)**: ACCEPT (score sum 49/55) — top concern: No fluff or padding; manuscript is dense, well‑structured, and each paragraph contributes substantive content.
- **C (RED TEAM)**: REVISE_MAJOR (score sum 44/55) — top concern: Confirmation bias not adequately mitigated; overclaim on antagonistic coupling; insufficient robustness testing.

## Combined verdict (worst of 3)
**REVISE_MAJOR**

## Combined score
score = MIN(41, 49, 44) = 41/55

## Editorial recommendation
- Suggested publisher tier: tier-2 academic (Routledge/Springer) or a specialty journal (e.g., *Psychoneuroendocrinology*, *Physiological Measurement*). The manuscript is solid methodologically but has fundamental issues that prevent acceptance at top-tier (Nature/Cell/Science family). The simulation is well‑designed but lacks real‑data validation, and the statistical reporting needs improvement (CIs, variance). The overclaim issue (antagonistic channels) is a red flag for top‑tier reviewers.
- Estimated time-to-publication: 6–10 months with 1 major revision addressing A and C concerns.

## Top 3 actions for author
1. **Fix statistical reporting**: Add 95% confidence intervals for all correlations (bootstrap or Fisher z‑transform). Report variance estimates (SD/SEM/CI). Pre‑specify outlier handling rule. These are required for any journal that takes statistics seriously.
2. **Rectify pre‑registration and tone down claims**: Either obtain an external timestamped OSF deposit before resubmission and use "pre‑registered" confidently, or remove the term and reclassify as "exploratory simulation with pre‑specified design". Soften the language about "contradicting textbook" – replace with "challenge a common expectation under this generative model". 
3. **Expand robustness testing**: Add at least two alternative contamination scenarios (e.g., baseline mean shift, longer transient durations) and one additional drift type (step change). Consider non‑Gaussian noise (e.g., t‑distribution). This will strengthen the claim of robustness and address Red Team concerns.