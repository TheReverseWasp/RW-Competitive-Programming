#include <bits/stdc++.h>
#include <cstdio>

using namespace std;

#define rep(i, a, b) for(long long i = a; i < b; ++i)
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
  int t;
  cin >> t;
  while (t) {
    t--;
    ll b, c;
    cin >> b >> c;
    if(b == c) {
      cout<<1<<"\n";
    }
    else if(b > c){
      if (c % b == 0) {
        cout<< 1 <<"\n";
      }
      else{
        b = b% c;
        if(__gcd(b,c) == 1) {
          cout << c-1 << "\n";
        }
        else{
          rep(i,1LL,__gcd(c,b) + 5)  {
            if ((i *c)% b == 0) {
              cout << (i * c) / b << "\n";
              break;
            }
          }
        }
      }
    }
    else{
      if(__gcd(b,c) == 1) {
        cout << c-1 << "\n";
      }
      else{
        for(ll i = 1LL; i < __gcd(b, c) + 10LL ; ++i) {
          if ((i * c)% b == 0) {
            cout << (i * c) / b << "\n";
            break;
          }
        }
      }
    }
  }
}
