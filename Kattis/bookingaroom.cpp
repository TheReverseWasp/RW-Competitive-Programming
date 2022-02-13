#include <bits/stdc++.h>

using namespace std;

int main() {
    int r, n;
    map <int, bool> m;
    cin >> r >> n;
    for(int i = 0; i < n; i++) {
        int t;
        cin >> t;
        m[t]= true;
    }
    for(int i = 1; i<r; i++) {
        if(m.contains(i) == false) {
            cout << i << endl;
            return 1;
        }
    }
    cout << "too late" << endl;
}