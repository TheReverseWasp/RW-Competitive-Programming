#include <bits/stdc++.h>

using namespace std;

int main() {
    int b;
    cin >> b;
    double t = b;
    double acum = 0;
    while (b) {
        double temp;
        cin >> temp;
        if(temp >= 0) acum+=temp;
        else t-=1;
        --b;
    }
    cout << fixed;
    cout << setprecision(6) ;
    cout << acum / t << endl;
}