#ifndef _CGF_H
#define _CGF_H

#include<iostream>
#include<vector>
#include<string>
#include "vec3.h"
#include "gto.h"

/*
Contracted Gaussian Function
*/

class CGF{
    public:
    std::vector<GTO> gtos;
    Vec3 r;
    std::string type;

    public:
    CGF(const std::string typee, const unsigned int z, const Vec3 &rr, std::vector<GTO> gtoss);
    const std::string orb() const;

    friend std::ostream& operator <<(std::ostream &os,const CGF &rhs);
};

#endif //_CGF_H