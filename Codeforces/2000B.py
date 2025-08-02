tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    starto = set()
    starto.add(a[0] + 1)
    starto.add(a[0] - 1)
    ans = True
    for i in range(1,n):
        if a[i] in starto:
            starto.add(a[i] + 1)
            starto.add(a[i] - 1)
        else:
            ans = False
            break
    if ans:
        print("YES")
    else:
        print("NO")