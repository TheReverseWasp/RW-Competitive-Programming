#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

int main() {
    int tc;
    cin >> tc;
    int c = 1;
    while(tc) {
        int cc;
        cin >> cc;
        vector<long> v;
        for(int i= 0; i< cc; ++i){
            long t;
            cin >> t;
            v.push_back(t);
        }
        sort(v.begin(), v.end());
        bool acum = true;
        long prev = -1;
        for(int i = 0; i<v.size();++i){
            if(prev == -1) prev = v[i];
            else if (prev != v[i]) {
                cout << "Case #"<< c<<": "<<prev << endl;
                acum = false;
                break;
            }
            else{
                prev = -1;
            }
        }
        if (acum) {
            cout << "Case #"<< c<<": "<<v[v.size()-1] << endl;
        }
        tc--;
        c++;
    }
}