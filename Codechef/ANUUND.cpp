#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
#define rep(i,a,b) for(int i = a; i <b; ++i)

int main(){
  int t;
  cin >> t;
  while (t) {
    t--;
    int n;
    cin >> n;
    vector<ll> v(n);
    rep(i,0,n){ cin >> v[i]; }
    sort(v.begin(), v.end());
    vector<ll> ans(n);
    ans[0] = v[0];
    if(n%2 == 0) { ans[n-1] = v[n-1];}
    for(int i = 1; i < n - 1; i+=2) {
      ans[i] = v[i+1];
      ans[i+1] = v[i];
    }
    rep(i,0,n){
      cout << ans[i] << " ";
    }
    cout << endl;
  }
}
