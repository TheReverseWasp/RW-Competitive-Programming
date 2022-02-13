#include <bits/stdc++.h>

using namespace std;

#define ER_CV 1e-6

double bin_search(double t, double D, double val, double piso, double techo) {
  double answer =
  int it = 0;
  while (abs(answer - t) > ER_CV && it < 100) {
    it += 1;
    if(answer > t) {
      techo = val;
      val = (piso + techo) / 2;
    }
    else {
      piso = val;
      val = (piso + techo) / 2;
    }
    answer =
  }
  return val;
}


int main(int argc, char const *argv[]) {
  double D, V;
  cin >> D >> V;
  while(D != 0 && V != 0) {
    double t = V;
    cout << bin_search(t, D, D/2, 0, D) << endl;
    cin >> D >> V;
  }
  return 0;
}
