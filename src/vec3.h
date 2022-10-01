#pragma once
#include <iostream>
#include <vector>

class Vec3 {
private:
    double x, y, z;
public:
    Vec3();
    Vec3(const double xx, const double yy, const double zz);
    const double getx();
    const double gety();
    const double getz();
    const double get_radius();
};

