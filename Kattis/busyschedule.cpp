#include <bits/stdc++.h>
#include <algorithm>
#include <functional>
#include <utility>
#include <string>

using namespace std;

#define rep(i,a,b) for (int i= a; i<b; ++i)

typedef pair<string, float> psf;
typedef vector<psf> vpsf;

float conv_str_float(string s) {
    float hours=0, mins=0;
    int t = s.find(":");
    hours += stof(s.substr(0, t));
    if (s.substr(0, t) == "12") {
        hours = 0;
    }
    mins = stof(s.substr(t+1, 2));
    mins /= 100;
    hours += mins;
    if(s.find("p.m.") != string::npos) {
        hours +=12;
    }
    return hours;
}

bool compare(psf p1, psf p2) {
    return p1.second < p2.second;
}


int main() {
    int tc;
    cin >>tc;
    while (tc > 0) {
        vpsf v;
        cin.ignore();

        rep(i,0,tc) {
            string line;
            getline(cin, line);
            psf p;
            p.first = line;
            p.second = conv_str_float(line);
            v.push_back(p);
        }
        sort(v.begin(), v.end(), compare);
        rep(i, 0, tc) {
            cout << v[i].first << endl;
        }
        cout << endl;
        cin >> tc;
    }

}