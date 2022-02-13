#include <bits/stdc++.h>
#include <vector>
using namespace std;

#define rep(i,a,b) for(int i = a; i < (b); ++i)

struct v{
    vector<int> ls;
    void push(int num){
        int s = 0, e = ls.size();
        int h = (s + e) / 2;
        while(s != e) {
            if(ls[h] < num) {
                s = h + 1;
            }
            else {
                e = h;
            }
            h = (s + e) / 2;
        }
        ls.insert(ls.begin() + s, num);
    }
    int pop(){
        int temp = ls.size() / 2;
        int answer = ls[temp];
        ls.erase(ls.begin()+temp);
        return answer;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    priority_queue<int> qmax;

    string str;
    v v1;
    while(!(cin >> str).eof()) {
        if(str[0] != '#') {
            v1.push(stoi(str));           
        }
        else {
            cout << v1.pop() << endl;
        }
    }
}