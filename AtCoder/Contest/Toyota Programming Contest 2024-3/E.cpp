#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ll;
typedef pair<ll, ll> llll;

int main() {
    int n;
    cin >> n;
    map<ll, llll> m;
    vector <ll> v;
    for(int i = 0; i < n; i++){
        ll temp;
        cin >> temp;
        v.push_back(temp);
    }
    for(int i = 0; i < n; i++){
        ll prev, next;
        if (i == 0){
            prev = 0;
            next = v[i+1];
        }
        else if (i == n-1){
            prev = v[i-1];
            next = 0;
        }
        else{
            prev = v[i-1];
            next = v[i+1];
        }
        m[v[i]] = llll(prev, next);
    }
    int q;
    cin >> q;
    for(int i = 0; i < q; i++){
        int type_;
        cin >> type_;
        if (type_ == 1){
            ll x, y;
            cin >> x >> y;
            ll next;
            next = m[x].second;
            m[y] = llll(x, next);
            m[x].second = y;
            if (next != 0) m[next].first = y;
        }
        else{
            ll x;
            cin >> x;
            ll prev, next;
            prev = m[x].first;
            next = m[x].second;
            m.erase(m.find(x));
            if (prev != 0) m[prev].second = next;
            if (next != 0) m[next].first = prev;
        }
    }
    vector<ll> ans (m.size());
    ll temp;
    for (auto& pair : m) {
        if (pair.second.first == 0) {
            temp = pair.first;
            break;
        }
    }
    for(int i = 0; i < ans.size(); i++){
        ans[i] = temp;
        temp = m[temp].second;
        cout << ans[i] << " ";
        if (temp == 0) break;
    }
    cout << endl;
}
