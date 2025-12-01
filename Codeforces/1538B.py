tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    prom = sum(a) // n
    if prom * n != sum(a):
        print(-1)
        continue
    ans = 0
    for elem in a:
        if elem > prom:
            ans+=1
    print(ans)