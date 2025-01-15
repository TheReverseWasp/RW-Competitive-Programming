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

bool comp(pii a, pii b){
    return a.first < b.first;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int s, n;
    cin >> s >>n;
    vector<pii> l;
    rep(i,0, n){
        pii temp;
        cin >> temp.first >> temp.second;
        l.push_back(temp);
    }
    sort(l.begin(), l.end(), comp);
    bool temp = true;
    rep(i,0,n){
        if(l[i].first < s){
            s+= l[i].second;
        }
        else {
            cout << "NO" <<endl;
            temp = false;
            break;
        }
    }
    if(temp) cout<<"YES"<<endl;
}
