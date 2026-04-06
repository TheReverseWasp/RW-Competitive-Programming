tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    min_max = 99999999999999
    for i in range(n-1):
        min_max = min(max(a[i], a[i+1]), min_max)
    min_max -= 1
    print(min_max)