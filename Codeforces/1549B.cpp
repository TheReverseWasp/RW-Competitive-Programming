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
        int n;
        cin >> n;
        string endo, starto;
        cin >> endo >> starto;
        int ans = 0;
        rep(idx, 0, n){
            if(starto[idx] == '1'){
                if(endo[idx] == '0'){
                    ++ans;
                }
                else{
                    if(idx - 1 >= 0 && endo[idx-1] == '1'){
                        ++ans;
                    }
                    else if(idx + 1 < n && endo[idx+1] == '1'){
                        try{
                            ans += 1;
                            endo = endo.substr(0, idx+1) + "0" + endo.substr(idx+2, n - idx - 2);
                        }
                        catch(...){
                            continue;
                        }
                    }
                }
            }
        }
        cout << ans << endl;
    }
}
