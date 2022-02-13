#include <bits/stdc++.h>
#include <string>
#include <algorithm>

using namespace std;

#define rep(i,a,b) for(int i=a;i<b;++i)

int main() {
    string a, b;
    cin >> a >>b;
    string a1, b1;
    rep(i,0,a.size()) {
        a1.push_back(a[a.size()-i-1]);
        b1.push_back(b[b.size()-i-1]);
    }
    cout << max(a1, b1) << endl;
}