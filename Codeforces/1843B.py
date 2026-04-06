tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    i = 0
    ops = 0
    while i < n:
        if a[i] >= 0:
            i+=1
            continue
        else:
            while i < n and a[i] <= 0:
                a[i] *=-1
                i += 1
            ops += 1
    print(sum(a), ops)