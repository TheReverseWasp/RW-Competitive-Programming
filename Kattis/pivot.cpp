#include <bits/stdc++.h>
#include <functional>
#include <algorithm>
#include <vector>

using namespace std;

#define rep(i,a,b) for(int i = a; i < b; ++i)
typedef long long ll;
typedef vector<ll> vll;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int len;
    cin >> len;
    vll v;
    while(len > 0) {
        ll temp;
        cin >> temp;
        v.push_back(temp);        
        --len;
    }
    ll mi = 9999999999999, ma = -9999999999999;
    vector<bool> va(v.size(), true);
    rep(i,0,v.size()) {
        if(v[i] < ma) {
            va[i] = false;
        }
        if(v[v.size()- i - 1] > mi){
            va[v.size()-1-i] = false;
        }
        mi = min(mi, v[v.size()- i - 1]);
        ma = max(ma, v[i]);
    }
    int answer= 0;
    rep(i,0,va.size()) {
        if (va[i] == true) ++answer;
    }
    cout << answer << endl;
}