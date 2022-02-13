#include <bits/stdc++.h>

using namespace std;

void print_game(int a[4][4]) {
  for (size_t i = 0; i < 4; i++) {
    for (size_t j = 0; j < 4; j++) {
      cout  << a[i][j] << " ";
    }
    cout << endl;
  }
}

void up(int a[4][4]) {
  for (size_t c = 0; c < 4; c++) {
    int row = 0;
    for (size_t f1 = 0; f1 < 4; f1++) {
      if (a[f1][c] != 0) {
        for (size_t f2 = f1 + 1; f2 < 4; f2++) {
          if (a[f2][c] != 0) {
            if(a[f1][c] == a[f2][c]) {
              a[row][c] = a[f1][c] * 2;
              a[f2][c] = 0;
            }
            else {
              a[row][c] = a[f1][c];
            }
            row ++;
            break;
          }
        }
      }
    }
  }
  for (size_t c = 0; c < 4; c++) {
    for (size_t f1 = 0; f1 < 4; f1++) {
      if (a[f1][c] == 0) {
        for (size_t f2 = f1 + 1; f2 < 4; f2++) {
          if (a[f2][c] != 0) {
            a[f1][c] = a[f2][c];
            a[f2][c] = 0 ;
          }
        }
      }
    }
  }
  print_game(a);
}


void down(int a[4][4]) {
  for (size_t c = 0; c < 4; c++) {
    int row = 3;
    for (size_t f1 = 3; f1 > 0; f1--) {
      if (a[f1][c] != 0) {
        for (size_t f2 = f1 - 1; f2 > -1; f2--) {
          if (a[f2][c] != 0) {
            if(a[f1][c] == a[f2][c]) {
              a[row][c] = a[f1][c] * 2;
              a[f2][c] = 0;
            }
            else {
              a[row][c] = a[f1][c];
            }
            row --;
            break;
          }
        }
      }
    }
  }
  for (size_t c = 0; c < 4; c++) {
    for (size_t f1 = 3; f1 > -1; f1--) {
      if (a[f1][c] == 0) {
        for (size_t f2 = f1 - 1; f2 > -1; f2) {
          if (a[f2][c] != 0) {
            a[f1][c] = a[f2][c];
            a[f2][c] = 0 ;
          }
        }
      }
    }
  }
  print_game(a);
}

void left(int a[4][4]) {
  for (size_t r = 0; r < 4; r++) {
    int col = 0;
    for (size_t c1 = 0; c1 < 4; c1++) {
      if (a[r][c1] != 0) {
        for (size_t c2 = c1 + 1; c2 < 4; c2++) {
          if (a[r][c2] != 0) {
            if(a[r][c1] == a[r][c2]) {
              a[r][col] = a[r][c1] * 2;
              a[r][c2] = 0;
            }
            else {
              a[r][col] = a[r][c1];
            }
            col++;
            break;
          }
        }
      }
    }
  }
  for (size_t r = 0; r < 4; r++) {
    for (size_t c1 = 0; c1 < 4; c1++) {
      if (a[r][c1] == 0) {
        for (size_t c2 = c1 + 1; c2 < 4; c2++) {
          if (a[r][c2] != 0) {
            a[r][c1] = a[r][c2];
            a[r][c2] = 0 ;
          }
        }
      }
    }
  }
  print_game(a);
}

void right(int a[4][4]) {
  for (size_t r = 0; r < 4; r++) {
    int col = 3;
    for (size_t c1 = 3; c1 < 0; c1--) {
      if (a[r][c1] != 0) {
        for (size_t c2 = c1 - 1; c2 < -1; c2--) {
          if (a[r][c2] != 0) {
            if(a[r][c1] == a[r][c2]) {
              a[r][col] = a[r][c1] * 2;
              a[r][c2] = 0;
            }
            else {
              a[r][col] = a[r][c1];
            }
            col--;
            break;
          }
        }
      }
    }
  }
  for (size_t r = 0; r < 4; r++) {
    for (size_t c1 = 3; c1 > -1; c1--) {
      if (a[r][c1] == 0) {
        for (size_t c2 = c1 - 1; c2 > -1; c2--) {
          if (a[r][c2] != 0) {
            a[r][c1] = a[r][c2];
            a[r][c2] = 0 ;
          }
        }
      }
    }
  }
  print_game(a);
}

int main(int argc, char const *argv[]) {
  int a[4][4];
  for (size_t i = 0; i < 4; i++) {
    for (size_t j = 0; j < 4; j++) {
      cin >> a[i][j];
    }
  }
  int m;
  cin >> m;
  if (m == 0) {
    left(a);
  }
  if (m == 1) {
    up(a);
  }
  if (m == 2) {
    right(a);
  }
  if (m == 3) {
    down(a);
  }
  return 0;
}
