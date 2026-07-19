# Glueball-SIDM seeding of the JWST Little Red Dots — assessment (2026-07-17)

**Script:** `src/glueball_lrd_seeding.py` (σ(M,z) from the real classy linear P(k),
Sheth–Tormen HMF, NFW gravothermal time `t_c = (150/0.75)/(ρ_s·(σ/m)·v_s)`, lognormal
concentration tail c̄=4.5, σ_lnc=0.35, collapse window z_form∈{10–15} → z=7).

**Question:** USC horn (iii) fixes a velocity-independent SIDM cross-section
`σ/m ≈ 0.47 / 0.09 / 0.01 cm²/g` at `Λ_h = 30 / 52 / 105 MeV`. SIDM gravothermal collapse is a
heavy-seed channel for the LRD overmassive black holes (`M_BH ~ 10⁶–10⁸ M⊙` at z~5–9,
`n_LRD ~ 10⁻⁵ Mpc⁻³`). Can the glueball do it?

## Result table (best formation redshift z_f=15, window ≈ 495 Myr to z=7)

| Λ_h | σ/m | DM-only n_seed/n_LRD | baryon-boosted ×30 n_seed/n_LRD | seed mass |
|---|---|---|---|---|
| 30 MeV | 0.47 | 8×10⁻⁴ (needs c>30) | **5×10²** (overshoot; c>10 suffices) | ~5×10⁶–10⁷ M⊙ |
| **52 MeV (UZ)** | 0.09 | 2×10⁻⁸ | **2.5 — lands on target** | **~7×10⁶ M⊙ — in the LRD range** |
| 105 MeV | 0.01 | 0 (no halo at any c≤40) | 7×10⁻⁵ | — |

Reference single-halo numbers (z_f=10, M=10¹⁰): median-concentration t_c = 90/470/4200 Gyr for
Λ_h=30/52/105 — **DM-only collapse is hopeless at the median for every Λ_h**; everything lives in
the high-concentration tail and/or the baryonic acceleration.

## Findings

1. **DM-only: the glueball cannot seed the LRDs.** Even the most-interacting case (Λ_h=30) falls
   3 orders of magnitude short and needs c>30 (a >5σ concentration). This half is *robust* — it
   fails at maximum optimism on every other axis.
2. **With baryon-accelerated collapse (×30, the Feng/Yu-type bracket), the UZ value Λ_h=52 MeV
   lands within a factor ~2.5 of the LRD abundance, with seed masses ~7×10⁶ M⊙ — inside the
   observed LRD black-hole range.** Λ_h=30 overshoots ×540 (absorbable by an LRD duty cycle of
   ~10⁻²–10⁻³ — every massive galaxy hosts an SMBH, so over-seeding is not per se excluded);
   Λ_h=105 fails by 10⁴ even boosted.
3. **The pincer (the useful structural result).** Combined with the pre-registered cluster-SIDM
   discriminator (`σ/m ≲ 0.1–0.5` from clusters, probing the low-Λ_h end):
   - clusters press from **above**: σ/m ≲ 0.1–0.5 → disfavors Λ_h ≈ 30;
   - LRD seeding (if SIDM-driven) presses from **below**: σ/m ≳ 0.1 (with baryons) → excludes Λ_h ≈ 105;
   - **the two-sided squeeze selects Λ_h ≈ 52 MeV — exactly the UZ-corrected transmutation value
     that the SEDE H-linear mechanism independently wants.** A three-way convergence (UZ
     coefficient ↔ cluster bound ↔ LRD seeding) that the theory did not tune for.
4. **Falsifier content (conditional, honest):** *if* LRD follow-up establishes that the seeds
   require SIDM gravothermal collapse (i.e. the astrophysical channels — BH*/supermassive-star,
   super-Eddington bursts, DCBH — are excluded), then within USC: Λ_h=105 MeV is dead as the DM
   scale, and the surviving window is Λ_h ≈ 30–52 MeV with baryon-boosted collapse. Conversely, if
   LRDs are resolved astrophysically (the current mainstream), this channel goes quiet and nothing
   in USC changes.

## Honest error budget (do not oversell)

- **Exponential sensitivity.** n_seed traverses ~6 orders of magnitude between the DM-only and
  ×30-boosted brackets; the boost factor, the collapse-time calibration C≈0.75, c̄, σ_lnc, and the
  2% seed fraction are each O(1)-uncertain, and the abundance responds exponentially through the
  concentration tail. The Λ_h=52 "lands on target" is therefore a **viability statement, not a
  prediction** — the honest claim is "within the plausible baryon-boost bracket, Λ_h≈52 crosses
  n_LRD while 105 cannot and 30 over-seeds."
- The lognormal concentration tail is trusted out to ~4σ, where it is not sim-calibrated.
- t_c conventions differ at O(1) between groups (this uses the Essig+19 calibration).
- Velocity-independence is a *simplifying strength* here (no extra σ(v) freedom), but it also means
  the same σ/m must satisfy dwarf/cluster constraints simultaneously — the pincer cuts both ways.

## Status

- New conditional discriminator added to the glueball horn; strengthens the case that **Λ_h ≈ 52
  MeV (UZ) is the distinguished point** of the transmutation branch.
- Suggested pre-registration append (P-LRD, conditional): "If LRD seeds are shown to require SIDM
  gravothermal collapse, USC horn (iii) survives only with Λ_h ≈ 30–52 MeV + baryon-boosted
  collapse; Λ_h ≈ 105 MeV is excluded as the seeder." Not yet appended — the trigger condition
  (astrophysical channels excluded) is not currently met and may never be.
