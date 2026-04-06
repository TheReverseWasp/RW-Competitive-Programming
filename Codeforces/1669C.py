tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    ans = True
    for i in range(0,n-2, 2):
        if a[i] % 2 == a[i+2] % 2:
            continue
        else:
            ans = False
            break
    for i in range(1,n-2, 2):
        if a[i] % 2 == a[i+2] % 2:
            continue
        else:
            ans = False
            break
    if ans:
        print("YES")
    else:
        print("NO")