tc=int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = sum([a[i] - a[0] for i in range(n)])
    print(ans)
