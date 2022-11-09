import numpy as np
from basis import ReadBasis, Basis
from geometry import Atom
from overlap import get_overlap_mx
from kinetics import get_kinetics_mx
from functions import compute_diag

class HF(ReadBasis):
    def __init__(self, basis_type: str, natoms: int, atom_list: list, debug=False) -> None:
        super().__init__(basis_type, atom_list)
        self.basis_type = basis_type
        self.natoms = natoms
        self.atom_list = atom_list
        self.debug = debug
        self.basis = self.get_basis()
        self.raw_overlap_mx = get_overlap_mx(self.basis, self.basis, debug=self.debug)
        self.raw_kinetics_mx = get_kinetics_mx(self.basis, self.basis, debug=self.debug)
        self.overlap_eig_val, self.overlap_eig_vec = compute_diag(self.raw_overlap_mx)

    def run(self,debug=True):
        pass
        










