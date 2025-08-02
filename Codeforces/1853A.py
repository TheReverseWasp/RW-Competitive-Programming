tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int, input().split()))
    diff = list()
    for i in range(1,n):
        diff.append(a[i]-a[i-1])
    min_diff = min(diff)
    if min_diff < 0:
        print(0)
    else:
        print(min_diff // 2 + 1)