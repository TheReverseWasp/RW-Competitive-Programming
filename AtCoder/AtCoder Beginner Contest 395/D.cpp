#include <bits/stdc++.h>
#include <cstdio>
#include <unordered_map>
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

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N, Q;
    cin >> N >> Q;
    unordered_map<int, unordered_set<int>> db;
    unordered_map<int, int> _3_log;
    rep(i,1,N + 1){
        _3_log[i] = i;
        db[i].insert(i);
    }
    rep(__,0,Q){
        int op, a, b, nest;
        cin>>op;
        if (op == 1){
            cin >> a >> b;
            nest = _3_log[a];
            db[nest].erase(a);
            db[b].insert(a);
            _3_log[a] = b;
        }
        else if(op == 2){
            cin >> a >> b;
            swap(db[a], db[b]);
            trav(elem, db[a]){
                _3_log[elem] = a;
            }
            trav(elem, db[b]){
                _3_log[elem] = b;
            }
        }
        else {
            cin >> a;
            cout << _3_log[a] << endl;
        }
    }
}
