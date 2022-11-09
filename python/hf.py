import numpy as np
from basis import ReadBasis
from geometry import Atom
from overlap import get_overlap_mx
from functions import compute_diag

class HF(ReadBasis):
    def __init__(self, basis_type: str, natoms: int, atom_list: list) -> None:
        super().__init__(basis_type, atom_list)
        self.basis_type = basis_type
        self.natoms = natoms
        self.atom_list = atom_list
        self.mol_cgf_list = self.get_mol_cgf_list()
        self.raw_overlap_mx = self.get_cgf_mx()
        self.overlap_eig_val, self.overlap_eig_vec = compute_diag(self.raw_overlap_mx)
        print(self.overlap_eig_vec)


    def get_cgf_mx(self):
        return get_overlap_mx(self.mol_cgf_list, self.mol_cgf_list)

    def run(self,debug=True):
        pass
        










