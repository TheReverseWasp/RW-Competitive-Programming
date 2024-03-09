#include <bits/stdc++.h>

using namespace std;

#define rep(i,a,b) for (int i = (a); i < (b); ++i)
#define trav(it, v) for (auto& it : v)
#define all(v) (v).begin(), (v).end()
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> Board;
template <class T> int size(T &x) { return x.size(); }

const vii DIAGONAL = {{-1, 1}, {-1, -1}, {1, -1}, {1, 1}};
const vii CROSS = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
const vii ALL_MOVES = {{-1, 1}, {-1, -1}, {1, -1}, {1, 1},
{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
const vii KNIGHT = {{-1, -2}, {-1, 2}, {1, -2}, {1, 2},
{-2, -1}, {-2, 1}, {2, -1}, {2, 1}};
Board board;


bool isEmpty(int x, int y) {
    return board[x][y] == '.';
}
bool isWhite(int x, int y) {
    return board[x][y] >= 'A' && board[x][y] <= 'Z';
}

bool isValid(int x, int y) {
    return x >= 0 && x < 8 && y >= 0 && y < 8;
}
vii directionMoves(const vii& D, int L, int x, int y) {
    vii moves;
    trav(dir, D) {
        rep(i,1,L+1) {
            int nx = x + dir.first * i, ny = y + dir.second * i;
            if (!isValid(nx, ny)) break;
            if (isEmpty(nx, ny)) moves.emplace_back(nx, ny);
            else {
                if (isWhite(x, y) != isWhite(nx, ny)) moves.emplace_back(nx, ny);
                break;
            }
        }
    }
    return moves;
}

vii pawnMoves(int x, int y) {
    vii moves;
    if (x == 0 || x == 7) {
        vii queenMoves = directionMoves(ALL_MOVES, 16, x, y);
        vii knightMoves = directionMoves(KNIGHT, 1, x, y);
        queenMoves.insert(queenMoves.begin(), all(knightMoves));
        return queenMoves;
    }
    int mv = (isWhite(x, y) ? - 1 : 1);
    if (isValid(x + mv, y) && isEmpty(x + mv, y)) {
        moves.emplace_back(x + mv, y);
        bool canMoveTwice = (isWhite(x, y) ? x == 6 : x == 1);
        if (canMoveTwice && isValid(x + 2 * mv, y) && isEmpty(x + 2 * mv, y)) {
            moves.emplace_back(x + 2 * mv, y);
        }
    }
    auto take = [&](int nx, int ny) {
        if (isValid(nx, ny) && !isEmpty(nx, ny)
        && isWhite(x, y) != isWhite(nx, ny))
            moves.emplace_back(nx, ny);
    };
    take(x + mv, y - 1);
    take(x + mv, y + 1);
    return moves;
}

vii next(int x, int y) {
    vii moves;
    switch(toupper(board[x][y])) {
        case 'Q': return directionMoves(ALL_MOVES, 16, x, y);
        case 'R': return directionMoves(CROSS, 16, x, y);
        case 'B': return directionMoves(DIAGONAL, 16, x, y);
        case 'N': return directionMoves(KNIGHT, 1, x, y);
        case 'K': return directionMoves(ALL_MOVES, 1, x, y);
        case 'P': return pawnMoves(x, y);
    }
    return moves;
}

vector<pair<ii, ii>> getMoves(bool white) {
    vector<pair<ii, ii>> allMoves;
    rep(x,0,8) rep(y,0,8) if (!isEmpty(x, y) && isWhite(x, y) == white) {
        vii moves = next(x, y);
        trav(it, moves) allMoves.emplace_back(ii{x, y}, it);
    }
    return allMoves;
}

Board doMove(pair<ii, ii> mv) {
    Board newBoard = board;
    ii from = mv.first, to = mv.second;
    if ((toupper(newBoard[from.first][from.second]) == 'P') && (from.first == 0 || from.first == 7)) {
        if(to.first == from.first + 1 || to.first == from.first - 1){
            if(to.second == from.second + 2 || to.second == from.second - 2){
                if (isWhite(from.first, from.second)){
                    newBoard[from.first][from.second] = 'N';
                }
                else {
                    newBoard[from.first][from.second] = 'n';
                }
            }
            else{
                if (isWhite(from.first, from.second)){
                    newBoard[from.first][from.second] = 'Q';
                }
                else {
                    newBoard[from.first][from.second] = 'q';
                }
            }
        }
        else if (to.first == from.first + 2 || to.first == from.first - 2){
            if(to.second == from.second + 1 || to.second == from.second - 1){
                if (isWhite(from.first, from.second)){
                    newBoard[from.first][from.second] = 'N';
                }
                else {
                    newBoard[from.first][from.second] = 'n';
                }
            }
            else{
                if (isWhite(from.first, from.second)){
                    newBoard[from.first][from.second] = 'Q';
                }
                else {
                    newBoard[from.first][from.second] = 'q';
                }
            }
        }
        else{
            if (isWhite(from.first, from.second)){
                newBoard[from.first][from.second] = 'Q';
            }
            else {
                newBoard[from.first][from.second] = 'q';
            }
        }
    }

    newBoard[to.first][to.second] = newBoard[from.first][from.second];
    newBoard[from.first][from.second] = '.';
    return newBoard;
}

bool inCheck(bool white) {
    trav(mv, getMoves(!white)) {
        ii to = mv.second;
        if (!isEmpty(to.first, to.second)
            && isWhite(to.first, to.second) == white
            && toupper(board[to.first][to.second]) == 'K') {
            return true;
        }
    }
    return false;
}

bool isMate() {
    if (!inCheck(false)) return false;
    Board oldBoard = board;
    trav(mv, getMoves(false)) {
        board = doMove(mv);
        if (!inCheck(false)) return false;
        board = oldBoard;
    }
    return true;
}

void outputMove(int x, int y) {
    char c = 'a' + y;
    cout << c << 8 - x;
}
int main() {
    string from, to;
    rep(i,0,8) {
        string row;
        cin >> row;
        board.push_back(row);
    }
    Board oldBoard = board;
    trav(mv, getMoves(true)) {
        board = doMove(mv);
        if (!inCheck(true) && isMate()) {
            outputMove(mv.first.first, mv.first.second);
            outputMove(mv.second.first, mv.second.second);
            cout << endl;
            break;
        }
        board = oldBoard;
    }
    return 0;
}