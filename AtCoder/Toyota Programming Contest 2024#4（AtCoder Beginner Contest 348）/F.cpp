#include <bits/stdc++.h>

using namespace std;

bool find_intersection(vector<int> v1, vector<int>  v2) {
    int acum = 0;
    for(int i = 0; i < v1.size(); i++){
        if (v1[i] == v2[i]) {
            acum += 1;
        }
    }
    return acum % 2 == 1;
}

int main(){
    ios::sync_with_stdio(false);
    int n, m;
    cin>>n>>m;
    vector<vector<int> > v;
    for(int i = 0; i < n; i++) {
        vector<int> current;
        for(int j=0; j<m; j++) {
            int temp;
            cin>>temp;
            current.push_back(temp);
        }
        v.push_back(current);
    }
    long long int ans = 0;
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            if(i != j && find_intersection(v[i], v[j])){
                ans += 1;
            }
        }
    }
    cout << ans << endl;
}