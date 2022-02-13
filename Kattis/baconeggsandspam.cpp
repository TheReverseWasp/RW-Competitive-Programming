#include <bits/stdc++.h>
#include <sstream>
#include <map>
#include <algorithm>
using namespace std;

typedef vector<string> vs;
typedef map<string, vs> msvs;
typedef pair<string, vs> psvs;

#define rep(i,a,b) for(int i = a; i < b ; ++i)

int main() {
    int tc;
    cin >>tc;
    cin.ignore();
    while(tc > 0){
        msvs m;
        while(tc > 0) {

            string cad;
            getline(cin, cad);
            stringstream line(cad);
            string name, item;
            line >> name;
            while(line >> item) {
                m[item].push_back(name);
            }
            tc--;
        }
        vector<psvs> v;
        for(auto it = m.begin(); it != m.end(); it++) {
            sort((it->second.begin()), (it->second.end()));
            psvs p;
            p.first = it->first;
            p.second = it->second;
            v.push_back(p);
        }
        rep(i,0,v.size()){
            cout << v[i].first << " ";
            rep(j,0,v[i].second.size()){
                cout << v[i].second[j] << " ";
            }
            cout << endl;
        }
        cout << endl;

        cin >>tc; 
        cin.ignore();
    }
}