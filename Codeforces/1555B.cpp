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

int xOverlap_intersect(Rect p, Rect q) {
  ll xOverlap = max(0LL, min(p.x2, q.x2) - max(p.x1, q.x1));
  return xOverlap;
}

int yOverlap_intersect(Rect p, Rect q) {
  ll yOverlap = max(0LL, min(p.y2, q.y2) - max(p.y1, q.y1));
  return yOverlap;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int tc;
  cin >> tc;
  while (tc){
    tc--;
    ll w, h;
    cin >> w >> h;
    ll x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    Rect table1(x1, y1, x2, y2);
    ll wt, ht;
    cin >> wt >> ht;
    ll wt1 = x2 - x1, ht1 = y2 - y1;
    if((wt1 + wt > w) || (ht1 + ht > h)) {
      cout << -1 << "\n";
    }
    else {
      vector<Rect> vr;
      vr.push_back(Rect(0, 0, wt, ht));
      vr.push_back(Rect(w - wt, 0, w, ht));
      vr.push_back(Rect(0, h - ht, wt, h));
      vr.push_back(Rect(w - wt, h - ht, w, h));

      vector <ll> overlaps;
      rep(i, 0, 4){
        ll xOv = xOverlap_intersect(vr[i], table1);
        overlaps.push_back(xOv);
        ll yOv = yOverlap_intersect(vr[i], table1);
        overlaps.push_back(yOv);
      }
      sort(overlaps.begin(), overlaps.end());
      printf("%.6f\n", overlaps[0]);
    }
  }
}
