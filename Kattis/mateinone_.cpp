#include <bits/stdc++.h>

using namespace std;

#define rep(i,a,b) for (int i = (a); i < (b); ++i)
#define trav(it, v) for (auto& it : v)
#define all(v) (v).begin(), (v).end()
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef pair<ii, ii> iiii;
typedef vector<iiii> viiii;

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
viiii directionMoves(const vii& D, int L, int x, int y) {
    viiii moves;
    trav(dir, D) {
        rep(i,1,L+1) {
            int nx = x + dir.first * i, ny = y + dir.second * i;
            if (!isValid(nx, ny)) break;
            if (isEmpty(nx, ny)) moves.emplace_back(ii{nx, ny}, ii{-1, -1});
            else {
                if (isWhite(x, y) != isWhite(nx, ny)) moves.emplace_back(ii{nx, ny}, ii{-1, -1});
                break;
            }
        }
    }
    return moves;
}

viiii pawnMoves(int x, int y,  iiii last_move) {
    viiii moves;
    if (x == 0 || x == 7) {
        viiii queenMoves = directionMoves(ALL_MOVES, 16, x, y);
        viiii knightMoves = directionMoves(KNIGHT, 1, x, y);
        queenMoves.insert(queenMoves.begin(), all(knightMoves));
        return queenMoves;
    }
    int mv = (isWhite(x, y) ? - 1 : 1);
    if (isValid(x + mv, y) && isEmpty(x + mv, y)) {
        moves.emplace_back(ii(x + mv, y), ii(-1,-1));
        bool canMoveTwice = (isWhite(x, y) ? x == 6 : x == 1);
        if (canMoveTwice && isValid(x + 2 * mv, y) && isEmpty(x + 2 * mv, y)) {
            moves.emplace_back(ii(x + 2 * mv, y), ii(-1,-1));
        }
    }
    auto take = [&](int nx, int ny) {
        if (isValid(nx, ny) && !isEmpty(nx, ny)
        && isWhite(x, y) != isWhite(nx, ny))
            moves.emplace_back(ii(nx, ny), ii(-1,-1));
    };

    take(x + mv, y - 1);
    take(x + mv, y + 1);

    ii from = last_move.first, to = last_move.second;
    if (from.first != -1 && x == to.first && abs(from.first - to.first) == 2 && abs(y - to.second) == 1 && toupper(board[to.first][to.second]) == 'P'){
        bool myColor = isWhite(x,y);
        bool myRivalsColor = isWhite(to.first,to.second);
        int myValidX = (myColor ? 3: 4);
        if(myColor != myRivalsColor && myValidX == x){
            int adder =  (myColor ? -1: 1);
            iiii move = iiii{ii{x + adder, to.second}, to};
            moves.emplace_back(move);
        }
    }
    return moves;
}

viiii next(int x, int y, pair<ii, ii> last_move) {
    viiii moves;
    switch(toupper(board[x][y])) {
        case 'Q': return directionMoves(ALL_MOVES, 16, x, y);
        case 'R': return directionMoves(CROSS, 16, x, y);
        case 'B': return directionMoves(DIAGONAL, 16, x, y);
        case 'N': return directionMoves(KNIGHT, 1, x, y);
        case 'K': return directionMoves(ALL_MOVES, 1, x, y);
        case 'P': return pawnMoves(x, y, last_move);
    }
    return moves;
}

vector<pair<iiii, ii>> getMoves(bool white, iiii last_move) {
    vector<pair<iiii, ii>> allMoves;
    rep(x,0,8) rep(y,0,8) if (!isEmpty(x, y) && isWhite(x, y) == white) {
        viiii moves = next(x, y, last_move);
        trav(it, moves) allMoves.emplace_back(iiii{ii{x, y}, it.first}, it.second);
    }
    return allMoves;
}

Board doMove(iiii mv, ii colateral) {
    Board newBoard = board;
    ii from = mv.first, to = mv.second;
    newBoard[to.first][to.second] = newBoard[from.first][from.second];
    newBoard[from.first][from.second] = '.';
    if(colateral.first != -1) {
        newBoard[colateral.first][colateral.second] = '.';
    }
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

    
    return newBoard;
}

bool inCheck(bool white) {
    trav(mv, getMoves(!white, iiii{ii{-1,-1}, ii{-1,-1}})) {
        ii to = mv.first.second;
        if (!isEmpty(to.first, to.second)
            && isWhite(to.first, to.second) == white
            && toupper(board[to.first][to.second]) == 'K') {
            return true;
        }
    }
    return false;
}

bool isMate(iiii last_move) {
    if (!inCheck(false)) return false;
    Board oldBoard = board;
    trav(mv, getMoves(false, last_move)) {
        board = doMove(mv.first, mv.second);
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
    trav(mv, getMoves(true, iiii{ii{-1,-1}, ii{-1,-1}})) {
        board = doMove(mv.first, mv.second);
        if (!inCheck(true) && isMate(mv.first)) {
            iiii ans = mv.first;
            outputMove(ans.first.first, ans.first.second);
            outputMove(ans.second.first, ans.second.second);
            cout << endl;
            break;
        }
        board = oldBoard;
    }
    return 0;
}