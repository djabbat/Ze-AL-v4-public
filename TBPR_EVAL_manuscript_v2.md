# Review A: PARANOID — Ze-AL-v4-manuscript-v2

## Article-type
research (methodological original research with simulated data) — IMRaD structure, original synthetic data, pre-registered.

## Verdict
**REVISE_MAJOR**

## Scores (1-5)
- HypothesisClarity: 5
- IMRaDCompliance: 5
- StatisticalRigor: 4
- DataIntegrity: 4
- RefQualityTier: 3
- FactualAccuracy: 3
- SourceIntegrity: 3
- Reproducibility: 5
- AbstractMatch: 5
- DiscussionGrounded: 4
- COI_Honesty: 4

## Fact-check audit

| # | Claim/Quote/Number | Type | Verifiable? | Correct? | Action |
|---|---|---|---|---|---|
| 1 | Harb et al. (2025) I²=94.24% | Statistical/meta-analytic | Partial — year 2025 plausible but cannot verify existence without DOI lookup (no DOI given in text for ref 8). In-text: "Psychosom Med. 2025;87(4):341–52" — Psychosomatic Medicine is real journal. Issue: Volume 87 issue 4? JM: Vol 87 (2025) is plausible but issue 4 page range 341–52? Need confirmation. | ? | Request DOI or PMC ID; flag as unverifiable until supplied. |
| 2 | Madaria et al. (2025) r values | Statistical/meta-analytic | Same issue — "Psychol Med. 2025;55:e78" — Volume 55 (2025) for Psychological Medicine exists; e78 is plausible. | ? | Same request. |
| 3 | Kezios et al. (2022) from Epidemiology | Citation | Verifiable — Epidemiology 2022;33(3):369–77. DOI not given but known journal. | ✓ | OK |
| 4 | Friston 2010 Nat Rev Neurosci | Citation | Well-known — DOI 10.1038/nrn2787 correct. | ✓ | OK |
| 5 | Tschantz et al. 2022 PLoS Comput Biol | Citation | DOI 10.1371/journal.pcbi.1010327 — real. | ✓ | OK |
| 6 | Tkemaladze bioRxiv 2024 (self-citation) | Pre-print | DOI 10.1101/2024.11.15.623456 — plausible bioRxiv ID. | ? | Verify at bioRxiv; self-citation rate >30%? Not clear. |
| 7 | "v3 r=0.389 [0.260–0.502]" from previous study | Statistical | Ref 15 claims this. Cannot cross-check without full data. | ? | Author's own prior result; acceptable if documented. |
| 8 | Pre-registration seed 20260509 | Claim | Seed matches document date (2026-05-09) — suspicious coincidence. No OSF link to locked timestamp. | ? | Demand OSF link with timestamp before data generation. |
| 9 | n=200 subjects per primary condition? Methods say n=200 subjects total, but then "7 scenarios, total 350 subjects" (Abstract) vs "200 subjects (4 scenarios × 50 each; final analysis added three more)" — inconsistency. | Internal | Abstract says 350 subjects, methods says 200 for primary, then add 3 scenarios (150 more) → 350 total? Need clarification. | ✗ | Contradiction between Abstract "n=200 subjects (7 scenarios, total 350 subjects)" — each scenario n=50 → 7*50=350. But methods say "200 subjects (4 scenarios × 50 each)". Revise for clarity. |
| 10 | "The v4 Mahalanobis and v4 VFE improve upon v3 σ_E by approximately +1%" | Relative improvement | Computations: r=0.958 vs 0.949 → (0.958-0.949)/0.949 = 0.0095 ≈ 1%. Correct arithmetic. | ✓ | OK |
| 11 | CI width for v4 Mahalanobis: 0.947–0.969 (difference 0.022) | Statistical | Bootstrap BCa CI plausible given n=50 and r≈0.96. | ✓ | OK |
| 12 | "Under a correctly specified generative model, v3 achieved r=0.389" from v3 study — but in current study v3 achieves 0.949. | Consistency | The authors explain this as due to different kernel. But this is a major discrepancy; the v3 result in current study is not a replication of the original v3 study. They should clearly label it as "v3 with improved kernel," not "v3 σ_E weighted" without distinction. | ? | Clarify naming to avoid confusion. |

## Statistical sub-audit (v2.0)

| Test/method | Appropriate? | Multiple-comp? | Power | Effect size | Pre-registered? | Score |
|---|---|---|---|---|---|---|
| Pearson correlation with ground truth | Appropriate — continuous outcome | Holm-Bonferroni for primary condition (m=6) — correctly applied. For sensitivity, declared exploratory, no correction — acceptable. | Yes, power analysis for Δr≥0.10, power ≥99% — adequate. | Reported with 95% BCa CIs — excellent. | Declared but OSF link not provided in paper — incomplete. Seed consistency suspicious. | 7/8 (missing explicit pre-registration lock confirmation) |
| Bootstrap CI method | BCa appropriate for skewed distributions — good. | — | — | — | — | OK |
| Missing: outlier handling | Not discussed — simulation may have no outliers, but rule should be stated. | — | — | — | — | -1 |
| **Sub-audit total** | | | | | | **7/8** |

## Reference tier audit (v2.0)

| # | Citation | Tier (1-5) | Justification |
|---|---|---|---|
| 1 | Sterling & Eyer 1988 (book chapter) | 4 | Textbook/edited volume chapter |
| 2 | McEwen 1998 NEJM | 1 | New England Journal of Medicine (Tier 1) |
| 3 | Seeman et al. 1997 Arch Intern Med | 3 | Archives of Internal Medicine (now JAMA Internal Medicine, Tier 2) |
| 4 | Levine & Crimmins 2014 J Gerontol A | 3 | Good specialty journal |
| 5 | Wallace et al. 2022 Ann Epidemiol | 3 | Epidemiology journal |
| 6 | Seeman et al. 2001 PNAS | 1 | Tier 1 |
| 7 | Zannas et al. 2015 Mol Psychiatry | 2 | Top psychiatry journal |
| 8 | Harb et al. 2025 Psychosom Med | 3 | Solid psychosomatic journal (tier 3) |
| 9 | Madaria et al. 2025 Psychol Med | 2 | Top psychiatry journal (tier 2) |
| 10 | Kezios et al. 2022 Epidemiology | 2 | Top epidemiology (tier 2) |
| 11 | Friston 2010 Nat Rev Neurosci | 1 | Tier 1 |
| 12 | Friston et al. 2014 Lancet Psychiatry | 2 | Tier 2 |
| 13 | Barrett et al. 2016 Emotion Review | 3 | Good specialty |
| 14 | Tschantz et al. 2022 PLoS Comput Biol | 2 | PloS Computational Biology (tier 2) |
| 15 | Tkemaladze 2024 bioRxiv | 4 | Pre-print |
| 16 | Montgomery 2013 textbook | 5 | Textbook (non-peer-reviewed source) |
| 17 | Fearnhead & Rigail 2019 J R Stat Soc B | 2 | Top statistics journal |
| 18 | Rousseeuw & Van Zomeren 1990 JASA | 2 | Top statistics journal |
| 19 | Cohen et al. 2013 Biogerontology | 3 | Good specialty |
| 20 | Alber et al. 2019 npj Digital Medicine | 2 | Tier 2 |
| **Average tier** | | **2.85** | (1,1,3,3,3,1,2,3,2,2,1,2,3,2,4,5,2,2,3,2) = 49/20 = 2.45 ≈ 2.5 |
| **RefQualityTier score** | | **3** | (average tier 2.5 → round to 3 for score) |

**Note:** Ref 16 (Montgomery textbook) is Tier 5. Ref 1 (book chapter) Tier 4. Self-citation Ref 15 Tier 4. Overall boundary but acceptable for revise.

## Plagiarism / attribution audit

| # | Suspicious passage | Possible source | Action |
|---|---|---|---|
| 1 | Introduction para 1-2: Standard description of allostasis and McEwen — closely follows language from many reviews, but not exact copy. | Many sources | Acceptable summary, attributed correctly. |
| 2 | In-text: "stability through change" — phrase attributed to Sterling and Eyer (1988). Correct. | Common attribution | OK |
| 3 | Formal definition of variational free energy: F = 0.5[log|Σ| + D^2 + const] — standard formula but not attributed to Friston 2010? They cite [12] after "under a Gaussian approximation" — acceptable. | Friston et al. | OK |
| 4 | No verbatim copying detected. | — | Clean |

## Conflict-of-Interest audit (v2.0 — expanded)

| Type | Detected? | Severity | Disclosed in paper? |
|---|---|---|---|
| Financial (industry funding, stock, patents) | None declared | — | Not required (no funding sources listed) |
| Ideological (author = theory inventor) | YES — author developed Ze-AL formalism | Moderate (incentive to show v4 superior) | Disclosed: "author developed the Ze‑AL formalism and has an academic interest" — partial; should explicitly state "risk of confirmation bias" |
| Career (dependency on outcome / promotion / funding) | Possible — if method adopted, career benefit | Low-Medium | Not explicitly discussed |

**Action:** Author should add a statement: "The author acknowledges that being the originator of the Ze‑AL framework creates an ideological interest, which was mitigated by pre-registration and fully open code."

## Checklist (12 items ✓/✗)
1. Operationalised falsifiable hypothesis ✓ (Hypothesis: v4 will resolve self-cancellation and improve correlation)
2. IMRaD structure (or appropriate for article-type) ✓
3. Statistical methods appropriate (full sub-audit pass) ✓ (7/8, borderline)
4. Limitations explicit ✓ (section 4.4)
5. Conflict of interest declared FULLY (financial + ideological + career) ✗ (ideological partially, career not)
6. Reference reality + tier ≥3 average ✗ (average tier ~2.5, 2 references unverifiable)
7. No fabrication markers / data integrity ✓ (except seed coincidence needs explanation)
8. Internal consistency (Abstract = Results = Discussion) ✗ (Abstract says n=200 subjects total 350, methods says 200 for primary then 3 more scenarios=350 — inconsistent)
9. Evidence base + meta-analysis context ✓ (cites relevant meta-analyses)
10. Methodology depth (replication-ready) ✓ (code available, detailed generator)
11. Data/code availability ✓ (GitHub)
12. Author contributions (CRediT) ✓ (listed)

**Total ✓: 10/12** (items 5,6,8 fail)

## Blocking issues (factual integrity / plagiarism — text-revision won't fix)
- Pre-registration seed coincidence (20260509) with current date — must provide OSF timestamp before any analysis.
- Two 2025 references cannot be verified — author must provide DOIs or PMC IDs. If fabricated, this becomes REJECT.

## Fixable issues (max 3)
1. Correct the Abstract/Methods inconsistency regarding subject count (350 vs 200 vs 50 per condition).
2. Expand COI disclosure to explicitly address ideological and career risk.
3. Provide OSF pre-registration link and DOI for all 2025 references.

---

# Review B: CYNIC — Ze-AL-v4-manuscript-v2

## Article-type
research — original methodological study with simulated data.

## Verdict
**REVISE_MAJOR**

## Scores (1-5)
- HypothesisClarity: 5
- IMRaDCompliance: 5
- StatisticalRigor: 4
- DataIntegrity: 4
- RefQualityTier: 4
- FactualAccuracy: 4
- SourceIntegrity: 4
- Reproducibility: 5
- AbstractMatch: 4
- DiscussionGrounded: 3
- COI_Honesty: 3

## Fluff & Padding audit

| Section/Chapter | Real content (Y/N) | Specific to book's thesis (Y/N) | Generic/cliché | Score (1=fluff, 5=dense) |
|---|---|---|---|---|
| Introduction 1.1 | Y — literature review of AL heterogeneity | Y — specific to problem | N | 5 |
| Introduction 1.2 | Y — predictive coding background | Y — relevant | N | 4 |
| Introduction 1.3 | Y — v3 negative finding | Y — direct | N | 5 |
| Introduction 1.4 | Y — v4 hypothesis | Y — direct | N | 4 |
| Methods 2.1 | Y — detailed simulation | Y | N | 5 |
| Methods 2.2 | Y — estimator descriptions | Y | N | 5 |
| Methods 2.3-2.5 | Y — evaluation details | Y | N | 4 |
| Results 3.1-3.3 | Y — tables, statistics | Y | N | 5 |
| Discussion 4.1-4.5 | Y — interpretation | Y | N | 4 |
| Conclusion | Y — summary | Y | N | 4 |

**Overall fluff assessment:** Minimal. The manuscript is dense and technical. Each paragraph serves a purpose. The only potential fluff is the repeated emphasis on "theoretical grounding" in active inference, which is a framing device but not excessive. Score: 4.5/5.

## Repetition / circularity audit

| Idea | Mentioned in chapters | Different angles? |
|---|---|---|
| Self-cancellation of v3 | Intro 1.3, Results 3.3, Discussion 4.1 | Different contexts: problem statement, result comparison, mechanism explanation — acceptable repetition. |
| Importance of clean calibration | Methods 2.2, Results 3.2 (contamination), Discussion 4.1, 4.2 | Repeated across sections but with new information each time — not excessive. |
| v4 outperforms v3 by ~1% | Abstract, Results 3.1, Discussion 4.1 | Each mention provides additional context (absolute r, relative improvement, robustness). However, the **narrative exaggerates** the improvement: "resolves self‑cancellation" implies a major fix, but v3 already had r=0.949 in the current simulation. The only real improvement is in contamination scenarios where v3 degrades, but then v4 Mahalanobis also degrades. The σ_calib univariate holds up. But the title claims "Resolving Signal Cancellation" — yet the v3 with improved kernel didn't have cancellation. This is **misleading framing** — a form of rhetorical fluff. | Score deduction. |
| Limitations | Discussion 4.4 | Only mentioned once — appropriate. | |

**Padding red flags:**
- "This is a small but consistent improvement" — the improvement is +1%, which is statistically significant given n=50, but practically trivial. The authors make it sound like a major breakthrough. This is **overclaim**.
- The contamination scenario is presented as a success for σ_calib, but the Mahalanobis variant (which is the primary v4 contribution) performs worse than v3 σ_E at 10% contamination (0.601 vs 0.620). This **contradicts** the narrative of uniform superiority.
- The VFE measure is admitted to be equivalent to Mahalanobis — but it's still included in results. Why? Just to have "variational free energy" in the title? This smells like **buzzword inclusion**.

## Repetition / circularity audit (cont.)
- The phrase "ground‑truth allostatic burden" is used repeatedly, but it's a simulation construct — it's not actual ground truth. This could mislead readers into thinking real-world validation was done. The discussion section properly notes it's simulation only, but the abstract and results sections could give a different impression.

## Checklist (12 items ✓/✗)
1. Clear central thesis ✓
2. Target audience defined ✓
3. Logical structure ✓
4. Evidence quality ✗ (only simulation, no real data)
5. Originality ✓ (method novel but incremental)
6. Writing quality ✓ (clear, precise)
7. Reference reality + accuracy ✓ (assume OK for Cynic)
8. No plagiarism ✓
9. Internal consistency ✓ (except subject count discrepancy)
10. Depth of treatment ✓
11. Memorability / pedagogical value ✓
12. Honesty about limitations ✓ (but overclaim in abstract)

**Total ✓: 11/12** (evidence quality is borderline — simulation is acceptable for methods paper, but limited)

## Blocking issues (fluff/padding — text-revision won't fix)
- Overclaim in abstract: "resolves the self‑cancellation problem" when v3 (with same kernel) also doesn't have the problem in this simulation. The original v3 negative finding was with a different kernel. The authors need to reframe this as a **controlled comparison of weighting schemes** rather than a "resolution" of an earlier failure.
- The inclusion of VFE adds no empirical value (same correlation as Mahalanobis) — either justify its theoretical relevance or remove it.

## Fixable issues (max 3)
1. Tone down claims: replace "resolves self‑cancellation" with "improves robustness relative to instantaneous uncertainty weighting."
2. Remove VFE from main results if it adds nothing; move to supplement as a theoretical extension.
3. Restructure the narrative to honestly present that v4 Mahalanobis is fragile under contamination, and the univariate σ_calib (which is simpler) is the more robust option.

---

# Review C: RED TEAM — Ze-AL-v4-manuscript-v2

## Article-type
research — methodological simulation study.

## Verdict
**REVISE_MAJOR**

## Scores (1-5)
- HypothesisClarity: 5
- IMRaDCompliance: 5
- StatisticalRigor: 4
- DataIntegrity: 4
- RefQualityTier: 3
- FactualAccuracy: 3
- SourceIntegrity: 3
- Reproducibility: 5
- AbstractMatch: 4
- DiscussionGrounded: 3
- COI_Honesty: 3

## Counter-argument audit

| Author's claim | Strongest counter-argument | Engaged in book? | Quality of engagement |
|---|---|---|---|
| v4 Mahalanobis resolves self-cancellation | v3 σ_E (with same kernel) already achieves r=0.949; v4 only adds +1%. The "cancellation" only existed in the original v3 with a different kernel. Therefore the claim is a straw-man: they fixed a problem that they re-created with a poor kernel choice. | Weakly addressed in section 3.3: "The v3 implementation in the present study... should not be interpreted as a replication of the original negative findings." But this is buried; the abstract still claims "resolves self-cancellation." The counter-argument that the problem was artefactual is not fully acknowledged. | Poor — they should state upfront that v3 with an appropriate kernel performs nearly as well. |
| v4 is robust to model misspecification | The only misspecifications tested are length-scale (±50%), no circadian, and tripled noise. These are all within the GP family. Real misspecification (e.g., non-stationary, non-Gaussian, missing channels) is not tested. Also, the GP model is fitted to each subject individually with full data — unrealistic. | Partially in section 4.4: "cannot capture all complexities." But they do not test any non-GP misspecification. | Medium — they acknowledge limitation but don't test worst-case misspecification. |
| Calibration contamination is a minor issue | In real-world settings, a "clean" steady-state window is often impossible (e.g., chronic stress patients). The contamination analysis shows that at 10% contamination, the Mahalanobis variant drops to r=0.601 — worse than v3 (0.620). This is a major failure of the primary v4 measure under realistic conditions. Yet the authors still recommend Mahalanobis as the primary measure. | They note that univariate σ_calib is more robust and should be used if clean calibration cannot be guaranteed. But the title and abstract highlight Mahalanobis/VFE as the key improvement. | Moderate — they do discuss in discussion, but the overall recommendation is ambiguous. |
| VFE adds theoretical grounding | VFE = 0.5(log|Σ| + D^2 + constant). Since log|Σ| is constant across time for a fixed calibration window, VFE is monotonically related to D^2, which is monotonically related to D (Mahalanobis distance) for positive values. Therefore VFE adds zero information beyond Mahalanobis. The only reason to include it is for future online adaptation, which they do not test. This is a **just-so story** without empirical support. | Not engaged — they admit "correlations identical...expected" but include it anyway without justification for the static index. | Weak — if they include VFE, they should either test an online adaptation scenario or remove it. |
| The method correlates with "ground-truth allostatic burden" | The ground truth is defined as the integral of the additive stressor component across channels — this is exactly what the Mahalanobis distance measures (since the stressor is additive on all channels simultaneously). The correlation is circular: the estimator is designed to detect that specific pattern. A more realistic ground truth would involve non-linear interactions, channel-specific stress responses, or recovery dynamics. | Not addressed — they define burden in a way that almost guarantees v4 success. | Very poor — this is the most serious logical gap. |

## Bias audit

| Type (selection / confirmation / survivor / financial / ideological) | Severity | Disclosed? |
|---|---|---|
| **Confirmation bias** — only scenarios that support v4 are presented as primary; the contamination scenario shows v4 Mahalanobis failing, but it's framed as a "robustness check" rather than a limitation. | High | Not explicitly disclosed as bias. |
| **Selection bias** — stressor design is additive and coherent across channels, exactly matching the Mahalanobis assumption. No alternative stressor types (e.g., antagonistic channel responses, pure noise increase) tested. | High | Not acknowledged. |
| **Ideological bias** — author is creator of Ze-AL framework. The entire paper is designed to salvage the concept after v3 failure. | Moderate | Disclosed as "academic interest" but not as bias. |
| **Survivorship bias** — only 50 subjects per condition, all simulated. No attrition, no missing data, no non-responders. Real data would have all these. | Medium | Acknowledged as limitation. |

## Checklist (12 items ✓/✗)
1. Clear central thesis ✓
2. Target audience defined ✓
3. Logical structure ✓
4. Evidence quality ✗ (simulation only, ground truth circular)
5. Originality ✓ (incremental)
6. Writing quality ✓
7. Reference reality + accuracy ✓
8. No plagiarism ✓
9. Internal consistency ✓
10. Depth of treatment ✓ (but shallow on counter-arguments)
11. Memorability / pedagogical value ✓
12. Honesty about limitations ✓ (but not about circularity of ground truth)

**Total ✓: 11/12** (evidence quality weak because ground truth is not independent)

## Blocking issues (confirmation bias / missing counter-arguments — text-revision won't fix)
- **Circular ground truth:** The definition of "allostatic burden" is the integral of additive stressor deviations across channels — which is exactly the same pattern that Mahalanobis distance is designed to detect. The high correlation is essentially a self-consistency check, not a validation. The authors must either (a) use an independent, clinically defined outcome (e.g., later disease onset) in simulation, or (b) fundamentally re-frame the paper as "internal consistency of the measure" rather than "validation against ground truth."
- **Stressor design amplifies v4 advantage:** The stressor affects all channels equally and linearly. In real physiology, different channels respond at different rates and directions (e.g., cortisol vs HRV often inverse). The current simulation sets up a best-case scenario for Mahalanobis. Without testing alternative stressor patterns, the generalizability is severely limited.

## Fixable issues (max 3)
1. Replace "ground-truth burden" with "simulated stressor component" — avoid implying external validation.
2. Add at least one alternative stressor pattern (e.g., anti-correlated channels, single-channel stressor) to test the specificity of Mahalanobis.
3. Acknowledge explicitly that the correlation is inflated by the circular definition and provide an independent benchmark (e.g., predict a downstream clinical event in simulated survival data).

---

# TBPR-article Combined Verdict — Ze-AL-v4-manuscript-v2

## Per-reviewer breakdown
- A (PARANOID): **REVISE_MAJOR** (score sum 45/55) — top concern: unverifiable 2025 references + pre-registration seed coincidence + internal inconsistency in subject numbers.
- B (CYNIC): **REVISE_MAJOR** (score sum 46/55) — top concern: overclaim relative to v3 performance, inclusion of VFE without added value, narrative that exaggerates improvement.
- C (RED TEAM): **REVISE_MAJOR** (score sum 43/55) — top concern: circular ground-truth definition that guarantees high correlation for the proposed measure.

## Combined verdict (worst of 3)
**REVISE_MAJOR**

## Combined score
score = MIN(score_A, score_B, score_C) = 43/55 (Reviewer C)

## Editorial recommendation
- **Suggested publisher tier:** tier-2 academic (Routledge/Springer) or top specialty journal (e.g., *PLoS Computational Biology* or *Journal of Theoretical Biology*) after major revision.
- **Estimated time-to-publication:** 6–9 months with major revisions, including addressing circular ground truth, resolving reference verifiability, and toning down claims.

## Top 3 actions for author
1. **Reframe the validation:** The current "ground-truth burden" is circular — it is exactly the additive multi-channel stressor pattern that Mahalanobis distance detects. Use an independent measure of burden (e.g., simulated clinical outcomes: time to event or severity score) to validate all estimators equally. Report correlations with this external variable.
2. **Fix the narrative and verifiability:** Correct the Abstract/Methods subject-count inconsistency, provide DOIs for all references (especially 2025 ones), and upload the pre-registration with a locked timestamp on OSF. Clearly state that v3 with an appropriate kernel also achieves near-perfect correlation; relativise the "resolution" claim.
3. **Justify or remove VFE:** If VFE is included only for theoretical completeness, move it to supplement; otherwise, test an online adaptation scenario where VFE might provide advantage over static Mahalanobis. Also test at least one alternative stressor pattern (e.g., non-linear, channel-specific) to demonstrate robustness beyond the ideal case.