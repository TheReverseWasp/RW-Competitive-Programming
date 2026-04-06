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
    int dh, P;
    cin >> dh >> P;
    int ans = 1;
    while(true){
        double cost_exp = ((double)(dh * ans * 60 * P)) / 100000.0;
        cost_exp += 5 * ((dh * ans) / 1000);
        if((dh*ans) % 1000 > 0){
            cost_exp += 5;
        }
        double cost_cheap = ((double)(dh * ans * 11 * P)) / 100000.0;
        cost_cheap += 60 * ((dh * ans) / 8000);
        if((dh*ans) % 8000 > 0){
            cost_cheap += 60;
        }
        ////////////
        if(cost_exp > cost_cheap){
            break;
        }
        else{
            ans++;
        }
    }
    cout << ans << endl;
}
