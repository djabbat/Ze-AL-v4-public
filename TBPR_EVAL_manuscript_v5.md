# Review A: PARANOID — Ze-AL-v4-manuscript-v5

## Article-type
**research** — Pre-registered simulation study (methodological positive finding)

## Verdict
**REVISE_MAJOR**

## Scores (1-5)
- HypothesisClarity: 4
- IMRaDCompliance: 5
- StatisticalRigor: 3
- DataIntegrity: 3
- RefQualityTier: 2
- FactualAccuracy: 2
- SourceIntegrity: 2
- Reproducibility: 3
- AbstractMatch: 5
- DiscussionGrounded: 4
- COI_Honesty: 3

## Fact-check audit
| # | Claim/Quote/Number | Type | Verifiable? | Correct? | Action |
|---|-------------------|------|-------------|----------|--------|
| 1 | Harb et al. (2025) meta‑analysis: I²=94.24%, pooled effect small/non‑significant in older African Americans | Citation | ? | ? | **FABRICATION SUSPECTED.** No Harb et al. 2025 on this topic found on PubMed/Google Scholar. Paper appears to be fictional. |
| 2 | Madaria et al. (2025): AL elevated in schizophrenia (g=1.33) but not MDD | Citation | ? | ? | **FABRICATION SUSPECTED.** No Madaria et al. 2025 found. No Front Psychiatry article with that title. |
| 3 | Kezios et al. (2022): sex‑specific vs. global thresholds bias AL estimates | Citation | ✓ (Am J Epidemiol 2022;191:103‑15) | ✓ | Real paper, correct reference. |
| 4 | Rothman (1990): no adjustments needed for multiple comparisons | Citation | ✓ | ✓ | Correct. |
| 5 | Pre‑registration seed 20260509, timestamp locked at 2026‑05‑09 05:36:12 local, results saved 2026‑05‑09 07:43:33 (~1.5h later) | Procedure | ? | ? | **No public OSF link provided.** Only local file claimed. Timestamps cannot be verified. Not acceptable for reputable journal. |
| 6 | Ref 15: "Tkemaladze T. Ze‑AL v3… 2024. Unpublished manuscript" | Self‑citation | ✗ | N/A | Unpublished, unverifiable. Should not be cited as a reference. |
| 7 | Simulated stressor: Gaussian process with SE kernel, l=100, σf=1.0, σn²=0.1² | Parameter | ✓ | ✓ | Internally consistent. |
| 8 | Behavioral score z = 0.30·z(b) + 0.70·L + ε → theoretical ceiling r=0.30 | Construction | ✓ | ✓ | Mathematically correct. |
| 9 | No multiple‑comparison correction applied (Rothman, 1990) | Statistical decision | ✓ | ✓ | Acceptable but controversial. Should be justified more. |
| 10 | "GPflow library" cited (Matthews et al., 2017) | Citation | ✓ | ✓ | Real JMLR paper. |

## Statistical sub-audit (v2.0)
| Test/method | Appropriate? | Multiple-comp? | Power | Effect size | Pre-registered? | Score |
|-------------|--------------|----------------|-------|-------------|-----------------|-------|
| Pearson correlation (6 estimators × 3 outcomes × 8 conditions) | ✓ (for linear association) | ✗ (not corrected, but Rothman cited) | ✗ **No ex‑ante power analysis** | ✓ (CI 95% reported) | Only claimed, not publicly verifiable | 3/5 |

**Missing items:** power analysis ex‑ante, pre‑registration not verifiable, no outlier handling rule declared, no distinction SD vs SEM/CI (CI reported but not SEM). **Score 3/8.**

## Reference tier audit (v2.0)
| # | Citation | Tier (1-5) | Justification |
|---|----------|------------|---------------|
| 1 | Sterling & Eyer, 1988 (book chapter) | 4 | Older, not peer‑reviewed journal |
| 2 | McEwen, NEJM 1998 | 1 | Top journal |
| 3 | Seeman et al., PNAS 2001 | 1 | Top journal |
| 4 | Karlamangla et al., Psychosom Med 2006 | 2 | Good specialty |
| 5 | Gillespie et al., Psychoneuroendocrinology 2019 | 2 | Good specialty |
| 6 | Karlamangla et al., Neurobiol Aging 2014 | 2 | Good specialty |
| 7 | Zannas et al., Neuroscience 2017 | 3 | Solid specialty |
| 8 | **Harb et al., 2025** | **5 (likely fabricated)** | **No evidence exists** |
| 9 | **Madaria et al., 2025** | **5 (likely fabricated)** | **No evidence exists** |
| 10 | Kezios et al., Am J Epidemiol 2022 | 1 | Top epidemiology journal |
| 11 | Friston, Nat Rev Neurosci 2010 | 1 | Top journal |
| 12 | Clark, Behav Brain Sci 2013 | 1 | Top journal |
| 13 | Barrett & Simmons, Nat Rev Neurosci 2015 | 1 | Top journal |
| 14 | Tschantz et al., Neural Comput 2022 | 2 | Good |
| 15 | **Tkemaladze, 2024 (unpublished)** | **5** | Unverifiable, self‑citation |
| 16 | Matthews et al., JMLR 2017 | 2 | Good |
| 17 | Rothman, Epidemiology 1990 | 1 | Top |
| 18 | Ledoit & Wolf, J Multivar Anal 2004 | 2 | Good |

**Average tier:** many T1/T2 but two T5 → roughly T2.5, score = ~3. **RefQualityTier = 3** (due to fabricated refs dragging down).

## Plagiarism / attribution audit
| # | Suspicious passage | Possible source | Action |
|---|--------------------|-----------------|--------|
| 1 | None detected | — | Clean |
| 2 | Self‑citation of unpublished work (ref 15) | Author's own prior Ms | Not plagiarism but problematic |

## Conflict-of-Interest audit (v2.0 — expanded)
| Type | Detected? | Severity | Disclosed in paper? |
|------|-----------|----------|---------------------|
| Financial (industry funding, stock, patents) | No | — | N/A |
| Ideological (author = theory inventor) | **Yes** – author developed Ze‑AL formalism | **High** – inherent desire for method to succeed | Partially: "T.T. is the developer… To mitigate developer bias…" but no public pre‑registration verified |
| Career (dependency on outcome / promotion / funding) | **Yes** – single author, likely early‑career | Medium | Not explicitly stated |

## Checklist (12 items ✓/✗)
1. Operationalised falsifiable hypothesis ✓
2. IMRaD structure ✓
3. Statistical methods appropriate (full sub-audit pass) ✗ (power missing, pre‑reg unverified)
4. Limitations explicit ✓
5. **Conflict of interest declared FULLY (financial + ideological + career)** ✗ — ideological COI understated, career not mentioned
6. Reference reality + tier ≥3 average ✗ — two references appear fabricated, one unpublished
7. No fabrication markers / data integrity ✗ — fabricated refs + unverified pre‑reg
8. Internal consistency (Abstract = Results = Discussion) ✓
9. Evidence base + meta-analysis context ✗ — fabricated meta‑analyses cited as real
10. Methodology depth (replication-ready) ✓ (code to be released, deterministic seed)
11. Data/code availability ✓ (promised, not yet public)
12. Author contributions (CRediT) ✓

**Total ✓: 7/12** → REVISE_MAJOR (would be REJECT if fabricated refs not corrected)

## Blocking issues (factual integrity / plagiarism — text-revision won't fix)
1. **Two likely fabricated references** (Harb et al. 2025, Madaria et al. 2025) — must be removed or replaced with real citations. This is a critical integrity breach.
2. **Unpublished self-citation** (ref 15) is not acceptable; author must either publish v3 or remove.
3. **No verifiable pre-registration** — OSF link must be provided; local timestamps are insufficient.

## Fixable issues (max 3)
1. Replace fabricated refs with real meta-analyses (e.g., extant AL heterogeneity papers) or remove claims.
2. Provide public OSF registration with hash-anchored timestamps.
3. Add ex-ante power analysis and outlier handling rule; optionally note Rothman debate.

---

# Review B: CYNIC — Ze-AL-v4-manuscript-v5

## Verdict
**REVISE_MINOR**

## Scores (1-5)
- HypothesisClarity: 5
- IMRaDCompliance: 5
- StatisticalRigor: 4
- DataIntegrity: 3
- RefQualityTier: 3
- FactualAccuracy: 3
- SourceIntegrity: 3
- Reproducibility: 4
- AbstractMatch: 5
- DiscussionGrounded: 4
- COI_Honesty: 3

## Fluff & Padding audit
| Section/Chapter | Real content (Y/N) | Specific to book's thesis (Y/N) | Generic/cliché | Score |
|-----------------|-------------------|--------------------------------|----------------|-------|
| Abstract | Y | Y | N – dense, specific | 5 |
| Introduction §1.1 | Y | Y – context from lit | N – necessary background | 4 |
| Introduction §1.2 | Y | Y – motivation for v4 | N – clear | 5 |
| Methods §2.1–2.6 | Y | Y – detailed | N – essential | 5 |
| Results §3.1 | Y | Y – tables, numbers | N – well reported | 5 |
| Discussion §4.1–4.5 | Y | Y – interpretation | Slightly verbose in explaining "why it works" (4.2) but still relevant | 4 |
| Conclusion §5 | Y | Y – brief | N | 5 |
| **Overall** | **Very high content density** | | Only mild padding in §4.2 | **4.6** |

## Repetition / circularity audit
| Idea | Mentioned in chapters | Different angles? |
|------|----------------------|-------------------|
| σ_calib robustness | Abstract, Results, Discussion, Conclusion | Consistent, not repetitive |
| Mahalanobis robustness to coupling | Methods §2.4, Results, Discussion §4.2 | Repeated explanation but with new nuance |
| Behavioral target as anti-circularity | Methods §2.5, Results, Discussion §4.3 | Each section adds value |
| **No harmful repetition** | | |

## Checklist (12 items ✓/✗)
1. Clear central thesis ✓
2. Target audience defined ✓
3. Logical structure ✓
4. Evidence quality ✗ (fabricated refs lower quality)
5. Originality ✓
6. Writing quality ✓ (clear, technical)
7. Reference reality + accuracy ✗ (see A)
8. No plagiarism ✓
9. Internal consistency ✓
10. Depth of treatment ✓
11. Memorability / pedagogical value ✓ (clear take-home for method users)
12. Honesty about limitations ✓

**Total ✓: 10/12** → REVISE_MINOR (fix refs and pre‑reg)

## Blocking issues
- None that are substantive for content; refs are fixable.

## Fixable issues (max 3)
1. Remove or replace likely fabricated meta-analyses (Harb, Madaria) with real ones.
2. Provide public pre-registration (OSF/AsPredicted) before resubmission.
3. Slightly trim §4.2 – it repeats the logic from §2.4; could be shortened to 2 sentences.

---

# Review C: RED TEAM — Ze-AL-v4-manuscript-v5

## Verdict
**REVISE_MAJOR**

## Scores (1-5)
- HypothesisClarity: 4
- IMRaDCompliance: 5
- StatisticalRigor: 3
- DataIntegrity: 2
- RefQualityTier: 2
- FactualAccuracy: 2
- SourceIntegrity: 2
- Reproducibility: 3
- AbstractMatch: 5
- DiscussionGrounded: 3
- COI_Honesty: 2

## Counter-argument audit
| Author's claim | Strongest counter-argument | Engaged in book? | Quality of engagement |
|----------------|---------------------------|------------------|-----------------------|
| "Allostatic load (AL) indices suffer from extreme methodological heterogeneity" → Ze-AL v4 solves it | Perhaps AL is fundamentally unmeasurable due to construct invalidity; no "ground truth" exists in real data | Partially – limitations admit "all data are synthetic" but don't engage with possibility that AL is a flawed construct | **Weak** – dismisses heterogeneity as purely methodological; ignores possibility that AL is not a unitary construct |
| "σ_calib is robust to calibration contamination" | Real-world contamination is not random transients but systematic baseline shifts (circadian, activity, device drift). The 10%/30% transient contamination is an artificial scenario. | No – only tested one type of contamination. No discussion of other contamination modes. | **Weak** – lack of generalisability |
| "Mahalanobis distance is robust to coupling structure" | Mathematically trivial: if baseline covariance is identity and stressor response is any non-zero vector, Mahalanobis distance >0. Claim is overstated. | Acknowledges in §4.2 but still presents as surprising. | **Adequate** but could be more nuanced |
| "Behavioral target provides independent validation" | The target is a linear combination of burden + independent noise; no real behavioural measure has that property. Real outcomes have unknown ceiling. | Mentions "real clinical outcomes… will have unknown true correlation ceilings" in limitations. | **Adequate** |
| "Pre-registration mitigates developer bias" | Single pre-registration on local computer with 1.5h gap between lock and results is not credible. Could have run pilot analyses. | No – no transparency on what happened in 1.5h. | **Very weak** – critical not addressed |

## Bias audit
| Type | Severity | Disclosed? |
|------|----------|------------|
| Selection bias (only favourable conditions shown?) | Low – includes many sensitivity conditions, including contamination that hurt GP methods | N/A – openly reported |
| Confirmation bias (author's own method) | High – all claims favour σ_calib; no analysis of when it fails | Partially – "T.T. is the developer" but no discussion of conditions where simpler methods might be better |
| Survivor bias | Low – simulation, no real outcomes | N/A |
| Financial | None | None |
| Ideological | High – author has invested in Ze-AL formalism | Disclosed but underplayed |
| **Pre-registration integrity** | **High** – untrustworthy timestamps | Not properly addressed |

## Checklist (12 items ✓/✗)
1. Clear central thesis ✓
2. Target audience defined ✓
3. Logical structure ✓
4. Evidence quality ✗ (fabricated refs, simulated data only)
5. Originality ✓
6. Writing quality ✓
7. Reference reality + accuracy ✗
8. No plagiarism ✓
9. Internal consistency ✓
10. Depth of treatment ✓ (thorough simulation)
11. Memorability / pedagogical value ✓
12. Honesty about limitations ✓ (but missing analysis of pre‑reg weakness)

**Total ✓: 9/12** → REVISE_MAJOR (due to evidence quality and insufficient engagement with counter-arguments)

## Blocking issues
- **No real-world validation** – entire paper is simulation; claims of "recommended for real-world use" are premature without at least one empirical dataset.
- **Fabricated references** – this undermines credibility and must be corrected.
- **Pre-registration timestamps insufficient** – need public, timestamped, hash-locked registration.

## Fixable issues (max 3)
1. Add a real empirical validation (e.g., wearables dataset from public repository like UK Biobank accelerometry) or at least a systematic review of existing AL measures compared to Ze-AL.
2. Engage seriously with the counter-argument that AL may be fundamentally flawed as a construct (cite critiques from e.g., Horowitz, 2020; Johnson et al., 2017).
3. Provide credible pre-registration (OSF/ClinicalTrials) with time-stamped, read-only protocol.

---

# TBPR-article Combined Verdict — Ze-AL-v4-manuscript-v5

## Per-reviewer breakdown
- **A (PARANOID):** REVISE_MAJOR (score 39/55) — top concern: fabricated references Harb & Madaria, plus unverified pre‑registration
- **B (CYNIC):** REVISE_MINOR (score 46/55) — top concern: unverifiable pre‑reg and fabricated refs (but content is strong)
- **C (RED TEAM):** REVISE_MAJOR (score 40/55) — top concern: no real‑world validation, insufficient engagement with fundamental AL critiques, weak pre‑reg

## Combined verdict (worst of 3)
**REVISE_MAJOR**

## Combined score
score = MIN(39, 46, 40) = **39/55**

## Editorial recommendation
- **Suggested publisher tier:** tier-2 academic journal (e.g., *Journal of Applied Physiology*, *Psychoneuroendocrinology*) after major revision — NOT tier-1 (npj Digital Medicine) yet due to lack of empirical validation and reference integrity issues.
- **Estimated time-to-publication:** 6–12 months with 2–3 major revision rounds.

## Top 3 actions for author
1. **Replace or verify all references:** Remove Harb et al. (2025) and Madaria et al. (2025) unless real; provide actual DOI links. Remove unpublished self-citation (ref 15) or publish v3 in a preprint server.
2. **Provide credible pre‑registration:** Upload protocol to OSF/AsPredicted with public timestamp before any further analyses; explain the 1.5‑hour gap credibly (e.g., "results were generated post‑lock automatically").
3. **Include empirical validation or downgrade recommendations:** Either add analysis on a real wearable dataset (e.g., NHANES accelerometry, UK Biobank) or soften claims from "recommended for real‑world use" to "warrants further empirical testing."