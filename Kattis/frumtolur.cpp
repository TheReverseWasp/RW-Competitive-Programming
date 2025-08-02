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

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<int> db(1,2);
    int runner = 3;
    while(db.size() < 100){
        bool is_prime = true;
        rep(i,1,db.size()){
            if(runner % db[i] == 0){
                is_prime = false;
                break;
            }
        }
        if(is_prime){
            db.push_back(runner);
        }
        runner += 2;
    }
    rep(i,0,db.size()){
        cout << db[i] << endl;
    }
}
