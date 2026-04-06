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
#define ll long long
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
    int n;
    cin >> n;
    vi a;
    unordered_map<int,int> db;
    rep(j,0,n){
        int temp;
        cin >> temp;
        a.push_back(temp);
        db[temp]=0;
    }
    int ans = 0;
    int j = 0;
    for(; j<n; ++j){
        int temp = a[n-j-1];
        db[temp]++;
        if(db[temp] == 2){
            break;
        }
    }
    ans = n - j;
    cout << ans << endl;
  }
}
