import numpy as np
from geometry import Atom, Vec

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
      sum_val += compute_binomial(ia,s-t)*compute_binomial(ib,t)*np.pow(xpa,ia-s+t)*np.pow(xpb,ib-t)
  return sum_val

