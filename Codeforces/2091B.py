t=int(input())
for __ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    a=a[::-1]
    ini, fin = 0, 0
    ans = 0
    while fin < n:
        mini = a[fin]
        power = mini *(fin-ini + 1)
        if power >= k:
            ini = fin + 1
            fin = ini + 0
            ans += 1
        else:
            fin += 1
    print(ans)

