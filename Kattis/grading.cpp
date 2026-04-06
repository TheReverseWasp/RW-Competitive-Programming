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
    int a,b,c,d,e;
    cin >> a >> b >> c >> d >> e;
    int score;
    cin >> score;
    if (score >= a){
        cout << "A" << endl;
    }
    else if (score >= b){
        cout << "B" << endl;
    }
    else if (score >= c) {
        cout << "C" << endl;
    }
    else if (score >= d) {
        cout << "D" << endl;
    }
    else if (score >= e) {
        cout << "E" << endl;
    }
    else {
        cout << "F" << endl;
    }
}
