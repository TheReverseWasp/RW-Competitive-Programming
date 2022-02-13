#include <bits/stdc++.h>
#include <sstream>
#include <string>
#include <map>

using namespace std;

typedef vector<string> vs;
typedef map<string,bool> msb;

#define rep(i,a,b) for(int i=a; i<b; ++i)

int main() {
    string s1;
    vs subw;
    while(getline(cin, s1)){
        stringstream line(s1);
        string t;
        while(line>>t) {
            subw.push_back(t);
        }
    }
    msb m;
    rep(i,0,subw.size()) {
        rep(j,0,subw.size()) {
            if(i != j) {
                m[subw[i]+subw[j]] = true;
            }
        }
    }
    vs answer;
    for(auto it=m.begin(); it!=m.end(); ++it) {
        answer.push_back(it->first);
    }
    sort(answer.begin(), answer.end());
    rep(i,0,answer.size()){
        cout << answer[i] << endl;
    }
}