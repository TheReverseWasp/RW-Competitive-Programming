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
#include <unordered_map>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define ll long long int
#define mp make_pair
#define f first
#define s second
#define pb push_back

void setIO(string s) {
    freopen((s + ".txt").c_str(), "r", stdin);
    freopen((s + "_out.txt").c_str(), "w", stdout);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector <string> v;
    int people;
    cin >> people;
    rep(i,0,people){
        string temp;
        cin >> temp;
        v.push_back(temp);
    }
    int operations;
    cin >> operations;
    rep(i,0,operations){
        string op_type;
        cin >> op_type;
        if (op_type == "cut") {
            string before, after;
            cin >> before >> after;
            int elem_pos;
            rep(j, 0, v.size()){
                if(v[j] == after){
                    elem_pos = j;
                    break;
                }
            }
            v.insert(v.begin()+elem_pos, before);
        }
        else{
            string to_delete;
            cin >> to_delete;
            int elem_pos;
            rep(j, 0, v.size()){
                if(v[j] == to_delete){
                    elem_pos = j;
                    break;
                }
            }
            v.erase(v.begin()+elem_pos);
        }
    }
    rep(i,0,v.size()){
        cout << v[i] << endl;
    }
}
