tc = int(input())
for __ in range(tc):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(k-1):
        ans += a[i] - 1 + a[i]
    print(ans)