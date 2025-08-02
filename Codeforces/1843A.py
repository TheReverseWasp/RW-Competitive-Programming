tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ini = 0 
    fin = n - 1
    ans = 0
    while ini < fin:
        ans += abs(a[ini] - a[fin])
        ini += 1
        fin -= 1
    print(ans)