tc = int(input())
for __ in range(tc):
    n,k=map(int,input().split())
    a = list(map(int,input().split()))
    ini, fin = 0, 0
    ans = 0
    while fin < n:
        dist = fin+1 - ini
        if a[fin] == 0:
            if dist == k:
                ini = fin + 2
                fin = ini + 0
                ans += 1
            else:
                fin += 1
        else:
            ini = fin + 1
            fin = ini + 0
    print(ans)