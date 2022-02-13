#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

typedef long long ll;

int main() {
    ll a, b;
    while(cin >> a >> b) {
        cout << max(a,b) - min(a,b) << endl;
    }
}