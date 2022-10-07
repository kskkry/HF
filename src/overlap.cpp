#include "overlap.h"

double cgf_overlap(CGF &cgf1, CGF &cgf2) {
    unsigned int i = cgf1.gtos.size();
    unsigned int j = cgf2.gtos.size();

    double sum = 0;
    double norm1, norm2;

    for(unsigned int k = 0; k < i; k++) {
        for(unsigned int l = 0; l < j; l++) {
            norm1 = cgf1.gtos[k].norm;
            norm2 = cgf2.gtos[l].norm;
            sum += cgf1.gtos[k].coef * cgf2.gtos[l].coef * norm1 * norm2 * gto_overlap(cgf1.gtos[k], cgf2.gtos[l]);
        }
    }

    return sum;
}

double gto_overlap(GTO &gto1, GTO &gto2) {
    return overlap(gto1.alpha, gto1.l, gto1.m, gto1.n, gto1.r,
        gto2.alpha, gto2.l, gto2.m, gto2.n, gto2.r);
}

double overlap(double alpha1, int l1, int m1, int n1, Vec3 &a,
    double alpha2, int l2, int m2, int n2, Vec3 &b) {

    double rab2 = dist_sqr(a,b);
    double gamma = alpha1 + alpha2;
    Vec3 p = gaussian_product_center(alpha1, a, alpha2, b);

    double pre = pow(PI / gamma,1.5) * exp(-alpha1 * alpha2 * rab2 / gamma);
    double wx = overlap_1D(l1, l2, p.getx()-a.getx(), p.getx()-b.getx(), gamma);
    double wy = overlap_1D(m1, m2, p.gety()-a.gety(), p.gety()-b.gety(), gamma);
    double wz = overlap_1D(n1, n2, p.getz()-a.getz(), p.getz()-b.getz(), gamma);

    return pre*wx*wy*wz;
}

double overlap_1D(int l1, int l2, double x1, double x2, double gamma) {
    double sum = 0;

    for(int i=0; i < (1 + floor(0.5*(l1+l2))); i++) {
        sum += binomial_prefactor(2*i, l1, l2, x1, x2) *
        factorial2(2*i-1)/pow(2*gamma,i);
    }

    return sum;
}