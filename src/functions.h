#include<cmath>
#include "vec3.h"
#include "systemparam.h"

/* functions for binomial expansion */
double binomial_prefactor(int s, int m1, int m2, double x1, double x2);
int binomial(int a, int b);
int factorial(int a);
int factorial2(int a);

/* functions for vectors */
double dist(const Vec3 &a, const Vec3 &b);
double dist_sqr(const Vec3 &a, const Vec3 &b);
Vec3 gaussian_product_center(const double &alpha1, const Vec3 &a, 
  const double &alpha2, const Vec3 &b);

/* swap functions */
void swap(unsigned int &i, unsigned int &j);


