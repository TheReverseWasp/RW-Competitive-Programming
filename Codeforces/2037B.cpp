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
    int tc;
    cin >> tc;
    rep(i,0,tc){
        int k;
        cin >> k;
        unordered_map<int,int> db;
        rep(j,0,k){
            int temp;
            cin >> temp;
            if(db.find(temp) == db.end()){
                db[temp] = 1;
            }
            else{
                ++db[temp];
            }
        }
        int to_search = k-2;
        pii ans{-1,-1};
        trav(pato1, db){
            if(pato1.s >= 2 && pato1.f * pato1.f == to_search){
                ans.f = pato1.f;
                ans.s = pato1.f;
                break;
            }
            else if((db.find(to_search / pato1.f) != db.end()) && ((to_search / pato1.f) * pato1.f == to_search)){
                ans.f = pato1.f;
                ans.s = to_search / pato1.f;
                break;
            }
        }
        cout << ans.f << " " << ans.s << endl;
    }
}
