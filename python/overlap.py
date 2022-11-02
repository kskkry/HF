import math
import numpy as np
from geometry import Atom, Vec
from config import Config
from functions import compute_dist2, compute_gaussian_product_center, compute_binomial_prefactor, factorial, factorial2
cfg = Config

def compute_overlap_1D(l1: int, l2: int, x1: float, x2: float, gamma: float):
    sum = 0.0
    for i in range(1+math.floor(0.5*(l1+l2))):
        sum += compute_binomial_prefactor(2*i, l1, l2, x1, x2) * factorial2(2*i-1)/np.pow(2*gamma,i)
    return sum

def compute_overlap(alpha1:float, l1:int,m1:int, n1:int, atom1: Atom, alpha2:float, l2:int, m2:int, n2:int, atom2:Atom) -> float:
    dist2 = compute_dist2(atom1, atom2)
    gamma = alpha1 + alpha2
    pos = compute_gaussian_product_center(alpha1, atom1, alpha2, atom2)
    pre = np.pow(cfg.PI / gamma, 1.5) * np.exp(-alpha1 * alpha2 * dist2 / gamma)
    wx = compute_overlap_1D(l1, l2, pos.getx()-atom1.getx(), pos.getx()-atom2.getx(), gamma);
    wy = compute_overlap_1D(m1, m2, pos.gety()-atom1.gety(), pos.gety()-atom2.gety(), gamma);
    wz = compute_overlap_1D(n1, n2, pos.getz()-atom1.getz(), pos.getz()-atom2.getz(), gamma);
    return pre*wx*wy*wz

def compute_gto_overlap():
    pass