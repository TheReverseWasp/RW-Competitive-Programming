tc = int(input())
for __ in range(tc):
    n, x = map(int,input().split())
    arr = list(map(int,input().split()))
    max_dist = arr[0] + 0
    for i in range(1, n):
        max_dist = max(max_dist, arr[i] - arr[i - 1])
    max_dist = max(max_dist,(x - arr[n - 1])*2)
    print(max_dist)