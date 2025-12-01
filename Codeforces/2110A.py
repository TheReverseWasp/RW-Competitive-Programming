tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(n):
        a[i] = a[i] % 2
    ans = n + 0
    for i in range(n):
        ini = i
        for j in range(n):
            fin = n - j - 1
            if fin < ini:
                break
            cost = ini + j
            if cost < ans:
                pass
            else:
                break
            if a[ini] == a[fin]:
                ans = min(cost,ans)
    print(ans)
