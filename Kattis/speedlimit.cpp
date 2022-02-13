#include <bits/stdc++.h>

using namespace std;

using p = pair<int, int>;

int main(int argc, char const *argv[]) {
  for (size_t i = 0; i < 10; i++) {
    int vSize;
    cin >> vSize;
    if (vSize == -1) break;
    vector<p> v;
    p r;
    r.first = 0;
    r.second = 0;
    v.push_back(r);
    for (size_t j = 0; j < vSize; j++) {
      cin >> r.first >> r.second;
      v.push_back(r);
    }
    int acum = 0;
    for (size_t k = v.size() - 1; k > 0; k--) {
      acum += v[k].first * (v[k].second - v[k - 1].second);
    }
    cout << acum << " miles" << endl;
  }
  return 0;
}
