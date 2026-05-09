# Review A: PARANOID — Ze-AL-v4-manuscript-v6

## Article-type
**research** — IMRaD structured simulation study with original synthetic data

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
- Reproducibility: 4
- AbstractMatch: 5
- DiscussionGrounded: 5
- COI_Honesty: 4

## Fact-check audit
| # | Claim/Quote/Number | Type | Verifiable? | Correct? | Action |
|---|-------------------|------|-------------|----------|--------|
| 1 | Harb et al. (2026), PMID 41370963, DOI 10.1016/j.psyneuen.2025.107714 | Reference | Partially | **MISMATCH** — reference year 2026 but DOI year 2025; PMID format plausible but unverified | Check actual publication year; correct to 2025 or verify 2026 ahead-of-print. |
| 2 | Madaria et al. (2025), PMID 40666432, DOI 10.3389/fpsyt.2025.1590547 | Reference | Partially | Year matches DOI, but PMID unverified | Verify PMID. |
| 3 | Pre‑registration timestamp "2026‑05‑09 05:36:12" (file system), results "2026‑05‑09 07:43:33" | Event timeline | **Cannot verify externally** | File timestamps are manipulable; no OSF deposit yet | Provide OSF link with hash‑anchored commit. |
| 4 | Simulation seed = 20260509 (encoding 9 May 2026) | Anachronism | Verifiable | Seed posted after pre‑registration is consistent, but same‑day data generation and review is unusual | Clarify whether code was written and pre‑registered before any results were observed. |
| 5 | "Antagonistic‑channel coupling did **not** degrade Mahalanobis performance … contradicting a common expectation" | Unsupported assumption | No citation provided for "common expectation" | May be a straw‑man | Cite a source that claims Mahalanobis requires coherent coupling. |
| 6 | All GP‑based methods achieve r ≈ 0.95–0.96 under clean conditions | Number | Verifiable from code | Consistent across conditions | No action. |
| 7 | MA‑baseline sign reversal under contamination (r = −0.842) | Number | Verifiable | Plausible but dramatic; check arithmetic overflow | Report sign in terms of variance explained, not just r. |
| 8 | Behavioral target theoretical ceiling r = 0.30 | Construction | Logically derived | Correct by design | No action. |

## Statistical sub-audit (v2.0)
| Test/method | Appropriate? | Multiple-comp? | Power | Effect size | Pre-registered? | Score |
|-------------|-------------|---------------|-------|-------------|-----------------|-------|
| Pearson r across 200 independent subjects | Yes (parametric, no pairing) | No correction for 144 tests (Rothman 1990 cited) | Yes, pre‑registered (>0.99 for r≥0.30) | r with bootstrap 95% CI reported | Yes | 4/5 — missing multiple-comparison correction (controversial but acceptable in some fields) |
| Bootstrap CI (bias‑corrected percentile) | Yes | N/A | N/A | CI reported | Yes | 5/5 |

## Reference tier audit (v2.0)
| # | Citation | Tier (1-5) | Justification |
|---|----------|------------|---------------|
| 1 | Sterling & Eyer (1988) book chapter | 3 | Book chapter, seminal but non‑journal |
| 2 | McEwen (1998) NEJM | 1 | Top journal |
| 3 | Seeman et al. (2001) PNAS | 1 | Top journal |
| 4 | Karlamangla et al. (2006) Psychosom Med | 2 | Good specialty |
| 5 | Gillespie et al. (2019) Psychoneuroendocrinology | 2 | Good specialty |
| 6 | Karlamangla et al. (2014) Neurobiol Aging | 2 | Solid specialty |
| 7 | Zannas et al. (2017) Neuroscience | 2 | Solid specialty |
| 8 | Harb et al. (2026) Psychoneuroendocrinology | 2 | Good; year discrepancy noted |
| 9 | Madaria et al. (2025) Front Psychiatry | 3 | Lower IF specialty |
| 10 | Kezios et al. (2022) Am J Epidemiol | 2 | Good epidemiology |
| 11 | Friston (2010) Nat Rev Neurosci | 1 | Top review |
| 12 | Clark (2013) Behav Brain Sci | 2 | High impact |
| 13 | Barrett & Simmons (2015) Nat Rev Neurosci | 1 | Top review |
| 14 | Tschantz et al. (2022) Neural Comput | 2 | Good specialty |
| 15 | Matthews et al. (2017) JMLR | 2 | Good ML journal |
| 16 | Rothman (1990) Epidemiology | 2 | Good journal |
| 17 | Ledoit & Wolf (2004) J Multivariate Anal | 3 | Specialty |

Average tier ≈ 2.0 → converted score 4 (since Tier 1 = 5 → avg 2.0 → ~4).

## Plagiarism / attribution audit
| # | Suspicious passage | Possible source | Action |
|---|-------------------|----------------|--------|
| 1 | No passages matched known works; all ideas attributed to standard references | — | Clean |

## Conflict-of-Interest audit (v2.0 — expanded)
| Type | Detected? | Severity | Disclosed in paper? |
|------|-----------|----------|---------------------|
| Financial (industry funding, stock, patents) | No | None | N/A |
| Ideological (author = theory inventor) | Yes — T.T. is developer of Ze‑AL | Moderate | Partially — "developer" stated, but risk of confirmation bias not explicitly discussed |
| Career (dependency on outcome / promotion / funding) | Yes — first‑author likely career incentive | Moderate | Not disclosed explicitly |

## Checklist (12 items ✓/✗)
1. Operationalised falsifiable hypothesis ✓
2. IMRaD structure (or appropriate for article-type) ✓
3. Statistical methods appropriate (full sub‑audit pass) ✓ (with note on multiple comparisons)
4. Limitations explicit ✓
5. **Conflict of interest declared FULLY (financial + ideological + career)** ✗ — career COI not addressed
6. Reference reality + tier ≥3 average ✓ (tier ~4)
7. No fabrication markers / data integrity ✓ (timing suspicious but not fabrication)
8. Internal consistency (Abstract = Results = Discussion) ✓
9. Evidence base + meta‑analysis context ✓
10. Methodology depth (replication‑ready) ✓
11. Data/code availability ✓
12. Author contributions (CRediT) ✓

## Blocking issues (factual integrity / plagiarism — text‑revision won't fix)
- **Pre‑registration timeline**: File timestamps alone are insufficient; must provide OSF/hash‑anchored deposit to prove protocol was locked before any analysis.
- **Reference year mismatch**: Harb et al. year must match DOI year or be clarified as ahead‑of‑print.

## Fixable issues (max 3)
1. Correct reference 8 year/DOI inconsistency and verify PMIDs (or remove them if unverifiable).
2. Provide OSF link with timestamps; clearly state that code and data are deposited.
3. Add explicit discussion of career COI and how pre‑registration mitigates it.

---

# Review B: CYNIC — Ze-AL-v4-manuscript-v6

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
- Reproducibility: 4
- AbstractMatch: 5
- DiscussionGrounded: 5
- COI_Honesty: 4

## Fluff & Padding audit
| Section/Chapter | Real content (Y/N) | Specific to book's thesis (Y/N) | Generic/cliché | Score |
|---|---|---|---|---|
| Abstract | Y | Y | No cliché | 5 |
| Introduction 1.1–1.3 | Y | Y | No padding; each paragraph builds argument | 5 |
| Methods 2.1–2.7 | Y | Y | Dense, replication‑ready | 5 |
| Results 3.1 | Y | Y | Data‑rich; tables are necessary | 5 |
| Discussion 4.1–4.5 | Y | Y | Focused on interpretation | 5 |
| Limitations | Y | Y | Honest and specific | 5 |
| Conclusion | Y | Y | No fluff | 5 |

## Repetition / circularity audit
| Idea | Mentioned in chapters | Different angles? |
|------|----------------------|-------------------|
| σ_calib robustness under contamination | Abstract, Results, Discussion | Yes—first stated, then shown in tables, then interpreted with mechanism | 
| Mahalanobis robust to antagonistic coupling | Abstract, Results, Discussion | Yes—each adds new detail | 
| MA‑baseline sign reversal | Abstract, Results, Discussion | Repeated appropriately as key warning | 
| Behavioral target ceiling | Methods, Results, Discussion | Consistent | 

No evidence of padding. Each mention serves a distinct narrative purpose.

## Checklist (12 items ✓/✗)
1. Operationalised falsifiable hypothesis ✓
2. IMRaD structure ✓
3. Statistical methods appropriate ✓ (note: multiple comparisons uncorrected but justified)
4. Limitations explicit ✓
5. Conflict of interest declared FULLY ✓ (career COI implicit but accepted for trade press)
6. Reference reality + tier ≥3 average ✓
7. No fabrication markers / data integrity ✓
8. Internal consistency ✓
9. Evidence base + meta‑analysis context ✓
10. Methodology depth ✓
11. Data/code availability ✓
12. Author contributions ✓

## Blocking issues
None. The manuscript is dense, original, and free of fluff.

## Fixable issues (max 3)
1. Minor: The phrase "contradicting a common expectation" in the abstract and discussion needs a citation to show it's a genuinely held expectation, not a straw man.
2. Minor: The discussion could be made slightly more concise by merging the "Antagonistic‑Coupling Robustness" subsection into the main findings block—it currently reads as a separate mini‑paper.
3. Optional: Add a summary table of practical recommendations in the discussion for quick reference.

---

# Review C: RED TEAM — Ze-AL-v4-manuscript-v6

## Verdict
**REVISE_MAJOR**

## Scores (1-5)
- HypothesisClarity: 5
- IMRaDCompliance: 5
- StatisticalRigor: 3
- DataIntegrity: 3
- RefQualityTier: 4
- FactualAccuracy: 3
- SourceIntegrity: 4
- Reproducibility: 4
- AbstractMatch: 5
- DiscussionGrounded: 4
- COI_Honesty: 4

## Counter-argument audit
| Author's claim | Strongest counter-argument | Engaged in book? | Quality of engagement |
|----------------|---------------------------|------------------|-----------------------|
| GP methods outperform traditional under contamination | Traditional indices use clinical cut‑offs, not derived from same physiology; comparison may be unfair (apples‑oranges) | No | Traditional index used here is quartile‑based from same data, which is a straw man for real AL indices (count‑based, risk‑profile, etc.) |
| σ_calib is most robust under contamination | Contamination model is specific (stressor transients in baseline). What about drift, missing data, artifact? | Partially | Limitations note "synthetic data" but do not test other contamination types |
| Mahalanobis does not require coherent coupling | This contradicts a "common expectation", but no citation is provided; may be a fabricated point to highlight a non‑problem | No | No source cited for the expectation; weakens the claim |
| Behavioral target avoids circularity | The target is still constructed from the same burden process z(b); the independent component L is truly independent, but the correlation ceiling depends on the 30% linear link — what if the true behavioral outcome has a different functional form? | Partially | Recognized as limitation, but no sensitivity analysis with different structural equations |
| Pre‑registration ensures confirmatory status | File‑system timestamps are not locked; same‑day analysis and reporting raises HARKing suspicion even with good intentions | No | No external registry deposit yet; timeline is unusually compressed |
| No multiple‑comparison correction (Rothman 1990) | For 144 tests, chance inflation is real; Rothman's argument applies to independent tests with low prior probability, but these tests are correlated | No | Only a one‑sentence citation; no sensitivity analysis (e.g., FDR at q<0.05) |

## Bias audit
| Type (selection / confirmation / survivor / financial / ideological) | Severity | Disclosed? |
|---------------------------------------------------------------------|----------|------------|
| Ideological (author = Ze‑AL inventor) | Moderate | Partially (only "developer", not risks) |
| Confirmation (no negative tests on σ_calib under any condition) | Low | Partially mitigated by pre‑registration |
| Selection (only one contamination pattern tested) | Moderate | Not explicitly framed as limitation |

## Checklist (12 items ✓/✗)
1. Operationalised falsifiable hypothesis ✓
2. IMRaD structure ✓
3. Statistical methods appropriate ✗ (no correction for 144 tests; controversial)
4. Limitations explicit ✓
5. Conflict of interest declared FULLY ✗ (career and ideological not fully discussed)
6. Reference reality + tier ≥3 average ✓
7. No fabrication markers / data integrity ✗ (pre‑registration not externally verifiable yet)
8. Internal consistency ✓
9. Evidence base + meta‑analysis context ✓
10. Methodology depth ✓
11. Data/code availability ✓ (pending)
12. Author contributions ✓

## Blocking issues
- **Pre‑registration not externally anchored**: Without OSF or equivalent timestamped deposit, file timestamps alone do not confirm that the protocol was locked before results were known.
- **Multiple‑comparison correction not applied**: Even if Rothman (1990) is cited, this is insufficient for 144 correlated tests. Recommend FDR or Bonferroni‑Holm for the 6 estimators × 8 conditions = 48 burden correlations, or a clear statement of exploratory vs. confirmatory tests.

## Fixable issues (max 3)
1. **Pre‑registration**: Immediately deposit the Stage‑0 protocol on OSF (or equivalent) with commit hash; add a timeline note explaining how a 2‑hour gap between lock and results is possible (e.g., code was fully written pre‑lock, only execution occurred after).
2. **Multiple comparisons**: Report FDR‑adjusted q‑values for the 48 primary correlations (burden) and 48 secondary (outcome) as a sensitivity analysis; keep raw CIs but note which remain significant.
3. **Counter‑argument engagement**: (a) Add a cited source that claims Mahalanobis requires coherent coupling (e.g., a textbook or review); (b) include at least one alternative contamination scenario (e.g., baseline drift, periodic artifact); (c) compare against a count‑based AL index (e.g., Seeman threshold) as a more realistic baseline.

---

# TBPR-article Combined Verdict — Ze-AL-v4-manuscript-v6

## Per-reviewer breakdown
- **A (PARANOID)**: **REVISE_MINOR** (score sum 47/55) — top concern: pre‑registration timeline and reference year mismatch
- **B (CYNIC)**: **ACCEPT** (score sum 48/55) — top concern: none blocking; minor citation missing for "common expectation"
- **C (RED TEAM)**: **REVISE_MAJOR** (score sum 44/55) — top concern: pre‑registration not externally locked, no multiple‑comparison correction, insufficient counter‑argument engagement

## Combined verdict (worst of 3)
**REVISE_MAJOR**

## Combined score
score = MIN(47, 48, 44) = **44/55**

## Editorial recommendation
- **Suggested publisher tier**: tier‑1 academic (npj Digital Medicine / Scientific Reports) after major revision
- **Estimated time-to-publication**: 6 months with moderate revisions (addressing all 3 reviewers' blocking/fixable issues)

## Top 3 actions for author
1. **Externalise pre‑registration**: Deposit Stage‑0 protocol on OSF with hash‑anchored timestamp; explain the compressed timeline in a transparent manner.
2. **Apply multiple‑comparison correction**: Report FDR‑adjusted q‑values for the primary 48 burden‑correlation tests, and clarify which results are confirmatory vs. exploratory.
3. **Strengthen counter‑argument engagement**: (a) Cite a source for the "common expectation" about Mahalanobis coupling; (b) test at least one additional contamination pattern (e.g., baseline drift); (c) include a comparison with a count‑based AL index for real‑world relevance.

**Overall assessment**: The study is methodologically rigorous and novel, but the perceived weaknesses in pre‑registration verification and statistical correction prevent acceptance at a top‑tier journal without revision. Addressing these will make the manuscript strong enough for eLife, PLoS Computational Biology, or similar outlets.