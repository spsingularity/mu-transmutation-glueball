#!/usr/bin/env python3
"""Can glueball-SIDM gravothermal collapse seed the JWST Little Red Dots?

Glueball DM (USC horn iii) has a velocity-INDEPENDENT self-interaction fixed by Lambda_h:
    sigma/m ~= 0.47 / 0.09 / 0.01 cm^2/g  at  Lambda_h = 30 / 52 / 105 MeV
(GLUEBALL_DM_assessment.md). SIDM gravothermal collapse of early dense halos is a
heavy-seed channel for the LRD overmassive black holes (M_BH ~ 1e6-1e8 Msun at z~5-9,
comoving abundance n_LRD ~ 1e-5 Mpc^-3).

Test: for each Lambda_h, which halos (M, c, z_form) collapse before z=7, what seed
masses result (M_seed ~ 2% M_halo, relativistic-instability core), and does the
abundance of collapsing halos reach n_LRD?

Machinery:
 - sigma(M,z) from the real linear P(k) via classy (same engine as the rest of Tier-2).
 - Sheth-Tormen halo mass function.
 - NFW (rho_s, r_s) from (M200c, c, z); v_s = V_max/sqrt(2) as the characteristic
   1D dispersion; t_c = (150/C) / (rho_s (sigma/m) v_s), C = 0.75 (Essig+19 calibration;
   conventions differ at O(1) -- results quoted with that caveat).
 - concentration: lognormal around cbar = 4.5 (high-z sims: c ~ 3-6, flat), sigma_lnc = 0.35.
 - collapse window: halo forms at z_f in {15, 12, 10}, must collapse by z = 7.
 - optimistic branch: baryon-potential acceleration of collapse x30 (Feng/Yu-type;
   '2605.31335 robust-against-feedback' regime) -- bracketed, not assumed.
"""
import numpy as np, os
from scipy.integrate import quad
from scipy.stats import norm

# ---------------- cosmology ----------------
h=0.685; Om=0.301; OL=1-Om; H0=100*h  # km/s/Mpc
G_kpc = 4.30091e-6           # kpc (km/s)^2 / Msun
rho_crit0 = 2.775e2*h**2     # Msun/kpc^3  (2.775e11 h^2 Msun/Mpc^3)
rho_m0 = Om*rho_crit0        # Msun/kpc^3
KPC_CM=3.0857e21; MSUN_G=1.989e33; KMS_CMS=1e5; GYR_S=3.156e16

def Ez(z): return np.sqrt(Om*(1+z)**3+OL)
def age_Gyr(z):
    f=lambda zz: 1.0/((1+zz)*Ez(zz))
    val,_=quad(f,z,3000,limit=200)
    return val*(977.8/H0)  # 1/(H0 in 1/Gyr) = 977.8/H0[km/s/Mpc] Gyr

# ---------------- sigma(M,z) via classy ----------------
# classy = the mochi-class fork. If it is not already importable in your environment, set
# MOCHI_CLASS_DIR to its local build directory (avoids hardcoding a machine-specific path).
_mc = os.environ.get("MOCHI_CLASS_DIR")
if _mc:
    os.chdir(_mc)
from classy import Class
c=Class()
c.set(dict(h=h,omega_b=0.0224,omega_cdm=Om*h**2-0.0224,A_s=2.10e-9,n_s=0.9682,N_ur=3.046,
           output='mPk',z_max_pk=20))
c.set({'P_k_max_1/Mpc':300.0})
c.compute()
def sigma_M(M,z):
    R=(3*M/(4*np.pi*rho_m0))**(1/3)/1e3   # Mpc (rho_m0 in Msun/kpc^3 -> R in kpc -> /1e3)
    return c.sigma(R,z)

# ---------------- Sheth-Tormen HMF ----------------
DELTA_C=1.686
def n_ST(M,z):
    """dn/dlnM [Mpc^-3] via Sheth-Tormen."""
    dlnM=0.02
    s1,s2=sigma_M(M*np.exp(-dlnM/2),z),sigma_M(M*np.exp(dlnM/2),z)
    sig=0.5*(s1+s2); dlns_dlnM=(np.log(s2)-np.log(s1))/dlnM
    nu=DELTA_C/sig
    A,a,p=0.3222,0.707,0.3
    fnu=A*np.sqrt(2*a/np.pi)*nu*(1+(a*nu*nu)**(-p))*np.exp(-a*nu*nu/2)
    rho_m_Mpc=rho_m0*1e9   # Msun/Mpc^3
    return (rho_m_Mpc/M)*fnu*abs(dlns_dlnM)

# ---------------- NFW + gravothermal collapse time ----------------
CBAR=4.5; SLNC=0.35; C_CAL=0.75
def halo_props(M,cc,z):
    rc=rho_crit0*Ez(z)**2
    R200=(3*M/(4*np.pi*200*rc))**(1/3)      # kpc
    rs=R200/cc
    fc=np.log(1+cc)-cc/(1+cc)
    rho_s=(200/3.)*rc*cc**3/fc               # Msun/kpc^3
    Vmax=1.64*rs*np.sqrt(G_kpc*rho_s)        # km/s
    vs=Vmax/np.sqrt(2)                       # 1D dispersion proxy
    return rho_s,rs,vs
def t_collapse_Gyr(M,cc,z,sig_m,boost=1.0):
    rho_s,rs,vs=halo_props(M,cc,z)
    rho_cgs=rho_s*MSUN_G/KPC_CM**3
    rate=rho_cgs*sig_m*(vs*KMS_CMS)*boost    # 1/s
    return (150./C_CAL)/rate/GYR_S

def cmin_for_collapse(M,z_f,sig_m,t_avail,boost=1.0):
    """smallest concentration that collapses within t_avail (t_c falls steeply with c)."""
    for cc in np.linspace(2,40,381):
        if t_collapse_Gyr(M,cc,z_f,sig_m,boost)<t_avail: return cc
    return np.inf

def seeded_density(z_f,sig_m,boost=1.0):
    """comoving density [Mpc^-3] of halos at z_f whose (lognormal) concentration tail collapses by z=7,
       and the seed-mass-weighted census."""
    t_avail=age_Gyr(7.0)-age_Gyr(z_f)
    lnMs=np.linspace(np.log(1e8),np.log(3e11),40)
    tot=0.0; census=[]
    for lnM in lnMs:
        M=np.exp(lnM)
        cmin=cmin_for_collapse(M,z_f,sig_m,t_avail,boost)
        if not np.isfinite(cmin): continue
        P=1-norm.cdf(np.log(cmin/CBAR)/SLNC)   # P(c > cmin), lognormal
        dens=n_ST(M,z_f)*P*(lnMs[1]-lnMs[0])
        tot+=dens
        if dens>0: census.append((M,cmin,P,dens))
    return tot,t_avail,census

# ---------------- run ----------------
print("="*76)
print("Glueball-SIDM gravothermal seeding of the JWST Little Red Dots")
print("="*76)
print(f"  target: n_LRD ~ 1e-5 Mpc^-3 comoving, M_BH ~ 1e6-1e8 Msun by z~7")
print(f"  seed mass ~ 2% of M_halo (relativistic core); t_c=(150/{C_CAL})/(rho_s sigma/m v_s)")
print(f"  concentration: lognormal cbar={CBAR}, sigma_lnc={SLNC}; ST HMF; sigma(M,z) from classy")
print()
GLUE=[("Lambda_h=30 MeV",0.47),("Lambda_h=52 MeV",0.09),("Lambda_h=105 MeV",0.01)]
for boost,btag in [(1.0,"DM-only"),(30.0,"baryon-boosted x30 (optimistic bracket)")]:
    print(f"--- {btag} ---")
    for tag,sm in GLUE:
        best=None
        for z_f in [15.,12.,10.]:
            tot,t_avail,census=seeded_density(z_f,sm,boost)
            if best is None or tot>best[1]: best=(z_f,tot,t_avail,census)
        z_f,tot,t_avail,census=best
        ratio=tot/1e-5
        if census:
            Ms=np.array([x[0] for x in census]); ds=np.array([x[3] for x in census])
            Mtyp=np.exp(np.average(np.log(Ms),weights=ds)); seed=0.02*Mtyp
            cmin_at=census[np.argmax(ds)][1]
            extra=f"M_halo~{Mtyp:.1e}, seed~{seed:.1e} Msun, needs c>{cmin_at:.0f}"
        else:
            extra="no halo collapses at ANY c<=40"
        print(f"  {tag} (sigma/m={sm}): best z_f={z_f:.0f} (window {t_avail*1e3:.0f} Myr)")
        print(f"     n_seeded = {tot:.2e} Mpc^-3  = {ratio:.1e} x n_LRD ;  {extra}")
    print()
# example single-halo numbers for the note
print("--- reference single-halo t_c (z_f=10, M=1e10, c=4.5 median / c=15 tail) ---")
for tag,sm in GLUE:
    t1=t_collapse_Gyr(1e10,4.5,10,sm); t2=t_collapse_Gyr(1e10,15,10,sm)
    print(f"  {tag}: t_c(median c=4.5) = {t1:.1f} Gyr ; t_c(c=15 tail) = {t2:.2f} Gyr ; window ~0.3 Gyr")
