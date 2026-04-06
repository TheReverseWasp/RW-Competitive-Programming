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
    cin >>tc;
    rep(i,0,tc){
        int n;
        cin >> n;
        vector<ll>a;
        vector<ll>b;
        rep(j,0,n){
            ll temp;
            cin>>temp;
            a.push_back(temp);
        }
        rep(j,0,n){
            ll temp;
            cin>>temp;
            b.push_back(temp);
        }
        bool flag = true;
        bool it_happens = false;
        unordered_set<int> forbidden;
        do{
            it_happens = false;
            rep(j,0,n-1){
                if(forbidden.find(j) != forbidden.end()){
                    continue;
                }
                if(a[j] != b[j]){
                    if((a[j] ^ a[j+1]) == b[j]){
                        a[j]^=a[j+1];
                        it_happens = true;
                        forbidden.insert(j);
                    }
                }
            }
        }while(it_happens);
        rep(j,0,n){
            if(a[j] != b[j]){
                flag = false;
                break;
            }
        }
        
        if(flag){
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        }
    }
}
