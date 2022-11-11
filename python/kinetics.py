import math
import numpy as np
from basis import GTO, CGF, Basis
from config import Config
from geometry import Atom, Vec
from overlap import compute_gto_overlap, compute_overlap
cfg = Config()

def compute_gto_kinetics(gto1: GTO, gto2: GTO) -> float:
    '''
    This function computes kinetics energy integral.
    To compute kinetics, we need computing method to calculate overlap integral
    Ref : P29, Nakai
    '''
    term_angular_moment_plus2 = 4.0 * math.pow(gto2.alpha, 2)  \
        *(compute_overlap(gto1.alpha, gto1.l, gto1.m, gto1.n, gto1.atom, gto2.alpha, gto2.l+2, gto2.m, gto2.n, gto2.atom) \
        + compute_overlap(gto1.alpha, gto1.l, gto1.m, gto1.n, gto1.atom, gto2.alpha, gto2.l, gto2.m+2, gto2.n, gto2.atom) \
        + compute_overlap(gto1.alpha, gto1.l, gto1.m, gto1.n, gto1.atom, gto2.alpha, gto2.l, gto2.m, gto2.n+2, gto2.atom)
        )
        
    #term0 -2 -> -6 (minor error point)
    term_angular_moment_0 = (-4.0 * gto2.alpha * (gto2.l + gto2.m + gto2.n) - 6.0 * gto2.alpha) * compute_gto_overlap(gto1, gto2)
    
    term_angular_moment_minus2 = \
      (gto2.l * (gto2.l-1) * compute_overlap(gto1.alpha, gto1.l, gto1.m, gto1.n, gto1.atom, gto2.alpha, gto2.l-2, gto2.m, gto2.n, gto2.atom)) \
    + (gto2.m * (gto2.m-1) * compute_overlap(gto1.alpha, gto1.l, gto1.m, gto1.n, gto1.atom, gto2.alpha, gto2.l, gto2.m-2, gto2.n, gto2.atom)) \
    + (gto2.n * (gto2.n-1) * compute_overlap(gto1.alpha, gto1.l, gto1.m, gto1.n, gto1.atom, gto2.alpha, gto2.l, gto2.m, gto2.n-2, gto2.atom))
    return -0.5 * (term_angular_moment_plus2 + term_angular_moment_0 + term_angular_moment_minus2)

def compute_cgf_kinetics(cgf1: CGF, cgf2: CGF) -> float:
    '''
    '''
    sum_val = 0.0
    for gto1 in cgf1.gtos:
        for gto2 in cgf2.gtos:
            norm1 = gto1.norm
            norm2 = gto2.norm
            sum_val += gto1.coeff * gto2.coeff * norm1 * norm2 * compute_gto_kinetics(gto1, gto2)
    return sum_val

def get_kinetics_mx(basis1: Basis, basis2: Basis, debug=False) -> np.array:
    '''
    '''
    assert basis1.getsize() == basis2.getsize()
    size = basis1.getsize()
    kinetics_mx = np.zeros((size, size))
    for id1 in range(size):
        for id2 in range(size):
            kinetics_mx[id1, id2] = compute_cgf_kinetics(basis1.cgfs[id1], basis2.cgfs[id2])
    
    #===========================================================================================================================================================
    if debug:
        '''
        print as matrix format
        '''
        print("\n===== kinetics matrix ==========================================================================================================================")
        for id1 in range(size):
            for id2 in range(size):
                if id2 == size-1:
                    print(f"{kinetics_mx[id1, id2]:.5e}")
                else:
                    print(f"{kinetics_mx[id1, id2]:.5e}", end=',  ')
        print("===============================================================================================================================================\n")
    #===========================================================================================================================================================
    
    return kinetics_mx

