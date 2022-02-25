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

struct Rect {
  ll x1, y1, x2, y2;
  Rect(ll x1, ll y1, ll x2, ll y2) {
    this->x1 = x1;
    this->y1 = y1;
    this->x2 = x2;
    this->y2 = y2;
  }
  int area() {
    return (y2-y1) * (x2 - x1);
  }
};

int intersect(Rect p, Rect q) {
  ll xOverlap = max(0LL, min(p.x2, q.x2) - max(p.x1, q.x1));
  ll yOverlap = max(0LL, min(p.y2, q.y2) - max(p.y1, q.y1));
  return xOverlap * yOverlap;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  ll x1, y1, x2, y2;
  cin >> x1 >> y1 >> x2 >> y2;
  Rect w(x1, y1, x2, y2);
  cin >> x1 >> y1 >> x2 >> y2;
  Rect b1(x1, y1, x2, y2);
  cin >> x1 >> y1 >> x2 >> y2;
  Rect b2(x1, y1, x2, y2);
  ll wb1 = intersect(w, b1);
  ll wb2 = intersect(w, b2);
  ll b1b2 = intersect(b1,b2);
  ll left_area = w.area() - wb1 -(wb2 - b1b2);
  if(left_area <= 0) {
    cout << "NO" << "\n";
  }
  else {
    cout << "YES" << "\n";
  }
}
