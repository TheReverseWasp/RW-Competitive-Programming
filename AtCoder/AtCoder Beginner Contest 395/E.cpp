#include <bits/stdc++.h>
#include <cstdio>
#include <unordered_set>

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

long long int bfs_tricked(long long int actual, long long int acum_cost, long long int X, vector<unordered_set<long long int>> vs, vector<unordered_set<long long int>> rvs, bool way, unordered_set<long long int> visited, bool prev_rev){
    visited.insert(actual);
    if(actual == vs.size() - 1){
        return acum_cost;
    }
    if(way == true){//vs
        vector<long long int> possible;
        trav(elem, vs[actual]){
            if(visited.find(elem) == visited.end()){
                possible.push_back(elem);
            }
        }
        long long int ans;
        if(prev_rev){
            ans = 9223372036854775807;
        }
        else{
            ans = bfs_tricked(actual, acum_cost + X, X, vs, rvs, !way, visited, true);
        }
        trav(elem, possible){
            long long int temp = bfs_tricked(elem, acum_cost + 1, X, vs, rvs, way, visited, false);
            if (temp < ans){
                ans = temp;
            }

        }
        return ans;
    }
    else{ // rvs
        vector<long long int> possible;
        trav(elem, rvs[actual]){
            if(visited.find(elem) == visited.end()){
                possible.push_back(elem);
            }
        }
        long long int ans;
        if(prev_rev){
            ans = 9223372036854775807;
        }
        else{
            ans = bfs_tricked(actual, acum_cost + X, X, vs, rvs, !way, visited, true);
        }
        trav(elem, possible){
            long long int temp = bfs_tricked(elem, acum_cost + 1, X, vs, rvs, way, visited, false);
            if (temp < ans){
                ans = temp;
            }

        }
        return ans;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    long long int N, M, X;
    cin >> N >> M >> X;
    vector<unordered_set<long long int>> vs (N + 1);
    vector<unordered_set<long long int>> rvs (N + 1);
    rep(i,0,M){
        long long int a, b;
        cin >> a >> b;
        vs[a].insert(b);
        rvs[b].insert(a);
    }
    unordered_set<long long int> runner;
    cout<<bfs_tricked((long long int)(1), (long long int)(0), X, vs, rvs, true, runner, false) << endl;
}
