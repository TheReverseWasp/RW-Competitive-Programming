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

struct Item{
    int pos;
    ll value, weight;
    Item(int pos, ll value, ll weight){
        this->pos = pos;
        this->value = value;
        this->weight = weight;
    }
};

string parse_params(vector<Item> v, int cp){
    string ans = "";
    rep(i,0,v.size()){
        ans += to_string(v[i].pos) + "-" + to_string(v[i].value) + "-" + to_string(v[i].weight) + "-|-";
    }
    ans+="cp:" + to_string(cp);
    return ans;
}

pair<ll, vector<Item> > get_best(vector<Item> v, int cp, unordered_map<string, pair<ll,vector<Item> > > &db){
    pair<ll, vector<Item> > ans;
    ans.first = 0;
    if(cp == 0 || v.size() == 0){
        return ans;
    }
    string parsed_code = parse_params(v,cp);
    if(db.find(parsed_code) != db.end()){
        return db[parsed_code];
    }
    ll new_ans_first = 0;
    vector<Item> new_ans_second;
    rep(i,0,v.size()){
        if(v[i].weight > cp) continue;
        vector<Item> runner;
        rep(j,0,v.size()){
            if(i==j) continue;
            runner.push_back(v[j]);
        }
        pair<ll,vector<Item> > temp(get_best(runner, cp - v[i].weight, db));
        if(new_ans_first < temp.first + v[i].value){
            new_ans_first = temp.first + v[i].value;
            new_ans_second.clear();
            new_ans_second.push_back(v[i]);
            rep(j,0,temp.second.size()){
                new_ans_second.push_back(temp.second[j]);
            }
        }
    }
    pair<ll, vector<Item> > new_ans(new_ans_first, new_ans_second);
    db[parsed_code] = new_ans;
    return new_ans;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int cp, obj;
    unordered_map<string, pair<ll,vector<Item> > > db;
    while(cin>>cp>>obj){
        vector<Item> v;
        ll value, weight;
        rep(i,0,obj){
            cin>>value>>weight;
            Item temp(i,value,weight);
            v.push_back(temp);
        }
        pair<ll, vector<Item> > besto(get_best(v, cp, db));
        cout<<besto.second.size()<<endl;
        rep(i,0,besto.second.size()){
            cout << besto.second[i].pos<<" ";
        }
        cout << endl;
    }
    
}
