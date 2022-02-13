#include <bits/stdc++.h>

using namespace std;

void generador1(int r, int c) {
    for(int i = 0; i < r; ++i) {
        for(int j = 0; j < c; ++j) {
            if(i == 0 || i == r - 1) {
                if(j == 0 || j == c - 1) {
                    cout << "2 ";
                }
                else {
                    cout << "3 ";
                }
            }
            else {
                if(j == 0 || j == c - 1) {
                    cout << "3 ";
                }
                else {
                    cout << "4 ";
                } 
            }
        }
        cout << "\n";
    }
}

void fun(int r, int c, vector<vector<long> > t) {
    if (t[0][0] >= 3 || t[0][c - 1] >= 3 || t[r - 1][0] >= 3 || t[r - 1][c - 1] >= 3) {
        cout << "NO\n";
        return;
    }
    for(int i = 1; i < c - 1; ++i) {
        if (t[0][i] >= 4 || t[r - 1][i] >= 4){
            cout << "NO\n";
            return;
        }
    }
    for(int i = 1; i < r - 1; ++i) {
        if (t[i][0] >= 4 || t[i][c - 1] >= 4){
            cout << "NO\n";
            return;
        }
    }
    for(int i = 1; i < r - 1; ++i) {
        for(int j = 1; j < c - i; ++j) {
            if(t[i][j] >= 5) {
                cout << "NO\n";
                return;
            }
        }
    }
    cout << "YES\n";
    generador1(r, c);
}

int main() {
    int tc;
    int r, c;
    vector<vector<long> > tempmat;
    vector<long> tempv;
    cin >> tc;
    long tempi;
    for(int i = 0; i < tc; ++i) {
        cin >> r >> c;
        for(int ir = 0; ir < r; ++ir) {
            for(int ic = 0; ic < c; ++ic) {
                cin >> tempi;
                tempv.push_back(tempi);
            }
            tempmat.push_back(tempv);
            tempv.clear();
        }
        fun(r, c, tempmat);
        tempmat.clear();
    }
}