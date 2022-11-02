import sys
import numpy as np
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
        lines = f.readlines()
    basis_type,natoms,atom_list = read_input(lines)
    # 2. 基底
    ## sto-3g
    hf = HF(basis_type,natoms,atom_list)
    pass


if __name__ == "__main__":
    main()

















