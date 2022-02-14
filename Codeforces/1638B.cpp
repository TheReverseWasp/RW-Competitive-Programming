#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=a; i<b; ++i)
typedef long long ll;

int main(){
  int tc;
  cin>>tc;
  while(tc){
    int n;
    cin>>n;
    vector<ll> odds, evens;
    rep(i,0,n) {
      ll temp;
      cin >> temp;
      if(temp%2 == 0){
        evens.push_back(temp);
      }
      else{
        odds.push_back(temp);
      }
    }
    if(is_sorted(evens.begin(),evens.end()) and is_sorted(odds.begin(),odds.end())) {
      cout << "Yes" << endl;
    }
    else {
      cout << "No" << endl;
    }


    tc--;
  }
}
