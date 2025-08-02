#include <bits/stdc++.h>
#include <cstdio>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long int ll;
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

bool compare_fun(pair<string,ll> a, pair<string,ll> b){
    return a.second>b.second;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int tt;
    cin>>tt;
    map<string,ll> m;
    rep(i,0,tt){
        string temp;
        ll temp_views;
        cin>>temp>>temp_views;
        if(m.find(temp) == m.end()){
            m[temp] = 0;
        }
        m[temp] += temp_views;
    }
    vector<pair<string,ll> > v;
    trav(p, m){
        v.push_back(p);
    }
    sort(v.begin(), v.end(),compare_fun);
    cout << v[0].f <<endl;
}
