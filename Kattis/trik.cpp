#include <bits/stdc++.h>

using namespace std;

int main() {
    string cad;
    cin >> cad;
    int pos = 1;
    for(int i = 0; i < cad.size(); i++){
        switch(cad[i]){

            case 'A':
                if (pos == 1) pos = 2;
                else if (pos == 2) pos = 1;
                break;
            case 'B':
                if (pos == 2) pos = 3;
                else if (pos == 3) pos = 2;
                break;
            case 'C':
                if (pos == 1) pos = 3;
                else if (pos == 3) pos = 1;
                break;
            default:
                break;
        }
    }
    cout << pos << endl;
}