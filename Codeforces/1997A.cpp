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
  cin >> tc;
  rep(i,0,tc){
    string s;
    cin >> s;
    int pos = -1;
    rep(j,0,s.size() - 1){
        if(s[j] == s[j+1]){
            pos = j;
            break;
        }
    }
    string dic = "abcdefghijklmnopqrstuvwxyz";
    if(pos == -1){
        int pos_2 = dic.find(s[s.size()-1]);
        pos_2 ++;
        pos_2%=dic.size();
        s = s + dic[pos_2];
    }
    else{

        int pos_2 = dic.find(s[pos]);
        pos_2 ++;
        pos_2%=dic.size();
        s = s.substr(0,pos + 1) + dic[pos_2] + s.substr(pos+1,s.size()-pos-1);
    }
    cout << s << endl;
  }
}
