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
class mycomparison
{
  bool reverse;
public:
  mycomparison(const bool& revparam=false)
    {reverse=revparam;}
  bool operator() (const pair<int, ll> & lhs, const pair<int, ll> &rhs) const
  {
    if (reverse) return (lhs.s>rhs.s);
    else return (lhs.s<rhs.s);
  }
};
bool fun(pair<int, ll> a, pair<int, ll> b ){
  return a.s < b.s;
}

ll set_query(vector<ll> & a, map<int, set<int> > m) {
  set<int> visited;
  ll ans = 0;
  while(visited.size() < a.size()) {
    priority_queue<pair<int, ll>, vector <pair<int, ll>  >, mycomparison> pq;
    trav(elem, m) {
      if(visited.count(elem.f) == 0){
        pq.push(mp(elem.f, (long long)(elem.s.size()) * (long long)(a[elem.f - 1])));
      }
    }
    pair<int, ll> temp (pq.top());
    ans += a[temp.f - 1];
    visited.insert(temp.f);
    rep(i, 0 , a.size()) {
      if(i + 1 != temp.f) {
        if(m[temp.f].count(i + 1) != 0) {
          a[i] += 1;
        }
        else {
          a[i] -= 1;
        }
      }
    }

  }
  return ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, m_;
  cin >> n >> m_;
  vector <ll> a(n);
  rep(i,0,n) { cin >> a[i];}
  map<int, set<int> > m;
  rep(i,0,m_){
    int temp1, temp2;
    cin >> temp1 >> temp2;
    if (m.count(temp1) == 0) {
      m[temp1] = set<int>();
    }
    if (m.count(temp2) == 0) {
      m[temp2] = set<int>();
    }
    m[temp1].insert(temp2);
    m[temp2].insert(temp1);
  }
  int querys;
  cin >> querys;
  rep(i,0,querys) {
    string q_type;
    cin >> q_type;
    if(q_type == "+") {
      int temp1, temp2;
      cin >> temp1 >> temp2;
      if (m.count(temp1) == 0) {
        m[temp1] = set<int>();
      }
      if (m.count(temp2) == 0) {
        m[temp2] = set<int>();
      }
      m[temp1].insert(temp2);
      m[temp2].insert(temp1);
    }
    else if (q_type == "-"){
      int temp1, temp2;
      cin >> temp1 >> temp2;
      if (m.count(temp1) == 0 ){
        m[temp1] = set<int>();
      }
      if (m.count(temp2) == 0 ){
        m[temp2] = set<int>();
      }
      m[temp1].erase(temp2);
      m[temp2].erase(temp1);
    }
    else {
      cout << set_query(a, m) << endl;
    }
  }
}
