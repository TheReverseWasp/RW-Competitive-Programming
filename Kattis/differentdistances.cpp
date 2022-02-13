#include <bits/stdc++.h> 
#include <math.h>

using namespace std;

int main() {
    cout << fixed;
    cout << setprecision(5);
    long double x1, y1, x2, y2, p;
    cin >> x1;
    while(x1 != 0) {
        cin >> y1 >> x2 >> y2 >> p;
        cout << pow(pow(abs(x1 - x2), p) + pow(abs(y1 - y2), p), 1/p) << endl;
        cin >> x1;

    }
}