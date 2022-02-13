#include <bits/stdc++.h>
#include <math.h>
using namespace std;

int main(){
    int tc;
    cin >> tc;
    string cad;
    long long acum = 0;
    while(tc) {
        cin >> cad;
        acum += pow(stol(cad.substr(0, cad.size()-1)), stol(cad.substr(cad.size()-1, 1)));
        tc--;
    }
    cout << acum<<endl;
}