#include "gto.h"

GTO::GTO(double coeff, Vec3 rr, double alphaa, int ll, int mm, int nn){
    coef = coeff;
    r = rr;
    x = r.getx();
    y = r.gety();
    z = r.getz();
    alpha = alphaa;
    l = ll;
    m = mm; 
    n = nn;
}

double GTO::compute_radius(){
    double tmp = pow(x,2.0) + pow(y,2.0) + pow(z, 2.0);
    return sqrt(tmp);
}
