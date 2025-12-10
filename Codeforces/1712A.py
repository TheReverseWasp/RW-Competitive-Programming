tc = int(input())
for _ in range(tc):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = sorted(a)
    pos = b[k-1]
    ans = 0
    for i in range(k):
        if a[i] > pos:
            ans += 1
    print(ans)