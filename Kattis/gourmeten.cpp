#include <bits/stdc++.h>
#include <cstdio>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef unsigned long long ll;
typedef pair<int, int> pii;
typedef vector<unsigned long long int> vi;
#define ll long long int
#define mp make_pair
#define f first
#define s second
#define pb push_back

void setIO(string s) {
	freopen((s + ".txt").c_str(), "r", stdin);
	freopen((s + "_out.txt").c_str(), "w", stdout);
}

vi factorial(ll n) {
    vi ans;
    for(ll i=n; i >= 2; i--){
        ans.push_back(i);
    }
    return ans;
}

void restar(vi &base, vi to_restar){
    trav(resto_esto, to_restar){
        if (resto_esto == 1){
            continue;
        }
        rep(i,0,base.size()){
            if(base[i] % resto_esto == 0){
                base[i] /= resto_esto;
            }
        }
    }
}

ll solve(vi factor){
    ll ans = 1;
    trav(elem, factor){
        ans*=elem;
    }
    return ans;
}

ll special_factorial(ll n, vi memory){
    vi ans = factorial(n);
    trav(elem, memory){
        vi temp = factorial(elem);
        restar(ans, temp);
    }
    return solve(ans);
}

ll dp(ll total, int pos, vi memory, ll time_left, vi dishes){
    if (time_left < 0) {
        return 0;
    }
    if (time_left == 0) {
        return special_factorial(total, memory);
    } 
    if(pos == dishes.size()){
        return 0;
    }
    ll select_next = dp(total, pos + 1, memory, time_left, dishes);
    memory[pos]++;
    ll select_this = dp(total+1, pos, memory, time_left - dishes[pos], dishes);
    memory[pos]--;
    return select_this + select_next;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll time_left;
    int n;
    vi dishes;
    cin >> time_left;
    cin >> n;
    vi memory;
    rep(i,0,n){
        ll temp;
        cin >> temp;
        dishes.push_back(temp);
        memory.push_back(0);
    }
    
    cout << dp(0, 0, memory, time_left, dishes) << endl;
}
