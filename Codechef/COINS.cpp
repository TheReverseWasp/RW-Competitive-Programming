#include <bits/stdc++.h>
using namespace std;

#define REP(i,a,b) for(long long i=a; i<b; ++i)


map<long long, long long> m;

long long exchange_coin(long long val){
  if(val <= 2) m[val] = val;
  if(m.count(val)) return m[val];
  return m[val] = max(val, exchange_coin(val/2) + exchange_coin(val/3) + exchange_coin(val/4));
}

int main(){
  REP(i,0,3) {m[i] = i;}

  long long a;
  while(cin >> a) {
    cout << exchange_coin(a) << endl;
  }
}
