#pragma once
#include <iostream>
#include <cmath>
#include "systemparam.h"
#include "variables.h"
#include "vec3.h"

class GTO {
private:
    double compute_radius();
    double compute_norm();
public:
    int l, m, n;
    double alpha, coef;
    double x, y, z, norm;
    Vec3 r;
    GTO(double coeff, Vec3 rr, double alphaa, int ll, int mm, int nn);
    /*
    GTO: x^l * y^m + z^n * exp(-alpha*r^2), r^2 = x^2 + y^2 + z^2
    */
};


