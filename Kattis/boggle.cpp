#include <bits/stdc++.h>
#include <cstdio>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
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

vector<string> boggle_board(4);

void setIO(string s) {
    freopen((s + ".txt").c_str(), "r", stdin);
    freopen((s + "_out.txt").c_str(), "w", stdout);
}

struct iAmStronger {
    vector<iAmStronger*> next;
    char actual;
    int height;
    bool tail;
    int sons;
    iAmStronger *dad;

    iAmStronger() : next(26, nullptr), actual(0), height(0), tail(false), dad(nullptr), sons(0) {}
    ~iAmStronger() {next.clear();}
    void insert(const string temp) {
        if (temp.empty()) {
          tail = true;
          return;
        }
        int pos = temp[0] - 'A';
        sons = true;
        if (next[pos] == nullptr) {
            next[pos] = new iAmStronger();
            next[pos]->actual = temp[0];
            next[pos]->height = height + 1;
            next[pos]->dad = this;
            sons++;
        }
        next[pos]->insert(temp.substr(1));
    }
    int find(const string temp) {
        if (temp.empty()) {
            return tail ? height : 0;
        }
        int pos = temp[0] - 'A';
        if (next[pos] == nullptr) return -1;
        return next[pos]->find(temp.substr(1));
    }
    iAmStronger* cuzy_find(string temp) {
      if(temp.size() == 0) return this;
      int pos = temp[0] - 'A';
      if(next[pos] == nullptr) return nullptr;
      return next[pos] -> cuzy_find(temp.substr(1));
    }
    int remove(string to_remove){
      iAmStronger * pos = cuzy_find(to_remove);
      if (pos == nullptr) return 0;
      if(pos->tail == true) {
        pos->tail = false;
      }
      if(pos->sons == 0){
        iAmStronger* pos_dad = pos->dad;
        do{
          char temp = pos->actual;
          delete pos;
          pos_dad->next[temp - 'A'] = nullptr;
          pos_dad->sons--;
          pos = pos_dad;
          pos_dad = pos->dad;
        }while(pos_dad!=nullptr);
      }
      
      return 2;
    }
};

string map_pos(int x, int y){
  return to_string(x) + "-" + to_string(y);
}

bool valid(int x, int y){
  if(x < 0 || x > 3 || y < 0 || y > 3) return false;
  return true;
}

void calculate_xy(string backlog, iAmStronger *my_tree, unordered_set<string> recorrido, int x, int y, set<string>&_1, set<string>&_2, set<string>&_3, set<string>&_4, set<string>&_5, set<string>&_6, set<string>&_7, set<string>&_8){
  if(!valid(x,y)) return;
  if(recorrido.find(map_pos(x,y)) != recorrido.end()) return;
  if(backlog.size() == 8) return;
  backlog += boggle_board[x][y];
  recorrido.insert(map_pos(x,y));
  int search_for = my_tree->find(backlog);
  if(search_for == -1) return;
  else if(search_for > 0){
    my_tree->remove(backlog);
  }
  if(search_for == 1) _1.insert(backlog);
  if(search_for == 2) _2.insert(backlog);
  if(search_for == 3) _3.insert(backlog);
  if(search_for == 4) _4.insert(backlog);
  if(search_for == 5) _5.insert(backlog);
  if(search_for == 6) _6.insert(backlog);
  if(search_for == 7) _7.insert(backlog);
  if(search_for == 8) _8.insert(backlog);
  calculate_xy(backlog, my_tree, recorrido, x + 1, y, _1, _2, _3, _4, _5, _6, _7, _8);
  calculate_xy(backlog, my_tree, recorrido, x + 1, y + 1, _1, _2, _3, _4, _5, _6, _7, _8);
  calculate_xy(backlog, my_tree, recorrido, x + 1, y - 1, _1, _2, _3, _4, _5, _6, _7, _8);
  calculate_xy(backlog, my_tree, recorrido, x - 1, y, _1, _2, _3, _4, _5, _6, _7, _8);
  calculate_xy(backlog, my_tree, recorrido, x - 1, y + 1, _1, _2, _3, _4, _5, _6, _7, _8);
  calculate_xy(backlog, my_tree, recorrido, x - 1, y - 1, _1, _2, _3, _4, _5, _6, _7, _8);
  calculate_xy(backlog, my_tree, recorrido, x, y + 1, _1, _2, _3, _4, _5, _6, _7, _8);
  calculate_xy(backlog, my_tree, recorrido, x, y - 1, _1, _2, _3, _4, _5, _6, _7, _8);
}

void play_boogle(iAmStronger* my_tree){
  unordered_set<string>recorrido;
  set<string> _1;
  set<string> _2;
  set<string> _3;
  set<string> _4;
  set<string> _5;
  set<string> _6;
  set<string> _7;
  set<string> _8;
  rep(x, 0, 4){
    rep(y, 0, 4){
      calculate_xy("", my_tree, recorrido, x, y, _1, _2, _3, _4, _5, _6, _7, _8);
    }
  }
  cout << _1.size() * 0 + _2.size() * 0 + _3.size() + _4.size() + _5.size() * 2 + _6.size() * 3 + _7.size() * 5 + _8.size() * 11 << " ";
  if(_8.size() > 0) cout << *_8.begin() << " ";
  else if(_7.size() > 0) cout << *_7.begin() << " ";
  else if(_6.size() > 0) cout << *_6.begin() << " ";
  else if(_5.size() > 0) cout << *_5.begin() << " ";
  else if(_4.size() > 0) cout << *_4.begin() << " ";
  else if(_3.size() > 0) cout << *_3.begin() << " ";
  else if(_2.size() > 0) cout << *_2.begin() << " ";
  else cout << *_1.begin() << " ";
  cout << _1.size() + _2.size() + _3.size() + _4.size() + _5.size() + _6.size() + _7.size() + _8.size() << endl;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int db_len;
  cin>>db_len;
  iAmStronger* my_tree = new iAmStronger();
  string temp;
  vector<string> words_backlog;
  rep(i,0,db_len){
    cin>>temp;
    my_tree->insert(temp);
    words_backlog.push_back(temp);
  }
  int queries;
  cin>>queries;
  rep(i,0,queries){
    cin>>boggle_board[0]>>boggle_board[1]>>boggle_board[2]>>boggle_board[3];
    play_boogle(my_tree);
    rep(i, 0, words_backlog.size()){
      my_tree->insert(words_backlog[i]);
    }
  }
}