import numpy as np
from config import Config
from Geometry import Vec, Atom
cfg = Config()

class GTO(object):
    def __init__(self, alpha:float, coef: float, l: int, m: int, n: int, atom: Atom) -> None:
        self.alpha = alpha
        self.coeff = coef
        self.atom = atom
        self.x = atom.getx()
        self.y = atom.gety()
        self.z = atom.getz()
        self.l = l
        self.m = m
        self.n = n
        self.norm = self.compute_norm(alpha, l, m, n)
    
    def compute_norm(self, alpha: float, l:int, m:int, n:int):
        '''
        normalization constant value for gaussian type orbital(GTO)
        ref: p27, Nakai
        '''
        nom = np.pow(2.0, 2.0*(l+m+n)+3.0/2.0) * np.pow(alpha, (l+m+n)+3.0/2.0)
        denom = factorial2(2*l-1)*factorial2(2*m-1)*factorial2(2*n-1)*np.pow(cfg.getPI(), 3.0/2.0)
        return np.sqrt(nom / denom)

class CGF(object):
    def __init__(self, GTO_list:list) -> None:
        self.gtos = GTO_list

    def getsize(self) -> int:
        return len(self.gtos)



