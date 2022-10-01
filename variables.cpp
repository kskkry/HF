#include <iostream>
#include <algorithm>
#include "systemparam.hpp"
#include "variables.hpp"

// string -> std::string?
int get_Z_val(std::string name){
    if (name[0] == 'H') return 1;
    else if (name == "He") return 2;
    else if (name == "Li") return 3;
    else if (name == "Be") return 4;
    else if (name[0] == 'B') return 5;
    else if (name[0] == 'C') return 6;
    else if (name[0] == 'N') return 7;
    else if (name[0] == 'N') return 7;
    else if (name[0] == 'O') return 8;
    else if (name[0] == 'F') return 9;
    else if (name == "Ne") return 10;
    else if (name == "Na") return 11;
    else if (name == "Mg") return 12;
    else if (name == "Al") return 13;
    else if (name == "Si") return 14;
    else if (name[0] == 'P') return 15;
    else if (name[0] == 'S') return 16;
    else if (name == "Cl") return 17;
    else if (name == "Ar") return 18;
    else return -1;
}

void Variables::add_atoms(std::string name, double x, double y, double z){
    Atom atom;
    atom.name = name;
    atom.x = x;
    atom.y = y;
    atom.z = z;
    atom.Z = get_Z_val(name);
    atoms.push_back(atom);
}


