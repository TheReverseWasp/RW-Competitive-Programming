tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    min_elem = 9999999
    idx_min = 0
    for i in range(n):
        if a[i] < min_elem:
            idx_min = i + 0
            min_elem = a[i] + 0
    a[idx_min] += 1
    ans = 1
    for i in range(n):
        ans *= a[i]
    print(ans)
