#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[]) {
  int n;
  cin >> n;
  int p = 1;
  int d = 1;
  while (p < n) {
    p *= 2;
    d++;
  }
  cout << d << endl;
  return 0;
}
