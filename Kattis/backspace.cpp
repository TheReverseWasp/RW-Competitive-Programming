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
    string word;
    cin >> word;
    string ans = "";
    int erased = 0;
    rep(i,0,word.size()){
        char suicide_boy = word[word.size() - 1 - i];
        if(suicide_boy != '<'){
            if(erased > 0){
                erased--;
                continue;
            }
            else{
                ans += suicide_boy;
            }
        }
        else{
            erased++;
        }
    }
    string new_ans = "";
    rep(i,0,ans.size()){
        new_ans+=ans[ans.size()-1-i];
    }
    cout << new_ans << endl;
}
