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

bool comp(pair<ll,ll> a, pair<ll,ll> b){
    if(a.f < b.f) return true;
    else if(a.f == b.f){
        return a.s > b.s;
    }
    return false;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin>>t;
    rep(i,0,t){
        ll n,k;
        cin>>n>>k;
        vector<ll>a,b;
        rep(j,0,n){
            ll temp;
            cin>>temp;
            a.push_back(temp);
        }
        rep(j,0,n){
            ll temp;
            cin>>temp;
            b.push_back(temp);
        }
        vector<pair<ll,ll> > to_sort;
        rep(j,0,n){
            pair<ll,ll> tempo;
            tempo.f=a[j];
            tempo.s=b[j];
            to_sort.push_back(tempo);
        }
        sort(to_sort.begin(),to_sort.end(),comp);
        a.clear();
        b.clear();
        ll used = 0;
        int runner=0;
        while(runner<n){
            if(to_sort[runner].f > k){
                break;
            }
            k+=to_sort[runner].s;
            runner+=1;
        }
        cout<<k<<endl;
    }
}
