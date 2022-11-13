import math
import numpy as np
from basis import Atom, GTO, CGF, Basis
from config import Config
from functions import compute_binomial_prefactor, factorial, compute_dist2, compute_gaussian_product_center, Fgamma, pair_index
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
    bx = get_B_array(l1,l2,l3,l4,p_vec.getx(), atom1.getx(), atom2.getx(), q_vec.getx(), atom3.getx(), atom4.getx(), gamma12, gamma34, delta)
    by = get_B_array(m1,m2,m3,m4,p_vec.gety(), atom1.gety(), atom2.gety(), q_vec.gety(), atom3.gety(), atom4.gety(), gamma12, gamma34, delta)
    bz = get_B_array(n1,n2,n3,n4,p_vec.getz(), atom1.getz(), atom2.getz(), q_vec.getz(), atom3.getz(), atom4.getz(), gamma12, gamma34, delta)
    sum_val = 0.0
    for i in range(l1+l2+l3+l4+1):
        for j in range(m1+m2+m3+m4+1):
            for k in range(n1+n2+n3+n4+1):
                sum_val += bx[i]*by[j]*bz[k]*Fgamma(i+j+k, 0.25*Rpq2/delta)
    return sum_val
    
def compute_gto_repulsion(gto1: GTO, gto2: GTO, gto3: GTO, gto4: GTO) -> float:
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
                for l in range(cgf4.getsize()):
                    pre_coeff = cgf1.gtos[i].coeff * cgf2.gtos[j].coeff * cgf3.gtos[k].coeff * cgf4.gtos[l].coeff
                    sum_val +=  pre_coeff * compute_gto_repulsion(cgf1.gtos[i], cgf2.gtos[j], cgf3.gtos[k], cgf4.gtos[l])
    return sum_val

def get_repulsion_list(basis: Basis, atom_list: list, debug=False) -> np.array:
    '''
    '''
    size = basis.getsize()
    cnt = 0
    TE = [0.0 for i in range(get_repulsion_index(size,size,size,size))]
    for i in range(size):
        for j in range(i+1):
            ij = pair_index(i,j)
            for k in range(size):
                for l in range(k+1):
                    kl = pair_index(k,l)
                    if ij <= kl:
                        index = get_repulsion_index(i,j,k,l)
                        cnt += 1
                        TE[index] = compute_cgf_repulsion(basis.cgfs[i], basis.cgfs[j], basis.cgfs[k], basis.cgfs[l])
    return TE

def get_B_array(l1: int, l2: int, l3: int, l4: int, p: float, a: float, b: float, q: float, c: float, d: float, g1: float, g2: float, delta: float):
    imax = l1 + l2 + l3 + l4 + 1
    B_arr = [0 for i in range(imax)]
    for i1 in range(l1+l2+1):
        for i2 in range(l3+l4+1):
            for r1 in range(i1//2+1):
                for r2 in range(i2//2+1):
                    for u in range((i1+i2) // 2-r1-r2+1):
                        i = i1 + i2 - 2*(r1+r2) - u
                        B_arr[i] += B_term( \
                            i1,i2,r1,r2,u,l1,l2,l3,l4, \
                            p,a,b,q,c,d,g1,g2,delta)
    return B_arr


def B_term(i1: int, i2: int, r1: int, r2: int, u: int, \
    l1: int, l2: int, l3: int, l4: int, \
    px: float, ax: float, bx: float, qx: float, cx: float, dx: float, \
    gamma1: float, gamma2: float, delta: float):
    '''
    '''
    return fB(i1,l1,l2,px,ax,bx,r1,gamma1) * math.pow(-1,i2) * fB(i2,l3,l4,qx,cx,dx,r2,gamma2) \
        * math.pow(-1,u) * fact_ratio2(i1+i2-2*(r1+r2),u) * math.pow(qx-px,i1+i2-2*(r1+r2)-2*u) / math.pow(delta, i1+i2-2*(r1+r2)-u)

def fB(i: int, l1: int, l2: int, p: float, a: float, b: float, r: int, g: float):
    return compute_binomial_prefactor(i,l1,l2,p-a,p-b) * B0(i,r,g)

def B0(i: int, r: int, g: float):
    return fact_ratio2(i,r) * math.pow(4*g, r-i)

def fact_ratio2(a: int, b: int):
    return factorial(a) / (factorial(b) * factorial(a-2*b))

def get_repulsion_index(i: int, j: int, k: int, l: int):
    ij = pair_index(i,j)
    kl = pair_index(k,l)
    return pair_index(ij,kl)

