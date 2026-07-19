#!/usr/bin/env python3
"""
Glueball SIMP/cannibal relic from the mu-transmutation sector: does 3->2 freeze-out
land on Omega_DM with natural alpha_eff?  (user proposal, quantitative check)

Setup: hidden pure SU(3) confining at Lambda_h, glueballs m_G = 6 Lambda_h, sector
DECOUPLED from the SM (pure glue has no renormalizable portal -> the operative regime
is the decoupled cannibal one, NOT the kinetically-coupled SIMP; the dial is the
temperature ratio xi = T_h/T_vis set at reheating).

Method (standard cannibal freeze-out, Boltzmann-equilibrium + separate entropy):
  * hidden/visible entropy ratio kappa = g_h xi^3 / g*s(T_vis,conf), conserved;
  * during cannibalization: n_eq(T_h) (m/T_h + 5/2) = kappa s_vis(T_vis)  fixes T_h(T_vis);
  * freeze-out when Gamma_32 = n^2 <sigma v^2> = H(T_vis),  <sigma v^2> = alpha^3/m^5;
  * relic Y = n_f/s_vis,f;  Omega h^2 = 2.744e8 (m/GeV) Y.
Solve for the alpha_eff that gives Omega h^2 = 0.12, over (Lambda_h, xi).

Also: the SIDM cross-section of a 100% glueball DM, the Delta N_eff in this regime
(correcting my earlier step-5(a) exclusion), and the reheating branching Br(xi).
"""
import numpy as np
from scipy.optimize import brentq

MPl = 1.22091e19
def gstar(T):   # visible g*s, crude piecewise (GeV)
    for Tc, g in [(170,106.75),(4,86.25),(1,75.75),(0.15,61.75),(0.10,17.25),(5e-4,10.75)]:
        if T > Tc: return g
    return 3.91
def s_vis(T): return (2*np.pi**2/45)*gstar(T)*T**3
def H_vis(T): return 1.66*np.sqrt(gstar(T))*T**2/MPl
def n_eq(Th, m, g=1.0): return g*(m*Th/(2*np.pi))**1.5*np.exp(-m/Th)

def relic(alpha, Lam, xi):
    m = 6*Lam
    Tconf_vis = Lam/xi
    kappa = 16*xi**3/gstar(Tconf_vis)          # hidden/visible entropy ratio
    sv2 = alpha**3/m**5
    # scan T_vis downward; find freeze-out Gamma_32 = H
    Tv = np.logspace(np.log10(Tconf_vis), np.log10(1e-6), 4000)
    Y = None
    for T in Tv:
        rhs = kappa*s_vis(T)
        # solve T_h from n_eq(Th)*(m/Th+2.5) = rhs
        f = lambda lTh: np.log(n_eq(np.exp(lTh), m)*(m/np.exp(lTh)+2.5)) - np.log(rhs)
        try:
            lTh = brentq(f, np.log(m/60), np.log(m*2))
        except ValueError:
            continue
        Th = np.exp(lTh); n = n_eq(Th, m)
        if n*n*sv2 < H_vis(T):                  # frozen out
            Y = n/s_vis(T)
            break
    if Y is None: return np.nan
    return 2.744e8*m*Y                          # Omega h^2

print("="*80)
print("Glueball cannibal relic: required alpha_eff for Omega h^2 = 0.12")
print("="*80)
print(f"  {'Lambda_h':>9} | {'m_G':>7} | " + " | ".join(f"xi={x:7.3f}" for x in [0.002,0.004,0.006,0.010,0.020]))
for Lam in [0.030, 0.052, 0.105]:
    row = []
    for xi in [0.002, 0.004, 0.006, 0.010, 0.020]:
        try:
            a = brentq(lambda a: relic(a, Lam, xi) - 0.12, 0.05, 60.0, xtol=1e-3)
            row.append(f"{a:8.2f}")
        except Exception:
            om_lo, om_hi = relic(0.05, Lam, xi), relic(60, Lam, xi)
            row.append("  under" if (np.isnan(om_lo) or max(om_lo,om_hi)<0.12) else "   over")
    print(f"  {Lam*1e3:6.0f} MeV | {6*Lam*1e3:4.0f} MeV | " + " | ".join(row))
print()
print("  (alpha_eff in the 3->2 cross-section <sigma v^2> = alpha^3/m_G^5; 'natural strong")
print("   coupling' means alpha_eff ~ 0.5-4pi for a confining sector at its own scale)")

# ---------------- SIDM, DeltaNeff, reheating branching ----------------
print()
print("="*80)
print("Companion constraints for glueballs = 100% of DM")
print("="*80)
for Lam in [0.030, 0.052, 0.105]:
    m = 6*Lam
    sig_cm2 = (4*np.pi/m**2)*0.389e-27
    som = sig_cm2/(m*1.783e-24)
    print(f"  Lambda_h={Lam*1e3:3.0f} MeV: m_G={m*1e3:3.0f} MeV, SIDM sigma/m ~ 4pi/m^3 = {som:5.2f} cm^2/g"
          f"  ({'cluster-tension (>0.5)' if som>0.5 else 'SIDM-interesting (0.1-0.5)' if som>0.1 else 'safe'})")
print()
xi = 0.006
print(f"  Delta N_eff in this regime: confinement at T_h~Lambda converts hidden gluons to")
print(f"  MASSIVE glueballs long before BBN; cannibalization keeps them non-relativistic.")
print(f"  -> Delta N_eff ~ 0 (my earlier 'thermalized -> 0.43 excluded' applied only to a")
print(f"     sector still RELATIVISTIC at BBN/CMB -- it does NOT exclude this scenario).")
print(f"  Reheating branching needed for xi = {xi}: Br ~ (g_h/g*)*xi^4 = "
      f"{16/106.75*xi**4:.1e}")
print(f"    vs gravitational-strength leakage Br_grav ~ (T_RH/M_Pl)^2 = {(3.2e12/MPl)**2:.1e}")
print(f"  -> the required portal is ~3.5 decades ABOVE pure gravity and ~10 below thermal:")
print(f"     a genuine (mild) model-building selection -- this dial REPLACES the Omega_DM/")
print(f"     Omega_b explanation that ECCG's ADM provided.")
