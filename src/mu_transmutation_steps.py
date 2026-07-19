#!/usr/bin/env python3
"""
Executes steps 2-4 of the mu-transmutation program (step 1 is the structural note).

 STEP 2: two-loop + threshold refinement of the mirror-unified N_f=6 running.
         Visible: alpha_s(MZ)=0.1181 run UP (2-loop, N_f=5 -> 6 at m_t) to M_Pl.
         Hidden:  same alpha at M_Pl run DOWN (2-loop, N_f=6 massless) to the pole.
         Question: does Lambda_h move from ~46 MeV toward the UZ target 52 MeV?

 STEP 3: the D-5 acceptance test with b freed (transmutation replaces the
         visible-QCD b_QCD hypothesis): restate the sum rule and quantify how
         growth data measure b.

 STEP 4: the glueball relic boundary vs C1 (ECCG's pure-ADM dark matter):
         xi ranges for invisible / absorbable-subcomponent / C1-breaking / overclosed,
         plus the glueball self-interaction cross-section.
"""
import numpy as np
from scipy.integrate import solve_ivp

MPl = 1.22091e19; MZ = 91.19; mt = 172.6

def run_alpha(alpha0, mu0, mu1, Nf):
    """two-loop running of alpha from mu0 to mu1 (GeV)."""
    b0 = 11 - 2*Nf/3; b1 = 102 - 38*Nf/3
    def rhs(t, y):
        al = y[0]
        return [-(b0/(2*np.pi))*al**2 - (b1/(8*np.pi**2))*al**3]
    sol = solve_ivp(rhs, [np.log(mu0), np.log(mu1)], [alpha0],
                    rtol=1e-10, atol=1e-14, dense_output=True)
    return sol

# ---------------- STEP 2 ----------------
print("="*78)
print("STEP 2 -- two-loop mirror-unified running (N_f = 6)")
print("="*78)
# visible: up MZ -> mt (Nf=5), mt -> MPl (Nf=6)
a_mt   = run_alpha(0.1181, MZ, mt, 5).y[0, -1]
a_MPl  = run_alpha(a_mt, mt, MPl, 6).y[0, -1]
print(f"    alpha_s(m_t) = {a_mt:.5f};  alpha_s(M_Pl) = {a_MPl:.6f}  (1/alpha = {1/a_MPl:.1f})")

def Lambda_pole(alpha0, Nf, two_loop=True):
    """integrate down from M_Pl until alpha explodes; report mu where 1/alpha = 0.05."""
    b0 = 11 - 2*Nf/3; b1 = (102 - 38*Nf/3) if two_loop else 0.0
    def rhs(t, y):
        al = y[0]
        return [-(b0/(2*np.pi))*al**2 - (b1/(8*np.pi**2))*al**3]
    def blow(t, y): return 1/y[0] - 0.05
    blow.terminal, blow.direction = True, -1
    sol = solve_ivp(rhs, [np.log(MPl), np.log(1e-6)], [alpha0],
                    events=blow, rtol=1e-10, atol=1e-14, max_step=0.5)
    return np.exp(sol.t_events[0][0]) if len(sol.t_events[0]) else np.nan

L1 = Lambda_pole(a_MPl, 6, two_loop=False)
L2 = Lambda_pole(a_MPl, 6, two_loop=True)
# MSbar-style 2-loop Lambda for reference: Lam = mu (b0 a/(4pi))^{-b1/b0^2} e^{-2pi/(b0 alpha)} ... use standard:
b0, b1 = 7.0, 26.0
t = 2*np.pi/(b0*a_MPl)
Lam_ms = MPl*np.exp(-t)*(b0*a_MPl/(4*np.pi))**(-b1/(2*b0**2))*(1+0)  # leading 2-loop form
print(f"    pole scale, 1-loop : Lambda_h = {L1*1e3:.1f} MeV")
print(f"    pole scale, 2-loop : Lambda_h = {L2*1e3:.1f} MeV")
print(f"    MSbar-form 2-loop  : Lambda_h = {Lam_ms*1e3:.1f} MeV")
print(f"    UZ-coefficient target (rho = H*chi/m_G): Lambda_h = 6^(1/3)*28.55 = 51.9 MeV")
print(f"    -> direction and landing quantified above; scheme spread (pole vs MSbar) is the")
print(f"       honest uncertainty band. Verdict printed at bottom.")

# ---------------- STEP 3 ----------------
print()
print("="*78)
print("STEP 3 -- D-5 acceptance test with b FREED")
print("="*78)
print("    Sum rule (exact):  zeta_explicit(b) + zeta_reservoir = rho_X * f'/(9H)")
print("                       zeta_explicit(b) = b * rho_X * f'/(9H)")
print("    With transmutation replacing the visible-QCD amplitude hypothesis, b is no")
print("    longer pinned to 0.2062; its constraints are:")
print("      * FPAB stability/convergence floor:  b >= 0.164")
print("      * growth/lensing (mu_infinity anchors from the FPAB pipeline):")
print("            b = 0.20  -> mu_inf(0) = 1.0507")
print("            b = 0.206 -> mu_inf(0) = 1.0525")
print("            b = 1.00  -> mu_inf(0) = 1.3226")
print("      * current data: DESI+CMB+DESY3 mu0 = 0.04 +/- 0.22 -> all b in [0.164,1] allowed")
print("      * FORECAST: sigma(mu0) ~ 0.05 (DR3+Euclid) separates b=0.2 from b=1 at ~5 sigma")
print("    -> b becomes a MEASURED parameter; once measured, the reservoir must supply")
print("       exactly (1-b) of the dissipative response -- the acceptance test survives,")
print("       with its target now data-set rather than QCD-set.")

# ---------------- STEP 4 ----------------
print()
print("="*78)
print("STEP 4 -- glueball relic: invisible / absorbable / C1-breaking / overclosed")
print("="*78)
Lam = 0.052                      # GeV (UZ-corrected target)
m_G = 6*Lam
g_h = 16.0; gstar_conf = 61.75
n_over_s = 0.2777*g_h/gstar_conf     # per xi^3
red32 = 10.0
rho_DM_over_s = 4.4e-10              # GeV
OmegaG_over_DM = lambda xi: m_G*(n_over_s/red32)*xi**3/rho_DM_over_s
from scipy.optimize import brentq
xi_at = lambda frac: (frac*rho_DM_over_s/(m_G*n_over_s/red32))**(1/3)
# C1 absorbable: m_X band 1.63-1.78 tolerates Omega_G/Omega_DM <= 1 - 1.63/1.78 = 8.4%
frac_band = 1 - 1.63/1.78
print(f"    m_G = 6*Lambda_h = {m_G*1e3:.0f} MeV   (Lambda_h = {Lam*1e3:.0f} MeV)")
print(f"    Omega_G/Omega_DM = {OmegaG_over_DM(0.01):.3f} at xi=0.01  (scales as xi^3)")
print(f"    xi thresholds:")
print(f"      invisible   (Omega_G < 0.1% DM)        : xi < {xi_at(0.001):.4f}")
print(f"      ABSORBABLE  (shifts m_X within 1.63-1.78): xi < {xi_at(frac_band):.4f}   [C1 intact]")
print(f"      C1-BREAKING (m_X pushed below 1.63)     : xi > {xi_at(frac_band):.4f}")
print(f"      overclosed  (Omega_G > Omega_DM)        : xi > {xi_at(1.0):.4f}")
print(f"    -> the mirror sector is safe for xi <~ {xi_at(frac_band):.3f}; between "
      f"{xi_at(0.001):.3f} and {xi_at(frac_band):.3f}")
print(f"       glueballs are a genuine subcomponent ABSORBED by ECCG's existing m_X band --")
print(f"       i.e. a measured m_X at the LOW end (1.63-1.70) would be a HINT of the sector.")
sigma_over_m = (1/Lam**2)*0.389e-27/ (m_G*1.783e-24)   # cm^2/g : (1/Lam^2 in GeV^-2 -> cm^2) / (m_G in g)
print(f"    glueball self-interaction: sigma/m ~ 1/(Lam^2 m_G) = {sigma_over_m:.2f} cm^2/g")
print(f"    -> right at the SIDM-relevant range (0.1-1): a glueball subcomponent is")
print(f"       self-interacting at astrophysically interesting levels (dwarf cores) --")
print(f"       connects to the dark-sector completion's SIDM channel as a second source.")

print()
print("="*78)
print("STEP 2 VERDICT")
print("="*78)
d1, d2 = abs(L1*1e3-51.9), abs(L2*1e3-51.9)
print(f"    1-loop -> {L1*1e3:.0f} MeV; 2-loop -> {L2*1e3:.0f} MeV; target 52 MeV.")
print(f"    two-loop moved the prediction {'TOWARD' if d2<d1 else 'AWAY from'} the UZ target"
      f" (|delta| {d1:.0f} -> {d2:.0f} MeV).")
