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
    int N;
    cin>>N;
    ll total_weight = 0;
    vector<ll> fruit_b(N);
    rep(i,0,N){
        cin>>fruit_b[i];
        total_weight+=fruit_b[i] * pow(2, N-1);
    }
    rep(i,0,N){
        total_weight -= fruit_b[i] < 200 ? fruit_b[i] : 0;
        rep(j,i+1,N){
            total_weight -= fruit_b[i] + fruit_b[j] < 200 ? fruit_b[i] + fruit_b[j] : 0;
            rep(k,j+1,N){
                total_weight -= fruit_b[i] + fruit_b[j] + fruit_b[k] < 200 ? fruit_b[i] + fruit_b[j] + fruit_b[k] : 0;
            }
        }
    }
    cout << total_weight <<endl;
}
