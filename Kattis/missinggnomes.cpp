#include <bits/stdc++.h>
#include <vector>
#include <set>
using namespace std;

typedef set<int> si;

#define rep(i,a,b) for(int i = a; i<b ; ++i)

int main() {
    int n, m;
    cin >> n >> m;
    vector <int> v;
    int t;
    si s;
    rep(i,0,m) {
        cin >> t;
        v.push_back(t);
        s.insert(t);
    }
    int vpos = 0, i = 1;
    while(i <=n) {
        if (s.find(i) != s.end()) {
            if(i == v[vpos]){
                cout << v[vpos] << endl;
                vpos++;
            }
            i++;

        } 
        else {
            if(vpos == v.size()) {
                cout << i << endl;
                i++;
            }
            else if(i < v[vpos]) {
                cout << i << endl;
                ++i;
            }
            else if(v[vpos] < i) {
                cout << v[vpos] << endl;
                vpos++;
            }
        }
    }
    rep(i,vpos, v.size()) {
        cout << v[i] << endl;
    }
}
