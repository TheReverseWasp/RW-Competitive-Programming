tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(1,n):
        if a[i] % 2 == a[i-1] % 2:
            ans += 1
    print(ans)