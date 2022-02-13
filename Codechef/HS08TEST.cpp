#include <bits/stdc++.h>

using namespace std;

int main() {
    int w;
    double c;
    cout << fixed;
    cout << setprecision(2);
    cin >> w >> c;
    if (w > c - .5 || w%5!= 0) {
        cout<<c<<endl;
    }
    else  {
        cout << c - .5 - w <<endl;
    }
}