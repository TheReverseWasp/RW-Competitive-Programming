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
    cin >> tc;
    rep(i,0,tc){
        int n;
        string s;
        cin >> n >> s;
        unordered_set<char> db;
        trav(letter, s){
            db.insert(letter);
        }
        vector<char>db_2;
        trav(letter,db){
            db_2.push_back(letter);
        }
        sort(db_2.begin(), db_2.end());
        map<char,char> translator;
        rep(j,0,db_2.size()){
            char letter = db_2[j];
            char translation = db_2[db_2.size() - 1 - j];
            translator[letter] = translation;
        }
        string ans;
        trav(letter, s){
            ans += translator[letter];
        }
        cout << ans << endl;
    }
}