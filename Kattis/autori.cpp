#include <iostream>
#include <string>

using namespace std;

int main() {
    string cad;
    cin >> cad;
    bool flag = true;
    string answer;
    for(int i =0;i < cad.size(); ++i) {
        if (flag) {
            answer.push_back(cad[i]);
            flag = false;
        }
        if (cad[i] == '-') {
            flag = true;
        }
    }
    cout << answer << endl;
}