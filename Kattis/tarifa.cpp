#include <bits/stdc++.h>

using namespace std;

int main() {
    int x, n;
    cin >> x >> n;
    int a = 0;
    for(int i = 0; i< n; ++i) {
        int t;
        cin >> t;
        a += x - t;
    }
    a += x;
    cout << a << endl;
}