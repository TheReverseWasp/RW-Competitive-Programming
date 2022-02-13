#include <bits/stdc++.h>

using namespace std;

#define rep(i,a,b) for(int i = a; i<b; ++i)
#define trav(it, v) for(auto& it: v)
#define all(v) v.begin(), v.end()
#define assign(t,a,b) t.first = a, t.second= b;

typedef pair<int, int> ii;

struct nextmove {
    char piece;
    ii s, f;
    nextmove(char piece, ii s, ii f) {
        this.piece = piece;
        this.s = s;
        this.f = f;
    }
};

typedef vector<nextmove> vii;

vector<string> board(8);


int rook[4][2] = {
    {1,0},
    {-1,0},
    {0,1},
    {0,-1}
}

bool is_empty(int x, int y) {
    return board[x][y] == '.';
}

bool is_white(int x, int y) {
    return board[x][y] >= 'A' && board[x][y] <='Z';
}

bool is_valid(int x, int y) {
    return x >= 0 && x < 8 && y>=0 && y<8;
}

vii next(int x, int y) {
    vii res;
    ii t;
    
}

int main() {
    string l;
    rep(i,0,8) {
        cin >> l;
        rep(j,0,8) {
            board[j].push_back(l[7 - j]);
        }
    }

}