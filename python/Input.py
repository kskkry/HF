from geometry import Atom

def read_input(lines):
    natoms = -1
    basis = None
    atom_list = []
    for index, line in enumerate(lines):
        if index == 0:
            basis = str(line).lower()
        elif index == 1:
            natoms = int(line)
        else:
            element,x,y,z = line.split()[0], float(line.split()[1]), float(line.split()[2]), float(line.split()[3])
            atom = Atom(element,x,y,z)
            atom_list.append(atom)
    return basis, natoms, atom_list


