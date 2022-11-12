import math
import numpy as np
from basis import Atom, GTO, CGF, Basis
from config import Config
from functions import factorial, compute_dist2, compute_gaussian_product_center, Fgamma
cfg = Config()

def compute_coulomb_repulsion(
    atom1: Atom, norm1: float, l1: int, m1: int, n1: int, alpha1: float, \
    atom2: Atom, norm2: float, l2: int, m2: int, n2: int, alpha2: float, \
    atom3: Atom, norm3: float, l3: int, m3: int, n3: int, alpha3: float, \
    atom4: Atom, norm4: float, l4: int, m4: int, n4: int, alpha4: float  \
    ) -> float:
    '''
    '''
    Rab2 = compute_dist2(atom1, atom2)
    Rcd2 = compute_dist2(atom3, atom4)
    
    p_vec = compute_gaussian_product_center(alpha1, atom1, alpha2, atom2)
    q_vec = compute_gaussian_product_center(alpha3, atom3, alpha4, atom4)
    p_vir_atom = Atom('X', p_vec.getx(), p_vec.gety(), p_vec.getz())
    q_vir_atom = Atom('X', q_vec.getx(), q_vec.gety(), q_vec.getz())
    Rpq2 = compute_dist2(p_vir_atom, q_vir_atom)
    
    gamma12 = alpha1 + alpha2
    gamma34 = alpha3 + alpha4
    
    delta = 0.25 * (1.0 / gamma12 + 1.0 / gamma34)
    
    return
    
def compute_gto_repulsion(gto1: GTO, gto2: GTO, gto3: GTO, gto4: GTO):
    '''
    '''
    return compute_coulomb_repulsion(
        gto1.atom, gto1.norm, gto1.l, gto1.m, gto1.n, gto1.alpha, \
        gto2.atom, gto2.norm, gto2.l, gto2.m, gto2.n, gto2.alpha, \
        gto3.atom, gto3.norm, gto3.l, gto3.m, gto3.n, gto3.alpha, \
        gto4.atom, gto4.norm, gto4.l, gto4.m, gto4.n, gto4.alpha,
    )

def compute_cgf_repulsion(cgf1: CGF, cgf2: CGF, cgf3: CGF, cgf4: CGF):
    '''
    '''
    sum_val = 0.0
    for i in range(cgf1.getsize()):
        for j in range(cgf2.getsize()):
            for k in range(cgf3.getsize()):
                for il in range(cgf4.getsize()):
                    pre_coeff = cgf1.gtos[i].coeff * cgf2.gtos[j].coeff * cgf3.gtos[k].coeff * cgf4.gtos[l].coeff
                    sum_val +=  pre_coeff * compute_gto_repulsion(cgf1.gtos[i], cgf2.gtos[j], cgf3.gtos[k], cgf4.gtos[l])
    return sum_val

def get_repulsion_mx(basis1: Basis, basis2: Basis, atom_list: list, debug=False) -> np.array:
    '''
    '''
    pass

