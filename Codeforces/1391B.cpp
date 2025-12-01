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


pair<bool,vector<pii> > llega_meta(vector<string>mapa){
    int r = mapa.size();
    int c = mapa[0].size();
    int ini_r = 0;
    int ini_c = 0;
    vector<pii> recorrido;
    while(ini_r <r and ini_c < c){
        if(mapa[ini_r][ini_c] == 'C'){
            return mp(true,recorrido);
        }
        pii temp;
        temp.f = ini_r;
        temp.s = ini_c;
        recorrido.push_back(temp);
        if(mapa[ini_r][ini_c] == 'R'){
            ini_c++;
        }
        else{
            ini_r++;
        }
    }
    return mp(false,recorrido);
}

bool is_in_swaped(pii to_search, vector<pii>swaped){
    trav(elem, swaped){
        if(elem.f == to_search.f and elem.s == to_search.s){
            return true;
        }
    }
    return false;
}

string swaper(string row, int c){
    string new_r = row.substr(0,c);
    if(row[c] == 'R'){
        new_r += "D";
    }
    else{
        new_r += "R";
    }
    if(c+1 == row.size()){
        return new_r;
    }
    new_r += row.substr(c + 1, row.size() - c);
    return new_r;
}

int find_minimum(vector<string>mapa, vector<pii>swaped, int allowed_inheritance){
    pair<bool, vector<pii> > llego_recorrido = llega_meta(mapa);
    if(llego_recorrido.f){
        return 0;
    }
    if(allowed_inheritance < 0){
        return 999999;
    }
    trav(to_search, llego_recorrido.s){
        if(!is_in_swaped(to_search, swaped)){
            swaped.push_back(to_search);
            mapa[to_search.f] = swaper(mapa[to_search.f], to_search.s);
            int temp = 1 + find_minimum(mapa,swaped, allowed_inheritance - 1);
            if(temp < allowed_inheritance){
                allowed_inheritance = temp;
            }
            mapa[to_search.f] = swaper(mapa[to_search.f], to_search.s);
            swaped.pop_back();
        }
    }
    return allowed_inheritance;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int tc;
    cin >> tc;
    rep(__,0,tc){
        int r,c;
        cin >> r >> c;
        vector<string> mapa;
        rep(i,0,r){
            string temp;
            cin >> temp;
            mapa.push_back(temp);
        }
        vector<pii> swaped;
        cout << find_minimum(mapa,swaped, 999999) << endl;;
    }
}
