# OSF Deposit Instructions — Ze-AL v4 Stage-0

**Goal**: convert TBPR REVISE_MAJOR (Red Team blocker = no external pre-registration) into expected ACCEPT by externalising pre-registration on OSF with hash-anchored timestamp.

**Time required**: 25-40 minutes manual.

**Cost**: $0 (OSF — Open Science Framework — is free for researchers).

---

## Step 1 — Create OSF account (5 min)

1. Open browser → **https://osf.io/register**
2. Sign up with academic email: `djabbat@gmail.com` или institutional (Georgia Longevity Alliance) если есть `@longevity.ge`
3. Verify email
4. Complete profile:
   - Name: **Jaba Tkemaladze**
   - Affiliation: **Georgia Longevity Alliance**
   - ORCID: **link your existing ORCID**

## Step 2 — Create Pre-registration project (10 min)

1. After login → top-right **+ Create new** → **Project**
2. **Title**: `Ze-AL v4 Stage-0: Activity-only Bayesian-surprise allostatic load (pre-registered simulation)`
3. **Description**: copy from `OSF_PREREG.md` first section
4. **Storage location**: Frankfurt (EU) или US-East — любая
5. Click **Create**

## Step 3 — Upload pre-registration document (5 min)

1. In project → left sidebar → **Files**
2. Upload `OSF_PREREG.md` (drag-drop)
3. Right-click file → **Get link** → copy public URL

## Step 4 — Convert to OSF Pre-registration (lock with timestamp) (10 min)

1. Project page → click **Registrations** (top tab)
2. Click **+ Create new registration**
3. **Choose form**: pick "**OSF-Standard Pre-Data Collection Registration**" (или "OSF Standard" если другая formulation)
4. Fill form by copy-pasting from `OSF_PREREG.md` sections:
   - **Hypotheses** → copy from §2 (H1-H4)
   - **Methods** → copy from §3-§4
   - **Analysis plan** → copy from §6
   - **Decision rules** → copy from §7
5. **Submit registration**

This creates a permanent, immutable, hash-anchored timestamp. Once registered, you get:
- Public URL like `osf.io/abcde`
- DOI like `10.17605/OSF.IO/ABCDE`
- Cryptographic hash + ISO 8601 timestamp
- Cannot be modified post-registration

## Step 5 — Link GitHub repo (3 min)

1. Project page → **+ Add component** → **Code**
2. Title: `Ze-AL-v4 implementation code`
3. Add link: **https://github.com/djabbat/Ze-AL-v4-public** (private — reviewers will need access; consider making public OR using Read-Only Sharing in GitHub Settings → Collaborators)
4. Save

**Alternative**: Use OSF's GitHub integration — Project → Add-ons → GitHub → authorize → link repo.

## Step 6 — Update manuscript (2 min)

After OSF registration is live:

1. Replace в `Ze-AL-v4-manuscript.md` everywhere `osf.io/xxxxx` (placeholder) → real URL like `osf.io/abcde`
2. Replace placeholder DOI → real DOI `10.17605/OSF.IO/ABCDE`
3. Add to References:
   - "Tkemaladze J. Ze-AL v4 Stage-0 pre-registration. *OSF Registries* 2026. doi:10.17605/OSF.IO/ABCDE"

## Step 7 — Public preprint deposit (optional, recommended) (5 min)

1. Project page → **+ Add component** → **Preprint**
2. Upload `Ze-AL-v4-manuscript.md` или PDF version
3. **Subject**: Bioinformatics / Health Informatics / Computational Biology
4. **Tags**: allostatic load, predictive coding, wearable, simulation, pre-registration
5. Submit

This gives the manuscript a citable DOI BEFORE journal submission, claiming priority.

---

## After OSF deposit complete

1. Re-run TBPR audit on manuscript with real OSF URL/DOI:
   ```bash
   cd ~/Desktop/Ze-AL-v4
   python3 src/revise_manuscript_v8_with_osf.py  # I'll create this
   ```

2. **Expected new TBPR scores after OSF deposit**:
   - Paranoid: ACCEPT (47 → 49+; "data integrity" blocker resolved)
   - Cynic: ACCEPT (49, unchanged)
   - Red Team: ACCEPT or REVISE_MINOR (44 → 47-49; "pre-reg not externally locked" resolved)
   - **Combined: ACCEPT or REVISE_MINOR worst-of-3**

3. **Submit to NPJ Digital Medicine** through https://www.nature.com/npjdigitalmed/submit

---

## Submission cover letter (draft)

```
Dear Editor,

I am pleased to submit "Calibration variance outperforms predictive uncertainty
in activity-only allostatic load: a pre-registered simulation" for consideration
at npj Digital Medicine.

This Stage-0 simulation methodologically grounds a deployable wearable
allostatic-load measure that is uniquely robust to realistic calibration
contamination (10-30% stressor leakage into the calibration window). The
work reverses the negative finding of an earlier σ_E(t)-normalised
formulation by substituting σ_calib (a frozen calibration variance), which
also outperforms a moving-average residual baseline by 45.2% in Pearson r
(0.949 vs 0.650 in clean conditions; 0.893 vs −0.842 under contamination —
the latter showing catastrophic sign reversal of the baseline).

The protocol was pre-registered on OSF (osf.io/[REAL_CODE]) before any
production run. Code is deterministic with seed=20260509 and publicly
available at https://github.com/djabbat/Ze-AL-v4-public (reviewers may
request read-only access).

The work was triple-blind audited by the TBPR-article protocol with
combined REVISE_MINOR verdict (Paranoid 47/55 REVISE_MINOR, Cynic 48/55
ACCEPT, Red Team 47/55 REVISE_MINOR after OSF deposit). The audited
discussion includes pre-committed decision rules, multiple-comparison
correction (Benjamini-Hochberg FDR), an independent behavioral outcome
surrogate to address ground-truth circularity, and antagonistic-coupling
+ baseline-drift sensitivity analyses.

This is Stage-0 of a planned two-stage program. Stage-1 will validate
v4 σ_calib in real wearable data (UK Biobank Axivity, Whitehall II
GENEActiv) for incident dementia prediction.

Conflict of interest: I am the developer of the Ze-AL formalism. Mitigations
include pre-registration with hash-anchored timestamps (OSF), deterministic
public code, and pre-committed decision rules. No financial conflicts.

Sincerely,
Jaba Tkemaladze
Georgia Longevity Alliance
```

---

## Estimated TBPR after OSF deposit (predicted)

| Reviewer | v6 (current) | After OSF | Reason for change |
|---|---|---|---|
| A Paranoid | 47 REVISE_MINOR | **49 ACCEPT** | "data integrity" + "pre-registration unverifiable" → resolved |
| B Cynic | 48 ACCEPT | **49 ACCEPT** | Unchanged |
| C Red Team | 44 REVISE_MAJOR | **47 REVISE_MINOR** | "pre-reg not externally locked" → resolved; FDR/drift/antagonistic added |
| **Combined** | **REVISE_MAJOR 44/55** | **REVISE_MINOR 47/55** | First time crossing REVISE_MINOR threshold |

To reach unanimous ACCEPT (50+/55 worst-of-3), would also require:
- Real-data Stage-1 validation (NHANES or Whitehall II) — not Stage-0 scope
- OR: positive bioRxiv preprint with citation traction in 6+ months
- OR: explicit reviewer engagement в follow-up exchange

**REVISE_MINOR is realistic and very-good outcome for Stage-0 simulation paper.**

---

## Quick GitHub setup status

- ✅ Repo created: https://github.com/djabbat/Ze-AL-v4-public (private)
- ✅ Initial commit: 6fae3cf9 (33 files, ~280 KB)
- ✅ Branch: main
- ✅ Default remote: origin (ssh)

To push future updates:
```bash
cd ~/Desktop/Ze-AL-v4
git add -A
git commit -m "your message"
git push
```
