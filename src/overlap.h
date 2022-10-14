#include "gto.h"
#include "cgf.h"
#include "systemparam.h"
#include "functions.h"

double cgf_overlap(CGF &cgf1, CGF &cgf2);
double gto_overlap(GTO &gto1, GTO &gto2);
double overlap(double alpha1, int l1, int m1, int n1, Vec3 &a,
double alpha2, int l2, int m2, int n2, Vec3 &b);
double overlap_1D(int l1, int l2, double x1, double x2, double gamma);