tc = int(input())
for _ in range(tc):
    n,m = map(int,input().split())
    perimeter = m*4
    ans = perimeter + 0
    for i in range(n):
        x, y = map(int,input().split())
        if i != 0:
            ans += perimeter - ((m-x) + (m-y))*2
    print(ans)