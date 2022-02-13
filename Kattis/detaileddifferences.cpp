#include <bits/stdc++.h>
#include <string>

using namespace std;

#define rep(i,a,b) for(int i = a; i<b; i++)
#define c(a) cout << a << endl;

int main() {
    int tc;
    cin >>tc;
    while(tc > 0) {
        string a,b,c;
        cin >> a >> b;
        rep(i,0,a.size()) {
            if(a[i] == b[i]) c.push_back('.');
            else c.push_back('*');
        }
        c(a);
        c(b);
        c(c);
        cout << endl;
        --tc;
    }
}