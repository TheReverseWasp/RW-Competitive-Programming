#include <bits/stdc++.h>

using namespace std;

using vs = vector<string>;

void printvec(vs v) {
  for (size_t i = 0; i < v.size(); i++) {
    cout << v[i] << endl;
  }
}

int main(int argc, char const *argv[]) {
  int s;
  cin >> s;
  long long c = 1;
  while(s != 0) {
    vs v1;
    string temp;
    for (size_t i = 0; i < s; i++) {
      cin >> temp;
      v1.push_back(temp);
    }
    vs v2(s);
    for (size_t i = 0; i < s / 2; i++) {
      v2[i] = v1[i * 2];
      v2[v2.size() - 1 - i] = v1[i * 2 + 1];
    }
    if(s % 2 == 1){
      v2[s / 2] = v1[v1.size() - 1];
    }
    cout << "SET " << c << endl;
    printvec(v2);
    cin >> s;
    c++;
  }
  return 0;
}
