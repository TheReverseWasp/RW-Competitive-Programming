#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <functional>
using namespace std;



int main(){
    int s;
    vector<long long> v;
    cin >> s;
    while(s > 0) {
        long long t;
        cin >> t;
        v.push_back(t);
        s--;
    }
    sort(v.begin(), v.end(), greater<int>() );
    int it = 0;
    long long acum =0;
    while (it + 3 <= v.size()){
        acum += v[it] + v[it + 1];
        it += 3;
    }
    while (it < v.size()){
        acum += v[it];
        it ++;
    }
    long long acum2 = 0;
    for(int i = 0; i < v.size(); ++i){
        acum2+= v[i];
    }
    cout << acum2 - acum << endl;

}