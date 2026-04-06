tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n - 1):
        mini, maxi = min(a[i], a[i + 1]), max(a[i], a[i + 1])
        while maxi/mini > 2:
            mini *= 2
            ans += 1
    print(ans)