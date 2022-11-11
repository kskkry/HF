import math
import numpy as np
from basis import GTO, CGF, Basis
from geometry import Atom, Vec
from config import Config
from functions import compute_dist2, compute_gaussian_product_center, compute_binomial_prefactor, factorial, factorial2
cfg = Config()

def compute_overlap_1D(l1: int, l2: int, x1: float, x2: float, gamma: float):
    sum_val = 0.0
    for i in range(1+math.floor(0.5*(l1+l2))):
        sum_val += compute_binomial_prefactor(2*i, l1, l2, x1, x2) * factorial2(2*i-1)/math.pow(2*gamma,i)
    return sum_val

def compute_overlap(alpha1:float, l1:int,m1:int, n1:int, atom1: Atom, alpha2: float, l2: int, m2: int, n2: int, atom2: Atom) -> float:
    dist2 = compute_dist2(atom1, atom2)
    gamma = alpha1 + alpha2
    # pos: Vec Object
    pos = compute_gaussian_product_center(alpha1, atom1, alpha2, atom2)
    pre = math.pow(cfg.getPI() / gamma, 1.5) * np.exp(-alpha1 * alpha2 * dist2 / gamma)
    wx = compute_overlap_1D(l1, l2, pos.getx()-atom1.getx(), pos.getx()-atom2.getx(), gamma)
    wy = compute_overlap_1D(m1, m2, pos.gety()-atom1.gety(), pos.gety()-atom2.gety(), gamma)
    wz = compute_overlap_1D(n1, n2, pos.getz()-atom1.getz(), pos.getz()-atom2.getz(), gamma)
    return pre*wx*wy*wz

def compute_gto_overlap(gto1: GTO, gto2: GTO):
    return compute_overlap(alpha1=gto1.alpha, l1=gto1.l, m1=gto1.m, n1=gto1.n, atom1=gto1.atom, \
        alpha2=gto2.alpha, l2=gto2.l, m2=gto2.m, n2=gto2.n, atom2=gto2.atom)
    
def compute_cgf_overlap(cgf1: CGF, cgf2: CGF):
    cgf1_size = cgf1.getsize()
    cgf2_size = cgf2.getsize()
    sum_val = 0.0
    for i in range(cgf1_size):
        for j in range(cgf2_size):
            norm1 = cgf1.gtos[i].norm
            norm2 = cgf2.gtos[j].norm
            sum_val += cgf1.gtos[i].coeff * cgf2.gtos[j].coeff * norm1 * norm2 * compute_gto_overlap(cgf1.gtos[i], cgf2.gtos[j])
    return sum_val

def get_overlap_mx(basis1: Basis, basis2: Basis, debug=False):
    assert basis1.getsize() == basis2.getsize()
    size = basis1.getsize()
    overlap_mx = np.zeros((size, size))
    for id1 in range(size):
        for id2 in range(size):
            overlap_mx[id1, id2] = compute_cgf_overlap(basis1.cgfs[id1], basis1.cgfs[id2])
    #===========================================================================================================================================================
    if debug:
        '''
        print as matrix format
        '''
        print("\n===== overlap matrix ==========================================================================================================================")
        for id1 in range(size):
            for id2 in range(size):
                if id2 == size-1:
                    print(f"{overlap_mx[id1, id2]:.5e}")
                else:
                    print(f"{overlap_mx[id1, id2]:.5e}", end=',  ')
        print("===============================================================================================================================================\n")
    #===========================================================================================================================================================
    return overlap_mx
    
    