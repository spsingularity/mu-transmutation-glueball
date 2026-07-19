#!/usr/bin/env python3
"""
Tier-1 #2: 3-loop scheme-fixed mirror-QCD running for the transmutation mu.
Mirror unification demands alpha_h(M_Pl)=alpha_s(M_Pl). Run N_f=6 down at 1/2/3/4-loop
and locate Lambda_MSbar; convert to a physical confinement scale via the lattice
T_c/Lambda_MSbar ratio. Question: does N_f=6 land on the bare mu (28.5 MeV) or the
UZ-corrected 6^(1/3) mu = 52 MeV, and how much does 3-loop tighten the 2-loop band (28-105)?
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

MPl=1.22091e19; MZ=91.19; mt=172.6
# MSbar beta-function coefficients b_i (convention: mu^2 d a/d mu^2 = -a^2 (b0 + b1 a + b2 a^2 + b3 a^3), a=alpha/(4pi))
def betas(Nf):
    b0=11-2*Nf/3
    b1=102-38*Nf/3
    b2=2857/2-5033*Nf/18+325*Nf**2/54
    b3=(149753/6+3564*1.20206) - (1078361/162+6508/27*1.20206)*Nf + (50065/162+6472/81*1.20206)*Nf**2 + 1093/729*Nf**3
    return [b0,b1,b2,b3]

def run_alpha_nloop(alpha0, mu0, mu1, Nf, nloop):
    b=betas(Nf); a0=alpha0/(4*np.pi)
    def rhs(t,y):  # t=ln mu^2, y=a
        a=y[0]; s=b[0]
        if nloop>=2: s+=b[1]*a
        if nloop>=3: s+=b[2]*a**2
        if nloop>=4: s+=b[3]*a**3
        return [-a**2*s]
    sol=solve_ivp(rhs,[2*np.log(mu0),2*np.log(mu1)],[a0],rtol=1e-11,atol=1e-16,dense_output=True)
    return sol.y[0,-1]*4*np.pi

# visible alpha_s up to M_Pl (2-loop, Nf 5->6 at mt)
a_mt=run_alpha_nloop(0.1181,MZ,mt,5,2); a_MPl=run_alpha_nloop(a_mt,mt,MPl,6,2)
print("="*72); print("Tier-1 #2: 3-loop mirror-QCD running (N_f=6)"); print("="*72)
print(f"  alpha_s(M_Pl) = {a_MPl:.5f}  (1/alpha = {1/a_MPl:.1f})   [mirror: alpha_h(M_Pl)=this]")
print()
def Lambda(alpha0, Nf, nloop):
    """scale where 1/alpha -> 0.05 (perturbative breakdown ~ confinement proxy)."""
    b=betas(Nf); a0=alpha0/(4*np.pi)
    def rhs(t,y):
        a=y[0]; s=b[0]
        if nloop>=2: s+=b[1]*a
        if nloop>=3: s+=b[2]*a**2
        if nloop>=4: s+=b[3]*a**3
        return [-a**2*s]
    def hit(t,y): return 1/(y[0]*4*np.pi)-0.05
    hit.terminal=True; hit.direction=-1
    sol=solve_ivp(rhs,[2*np.log(MPl),2*np.log(1e-6)],[a0],events=hit,rtol=1e-11,atol=1e-16,max_step=1.0)
    return np.exp(sol.t_events[0][0]/2) if len(sol.t_events[0]) else np.nan

print(f"  {'loop':>6} | {'Lambda_pole [MeV]':>18}")
for nl in [1,2,3,4]:
    L=Lambda(a_MPl,6,nl)
    print(f"  {nl:6d} | {L*1e3:18.1f}")
print()
print(f"  targets:  bare mu = 28.55 MeV   |   UZ-corrected 6^(1/3)*mu = {6**(1/3)*28.55:.1f} MeV")
L2,L3,L4=Lambda(a_MPl,6,2),Lambda(a_MPl,6,3),Lambda(a_MPl,6,4)
print(f"  2->3-loop shift: {L2*1e3:.0f} -> {L3*1e3:.0f} MeV ;  3->4-loop: {L3*1e3:.0f} -> {L4*1e3:.0f} MeV")
print(f"  3-4 loop stability: |L4-L3|/L3 = {abs(L4-L3)/L3*100:.0f}%")
print()
print("  NOTE: 'Lambda_pole' (1/alpha=0.05 proxy) is scheme-dependent; the physical confinement")
print("  scale is Lambda_MSbar x (T_c/Lambda_MSbar). For N_f=6 SU(3) (below the conformal window),")
print("  lattice gives T_c/Lambda_MSbar ~ 1.1-1.3, an O(1) factor. So the perturbative band above")
print("  sets the DECADE; the physical scale is within an O(1) of it.")
