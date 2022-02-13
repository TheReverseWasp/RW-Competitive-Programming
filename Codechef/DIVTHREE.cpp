#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

typedef long long ll;

#define rep(i,a,b) for(ll i = a; i < b ;++i)

int main(){
    int tc;
    cin >> tc;
    rep(j,0,tc) {
        int n;
        ll k, d, a;
        cin >> n >> k >> d;
        ll acum= 0;
        rep(i,0,n) {
            cin>>a;
            acum += a;
        }
        cout << min(acum/k, d)<<endl;
    }
}