#include <bits/stdc++.h>

using namespace std;

#define rep(i,a,b) for(int i=a; i<b; ++i)
#define trav(a, x) for(auto &a: x)

typedef vector<char> vc;
typedef vector<vc> vvc;


set<int> restar_sets(set<int> main_set, set<int> s) {
    set<int> answer;
    trav(item, main_set) {
        if(s.find(item) == s.end()) answer.insert(item);
    }
    return answer;
}

set<int> reverse_set(set<int> s) {
    set<int> answer;
    rep(i,1,10){
        if (s.find(i) == s.end()) answer.insert(i);
    }
    return answer;
}

void find_elems_fila_to_set(vvc v, int row, int col, set<int> &not_possibles) {
    rep(i,0,9){
        if(i != col) {
            if(v[row][i] != '.') not_possibles.insert(v[row][i] - '0');
        }
    }
}

int check_full_state_set(vvc &v, int row, int col, set<int> not_possibles){
    if (not_possibles.size() == 8) {
        rep(j,1,10) {
            if (not_possibles.find(j) == not_possibles.end()) {
                v[row][col] = to_string(j)[0];
                return 1;
            }
        }
    }
    return 0;
}

int check_repetition_state_set(vvc v, int row, int col, char actual, set<int> not_possibles) {
    int actual_int = actual - '0' ;
    if(not_possibles.find(actual_int) != not_possibles.end()) {
        return -1;
    }
    return 0;
}

void find_elems_columna_to_set(vvc v, int row, int col, set<int> &not_possibles) {
    rep(i,0,9){
        if(i != row) {
            if(v[i][col] != '.') not_possibles.insert(v[i][col] - '0');
        }
    }
}

void find_elems_celda_to_set(vvc v, int row, int col, set<int> &not_possibles){
    int rowcel_start = (row/3)*3;
    int colcel_start = (col/3)*3;
    rep(i, rowcel_start, rowcel_start + 3){
        rep(j, colcel_start, colcel_start + 3) {
            if (i != row && j != col) {
                if(v[i][j] != '.') not_possibles.insert(v[i][j] - '0');
            }
        }
    }
}

int test_fila(vvc & v, int i) {
    int row = i / 9;
    int col = i % 9;
    char actual = v[row][col];
    set<int> not_possibles;
    find_elems_fila_to_set(v, row, col, not_possibles);
    if (actual == '.') {
        return check_full_state_set(v, row, col, not_possibles);
    }
    else {
        return check_repetition_state_set(v, row, col, actual, not_possibles);
    }
}

int test_columna(vvc & v, int i) {
    int row = i / 9;
    int col = i % 9;
    char actual = v[row][col];
    set<int> not_possibles;
    find_elems_columna_to_set(v, row, col, not_possibles);
    if (actual == '.') {
        return check_full_state_set(v, row, col, not_possibles);
    }
    else {
        return check_repetition_state_set(v, row, col, actual, not_possibles);
    }
}

int test_celda(vvc &v, int i) {
    int row = i / 9;
    int col = i % 9;
    char actual = v[row][col];
    int rowcel_start = (row/3)*3;
    int colcel_start = (col/3)*3;
    set <int> not_possibles;
    find_elems_celda_to_set(v,row,col,not_possibles);
    if(actual == '.') {
       return check_full_state_set(v, row, col, not_possibles);
    }
    else {
        return check_repetition_state_set(v, row, col, actual, not_possibles);
    }
}

int test_cross(vvc &v, int i) {
    int row = i / 9;
    int col = i % 9;
    char actual = v[row][col];
    int rowcel_start = (row/3)*3;
    int colcel_start = (col/3)*3;
    vector<set<int> > set_vec;
    set<int> complete;
    rep(j,1,10) {
        complete.insert(j);
    }
    vvc vtemp = v;
    vtemp[row][col] = '.';
    rep(j,0,3){
        rep(k,0,3) {
            set<int> temp;
            int tr = rowcel_start + j, tc = colcel_start + k;
            if(actual == '.'){
                if (v[tr][tc] == '.'){
                    find_elems_fila_to_set(v, tr, tc, temp);
                    find_elems_columna_to_set(v, tr, tc, temp);
                    find_elems_celda_to_set(v, tr, tc, temp);
                    set_vec.push_back(temp);
                }
                else {
                    set_vec.push_back(complete);
                }
            }
            else {
                if (vtemp[tr][tc] == '.'){
                    find_elems_fila_to_set(vtemp, tr, tc, temp);
                    find_elems_columna_to_set(vtemp, tr, tc, temp);
                    find_elems_celda_to_set(vtemp, tr, tc, temp);
                    set_vec.push_back(temp);
                }
                else {
                    set_vec.push_back(complete);
                }
            }

            set_vec[set_vec.size() - 1] = reverse_set(set_vec[set_vec.size() - 1]);
        }
    }
    int elem = (row%3)*3 + (col%3);
    set<int> main_set = set_vec[elem];
    rep(j,0,9){
        if(j != elem && set_vec[j].size() > 0){
            main_set = restar_sets(main_set, set_vec[j]);
        }
    }
    if(main_set.size() == 1) {
        trav(a,main_set) { 
            char answer = to_string(a)[0];
            if (actual == '.') {
                v[row][col] = answer;
                return 1;
            }
            else {
                if (answer == actual) return 0;
                else return -1;
            }
        }
    }
    return 0;
}

int test_params(int fila, int columna, int celda) {
    if (fila == -1 || columna == -1 || celda == -1) return -1;
    if(fila == 0 && columna == 0 && celda == 0) return 0;
    return 1;
}

bool rellenar(vvc & v) { //returns true if fails else fills the sudoku matrix
    int fila = 1;
    int columna = 1;
    int celda = 1;
    int cross = 1;
    while(test_params(fila,columna,celda) == 1) {
        rep(i,0,81) {
            fila = test_fila(v, i);
            if(fila == 1 || fila == -1) break;
            columna = test_columna(v, i);
            if(columna == 1 || columna == -1) break;
            celda = test_celda(v,i);
            if(celda == 1 || celda == -1) break;
        }
    }
    bool fail = test_params(fila, columna, celda) == -1;
    if(fail) return fail;
    bool flag = 1;
    while(flag) {
        flag = 0;
        rep(i,0,81) {
            int tc = test_cross(v,i);
            if(tc == 1){
                flag = 1;
            }
            else if (tc == -1) {
                return 1; // fail
            }

        }
    }
    return 0;
}

int main() {
    vvc v;
    string s;
    rep(i,0,9) {
        cin >> s;
        vc temp;
        trav(c,s) temp.push_back(c);
        v.push_back(temp);
    }
    bool fail = rellenar(v);
    if(fail) {
        cout << "ERROR" << endl;
        return 0;
    }
    trav(line, v) {
        trav(ch, line) {
            cout << ch;
        }
        cout << endl;
    }
}
