tc = int(input())
for _ in range(tc):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    flag = True
    for i in range(n):
        if a[i+n] - a[i] < x:
            flag = False
            break

    if flag:
        print("yes")
    else:
        print("no")