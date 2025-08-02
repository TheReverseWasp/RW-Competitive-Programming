tc = int(input())
for __ in range(tc):
    n,d = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    minion = a[0] + a[1]
    flag = True
    for elem in a:
        if elem > d and minion > d:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")