#include <bits/stdc++.h>

using namespace std;

int main(int argc, char *argv[]) {
    int h, m;
    cin >> h >> m;

    if (m >= 45){
        m -= 45;
    } else{
        if (h == 0) {
            h = 24;
        }
        m += 60;
        h -=1;
        m -= 45;
    }
    cout << h << " " << m << endl;
    return 0;
}