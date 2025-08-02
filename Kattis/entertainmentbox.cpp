#include <bits/stdc++.h>
#include <cstdio>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<long long int, long long int> pii;
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

bool compare(pii a, pii b){
    if(a.second < b.second){
        return true;
    }
    else if (a.second > b.second) {
        return false;
    }
    else{
        return a.first > b.first;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,k;
    cin>>n>>k;
    pii temp;
    vector<pii> runner;
    rep(i,0,n){
        cin>>temp.first>>temp.second;
        runner.push_back(temp);
    }
    sort(runner.begin(), runner.end(), compare);
    int ans = 0;
    queue<pii> myqueue;
    rep(i,0,n){
        if(myqueue.size() < k){
            ans += 1;
            myqueue.push(runner[i]);
        }
        else{
            temp = myqueue.front();
            if(runner[i].first >= temp.second){
                myqueue.pop();
                ans += 1;
                myqueue.push(runner[i]);
            }
        }        
    }
    cout << ans << endl;
}
