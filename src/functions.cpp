#include "functions.h"

double dist(const Vec3 &a, const Vec3 &b){
    return sqrt(dist_sqr(a, b));
}

double dist_sqr(const Vec3 &a, const Vec3 &b) {
    return pow(a.getx() - b.getx(),2.0) + pow(a.gety() - b.gety(),2.0) + pow(a.getz() - b.getz(),2.0);
}

double binomial_prefactor(int s, int ia, int ib, double xpa, double xpb){
  int t;
  double sum=0.;
  for (t=0; t<s+1; t++)
    if ((s-ia <= t) && (t <= ib))
      sum += binomial(ia,s-t)*binomial(ib,t)*pow(xpa,ia-s+t)*pow(xpb,ib-t);
  return sum;
}

int factorial(int a){
    return a <= 1 ? 1 : a*factorial(a-1);
}

int factorial2(int a){
    return a <= 1 ? 1 : a*factorial2(a-2);
}

int binomial(int a, int b) {
    return factorial(a) / (factorial(b) * factorial(a-b));
}

Vec3 gaussian_product_center(const double &alpha1, const Vec3 &a, const double &alpha2, const Vec3 &b) {
    double gamma = alpha1 + alpha2;
    double x = (alpha1 * a.getx() + alpha2 * b.getx()) / gamma;
    double y = (alpha1 * a.gety() + alpha2 * b.gety()) / gamma;
    double z = (alpha1 * a.getz() + alpha2 * b.getz()) / gamma;

    return Vec3(x,y,z);
}

void swap(unsigned int &i, unsigned int &j) {
    unsigned int m = i;
    i = j;
    j = m;
}