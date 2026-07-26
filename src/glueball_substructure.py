#!/usr/bin/env python3
"""
Does strong-lensing substructure (e.g. JVAS B1938+666) constrain the glueball
dark matter of Paper VI?

THE TEST OBJECT
---------------
Vegetti et al. (2012, Nature) detected a dark satellite of M ~ 1.9e8 Msun in the
Einstein ring of JVAS B1938+666 at z = 0.881 -- a flagship small-scale-structure
constraint. Any dark-matter model predicting NO structure below ~1e8-1e9 Msun is
excluded by its existence.

THE MODEL (Paper VI, Zenodo 10.5281/zenodo.21525533)
----------------------------------------------------
Hidden SU(3) glueballs: m_G = 6 Lambda_h (312 MeV at the UZ point Lambda_h = 52
MeV), relic set by 3->2 cannibal freeze-out with SEPARATE hidden entropy at
xi = T_h/T_vis = 0.0051-0.0057, velocity-independent sigma/m = 0.09 cm^2/g.
Pure glue has no renormalisable portal, so the sector was never in kinetic
equilibrium with the SM -- the usual WIMP kinetic-decoupling cutoff does not
apply; the cutoff is set instead by (a) free-streaming after cannibal freeze-out
and (b) the horizon scale when the cannibal (pressure-supported) phase ends.

Both are computed here and compared to 1.9e8 Msun.

Run:  python3 src/glueball_substructure.py
"""
import os, json
import numpy as np

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")
os.makedirs(OUT, exist_ok=True)

# cosmology
h, OM, OR = 0.674, 0.315, 9.2e-5
C_OVER_H0 = 2997.9 / h                      # Mpc
RHO_M0 = 2.775e11 * h**2 * OM               # Msun / Mpc^3
A_EQ = OR / OM
T0_eV = 2.348e-4
GS0 = 3.938

# Paper VI hidden sector
XI = 0.0054                                  # T_h / T_vis (relic-abundance fit)
LAMBDA_H_MeV = 52.0
M_G_MeV = 6 * LAMBDA_H_MeV                   # glueball mass
SIGMA_OVER_M = 0.09                          # cm^2/g, velocity-independent

M_SAT_B1938 = 1.9e8                          # Msun, Vegetti et al. 2012


def g_star_s(T_GeV):
    """Crude but adequate SM entropy dof."""
    if T_GeV > 300: return 106.75
    if T_GeV > 100: return 96.
    if T_GeV > 10:  return 86.
    if T_GeV > 1:   return 75.
    if T_GeV > 0.2: return 62.
    if T_GeV > 0.1: return 20.
    if T_GeV > 5e-4:return 10.75
    return 3.938


def scale_factor_at(T_vis_eV):
    gs = g_star_s(T_vis_eV / 1e9)
    return (GS0 / gs) ** (1 / 3) * T0_eV / T_vis_eV


def E_of_a(a):
    return np.sqrt(OR / a**4 + OM / a**3 + (1 - OM - OR))


def free_streaming(a_f, v_f):
    """Comoving free-streaming length [Mpc]: int v(a) da / (a^2 E(a)) * c/H0,
    with v = min(1, v_f a_f / a) (non-relativistic redshifting)."""
    a = np.logspace(np.log10(a_f), 0.0, 200000)
    v = np.minimum(1.0, v_f * a_f / a)
    integ = v / (a**2 * E_of_a(a))
    return C_OVER_H0 * np.trapezoid(integ, a)


def mass_from_length(lam_Mpc):
    """Mass enclosed in a sphere of comoving radius lam/2."""
    return (4 * np.pi / 3) * RHO_M0 * (lam_Mpc / 2) ** 3


def horizon_mass(a_f):
    r_H = C_OVER_H0 / (a_f * E_of_a(a_f))    # comoving horizon [Mpc]
    return (4 * np.pi / 3) * RHO_M0 * r_H**3, r_H


def main():
    print("=" * 78)
    print("DOES LENSING SUBSTRUCTURE (JVAS B1938+666) CONSTRAIN GLUEBALL DARK MATTER?")
    print("=" * 78)
    print(f"\n target: Vegetti et al. 2012 satellite, M = {M_SAT_B1938:.1e} Msun")
    print(f" model : m_G = {M_G_MeV:.0f} MeV, xi = {XI}, sigma/m = {SIGMA_OVER_M} cm^2/g")
    print("\n note: pure glue has no renormalisable SM portal, so the sector was never in")
    print("       kinetic equilibrium with the SM -- the WIMP kinetic-decoupling cutoff")
    print("       does not apply. Cutoff is set by cannibal freeze-out instead.\n")

    print(f" {'x_f':>5} | {'T_h,f':>9} | {'T_vis,f':>10} | {'a_f':>10} | {'v_f/c':>7} | "
          f"{'M_fs [Msun]':>12} | {'M_hor [Msun]':>12}")
    print(" " + "-" * 84)
    rows = []
    for x_f in [15, 20, 25, 30]:
        T_h_f = M_G_MeV / x_f                       # MeV
        T_vis_f = T_h_f / XI                        # MeV
        a_f = scale_factor_at(T_vis_f * 1e6)
        v_f = np.sqrt(3.0 / x_f)                    # sqrt(3T/m), non-rel. thermal speed
        lam = free_streaming(a_f, v_f)
        M_fs = mass_from_length(lam)
        M_h, r_H = horizon_mass(a_f)
        rows.append(dict(x_f=x_f, T_h_f_MeV=T_h_f, T_vis_f_MeV=T_vis_f, a_f=float(a_f),
                         v_f=float(v_f), lambda_fs_Mpc=float(lam),
                         M_fs=float(M_fs), M_horizon=float(M_h)))
        print(f" {x_f:>5} | {T_h_f:>7.2f} MeV | {T_vis_f/1e3:>7.2f} GeV | {a_f:>10.2e} | "
              f"{v_f:>7.3f} | {M_fs:>12.2e} | {M_h:>12.2e}")

    M_cut = max(max(r["M_fs"] for r in rows), max(r["M_horizon"] for r in rows))
    print(f"\n largest cutoff mass over the scanned freeze-out range: {M_cut:.2e} Msun")
    print(f" B1938+666 satellite:                                    {M_SAT_B1938:.2e} Msun")
    print(f" margin: {M_SAT_B1938 / M_cut:.1e}  ({np.log10(M_SAT_B1938 / M_cut):.0f} orders of magnitude)")

    print("\n[WHY SO SMALL] the hidden sector is COLD (xi = %.4f), so reaching x_f ~ 20" % XI)
    print("  requires T_vis ~ %.1f GeV -- freeze-out is very EARLY, the scale factor is" %
          (rows[1]["T_vis_f_MeV"] / 1e3))
    print("  ~1e-14, and both the free-streaming length and the horizon are microscopic.")
    print("  A cold, heavy, secluded relic is effectively perfect CDM on observable scales.")

    print("\n[SIDM CHANNEL] sigma/m = %.2f cm^2/g" % SIGMA_OVER_M)
    print("  Subhalo evaporation / core formation at this cross-section is well below the")
    print("  ~1 cm^2/g scale where lensing-substructure signatures become diagnostic;")
    print("  Paper VI's binding SIDM constraint remains the cluster bound (0.1-0.5),")
    print("  which is ~an order of magnitude tighter than substructure lensing delivers.")

    print("\n[VERDICT]")
    print("  B1938+666 does NOT constrain the glueball sector -- by ~%d orders of magnitude"
          % np.log10(M_SAT_B1938 / M_cut))
    print("  on the cutoff side, and non-competitively on the self-interaction side.")
    print("  This is a GAP CLOSED (robustness), not a new falsifier: the model predicts")
    print("  abundant structure far below the detected satellite, so the detection is")
    print("  comfortably accommodated. Worth one sentence in Paper VI; not a constraint.")

    json.dump({"target": {"system": "JVAS B1938+666", "M_sat_Msun": M_SAT_B1938,
                          "ref": "Vegetti et al. 2012"},
               "model": {"m_G_MeV": M_G_MeV, "xi": XI, "sigma_over_m": SIGMA_OVER_M},
               "rows": rows, "M_cutoff_max_Msun": float(M_cut),
               "margin_orders": float(np.log10(M_SAT_B1938 / M_cut)),
               "verdict": "not constraining; gap closed (robustness), not a falsifier"},
              open(os.path.join(OUT, "glueball_substructure.json"), "w"), indent=2)
    print(f"\n wrote {os.path.join(OUT, 'glueball_substructure.json')}")


if __name__ == "__main__":
    main()
