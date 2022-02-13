#include <bits/stdc++.h>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

#define rep(i,a,b) for(int i = a; i<b; ++i)

typedef vector<int> vi;

int fun (vi v) {
    int acum = 0;
    rep(i,0,v.size()){
        acum*=10;
        acum+= v[i];
    }
    return acum;
}

int main() {
    string s;
    cin >> s;
    int n = stoi(s);
    vi v;
    rep(i,0,s.size()) {
        v.push_back((int)s[i] - 48);
    }
    int answer = 99999999;
    while(true){
        if(fun(v) > n && fun(v) < answer) {
            answer = fun(v);
        } 
        if(!next_permutation(v.begin(), v.end())) {
            break;
        }
    }
    if(answer != 99999999) {
        cout << answer << endl;
    }
    else {
        cout << 0 << endl;
    }
}