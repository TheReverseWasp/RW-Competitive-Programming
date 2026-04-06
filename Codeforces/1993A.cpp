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
#define ll long long
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
  int tc;
  cin>>tc;
  rep(i,0,tc){
    int n;
    string s;
    cin >>n >>s;
    map<char,int> db;
    db['A'] = 0;
    db['B'] = 0;
    db['C'] = 0;
    db['D'] = 0;
    trav(letter,s){
        if(letter == '?'){
            continue;
        }
        db[letter] = min(db[letter] + 1,n);
    }
    cout << db['A'] + db['B'] + db['C'] + db['D'] << endl;
  }
}
