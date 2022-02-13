#include <bits/stdc++.h>
#include <math.h>
#include <functional>

using namespace std;

int main() {
    double r, x, y;
    std::cout << std::fixed;
    std::cout << std::setprecision(6);
    while(!(cin >> r >> x >> y).eof()) {
        double d= sqrt(x*x+y*y);
        if (d > r) {
            cout << "miss" << endl;
        }
        else {
            double as = asin(sqrt(r*r - d*d) / r) * 360 / M_PI;
            double a1 = M_PI * r * r * as / 360  - r*r*sin(as/180*M_PI)/2;
            double a2 = M_PI * r * r - a1;
            cout << max(a1, a2)<< " "<<min(a1,a2) << endl;
        }
    }
}