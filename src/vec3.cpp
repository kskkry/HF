#include <cmath>
#include "vec3.h"

Vec3::Vec3(){
    x = 0;
    y = 0;
    z = 0;
}

Vec3::Vec3(const double xx, const double yy, const double zz){
    x = xx;
    y = yy;
    z = zz;

}
const double Vec3::getx() const {
    return x;
}

const double Vec3::gety() const {
    return y;
}

const double Vec3::getz() const {
    return z;
}

const double Vec3::get_radius() const{
    double tmp = pow(x,2.0) + pow(y, 2.0) + pow(z, 2.0);
    return tmp;
}
