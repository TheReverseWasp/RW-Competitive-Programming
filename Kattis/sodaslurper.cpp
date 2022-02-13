#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[]) {
  int e, f, c;
  cin >> e >> f >> c;
  int acum = e + f, total = 0;
  while (acum >= c) {
    total += acum / c;
    acum = acum % c + acum / c;
  }
  cout << total << endl;
  return 0;
}
