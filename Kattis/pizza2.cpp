#include <bits/stdc++.h>

using namespace std;

int main(){
    double r, c;
    cin >> r >> c;
    cout << fixed;
    cout << setprecision(6);
    cout << ((c-r)* (c-r) * M_PI * 100) / (r * r * M_PI) << endl;
}
