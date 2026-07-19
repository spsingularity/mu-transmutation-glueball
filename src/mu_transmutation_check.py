#!/usr/bin/env python3
"""
Verify and stress-test the dimensional-transmutation origin of mu = 28.5 MeV
(hidden confining sector), including two sharpenings and the cosmological bounds.

 (1) Coupling check: pure hidden SU(3) YM confining at Lambda_h.
     One-loop: 1/alpha_h(M_Pl) = (b0/2pi) ln(M_Pl/Lambda_h),  b0 = 11 (pure YM).
 (2) Sensitivity honesty: d ln Lambda / d ln alpha = ln(M_Pl/Lambda).
 (3) SHARPENING A -- mirror unification: if alpha_h(M_Pl) = alpha_s(M_Pl) (visible
     QCD coupling at Planck), what N_f makes Lambda_h ~ 30-50 MeV?
 (4) SHARPENING B -- the H-linear mechanism (Urban-Zhitnitsky/Ohta transplanted):
     rho ~ H * chi_top/m_G ~ H * Lambda_h^3/6  ->  required Lambda_h = 6^{1/3} mu.
 (5) COSMOLOGY: Delta N_eff of the hidden gluons and the glueball relic bound.
"""
import numpy as np

MPl = 1.22091e19       # GeV
mu  = 0.0285493        # GeV (SEDE closure)

# ---------------- (1) pure-YM coupling ----------------
b0_pure = 11.0
L = np.log(MPl/mu)
inv_alpha = b0_pure/(2*np.pi)*L
print("="*78)
print("(1) Pure hidden SU(3) YM confining at mu = 28.55 MeV")
print("="*78)
print(f"    ln(M_Pl/mu) = {L:.2f}   ->  1/alpha_h(M_Pl) = (11/2pi)*{L:.1f} = {inv_alpha:.1f}")
print(f"    alpha_h(M_Pl) = {1/inv_alpha:.5f}  (claim: ~1/83 ~ 0.012)  -> CHECKS OUT")
print(f"    compare SM at M_Pl: 1/alpha_1,2,3 ~ 52-59, 47, 52  -> same ballpark, NOT unified")

# ---------------- (2) sensitivity ----------------
print()
print("(2) Sensitivity: dLambda/Lambda = ln(M_Pl/Lambda) * dalpha/alpha "
      f"= {L:.1f} * (dalpha/alpha)")
print(f"    -> a 1% specification of alpha_h fixes mu to ~{L:.0f}% (factor ~1.6).")
print(f"    -> to fix mu to 1% needs alpha_h to {1/L*100:.3f}%.")
print(f"    The 10^60 tuning in rho does become a ~1% coupling spec -- but the '1%")
print(f"    specification of alpha' pins mu only to a factor ~1.6, NOT to 1%. Honest form:")
print(f"    transmutation naturalizes the SCALE; the precise value still selects alpha_h")
print(f"    at the 0.02% level (mild, log-natural, but a selection).")

# ---------------- (3) mirror unification ----------------
print()
print("(3) SHARPENING A: demand alpha_h(M_Pl) = alpha_s(M_Pl)")
alpha_s_MZ, MZ = 0.1181, 91.19
inv_a3_MPl = 1/alpha_s_MZ + 7/(2*np.pi)*np.log(MPl/MZ)   # b0=7 above top (crude 1-loop)
print(f"    visible QCD: 1/alpha_s(M_Pl) ~ {inv_a3_MPl:.1f}")
for Nf in [0, 3, 6, 7]:
    b0 = 11 - 2*Nf/3
    Lam = MPl*np.exp(-2*np.pi*inv_a3_MPl/b0)
    print(f"    hidden SU(3), N_f={Nf}: b0={b0:.2f}  ->  Lambda_h = {Lam*1e3:.3g} MeV")
print(f"    -> N_f = 6 light flavors with a PLANCK-UNIFIED coupling confines at ~48 MeV --")
print(f"       within a factor 1.7 of mu (one-loop, no thresholds). A 'mirror QCD with")
print(f"       alpha_h(M_Pl)=alpha_s(M_Pl) and 6 massless flavors' is the sharpest version:")
print(f"       ZERO new dimensionless inputs (coupling inherited, N_f discrete).")

# ---------------- (4) the H-linear mechanism coefficient ----------------
print()
print("(4) SHARPENING B: the rho ~ H*Lambda^3 mechanism (UZ ghost / topological")
print("    susceptibility, transplanted to the hidden sector):")
print("    rho = H * chi_top/m_G,  chi_top ~ Lambda^4, m_G ~ 6 Lambda (lattice 0++)")
print("    ->  mu^3 = Lambda_h^3/6  ->  Lambda_h = 6^(1/3) mu = "
      f"{6**(1/3)*mu*1e3:.1f} MeV")
print(f"    -> the UZ-coefficient-corrected requirement ({6**(1/3)*mu*1e3:.0f} MeV) sits within")
print(f"       ~10% of the mirror-unified N_f=6 value (~48 MeV). Suggestive alignment --")
print(f"       but the UZ/Veneziano-ghost mechanism is CONTESTED in the literature; grade")
print(f"       the alignment [ESTIMATE], the mechanism [CONJECTURE].")

# ---------------- (5) cosmological bounds ----------------
print()
print("(5) Cosmology: how visible can this sector be?")
# Delta N_eff of 16 thermalized hidden-gluon dof decoupling at the Planck/reheat scale
g_h = 16.0
xi = (3.91/106.75)**(1/3)             # T_h/T_gamma today-side if decoupled above EW
Tnu_over_Tg = (4/11)**(1/3)
dNeff_full = (4/7)*g_h*(xi/Tnu_over_Tg)**4
print(f"    (a) if ever fully thermalized with the SM then decoupled early:")
print(f"        T_h/T_gamma = {xi:.3f}  ->  Delta N_eff = {dNeff_full:.2f}   (Planck bound ~0.30)")
print(f"        -> ALREADY (marginally) EXCLUDED. The sector must be reheated below SM temp.")
# glueball relic overclosure
m_G = 6*mu                            # ~ 0.17 GeV
gstar_conf = 61.75                    # g*s(visible) at T_gamma ~ 90 MeV
n_over_s = 0.2777*g_h/gstar_conf      # relativistic gluon number / visible entropy, xi=1
red_32 = 10.0                         # crude 3->2 reduction factor
rho_DM_over_s = 4.4e-10               # GeV (observed)
# rho_G/s = m_G * (n/s) * xi^3 / red
xi_max = (rho_DM_over_s/(m_G*n_over_s/red_32))**(1/3)
print(f"    (b) glueball relic (m_G ~ 6 Lambda ~ {m_G*1e3:.0f} MeV, 3->2 freeze-out, crude):")
print(f"        rho_G/s ~ m_G*(0.072/10)*xi^3  ->  overcloses unless xi <~ {xi_max:.3f}")
dNeff_at_ximax = (4/7)*g_h*(xi_max/Tnu_over_Tg)**4
print(f"        at xi = xi_max: Delta N_eff = {dNeff_at_ximax:.1e}  -> INVISIBLE to CMB-S4")
print(f"    => the viable sector is COLD (xi <~ {xi_max:.2f}): the 'testable via Delta N_eff'")
print(f"       claim INVERTS -- Delta N_eff is invisible in the allowed region; the real")
print(f"       tests are (i) the DE observables themselves (H-linearity, growth lock),")
print(f"       (ii) the tuned corner xi ~ {xi_max:.3f} where glueballs are a DM SUBCOMPONENT")
print(f"       (clashes with ECCG's pure-ADM dark matter -- a live internal tension), and")
print(f"       (iii) lattice/theory: does a confining sector actually produce rho ~ H*Lambda^3?")
