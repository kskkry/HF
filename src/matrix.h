#include <iostream>
#include <vector>
using namespace std;

class Matrix{
  private:
    vector<double> get_column(vector<vector<double>> x, int n);
    double dot(vector<double> x, vector<double> y);
    vector<vector<double>> vec;
    vector<double> div(vector<double> x, double y);
    double pow(double x, int n);
  public:
    Matrix(vector<vector<double>> x){vec=x;};//変換コンストラクタ
    void show();
    static void show(Matrix x);
    Matrix operator+(Matrix x);
    friend Matrix operator+(Matrix X, double y);
    friend Matrix operator+(double y, Matrix X);
    Matrix operator*(Matrix x);
    friend Matrix operator*(Matrix X, double y);
    friend Matrix operator*(double y, Matrix X);
    Matrix operator-(Matrix x);
    friend Matrix operator-(Matrix X, double y);
    friend Matrix operator-(double y, Matrix X);
    Matrix operator/(double x);
    Matrix operator-();
    Matrix T();
    operator vector<vector<double>>(){return vec;};//変換関数
    double operator()(int x, int y){return vec[x][y];};
    int size();
    vector<int> shape();
    Matrix inv(); //逆行列
    double det(); //行列式
};

typedef Matrix Hmx;
typedef Matrix Tmx;
typedef Matrix Vmx;
typedef Matrix Smx;
typedef Matrix Xmx;
typedef Matrix Fmx;
typedef Matrix Pmx;
typedef Matrix Gmx;
typedef Matrix Cmx;