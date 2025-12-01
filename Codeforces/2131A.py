tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    dist = 0
    for i in range(n):
        if a[i] > b[i]:
            dist += a[i] - b[i]
    dist += 1

    print(dist)