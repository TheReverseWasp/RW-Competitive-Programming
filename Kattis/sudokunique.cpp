#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <bitset>
#include <numeric>
#include <sstream>
#include <utility>
#include <cassert>
#include <unordered_set>

using namespace std;

#define rep(i, a, b) for(int i = a; i < b; ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define ll long long
#define mp make_pair
#define f first
#define s second
#define pb push_back

void setIO(string s) {
	freopen((s + ".txt").c_str(), "r", stdin);
	freopen((s + "_out.txt").c_str(), "w", stdout);
}

pair<int, int> get_block(int i, int j) {
    pair<int, int> answer;
    answer.first = (i / 3) * 3;
    answer.second = (j / 3) * 3;
    return answer;
}

unordered_set<int> find_possible(vector<vector<int> > sudoku_to_fill, int row, int col) {
    unordered_set<int> result;
    rep(i,1,10){
        result.insert(i);
    }
    // check row
    rep(i, 0, 9){
        if(i == col){
            continue;
        }
        result.erase(sudoku_to_fill[row][i]);
    }
    // check column
    rep(i, 0, 9){
        if(i == row){
            continue;
        }
        result.erase(sudoku_to_fill[i][col]);
    }
    // check block
    pair<int, int> block_start(get_block(row, col));
    rep(i,block_start.first,block_start.first + 3){
        rep(j,block_start.second, block_start.second + 3){
            if(i == row && j == col){
                continue;
            }
            result.erase(sudoku_to_fill[i][j]);
        }
    }
    return result;
}

bool is_valid(vector<vector<int> > sudoku_to_fill){
    rep(i,0,9){
        rep(j,0,9){
            if(sudoku_to_fill[i][j] != 0){
                unordered_set<int> possible(find_possible(sudoku_to_fill, i, j));
                if(possible.find(sudoku_to_fill[i][j]) != possible.end()){
                    continue;
                }
                else{
                    return false;
                }
            }
        }
    }
    return true;
}

bool is_full(vector<vector<int> > sudoku_to_fill){
    rep(i,0,9){
        rep(j,0,9){
            if(sudoku_to_fill[i][j] == 0){
                return false;
            }
        }
    }
    return true;
}

string parse_sudoku(vector<vector<int> > sudoku_to_fill){
    string answer = "";
    rep(i,0,9){
        rep(j,0,9){
            answer+=to_string(sudoku_to_fill[i][j]) + " ";
        }
        answer += "\n";
    }
    return answer;
}

string get_answer(vector<vector<int> > sudoku_to_fill){
    if(!is_valid(sudoku_to_fill)){
        return "Find another job\n";
    }
    bool past;
    do{
        past=false;
        rep(i,0,9){
            rep(j,0,9){
                if(sudoku_to_fill[i][j] == 0){
                    unordered_set<int> possible(find_possible(sudoku_to_fill,i,j));
                    if(possible.size() == 1){
                        sudoku_to_fill[i][j] = *possible.begin();
                        past = true;
                    }
                }
            }
        }
    }while(past);
    if(!is_full(sudoku_to_fill)){
        return "Non-unique\n";
    }
    return parse_sudoku(sudoku_to_fill);
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  vector<int> v(9, 0);
  vector<vector<int> > sudoku_to_fill (9, v);
  int temp;
  int row = 0, col = 0;
  string answer = "";
  while(cin>>temp){
    sudoku_to_fill[row][col] = temp;
    col ++;
    if(col == 9){
        col = 0;
        row ++;
    }
    if (row == 9){
        row = 0;
        answer += get_answer(sudoku_to_fill) + "\n";
    }
  }
  cout<<answer.substr(0,answer.size() - 2);
}
