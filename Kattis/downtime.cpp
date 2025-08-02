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
    return a.second < b.second;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, k;
    cin >> n >> k;
    vector<pii> v;
    pii temp;
    rep(i,0,n){
        cin>>temp.first;
        temp.second = temp.first + 1000;
        v.push_back(temp);
    }
    sort(v.begin(), v.end(), comp);
    int ans = 0;
    int i = 0;
    int acum, runner, temp2;
    bool firsto = true;
    while(i<n){
        temp2 = v[i].second;
        if(firsto){        
            acum = 1;
            runner = i + 1;
        }
        else{
            acum--;
        }
        while(runner < n){
            if(v[runner].first < temp2){
                acum += 1;
            }
            else{
                break;
            }
            runner++;
        }
        if(ans < acum){
            ans = acum;
        }
        i++;
    }
    ans += k - 1;
    ans /= k;
    cout << ans << endl;
}
