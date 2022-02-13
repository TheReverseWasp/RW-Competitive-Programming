#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)

const double exactitud = 1e-4;

double fun(int a1, int b1, int a2, int b2) {
    double acum = 0;
    rep(i, a1, b1 + 1) {
        rep(j, a2, b2 + 1) {
            acum += (float(i + j) ) / ((b1 - a1 + 1) * (b2 - a2 + 1));
        }
    }
    return acum;
}

int main(){
    int a1, b1, a2, b2;
    cin >> a1 >> b1 >> a2 >> b2;
    double gs = fun (a1, b1, a2, b2);
    cin >> a1 >> b1 >> a2 >> b2;
    double es = fun (a1, b1, a2, b2);

    if (abs(es - gs) < exactitud) cout << "Tie" << endl;
    else if (es > gs) cout << "Emma" << endl;
    else cout << "Gunnar" << endl;
}