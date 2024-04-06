#include <bits/stdc++.h>
using namespace std;
bool compare(pair<long long int, long long int> a, pair<long long int, long long int>  b) {
    if ((a.first - a.second) > (b.first - b.second)){
        return true;
    }
    if((a.first - a.second) == (b.first - b.second) && a.second < b.second){
        return true;
    }
    return false;
}

int main(){
    int n;
    cin >> n;
    vector<pair<long long int, long long int> > v;
    for(int i = 0; i < n; i++) {
        long long int a, b;
        cin >> a >> b;
        v.push_back(make_pair(a,b));
    }
    sort(v.begin(), v.end(), compare);
    long long acum = 0, maxy = -200000000000099;
    for(int i = 0; i < n; i++) {
        acum += v[i].first;
        if(v[i].second > maxy) {
            maxy = v[i].second;
        }
        cout << acum - maxy << endl;
    }
}