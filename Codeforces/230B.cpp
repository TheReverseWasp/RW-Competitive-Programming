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

unordered_set<ll> accepted;
vector<ll> primes;

void setIO(string s) {
	  freopen((s + ".txt").c_str(), "r", stdin);
	  freopen((s + "_out.txt").c_str(), "w", stdout);
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int tc;
    cin>>tc;
    vector<ll> jaja_i_died;
    rep(i,0,tc){
        ll temp;
        cin>>temp;
        jaja_i_died.push_back(temp);
    }
    rep(i,2,1000001){
        ll temp = sqrt(i);
        bool flag = true;
        rep(j, 0, primes.size()){
            if(primes[j] > temp){
                break;
            }
            if(i % primes[j] != 0){
                continue;
            }
            else{
                flag = false;
                break;
            }
        }
        if(flag){
            primes.push_back(i);
            accepted.insert((long long int)(i)*(long long int)(i));
        }
    }
    rep(i,0,tc){
        cout << (accepted.find(jaja_i_died[i]) == accepted.end() ? "NO" : "YES") <<endl;
    }

}
