#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define rep(i, a, b) for(int i = a; i < b; ++i)

int main() {
  int tc;
  cin >> tc;
  while(tc) {
    int n;
    cin >> n;
    vector<ll> v(n);
    rep(i, 0, n){
      cin >> v[i];
    }
    vector<ll> v2(v);
    rep(i, 0, n){
      rep(j, 0, n) {
        cout << ((v[i]&v[j]) > 0) << " ";
      }
      cout << endl;
    }

    if(is_sorted(v.begin(), v.end())){
      cout << "Yes" << endl;
    }
    else{
      cout << "No" << endl;
    }
    tc--;
  }


}
