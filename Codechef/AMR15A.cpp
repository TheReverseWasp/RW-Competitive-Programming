#include <bits/stdc++.h>

using namespace std;

int main() {
  int n;
  cin >> n;
  int odd=0, even=0;
  int temp;
  while (n) {
    cin >> temp;
    if (temp%2 == 0) {
      even++;
    }
    else{
      odd++;
    }
    n--;
  }
  if (even > odd) {
    cout << "READY FOR BATTLE" << endl;
  }
  else {
    cout << "NOT READY" << endl;
  }
}
