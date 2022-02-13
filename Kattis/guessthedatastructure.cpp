#include <bits/stdc++.h>
#include <queue>
#include <stack>

using namespace std;

#define rep(i, a, b) for(int i = a; i < b; i++)

int main(){
    int tc;
    while(!(cin >> tc).eof()) {
        priority_queue<int> pq;
        queue<int> q;
        stack<int> st;
        bool arr[3];
        arr[0] = arr[1] = arr[2] = true;
        rep(i, 0, tc) {
            int op, val;
            cin >> op >> val;
            if(op==1) {
                if(arr[0] == true) pq.push(val);
                if(arr[1] == true) q.push(val);
                if(arr[2] == true) st.push(val);
            }
            else {
                if(arr[0]== true) {
                    if(pq.size() != 0 && pq.top() == val) pq.pop();
                    else {
                        arr[0] = false;
                    }
                }
                if(arr[1] == true) {
                    if(q.size() != 0 && q.front() == val) q.pop();
                    else{
                        arr[1] = false;
                    }
                }
                if (arr[2]==true) {
                    if(st.size()!= 0 && st.top() == val) st.pop();
                    else {
                        arr[2] = false;
                    }
                }
            }
        }
        int ac = 0;
        rep(i,0, 3) {
            if (arr[i] == true) ac++;
        }
        if (ac > 1) {
            cout << "not sure" << endl;
        }
        else if (ac == 0) {
            cout << "impossible" << endl;
        }
        else {
            if(arr[0]) cout << "priority queue" << endl;
            else if(arr[1]) cout << "queue" << endl;
            else  cout << "stack" << endl;
        }
    }
}