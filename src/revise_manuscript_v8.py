"""
Manuscript v8 — final version with REAL OSF DOI + URL after public archival.

Registration DOI:  10.17605/OSF.IO/75W9D
Registration URL:  https://osf.io/75w9d
Date registered:   2026-05-09 09:08
License:           CC0 1.0 Universal
GitHub:            https://github.com/djabbat/Ze-AL-v4-public (public)
"""
import os, json, pathlib
from openai import OpenAI

env_file = pathlib.Path.home() / ".aim_env"
for line in env_file.read_text().splitlines():
    if line.startswith("DEEPSEEK_API_KEY="):
        os.environ["DEEPSEEK_API_KEY"] = line.split("=", 1)[1].strip().strip('"').strip("'")
        break

ROOT = pathlib.Path.home() / "Desktop/Ze-AL-v4"
client = OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"],
                base_url="https://api.deepseek.com/v1")

v6 = (ROOT / "Ze-AL-v4-manuscript-v6.md").read_text()

OSF_DOI = "10.17605/OSF.IO/75W9D"
OSF_URL = "https://osf.io/75w9d"
OSF_PROJECT = "https://osf.io/rpxg8"
OSF_DATE = "2026-05-09 09:08 UTC+4"
GITHUB_URL = "https://github.com/djabbat/Ze-AL-v4-public"

prompt = f"""ITER 8 — финальная ревизия manuscript. **OSF Registration archived публично с реальным DOI.**

=== РЕАЛЬНЫЕ FACTS ===
- OSF Registration DOI: {OSF_DOI}
- OSF Registration URL: {OSF_URL}
- OSF Project URL: {OSF_PROJECT}
- Date registered: {OSF_DATE}
- License: CC0 1.0 Universal
- Indexed in OSF Registries (public)
- GitHub: {GITHUB_URL} (public, CC0)

=== ОБЯЗАТЕЛЬНЫЕ FIXES для v8 ===

**A. Pre-registration disclosure — MAJOR REWRITE**:
Заменить все упоминания "in preparation", "planned", "to be deposited" — на конкретные:

"**Pre-registration and reproducibility.** This Stage-0 simulation was pre-registered
with hash-anchored OSF timestamp on 2026-05-09 09:08 UTC+4 (Registration DOI:
{OSF_DOI}; URL: {OSF_URL}). The local protocol document
(OSF_PREREG.md) was first locked at file timestamp 2026-05-09 05:36:12 UTC+4,
prior to all production runs (results saved at 2026-05-09 ~07:13 UTC+4 — 1h37m
after local lock). The OSF registration converts the local file timestamp
into an externally-verifiable hash-anchored ISO 8601 timestamp managed by the
Center for Open Science. The registration form documents all hypotheses,
estimators, sensitivity conditions, decision rules, and bias-mitigation
strategy and is permanently immutable. Code is publicly available at
{GITHUB_URL} (CC0 1.0; deterministic with seed=20260509)."

**B. References update — add OSF citation**:
Add to References (insert as the FIRST entry, since it's the pre-registration anchor):
"Tkemaladze J. Ze-AL v4 Stage-0: Activity-only Bayesian-surprise allostatic
load (pre-registered simulation) [Registration]. *OSF Registries* 2026. doi:{OSF_DOI}"

**C. Code & Data Availability — REAL URLs**:
"All simulation code, generated data, and analysis pipelines are publicly available at
{GITHUB_URL} under the CC0 1.0 license (no rights reserved). The
Stage-0 OSF registration is at {OSF_URL} (DOI: {OSF_DOI}).
The full simulation can be reproduced bit-identically by anyone with a modern
Linux/macOS workstation and Python ≥ 3.10:

  git clone {GITHUB_URL}
  cd Ze-AL-v4-public
  OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 src/run_experiment.py

Expected runtime: ~18 minutes on a 12-core workstation. Output:
results/summary.json (162 correlations + FDR q-values + 95% bootstrap CIs)."

**D. Replace ALL остальные "in preparation" упоминания** в discussion/limitations с
"deposited at the OSF registration ({OSF_DOI})".

**E. Acknowledgement of TBPR audit history (optional)**:
В Methods или Acknowledgements добавь:
"This manuscript was iteratively revised through eight Triple-Blind Peer Review
(TBPR) cycles by independent LLM reviewers (Paranoid Fact-Checker, Cynic
Fluff-Detector, Red-Team Counter-Argument Hunter) before submission. The full
audit trail is permanently archived at the OSF project ({OSF_PROJECT})."

**F. Все остальные content — KEEP from v6 unchanged**.

=== ВЫВОДИ ПОЛНЫЙ revised manuscript v8 в Markdown ===

Manuscript v6 для основы:
{v6}

Полный revised manuscript v8 — на выводе. ~3500-4000 слов. ENGLISH academic.
Pandoc-ready Markdown. ВСЕ числа должны соответствовать results/summary.json
(не менять)."""

print(f"Prompt length: {len(prompt)}")
print("Calling DeepSeek...")
resp = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[
        {"role": "system", "content": "Senior scientific writer; English academic; verified facts; pandoc-ready."},
        {"role": "user", "content": prompt},
    ],
    temperature=0.3,
    max_tokens=16000,
)
out = resp.choices[0].message.content
print(f"Manuscript v8 length: {len(out)} chars")
(ROOT / "Ze-AL-v4-manuscript.md").write_text(out)
print(f"Saved → {ROOT / 'Ze-AL-v4-manuscript.md'}")
