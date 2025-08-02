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

int count_boxes(vector<int>v, int minimum_m){
    int ans = 0;
    trav(a,v){
        if(a%minimum_m > 0){
            ans += 1;
        }
        ans += a/minimum_m ;
    }
    return ans;
}

int survey(vector<int> v, int boxes){
    int low = 0, high = 5000001;
    while(high - low != 1) {
        int mid = (low + high) / 2;
        int temp = count_boxes(v,mid);
        if(temp <= boxes){
            high = mid;
        }
        else{
            low = mid;
        }
    }
    return low + 1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, b;
    cin>>n>>b;
    while(n!=-1){
        vector<int> v(n);
        rep(i,0,n){
            cin>>v[i];
        }
        cout << survey(v,b) << endl;
        cin>>n>>b;
    }
}
