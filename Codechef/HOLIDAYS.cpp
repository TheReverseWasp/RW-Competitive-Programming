#include <bits/stdc++.h>
#include <cstdio>

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

void setIO(string s) {
	freopen((s + ".txt").c_str(), "r", stdin);
	freopen((s + "_out.txt").c_str(), "w", stdout);
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int tc;
  cin >> tc;
  while (tc){
    tc--;
    int n, w;
    cin >> n >> w;
    vector<int> v(n);
    rep(i, 0, n) {
      cin >> v[i];
    }
    sort(v.begin(), v.end());
    int acum = 0;
    int i;
    int holidays = n;
    for(i = n-1; i >= 0; i--){
      if (acum >= w){
        break;
      }
      acum+= v[i];
      holidays-=1;
    }
    cout << holidays << endl;
  }
}
