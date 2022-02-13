#include <bits/stdc++.h>

using namespace std;

using p = pair<string, string>;
using sc = pair<p, int>;

int main(int argc, char const *argv[]) {
  vector<sc> scores;
  sc s1;
  s1.second = 0;

  s1.first.first = "Adrian";
  s1.first.second = "ABC";
  scores.push_back(s1);

  s1.first.first = "Bruno";
  s1.first.second = "BABC";
  scores.push_back(s1);

  s1.first.first = "Goran";
  s1.first.second = "CCAABB";
  scores.push_back(s1);

  int l;
  string s;
  cin >> l >> s;

  for (size_t i = 0; i < l; i++) {
    for (size_t j = 0; j < scores.size(); j++) {
      int shp = scores[j].first.second.size();
      if (s[i] == scores[j].first.second[i % shp]) {
        scores[j].second++;
      }
    }
  }
  int m = 0;
  for (size_t j = 0; j < scores.size(); j++) {
    if(scores[j].second > m) {
      m = scores[j].second;
    }
  }
  cout << m << endl;
  for (size_t j = 0; j < scores.size(); j++) {
    if(scores[j].second == m) {
      cout << scores[j].first.first << endl;
    }
  }

  return 0;
}
