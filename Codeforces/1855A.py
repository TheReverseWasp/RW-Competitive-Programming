tc = int(input())
for __ in range(tc):
    n = int(input())
    p = list(map(int,input().split()))
    ans = 0
    for i,elem in zip(range(1,n+1), p):
        if elem == i:
            ans += 1
    print(ans // 2 + (1 if ans % 2 == 1 else 0))