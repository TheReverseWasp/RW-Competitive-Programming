tc=int(input())
for _ in range(tc):
    n,m = map(int,input().split())
    ans = 0
    for i in range(m+1):
        ans += i
    for i in range(2,n+1):
        ans += m*i
    print(ans)
