#!/usr/bin/env python3
"""Figures for Paper VI (scale sector). Numbers are the committed results from the
assessment notes (mirror_qcd_3loop.py, glueball_lrd_seeding.py); reproduced here as
stand-alone plotting so the figure regenerates without the full pipeline."""
import numpy as np, os
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(__file__), "..", "paper", "figures")
os.makedirs(OUT, exist_ok=True)

# ---- Fig 1: mirror-QCD running band (Lambda_pole vs loop order) ----
def fig_band():
    loops = [1, 2, 4]                       # 3-loop is a spurious IR fixed point (excluded)
    Lam   = [28.0, 105.0, 133.0]            # MeV, from mirror_qcd_3loop.py (N_f=6)
    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    ax.plot(loops, Lam, "o-", color="#2c3e50", lw=1.8, ms=8, label=r"$\Lambda_{\rm pole}$ ($N_f=6$)")
    ax.scatter([3], [90], marker="x", s=90, color="0.6")
    ax.annotate("3-loop: spurious IR\nfixed point (excluded)", (3, 90), (2.3, 55),
                fontsize=8, color="0.45", ha="center")
    ax.axhspan(28, 133, color="#f1c40f", alpha=0.15)
    ax.axhline(28.5, ls="--", color="#c0392b", lw=1.3)
    ax.text(3.6, 30.5, r"bare $\mu = 28.5$ MeV", color="#c0392b", fontsize=8.5)
    ax.axhline(52.0, ls="--", color="#27ae60", lw=1.3)
    ax.text(3.6, 54, r"UZ-corrected $6^{1/3}\mu = 52$ MeV", color="#27ae60", fontsize=8.5)
    ax.set(xlabel="loop order", ylabel=r"confinement scale $\Lambda_{\rm pole}$  [MeV]",
           xticks=[1, 2, 3, 4], ylim=(15, 150),
           title="Mirror unification brackets the decade, not the value")
    ax.legend(fontsize=8.5, loc="upper left")
    ax.text(1.05, 19.5, r"zero new continuous parameters ($\alpha_h(M_{\rm Pl})=\alpha_s(M_{\rm Pl})$)",
            fontsize=7.8, color="0.4")
    fig.tight_layout(); p = f"{OUT}/fig1_mirror_band.png"; fig.savefig(p, dpi=170); plt.close(fig); print("wrote", p)

# ---- Fig 2: the Lambda_h pincer (sigma/m vs Lambda_h) ----
def fig_pincer():
    Lh   = np.array([30., 52., 105.])       # MeV
    som  = np.array([0.47, 0.09, 0.01])     # cm^2/g, velocity-independent SIDM
    fig, ax = plt.subplots(figsize=(6.6, 4.1))
    ax.loglog(Lh, som, "o-", color="#8e44ad", lw=1.9, ms=9, zorder=5, label=r"glueball $\sigma/m(\Lambda_h)$")
    # cluster bound from above: sigma/m <~ 0.1-0.5 disfavours the low-Lambda_h (high sigma/m) end
    ax.axhspan(0.1, 1.0, color="#c0392b", alpha=0.10)
    ax.annotate("cluster SIDM bound\n(from above → disfavours 30 MeV)", (33, 0.30), (33, 0.30),
                fontsize=8, color="#c0392b", ha="left", va="center")
    # LRD seeding from below: needs sigma/m >~ 0.1 (with baryon boost); excludes 105 MeV
    ax.axhspan(0.005, 0.1, color="#2980b9", alpha=0.08)
    ax.annotate("LRD gravothermal seeding\n(from below → excludes 105 MeV)", (60, 0.018), (60, 0.018),
                fontsize=8, color="#2980b9", ha="left", va="center")
    ax.scatter([52], [0.09], s=240, facecolor="none", edgecolor="#27ae60", lw=2.4, zorder=6)
    ax.annotate("selected: $\\Lambda_h\\approx52$ MeV\n(= UZ value; a convergence\nof constraints, not a measurement)",
                (52, 0.09), (52, 0.0055), fontsize=8.2, color="#27ae60", ha="center", va="bottom")
    for L, s in zip(Lh, som):
        ax.annotate(f"{int(L)} MeV", (L, s), (L*1.04, s*1.35), fontsize=7.6, color="0.35")
    ax.set(xlabel=r"hidden confinement scale $\Lambda_h$  [MeV]",
           ylabel=r"velocity-independent $\sigma/m$  [cm$^2$/g]",
           title="A two-sided squeeze on $\\Lambda_h$", xlim=(25, 120), ylim=(0.004, 1.2))
    ax.legend(fontsize=8.5, loc="upper right")
    fig.tight_layout(); p = f"{OUT}/fig2_pincer.png"; fig.savefig(p, dpi=170); plt.close(fig); print("wrote", p)

if __name__ == "__main__":
    fig_band(); fig_pincer()
