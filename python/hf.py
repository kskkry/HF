import numpy as np
from basis import ReadBasis, Basis
from geometry import Atom
from config import Config
from overlap import get_overlap_mx
from kinetics import get_kinetics_mx
from nuclear import get_nuclear_mx
from repulsion import get_repulsion_list
from functions import compute_diag, pair_index, get_canonical_othogonal, compute_nuclear_repulsion
cfg = Config()

class HF(ReadBasis):
    def __init__(self, basis_type: str, natoms: int, atom_list: list, n_step = 100, alpha=0.5, debug=False) -> None:
        super().__init__(basis_type, atom_list)
        self.basis_type = basis_type
        self.natoms = natoms
        self.atom_list = atom_list
        self.n_step = n_step
        self.alpha = alpha
        self.debug = debug
        self.energy_list = []

        # get from basis-function-json-file
        self.basis = self.get_basis()

        # initialize
        self.C_mx = np.eye((self.basis.getsize()))
        self.Cprime_mx = np.zeros((self.basis.getsize(), self.basis.getsize()))
        self.P_mx = self.C_mx.T * self.C_mx

        self.raw_S_mx = get_overlap_mx(self.basis, self.basis, debug=self.debug)
        self.raw_kinetics_mx = get_kinetics_mx(self.basis, self.basis, debug=self.debug)
        self.raw_nuclear_mx = get_nuclear_mx(self.basis, self.basis, self.atom_list, debug=self.debug)
        self.raw_TE_list = get_repulsion_list(self.basis, self.atom_list, debug=True)

        # core-core-repulsion-value
        self.nuclear_repulsion_val = compute_nuclear_repulsion(self.atom_list, debug=self.debug)

        # X: transform matrix for S
        self.X_mx = get_canonical_othogonal(self.raw_S_mx, debug=self.debug)

        # 
        self.raw_H_mx = self.raw_kinetics_mx + self.raw_nuclear_mx
        self.G_mx = np.zeros((self.basis.getsize(), self.basis.getsize()))

        #===========================================================================================================================================================
        if self.debug:
            S_mx = self.X_mx * self.raw_S_mx
            '''
            print as matrix format
            '''
            print("\n===== overlap matrix ==========================================================================================================================")
            size = S_mx.shape[0]
            for id1 in range(size):
                for id2 in range(size):
                    if id2 == size-1:
                        print(f"{S_mx[id1, id2]:.5e}")
                    else:
                        print(f"{S_mx[id1, id2]:.5e}", end=',  ')
            print("===============================================================================================================================================\n")
        #===========================================================================================================================================================
    

    def run(self,debug=True):
        self.H_mx = self.X_mx.T * self.raw_H_mx * self.X_mx
        for step in range(self.n_step):
            self.step(iter=step)
            if step >= 1 and np.abs(self.energy_list[-1] - self.energy_list[-2]) < cfg.getEPS():
                break
        
    def step(self, iter):
        for i in range(self.basis.getsize()):
            for j in range(self.basis.getsize()):
                # initialize
                id1 = pair_index(i,j)
                self.G_mx[i,j] = 0.0
                for k in range(self.basis.getsize()):
                    for l in range(self.basis.getsize()):
                        id2 = pair_index(l,j)
                        id = pair_index(id1, id2)
                        self.G_mx[i,j] += self.P_mx[k,l] * (self.raw_TE_list[id1] - 0.5*self.raw_TE_list[id2])

        F_mx = self.raw_H_mx + self.G_mx
        Fprime_mx = self.X_mx.T * F_mx * self.X_mx
        mo_energy, Cprime_mx = compute_diag(Fprime_mx)
        C_mx = self.X_mx * Cprime_mx
        Pnew_mx = np.zeros((F_mx.shape[0], F_mx.shape[0]))
        for i in range(Pnew_mx.shape[0]):
            for j in range(Pnew_mx.shape[0]):
                for k in range(Pnew_mx.shape[0]):
                    Pnew_mx[i,j] = 2.0 * C_mx[i,k] * C_mx[k,j]
        
        for i in range(Pnew_mx.shape[0]):
            for j in range(Pnew_mx.shape[0]):
                self.P_mx[i,j] = (1-self.alpha) * Pnew_mx[i,j] + self.alpha * self.P_mx[i,j]

        RHF_energy = (self.P_mx * (self.H_mx + Fprime_mx)).sum().sum() * 0.5 + self.nuclear_repulsion_val
        
        print(f"step: {iter+1} RHF-Energy= {RHF_energy}")
        
        self.energy_list.append(RHF_energy)

