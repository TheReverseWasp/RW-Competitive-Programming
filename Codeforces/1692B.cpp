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
	freopen((s + ".txt").c_str(), "r", stdin);
	freopen((s + "_out.txt").c_str(), "w", stdout);
}

bool comp(pii a, pii b){
    return a.s < b.s;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int tc;
    cin>>tc;
    rep(__,0,tc){
        int n;
        vector<int>v;
        cin>>n;
        rep(i,0,n){
            int temp;
            cin>>temp;
            v.push_back(temp);
        }
        map<int,int> db;
        trav(elem,v){
            if(db.find(elem) == db.end()){
                db[elem] = 0;
            }
            db[elem] += 1;
        }
        vector<pii>runner;
        trav(elem, db){
            runner.push_back(pii(elem.f, elem.s));
        }
        int even_ = 0, odd_ = 0;
        trav(elem, runner){
            if(elem.s % 2 == 0){
                even_++;
            }
            else{
                odd_++;
            }
        }
        int ans = odd_ + even_ - even_ % 2;
        cout << ans << endl;
    }
}
