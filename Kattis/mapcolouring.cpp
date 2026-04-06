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

int best(int at, int excluded, int clique, vector<int> adjacent){
	if (at == sz(adjacent)) return clique;
	int answer = best(at + 1, excluded, clique, adjacent);
	if (!((1 << at)&excluded)) {
		answer = max(answer,
		best(at + 1, excluded | ~adjacent[at], clique + 1, adjacent));
	}
	return answer;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int tc;
  cin>>tc;
  rep(i,0,tc){
  	int nodes, edges;
  	cin>>nodes>>edges;
	vector<int> adjacent(nodes, 0);
  	rep(j,0,edges){
  		int l, r;
  		cin>>l>>r;
  		adjacent[l] |= 1 << r;
  		adjacent[l] |= 1 << l;
  		adjacent[r] |= 1 << l;
  		adjacent[r] |= 1 << r;
  	}
	int answer = best(0,0,0,adjacent);
	if (answer == nodes){
		cout << "many" <<endl;
	}
	else{
		cout << answer << endl;
	}
  }

}
