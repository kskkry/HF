#include <iostream>
#include "hf.h"
#include "systemparam.h"
#include "variables.h"

HF::HF(void){
    vars = new Variables();
}

HF::~HF(void){
    delete vars;
}

void HF::read_input(void){
    // declare variables
    std::string basis_function;
    std::string element;
    int n_atoms;
    double x, y, z;

    // read inputs information
    std::cin >> basis_function >> n_atoms;
    this->basis_function = basis_function;
    for (int i = 0; i < n_atoms; i++){
        std::cin >> element >> x >> y >> z;
        vars->add_atoms(element, x, y, z);
    }

    // check
    std::cout << "basis_function = " << this->basis_function << std::endl;
    std::cout << vars->atoms[0].name << " " << (double)vars->atoms[0].Z << " " << vars->atoms[0].x << " " << vars->atoms[0].y << " " << vars->atoms[0].z << " ";
    std::cout << std::endl;
}

void HF::run(void){
    read_input();
}

