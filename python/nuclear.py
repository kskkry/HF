import math
import numpy as np
from basis import GTO, CGF, Basis
from config import Config
from functions import compute_binomial_prefactor, factorial, compute_gaussian_product_center
from geometry import Atom, Vec
from overlap import compute_gto_overlap, compute_overlap
cfg = Config()

def compute_gto_nuclear(gto1: GTO, gto2: GTO):
    '''
    '''
    pass

def compute_cgf_nuclear(cgf1: CGF, cgf2: CGF):
    '''
    '''
    pass

def get_nuclear_mx(basis1: Basis, basis2: Basis, debug=False):
    '''
    '''
    pass

def A_term(l: int, r: int, i: int, l1: int, l2: int, xa: float, xb: float, xc: float, gamma: float):
    '''
    Ref: Handbook of Computational Quantum Chemistry, Cook, p.245
    '''
    val = math.pow(-1,l) * compute_binomial_prefactor(l, l1, l2, xa, xb) * math.pow(-1, i) \
        * factorial(l) * math.pow(xc, l-2*r-2*i) * math.pow(0.25 / gamma, r+i) / factorial(r) / factorial(i) / factorial(l-2*r-2*i)
    
    
    
