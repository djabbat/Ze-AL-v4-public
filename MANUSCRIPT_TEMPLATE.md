# Ze-AL v4 Manuscript Template

This is the input to DeepSeek for manuscript drafting AFTER results are in.
The template defines structure; DeepSeek will fill with real numbers.

## Title (working)
**Activity-only Bayesian-surprise allostatic load: closed-form correction of the σ_E self-cancellation problem in predictive-uncertainty wearable biomarkers**

## Target journals
1. NPJ Digital Medicine (IF 16) — primary
2. PLOS ONE (IF 4) — fallback

## Manuscript skeleton

### Abstract (250 words)
- Background: traditional AL heterogeneous (I²>90%); v3 σ_E formulation showed sign-reversal under misspecification
- Methods: pre-registered simulation, n=200, 4 scenarios × 50, 90-day multichannel
- Results: v4 Mahalanobis r={r_v4_mahal_primary}, v4 VFE r={r_v4_vfe_primary}, vs MA-baseline r={r_ma_primary}, vs v3 σ_E r={r_v3_primary}
- Sensitivity: v4 Mahalanobis stays positive under all 4 misspecification conditions vs v3 sign-reversal under length-scale −50%
- Conclusion: σ_calib normalization + multivariate Mahalanobis + KL surprise resolves the v3 self-cancellation; provides activity-only formalism deployable on devices without HR sensor

### 1. Introduction (~600 words)
- Allostatic load: McEwen, Sterling
- Predictive coding: Friston, Tschantz
- v3 negative finding (cite v3): σ_E inflates during stressor → divides out signal
- Hypothesis: σ_calib (frozen scale) + multichannel Mahalanobis + KL surprise

### 2. Methods (~800 words)
- Multivariate generator: 5 channels, coherent stressor pattern, 4 scenarios
- 6 estimators (traditional, MA-residual, v3, v4-σcalib, v4-Mahalanobis, v4-VFE)
- Pre-registered seed = 20260509
- Sensitivity: 4 misspecification conditions
- Pearson r, bootstrap CI

### 3. Results (~600 words)
- Primary table (real numbers from results/summary.json)
- Sensitivity table (real numbers)
- Improvement %s vs v3 baseline
- Sign-reversal robustness

### 4. Discussion (~600 words)
- Why σ_calib resolves cancellation (frozen scale during stressor)
- Why Mahalanobis amplifies coherent multichannel deviations
- Why KL surprise adds beyond Mahalanobis (cost of belief update)
- Limitations: synthetic data favors GP-based methods (acknowledged)
- Future work: real-data validation (NHANES, Whitehall II)

### 5. Conclusion (~150 words)

### Pre-registration / Data availability
- OSF protocol pre-locked
- Code public on GitHub
- All deterministic with seed=20260509
