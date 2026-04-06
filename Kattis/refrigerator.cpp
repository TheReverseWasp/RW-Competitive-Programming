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

vector<pair<int, pii> >dp;

int calculate(int pa, int ka, int pb, int kb, int left_to_load, pii & ans){
    if(left_to_load <= 0){
        return ans.f * pa + ans.s * pb;
    }
    if (dp[left_to_load].f != -1) {
        ans = dp[left_to_load].s;
        return dp[left_to_load].f;
    }
    pii chose_a = ans;
    chose_a.f++;
    int cost_a = calculate(pa,ka,pb,kb, left_to_load-ka, chose_a);
    pii chose_b = ans;
    chose_b.s++;
    int cost_b = calculate(pa,ka,pb,kb, left_to_load-kb, chose_b);
    if(cost_a < cost_b){
        ans = chose_a;
        dp[left_to_load].f = cost_a;
        dp[left_to_load].s = ans;
        return cost_a;
    }
    else{
        ans = chose_b;
        dp[left_to_load].f = cost_b;
        dp[left_to_load].s = ans;
        return cost_b;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int pa, ka, pb, kb, n;
    cin >> pa >> ka >> pb >> kb >> n;
    pair<int, pii> temp;
    temp.f = -1;
    rep(i,0,n + 10){
        dp.push_back(temp);
    }
    pii runner;
    runner.f = 0;
    runner.s = 0;
    int cost = calculate(pa, ka, pb, kb, n, runner);
    cout << runner.f << " " << runner.s << " " << cost << endl;
}
