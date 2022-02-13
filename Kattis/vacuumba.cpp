#include <bits/stdc++.h>
#include <cmath>

using namespace std;

#define rep(i,a,b) for(int i = a; i < b; ++i)
#define PI 3.14159265

int main() {
    int tc;
    cin >> tc;
    while(tc>0) {
        int moves;
        double xs = 0, ys = 0;
        double ca = 90;
        cin >> moves;
        rep(i,0,moves){
            double angle, d;
            cin >> angle >> d;
            ca += angle;
            xs += sin(ca * PI / 180) * d;
            ys += cos(ca * PI / 180) * d;
        }
        cout << ys << " " << xs << endl;
        tc--;
    }
}