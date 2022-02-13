#include <bits/stdc++.h>
#include <math.h>

using namespace std;

#define rep(i,a,b) for(int i=a; i<b; ++i)

typedef long long ll;
typedef vector<ll> vll;

int main() {
    cout << fixed;
    cout << setprecision(11);
    int l;
    cin >> l;
    l--;
    vll cl;
    rep(i,0,l) {
        ll t;
        cin >> t;
        cl.push_back(t);
    }
    double longSide = pow(2, -(3./4.)), shortSide = pow(2, -(5./4.));
    double tape = 0;
    ll portion = 1;
    rep(i,0,cl.size()) {
        tape += portion * longSide;
        swap(longSide, shortSide);
        shortSide /= 2;
        
        portion *= 2;
        portion -=cl[i];
        if (portion <= 0) {
            break;
        }
    }
    if (portion <=0) {
        cout << tape << endl;
    }
    else {
        cout << "impossible" << endl;
    }
}