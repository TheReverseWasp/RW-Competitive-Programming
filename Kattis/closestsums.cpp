#include <bits/stdc++.h>

using namespace std;

using vi = vector<int>;

int main(int argc, char const *argv[]) {
  while(true) {
    vi nv;
    vi qv;
    int n, m;
    int temp;
    cin >> n;
    for (size_t i = 0; i < n; i++) {
      cin >> temp;
      nv.push_back(temp)
    }
    cin >> m;
    for (size_t i = 0; i < m; i++) {
      cin >> temp;
      mv.push_back(temp);
    }
    sort(v.begin(), v.end());
    vi distances;
    for (size_t i = 0; i < m; i++) {
      int dis1 = 999999999;
      int num1 = 999999999;
      bool init = False, up = False;
      int pos1 = nv.size() / 2 - 1, pos2 = nv.size() / 2;
      while((pos1 != 0 && pos2 != 1) || (pos1 != nv.size() - 2 && pos2 != nv.size() - 1)) {
        int tdist = abs(nv[pos1] + nv[pos2] - mv[i]);
        int tnum = nv[pos1] + nv[pos2];
        if (dis1 > tdist) {
          dis1 = tdist;
          num1 = tnum;
        }
        if(tnum < m[i]) {
          if pos
        }
      }
      if (dist1 == 999999999) {
        if(abs(nv[0] + nv[1] - m[i]) <= abs(nv[nv.size() - 2] + nv[nv.size() - 1] - mv[i]) ) 
      }
    }


  }
  return 0;
}
