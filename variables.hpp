#pragma once
#include <vector>
#include <iostream>
#include <algorithm>

struct Atom {
    std::string name;
    double Z;
    double x,y,z;
};

class Variables {
public:
    std::vector<Atom> atoms;
    std::string basis_function;
    void add_atoms(std::string name, double x, double y, double z);
    int n_atoms(void){ return static_cast<int>(atoms.size());}
};



