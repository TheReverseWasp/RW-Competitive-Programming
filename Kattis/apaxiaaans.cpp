#include <bits/stdc++.h>
#include <string>
using namespace std;

int main() {
    string s;
    string a;
    cin >> s;
    a.push_back(s[0]);
    for(int i =1; i< s.size(); ++i) {
        if(s[i] != a[a.size()-1]) {
            a.push_back(s[i]);
        }
    }
    cout <<a<<endl;
}