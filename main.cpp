#include <iostream>
#include "hf.h"

int main(void){
    HF *hf = new HF();
    hf->run();
    delete hf;
}