#include "basis.h"

Basis::Basis(){
    basisset="none";
}

Basis::Basis(std:: string basissett){
    basisset = basissett;
}

void Basis::setType(std::string basissett){
    basisset = basissett;
}

std::vector<GTO> Basis::getGTOs() const {
    return gtos;
}

void Basis::set(std::string type, int Z, Vec3 r){
    gtos.clear();
    if (basisset.compare("sto-3g") == 0){
        addGTOs_sto3g(type, Z, r);
    //} else if(basisset.compare("sto-6g") == 0) {
    //    addGTOs_sto6g(type, Z, r);
    } else {
        std::cout << "Unrecognized basis set" << std::endl;
        exit(1);
    }
}

// s-orbital
void Basis::addGTO_s(double alpha, double c, Vec3 r){
    gtos.push_back(GTO(c, r, alpha, 0, 0, 0));
}

// px-orbital
void Basis::addGTO_px(double alpha, double c, Vec3 r){
    gtos.push_back(GTO(c, r, alpha, 1, 0, 0));
}

// py-orbital
void Basis::addGTO_py(double alpha, double c, Vec3 r){
    gtos.push_back(GTO(c, r, alpha, 0, 1, 0));
}

// pz-orbital
void Basis::addGTO_pz(double alpha, double c, Vec3 r){
    gtos.push_back(GTO(c, r, alpha, 0, 0, 1));
}

// dx2-orbital
void Basis::addGTO_dx2(double alpha, double c, Vec3 r){
    gtos.push_back(GTO(c, r, alpha, 2, 0, 0));
}

// dy2-orbital
void Basis::addGTO_dy2(double alpha, double c, Vec3 r){
    gtos.push_back(GTO(c, r, alpha, 0, 2, 0));
}

// dz2-orbital
void Basis::addGTO_dz2(double alpha, double c, Vec3 r){
    gtos.push_back(GTO(c, r, alpha, 1, 0, 0));
}

// dxy-orbital
void Basis::addGTO_dxy(double alpha, double c, Vec3 r){
    gtos.push_back(GTO(c, r, alpha, 1, 1, 0));
}

// dxz-orbital
void Basis::addGTO_dxz(double alpha, double c, Vec3 r){
    gtos.push_back(GTO(c, r, alpha, 1, 0, 1));
}

// dyz-orbital
void Basis::addGTO_dyz(double alpha, double c, Vec3 r){
    gtos.push_back(GTO(c, r, alpha, 0, 1, 1));
}

void Basis::addGTOs_sto3g(std::string type, int Z, Vec3 r){
    /* (1) HYDROGEN */
    if (type.compare("1s") == 0 && Z == 1){
        addGTO_s(3.4252509099999999,0.15432897000000001,r);
        addGTO_s(0.62391373000000006, 0.53532813999999995,r);
        addGTO_s(0.16885539999999999, 0.44463454000000002,r);
    }
    /* (2) HELIUM */
    if(type.compare("1s")==0 && Z==2) {
        addGTO_s(6.3624213899999997, 0.15432897000000001,r);
        addGTO_s(1.1589229999999999, 0.53532813999999995,r);
        addGTO_s(0.31364978999999998, 0.44463454000000002,r);
    }
    /* (3) LITHIUM */
    if(type.compare("1s")==0 && Z==3) {
        addGTO_s(16.119575000000001, 0.15432897000000001,r);
        addGTO_s(2.9362007000000001, 0.53532813999999995,r);
        addGTO_s(0.79465050000000004, 0.44463454000000002,r);
    }
    if(type.compare("2s")==0 && Z==3) {
        addGTO_s(0.63628969999999996, -0.099967230000000004,r);
        addGTO_s(0.14786009999999999, 0.39951282999999999,r);
        addGTO_s(0.048088699999999998, 0.70011546999999996,r);
    }
    if(type.compare("2px")==0 && Z==3) {
        addGTO_px(0.63628969999999996, 0.15591627,r);
        addGTO_px(0.14786009999999999, 0.60768372000000004,r);
        addGTO_px(0.048088699999999998, 0.39195739000000002,r);
    }
    if(type.compare("2py")==0 && Z==3) {
        addGTO_py(0.63628969999999996, 0.15591627,r);
        addGTO_py(0.14786009999999999, 0.60768372000000004,r);
        addGTO_py(0.048088699999999998, 0.39195739000000002,r);
    }
    if(type.compare("2pZ")==0 && Z==3) {
        addGTO_pz(0.63628969999999996, 0.15591627,r);
        addGTO_pz(0.14786009999999999, 0.60768372000000004,r);
        addGTO_pz(0.048088699999999998, 0.39195739000000002,r);
    }
    /* (4) BERLYLLIUM */
    if(type.compare("1s")==0 && Z==4) {
        addGTO_s(30.167871000000002, 0.15432897000000001,r);
        addGTO_s(5.4951153000000001, 0.53532813999999995,r);
        addGTO_s(1.4871927, 0.44463454000000002,r);
    }
    if(type.compare("2s")==0 && Z==4) {
        addGTO_s(1.3148331, -0.099967230000000004,r);
        addGTO_s(0.3055389, 0.39951282999999999,r);
        addGTO_s(0.099370700000000006, 0.70011546999999996,r);
    }
    if(type.compare("2px")==0 && Z==4) {
        addGTO_px(1.3148331, 0.15591627,r);
        addGTO_px(0.3055389, 0.60768372000000004,r);
        addGTO_px(0.099370700000000006, 0.39195739000000002,r);
    }
    if(type.compare("2py")==0 && Z==4) {
        addGTO_px(1.3148331, 0.15591627,r);
        addGTO_px(0.3055389, 0.60768372000000004,r);
        addGTO_px(0.099370700000000006, 0.39195739000000002,r);
    }
    if(type.compare("2pz")==0 && Z==4) {
        addGTO_px(1.3148331, 0.15591627,r);
        addGTO_px(0.3055389, 0.60768372000000004,r);
        addGTO_px(0.099370700000000006, 0.39195739000000002,r);
    }
    /* (5) BORON */
    if(type.compare("1s")==0 && Z==5) {
        addGTO_s(48.791113000000003, 0.15432897000000001,r);
        addGTO_s(8.8873622000000001, 0.53532813999999995,r);
        addGTO_s(2.4052669999999998, 0.44463454000000002,r);
    }
    if(type.compare("2s")==0 && Z==5) {
        addGTO_s(2.2369561, -0.099967230000000004,r);
        addGTO_s(0.51982050000000002, 0.39951282999999999,r);
        addGTO_s(0.16906180000000001, 0.70011546999999996,r);
    }
    if(type.compare("2px")==0 && Z==5) {
        addGTO_px(2.2369561, 0.15591627,r);
        addGTO_px(0.51982050000000002, 0.60768372000000004,r);
        addGTO_px(0.16906180000000001, 0.39195739000000002,r);
    }
    if(type.compare("2py")==0 && Z==5) {
        addGTO_px(2.2369561, 0.15591627,r);
        addGTO_px(0.51982050000000002, 0.60768372000000004,r);
        addGTO_px(0.16906180000000001, 0.39195739000000002,r);
    }
    if(type.compare("2pz")==0 && Z==5) {
        addGTO_px(2.2369561, 0.15591627,r);
        addGTO_px(0.51982050000000002, 0.60768372000000004,r);
        addGTO_px(0.16906180000000001, 0.39195739000000002,r);
    }
    /* (6) CARBON */
    if(type.compare("1s")==0 && Z==6) {
        addGTO_s(71.616837000000004, 0.15432897000000001,r);
        addGTO_s(13.045095999999999, 0.53532813999999995,r);
        addGTO_s(3.5305122, 0.44463454000000002,r);
    }
    if(type.compare("2s")==0 && Z==6) {
        addGTO_s(2.9412493999999998, -0.099967230000000004,r);
        addGTO_s(0.68348310000000001, 0.39951282999999999,r);
        addGTO_s(0.22228990000000001, 0.70011546999999996,r);
    }
    if(type.compare("2px")==0 && Z==6) {
        addGTO_px(2.9412493999999998, 0.15591627,r);
        addGTO_px(0.68348310000000001, 0.60768372000000004,r);
        addGTO_px(0.22228990000000001, 0.39195739000000002,r);
    }
    if(type.compare("2py")==0 && Z==6) {
        addGTO_py(2.9412493999999998, 0.15591627,r);
        addGTO_py(0.68348310000000001, 0.60768372000000004,r);
        addGTO_py(0.22228990000000001, 0.39195739000000002,r);
    }
    if(type.compare("2pz")==0 && Z==6) {
        addGTO_pz(2.9412493999999998, 0.15591627,r);
        addGTO_pz(0.68348310000000001, 0.60768372000000004,r);
        addGTO_pz(0.22228990000000001, 0.39195739000000002,r);
    }
    /* (7) NITROGEN */
    if(type.compare("1s")==0 && Z==7) {
        addGTO_s(99.106168999999994, 0.15432897000000001,r);
        addGTO_s(18.052312000000001, 0.53532813999999995,r);
        addGTO_s(4.8856602000000002, 0.44463454000000002,r);
    }
    if(type.compare("2s")==0 && Z==7) {
        addGTO_s(3.7804559000000002, -0.099967230000000004,r);
        addGTO_s(0.87849659999999996, 0.39951282999999999,r);
        addGTO_s(0.28571439999999998, 0.70011546999999996,r);
    }
    if(type.compare("2px")==0 && Z==7) {
        addGTO_px(3.7804559000000002, 0.15591627,r);
        addGTO_px(0.87849659999999996, 0.60768372000000004,r);
        addGTO_px(0.28571439999999998, 0.39195739000000002,r);
    }
    if(type.compare("2py")==0 && Z==7) {
        addGTO_py(3.7804559000000002, 0.15591627,r);
        addGTO_py(0.87849659999999996, 0.60768372000000004,r);
        addGTO_py(0.28571439999999998, 0.39195739000000002,r);
    }
    if(type.compare("2pz")==0 && Z==7) {
        addGTO_pz(3.7804559000000002, 0.15591627,r);
        addGTO_pz(0.87849659999999996, 0.60768372000000004,r);
        addGTO_pz(0.28571439999999998, 0.39195739000000002,r);
    }
    /* (8) OXYGEN */
    if(type.compare("1s")==0 && Z==8) {
        addGTO_s(130.70931999999999, 0.15432897000000001,r);
        addGTO_s(23.808861, 0.53532813999999995,r);
        addGTO_s(6.4436083000000002, 0.44463454000000002,r);
    }
    if(type.compare("2s")==0 && Z==8) {
        addGTO_s(5.0331513000000001, -0.099967230000000004,r);
        addGTO_s(1.1695960999999999, 0.39951282999999999,r);
        addGTO_s(0.38038899999999998, 0.70011546999999996,r);
    }
    if(type.compare("2px")==0 && Z==8) {
        addGTO_px(5.0331513000000001, 0.15591627,r);
        addGTO_px(1.1695960999999999, 0.60768372000000004,r);
        addGTO_px(0.38038899999999998, 0.39195739000000002,r);
    }
    if(type.compare("2py")==0 && Z==8) {
        addGTO_py(5.0331513000000001, 0.15591627,r);
        addGTO_py(1.1695960999999999, 0.60768372000000004,r);
        addGTO_py(0.38038899999999998, 0.39195739000000002,r);
    }
    if(type.compare("2pz")==0 && Z==8) {
        addGTO_pz(5.0331513000000001, 0.15591627,r);
        addGTO_pz(1.1695960999999999, 0.60768372000000004,r);
        addGTO_pz(0.38038899999999998, 0.39195739000000002,r);
    }
}











