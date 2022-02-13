#include <bits/stdc++.h>
#include <algorithm>
#include <utility>

using namespace std;

typedef pair<string, double> psd;
typedef vector<psd> vp;

bool comp (psd a, psd b) {
    return a.second < b.second;
}

int main() {
    int c;
    cin >> c;
    vp v;
    while(c) { 
        string a, b;
        cin >> a >> b;
        stringstream ss;
        double val;
        psd p;
        ss << a;
        if(ss >> val) {
            p.first= b;
            p.second = val / 2;
            v.push_back(p);
        }
        else{
            stringstream ss;
            ss << b;
            ss >> val;
            p.first = a;
            p.second = val;
            v.push_back(p);
        }
        --c;
    }
    sort(v.begin(), v.end(), comp);
    for(int i= 0; i <v.size(); i++) {
        cout << v[i].first << endl;
    }
}