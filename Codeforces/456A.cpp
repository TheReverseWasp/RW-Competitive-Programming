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

bool compare_pairs(pair<int, int> a, pair<int, int> b){
    if(a.f < b.f){
        return true;
    }
    else{
        return
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin>>n;
    vector<pair<int,int> > v(n);
    rep(i,0,n){
        cin>>v[i].f>>v[i].s;
    }
    if(n == 1){
        cout << "Poor Alex" <<endl;
    }
    else{
        sort(v.begin(),v.end(), compare_pairs);
        bool winner = false;
        rep(i,1,n){
            if(v[0].f < v[i].f && v[0].s > v[i].s){
                winner = true;
                break;
            }
        }
        if(winner){
            cout << "Happy Alex" << endl;
        }
        else {
            cout << "Poor Alex" << endl;
        }
    }

}
