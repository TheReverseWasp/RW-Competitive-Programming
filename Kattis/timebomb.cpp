#include <bits/stdc++.h>

using namespace std;

int decode_number(string l1, string l2, string l3, string l4, string l5) {
    if (l1 == "***" && l2 == "* *" && l3 == "* *" && l4 == "* *" && l5 == "***") {//check
        return 0;
    }
    else if (l1 == "  *" && l2 == "  *" && l3 == "  *" && l4 == "  *" && l5 == "  *") {//check
        return 1;
    }
    else if (l1 == "***" && l2 == "  *" && l3 == "***" && l4 == "*  " && l5 == "***") {//check
        return 2;
    }
    else if (l1 == "***" && l2 == "  *" && l3 == "***" && l4 == "  *" && l5 == "***") {//check
        return 3;
    }
    else if (l1 == "* *" && l2 == "* *" && l3 == "***" && l4 == "  *" && l5 == "  *") {//check
        return 4;
    }
    else if (l1 == "***" && l2 == "*  " && l3 == "***" && l4 == "  *" && l5 == "***") {//check
        return 5;
    }
    else if (l1 == "***" && l2 == "*  " && l3 == "***" && l4 == "* *" && l5 == "***") {//check
        return 6;
    }
    else if (l1 == "***" && l2 == "  *" && l3 == "  *" && l4 == "  *" && l5 == "  *") {//check
        return 7;
    }
    else if (l1 == "***" && l2 == "* *" && l3 == "***" && l4 == "* *" && l5 == "***") {
        return 8;
    }
    else if (l1 == "***" && l2 == "* *" && l3 == "***" && l4 == "  *" && l5 == "***") {
        return 9;
    }
    else{
        return -1;
    }
}
int main(int argc, char *argv[]) {
    string l1_macro, l2_macro, l3_macro, l4_macro, l5_macro;
    string l1, l2, l3, l4, l5;
    getline(cin, l1_macro);
    getline(cin, l2_macro);
    getline(cin, l3_macro);
    getline(cin, l4_macro);
    getline(cin, l5_macro);
    long long to_test = 0LL; 
    for(int i = 0; i < l1_macro.size(); i+=4){
        l1 = l1_macro.substr(i, 3);
        l2 = l2_macro.substr(i, 3);
        l3 = l3_macro.substr(i, 3);
        l4 = l4_macro.substr(i, 3);
        l5 = l5_macro.substr(i, 3);
        int decoded = decode_number(l1, l2, l3, l4, l5);
        if (decoded < 0){
            cout << "BOOM!!" <<endl;
            return 0;
        }
        to_test *= 10;
        to_test += decoded;
    }
    if (to_test % 6 == 0) {
        cout << "BEER!!" << endl;
    }
    else {
        cout << "BOOM!!" << endl;
    }
    return 0;
}