#include <bits/stdc++.h>
#include <vector>
#include <algorithm>
using namespace std;

typedef vector<int> vi;

int main() {
    int t, temp;
    int c = 1;
    while(cin >> t) {
        vi v;
        while(t > 0) {
            t--;
            int temp;
            cin >> temp;
            v.push_back(temp);
        }
        sort(v.begin(), v.end());
        cout << "Case " << c << ": " << v[0] << " " << v[v.size()-1] << " " << v[v.size() -1] - v[0] <<endl; 
        c++;
    }
}
