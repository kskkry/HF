import numpy as np
from basis import ReadBasis, Basis
from geometry import Atom
from overlap import get_overlap_mx
from kinetics import get_kinetics_mx
from nuclear import get_nuclear_mx
from repulsion import get_repulsion_list
from functions import compute_diag, pair_index, get_canonical_othogonal, compute_nuclear_repulsion

class HF(ReadBasis):
    def __init__(self, basis_type: str, natoms: int, atom_list: list, n_step = 10, debug=False) -> None:
        super().__init__(basis_type, atom_list)
        self.basis_type = basis_type
        self.natoms = natoms
        self.atom_list = atom_list
        self.n_step = n_step
        self.debug = debug

        # get from basis-function-json-file
        self.basis = self.get_basis()

        # initialize
        self.C_mx = np.zeros((self.basis.getsize(), self.basis.getsize()))
        self.Cprime_mx = np.zeros((self.basis.getsize(), self.basis.getsize()))
        self.P_mx = np.zeros((self.basis.getsize(), self.basis.getsize()))

        self.raw_S_mx = get_overlap_mx(self.basis, self.basis, debug=self.debug)
        self.raw_kinetics_mx = get_kinetics_mx(self.basis, self.basis, debug=self.debug)
        self.raw_nuclear_mx = get_nuclear_mx(self.basis, self.basis, self.atom_list, debug=self.debug)
        self.raw_TE_list = get_repulsion_list(self.basis, self.atom_list, debug=True)

        # core-core-repulsion-value
        self.nuclear_repulsion_val = compute_nuclear_repulsion(self.atom_list)

        # X: transform matrix for S
        self.X_mx = get_canonical_othogonal(self.raw_S_mx, debug=self.debug)

        # 
        self.raw_H_mx = self.raw_kinetics_mx + self.raw_nuclear_mx
        self.G_mx = np.zeros((self.basis.getsize(), self.basis.getsize()))
        

    def run(self,debug=True):
        for step in range(self.n_step):
            continue
        
    def step(self):
        for i in range(self.basis.getsize()):
            for j in range(self.basis.getsize()):
                # initialize
                self.G_mx[i,j] = 0.0
                for k in range(self.basis.getsize()):
                    for l in range(self.basis.getsize()):
                        id1 = pair_index(i,j,k,l)
                        id2 = pair_index(i,k,l,j)
                        self.G_mx[i,j] += self.P_mx[k,l] * (self.TE[id1] - 0.5*self.raw_TE[id2])

        F_mx = self.raw_H_mx + self.G_mx
        Fprime_mx = self.X_mx.T * F_mx * self.X_mx










