#include <bits/stdc++.h>
#include <map>
#include <string>
using namespace std;

typedef pair<string, string> pss;

pss spliter(string line) {
    string s1, s2;
    int i = 0;
    while(true) {
        if(line[i] == ' ') {
            i++;
            break;
        }
        else {
            s1 = s1 + line[i];
        }
        ++i;
    }

    while(i < line.size()) {
        s2 = s2 + line[i];
        ++i;
    }
    pss a;
    a.first = s1;
    a.second = s2;
    return a;
}

int main() {
    string line;
    map<string, string> m;
    getline(cin, line);
    while(line.size() != 0) {
        pss a = spliter(line);
        m[a.second] = a.first;
        getline(cin, line);
    }
    while(!(cin >> line).eof()) {
        if(m.find(line) == m.end()) cout << "eh" << endl;
        else cout <<m[line] << endl;
    }
}