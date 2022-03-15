t = int(input())
while t:
    t-=1
    n, bp = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1,-1,-1):
        if bp > a[i]:
            ans = i + 1
            break
    print(ans)
