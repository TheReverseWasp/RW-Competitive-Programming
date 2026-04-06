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

#define rep(i, a, b) for(long long int i = a; i < (b); ++i)
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
    long long int destiny;
    cin >> destiny;
    unordered_set<long long int> db;
    rep(runner,1,(ll)(sqrt(destiny) + 1)){
        ll square = runner * runner;
        ll cube = runner * runner * runner;
        if(square <= destiny)
            db.insert(square);
        if(cube <= destiny)
            db.insert(cube);
    }
    cout << db.size() << endl;
  }
}
