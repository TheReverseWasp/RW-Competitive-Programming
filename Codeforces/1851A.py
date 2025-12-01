tc = int(input())
for __ in range(tc):
    n,m,k,H = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for elem in a:
        diff = abs(H-elem)
        if diff % k != 0:
            continue
        if diff // k <= m-1 and diff != 0:
            ans += 1
    print(ans)