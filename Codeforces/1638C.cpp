#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i = a; i<b; ++i)

void dfs(vector<int> &visited, vector<vector<int> > vertex, int current_pos, int val) {
  if (visited[current_pos] == 0){
    visited[current_pos] = val;
  }
  else{
    return;
  }
  rep(i,0,vertex[current_pos].size()){
    dfs(visited, vertex, vertex[current_pos][i], val);
  }
}

int main() {
  int tc;
  cin>>tc;
  while (tc){
    int n;
    cin>>n;
    vector<int> v(n);
    rep(i,0,n) {
      cin>>v[i];
    }
    vector<int> visited(n,0);
    vector<vector<int> > vertex(n);
    int answer = 1;
    rep(i,0,n){
      rep(j, i+1, n) {
        if(v[i] > v[j]){
          vertex[i].push_back(j);
          vertex[j].push_back(i);
        }
      }
    }

    rep(i,0,n){
      if(visited[i] == 0){
        

        answer ++;
      }
    }
    cout << answer - 1 << endl;
    tc--;
  }
}
