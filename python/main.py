import sys
import numpy as np
from basis import ReadBasis
from geometry import Atom
from Input import read_input
from hf import HF

'''
args[0]: xxx.py
args[1]: (path)./yyy.txt
'''
args = sys.argv


def main():
    # 1. 入力
    with open(args[1]) as f:
        input_lines = f.readlines()
    basis_type,natoms,atom_list = read_input(input_lines)
    
    # 2. 基底関数の取出し
    hf = HF(basis_type, natoms, atom_list)
    #rb = ReadBasis(basis_type, atom_list)
    #mol_cgf_list = list(rb.get_mol_cgf_list)

    # 3. HF-Roothaan法の実行
    hf.run()


if __name__ == "__main__":
    main()

















