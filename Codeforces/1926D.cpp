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
    cin>>tc;
    rep(amsiedad,0,tc){
        int n;
        cin>>n;
        vector<int>v(n);
        rep(i,0,n){
            cin>>v[i];
        }
        sort(v.begin(), v.end());
        int endo = n - 1;
        int i = 0;
        int ans1 = 0;
        while (i <= endo){
            if (~(v[i]^v[endo]) == -2147483648){
                endo -= 1;
            }
            ans1 += 1;
            i += 1;
        }
        endo = n - 1;
        i = 0;
        int ans2 = 0;
        while (i <= endo){
            if (~(v[i]^v[endo]) == -2147483648){
                i += 1;
            }
            ans2 += 1;
            endo -= 1;
        }
        cout << min(ans1,ans2) <<endl;
    }
}
