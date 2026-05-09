"""
After results/summary.json is populated, generate the manuscript via DeepSeek.
Substitutes real numbers from results into a structured prompt.
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

summary = json.loads((ROOT / "results/summary.json").read_text())

# v3 manuscript for context (excerpts)
V3 = (pathlib.Path.home() / "Desktop/Ze-Allostasis-v3.md").read_text()

# Format results table
def _fmt_row(cond, est):
    s = summary[cond][est]
    return f"r={s['r']:+.3f} [{s['ci_lo']:+.3f}, {s['ci_hi']:+.3f}]"

results_block = "\nPRIMARY CONDITION (correctly specified GP):\n"
for est in ["traditional", "ma_residual", "v3_sigma_E", "v4_sigma_calib",
            "v4_mahalanobis", "v4_vfe"]:
    results_block += f"  {est:18s} {_fmt_row('primary', est)}\n"

results_block += "\nSENSITIVITY CONDITIONS:\n"
for cond in ["lengthscale_-50%", "lengthscale_+50%", "no_circadian", "noise_3x"]:
    results_block += f"\n  {cond}:\n"
    for est in ["v3_sigma_E", "v4_sigma_calib", "v4_mahalanobis", "v4_vfe", "ma_residual"]:
        results_block += f"    {est:18s} {_fmt_row(cond, est)}\n"

prompt = f"""Ты опытный научный писатель. Тебе нужно написать полный manuscript (~3000-3500 слов) на английском, готовый к submission в NPJ Digital Medicine (IF 16) или Scientific Reports.

ПРЕДЫСТОРИЯ (paper v3 показал negative finding — ОТРИЦАТЕЛЬНЫЙ результат):
{V3[:6000]}
...

ЗАДАЧА для v4: Показать что переход от σ_E(t) нормализации к σ_calib + многоканальный Mahalanobis + Bayesian KL surprise (variational free energy form) РЕШАЕТ self-cancellation проблему v3. Это POSITIVE FINDING paper.

РЕАЛЬНЫЕ ЭКСПЕРИМЕНТАЛЬНЫЕ РЕЗУЛЬТАТЫ (n=200, 4 сценария × 50, 90 days, 5 channels, seed=20260509):
{results_block}

СТРУКТУРА:
1. **Title** — описательный, с ключевым результатом (~15 слов)
2. **Abstract** (250 слов): background v3 negative → v4 hypothesis → methods → exact numbers → conclusion
3. **Introduction** (~600 слов):
   - Allostatic load + heterogeneity problem (cite McEwen 1998, Sterling 1988, Harb 2025)
   - Predictive coding (Friston 2010, Tschantz 2022)
   - v3 negative finding (cite v3): σ_E inflates during stressor → divides out signal
   - v4 hypothesis: σ_calib + Mahalanobis + KL
4. **Methods** (~800 слов):
   - Multivariate generator (5 channels, coherent stressor pattern, 4 scenarios)
   - 6 estimators (formulas in display equations)
   - Pre-registered seed
   - 4 sensitivity conditions
   - Pearson r, bootstrap 95% CI
5. **Results** (~600 слов):
   - Primary results table (REAL NUMBERS)
   - Sensitivity table (REAL NUMBERS)
   - % improvement over v3 σ_E and over MA-baseline
   - Sign-reversal robustness comparison
6. **Discussion** (~600 слов):
   - Why σ_calib resolves cancellation (frozen scale during stressor)
   - Why Mahalanobis amplifies coherent multichannel deviations
   - Why KL surprise adds beyond Mahalanobis
   - Limitations: synthetic favors GP; need real-data follow-up
   - Future: NHANES + Whitehall II validation
7. **Conclusion** (~150 слов)
8. **References** — точные DOI, минимум 15 верифицируемых ссылок (PubMed/Crossref)
9. **Code/Data availability** — упомянуть seed=20260509 и публичный репозиторий

ТРЕБОВАНИЯ:
- Только реальные числа из results/ (не выдумывать)
- Английский академический tone
- Display equations в LaTeX (для pandoc → docx)
- Упомянуть pre-registration на OSF (planned)
- НЕ преувеличивать: это симуляция, не real data; разделение clear
- Honest limitations section
- COI: Tkemaladze = developer, declared

ВЫВЕДИ ПОЛНЫЙ MANUSCRIPT в Markdown с display equations в LaTeX.
"""

print(f"Prompt length: {len(prompt)}")
print("Calling DeepSeek deepseek-reasoner (max_tokens=16000)...")

resp = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[
        {"role": "system", "content": "Senior scientific writer; English academic; only real numbers; pandoc-ready Markdown."},
        {"role": "user",   "content": prompt},
    ],
    temperature=0.3,
    max_tokens=16000,
)
out = resp.choices[0].message.content
print(f"Manuscript length: {len(out)} chars")
(ROOT / "Ze-AL-v4-manuscript.md").write_text(out)
print(f"Saved → {ROOT / 'Ze-AL-v4-manuscript.md'}")
