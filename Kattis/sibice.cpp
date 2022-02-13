#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[]) {
  int n;
  double w, h;
  cin >> n >> w >> h;
  for (size_t i = 0; i < n; i++) {
    double temp;
    cin >> temp;
    if (temp <= sqrt(w*w + h*h)) {
      cout << "DA" << endl;
    }
    else{
      cout << "NE" << endl;
    }
  }

  return 0;
}
