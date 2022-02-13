#include <bits/stdc++.h>
#include <math.h>

using namespace std;

int main() {
    double h, angle;
    cin >> h >> angle;
    cout << ceil(1/sin(angle /180 * M_PI) *h) << endl;

}