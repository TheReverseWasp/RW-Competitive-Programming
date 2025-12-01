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

bool comp(int a, int b){
    return a>b;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int tc;
  cin >> tc;
  rep(i,0,tc){
    int n;
    cin >> n;
    vector<int>a;
    vector<int>b;
    int x = 0;
    rep(j,0,n){
        int temp;
        cin >> temp;
        a.push_back(temp);
    }
    sort(a.begin(),a.end(),comp);
    trav(elem,a){
        x^=elem;
    }
    int ans = 0;
    trav(elem,a){
        b.push_back(elem^x);
        ans^=b[b.size()-1];
    }
    if(ans == 0){
        cout << x << endl;
    }
    else{
        cout << -1 << endl;
    }
  }
}
