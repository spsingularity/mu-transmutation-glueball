# μ-transmutation program — all four steps executed

**Script:** `src/mu_transmutation_steps.py` (steps 2–4). Step 1 is the structural analysis below.
Supersedes the one-loop `Λ_h ≈ 46 MeV` quoted in `MU_transmutation_assessment.md` §2 — the honest number is a
loop/scheme **band**, computed here.

---

## STEP 1 — the load-bearing question: does a confining sector give `ρ ∝ HΛ³`? [ANALYZED]

**The mechanism.** Urban–Zhitnitsky / Ohta: in a universe with a finite causal horizon, the topological
(Veneziano-ghost / contact-term) sector of a confining theory shifts the vacuum energy from its Minkowski
value by `Δρ ∝ H·χ_top/m_{η'}` — for a pure-glue hidden sector, `Δρ ~ H·χ_top/m_G ~ H·Λ³/6`. The linear-H,
boundary-sensitive form is exactly SEDE's law.

**Status in the literature:** contested. The ghost is gauge-variant and non-propagating; whether the
linear-in-H term survives careful regularization has been debated since ~2011 and is unsettled. Grade:
**[CONJECTURE]**, and it is now the single load-bearing assumption of the transmutation route.

**The new structural argument (why USC should take it seriously):** USC's own gap audit proved a no-go —
the volume-law horizon count *cannot* be the entanglement entropy of local QFT degrees of freedom
(Casini/Bekenstein: `S_vol/S_Bek = 1/H₀R`), forcing **nonlocal horizon dof** (node N1, "the single most
important remaining open problem"). The Veneziano-ghost/topological sector is precisely a **nonlocal,
non-propagating, boundary-sensitive contact term** — not local propagating QFT dof. So the UZ mechanism is
the *unique known microphysical candidate* that simultaneously (a) produces `ρ ∝ HΛ³` and (b) has exactly the
nonlocal character N1 demands. **The transmutation proposal is therefore not just an origin for μ — it is a
candidate identity for N1's mystery dof.** It also *evades* (does not violate) the corpus's
Casini-at-all-times theorem: that theorem excludes local processes producing the horizon *count*; the
contact-term vacuum energy is not local entanglement by construction. Consistent.

**The gate fits structurally:** UZ supplies the *ceiling* `μ³H`; SEDE's `u = f_sat ∈ [0,1]` is the activation
fraction (the foundations paper's own "occupancy" reading), driven by the Avrami structure-collapse coverage
in the injection frame. The two-part story (transmutation scale + gate timing) maps cleanly onto existing
corpus structure. Open sub-question: *what makes the contact term gateable* (respond to collapsed structure)
— this is the covariant-gate question the corpus already owns, unchanged.

**The concrete discharge path (new, falsifiable):** the UZ claim implies a finite-volume/boundary dependence
of the pure-glue vacuum energy,
> `ρ_vac(L) − ρ_vac(∞) ∝ χ_top/(m_G·L)`,
which is **lattice-measurable in principle** (pure SU(3), varying box size/boundary conditions; target
coefficient `χ_top/m_G`). This turns the contested-mechanism question into a computable yes/no — the sharpest
available way to settle step 1, and it requires no cosmology at all.

## STEP 2 — two-loop + threshold refinement [COMPUTED — the alignment blurs into a band]

Visible side (2-loop, `N_f 5→6` at `m_t`): `α_s(M_Pl) = 0.01886` (`1/α = 53.0`). Hidden `SU(3)`, `N_f=6`
massless, same coupling at `M_Pl`, run down:

| scheme / order | `Λ_h` |
|---|---|
| 1-loop pole | **27.6 MeV** |
| 2-loop pole | 105 MeV |
| 2-loop MS̄-form | 88 MeV |
| *(targets)* | bare `μ = 28.5` · UZ-corrected `6^{1/3}μ = 51.9` |

**Honest reading:** the striking single number ("46 MeV") dissolves into a **loop/scheme band ≈ 28–105 MeV**.
Notably, the 1-loop pole with the properly-run visible coupling lands *on μ itself* (27.6 vs 28.5 — 3%), while
2-loop overshoots the UZ target. Two conclusions: (i) **mirror unification with N_f=6 robustly lands in the
right decade with zero new continuous parameters** — a genuine order-of-magnitude success; (ii) the loop/scheme
spread (×2 each way) **cannot yet distinguish** the bare (`Λ=μ`) from the UZ-corrected (`Λ=6^{1/3}μ`)
coefficient — claiming the 12% alignment of the earlier note was premature. Sharpening requires a proper
scheme-fixed 3-loop + lattice-matched calculation (standard technology, well-posed).

## STEP 3 — D-5 acceptance test with b freed [RESTATED + MEASURABILITY QUANTIFIED]

With transmutation replacing the visible-QCD amplitude hypothesis, `b` is unpinned. The acceptance test
survives in sum-rule form: **`ζ_explicit(b) + ζ_reservoir = ρ_X f′/9H`** with `ζ_explicit = b·ρ_X f′/9H`.
Constraints on b: FPAB stability floor `b ≥ 0.164`; growth anchors `μ_∞(0) = 1.051 / 1.052 / 1.323` at
`b = 0.20 / 0.206 / 1.0`; current data (`μ₀ = 0.04±0.22`) allow the whole range; **forecast `σ(μ₀) ≈ 0.05`
(DR3+Euclid) separates b=0.2 from b=1 at ~5σ.** So `b` becomes a *measured* parameter, and once measured the
reservoir must supply exactly `(1−b)` of the dissipation — the acceptance target is now data-set, not QCD-set.
(A measured `b ≈ 0.206` would resurrect the visible-QCD hypothesis; any other value kills it — a clean
three-way discrimination: visible-QCD vs transmutation vs neither.)

## STEP 4 — the glueball boundary vs C1 [COMPUTED — with a bonus signature]

For `Λ_h = 52 MeV` (`m_G = 6Λ ≈ 312 MeV`), `Ω_G/Ω_DM ∝ ξ³`:

| regime | ξ = T_h/T_vis |
|---|---|
| invisible (`Ω_G < 0.1%` DM) | `ξ < 0.0006` |
| **absorbable subcomponent** (m_X shifts *within* ECCG's quoted 1.63–1.78 band) | `0.0006 < ξ < 0.0025` |
| **C1-breaking** (m_X pushed below 1.63) | `ξ > 0.0025` |
| overclosed | `ξ > 0.0058` |

Two findings beyond the boundary itself:
1. **The absorbable window is a real signature:** a future m_X measurement at the *low* end of the band
   (1.63–1.70 GeV) would be a hint of a glueball subcomponent — the transmutation sector becomes indirectly
   visible through the dark-matter mass, not through ΔN_eff.
2. **Glueball self-interaction: `σ/m ≈ 0.26 cm²/g`** — squarely in the SIDM-relevant range (dwarf cores).
   A subcomponent at the few-% level is self-interacting at astrophysically interesting strength, providing a
   *second* SIDM channel alongside the dark-sector completion's `φ`-mediated one.

---

# Program state after all steps

| step | outcome |
|---|---|
| 1 (UZ mechanism) | [CONJECTURE], contested — **but uniquely aligned with N1** (nonlocal contact term = the required non-QFT dof), evades Casini; **lattice-testable** via `ρ_vac(L) ∝ χ/(m_G L)` |
| 2 (mirror running) | zero-parameter success at decade level (band 28–105 MeV brackets both targets); loop/scheme spread blocks the coefficient test — needs 3-loop/lattice matching |
| 3 (b freed) | sum rule restated; b measurable at ~5σ by DR3+Euclid → three-way origin discrimination |
| 4 (glueball boundary) | `ξ < 0.0025` safe; absorbable window gives an **m_X-shift signature**; σ/m ≈ 0.26 cm²/g SIDM bonus |

**The transmutation route now stands as:** the leading μ-origin candidate, with one contested load-bearing
assumption (UZ) that has a concrete non-cosmological discharge path (lattice), one zero-parameter scale
success (mirror-unified N_f=6, right decade), and three indirect signatures (measured b, low-end m_X,
SIDM subcomponent) replacing the inverted ΔN_eff test.
