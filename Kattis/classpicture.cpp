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

void setIO(string s) {
    freopen((s + ".txt").c_str(), "r", stdin);
    freopen((s + "_out.txt").c_str(), "w", stdout);
}

string parser(vector<int> order, vector<string> names){
    string answer = "";
    rep(i,0,order.size()){
        answer+=names[order[i]] + " ";
    }
    return answer;
}

string dfs(int at, vector<int> chain, int excluded, vector<int>hate, vector<string>names){
    chain.push_back(at);
    if(chain.size() > 1){
        if(1<<at & hate[chain[chain.size()-2]]){
            return "";
        }
    }
    excluded |= 1<<at;
    if(chain.size() == hate.size()){
        return parser(chain, names);
    }
    string answer = "";
    int prev_found;
    rep(i,0,hate.size()){
        if(!(1<<i & excluded)){
            if(answer.size() == 0){
                prev_found = i;
                answer = dfs(i, chain, excluded, hate, names);
            }
            else{
                if(i < prev_found){
                    string temp = dfs(i, chain, excluded, hate, names);
                    if(temp.size() != 0){
                        answer = temp;
                        prev_found = i;
                    }
                }
            }
        }
    }
    return answer;
}

string bt(vector<int>hate, vector<string> names){
    int prev_word;
    string answer = "";
    vector<int> chain;
    rep(i,0,names.size()){
        if(answer.size()==0){
            answer = dfs(i,chain,0,hate,names);
            prev_word = i;
        }
        else{
            if (i < prev_word){
                string temp = dfs(i,chain,0,hate,names);
                if(temp.size()!=0){
                    answer = temp;
                    prev_word = i;
                }
            }
        }
    }
    return answer;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int cm;
  while(cin>>cm){
    vector<string>names (cm);
    map<string, int> names_map;
    rep(i,0,cm){
        cin>>names[i];
    }
    sort(names.begin(), names.end());
    rep(i,0,names.size()){
        names_map[names[i]] = i;
    }
    int hate_rel;
    cin>>hate_rel;
    vector<int> hate(cm);
    string temp1, temp2;
    rep(i,0,hate_rel){
        cin>>temp1>>temp2;
        hate[names_map[temp1]] |= 1 << names_map[temp2];
        hate[names_map[temp1]] |= 1 << names_map[temp1];
        hate[names_map[temp2]] |= 1 << names_map[temp2];
        hate[names_map[temp2]] |= 1 << names_map[temp1];
    }
    int temp = 0;
    rep(i,0,names.size()){
        temp |= 1<<i;
    }
    bool flag = true;
    rep(i,0,hate.size()){
        if (hate[i] == temp){
            flag = false;
            break;
        }
    }
    if (flag){
        string answer = bt(hate, names);
        if(answer.size() == 0){
            cout<<"You all need therapy."<<endl;
        }
        else{
            cout<<answer<<endl;
        }
    }
    else{
        cout<<"You all need therapy."<<endl;
    }
  }
}