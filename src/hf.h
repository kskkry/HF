#pragma once
#include "systemparam.h"
#include "variables.h"

class HF {
private:
    std::string basis_function;
    Variables *vars;
    void read_input(void);
public:
    HF(void);
    ~HF(void);
    void run(void);
};
