#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <bitset>
#include <numeric>
#include <sstream>
#include <utility>
#include <cassert>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define ll long long int
#define mp make_pair
#define f first
#define s second
#define pb push_back

void setIO(string s) {
    freopen((s + ".txt").c_str(), "r", stdin);
    freopen((s + "_out.txt").c_str(), "w", stdout);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int tc;
    cin >> tc;
    rep(i,0,tc){
        ll n, k;
        cin >> n >> k;
        map<ll,int> s;
        map<ll,int> t;
        rep(j,0,n){
            ll temp;
            cin >> temp;
            temp = min(temp%k, k-(temp%k));
            if(s.find(temp) == s.end()){
                s[temp] = 0;
            }
            s[temp]++;
        }
        rep(j,0,n){
            ll temp;
            cin >> temp;
            temp = min(temp%k, k-(temp%k));
            if(t.find(temp) == t.end()){
                t[temp] = 0;
            }
            t[temp]++;
        }
        bool flag = true;
        trav(pp, s){
            if(t.find(pp.f) == t.end()){
                flag = false;
                break;
            }
            t[pp.f] -= pp.s;
        }
        if(!flag){
            cout <<"NO" << endl;
            continue;
        }
        trav(pp,t){
            if(pp.s != 0){
                flag = false;
                break;
            }
        }
        if(flag){
            cout << "YES" << endl;
        }
        else{
            cout << "NO" <<endl;
        }
    }
}
