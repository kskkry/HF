import math
import numpy as np
from config import Config
from geometry import Atom, Vec
from scipy.special import gamma, gammainc
cfg = Config()

def compute_dist2(atom1: Atom, atom2: Atom):
    return (atom1.x - atom2.x)**2.0 + (atom1.y - atom2.y)**2.0 + (atom1.z - atom2.z)**2.0

def compute_dist(atom1: Atom, atom2: Atom):
    return np.sqrt(compute_dist2(atom1, atom2))

def compute_gaussian_product_center(alpha1, atom1: Atom, alpha2, atom2: Atom)-> Vec:
    gamma = alpha1 + alpha2
    newx = (alpha1 * atom1.getx() + alpha2 * atom2.getx()) / gamma
    newy = (alpha1 * atom1.gety() + alpha2 * atom2.gety()) / gamma
    newz = (alpha1 * atom1.getz() + alpha2 * atom2.getz()) / gamma
    return Vec(newx, newy, newz)

def factorial(n: int):
    if n <= 1:
        return 1
    else:
        return factorial(n-1)

def factorial2(n: int):
    if n <= 1:
        return 1
    else:
        return factorial2(n-2)

def compute_binomial(a: int, b: int):
    if a <= b:
        AttributeError()
    return factorial(a) / (factorial(b) * factorial(a-b))

def compute_binomial_prefactor(s: int, ia: int, ib: int, xpa: float, xpb: float)-> float:
  sum_val=0.0
  for t in range(s+1):
    if ((s-ia) <= t) and (t <= ib):
      sum_val += compute_binomial(ia,s-t)*compute_binomial(ib,t)*math.pow(xpa,ia-s+t)*math.pow(xpb,ib-t)
  return sum_val

def compute_diag(mx: np.array):
    assert mx.shape[0] == mx.shape[1]
    eig = np.linalg.eig(mx)
    eig_val = np.diag(eig[0])
    eig_vec = eig[1]
    return  eig_val, eig_vec

def Fgamma(a: float, x: float):
    '''
    Ref:
    -   https://github.com/RMeli/Hartree-Fock/blob/master/Python/integrals.py
    -   Evaluation of the Boys Function using Analytical Relations
        I.I.Guseinov and B.A.Mamedov, Journal of Mathematical Chemistry, 2006
    
    scipy.special.gamma:    https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.gamma.html
    scipy.special.gammainc: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.gammainc.html
    lower-incomplete-gamma-function = gamma * gammainc
    '''
    if x < cfg.getEPS():
        val = 1 / (2*a + 1) - x / (2*a + 3)
    else:
        val = 0.5 / x**(a + 0.5) * gamma(a + 0.5) * gammainc(a + 0.5, x)
    return val
        
        
    