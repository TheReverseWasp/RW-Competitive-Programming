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
#define ll long long int
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
    map<int, int> ini;
    map<int, int> fin;
    vector<int> ini_v, fin_v;
    rep(i,0,3) {
        int a, b;
        cin >> a >> b;
        ini[a] = 0;
        fin[b] = 0;
        ini_v.push_back(a);
        fin_v.push_back(b);
    }
    rep(i,0,3){
        ini[ini_v[i]]++;
        fin[fin_v[i]]++;
    }
    int ans_ini, ans_fin;
    trav(a,ini){
        if(a.s == 1){
            ans_ini = a.f;
        }
    }
    trav(b, fin){
        if(b.s == 1){
            ans_fin = b.f;
        }
    }
    cout << ans_ini << " " << ans_fin << endl;
}
