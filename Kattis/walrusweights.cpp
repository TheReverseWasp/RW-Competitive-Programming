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

void setIO(string s) {
	  freopen((s + ".txt").c_str(), "r", stdin);
	  freopen((s + "_out.txt").c_str(), "w", stdout);
}

string parse_plates(vector<int> plates_l)
{
    string ans = "";
    rep(i,0,plates_l.size()){
        ans += to_string(plates_l[i]) + "-";
    }
    return ans;
}
struct classcomp{
    bool operator()(int a, int b) const{
        int new_a = abs(1000 - a);
        int new_b = abs(1000 - b);
        if(new_a == new_b){
            return a > b;
        }
        return new_a < new_b;
    }
};

unordered_map<string, int> db;

int get_weight(vector<int> plates_l){
    if(plates_l.size() == 0){
        return 0;
    }
    string parsed = parse_plates(plates_l);
    if(db.find(parsed) != db.end()){
        return db[parsed];
    }
    int actual = 0;
    int weight = 0;
    int ans = 0;
    rep(i,0,plates_l.size()){
        weight = plates_l[i];
        vector<int> new_plates_l;
        rep(j,0,plates_l.size()){
            if(i == j) continue;
            new_plates_l.push_back(plates_l[j]);
        }
        int temp = get_weight(new_plates_l);
        set<int, classcomp> runner_list;
        runner_list.insert(weight + temp);
        runner_list.insert(weight);
        runner_list.insert(temp);
        runner_list.insert(actual);        
        actual = *runner_list.begin();
    }
    db[parsed] = actual;
    return actual;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int plates;
    cin >> plates;
    vector<int>plates_l(plates);
    rep(i,0,plates){
        cin>>plates_l[i];
    }
    sort(plates_l.begin(), plates_l.end());
    cout << get_weight(plates_l) << endl;
}
