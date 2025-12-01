tc = int(input())
for __ in range(tc):
    n = int(input())
    ans = 0
    for i in range(n):
        a,b = map(int,input().split())
        if a - b > 0:
            ans += 1
    print(ans)