# μ from dimensional transmutation — assessment, two sharpenings, one inversion

> **Update (steps executed — see `MU_transmutation_steps_results.md`):** the §2 one-loop `Λ_h ≈ 46 MeV` is
> superseded by the loop/scheme **band 28–105 MeV** (1-loop pole lands on μ itself at 27.6; 2-loop at 88–105);
> the §3 "12% alignment" was premature — the band brackets both targets but can't yet distinguish them. The UZ
> mechanism gained a structural argument (it is the unique candidate matching N1's nonlocal-dof requirement)
> and a lattice discharge path; the glueball boundary is `ξ < 0.0025` with an m_X-shift signature.

**Script:** `src/mu_transmutation_check.py`. Assesses the proposal: μ = 28.5 MeV as the confinement
scale of a hidden sector (`α_h(M_Pl) ≈ 1/83`), with the growth gate handling the relocated "why now."

## Verdict up front
**Adopted as the leading candidate origin for μ** — it is the first proposal that attacks SEDE's
self-declared deepest open problem (v0.3 completion standard #5) in the corpus's own native mechanism
(transmutation is how ECCG makes Λ_H). The core claim verifies exactly; the sharpened version below is
better than the original; the testability claim inverts; and it creates one new internal tension.

## 1. Verification [DERIVED]
- Pure hidden SU(3) YM confining at 28.55 MeV needs `1/α_h(M_Pl) = (11/2π)·ln(M_Pl/μ) = 83.2` →
  `α_h = 0.0120`. **Checks out exactly.** Same ballpark as SM couplings at M_Pl (1/47–59), not equal.
- The 10⁶⁰ tuning in ρ genuinely becomes a log-natural coupling spec. **Honesty correction:** a 1% spec of
  α_h fixes μ only to ~48% (factor 1.6), since `dlnΛ/dlnα = ln(M_Pl/Λ) = 47.5`; pinning μ to 1% needs α_h to
  0.02%. So: transmutation *naturalizes the scale*; the precise value remains a (mild, log-level) selection.

## 2. Sharpening A — mirror unification: zero new continuous parameters
Instead of postulating a new coupling, **demand `α_h(M_Pl) = α_s(M_Pl)`** (the visible QCD value, ≈1/52.4).
Then the confinement scale is fixed by the discrete flavor content alone:

| hidden SU(3) content | Λ_h |
|---|---|
| N_f = 0 | 1.2×10⁶ MeV |
| N_f = 3 | 1.6×10³ MeV |
| **N_f = 6** | **46 MeV** |
| N_f = 7 | 0.3 MeV |

**A mirror QCD with six light flavors and a Planck-unified coupling confines at ≈46 MeV** — within a factor
1.7 of μ at one loop, with *no new dimensionless inputs* (coupling inherited, N_f discrete). This upgrades
the proposal from "a natural coupling" to "no new coupling at all."

## 3. Sharpening B — the H-linearity coefficient closes the gap
Transmutation gives the *scale*; SEDE needs the *law* `ρ_X = μ³H`. The corpus's own cited mechanism
(Urban–Zhitnitsky/Ohta topological-susceptibility vacuum energy), transplanted to the hidden sector, gives
`ρ ~ H·χ_top/m_G ~ H·Λ_h³/6` (lattice `m_G ≈ 6Λ`). So the *required* confinement scale is not μ but

> `Λ_h = 6^{1/3}·μ = 52 MeV` — **within ~12% of the mirror-unified N_f=6 value (46 MeV).**

Two independent O(1)-free constructions (Planck-unified running down; UZ coefficient up from the observed μ)
land on the same ~50 MeV. Suggestive. **Grades:** the alignment [ESTIMATE]; the UZ/Veneziano-ghost mechanism
itself is *contested in the literature* — [CONJECTURE]. This is also where the proposal competes with the
corpus's existing `b_QCD = 0.2062` visible-QCD hypothesis: **mutually exclusive origins, distinguishable** —
the visible-QCD origin ties μ to `f_π, m_π, m_η'` and *predicts b*; the hidden origin frees b and predicts a
hidden spectrum. Only one can be right.

## 4. The inversion — ΔN_eff is NOT the test (the viable sector is invisible)
- If the hidden gluons were ever SM-thermalized: `ΔN_eff = 0.43` — **already (marginally) excluded** by
  Planck. So the sector must be reheated cold.
- The binding constraint is **glueball overclosure** (`m_G ≈ 170 MeV`, 3→2 freeze-out): requires
  `ξ = T_h/T_vis ≲ 0.007`. At that ceiling, `ΔN_eff ≈ 10⁻⁷` — **invisible to CMB-S4 forever.**
- **So the testability claim inverts:** in its allowed region the sector has no kinetic cosmological
  signature. The actual tests are (i) the DE observables themselves (the H-linear law, the growth lock, Δ=1
  — unchanged), (ii) *theory/lattice*: does a confining sector really produce `ρ ∝ HΛ³`? (the contested UZ
  step — now the single load-bearing question), and (iii) the tuned corner `ξ ≈ 0.007`, where glueballs are a
  **DM subcomponent** — which **clashes with ECCG's pure-ADM dark matter** (`Ω_DM/Ω_b = 5.36` fully supplied
  by the 1.78 GeV relic). A new, live internal tension: if the transmutation sector is warm enough to matter,
  it breaks C1; if cold, it is invisible except through the vacuum channel.

## 5. What it buys the union (and what it doesn't)
- **Buys:** μ dynamically generated (deepest hole addressed); the "why now" relocation is exactly the shape
  the corpus already validated (Candidate-E closure: timing is co-controlled by the gate — `f_sat` handles
  onset; transmutation handles scale). Via B.2's identity `μ³ = (6πΩ_X0/u₀)a₀M_P²`, a derived μ **also fixes
  the MOND scale a₀** — the transmutation chain would then run `α_s(M_Pl) → Λ_h → μ → a₀`, connecting Planck
  coupling to galaxy rotation curves in four steps.
- **Doesn't buy:** the H-linearity mechanism (still the contested UZ step — this is now *the* question);
  falsifiability in the dark-radiation channel (inverted, §4); and it adds a **third** hidden sector to the
  union (ECCG's SU(3)_H at 6×10¹², the V/φ dark force, now mirror-QCD at 50 MeV) — a real proliferation cost
  against USC's economy claim, unless the mirror sector can be related to existing structure.

## 6. Concrete next steps
1. **The load-bearing check:** settle whether `ρ ∝ H·χ_top/m_G` survives scrutiny (the UZ debate) — ideally
   as a lattice-computable statement about the hidden sector's boundary-sensitive vacuum energy. Everything
   else hangs on this.
2. **Two-loop + threshold refinement of Sharpening A:** does mirror-unified N_f=6 move from 46 toward 52 MeV
   (the UZ-corrected target) or away? A ±10% calculation, decisive for the alignment.
3. **The b question:** if transmutation replaces the visible-QCD amplitude hypothesis, `b` returns to a free
   (or FPAB-stability-selected) parameter — rerun the D-5 acceptance test with b free.
4. **Glueball-subcomponent corner:** compute the exact `ξ` at which glueballs spoil C1/Ω_DM — the boundary
   between "invisible" and "excluded" for the mirror sector.
