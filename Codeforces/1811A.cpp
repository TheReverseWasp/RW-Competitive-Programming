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
    int tc;
    cin >> tc;
    rep(i,0,tc){
        int n,d;
        string s;
        cin >>n >> d;
        cin >> s;
        string ans;
        for(int j = 0; j < n; j++){
            if(stoi(s.substr(j,1)) < d){
                ans = s.substr(0,j) + to_string(d) + s.substr(j, s.size()-j);
                break;
            }
        }
        if(ans == ""){
            ans = s + to_string(d);
        }
        cout << ans << endl;
    }
}