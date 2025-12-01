tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if n == 1 and a[0] > 1:
        print("NO")
    elif n == 1:
        print("YES")
    else:
        diff = abs(a[-1] - a[-2])
        if diff <= 1:
            print("YES")
        else:
            print("NO")