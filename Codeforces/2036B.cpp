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
typedef pair<long long int, long long int> pll;
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

bool comp(pll a, pll b){
    return a.s > b.s;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int tc;
    cin >> tc;
    rep(__,0,tc){
        ll shelf, bottles;
        cin >> shelf >> bottles;
        map<ll,ll> db;
        rep(i,0,bottles){
            int brand, price;
            cin >> brand >> price;
            if(db.find(brand) == db.end()){
                db[brand] = 0;
            }
            db[brand] += price;
        }
        vector<pll> useful_db;
        trav(p, db){
            useful_db.push_back(p);
        }
        sort(useful_db.begin(), useful_db.end(), comp);
        ll ans = 0;
        rep(i,0,min(shelf, (ll)useful_db.size())){
            ans += useful_db[i].s;
        }
        cout << ans << endl;
    }
}
