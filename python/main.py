import sys
import numpy as np
from Input import input

'''
args[0]: xxx.py
args[1]: (path)./yyy.txt
'''
args = sys.argv


def main():
    with open(args[1]) as f:
        lines = f.readlines()
    basis_type,natom,atom_list = input(lines)
    print(atom_list)
    pass


if __name__ == "__main__":
    main()

















