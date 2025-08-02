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

vector<ll> purge_vec(vector<ll>victim){
    vector<ll> ans;
    int i = 0;
    while(victim.size()-1-i > 0 && victim[victim.size()-1-i] == 0){
        i++;
    }
    rep(j,0,victim.size()-i){
        ans.push_back(victim[j]);
    }
    return ans;
}

vector<ll> get_pol(vector<ll>a, vector<ll>b){
    if(a.size() == 1 || b.size() == 1){
        vector<ll> ans;
        trav(elem1, a){
            trav(elem2, b){
                ans.push_back(elem1*elem2);
            }
        }
        return ans;
    }
    if(a.size() % 2 == 1){
        a.push_back(0);
    }
    if(b.size() % 2 == 1){
        b.push_back(0);
    }
    vector<ll>pl,pr,ql,qr;
    rep(i,0,a.size() / 2){
        pl.push_back(a[i]);
    }
    rep(i,a.size() / 2, a.size()){
        pr.push_back(a[i]);
    }
    rep(i,0,b.size() / 2){
        ql.push_back(b[i]);
    }
    rep(i,b.size() / 2, b.size()){
        qr.push_back(b[i]);
    }
    vector<ll>pol_1(purge_vec(get_pol(pl,ql)));
    vector<ll>pol_2(get_pol(pl,qr));
    vector<ll>pol_3(get_pol(pr,ql));
    rep(i,0,pol_2.size()){
        pol_2[i] += pol_3[i];
    }
    vector<ll>pol_4(purge_vec(get_pol(pr,qr)));
    vector<ll>ans;
    rep(i,0,pol_1.size()){
        ans.push_back(pol_1[i]);
    }

    rep(i,0,pol_2.size()){
        ans.push_back(pol_2[i]);
    }

    rep(i,0,pol_4.size()){
        ans.push_back(pol_4[i]);

    }
    return ans;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int tc;
    cin>>tc;
    rep(__,0,tc){
        int n,m;
        cin >> n;
        vector<ll> a;
        rep(i,0,n + 1){
            ll temp;
            cin>>temp;
            a.push_back(temp);
        }
        cin>>m;
        vector<ll> b;
        rep(i,0,m + 1){
            ll temp;
            cin>>temp;
            b.push_back(temp);
        }
        vector<ll> ans (get_pol(a,b));
        cout << ans.size() - 1 << endl;
        trav(a,ans){
            cout << a << " ";
        }
        cout << endl;
    }
}
