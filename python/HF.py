import numpy as np
from basis import ReadBasis
from geometry import Atom

class HF(object):
    def __init__(self, basis_type:str, natoms:int, atom_list:list) -> None:
        self.basis_type = basis_type
        self.natoms = natoms
        self.atom_list = atom_list

    def run(self,debug=True):
        pass
        










