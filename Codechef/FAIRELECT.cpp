#include <bits/stdc++.h>
#include <queue>
#include <functional>
using namespace std;

typedef long long ll;

int main(){
    int tc;
    cin >> tc;

    while(tc > 0) {
        int jj1, jj2;
        cin >> jj1 >> jj2;
        priority_queue<int, vector<int>, greater<int> > jj1q;
        priority_queue<int, vector<int>, less<int> > jj2q;
        ll t, aj1= 0, aj2=0;
        while(jj1 > 0){
            jj1--;
            cin>>t;
            jj1q.push(t);
            aj1 +=t;
        }
        while(jj2 > 0){
            jj2--;
            cin>>t;
            jj2q.push(t);
            aj2 +=t;
        }
        int answer = 0;
        while(aj1 <= aj2) {
            if(answer > jj1q.size()) {
                answer = -1;
                break;
            }
            int t1 = jj1q.top(), t2 = jj2q.top();
            jj1q.pop();
            jj2q.pop();
            jj1q.push(t2);
            jj2q.push(t1);
            aj1 -= t1 - t2;
            aj2 -= t2 -t1;
            answer ++;
        }
        cout << answer << endl;
        --tc;
    }
}