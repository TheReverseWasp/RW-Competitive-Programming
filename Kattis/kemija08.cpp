#include <bits/stdc++.h>

using namespace std;

string decoder(string s) {
  string abc = "aeiou";
  string answer = "";
  for (size_t i = 0; i < s.size(); i++) {
    answer += s[i];
    if(abc.find(s[i]) != string::npos) {
      i += 2;
    }
  }
  return answer;
}

int main(int argc, char const *argv[]) {
  string s1;
  getline(cin, s1);
  cout << decoder(s1) << endl;

  return 0;
}
