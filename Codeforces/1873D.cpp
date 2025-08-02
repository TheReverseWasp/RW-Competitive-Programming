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
    int tc, n, k;
    cin>>tc;
    rep(__,0,tc){
        cin>>n>>k;
        string s;
        cin>>s;
        int ans = 0;
        int pos = s.find("B"); 
        while(pos != -1){
            ++ans;
            try
            {
                s = s.substr(pos + k, s.size() - pos - k);
                pos = s.find("B"); 
            }
            catch(const std::exception& e)
            {
                break;
            }
        }
        cout << ans << endl;
    }
}