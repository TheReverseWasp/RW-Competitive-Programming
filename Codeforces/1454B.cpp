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

bool comp(pair<int,vector<int> > a,pair<int,vector<int> > b){
    return a.f < b.f;
}
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int tc;
    cin>>tc;
    rep(__,0,tc){
        int n;
        cin>>n;
        map<int,vector<int> > db;
        rep(i,0,n){
            int temp;
            cin>>temp;
            if(db.find(temp) != db.end()){
                db[temp].push_back(i);
            }
            else{
                vector<int>temp2;
                db[temp] = temp2;
                db[temp].push_back(i);
            }
        }
        vector<pair<int,vector<int> > > source;
        trav(a,db){
            source.push_back(a);
        }
        sort(source.begin(),source.end(), comp);
        bool flag=false;
        int indice = -1;
        trav(a,source){
            if(a.s.size() == 1){
                flag=true;
                indice=a.s[0];
                break;
            }
        }
        if(flag){
            cout<<indice + 1<<endl;
        }
        else{
            cout<<-1<<endl;
        }
    }
}
