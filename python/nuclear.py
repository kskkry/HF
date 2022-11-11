import math
import numpy as np
from basis import GTO, CGF, Basis
from config import Config
from functions import compute_binomial_prefactor, compute_dist2, factorial, compute_gaussian_product_center, Fgamma
from geometry import Atom, Vec
from overlap import compute_gto_overlap, compute_overlap
cfg = Config()

'''
This Program referred to the following Source!
https://github.com/ifilot/hfcxx/blob/master/src/nuclear.cpp
'''

def compute_nuclear(atom1: Atom, norm1: float, l1: int, m1: int, n1: int, alpha1: float, atom2: Atom, norm2: float, l2: int, m2: int, n2: int, alpha2: float, atom3: Atom) -> float:
    '''
    [parameter]
    atom3: Atom that adds nuclear-attraction-value
    '''
    gamma = alpha1 + alpha2
    p_vec = compute_gaussian_product_center(alpha1, atom1, alpha2, atom2)
    
    # virtual atom that shows internal division point
    atom_empty = Atom('X', p_vec.getx(), p_vec.gety(), p_vec.getz())
    Rab2 = compute_dist2(atom1, atom2)
    Rcp2 = compute_dist2(atom3, atom_empty)
    arr_x = get_A_array(l1, l2, atom_empty.getx()-atom1.getx(), atom_empty.getx()-atom2.getx(), atom_empty.getx()-atom3.getx(), gamma)
    arr_y = get_A_array(m1, m2, atom_empty.gety()-atom1.gety(), atom_empty.gety()-atom2.gety(), atom_empty.gety()-atom3.gety(), gamma)
    arr_z = get_A_array(n1, n2, atom_empty.getz()-atom1.getz(), atom_empty.getz()-atom2.getz(), atom_empty.getz()-atom3.getz(), gamma)
    sum_val = 0.0
    for i in range(l1+l2+1):
        for j in range(m1+m2+1):
            for k in range(n1+n2+1):
                sum_val += arr_x[i] * arr_y[j] * arr_z[k] * Fgamma(i+j+k, Rcp2*gamma)
    
    return -norm1 * norm2 * 2.0 * cfg.getPI() / gamma * np.exp(-alpha1*alpha2*Rab2 / gamma) * sum_val

def compute_gto_nuclear(gto1: GTO, gto2: GTO, atom: Atom):
    '''
    '''
    return compute_nuclear(gto1.atom, gto1.norm, gto1.l, gto1.m, gto1.n, gto1.alpha, gto2.atom, gto2.norm, gto2.l, gto2.m, gto2.n, gto2.alpha, atom)


def compute_cgf_nuclear(cgf1: CGF, cgf2: CGF, atom: Atom):
    '''
    '''
    sum_val = 0.0
    for gto1 in cgf1.gtos:
        for gto2 in cgf2.gtos:
            norm1 = gto1.norm
            norm2 = gto2.norm
            sum_val += gto1.coeff * gto2.coeff * compute_gto_nuclear(gto1, gto2, atom)
    return float(atom.element) * sum_val

def get_nuclear_mx(basis1: Basis, basis2: Basis, atom_list: list, debug=False) -> np.array:
    '''
    '''
    assert basis1.getsize() == basis2.getsize()
    size = basis1.getsize()
    nuclear_mx = np.zeros((size, size))
    for id1 in range(size):
        for id2 in range(size):
            for atom in atom_list:
                nuclear_mx[id1, id2] += compute_cgf_nuclear(basis1.cgfs[id1], basis2.cgfs[id2], atom)
    #===========================================================================================================================================================
    if debug:
        '''
        print as matrix format
        '''
        print("\n===== nuclear matrix ==========================================================================================================================")
        for id1 in range(size):
            for id2 in range(size):
                if id2 == size-1:
                    print(f"{nuclear_mx[id1, id2]:.5e}")
                else:
                    print(f"{nuclear_mx[id1, id2]:.5e}", end=',  ')
        print("===============================================================================================================================================\n")
    #===========================================================================================================================================================
    return nuclear_mx

def get_A_array(l1: int, l2: int, pos1: float, pos2: float, pos3: float, gamma: float) -> list:
    imax = l1 + l2 + 1
    A_arr = [0.0 for i in range(imax)]
    for i in range(imax):
        rmax = i/2
        if i == 0:
            rmax = 1
        elif i % 2 == 0:
            rmax = i // 2
        else:
            rmax = i // 2 + 1
        for r in range(rmax):
            umax = 0
            if (i-2*r) == 0:
                umax = 1
            elif (i-2*r) % 2 == 0:
                umax = (i-2*r) // 2
            else:
                umax = (i-2*r) // 2 + 1
            for u in range(umax):
                iI = i - 2*r - u
                A_arr[iI] += compute_A_term(i, r, u, l1, l2, pos1, pos2, pos3, gamma)
    return A_arr

def compute_A_term(l: int, r: int, i: int, l1: int, l2: int, xa: float, xb: float, xc: float, gamma: float) -> float:
    '''
    Ref: Handbook of Computational Quantum Chemistry, Cook, p.245
    '''
    return math.pow(-1,l) * compute_binomial_prefactor(l, l1, l2, xa, xb) * math.pow(-1, i) \
        * factorial(l) * math.pow(xc, l-2*r-2*i) * math.pow(0.25 / gamma, r+i) / (factorial(r) * factorial(i) * factorial(l-2*r-2*i))
    
    
    
