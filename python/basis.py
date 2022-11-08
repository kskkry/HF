import json
import numpy as np
from config import Config
from geometry import Vec, Atom
from functions import factorial, factorial2
cfg = Config()

class ReadBasis(object):
    def __init__(self, basis_type) -> None:
        self.basis_type = basis_type
        lines = None
        basis_list = ["sto-3g", "sto-6g", "6-31g"]
        json_load = None
        # read basisset
        if self.basis_type in basis_list:
            json_open = open(f"./python/basisset/{self.basis_type}.json", 'r')
            json_load = json.load(json_open) # type: dict
            
                
        # 基底関数の入力が正しければ、具体的な値を ./basisset/*.in から取り出す
        if json_load is not None:
            self.get_basis_value(json_load)
        else:
            pass 
            
    def get_basis_value(self, json_load):
        # 具体的な基底関数の値の取り出し（alpha, coefficient, angular moment）
        elements = json_load["elements"]
        print(type(elements))
        

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



