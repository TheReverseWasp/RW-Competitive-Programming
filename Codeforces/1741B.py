from copy import copy as cp

tc=int(input())
for _ in range(tc):
    n = int(input())
    if n == 3:
        print(-1)
        continue
    ans = [i for i in range(1,n+1)]
    ans = ans[::-1]
    temp = cp(ans[2:])
    for i in range(2, n):
        less_pos = i - 2
        ans[i] = temp[-1-less_pos]
    for elem in ans:
        print(elem, end=" " )
