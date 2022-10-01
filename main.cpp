#include <iostream>
#include "hf.hpp"

int main(void){
    HF *hf = new HF();
    hf->run();
    delete hf;
}