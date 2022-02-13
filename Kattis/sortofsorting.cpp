#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

typedef string str;
typedef pair<pair<str, int> ,str> pss;
typedef vector<pss> vpss;

#define rep(i,a,b) for(int i = a; i < b; ++ i)

bool comp(pss p1, pss p2) {
    if(p1.first.first == p2.first.first) {
        return p1.first.second < p2.first.second;
    }
    return p1.first.first < p2.first.first;
}

int main(){
    int tc;
    cin >>tc;
    while(tc > 0) {
        vpss v;
        rep(i,0,tc) {
            str s;
            cin >> s;
            pss p;
            p.second = s;
            pair<str, int> temp;
            temp.first = s.substr(0,2);
            temp.second = i;
            p.first = temp;
            v.push_back(p);
        }
        sort(v.begin(), v.end(), comp);
        rep(i,0,tc) {
            cout << v[i].second << endl;
        }
        cout << endl;
        cin >> tc;
    }
}
