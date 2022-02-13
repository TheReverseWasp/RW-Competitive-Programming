#include <bits/stdc++.h>

using namespace std;

using vc = vector<char>;
using vvc = vector<vc>;

vvc vvc_constructor(vvc a, int zr, int zc) {
  vvc answer;
  for (size_t i = 0; i < a.size(); i++) { //rows
    for (size_t k = 0; k < zr; k++) { // zr
      vc temp;
      for (size_t j = 0; j < a[i].size(); j++) { //cols
        for (size_t l = 0; l < zc; l++) { // z
          temp.push_back(a[i][j]);
        }
      }
      answer.push_back(temp);
    }
  }
  return answer;
}

int main(int argc, char const *argv[]) {
  string temp;
  vvc a;
  int r, c, zr, zc;
  cin >> r >> c >> zr >> zc;
  for (size_t i = 0; i < r; i++) {
    cin >> temp;
    vc tempvc;
    for (size_t j = 0; j < temp.size(); j++) {
      tempvc.push_back(temp[j]);
    }
    a.push_back(tempvc);
  }
  vvc answer(vvc_constructor(a, zr, zc));
  for (size_t i = 0; i < answer.size(); i++) {
    for (size_t j = 0; j < answer[i].size(); j++) {
      cout << answer[i][j];
    }
    cout << endl;
  }

  return 0;
}
