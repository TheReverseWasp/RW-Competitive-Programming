t = int(input())
while t:
    t-=1
    n = int(input())
    ans = 0
    for i in range(1,n+1,2):
        side = n - i + 1
        ans += side * side
    print(ans)
