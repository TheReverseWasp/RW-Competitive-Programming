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

string parse_m(map<ll,ll> m){
    string ans = "";
    trav(a,m){
        ans += to_string(a.first) + "-";
    }
    return ans;
}

unordered_map<string, ll> db;

ll get_score(unordered_map<ll,ll> m){
    if(m.size() == 0){
        return 0
    }
    string parsed_m = parse_m(m);
    if(db.find(parsed_m) != db.end()){
        return db[parsed_m];
    }
    ll ans;
    ll runner = 0
    trav(a,m){
        ll temp_a_f, temp_a_s, temp_1_f, temp_1_s, temp_l1_f, temp_l2_s;
        temp_a_f = a.first;
        temp_a_s = a.second;
        if(m.find(temp_a_f + 1) != m.end()){
            temp_1_f = temp_a_f + 1;
            temp_1_s = m[temp_a_f + 1];
        }
        else{
            temp_1_f = -1
            temp_1_s = -1;
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    unordered_map<ll, ll> m;
    rep(i,0,n) {
        ll temp;
        cin >> temp;
        if(m.find(temp) == m.end()){
            m[temp] = 0;
        }
        m[temp] += temp;
    }

}
