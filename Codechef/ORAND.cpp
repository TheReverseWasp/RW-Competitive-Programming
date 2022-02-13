#include <bits/stdc++.h>
#include <functional>
#include <vector>
#include <map>

using namespace std;

#define rep(i,a,b) for(int i=a; i<b; ++i)
#define rep_(i,a,b) for(int i=a; i>=b; --i)

typedef long long ll;
typedef vector<ll> vll;


int binsearch(vll t, ll num) {
    int i= 0, f = t.size();
    int h = (i + f)/2;
    while(i < f) {
        if (t[h] >= num) {
            f = h;
        }
        else {
            i = h + 1;
        }
        h = (i+f)/2;
    }
    return i;
}

void runner(vll vm, ll val,int a, int b, map<ll,bool> &m1) {
    ll t;
    rep_(i, a, b) {
        t = val & vm[i];
        if(m1.find(t) == m1.end()) {
            m1[t] = true;
        }
        else break;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int tc;
    cin >> tc;
    while(tc > 0){
        ll n, m;
        cin >> n >> m;
        vll vn, vm;
        map<ll,bool> m1;

        while(n > 0) {
            ll t;
            cin >>t;
            vn.push_back(t);
            --n;
        }

        while(m > 0) {
            ll t;
            cin >>t;
            vm.push_back(t);
            --m;
        }
        sort(vm.begin(), vm.end(), less<ll>());
        m1[ll(0)] = true;
        ll st = 0;
        rep(i,0,vn.size()) {
            st |= vn[i];
            if(m1.find(st) == m1.end()) {
                m1[st] = true;
                rep_(j, vm.size() - 1, 0) {
                    ll tst = st & vm[j];
                    if(m1.find(tst) == m1.end()){
                        m1[tst]=true;
                        runner(vm, tst, j - 1, 0, m1);
                    }
                    else break;
                    
                }
            }
        }
        cout << m1.size() << endl;
        --tc;
    }

}
