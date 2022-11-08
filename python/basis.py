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
        # read basisset
        if self.basis_type == "sto-3g":
            print(self.basis_type)
            with open(f"./python/basisset/{self.basis_type}.in") as f:
                lines = f.readlines()
        elif self.basis_type == "sto-6g":
            with open(f"./python/basisset/{self.basis_type}.in") as f:
                lines = f.readlines()
                
        # 基底関数の入力が正しければ、具体的な値を ./basisset/*.in から取り出す
        if lines is None:
            pass
        else:
            self.get_basis_value(lines)
            
    def get_basis_value(self, lines):
        '''
        具体的な基底関数の値の取り出し（alpha, coefficient, angular moment）
        '''
        for line in lines:
            if str(line[0]).replace(" ", "").replace("\n", "") == "!" or str(line).replace(" ", "") == "\n":
                continue
            elif str(line[:4] == "****"):
                continue
            else:
                print(line.replace("\n", ""))
        

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



