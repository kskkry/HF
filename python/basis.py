import sys
import json
import math
import numpy as np
from config import Config
from geometry import Vec, Atom
from functions import factorial, factorial2
cfg = Config()

class ReadBasis(object):
    def __init__(self, basis_type: str, atom_list: list) -> None:
        self.basis_type = basis_type  # str
        self.atom_list = atom_list    # list of Atom class
        self.atom_int_list = [atom.element for atom in self.atom_list] # list of element-integer
        
        basis_list = ["sto-3g", "sto-6g", "6-31g"]
        json_load = None

        # Read Basisset
        if self.basis_type in basis_list:
            json_open = open(f"./python/basisset/{self.basis_type}.json", 'r')
            json_load = json.load(json_open) # type: dict
            
        # 基底関数の入力が正しければ、具体的な値を ./python/basisset/*.json から取り出す
        if json_load is not None:
            self.basis4compute_dict = self.get_basis_value(json_load, self.atom_int_list)
            self._basis = self.get_concat_basis_vector(self.atom_list)
        else:
            print("Input Following Basis Function that is Supported")
            print()
            print("=====Basis Function Option==================================================")
            for bas in basis_list:
                print(f" - {bas}")
            print("============================================================================")
            sys.exit()

    def get_basis(self):
        return self._basis
            
    def get_basis_value(self, json_load: dict, atom_int_list: list) -> dict:
        # 具体的な基底関数の値の取り出し（alpha, coefficient, angular moment）
        elements = json_load["elements"]
        basis_use_dict = {}
        for atom_index in elements.keys():
            atom_int = int(atom_index)
            if (atom_int in atom_int_list) is True:
                basis_use_dict = {**basis_use_dict, atom_index: elements[atom_index]}
        return basis_use_dict

    def get_atom_basis_vector(self, atom: Atom) -> list:
        # Input: atom: Atom Object
        # Return: CGF-List
        basis_atom_list = self.basis4compute_dict[str(atom.element)]["electron_shells"]
        gto_s_list, gto_px_list, gto_py_list, gto_pz_list = [], [], [], []
        cgf_list = []
        for basis_dict in basis_atom_list:
            for angular_val in basis_dict["angular_momentum"]:
                gto_s_list, gto_px_list, gto_py_list, gto_pz_list = [], [], [], []
                for index in range(len(basis_dict["exponents"])):
                    alpha = float(basis_dict["exponents"][index])
                    coeff = float(basis_dict["coefficients"][angular_val][index])
                    if angular_val == 0:
                        gto_s_list.append(GTO(alpha, coeff, 0, 0, 0, atom))
                    elif angular_val == 1:
                        gto_px_list.append(GTO(alpha, coeff, 1, 0, 0, atom))
                        gto_py_list.append(GTO(alpha, coeff, 0, 1, 0, atom))
                        gto_pz_list.append(GTO(alpha, coeff, 0, 0, 1, atom))

                if len(gto_s_list) > 0:
                    cgf_s = CGF(gto_s_list)
                    cgf_list.append(cgf_s)
                if len(gto_px_list) > 0:
                    cgf_px = CGF(gto_px_list)
                    cgf_list.append(cgf_px)
                if len(gto_py_list) > 0:
                    cgf_py = CGF(gto_py_list)
                    cgf_list.append(cgf_py)
                if len(gto_pz_list) > 0:
                    cgf_pz = CGF(gto_pz_list)
                    cgf_list.append(cgf_pz)
        return cgf_list

    def get_concat_basis_vector(self, atom_list: list):
        # atom_list: list of Atom Object
        mol_cgf_list = []
        for atom in atom_list:
            cgf_list = self.get_atom_basis_vector(atom)
            mol_cgf_list.extend(cgf_list)
        basis = Basis(mol_cgf_list)
        return basis
        

class GTO(object):
    def __init__(self, alpha:float, coeff: float, l: int, m: int, n: int, atom: Atom) -> None:
        self.alpha = alpha
        self.coeff = coeff
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
        nom = math.pow(2.0, 2.0*(l+m+n)+3.0/2.0) * math.pow(alpha, (l+m+n)+3.0/2.0)
        denom = factorial2(2*l-1)*factorial2(2*m-1)*factorial2(2*n-1)*math.pow(cfg.getPI(), 3.0/2.0)
        return np.sqrt(nom / denom)

class CGF(object):
    def __init__(self, GTO_list:list) -> None:
        self.gtos = GTO_list

    def getsize(self) -> int:
        return len(self.gtos)

class Basis(object):
    def __init__(self, CGF_list: list) -> None:
        self.cgfs = CGF_list
    
    def getsize(self) -> int:
        return len(self.cgfs)


