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
#define pb push_back

void setIO(string s) {
	freopen(("input_data" + s + ".txt").c_str(), "r", stdin);
	freopen((s + "_out.txt").c_str(), "w", stdout);
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  setIO("a_an_example");
  int people, projects;
  cin >> people >> projects;
  map<string, map<string, int> > skill_map;
  rep(i,0,people){
    string col;
    int skills;
    cin >> col >> skills;
    rep(j,0,skills){
      string sk;
      int lv;
      cin >> sk >> lv;
      skill_map[sk][col] = lv;
    }

  }
}
